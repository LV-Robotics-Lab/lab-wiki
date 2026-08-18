# Non-Hardware Team Collaboration Guide Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a bilingual, operational Wiki page for the unified collaboration model used by all non-hardware teams, currently the world-model and simulation teams.

**Architecture:** Add a focused page pair under a new top-level `项目协作` / `Project Collaboration` navigation section. Keep `如何贡献` / `How to Contribute` limited to Wiki editing workflow. The Chinese and English pages share the same section order and constraints, while `mkdocs.yml` provides the English navigation translations.

**Tech Stack:** Markdown, Material for MkDocs, `mkdocs-static-i18n` navigation suffixes.

---

## File Map

- `docs/project-collaboration/non-hardware-worktree.md`: Chinese operational guide and source-of-truth wording for the requested rule.
- `docs/project-collaboration/non-hardware-worktree.en.md`: English mirror with matching headings, examples, and safety boundaries.
- `docs/assets/data/ai-index.json`: Register the new public pages and their role-based maintainer so the repository index contract remains complete.
- `mkdocs.yml`: Add the top-level bilingual navigation section and its English labels.
- `docs/superpowers/plans/2026-08-14-non-hardware-team-collaboration.md`: This implementation record; excluded from the published site by `exclude_docs`.

### Task 1: Add the Chinese collaboration guide

**Files:**
- Create: `docs/project-collaboration/non-hardware-worktree.md`

- [ ] **Step 1: Create the page with the required operational sections**

Write a Chinese page titled `# 非真机组统一协作模式` with the following sections in order: `## 一句话原则`, `## 用途`, `## 适用范围`, `## 前置条件`, `## 目录与分支模型`, `## 日常协作流程`, `## 大型文件与实验产物`, `## 合入 main 的条件`, `## 清理前检查`, `## 验证清单`, `## 故障排查`, and `## 维护信息`.

Use the approved content rules:

- State that the rule applies to all non-hardware teams and currently covers the world-model and simulation teams; state that hardware teams have additional device, calibration, real-time-control, and experiment-data boundaries.
- Show only placeholder paths: `/home/<SHARED_ACCOUNT>/workspace/<REPO>/` for the shared repository and `/home/<MEMBER_NAME>/<REPO>/` mapped to `worktree/<MEMBER_NAME>` for a personal worktree.
- State that one project uses one organization repository and one shared `main`; prohibit personal GitHub repositories and long-lived second clones.
- Require all code, experiment configuration, scripts, notes, and stage results to remain inside the member worktree and be committed and pushed promptly.
- Keep large datasets, checkpoints, caches, and run results in a worktree-local `local_data/`, `data/`, or agreed directory; exclude them with `.gitignore` and track a manifest containing source, hash, version, owner, and verification date.
- Require regular synchronization from `main`; allow only verified, reusable shared functionality into `main`; leave unfinished experiments on personal branches.
- Before deleting directories, branches, or experiment materials, require confirmation that commits were pushed, unique commits are covered by active branches, and important local data has a manifest or backup.
- Include troubleshooting for an accidental personal clone, files outside the worktree, a branch behind `main`, an accidentally tracked large file, and an unpushed commit discovered during cleanup. Do not provide recursive deletion commands.
- End with role-based maintainer information and `最后核验：2026-08-14`; do not include personal contacts or credentials.

- [ ] **Step 2: Check the Chinese page for publication safety and wording consistency**

Run:

```bash
git diff --check -- docs/project-collaboration/non-hardware-worktree.md
rg -n 'TBD|TODO|<API_TOKEN>|password|私钥|手机号|邮箱|192\.168\.|smb://' docs/project-collaboration/non-hardware-worktree.md
```

Expected: `git diff --check` produces no output; the sensitive-pattern search produces no matches. Placeholder path tokens such as `<REPO>` and `<MEMBER_NAME>` are expected and safe.

### Task 2: Add the English mirror

**Files:**
- Create: `docs/project-collaboration/non-hardware-worktree.en.md`

- [ ] **Step 1: Mirror the Chinese guide section by section**

