# Lab Resources Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a bilingual Lab Resources section that exposes only approved public information and uses descriptive placeholders for internal spreadsheets.

**Architecture:** Material for MkDocs will render two suffix-paired page sets under `docs/resources/`. The Chinese `nav` entries in `mkdocs.yml` will define the section, while `nav_translations` supplies aligned English labels. The resource overview links to the local Hardware Resource Center page and the public GitHub organization, but shows internal spreadsheet destinations only as non-clickable placeholders.

**Tech Stack:** Material for MkDocs, `mkdocs-static-i18n`, Markdown, YAML

## Global Constraints

- Chinese is the default language; every Chinese page must have a matching `.en.md` page with aligned structure.
- Use `<INTERN_VISITING_TRACKER_URL>`, `<PURCHASE_ASSET_REGISTER_URL>`, and `<ROMOYA_RESOURCE_SHEET_URL>` exactly for the internal spreadsheets.
- Do not include Google Sheet URLs or IDs, Notion page URLs or IDs, Google account identifiers, backup codes, or authentication instructions.
- Keep the GitHub organization URL explicit: `https://github.com/orgs/LV-Robotics-Lab/repositories`.
- Mark the incomplete Hardware Resource Center content with `Requires maintainer review`; do not invent operational procedures.
- Preserve all unrelated working-tree changes and never add `.venv/` or `site/` to Git.
- Run `mkdocs build --strict` after the complete content and navigation change.

---

### Task 1: Bilingual Resource Directory

**Files:**
- Create: `docs/resources/index.md`
- Create: `docs/resources/index.en.md`

**Interfaces:**
- Consumes: Existing suffix-based bilingual page convention and the approved URL placeholder names.
- Produces: The section landing page referenced by `mkdocs.yml` and a local link to `resources/hardware.md`.

- [ ] **Step 1: Verify the new page pair does not already exist**

Run:

```bash
test ! -e docs/resources/index.md && test ! -e docs/resources/index.en.md
```

Expected: exit status 0. If either file exists, inspect it and merge carefully instead of overwriting it.

- [ ] **Step 2: Create the Chinese resource directory**

Create `docs/resources/index.md` with this exact content:

```markdown
# 实验室资源

## 用途

集中查找实验室常用的管理表格、代码仓库和硬件资源说明。

!!! warning "内部资源链接"
    下列内部表格使用占位符。只有在负责人确认链接适合公开后，才能替换为实际地址。

## 资源入口

- **实习生与访问人员管理表**：`<INTERN_VISITING_TRACKER_URL>`
- **采购与资产登记表**：`<PURCHASE_ASSET_REGISTER_URL>`
- **代码仓库**：[LV Robotics Lab repositories](https://github.com/orgs/LV-Robotics-Lab/repositories)
- **Romoya 相关资源表**：`<ROMOYA_RESOURCE_SHEET_URL>`
- **硬件资源中心**：[查看硬件资源中心](hardware.md)

!!! info "访问权限"
    部分代码仓库可能需要 LV Robotics Lab GitHub 组织权限。无法访问时，请联系对应项目的维护者。

<p class="wiki-meta">负责人：Lab Resources Maintainer · 最后核验：2026-07-31</p>
```

- [ ] **Step 3: Create the aligned English resource directory**

Create `docs/resources/index.en.md` with this exact content:

```markdown
# Lab Resources

## Purpose

Find commonly used laboratory administration sheets, code repositories, and hardware resource guidance in one place.

!!! warning "Internal resource links"
    The internal sheets below use placeholders. Replace them with actual URLs only after the maintainer confirms that publication is appropriate.

## Resource Links

- **Intern and visiting-member tracker**: `<INTERN_VISITING_TRACKER_URL>`
- **Purchase and asset register**: `<PURCHASE_ASSET_REGISTER_URL>`
- **Code repositories**: [LV Robotics Lab repositories](https://github.com/orgs/LV-Robotics-Lab/repositories)
- **Romoya resource sheet**: `<ROMOYA_RESOURCE_SHEET_URL>`
- **Hardware Resource Center**: [Open the Hardware Resource Center](hardware.md)

!!! info "Access permissions"
    Some repositories may require membership in the LV Robotics Lab GitHub organization. Contact the relevant project maintainer if access is unavailable.

<p class="wiki-meta">Owner: Lab Resources Maintainer · Last verified: 2026-07-31</p>
```

- [ ] **Step 4: Verify pairing, structure, and approved destinations**

Run:

```bash
test -f docs/resources/index.md && test -f docs/resources/index.en.md
rg -n '^# |^## |INTERN_VISITING_TRACKER_URL|PURCHASE_ASSET_REGISTER_URL|ROMOYA_RESOURCE_SHEET_URL|github.com/orgs/LV-Robotics-Lab/repositories|hardware.md' docs/resources/index.md docs/resources/index.en.md
```

Expected: both files exist; each file has one title, Purpose/用途 and resource-link sections, all three descriptive placeholders, the GitHub URL, and the local hardware link.

- [ ] **Step 5: Commit only the resource directory pair**

```bash
git add docs/resources/index.md docs/resources/index.en.md
git diff --cached --check
git commit -m "docs: add bilingual lab resource directory"
```

### Task 2: Bilingual Hardware Resource Center Status Page

**Files:**
- Create: `docs/resources/hardware.md`
- Create: `docs/resources/hardware.en.md`

**Interfaces:**
- Consumes: The local `hardware.md` links created in Task 1.
- Produces: A bilingual status page that identifies the missing reviewed content without presenting an operational guide.

- [ ] **Step 1: Verify the hardware page pair does not already exist**

Run:

```bash
test ! -e docs/resources/hardware.md && test ! -e docs/resources/hardware.en.md
```

