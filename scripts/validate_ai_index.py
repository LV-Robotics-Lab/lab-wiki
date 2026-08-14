#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlparse


SITE_URL = "https://lv-robotics-lab.github.io/lab-wiki/"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


def validate_index(payload: object, docs_root: Path | None = None) -> list[str]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return ["index root must be an object"]
    if payload.get("schema_version") != 1:
        errors.append("schema_version must equal 1")
    if payload.get("site_url") != SITE_URL:
        errors.append(f"site_url must equal {SITE_URL}")
    if payload.get("default_language") != "zh":
        errors.append("default_language must equal zh")
    if not TIMESTAMP_RE.fullmatch(str(payload.get("generated_at", ""))):
        errors.append("generated_at must use YYYY-MM-DDTHH:MM:SSZ")
    maintainers = payload.get("maintainers")
    pages = payload.get("pages")
    if not isinstance(maintainers, list) or not isinstance(pages, list):
        return errors + ["maintainers and pages must be arrays"]

    maintainer_ids: set[str] = set()
    for maintainer in maintainers:
        if not isinstance(maintainer, dict):
            errors.append("every maintainer must be an object")
            continue
        maintainer_id = maintainer.get("id")
        if not isinstance(maintainer_id, str) or not maintainer_id:
            errors.append("every maintainer must have a non-empty id")
            continue
        if maintainer_id in maintainer_ids:
            errors.append(f"duplicate maintainer id: {maintainer_id}")
        maintainer_ids.add(maintainer_id)
        for field in ("name_zh", "name_en"):
            if not isinstance(maintainer.get(field), str) or not maintainer[field]:
                errors.append(f"{maintainer_id} {field} must be a non-empty string")
        contacts = maintainer.get("contacts")
        if not isinstance(contacts, list) or not contacts:
            errors.append(f"{maintainer_id} must have at least one contact path")

    page_ids: set[str] = set()
    source_paths: set[str] = set()
    pages_by_url: dict[str, dict] = {}
    for page in pages:
        if not isinstance(page, dict):
            errors.append("every page must be an object")
            continue
        page_id = page.get("id")
        if not isinstance(page_id, str) or not page_id:
            errors.append("every page must have a non-empty id")
            continue
        if page_id in page_ids:
            errors.append(f"duplicate page id: {page_id}")
        page_ids.add(page_id)

        url = page.get("url")
        if not isinstance(url, str) or not url.startswith(SITE_URL):
            errors.append(f"{page_id} url must be inside site_url")
        elif urlparse(url).scheme != "https":
            errors.append(f"{page_id} url must use HTTPS")
        elif url in pages_by_url:
            errors.append(f"duplicate page url: {url}")
        else:
            pages_by_url[url] = page

        if page.get("language") not in {"zh", "en"}:
            errors.append(f"{page_id} language must be zh or en")
        for field in ("title", "summary", "alternate_url"):
            if not isinstance(page.get(field), str) or not page[field]:
                errors.append(f"{page_id} {field} must be a non-empty string")

        source_path = page.get("source_path")
        if (
            not isinstance(source_path, str)
            or not source_path.startswith("docs/")
            or ".." in Path(source_path).parts
        ):
            errors.append(f"{page_id} source_path must be a safe path below docs/")
        elif source_path in source_paths:
            errors.append(f"duplicate source_path: {source_path}")
        else:
            source_paths.add(source_path)

        keywords = page.get("keywords")
        if not isinstance(keywords, list) or not keywords:
            errors.append(f"{page_id} keywords must be a non-empty array")
        elif not all(isinstance(keyword, str) and keyword for keyword in keywords):
            errors.append(f"{page_id} keywords must contain non-empty strings")
        if not DATE_RE.fullmatch(str(page.get("last_verified", ""))):
            errors.append(f"{page_id} last_verified must use YYYY-MM-DD")

        refs = page.get("maintainer_ids")
        if not isinstance(refs, list) or not refs:
            errors.append(f"{page_id} must reference at least one maintainer")
        else:
            for ref in refs:
                if ref not in maintainer_ids:
                    errors.append(f"{page_id} references unknown maintainer: {ref}")

    for page in pages:
        if not isinstance(page, dict) or not isinstance(page.get("id"), str):
            continue
        alternate = pages_by_url.get(page.get("alternate_url"))
        if alternate is None or alternate.get("alternate_url") != page.get("url"):
            errors.append(f"{page['id']} alternate_url is not reciprocal")

    if docs_root is not None:
        expected = {
            path.relative_to(docs_root).as_posix()
            for path in docs_root.rglob("*.md")
            if "superpowers" not in path.parts
        }
        indexed = {
            Path(page["source_path"]).relative_to("docs").as_posix()
            for page in pages
            if isinstance(page, dict)
            and isinstance(page.get("source_path"), str)
            and page["source_path"].startswith("docs/")
            and ".." not in Path(page["source_path"]).parts
        }
        for missing in sorted(expected - indexed):
            errors.append(f"public Markdown page missing from index: {missing}")
        for extra in sorted(indexed - expected):
            errors.append(f"indexed page has no Markdown source: {extra}")
        for page in pages:
            if not isinstance(page, dict) or not isinstance(
                page.get("source_path"), str
            ):
                continue
            source = docs_root.parent / page["source_path"]
            verified = str(page.get("last_verified", ""))
            if source.is_file() and verified not in source.read_text(encoding="utf-8"):
                errors.append(
                    f"{page.get('id', '<unknown>')} last_verified is absent from source page"
                )
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate the published Lab Wiki AI index"
    )
    parser.add_argument(
        "index",
        type=Path,
        nargs="?",
        default=Path("docs/assets/data/ai-index.json"),
    )
    parser.add_argument("--docs-root", type=Path, default=Path("docs"))
    args = parser.parse_args()
    payload = json.loads(args.index.read_text(encoding="utf-8"))
    errors = validate_index(payload, docs_root=args.docs_root)
    if errors:
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print(f"AI index validation passed: {args.index}")


if __name__ == "__main__":
    main()