Write `# Unified Collaboration for Non-Hardware Teams` with the same 12 headings and the same examples as the Chinese page. Translate the scope as “all non-hardware teams; currently the world-model and simulation teams,” preserve the distinction from hardware-team safety rules, and keep the placeholder paths `<SHARED_ACCOUNT>`, `<MEMBER_NAME>`, and `<REPO>` unchanged.

Use the same requirements for one organization repository, one shared `main`, personal worktrees, prompt commit/push, local ignored data, manifests and hashes, synchronization, promotion criteria, cleanup checks, troubleshooting, role-based maintainer information, and last verification date `2026-08-14`.

- [ ] **Step 2: Verify bilingual parity**

Compare the heading lists and code/path examples:

```bash
rg '^## ' docs/project-collaboration/non-hardware-worktree.md
rg '^## ' docs/project-collaboration/non-hardware-worktree.en.md
rg -n '<SHARED_ACCOUNT>|<MEMBER_NAME>|<REPO>|2026-08-14' docs/project-collaboration/non-hardware-worktree{,.en}.md
```

Expected: both pages have the same 12 section positions, all three placeholder tokens occur in both pages, and both pages use the same verification date.

### Task 3: Add the new navigation section

**Files:**
- Modify: `mkdocs.yml`
- Modify: `docs/assets/data/ai-index.json`

- [ ] **Step 1: Add English navigation translations**

Under `plugins.i18n.languages[locale=en].nav_translations`, add:

```yaml
项目协作: Project Collaboration
非真机组统一协作模式: Unified Collaboration for Non-Hardware Teams
```

- [ ] **Step 2: Add the Chinese navigation entry**

After the existing `研究与课程` section and before `如何贡献`, add:

```yaml
  - 项目协作:
      - 非真机组统一协作模式: project-collaboration/non-hardware-worktree.md
```

Do not move or rename the existing `如何贡献` entry.

- [ ] **Step 3: Register both pages in the public AI index**

Add the role-based maintainer `non-hardware-team-maintainer` with a controlled-directory contact, then add reciprocal `zh` and `en` page records for `docs/project-collaboration/non-hardware-worktree.md` and `docs/project-collaboration/non-hardware-worktree.en.md`. Use the published paths `/lab-wiki/project-collaboration/non-hardware-worktree/` and `/lab-wiki/en/project-collaboration/non-hardware-worktree/`, set `last_verified` to `2026-08-14`, and reference only the new role-based maintainer.

### Task 4: Build and review the complete change

**Files:**
- Verify: `docs/project-collaboration/non-hardware-worktree.md`
- Verify: `docs/project-collaboration/non-hardware-worktree.en.md`
- Verify: `docs/assets/data/ai-index.json`
- Verify: `mkdocs.yml`

- [ ] **Step 1: Run the strict MkDocs build**

Run:

```bash
mkdocs build --strict
```

Expected: the build exits with status 0 and reports no warning about missing navigation targets, untranslated navigation labels, or Markdown errors. The generated `site/` directory remains untracked.

- [ ] **Step 2: Review the diff and repository status**

Run:

```bash
git diff --check
git diff --stat
git status --short
```

Expected: only the two new bilingual pages, `docs/assets/data/ai-index.json`, and `mkdocs.yml` are implementation changes; no `.venv/`, `site/`, credentials, personal identifiers, or unrelated edits are present.

- [ ] **Step 3: Commit the implementation**

```bash
git add docs/project-collaboration/non-hardware-worktree.md docs/project-collaboration/non-hardware-worktree.en.md docs/assets/data/ai-index.json mkdocs.yml
git commit -m "docs: add non-hardware team collaboration guide"
```

Expected: one commit contains the bilingual guide and navigation update. Do not push; repository instructions require explicit user authorization before pushing.

## Self-review checklist

- [ ] Every design requirement has a corresponding page section or navigation task.
- [ ] No step relies on an unspecified file, command, or maintainer identity.
- [ ] Both language pages use the same scope, path placeholders, cleanup boundary, and verification date.
- [ ] The page is discoverable under `项目协作`, not under `如何贡献`.
- [ ] Strict build and diff review are completed before claiming the change is ready.
