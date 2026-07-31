# Hardware Resource Center Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the bilingual Hardware Resource Center placeholder with a safe operational resource guide that uses real public documentation links and descriptive placeholders for every internal or sensitive value.

**Architecture:** The existing suffix-paired Markdown pages remain the only content units. Both pages use identical heading depth and resource ordering, while inline admonitions define the security boundary: public links may be opened directly, internal links and access values must be retrieved from approved controlled systems, and real secrets must never be written into the Wiki.

**Tech Stack:** Material for MkDocs, `mkdocs-static-i18n`, Markdown

## Global Constraints

- Modify only `docs/resources/hardware.md` and `docs/resources/hardware.en.md` for the feature content.
- Keep Chinese and English section order, heading depth, resource order, placeholders, and verification date aligned.
- Use **YAM**, never **YUM**, for the i2rt arm resources.
- Publish only the approved public Gitee, WUJI, GitHub, and HigVR URLs.
- Do not publish any supplied Google Drive, Yuque, or Feishu URL.
- Do not include any supplied token, API key, password, account value, private host address, SSH target, or internal service path.
- The SSH command must be exactly `ssh <TACCLAW_USERNAME>@<TACCLAW_HOST>`.
- Real secrets must remain in an approved password manager or another access-controlled system; never replace Wiki placeholders with real values.
- Preserve unrelated working-tree changes and never stage `.venv/`, `site/`, `AGENTS.md`, `mkdocs.yml`, or onboarding files as part of this feature.
- Run `mkdocs build --strict` before completion.

---

### Task 1: Replace the Bilingual Hardware Resource Center Content

**Files:**
- Modify: `docs/resources/hardware.md`
- Modify: `docs/resources/hardware.en.md`

**Interfaces:**
- Consumes: The approved public documentation URLs and exact descriptive placeholders defined in `docs/superpowers/specs/2026-07-31-hardware-resource-center-expansion-design.md`.
- Produces: A bilingual operational resource guide linked from `docs/resources/index.md` and the existing MkDocs navigation.

- [ ] **Step 1: Run the content-presence check and confirm the current page fails it**

Run:

```bash
rg -q '^### Realhand$' docs/resources/hardware.md && rg -q '^### Realhand$' docs/resources/hardware.en.md
```

Expected: exit status 1 because the current placeholder pages do not contain the Realhand resource section.

- [ ] **Step 2: Replace the Chinese page with the approved content**

Set `docs/resources/hardware.md` to this exact content:

