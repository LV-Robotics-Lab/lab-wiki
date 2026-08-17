from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ZH_PAGE = ROOT / "docs/project-collaboration/repository-guide.md"
EN_PAGE = ROOT / "docs/project-collaboration/repository-guide.en.md"
URL_RE = re.compile(r"https://[^)\s]+")


class RepositoryGuideContentTests(unittest.TestCase):
    def test_chinese_page_keeps_approved_content_and_metadata(self) -> None:
        content = ZH_PAGE.read_text(encoding="utf-8")
        for marker in (
            "# LV Robotics Lab 仓库导览",
            "## 当前组织盘点",
            "| 仓库总数 | 92 |",
            "| Base repository permission | `write` |",
            "## 6. 完整仓库主归属索引",
            "- 最后核验：2026-08-16",
        ):
            self.assertIn(marker, content)
        self.assertNotIn("仓库导览（内部版）", content)

    def test_english_page_translates_the_complete_structure(self) -> None:
        content = EN_PAGE.read_text(encoding="utf-8")
        for marker in (
            "# LV Robotics Lab Repository Guide",
            "## Current Organization Inventory",
            "| Total repositories | 92 |",
            "| Base repository permission | `write` |",
            "## 6. Complete Repository Ownership Index",
            "- Last verified: 2026-08-16",
        ):
            self.assertIn(marker, content)

    def test_translations_preserve_structure_and_links(self) -> None:
        zh = ZH_PAGE.read_text(encoding="utf-8")
        en = EN_PAGE.read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r"^#{1,6} ", zh, re.MULTILINE)), 30)
        self.assertEqual(len(re.findall(r"^#{1,6} ", en, re.MULTILINE)), 30)
        self.assertEqual(len(re.findall(r"^\|", zh, re.MULTILINE)), 112)
        self.assertEqual(len(re.findall(r"^\|", en, re.MULTILINE)), 112)
        self.assertEqual(len(re.findall(r"^```", zh, re.MULTILINE)), 6)
        self.assertEqual(len(re.findall(r"^```", en, re.MULTILINE)), 6)
        self.assertEqual(URL_RE.findall(zh), URL_RE.findall(en))

    def test_navigation_exposes_the_bilingual_guide(self) -> None:
        config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        for marker in (
            "项目协作: Project Collaboration",
            "实验室仓库导览: Lab Repository Guide",
            "- 项目协作:",
            "- 实验室仓库导览: project-collaboration/repository-guide.md",
        ):
            self.assertIn(marker, config)

    def test_ai_index_contains_reciprocal_guide_entries(self) -> None:
        payload = json.loads(
            (ROOT / "docs/assets/data/ai-index.json").read_text(encoding="utf-8")
        )
        pages = {page["id"]: page for page in payload["pages"]}
        zh = pages["project-collaboration/repository-guide:zh"]
        en = pages["project-collaboration/repository-guide:en"]
        self.assertEqual(zh["source_path"], "docs/project-collaboration/repository-guide.md")
        self.assertEqual(
            en["source_path"],
            "docs/project-collaboration/repository-guide.en.md",
        )
        self.assertEqual(zh["alternate_url"], en["url"])
        self.assertEqual(en["alternate_url"], zh["url"])
        self.assertEqual(zh["maintainer_ids"], ["wiki-team"])
        self.assertEqual(en["maintainer_ids"], ["wiki-team"])
        self.assertEqual(zh["last_verified"], "2026-08-16")
        self.assertEqual(en["last_verified"], "2026-08-16")


if __name__ == "__main__":
    unittest.main()
