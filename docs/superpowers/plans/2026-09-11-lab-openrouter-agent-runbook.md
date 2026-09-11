# Lab OpenRouter Agent Runbook Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend the existing bilingual Wiki and `ask-wiki` Skill with an agent-oriented, cross-platform runbook for configuring and troubleshooting the Lab Self-hosted OpenRouter with Claude Code and Claude Desktop.

**Architecture:** Keep the deployed Wiki as the source of truth and expand the existing AI API, CC Switch, and Codex pages instead of adding a parallel page. Encode exact model and effort policies in bilingual Markdown, index them in `ai-index.json`, and teach `ask-wiki` to retrieve the runbook, choose an OS branch, preserve credential boundaries, verify real inference, and escalate server-side pool failures.

**Tech Stack:** Material for MkDocs, Markdown, JSON, Python `unittest`, PyYAML, the existing `ask-wiki` Codex Skill.

**Spec:** `docs/superpowers/specs/2026-09-11-lab-openrouter-agent-runbook-design.md`

## Global Constraints

- Public names are `实验室自有 OpenRouter` and `Lab Self-hosted OpenRouter`.
- Keep Chinese `.md` and English `.en.md` pages structurally aligned.
- Never publish a real credential, email address, internal IP address, privileged endpoint, upstream account name, local absolute path, process ID, scheduled-task name, or personal usage figure.
- Use `<LAB_OPENROUTER_ADMIN_URL>`, `<LAB_OPENROUTER_ANTHROPIC_BASE_URL>`, `<LAB_OPENROUTER_OPENAI_BASE_URL>`, `<LAB_OPENROUTER_API_KEY>`, and `<LOCAL_CLAUDE_GATEWAY_URL>` exactly.
- Approved models are exactly `claude-sonnet-5`, `claude-sonnet-4-6`, `claude-opus-5`, `claude-opus-4-8`, `claude-opus-4-7`, and `claude-fable-5`.
- Do not publish Fable 5.1, Haiku, legacy models, or floating `latest` aliases as approved choices.
- Approved effort values are exactly `low`, `medium`, `high`, and `xhigh`; prohibit `max`, `ultra`, and unlisted values.
- Windows is the detailed primary path; macOS, native Linux, and WSL receive explicit branches.
- `/models` success is not sufficient; require a minimal inference request.
- Pool Mode and account-group mutations are maintainer-only operations.
- Do not push until the user explicitly approves the publication step.

---

### Task 1: Add The Runbook Content Contract

**Files:**
- Create: `tests/test_lab_openrouter_runbook.py`
- Test: `tests/test_lab_openrouter_runbook.py`

**Interfaces:**
- Consumes: existing Markdown pages, AI index JSON, and `ask-wiki/SKILL.md`.
- Produces: executable content invariants that Tasks 2-6 must satisfy.

- [ ] **Step 1: Create failing content-contract tests**

Create `tests/test_lab_openrouter_runbook.py` with tests that:

```python
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
            zh_levels = re.findall(r"^(#{1,6}) ", zh_path.read_text(encoding="utf-8"), re.MULTILINE)
            en_levels = re.findall(r"^(#{1,6}) ", en_path.read_text(encoding="utf-8"), re.MULTILINE)
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
        for page_id in ("resources/ai-api-access:zh", "resources/ai-api-access:en", "resources/cc-switch:zh", "resources/cc-switch:en"):
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
```

- [ ] **Step 2: Run the new tests and verify they fail for missing runbook content**

Run: `python -m unittest tests.test_lab_openrouter_runbook -v`

Expected: failures for missing platform name, placeholders, model allowlist, OS branches, troubleshooting markers, index keywords, and Skill constraints.

- [ ] **Step 3: Commit the failing contract**

```bash
git add tests/test_lab_openrouter_runbook.py
git commit -m "test: define lab OpenRouter runbook contract"
```

---

### Task 2: Introduce The Lab Self-hosted OpenRouter

**Files:**
- Modify: `docs/resources/ai-api-access.md`
- Modify: `docs/resources/ai-api-access.en.md`
- Test: `tests/test_lab_openrouter_runbook.py`

**Interfaces:**
- Consumes: public names and endpoint placeholders from Global Constraints.
- Produces: the platform definition, protocol boundary, application flow, and escalation ownership used by the CC Switch runbook and `ask-wiki`.

- [ ] **Step 1: Update the Chinese AI API page**

Replace the generic service-entry treatment with a section headed `## 实验室自有 OpenRouter` that contains:

