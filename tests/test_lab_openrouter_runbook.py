from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ZH_API = ROOT / "docs/resources/ai-api-access.md"
EN_API = ROOT / "docs/resources/ai-api-access.en.md"
ZH_CC = ROOT / "docs/resources/cc-switch.md"
EN_CC = ROOT / "docs/resources/cc-switch.en.md"
ZH_CODEX = ROOT / "docs/resources/codex-cli.md"
EN_CODEX = ROOT / "docs/resources/codex-cli.en.md"
SKILL = ROOT / "plugins/lv-lab-wiki/skills/ask-wiki/SKILL.md"
INDEX = ROOT / "docs/assets/data/ai-index.json"

APPROVED_MODELS = (
    "claude-sonnet-5",
    "claude-sonnet-4-6",
    "claude-opus-5",
    "claude-opus-4-8",
    "claude-opus-4-7",
    "claude-fable-5",
)
REQUIRED_PLACEHOLDERS = (
    "<LAB_OPENROUTER_ADMIN_URL>",
    "<LAB_OPENROUTER_ANTHROPIC_BASE_URL>",
    "<LAB_OPENROUTER_OPENAI_BASE_URL>",
    "<LAB_OPENROUTER_API_KEY>",
    "<LOCAL_CLAUDE_GATEWAY_URL>",
)


class LabOpenRouterRunbookTests(unittest.TestCase):
    def test_ai_api_pages_introduce_the_platform_and_protocol_boundary(self) -> None:
        zh = ZH_API.read_text(encoding="utf-8")
        en = EN_API.read_text(encoding="utf-8")
        for marker in ("实验室自有 OpenRouter", "Anthropic Messages", "OpenAI"):
            self.assertIn(marker, zh)
        for marker in ("Lab Self-hosted OpenRouter", "Anthropic Messages", "OpenAI"):
            self.assertIn(marker, en)
        for placeholder in REQUIRED_PLACEHOLDERS[:4]:
            self.assertIn(placeholder, zh)
            self.assertIn(placeholder, en)

    def test_cc_switch_pages_expose_os_branches_and_exact_allowlists(self) -> None:
        zh = ZH_CC.read_text(encoding="utf-8")
        en = EN_CC.read_text(encoding="utf-8")
        for marker in ("Windows", "macOS", "Linux", "WSL", "Claude Desktop"):
            self.assertIn(marker, zh)
            self.assertIn(marker, en)
        for model in APPROVED_MODELS:
            self.assertIn(f"`{model}`", zh)
            self.assertIn(f"`{model}`", en)
        for effort in ("`low`", "`medium`", "`high`", "`xhigh`"):
            self.assertIn(effort, zh)
            self.assertIn(effort, en)
        for forbidden in ("claude-fable-5-1", "claude-fable-5.1", "`latest`"):
            self.assertNotIn(forbidden, zh)
            self.assertNotIn(forbidden, en)
        self.assertIn("`max`", zh)
        self.assertIn("`ultra`", zh)
        self.assertIn("`max`", en)
        self.assertIn("`ultra`", en)

    def test_cc_switch_pages_define_real_verification_and_failure_routing(self) -> None:
        for path in (ZH_CC, EN_CC):
            text = path.read_text(encoding="utf-8")
            for marker in (
                "/models",
                "/count_tokens",
                "503 No available accounts",
                "Pool Mode",
                "<LOCAL_CLAUDE_GATEWAY_URL>",
            ):
                self.assertIn(marker, text)

    def test_bilingual_runbooks_have_matching_heading_depths(self) -> None:
        for zh_path, en_path in ((ZH_API, EN_API), (ZH_CC, EN_CC), (ZH_CODEX, EN_CODEX)):
            zh_levels = re.findall(
                r"^(#{1,6}) ", zh_path.read_text(encoding="utf-8"), re.MULTILINE
            )
            en_levels = re.findall(
                r"^(#{1,6}) ", en_path.read_text(encoding="utf-8"), re.MULTILINE
            )
            self.assertEqual(zh_levels, en_levels, (zh_path, en_path))

    def test_codex_pages_explain_that_openai_and_anthropic_profiles_are_distinct(self) -> None:
        zh = ZH_CODEX.read_text(encoding="utf-8")
        en = EN_CODEX.read_text(encoding="utf-8")
        self.assertIn("实验室自有 OpenRouter", zh)
        self.assertIn("Lab Self-hosted OpenRouter", en)
        for marker in ("Anthropic Messages", "Responses"):
            self.assertIn(marker, zh)
            self.assertIn(marker, en)

    def test_ai_index_routes_openrouter_and_error_queries(self) -> None:
        payload = json.loads(INDEX.read_text(encoding="utf-8"))
        pages = {page["id"]: page for page in payload["pages"]}
        for page_id in (
            "resources/ai-api-access:zh",
            "resources/ai-api-access:en",
            "resources/cc-switch:zh",
            "resources/cc-switch:en",
        ):
            keywords = " ".join(pages[page_id]["keywords"])
            self.assertIn("OpenRouter", keywords)
        cc_keywords = " ".join(pages["resources/cc-switch:en"]["keywords"])
        for marker in ("503", "count_tokens", "Pool Mode", "Claude Desktop"):
            self.assertIn(marker, cc_keywords)

    def test_skill_contains_agent_execution_constraints(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        for marker in (
            "Lab Self-hosted OpenRouter",
            "operating system",
            "local credential entry",
            "claude-sonnet-5",
            "xhigh",
            "503 No available accounts",
            "Pool Mode",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