Expected: exit status 0. If either file exists, inspect it and merge carefully instead of overwriting it.

- [ ] **Step 2: Create the Chinese status page**

Create `docs/resources/hardware.md` with this exact content:

```markdown
# 硬件资源中心

!!! warning "Requires maintainer review"
    当前来源仅提供了页面标题，尚无经过审核的硬件清单或操作说明。请勿依据本页推断设备状态、存放位置或使用权限。

## 用途

本页计划用于汇总实验室硬件资源的查找和使用说明。

## 当前状态

硬件资源内容尚待负责人审核和补充。在审核完成前，本页不提供设备库存、内部位置、访问方式或操作步骤。

## 待负责人补充

- 可公开的硬件类别和资源范围
- 获取设备或申请使用权限的流程
- 安全、预约、借用和归还规则
- 内容验证方式和故障排查信息
- 负责维护本页的角色或团队

<p class="wiki-meta">负责人：Hardware Resources Maintainer · 最后核验：2026-07-31</p>
```

- [ ] **Step 3: Create the aligned English status page**

Create `docs/resources/hardware.en.md` with this exact content:

```markdown
# Hardware Resource Center

!!! warning "Requires maintainer review"
    The supplied source contains only a page title and no reviewed inventory or operating guidance. Do not infer equipment status, storage locations, or access permissions from this page.

## Purpose

This page is intended to collect guidance for finding and using laboratory hardware resources.

## Current Status

The hardware resource content is awaiting maintainer review and completion. Until that review is complete, this page does not provide equipment inventory, internal locations, access methods, or operating procedures.

## Maintainer Input Required

- Hardware categories and resource scope that are safe to publish
- Procedure for obtaining equipment or requesting access
- Safety, reservation, borrowing, and return rules
- Verification and troubleshooting information
- Role or team responsible for maintaining this page

<p class="wiki-meta">Owner: Hardware Resources Maintainer · Last verified: 2026-07-31</p>
```

- [ ] **Step 4: Verify bilingual structure and review status**

Run:

```bash
test -f docs/resources/hardware.md && test -f docs/resources/hardware.en.md
rg -n '^# |^## |Requires maintainer review|2026-07-31' docs/resources/hardware.md docs/resources/hardware.en.md
```

Expected: both files exist, have one title and three corresponding sections, display `Requires maintainer review`, and carry the same verification date.

- [ ] **Step 5: Commit only the hardware page pair**

```bash
git add docs/resources/hardware.md docs/resources/hardware.en.md
git diff --cached --check
git commit -m "docs: add hardware resource center status page"
```

### Task 3: Navigation, Redaction Audit, and Strict Build

**Files:**
- Modify: `mkdocs.yml`
- Validate: `docs/resources/index.md`
- Validate: `docs/resources/index.en.md`
- Validate: `docs/resources/hardware.md`
- Validate: `docs/resources/hardware.en.md`

**Interfaces:**
- Consumes: The four pages created in Tasks 1 and 2 and the existing Chinese-default i18n configuration.
- Produces: A visible, bilingual Lab Resources navigation section and a strict-build-verified site.

- [ ] **Step 1: Record and preserve the existing `mkdocs.yml` changes**

Run:

```bash
git diff -- mkdocs.yml
```

Expected: review all existing user changes, especially the Lab Access navigation entries, and retain them while editing.

- [ ] **Step 2: Add the English navigation translations**

Under `plugins.i18n.languages[1].nav_translations`, add these mappings without changing the existing mappings:

```yaml
            实验室资源: Lab Resources
            资源总览: Overview
            硬件资源中心: Hardware Resource Center
```

- [ ] **Step 3: Add the Chinese-default navigation section**

After the `行政流程` section and before `如何贡献`, add:

```yaml
  - 实验室资源:
      - 资源总览: resources/index.md
      - 硬件资源中心: resources/hardware.md
```

- [ ] **Step 4: Audit changed content for forbidden source material**

Run:

```bash
if rg -n 'docs\.google\.com/spreadsheets/d/|app\.notion\.com/p/|gmail\.com|[0-9]{4}[[:space:]][0-9]{4}' docs/resources mkdocs.yml; then exit 1; else exit 0; fi
```

Expected: exit status 0 with no matches. This generic audit catches spreadsheet links, Notion links, account addresses, and backup-code-like digit groups without recording the supplied secrets in the repository or command history.

- [ ] **Step 5: Verify navigation references and bilingual file pairing**

Run:

```bash
rg -n '实验室资源|资源总览|硬件资源中心|resources/index.md|resources/hardware.md' mkdocs.yml
for page in docs/resources/index.md docs/resources/hardware.md; do test -f "${page%.md}.en.md" || exit 1; done
```

Expected: all three English translations and both Chinese navigation paths appear; both English counterparts exist.

- [ ] **Step 6: Run the full strict build**

Run:

```bash
mkdocs build --strict
```

Expected: exit status 0 and `Documentation built` in the output. The existing informational notice about unlisted `docs/superpowers/` documents is acceptable.

- [ ] **Step 7: Review the final diff and repository status**

Run:

```bash
git diff --check
git diff -- docs/resources/index.md docs/resources/index.en.md docs/resources/hardware.md docs/resources/hardware.en.md mkdocs.yml
git status --short
```

Expected: no whitespace errors; the diff contains only the approved resource pages and navigation additions for this task. Existing unrelated changes remain unstaged and preserved.

- [ ] **Step 8: Leave the navigation change unstaged for final handoff**

```bash
git diff -- mkdocs.yml
git status --short
```

Expected: `mkdocs.yml` remains modified and unstaged. Do not commit the whole file because it already contains unrelated user changes; report this explicitly in the final handoff.