- a service table using the five approved placeholders rather than a deployed internal address;
- the exact flow `Claude Code / Claude Desktop → CC Switch → Anthropic Messages 兼容端点 → 可调度账号组 → 经审计的 Anthropic 上游`;
- a comparison table for administrative console, Anthropic Messages endpoint, and OpenAI-compatible endpoint;
- the rule that administrative and inference URLs are not interchangeable;
- the rule that OpenAI-compatible access does not prove Anthropic Messages compatibility;
- a link to `cc-switch.md` for agent execution.

Retain the existing request, usage, verification, troubleshooting, maintainer, and last-verified sections. Update the last-verified date to `2026-09-11`.

- [ ] **Step 2: Update the English AI API page with identical structure**

Use the heading `## Lab Self-hosted OpenRouter` and preserve the same tables, decision boundaries, placeholders, and date as the Chinese page.

- [ ] **Step 3: Run the platform and bilingual-structure tests**

Run:

```bash
python -m unittest tests.test_lab_openrouter_runbook.LabOpenRouterRunbookTests.test_ai_api_pages_introduce_the_platform_and_protocol_boundary tests.test_lab_openrouter_runbook.LabOpenRouterRunbookTests.test_bilingual_runbooks_have_matching_heading_depths -v
```

Expected: both tests pass.

- [ ] **Step 4: Commit the platform documentation**

```bash
git add docs/resources/ai-api-access.md docs/resources/ai-api-access.en.md
git commit -m "docs: introduce lab self-hosted OpenRouter"
```

---

### Task 3: Convert CC Switch Documentation Into An Agent Runbook

**Files:**
- Modify: `docs/resources/cc-switch.md`
- Modify: `docs/resources/cc-switch.en.md`
- Test: `tests/test_lab_openrouter_runbook.py`

**Interfaces:**
- Consumes: platform definition and placeholders from Task 2.
- Produces: exact OS branching, provider fields, model policy, effort policy, verification contract, and failure-routing procedure.

- [ ] **Step 1: Reorganize the Chinese CC Switch page**

Use this section order:

```text
# 使用 CC Switch 配置实验室自有 OpenRouter
## Agent 执行契约
## 必需输入
## 平台与部署拓扑判断
## 安装 CC Switch
### Windows
### macOS
### Linux
### WSL
## 配置 Claude Code
## 配置 Claude Desktop
## 模型白名单
## 思考强度策略
## 验证
## 故障排查决策树
## 维护信息
```

The agent contract must state: detect the OS first; never ask for a key in chat; require local credential entry; stop at password or permission prompts for the user; preserve existing unrelated providers; and do not assume Claude Code and Claude Desktop share configuration.

The required-input table must include the five approved placeholders and identify which values come from the maintainer versus the local machine.

The Claude Code provider table must use:

```text
名称: Lab Self-hosted OpenRouter
API Key / Authentication: <LAB_OPENROUTER_API_KEY>
Base URL: <LAB_OPENROUTER_ANTHROPIC_BASE_URL>
默认模型: claude-sonnet-5
默认思考强度: medium
```

The Claude Desktop section must explain the separate inference-gateway profile, `<LOCAL_CLAUDE_GATEWAY_URL>`, and optional compatibility adapter. Windows persistence uses a per-user startup mechanism, macOS uses a per-user LaunchAgent, and native Linux uses a systemd user service when available. WSL instructions must explicitly identify whether CC Switch and Claude Desktop run on Windows while Claude Code runs inside WSL.

The model table must include only the six approved canonical IDs. The effort table must allow `low`, `medium`, `high`, and `xhigh` and explicitly prohibit `max`, `ultra`, and any unlisted value.

The verification checklist must require active provider state, non-secret generated configuration, no stale environment override, optional model discovery, real minimal inference, Desktop token-count and Messages flows, and a secret-output check.

The troubleshooting table must include `401/403`, Messages-route `404`, `/count_tokens` `404`, `429`, `503 No available accounts`, model-listed-but-inference-fails, repeated account disablement, and unavailable loopback gateway. Mark Pool Mode and account-group changes as maintainer-only.

Update the last-verified date to `2026-09-11`.

- [ ] **Step 2: Write the English CC Switch page with matching structure and policy**

Use `# Configure the Lab Self-hosted OpenRouter with CC Switch` and translate every heading, table row, constraint, verification check, and troubleshooting branch without changing model IDs, effort values, placeholders, or date.

- [ ] **Step 3: Run the CC Switch contract tests**

Run:

```bash
python -m unittest tests.test_lab_openrouter_runbook.LabOpenRouterRunbookTests.test_cc_switch_pages_expose_os_branches_and_exact_allowlists tests.test_lab_openrouter_runbook.LabOpenRouterRunbookTests.test_cc_switch_pages_define_real_verification_and_failure_routing tests.test_lab_openrouter_runbook.LabOpenRouterRunbookTests.test_bilingual_runbooks_have_matching_heading_depths -v
```

