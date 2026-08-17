# Lab Repository Guide Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish the approved LV Robotics Lab repository guide as a bilingual, navigable, AI-indexed Wiki page.

**Architecture:** Treat the supplied Markdown as the canonical Chinese content, changing only the obsolete title label and adding maintenance metadata. Add a structure-preserving English translation, then connect both pages through MkDocs navigation and reciprocal AI-index entries. Focused publication-contract tests protect the source structure, translation pairing, navigation, and discovery metadata.

**Tech Stack:** Markdown, Material for MkDocs, `mkdocs-static-i18n`, Mermaid fences, Python `unittest`, JSON, YAML

---

## File Map

- Create `docs/project-collaboration/repository-guide.md`: approved Chinese repository guide.
- Create `docs/project-collaboration/repository-guide.en.md`: complete English translation with identical structure and links.
- Create `tests/test_repository_guide.py`: publication contract for both pages, navigation, and discovery metadata.
- Modify `mkdocs.yml`: bilingual navigation labels and the new Project Collaboration section.
- Modify `docs/assets/data/ai-index.json`: reciprocal Chinese and English discovery records.

### Task 1: Define the bilingual page contract

**Files:**
- Create: `tests/test_repository_guide.py`

- [ ] **Step 1: Add a failing content-parity test**

Create `tests/test_repository_guide.py` with this complete content:

```python
from __future__ import annotations

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


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test and verify the expected failure**

Run:

```bash
python -m unittest tests.test_repository_guide -v
```

Expected: three errors caused by missing `docs/project-collaboration/repository-guide.md` and `repository-guide.en.md`.

- [ ] **Step 3: Commit the publication contract**

```bash
git add tests/test_repository_guide.py
git commit -m "test: define repository guide publication contract"
```

### Task 2: Publish the Chinese source and English translation

**Files:**
- Create: `docs/project-collaboration/repository-guide.md`
- Create: `docs/project-collaboration/repository-guide.en.md`

- [ ] **Step 1: Create the Chinese page from the approved source**

Use `/mnt/d/Desktop/LV-Robotics-Lab-repository-guide.md` as the exact source. Add it with `apply_patch`, preserving every line except for these two deliberate changes:

```diff
-# LV Robotics Lab 仓库导览（内部版）
+# LV Robotics Lab 仓库导览
```

Append this exact block after the existing “维护规则” list:

```markdown

## 维护信息

- 维护者：Wiki Team
- 最后核验：2026-08-16
```

- [ ] **Step 2: Create the complete English translation**

Create `docs/project-collaboration/repository-guide.en.md` with the same ordering, 30 headings, 112 table lines, 6 code-fence lines, 110 links, repository names, branch names, property names, numeric values, and dates as the Chinese page. Use these exact section headings:

```markdown
# LV Robotics Lab Repository Guide
## One-Sentence Navigation
## Current Organization Inventory
### Access Governance Snapshot
## Four Repository Roles in This Guide
## 0. Common Layer
## 1. Simulation Team
### Main Entry Points
### Simulation Foundations and Research References
## 2. World Model Team
### Main Entry Points
### Research Reference Shelf
## 3. Shared Real-Robot Structure
### Unified Entry Points
### Shared Tactile VTLA Training Reference
### 3.1 Franka Real-Robot Control
### 3.2 NERO Real-Robot Control
### 3.3 Cobot Real-Robot Control
### 3.4 Piper Real-Robot Control
### 3.5 LeRobot Real-Robot Control
### 3.6 Ego Collection and Algorithm Testing
### 3.7 UMI Collection Team
## 4. Unowned, Archival, or Reclassification Candidates
## 5. Recommended GitHub Information Architecture
### Team Hierarchy
### Recommended Repository Custom Properties
### Standard First Screen for Each Entry-Point README
## 6. Complete Repository Ownership Index
## Maintenance Rules
## Maintenance
```

Translate prose faithfully without changing the status of a proposal or snapshot. Preserve technical identifiers such as `owner_group`, `hardware/franka-wuji`, `read`, `write`, `main`, and repository names verbatim. End with:

```markdown
## Maintenance

