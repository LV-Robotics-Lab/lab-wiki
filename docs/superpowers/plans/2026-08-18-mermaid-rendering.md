# Mermaid Rendering Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Render Mermaid fences as diagrams in both language variants of the repository guide.

**Architecture:** MkDocs converts `mermaid` fences into `.mermaid` containers through a `pymdownx.superfences` custom fence. A pinned Mermaid browser bundle and a local Material navigation subscriber render those containers on initial load and after instant navigation.

**Tech Stack:** Python `unittest`, MkDocs 1.6.1, Material for MkDocs 9.7.0, PyMdown Extensions, Mermaid 11.4.1

---

### Task 1: Add a build-output regression test

**Files:**
- Create: `tests/test_mermaid_rendering.py`

- [ ] **Step 1: Write the failing test**

```python
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class MermaidRenderingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.site_dir = Path(cls.temp_dir.name) / "site"
        subprocess.run(
            [
                sys.executable,
                "-m",
                "mkdocs",
                "build",
                "--strict",
                "--site-dir",
                str(cls.site_dir),
            ],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp_dir.cleanup()

    def test_repository_guides_emit_mermaid_containers(self) -> None:
        for relative_path in (
            "project-collaboration/repository-guide/index.html",
            "en/project-collaboration/repository-guide/index.html",
        ):
            html = (self.site_dir / relative_path).read_text(encoding="utf-8")
            self.assertIn('<pre class="mermaid"><code>flowchart TD', html)

    def test_repository_guides_load_mermaid_runtime(self) -> None:
        for relative_path in (
            "project-collaboration/repository-guide/index.html",
            "en/project-collaboration/repository-guide/index.html",
        ):
            html = (self.site_dir / relative_path).read_text(encoding="utf-8")
            self.assertIn(
                "https://unpkg.com/mermaid@11.4.1/dist/mermaid.min.js",
                html,
            )
            self.assertIn("assets/javascripts/mermaid.js", html)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the focused test and verify the expected failure**

Run: `../../.venv/bin/python -m unittest discover -s tests -p 'test_mermaid_rendering.py' -v`

Expected: FAIL because the generated guide contains a highlighted code block and does not load Mermaid.

- [ ] **Step 3: Commit the regression test**

```bash
git add tests/test_mermaid_rendering.py
git commit -m "test: cover Mermaid site rendering"
```

### Task 2: Configure and initialize Mermaid

**Files:**
- Modify: `mkdocs.yml`
- Create: `docs/assets/javascripts/mermaid.js`
- Test: `tests/test_mermaid_rendering.py`

- [ ] **Step 1: Register the Mermaid custom fence in `mkdocs.yml`**

```yaml
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
```

- [ ] **Step 2: Load the runtime and local initializer in `mkdocs.yml`**

```yaml
extra_javascript:
  - https://unpkg.com/mermaid@11.4.1/dist/mermaid.min.js
  - assets/javascripts/mermaid.js
```

- [ ] **Step 3: Create the Material navigation-aware initializer**

```javascript
mermaid.initialize({ startOnLoad: false });

document$.subscribe(async () => {
  await mermaid.run({
    nodes: document.querySelectorAll(".mermaid"),
  });
});
```

- [ ] **Step 4: Run the focused test and verify it passes**

Run: `../../.venv/bin/python -m unittest discover -s tests -p 'test_mermaid_rendering.py' -v`

Expected: 2 tests pass.

- [ ] **Step 5: Commit the implementation**

```bash
git add mkdocs.yml docs/assets/javascripts/mermaid.js
git commit -m "fix: render Mermaid diagrams"
```

### Task 3: Verify the complete change

**Files:**
- Verify: `mkdocs.yml`
- Verify: `docs/assets/javascripts/mermaid.js`
- Verify: `tests/test_mermaid_rendering.py`

- [ ] **Step 1: Run all unit tests**

Run: `../../.venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v`

Expected: 18 tests pass.

- [ ] **Step 2: Run the strict production build**

Run: `../../.venv/bin/mkdocs build --strict`

Expected: exit code 0 with both Chinese and English documentation built.

- [ ] **Step 3: Inspect the generated HTML contract**

Run: `rg -n 'class="mermaid"|mermaid@11.4.1|assets/javascripts/mermaid.js' site/project-collaboration/repository-guide/index.html site/en/project-collaboration/repository-guide/index.html`

Expected: both pages contain the Mermaid container and both scripts.

- [ ] **Step 4: Check whitespace and the final diff**

Run: `git diff --check HEAD~2..HEAD && git status --short`

Expected: no whitespace errors and no uncommitted implementation files.