Expected: all three tests pass.

- [ ] **Step 4: Commit the bilingual agent runbook**

```bash
git add docs/resources/cc-switch.md docs/resources/cc-switch.en.md
git commit -m "docs: add cross-platform OpenRouter agent runbook"
```

---

### Task 4: Clarify The Codex Protocol Boundary

**Files:**
- Modify: `docs/resources/codex-cli.md`
- Modify: `docs/resources/codex-cli.en.md`
- Test: `tests/test_lab_openrouter_runbook.py`

**Interfaces:**
- Consumes: platform and protocol definitions from Task 2.
- Produces: a cross-link and explicit prohibition against reusing an OpenAI Responses profile as a Claude Messages profile.

- [ ] **Step 1: Add a Chinese protocol-boundary section**

Add a matching section near the existing relay/profile configuration that says:

```text
## 与实验室自有 OpenRouter 的协议边界
```

It must explain that Codex uses an OpenAI-compatible `Responses` profile, Claude uses an `Anthropic Messages` profile, and a provider that can route a Claude-named model through an OpenAI schema is still not an Anthropic Messages endpoint. Link to `cc-switch.md` for Claude configuration.

- [ ] **Step 2: Add the matching English section**

Use:

```text
## Protocol Boundary With The Lab Self-hosted OpenRouter
```

Preserve the exact protocol names and link to `cc-switch.en.md`.

- [ ] **Step 3: Run the Codex boundary and bilingual tests**

Run:

```bash
python -m unittest tests.test_lab_openrouter_runbook.LabOpenRouterRunbookTests.test_codex_pages_explain_that_openai_and_anthropic_profiles_are_distinct tests.test_lab_openrouter_runbook.LabOpenRouterRunbookTests.test_bilingual_runbooks_have_matching_heading_depths -v
```

Expected: both tests pass.

- [ ] **Step 4: Commit the protocol clarification**

```bash
git add docs/resources/codex-cli.md docs/resources/codex-cli.en.md
git commit -m "docs: clarify Codex and Claude protocol boundary"
```

---

### Task 5: Update Discovery Metadata And Resource Summaries

**Files:**
- Modify: `docs/resources/index.md`
- Modify: `docs/resources/index.en.md`
- Modify: `docs/assets/data/ai-index.json`
- Test: `tests/test_lab_openrouter_runbook.py`
- Test: `tests/test_ai_index.py`

**Interfaces:**
- Consumes: the page titles, URLs, and terminology created in Tasks 2-4.
- Produces: discoverable index entries used by `ask-wiki` candidate selection.

- [ ] **Step 1: Update the bilingual Resources summaries**

Change the existing CC Switch entry to describe agent-driven configuration of the Lab Self-hosted OpenRouter for Claude Code and Claude Desktop across Windows, macOS, Linux, and WSL. Keep Chinese and English list order aligned.

- [ ] **Step 2: Update the AI index records**

For `resources/ai-api-access:zh`, `resources/ai-api-access:en`, `resources/cc-switch:zh`, and `resources/cc-switch:en`:

- update summaries to mention the Lab Self-hosted OpenRouter;
- add retrieval keywords for `OpenRouter`, `Claude Desktop`, `Claude Code`, `CC Switch`, `Anthropic Messages`, `503`, `count_tokens`, and `Pool Mode` as appropriate;
- set `last_verified` to `2026-09-11`;
- retain reciprocal URLs, source paths, and maintainer IDs.

Update `generated_at` to a valid `2026-09-11T...Z` timestamp without changing `schema_version` or `site_url`.

- [ ] **Step 3: Run index validation tests**

Run:

```bash
python -m unittest tests.test_lab_openrouter_runbook.LabOpenRouterRunbookTests.test_ai_index_routes_openrouter_and_error_queries tests.test_ai_index -v
```

Expected: all tests pass and the index has no duplicate IDs, duplicate URLs, unknown maintainers, uncovered Markdown, or nonreciprocal translations.

- [ ] **Step 4: Commit the discovery update**

```bash
git add docs/resources/index.md docs/resources/index.en.md docs/assets/data/ai-index.json
git commit -m "docs: index lab OpenRouter runbook"
```

---

### Task 6: Teach `ask-wiki` To Execute The Runbook Safely

**Files:**
- Modify: `plugins/lv-lab-wiki/skills/ask-wiki/SKILL.md`
- Modify: `tests/test_plugin_package.py`
- Modify: `tests/skill-evals/ask-wiki.md`
- Test: `tests/test_lab_openrouter_runbook.py`
- Test: `tests/test_plugin_package.py`