```markdown
# 硬件资源中心

!!! danger "不要在 Wiki 中保存真实凭据"
    本页所有尖括号字段均为占位符。真实链接、密钥、密码、账号、主机地址和内部路径只能从获批的密码管理器或其他受控系统获取，禁止将真实值回填到 Wiki。

## 用途

集中查找实验室硬件的公开文档、内部资料引用和访问配置占位符。

## 前置条件

- 确认要使用的产品、型号和任务。
- 获得对应设备、内部资料和账号的访问授权。
- 使用获批的密码管理器获取所需凭据。
- 操作设备前阅读厂商最新的安全说明和用户手册。

## 资源目录

### Realhand

- 内部资料文件夹：`<REALHAND_RESOURCE_FOLDER_URL>`
- 公开仓库：[LinkerHand teleoperation Python](https://gitee.com/ericbrunt/linkerhand_telop_python)

### AgileX

!!! warning "Requires maintainer review"
    三份 AgileX 支持资料缺少可确认的标题。负责人确认标题前，请勿推断其内容。

- 支持资料 1：`<AGILEX_SUPPORT_DOCUMENT_1_URL>`
- 支持资料 2：`<AGILEX_SUPPORT_DOCUMENT_2_URL>`
- 支持资料 3：`<AGILEX_SUPPORT_DOCUMENT_3_URL>`
- TRACER 2.0 用户手册：`<AGILEX_TRACER_2_USER_MANUAL_URL>`
- NERO 用户手册：`<AGILEX_NERO_USER_MANUAL_URL>`
- NERO CAN 协议：`<AGILEX_NERO_CAN_PROTOCOL_URL>`
- 机械臂通信协议：`<AGILEX_ARM_COMMUNICATION_PROTOCOL_URL>`

### Daimon 与 TacClaw

- 内部资料文件夹：`<DAIMON_RESOURCE_FOLDER_URL>`
- 设备访问配置：见下方“访问配置引用”。

### UDEXREAL 数据手套

- 内部文档：`<UDEXREAL_DATAGLOVES_DOCUMENT_URL>`

### WUJI

- 公开文档：[WUJI Hand 文档中心](https://docs.wuji.tech/docs/zh/wuji-hand/latest/)

### Franka

- GELLO 单臂遥操作指南：`<FRANKA_GELLO_SINGLE_ARM_GUIDE_URL>`

### YAM

- 内部资料文件夹：`<YAM_RESOURCE_FOLDER_URL>`
- 公开仓库：[i2rt Python API](https://github.com/i2rt-robotics/i2rt)

### HigVR

- 厂商手册：[HigVR User Manual](https://higvr.com/en-cn/pages/user-manual)

### LeRobot 中文教程

- 内部教程：`<LEROBOT_CHINESE_TUTORIAL_URL>`

## 访问配置引用

!!! info "占位符用途"
    下列字段只说明应从受控系统获取什么信息，不是可用凭据。不要把真实值提交到仓库。

### TacClaw

- 主机：`<TACCLAW_HOST>`
- 用户名：`<TACCLAW_USERNAME>`
- 密码引用：`<TACCLAW_PASSWORD>`
- 服务路径：`<TACCLAW_SERVICE_PATH>`
- SSH 命令模板：`ssh <TACCLAW_USERNAME>@<TACCLAW_HOST>`

### API 与服务凭据

- GitHub API token：`<GITHUB_API_TOKEN>`
- Hugging Face API token：`<HUGGINGFACE_API_TOKEN>`
- Weights & Biases API key：`<WANDB_API_KEY>`

### 实验室与设备账号

- 实验室通用密码：`<LAB_SHARED_PASSWORD>`
- MISUMI 账号 ID：`<MISUMI_ACCOUNT_ID>`
- ME Control Lab 用户名：`<ME_CONTROL_LAB_USERNAME>`
- ME Control Lab 密码：`<ME_CONTROL_LAB_PASSWORD>`
- Franka 管理员用户名：`<FRANKA_ADMIN_USERNAME>`
- Franka 管理员密码：`<FRANKA_ADMIN_PASSWORD>`
- Franka 安全员用户名：`<FRANKA_SAFETY_USERNAME>`
- Franka 安全员密码：`<FRANKA_SAFETY_PASSWORD>`

## 操作步骤

1. 确认需要使用的硬件类别和具体型号。
2. 优先打开本页列出的公开厂商文档或代码仓库。
3. 遇到内部链接占位符时，向对应维护者申请已批准的内部地址。
4. 需要凭据或设备访问时，从获批的密码管理器获取授权值；不要将其复制到 Wiki。
5. 控制硬件前，按厂商最新文档检查安全要求、连接方式和适用型号。

## 验证

- 确认打开的文档或仓库对应预期产品和型号。
- 确认内部资料与设备访问已获授权。
- 确认操作前已阅读相关安全说明。
- 确认 Wiki 中仍只有占位符，没有真实凭据或内部地址。

## 故障排查

- 占位符尚未替换时，联系对应硬件维护者获取受控资源。
- 无法打开内部资料时，检查组织成员资格和文档共享权限。
- 公开链接失效时，向维护者报告产品名称和失效页面。
- 如果凭据曾出现在文档、提交记录或聊天中，立即撤销并轮换该凭据。
- 不要通过在 Wiki 中嵌入密钥、密码或内部地址来绕过访问控制。

<p class="wiki-meta">负责人：Hardware Resources Maintainer · 最后核验：2026-07-31</p>
```

- [ ] **Step 3: Replace the English page with the aligned content**

Set `docs/resources/hardware.en.md` to this exact content:

