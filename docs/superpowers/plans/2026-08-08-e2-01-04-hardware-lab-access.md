# E2-01-04 Hardware Lab Access Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a bilingual E2-01-04 hardware-lab access guide with browser-readable training, application, and risk-assessment information plus sanitized editable form downloads.

**Architecture:** Add one suffix-paired Markdown guide under Onboarding and two sanitized static form assets under a location-specific assets directory. MkDocs serves the Markdown as the browser view and copies the Office documents unchanged as direct downloads; the existing COM2-0106 guide remains a separate navigation item.

**Tech Stack:** Material for MkDocs, `mkdocs-static-i18n`, Markdown, Python standard-library ZIP/XML processing for DOCX sanitization, fixed-width UTF-16LE replacement for the legacy DOC file

---

## File Map

- Create `docs/onboarding/hardware-lab-access.md`: Chinese operational guide and risk reference.
- Create `docs/onboarding/hardware-lab-access.en.md`: English page with matching structure.
- Create `docs/assets/forms/e2-01-04/user-registration-form-sanitized.doc`: sanitized editable registration form.
- Create `docs/assets/forms/e2-01-04/risk-assessment-form-sanitized.docx`: sanitized editable risk assessment retaining project hazards and controls.
- Modify `mkdocs.yml`: add aligned Chinese/English navigation labels.

The source email PDF is not copied into the repository. Its course list and five-step process are represented by the Markdown pages.

### Task 1: Produce Sanitized Downloadable Forms

**Files:**
- Read only: `/mnt/d/Desktop/User Registration Form_Control.doc`
- Read only: `/mnt/d/Desktop/Risk Assessment Form_Jun2026_Control 5x5.docx`
- Create: `docs/assets/forms/e2-01-04/user-registration-form-sanitized.doc`
- Create: `docs/assets/forms/e2-01-04/risk-assessment-form-sanitized.docx`

- [ ] **Step 1: Verify the sanitized outputs do not exist yet**

Run:

```bash
test ! -e docs/assets/forms/e2-01-04/user-registration-form-sanitized.doc
test ! -e docs/assets/forms/e2-01-04/risk-assessment-form-sanitized.docx
```

Expected: exit status 0.

- [ ] **Step 2: Create the legacy DOC download with fixed-width redaction**

Use a transient script outside the repository to copy the source and replace every UTF-16LE occurrence of the applicant name, matriculation number, supervisor name, phone number, personal email, emergency-contact values, attachment dates, training dates, and declaration name. Each replacement must have the same encoded length as its source so the OLE document offsets remain valid. Replace source-specific WPS user metadata with equal-length neutral values as well.

Do not place the confidential replacement mapping in this plan or in any repository file. The output must retain the form headings, empty fields, safety-training checklist, laboratory rules, and declaration text.

- [ ] **Step 3: Create the DOCX download with XML-aware redaction**

Use Python's `zipfile` and `xml.etree.ElementTree` modules in a transient script. Copy every ZIP member while rewriting text and metadata XML members to:

- Replace applicant and supervisor names with `<APPLICANT_NAME>` and `<SUPERVISOR_NAME>`.
- Replace review, approval, and signature dates with `<DATE>`.
- Replace all `Action By` applicant names with `<APPLICANT_NAME>`.
- Replace `dc:creator` and `cp:lastModifiedBy` with `LV Robotics Lab`.
- Clear source-specific WPS custom identifiers.

Retain E2-01-04, the Control & Mechatronics laboratory name, all activity sequences, all fourteen risk rows, the risk matrix, hazards, consequences, ratings, controls, deadlines expressed as workflow timing, and role/designation text.

- [ ] **Step 4: Verify file formats and archive integrity**

Run:

```bash
file docs/assets/forms/e2-01-04/user-registration-form-sanitized.doc
file docs/assets/forms/e2-01-04/risk-assessment-form-sanitized.docx
unzip -t docs/assets/forms/e2-01-04/risk-assessment-form-sanitized.docx
```

Expected: the first file is a Composite Document File V2 Word document, the second is a Microsoft Word 2007+ document, and `unzip -t` reports no errors.

- [ ] **Step 5: Run the non-disclosing personal-data audit**

Scan the DOC with `strings -el`, scan all DOCX XML with `unzip -p`, and test for every known original personal identifier without printing matches. If any identifier remains, print only `Sanitized attachment audit failed` and exit 1.

Expected: exit status 0 and no output.

- [ ] **Step 6: Verify retained operational content**

Confirm that the sanitized files still contain `USER REGISTRATION`, `OSHGEN01`, `GUIDELINES FOR APPROPRIATE USE OF LABORATORY FACILITIES`, `E2-01-04`, `Franka Research 3 Robot Operation`, `Aloha Robot Experiment`, `Dexterous Hand Hardware Setup`, and `Risk Assessment Matrix`.

Expected: every marker is present in the relevant output.

### Task 2: Add the Bilingual Browser View

**Files:**
- Create: `docs/onboarding/hardware-lab-access.md`
- Create: `docs/onboarding/hardware-lab-access.en.md`

- [ ] **Step 1: Run a failing page-presence check**

Run:

```bash
test -f docs/onboarding/hardware-lab-access.md
test -f docs/onboarding/hardware-lab-access.en.md
```

Expected before implementation: the first command exits 1.

- [ ] **Step 2: Create the Chinese guide**