**Interfaces:**
- Consumes: live Wiki pages and AI-index metadata from Tasks 2-5.
- Produces: retrieval and execution policy for OS selection, local credential entry, model/effort allowlists, real-inference verification, and maintainer escalation.

- [ ] **Step 1: Extend the plugin contract tests**

In `tests/test_plugin_package.py`, add required Skill-body markers:

```python
for phrase in (
    "Lab Self-hosted OpenRouter",
    "operating system",
    "local credential entry",
    "claude-sonnet-5",
    "xhigh",
    "503 No available accounts",
    "Pool Mode",
):
    self.assertIn(phrase, body)
```

Add evaluation scenarios to `tests/skill-evals/ask-wiki.md` for Windows setup, macOS/Linux branching, WSL topology, model selection, effort capping, `/count_tokens` failure, and `503 No available accounts`. Each expected behavior must require live page citation and prohibit requesting a secret in chat.

- [ ] **Step 2: Run plugin tests and verify they fail**

Run: `python -m unittest tests.test_plugin_package -v`

Expected: failure because the Skill lacks the new routing and execution policy.

- [ ] **Step 3: Add the Skill's OpenRouter execution workflow**

Add a section titled `## Lab Self-hosted OpenRouter Runbook` to `SKILL.md` that requires the agent to:

1. Fetch the current AI API and CC Switch pages.
2. Determine the operating system and distinguish Windows-hosted CC Switch plus WSL Claude Code from native Linux.
3. Use local credential entry and never request, repeat, or log the key.
4. Preserve the six-model allowlist and the `low`/`medium`/`high`/`xhigh` effort cap.
5. Treat `/models` as discovery only and require a minimal inference result.
6. Route `/count_tokens` compatibility failures separately from authentication failures.
7. Route `503 No available accounts`, account-group eligibility, scheduling, and Pool Mode to the maintainer.
8. Never perform privileged account-group or Pool Mode mutations from public Wiki instructions.

Keep endpoint data in the live Wiki rather than copying it into the Skill.

- [ ] **Step 4: Run Skill and plugin contract tests**

Run:

```bash
python -m unittest tests.test_plugin_package tests.test_lab_openrouter_runbook.LabOpenRouterRunbookTests.test_skill_contains_agent_execution_constraints -v
```

Expected: all tests pass.

- [ ] **Step 5: Commit the Skill update**

```bash
git add plugins/lv-lab-wiki/skills/ask-wiki/SKILL.md tests/test_plugin_package.py tests/skill-evals/ask-wiki.md
git commit -m "feat: route OpenRouter setup through ask-wiki"
```

---

### Task 7: Validate The Complete Wiki And Review Publication Safety

**Files:**
- Verify: all modified files from Tasks 1-6

**Interfaces:**
- Consumes: the complete implementation.
- Produces: evidence that the Wiki builds, the bilingual contract holds, and no sensitive values or generated artifacts will be published.

- [ ] **Step 1: Run the full repository test suite**

Run: `python -m unittest discover -s tests -v`

Expected: all tests pass with zero failures and zero errors.

- [ ] **Step 2: Run strict MkDocs build outside the repository output path**

Run:

```powershell
$siteOut = Join-Path $env:TEMP 'lab-wiki-openrouter-site'
python -m mkdocs build --strict --site-dir $siteOut
```

Expected: exit code `0`, no strict warnings, and no tracked `site/` directory.

- [ ] **Step 3: Compare bilingual structure and policy values**

Run:

```bash
python -m unittest tests.test_lab_openrouter_runbook -v
```

Expected: all bilingual heading, model, effort, protocol, troubleshooting, discovery, and Skill tests pass.

- [ ] **Step 4: Scan for prohibited sensitive values and unapproved models**

Run a case-sensitive repository scan over the modified files for:

```text
100.64.
8320
8324
18324
sk- followed by 32 or more hexadecimal characters
the previously supplied administrator email domain
the previously supplied password fragment
claude-fable-5-1
claude-fable-5.1
```

Expected: no matches in publishable source files. The design and plan may mention prohibited model names only as explicit negative requirements; the published Resources pages and Skill must not expose them as approved choices.

- [ ] **Step 5: Review the final diff and repository state**

Run:

```bash
git diff --check
git status --short
git log --oneline --decorate -10
```

Review every changed line for credential leakage, private endpoints, duplicated content, broken links, translation drift, generated files, and unrequested changes.

- [ ] **Step 6: Report the verified local result and request publication approval**

Report the test count, strict-build result, commit list, and changed files. Do not push until the user explicitly approves publishing the verified commits to GitHub `main`.
