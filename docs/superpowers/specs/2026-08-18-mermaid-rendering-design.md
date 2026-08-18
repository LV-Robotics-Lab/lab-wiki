# Mermaid Rendering Design

## Goal

Render fenced `mermaid` blocks as diagrams on the Material for MkDocs site, including the repository guide, without changing page content.

## Root Cause

The site enables `pymdownx.superfences`, but it does not register a Mermaid custom fence or load Mermaid in the browser. MkDocs therefore emits a highlighted `<pre><code>` block and no client-side renderer transforms it into a diagram.

## Considered Approaches

1. Use Material's documented custom-fence integration plus Mermaid JavaScript. This keeps Mermaid source in Markdown, supports the existing theme, and requires only site-level configuration. This is the selected approach.
2. Pre-render diagrams to SVG during the build. This avoids browser-side rendering but adds a Node or Mermaid CLI build dependency and generated assets.
3. Replace the diagram with a static image. This is simple for one page but makes future diagrams and text updates harder to maintain.

## Design

- Configure `pymdownx.superfences` with a `mermaid` custom fence using `fence_code_format`, producing a `.mermaid` container instead of a highlighted code block.
- Load a pinned Mermaid browser bundle through `extra_javascript` so site builds remain deterministic at the integration boundary.
- Add a small local initializer that disables Mermaid's automatic startup and renders `.mermaid` nodes whenever Material's `document$` navigation stream emits. This covers initial page load and instant navigation without rendering a diagram twice.
- Keep diagram source and all bilingual page content unchanged.

## Verification

- Add a test that builds the site and asserts the Chinese and English repository-guide HTML contain Mermaid containers rather than highlighted Mermaid source.
- Assert the built pages load both the pinned Mermaid bundle and the local initializer.
- Run the full unit-test suite, `mkdocs build --strict`, `git diff --check`, and inspect the generated repository-guide HTML.

## Scope

This change enables Mermaid rendering site-wide. It does not alter diagram content, add new diagrams, or change navigation.