- Maintainer: Wiki Team
- Last verified: 2026-08-16
```

- [ ] **Step 3: Run the focused content tests**

Run:

```bash
python -m unittest tests.test_repository_guide -v
```

Expected: `Ran 3 tests` and `OK`.

- [ ] **Step 4: Review the translated structure directly**

Run:

```bash
rg -c '^#{1,6} ' docs/project-collaboration/repository-guide.md docs/project-collaboration/repository-guide.en.md
rg -c '^\|' docs/project-collaboration/repository-guide.md docs/project-collaboration/repository-guide.en.md
rg -c '^```' docs/project-collaboration/repository-guide.md docs/project-collaboration/repository-guide.en.md
```

Expected: heading counts `30` and `30`, table-line counts `112` and `112`, and code-fence counts `6` and `6`.

- [ ] **Step 5: Commit the bilingual pages**

```bash
git add docs/project-collaboration/repository-guide.md docs/project-collaboration/repository-guide.en.md
git commit -m "docs: publish bilingual repository guide"
```

### Task 3: Add navigation and AI discovery

**Files:**
- Modify: `tests/test_repository_guide.py`
- Modify: `mkdocs.yml:58-82,106-130`
- Modify: `docs/assets/data/ai-index.json:1-7,630-653`

- [ ] **Step 1: Extend the contract with navigation and index tests**

Add `import json` after the future import in `tests/test_repository_guide.py`, then add these methods to `RepositoryGuideContentTests`:

```python
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
```

- [ ] **Step 2: Run the extended test and verify it fails**

Run:

```bash
python -m unittest tests.test_repository_guide -v
```

Expected: the three content tests pass; the navigation test fails because `mkdocs.yml` lacks the new labels, and the index test errors because the two page IDs are absent.

- [ ] **Step 3: Add bilingual MkDocs navigation**

Add these entries to the English `nav_translations` map in `mkdocs.yml`:

```yaml
            项目协作: Project Collaboration
            实验室仓库导览: Lab Repository Guide
```

Add this section immediately before “如何贡献” in `nav`:

```yaml
  - 项目协作:
      - 实验室仓库导览: project-collaboration/repository-guide.md
```

- [ ] **Step 4: Add reciprocal AI index entries**

Change `generated_at` in `docs/assets/data/ai-index.json` to `2026-08-17T00:00:00Z`. Insert these objects immediately before the `contributing:zh` entry:

```json
    {
      "id": "project-collaboration/repository-guide:zh",
      "language": "zh",
      "title": "LV Robotics Lab 仓库导览",
      "url": "https://lv-robotics-lab.github.io/lab-wiki/project-collaboration/repository-guide/",
      "alternate_url": "https://lv-robotics-lab.github.io/lab-wiki/en/project-collaboration/repository-guide/",
      "source_path": "docs/project-collaboration/repository-guide.md",
      "summary": "实验室组织仓库的组别归属、主入口、依赖层级、治理快照与导航建议。",
      "keywords": ["仓库导览", "GitHub", "仿真组", "世界模型组", "真机组", "仓库治理"],
      "maintainer_ids": ["wiki-team"],
      "last_verified": "2026-08-16"
    },
    {
      "id": "project-collaboration/repository-guide:en",
      "language": "en",
      "title": "LV Robotics Lab Repository Guide",
      "url": "https://lv-robotics-lab.github.io/lab-wiki/en/project-collaboration/repository-guide/",
      "alternate_url": "https://lv-robotics-lab.github.io/lab-wiki/project-collaboration/repository-guide/",
      "source_path": "docs/project-collaboration/repository-guide.en.md",
      "summary": "Team ownership, entry points, dependency layers, governance snapshot, and navigation guidance for the lab organization repositories.",
      "keywords": ["repository guide", "GitHub", "simulation team", "world model team", "real-robot team", "repository governance"],
      "maintainer_ids": ["wiki-team"],
      "last_verified": "2026-08-16"
    },
```

- [ ] **Step 5: Run the focused and index tests**

Run:

```bash
python -m unittest tests.test_repository_guide tests.test_ai_index -v
```

Expected: `Ran 12 tests` and `OK`.

- [ ] **Step 6: Commit navigation and discovery metadata**

```bash
git add tests/test_repository_guide.py mkdocs.yml docs/assets/data/ai-index.json
git commit -m "docs: index repository guide"
```

### Task 4: Verify the complete Wiki publication

**Files:**
- Verify only; no planned content changes.

- [ ] **Step 1: Run the full Python test suite**

Run:

```bash
python -m unittest discover -v
```

Expected: every discovered test passes with final status `OK`.

- [ ] **Step 2: Build both languages in strict mode**

Run:

```bash
mkdocs build --strict
```

Expected: both `zh` and `en` sites build successfully with no warnings or errors.

- [ ] **Step 3: Check formatting and inspect the final diff**

Run:

```bash
git diff --check HEAD~3..HEAD
git status --short
git log -4 --oneline
```

Expected: `git diff --check` prints nothing, `git status --short` is empty, and the log shows the test, bilingual-content, and indexing commits after the implementation-plan commit.

- [ ] **Step 4: Confirm the generated pages exist**

Run:

```bash
test -f site/project-collaboration/repository-guide/index.html
test -f site/en/project-collaboration/repository-guide/index.html
```

Expected: both commands exit with status `0`.
