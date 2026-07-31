# Lab Wiki Starter Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a bilingual Material for MkDocs laboratory wiki starter that deploys automatically to GitHub Pages.

**Architecture:** Markdown content is organized with Chinese default files and `.en.md` English translations. Material for MkDocs provides the documentation UI, `mkdocs-static-i18n` builds both languages, and GitHub Actions publishes the generated `site/` directory.

**Tech Stack:** Python 3.12, MkDocs 1.6.1, Material for MkDocs 9.7.0, mkdocs-static-i18n 1.3.0, GitHub Actions, GitHub Pages.

## Global Constraints

- Chinese is the default language.
- English pages mirror the Chinese navigation structure.
- The first version covers onboarding and administration.
- The homepage uses documentation cards and quick links.
- Public testing content contains no real internal information.

---

### Task 1: Configure the bilingual documentation site

**Files:**
- Create: `mkdocs.yml`
- Create: `requirements.txt`
- Create: `.gitignore`
- Create: `docs/assets/stylesheets/extra.css`

- [x] Pin the MkDocs, Material, and i18n dependencies.
- [x] Configure Chinese as default and English as the secondary locale.
- [x] Enable navigation, search, cards, code-copy, and light/dark mode.
- [x] Add safe repository ignore rules.

### Task 2: Add corresponding Chinese and English content

**Files:**
- Create: `docs/index.md`
- Create: `docs/index.en.md`
- Create: `docs/onboarding/*.md`
- Create: `docs/administration/*.md`
- Create: `docs/contributing*.md`

- [x] Add the dashboard-style homepage in both languages.
- [x] Add onboarding overview, checklist, and access pages.
- [x] Add administration overview, reimbursement, and purchasing pages.
- [x] Add contribution instructions and public-test warnings.

### Task 3: Add GitHub Pages deployment

**Files:**
- Create: `.github/workflows/deploy.yml`
- Create: `README.md`

- [x] Configure a strict MkDocs build on every push to `main`.
- [x] Upload the generated site as a Pages artifact.
- [x] Deploy through GitHub Pages using OIDC permissions.
- [x] Document local preview and repository setup.

### Task 4: Verify the starter

- [x] Install dependencies in a clean virtual environment.
- [x] Run `mkdocs build --strict`.
- [x] Confirm the generated site contains Chinese and English outputs.
- [x] Package the complete starter as a ZIP archive.
