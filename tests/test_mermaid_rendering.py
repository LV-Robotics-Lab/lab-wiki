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
