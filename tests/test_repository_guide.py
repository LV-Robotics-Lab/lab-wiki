from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ZH_PAGE = ROOT / "docs/project-collaboration/repository-guide.md"
EN_PAGE = ROOT / "docs/project-collaboration/repository-guide.en.md"
URL_RE = re.compile(r"https://[^)\s]+")


class RepositoryGuideContentTests(unittest.TestCase):
    def test_chinese_page_keeps_approved_content_and_metadata(self):
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

    def test_english_page_translates_the_complete_structure(self):
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

    def test_translations_preserve_structure_and_links(self):
        zh_content = ZH_PAGE.read_text(encoding="utf-8")
        en_content = EN_PAGE.read_text(encoding="utf-8")

        self.assertEqual(
            len(re.findall(r"^#{1,6} ", zh_content, flags=re.MULTILINE)),
            30,
        )
        self.assertEqual(
            len(re.findall(r"^#{1,6} ", en_content, flags=re.MULTILINE)),
            30,
        )
        self.assertEqual(
            len(re.findall(r"^\|", zh_content, flags=re.MULTILINE)),
            112,
        )
        self.assertEqual(
            len(re.findall(r"^\|", en_content, flags=re.MULTILINE)),
            112,
        )
        self.assertEqual(
            len(re.findall(r"^```", zh_content, flags=re.MULTILINE)),
            6,
        )
        self.assertEqual(
            len(re.findall(r"^```", en_content, flags=re.MULTILINE)),
            6,
        )
        self.assertEqual(URL_RE.findall(zh_content), URL_RE.findall(en_content))


if __name__ == "__main__":
    unittest.main()
