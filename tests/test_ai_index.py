from __future__ import annotations

import json
import unittest
from pathlib import Path

from scripts.validate_ai_index import validate_index


ROOT = Path(__file__).resolve().parents[1]


class AiIndexValidationTests(unittest.TestCase):
    def make_index(self) -> dict:
        return {
            "schema_version": 1,
            "site_url": "https://lv-robotics-lab.github.io/lab-wiki/",
            "generated_at": "2026-08-14T00:00:00Z",
            "default_language": "zh",
            "maintainers": [
                {
                    "id": "wiki-team",
                    "name_zh": "Wiki Team",
                    "name_en": "Wiki Team",
                    "contacts": [
                        {
                            "type": "controlled-directory",
                            "value": "Contact through the lab controlled directory",
                        }
                    ],
                }
            ],
            "pages": [
                {
                    "id": "index:zh",
                    "language": "zh",
                    "title": "LV Robotics Lab Wiki",
                    "url": "https://lv-robotics-lab.github.io/lab-wiki/",
                    "alternate_url": "https://lv-robotics-lab.github.io/lab-wiki/en/",
                    "source_path": "docs/index.md",
                    "summary": "实验室公开流程与资源入口。",
                    "keywords": ["Wiki", "实验室"],
                    "maintainer_ids": ["wiki-team"],
                    "last_verified": "2026-08-03",
                },
                {
                    "id": "index:en",
                    "language": "en",
                    "title": "LV Robotics Lab Wiki",
                    "url": "https://lv-robotics-lab.github.io/lab-wiki/en/",
                    "alternate_url": "https://lv-robotics-lab.github.io/lab-wiki/",
                    "source_path": "docs/index.en.md",
                    "summary": "Public lab procedures and resource entry points.",
                    "keywords": ["Wiki", "lab"],
                    "maintainer_ids": ["wiki-team"],
                    "last_verified": "2026-08-03",
                },
            ],
        }

    def test_accepts_valid_index(self) -> None:
        self.assertEqual(validate_index(self.make_index()), [])

    def test_rejects_duplicate_page_id(self) -> None:
        index = self.make_index()
        index["pages"][1]["id"] = "index:zh"
        self.assertIn("duplicate page id: index:zh", validate_index(index))

    def test_rejects_duplicate_page_url(self) -> None:
        index = self.make_index()
        index["pages"][1]["url"] = index["pages"][0]["url"]
        self.assertIn(
            f"duplicate page url: {index['pages'][0]['url']}",
            validate_index(index),
        )

    def test_rejects_unknown_maintainer(self) -> None:
        index = self.make_index()
        index["pages"][0]["maintainer_ids"] = ["missing"]
        self.assertIn(
            "index:zh references unknown maintainer: missing",
            validate_index(index),
        )

    def test_rejects_url_outside_published_wiki(self) -> None:
        index = self.make_index()
        index["pages"][0]["url"] = "https://example.com/"
        self.assertIn(
            "index:zh url must be inside site_url",
            validate_index(index),
        )

    def test_rejects_nonreciprocal_translation(self) -> None:
        index = self.make_index()
        index["pages"][1]["alternate_url"] = index["pages"][1]["url"]
        self.assertIn(
            "index:zh alternate_url is not reciprocal",
            validate_index(index),
        )

    def test_repository_index_covers_all_public_markdown(self) -> None:
        payload = json.loads(
            (ROOT / "docs/assets/data/ai-index.json").read_text(encoding="utf-8")
        )
        self.assertEqual(validate_index(payload, docs_root=ROOT / "docs"), [])


if __name__ == "__main__":
    unittest.main()
