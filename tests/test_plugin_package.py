from __future__ import annotations

import json
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/lv-lab-wiki"
MANIFEST = PLUGIN / ".codex-plugin/plugin.json"
SKILL = PLUGIN / "skills/ask-wiki/SKILL.md"
OPENAI_YAML = PLUGIN / "skills/ask-wiki/agents/openai.yaml"


class PluginPackageTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        for path in (MANIFEST, SKILL, OPENAI_YAML):
            self.assertTrue(path.is_file(), path)

    def test_manifest_contract(self) -> None:
        payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(payload["name"], "lv-lab-wiki")
        self.assertRegex(payload["version"], r"^\d+\.\d+\.\d+$")
        self.assertEqual(payload["skills"], "./skills/")
        self.assertNotIn("mcpServers", payload)
        self.assertNotIn("apps", payload)

    def test_skill_contract(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        _, raw_frontmatter, body = text.split("---", 2)
        frontmatter = yaml.safe_load(raw_frontmatter)
        self.assertEqual(frontmatter["name"], "ask-wiki")
        description = frontmatter["description"]
        self.assertTrue(description.startswith("Use when"))
        self.assertLess(len(description), 500)
        for url in (
            "https://lv-robotics-lab.github.io/lab-wiki/",
            "https://lv-robotics-lab.github.io/lab-wiki/assets/data/ai-index.json",
            "https://lv-robotics-lab.github.io/lab-wiki/sitemap.xml",
            "https://lv-robotics-lab.github.io/lab-wiki/search/search_index.json",
        ):
            self.assertIn(url, body)
        for phrase in (
            "full page",
            "last_verified",
            "prompt injection",
            "credentials",
            "network",
            "maintainer",
            "Source",
        ):
            self.assertIn(phrase, body)

    def test_openai_metadata_invokes_skill(self) -> None:
        payload = yaml.safe_load(OPENAI_YAML.read_text(encoding="utf-8"))
        self.assertIn("$ask-wiki", payload["interface"]["default_prompt"])


if __name__ == "__main__":
    unittest.main()