Write the page with this exact section order:

```markdown
# E2-01-04 硬件实验室准入
## 用途
## 申请前准备
## 必修安全培训
## 申请流程
## 表格下载与浏览
### 用户注册表
### 风险评估表
## 风险评估参考
### 活动顺序
### 风险与控制措施
### 风险矩阵
## 验证
## 故障排查
```

The training table must include OSHGEN01, OSHGEN02, OSHGEN03, OSHGEN06, OSHERGO02, and OSHFS01; identify OSHGEN03 and OSHFS01 as staff-only; link Canvas courses to `https://www.nus.edu.sg/canvas/login/`; and retain the supplied Panopto risk-assessment overview link.

The five-step process must state: complete training; complete both forms; export completed forms to PDF and email both PDFs plus a photo to the functional Control Lab mailbox; attend the emailed 20-minute lab safety orientation; wait for emailed access activation.

Link both sanitized attachments with relative paths. Warn users not to commit completed forms to the Wiki. Summarize every source risk row under Aloha, Franka Research 3, and dexterous-hand work with task, hazard, consequence, existing/new controls, initial risk, residual risk, and timing. End with owner `Onboarding Maintainer` and last verified `2026-08-08`.

- [ ] **Step 3: Create the aligned English guide**

Use the same heading levels, table ordering, course ordering, process ordering, form links, risk-row ordering, warnings, owner, and verification date as the Chinese page. Preserve official English course, form, laboratory, hazard, and control names where they come from the source.

- [ ] **Step 4: Verify bilingual structure and required content**

Run:

```bash
test "$(rg -c '^## ' docs/onboarding/hardware-lab-access.md)" -eq "$(rg -c '^## ' docs/onboarding/hardware-lab-access.en.md)"
test "$(rg -c '^### ' docs/onboarding/hardware-lab-access.md)" -eq "$(rg -c '^### ' docs/onboarding/hardware-lab-access.en.md)"
for code in OSHGEN01 OSHGEN02 OSHGEN03 OSHGEN06 OSHERGO02 OSHFS01; do
  rg -q "$code" docs/onboarding/hardware-lab-access.md
  rg -q "$code" docs/onboarding/hardware-lab-access.en.md
done
rg -q 'E2-01-04' docs/onboarding/hardware-lab-access.md
rg -q 'E2-01-04' docs/onboarding/hardware-lab-access.en.md
```

Expected: exit status 0 for every check.

### Task 3: Add Distinct Navigation

**Files:**
- Modify: `mkdocs.yml`

- [ ] **Step 1: Run the failing navigation check**

Run:

```bash
rg -q 'E2-01-04 硬件实验室: onboarding/hardware-lab-access.md' mkdocs.yml
```

Expected before implementation: exit status 1.

- [ ] **Step 2: Add aligned navigation labels**

Add `E2-01-04 硬件实验室: E2-01-04 Hardware Lab` under `nav_translations`, then add `- E2-01-04 硬件实验室: onboarding/hardware-lab-access.md` immediately after the existing COM2-0106 lab-access item. Do not rename or edit the existing `实验室门禁: onboarding/lab-access.md` entry.

- [ ] **Step 3: Verify both locations remain present**

Run:

```bash
rg -q '实验室门禁: onboarding/lab-access.md' mkdocs.yml
rg -q 'E2-01-04 硬件实验室: onboarding/hardware-lab-access.md' mkdocs.yml
rg -q 'COM2-0106' docs/onboarding/lab-access.md docs/onboarding/lab-access.en.md
```

Expected: all checks pass.

### Task 4: Validate Privacy, Links, And Site Build

**Files:**
- Verify: `docs/onboarding/hardware-lab-access.md`
- Verify: `docs/onboarding/hardware-lab-access.en.md`
- Verify: `docs/assets/forms/e2-01-04/user-registration-form-sanitized.doc`
- Verify: `docs/assets/forms/e2-01-04/risk-assessment-form-sanitized.docx`
- Verify: `mkdocs.yml`

- [ ] **Step 1: Verify local attachment targets**

Extract relative Markdown links from both new pages, resolve links beginning with `../assets/` against each page directory, and exit nonzero if any target is absent.

Expected: both pages resolve both sanitized form links.

- [ ] **Step 2: Run the repository privacy audit**

Scan only the new pages, new attachments, navigation, and implementation documentation for known applicant identifiers. The check must not print matching contents; on failure it prints only `Privacy audit failed`.

Expected: exit status 0.

- [ ] **Step 3: Run the strict site build**

Run:

```bash
mkdocs build --strict
```

Expected: exit status 0 and `Documentation built` in the output. Informational notices about unlisted `docs/superpowers/` files are acceptable.

- [ ] **Step 4: Review the final diff**

Run:

```bash
git diff --check
git status --short
git diff --stat
```

Expected: no whitespace errors; only the approved pages, attachments, navigation, and implementation plan are changed.

- [ ] **Step 5: Commit the implementation**

```bash
git add mkdocs.yml docs/onboarding/hardware-lab-access.md docs/onboarding/hardware-lab-access.en.md docs/assets/forms/e2-01-04/user-registration-form-sanitized.doc docs/assets/forms/e2-01-04/risk-assessment-form-sanitized.docx docs/superpowers/plans/2026-08-08-e2-01-04-hardware-lab-access.md
git commit -m "docs: add E2-01-04 hardware lab access guide"
```