```markdown
# Hardware Resource Center

!!! danger "Do not store real credentials in the Wiki"
    Every angle-bracketed field on this page is a placeholder. Actual links, keys, passwords, accounts, host addresses, and internal paths must be retrieved only from an approved password manager or another access-controlled system. Never replace these placeholders with real values in the Wiki.

## Purpose

Find public documentation, internal resource references, and access-configuration placeholders for laboratory hardware in one place.

## Prerequisites

- Confirm the product, model, and task you intend to use.
- Obtain authorization for the relevant device, internal resources, and accounts.
- Use the approved password manager to retrieve required credentials.
- Read the vendor's current safety information and user manual before operating equipment.

## Resource Catalog

### Realhand

- Internal resource folder: `<REALHAND_RESOURCE_FOLDER_URL>`
- Public repository: [LinkerHand teleoperation Python](https://gitee.com/ericbrunt/linkerhand_telop_python)

### AgileX

!!! warning "Requires maintainer review"
    Three AgileX support resources do not have confirmed titles. Do not infer their contents until the maintainer confirms the titles.

- Support resource 1: `<AGILEX_SUPPORT_DOCUMENT_1_URL>`
- Support resource 2: `<AGILEX_SUPPORT_DOCUMENT_2_URL>`
- Support resource 3: `<AGILEX_SUPPORT_DOCUMENT_3_URL>`
- TRACER 2.0 user manual: `<AGILEX_TRACER_2_USER_MANUAL_URL>`
- NERO user manual: `<AGILEX_NERO_USER_MANUAL_URL>`
- NERO CAN protocol: `<AGILEX_NERO_CAN_PROTOCOL_URL>`
- Robot-arm communication protocol: `<AGILEX_ARM_COMMUNICATION_PROTOCOL_URL>`

### Daimon and TacClaw

- Internal resource folder: `<DAIMON_RESOURCE_FOLDER_URL>`
- Device access configuration: see Access Configuration References below.

### UDEXREAL Data Gloves

- Internal documentation: `<UDEXREAL_DATAGLOVES_DOCUMENT_URL>`

### WUJI

- Public documentation: [WUJI Hand Documentation Center](https://docs.wuji.tech/docs/zh/wuji-hand/latest/)

### Franka

- GELLO single-arm teleoperation guide: `<FRANKA_GELLO_SINGLE_ARM_GUIDE_URL>`

### YAM

- Internal resource folder: `<YAM_RESOURCE_FOLDER_URL>`
- Public repository: [i2rt Python API](https://github.com/i2rt-robotics/i2rt)

### HigVR

- Vendor manual: [HigVR User Manual](https://higvr.com/en-cn/pages/user-manual)

### LeRobot Chinese Tutorial

- Internal tutorial: `<LEROBOT_CHINESE_TUTORIAL_URL>`

## Access Configuration References

!!! info "Placeholder purpose"
    These fields identify what information must be retrieved from a controlled system; they are not usable credentials. Do not commit real values to the repository.

### TacClaw

- Host: `<TACCLAW_HOST>`
- Username: `<TACCLAW_USERNAME>`
- Password reference: `<TACCLAW_PASSWORD>`
- Service path: `<TACCLAW_SERVICE_PATH>`
- SSH command template: `ssh <TACCLAW_USERNAME>@<TACCLAW_HOST>`

### API and Service Credentials

- GitHub API token: `<GITHUB_API_TOKEN>`
- Hugging Face API token: `<HUGGINGFACE_API_TOKEN>`
- Weights & Biases API key: `<WANDB_API_KEY>`

### Laboratory and Device Accounts

- Laboratory shared password: `<LAB_SHARED_PASSWORD>`
- MISUMI account ID: `<MISUMI_ACCOUNT_ID>`
- ME Control Lab username: `<ME_CONTROL_LAB_USERNAME>`
- ME Control Lab password: `<ME_CONTROL_LAB_PASSWORD>`
- Franka administrator username: `<FRANKA_ADMIN_USERNAME>`
- Franka administrator password: `<FRANKA_ADMIN_PASSWORD>`
- Franka safety-officer username: `<FRANKA_SAFETY_USERNAME>`
- Franka safety-officer password: `<FRANKA_SAFETY_PASSWORD>`

## Procedure

1. Identify the relevant hardware category and exact model.
2. Prefer the public vendor documentation or code repository listed on this page.
3. When a placeholder represents an internal link, request the approved destination from the relevant maintainer.
4. When credentials or device access are required, retrieve authorized values from the approved password manager; never copy them into the Wiki.
5. Before controlling hardware, use the vendor's latest documentation to check safety requirements, connection methods, and supported models.

## Verification

- Confirm that the opened documentation or repository matches the intended product and model.
- Confirm that internal-resource and device access is authorized.
- Confirm that relevant safety information was reviewed before operation.
- Confirm that the Wiki still contains placeholders only, with no real credentials or internal addresses.

## Troubleshooting

- If a placeholder is unresolved, contact the relevant hardware maintainer for the controlled resource.
- If an internal resource is unavailable, check organization membership and document-sharing permissions.
- If a public link is unavailable, report the product name and failed page to the maintainer.
- If a credential appeared in documentation, commit history, or chat, revoke and rotate it immediately.
- Never bypass access controls by embedding keys, passwords, or internal addresses in the Wiki.

<p class="wiki-meta">Owner: Hardware Resources Maintainer · Last verified: 2026-07-31</p>
```

- [ ] **Step 4: Verify bilingual structure, resource order, and required placeholders**

Run:

```bash
test "$(rg -c '^## ' docs/resources/hardware.md)" -eq 7
test "$(rg -c '^## ' docs/resources/hardware.en.md)" -eq 7
test "$(rg -c '^### ' docs/resources/hardware.md)" -eq 12
test "$(rg -c '^### ' docs/resources/hardware.en.md)" -eq 12
for value in REALHAND_RESOURCE_FOLDER_URL AGILEX_SUPPORT_DOCUMENT_1_URL AGILEX_SUPPORT_DOCUMENT_2_URL AGILEX_SUPPORT_DOCUMENT_3_URL AGILEX_TRACER_2_USER_MANUAL_URL AGILEX_NERO_USER_MANUAL_URL AGILEX_NERO_CAN_PROTOCOL_URL AGILEX_ARM_COMMUNICATION_PROTOCOL_URL DAIMON_RESOURCE_FOLDER_URL UDEXREAL_DATAGLOVES_DOCUMENT_URL FRANKA_GELLO_SINGLE_ARM_GUIDE_URL YAM_RESOURCE_FOLDER_URL LEROBOT_CHINESE_TUTORIAL_URL TACCLAW_HOST TACCLAW_USERNAME TACCLAW_PASSWORD TACCLAW_SERVICE_PATH GITHUB_API_TOKEN HUGGINGFACE_API_TOKEN WANDB_API_KEY LAB_SHARED_PASSWORD MISUMI_ACCOUNT_ID ME_CONTROL_LAB_USERNAME ME_CONTROL_LAB_PASSWORD FRANKA_ADMIN_USERNAME FRANKA_ADMIN_PASSWORD FRANKA_SAFETY_USERNAME FRANKA_SAFETY_PASSWORD; do
  rg -q "<$value>" docs/resources/hardware.md || exit 1
  rg -q "<$value>" docs/resources/hardware.en.md || exit 1
done
```

Expected: both pages have seven level-two headings, twelve level-three headings, and every exact placeholder appears in both languages.

- [ ] **Step 5: Run the silent sensitive-source audit**

Run:

```bash
if rg -q 'drive\.google\.com/drive/folders/|agilexsupport\.yuque\.com/|feishu\.cn/|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|wandb_v1_[A-Za-z0-9_]{20,}|192\.168\.[0-9]{1,3}\.[0-9]{1,3}' docs/resources/hardware.md docs/resources/hardware.en.md; then
  printf 'Sensitive-source audit failed\n'
  exit 1
fi
```

Expected: exit status 0. The command prints only a generic failure message if a forbidden source pattern is found and never prints the matching value.

- [ ] **Step 6: Verify the approved public URLs and YAM spelling**

Run:

```bash
for url in 'https://gitee.com/ericbrunt/linkerhand_telop_python' 'https://docs.wuji.tech/docs/zh/wuji-hand/latest/' 'https://github.com/i2rt-robotics/i2rt' 'https://higvr.com/en-cn/pages/user-manual'; do
  rg -Fq "$url" docs/resources/hardware.md || exit 1
  rg -Fq "$url" docs/resources/hardware.en.md || exit 1
done
if rg -q '^### YUM$|YUM_RESOURCE' docs/resources/hardware.md docs/resources/hardware.en.md; then exit 1; fi
```

Expected: all four approved public URLs occur in both pages and no YUM heading or placeholder appears.

- [ ] **Step 7: Run the strict site build**

Run:

```bash
mkdocs build --strict
```

Expected: exit status 0 and `Documentation built` in the output. Informational notices about unlisted `docs/superpowers/` documents are acceptable.

- [ ] **Step 8: Review the exact diff and repository state**

Run:

```bash
git diff --check
git diff -- docs/resources/hardware.md docs/resources/hardware.en.md
git status --short
```

Expected: no whitespace errors; the content diff contains only the approved bilingual Hardware Resource Center replacement. Existing unrelated changes remain preserved and unstaged.

- [ ] **Step 9: Commit only the bilingual hardware pages**

```bash
git add docs/resources/hardware.md docs/resources/hardware.en.md
git diff --cached --check
git commit -m "docs: expand bilingual hardware resource center"
```
