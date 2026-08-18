# CC Switch AI API Guide Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a bilingual, cross-platform CC Switch guide that configures the lab AI API for Claude Code and the lab relay for Codex from the graphical interface.

**Architecture:** Keep access policy in the existing AI API page and put tool-specific setup in a new sibling Resources page. Maintain Chinese/English structural parity, expose only approved endpoints and placeholders, and register both pages in MkDocs navigation and the machine-readable AI index.

**Tech Stack:** Material for MkDocs, mkdocs-static-i18n suffix pages, Markdown, JSON, Python `unittest`

---

### Task 1: Synchronize The AI API Access Pages

**Files:**
- Modify: `docs/resources/ai-api-access.md`
- Modify: `docs/resources/ai-api-access.en.md`

- [ ] **Step 1: Replace the local Chinese page with the current GitHub `main` content**

Apply these source-of-truth changes from `https://raw.githubusercontent.com/LV-Robotics-Lab/lab-wiki/main/docs/resources/ai-api-access.md`:

- Remove the hard-coded Base URL sentence from the opening info box.
- Change the lab AI API contact to `@赖咏曦`.
- Change the Codex relay to `https://cpa114515.somnia.ltd`.
- Remove the separate personal-key note.
- Remove the usage estimate row from the request table.
- Replace the Goal-mode rule with: `多 Agent、长时间运行和高并发任务可能快速消耗额度，启动前应评估预算并取得批准。（不要使用Goal 模式！）`
- Set the maintenance date to `2026-08-18`.

Add this sentence after the service table so the setup tutorial remains discoverable:

```markdown
需要图形化配置 Claude Code 或 Codex 时，请参阅[使用 CC Switch 配置 AI API](cc-switch.md)。
```

- [ ] **Step 2: Mirror the policy changes in English**

Use the same section order as Chinese, translate the changed service table and warning faithfully, and add:

```markdown
For graphical Claude Code or Codex setup, see [Configure AI APIs with CC Switch](cc-switch.en.md).
```

Translate the Goal-mode sentence as:

```markdown
- Multi-agent, long-running, and high-concurrency tasks can consume quota rapidly; estimate the budget and obtain approval before launch. Do not use Goal mode.
```

Set `Last verified: 2026-08-18`.

- [ ] **Step 3: Check translation structure and Markdown whitespace**

Run:

```bash
rg '^## ' docs/resources/ai-api-access.md docs/resources/ai-api-access.en.md
git diff --check
```

Expected: both pages have matching section counts; `git diff --check` exits 0.

- [ ] **Step 4: Commit the synchronized access pages**

```bash
git add docs/resources/ai-api-access.md docs/resources/ai-api-access.en.md
git commit -m "docs: sync AI API access guidance"
```

### Task 2: Add The Bilingual CC Switch Guide

**Files:**
- Create: `docs/resources/cc-switch.md`
- Create: `docs/resources/cc-switch.en.md`

- [ ] **Step 1: Create the Chinese guide**

Write the page with these exact sections and configuration values:

```markdown
# 使用 CC Switch 配置 AI API

!!! info "适用范围"
    本教程使用 CC Switch 的图形化界面管理 Claude Code 和 Codex 的实验室 API 配置，适用于 Windows、macOS 和 Linux。

!!! danger "只填写个人 key"
    每位成员必须使用自己的 API key。不要把 key 粘贴到 Wiki、代码、聊天、截图或 Git 提交中。

## 用途

通过 CC Switch 分别配置实验室 AI API 和 Codex 中转站，并在不同供应商之间切换，无需手动编辑 CLI 配置文件。

## 前置条件

- 已按[AI API 申请与使用](ai-api-access.md)获得个人 API key 和模型权限。
- 已安装需要使用的 [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) 或 [Codex CLI](https://github.com/openai/codex)。
- 已向管理员确认可用的 `<MODEL_ID>`；不要根据他人的配置猜测模型名。
- 系统满足 CC Switch 要求：Windows 10+、macOS 12+，或官方支持的主流 Linux 发行版。

## 安装 CC Switch

只从 [CC Switch 官网](https://ccswitch.io) 或 [GitHub Releases](https://github.com/farion1231/cc-switch/releases/latest) 下载。

| 系统 | 推荐方式 |
|---|---|
| Windows | 下载 `.msi`；需要免安装版本时使用 `Windows-Portable.zip` |
| macOS | 运行 `brew install --cask cc-switch`，或下载 `.dmg` |
| Debian / Ubuntu | 下载与 CPU 架构匹配的 `.deb` |
| Fedora / RHEL / openSUSE | 下载与 CPU 架构匹配的 `.rpm` |
| 其他 Linux | 下载与 CPU 架构匹配的 `.AppImage`，添加执行权限后运行 |

安装后启动 CC Switch，确认窗口和系统托盘图标正常显示。完整安装说明见[官方安装指南](https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/zh/1-getting-started/1.2-installation.md)。

## 配置 Claude Code

1. 在顶部应用切换器中选择 **Claude Code**。
2. 点击右上角的 **+**，选择**应用专属供应商**和**自定义**。
3. 填写以下字段：

    | 字段 | 值 |
    |---|---|
    | 名称 | `Lab AI API` |
    | API Key / Authentication | `<AI_API_KEY>` |
    | Base URL | `https://kjapi.botsmart.net` |
    | Model | 管理员确认的 `<MODEL_ID>` |

4. 如果界面显示认证字段选项，优先保持自定义供应商的默认值；只有管理员明确要求时才在 `ANTHROPIC_API_KEY` 与 `ANTHROPIC_AUTH_TOKEN` 之间切换。
5. 保存后，在 `Lab AI API` 卡片上点击**启用**。

CC Switch 会把选中的供应商写入 Claude Code 配置；不要再把同名变量长期写入 Shell 启动文件，否则旧的环境变量可能覆盖图形界面配置。

## 配置 Codex 中转站

1. 在顶部应用切换器中选择 **Codex**。
2. 点击右上角的 **+**，选择**应用专属供应商**和**自定义**。
3. 填写以下字段：

    | 字段 | 值 |
    |---|---|
    | 名称 | `Lab Codex Relay` |
    | API Key | `<AI_API_KEY>` |
    | Base URL | `https://cpa114515.somnia.ltd/v1` |
    | Wire API / 协议 | `Responses` |
    | Model | 管理员确认的 `<MODEL_ID>` |
    | Requires OpenAI Auth | 开启 |

4. 不要开启 **Goal mode**、本地路由映射或协议转换；实验室中转站使用原生 Responses 配置。
5. 保存后，在 `Lab Codex Relay` 卡片上点击**启用**。
6. 关闭所有正在运行的 Codex 进程并重新打开终端，使新配置生效。

!!! note "为什么 Base URL 带 `/v1`"
    Codex 的自定义供应商需要 API 根路径。登录网页地址用于账户管理，CLI 配置应使用 `https://cpa114515.somnia.ltd/v1`。

## 验证

1. 新建一个不包含研究数据的空目录。
2. 启动 `claude` 或 `codex`，发送“只回复 OK”之类的最小测试。
3. 确认请求成功，并请管理员在需要时核对个人用量记录。
4. 测试完成后检查终端、截图和 Git 状态，确认未显示或写入 API key。

## 故障排查

| 现象 | 处理方式 |
|---|---|
| `401` 或 `403` | 重新输入个人 key，并联系管理员确认账户权限；不要发送 key 截图 |
| `404` 或协议错误 | Codex 检查 Base URL 是否包含 `/v1`、协议是否为 `Responses`；Claude Code 确认没有误用 Codex 中转站 |
| 模型不可用 | 使用管理员确认的模型 ID，不要照抄他人的模型名 |
| 切换后仍连接旧服务 | 完全退出 CLI；Codex 还需要重新打开终端 |
| CC Switch 提示环境变量冲突 | 删除或临时取消 Shell、PowerShell 用户环境中的旧 API Base URL，再重启终端 |
| 用量异常 | 立即停用供应商，联系管理员吊销并轮换 key |

## 维护信息

- 负责人：`@赖咏曦`
- CC Switch：[官网](https://ccswitch.io) · [源代码与版本发布](https://github.com/farion1231/cc-switch) · [供应商配置手册](https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/zh/2-providers/2.1-add.md)
- AI API：`https://kjapi.botsmart.net`
- Codex 中转站：`https://cpa114515.somnia.ltd`
- 最后核验：2026-08-18
```

- [ ] **Step 2: Create the English guide with structural parity**

Write this matching page:

```markdown
# Configure AI APIs with CC Switch

!!! info "Scope"
    This guide uses the CC Switch graphical interface to manage the lab API configuration for Claude Code and Codex on Windows, macOS, and Linux.

!!! danger "Enter only your personal key"
    Every member must use their own API key. Never paste a key into the Wiki, source code, chat, screenshots, or Git commits.

## Purpose

Configure the lab AI API and Codex relay as separate CC Switch providers, then switch between providers without manually editing CLI configuration files.

## Prerequisites

- You have received a personal API key and model permissions through [AI API Access and Usage](ai-api-access.en.md).
- You have installed the required [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) or [Codex CLI](https://github.com/openai/codex).
- You have confirmed the available `<MODEL_ID>` with the administrator; do not guess a model name from another person's configuration.
- Your system meets the CC Switch requirements: Windows 10+, macOS 12+, or a supported mainstream Linux distribution.

## Install CC Switch

Download CC Switch only from the [official website](https://ccswitch.io) or [GitHub Releases](https://github.com/farion1231/cc-switch/releases/latest).

| System | Recommended method |
|---|---|
| Windows | Download the `.msi`; use `Windows-Portable.zip` if you need a portable build |
| macOS | Run `brew install --cask cc-switch`, or download the `.dmg` |
| Debian / Ubuntu | Download the `.deb` matching your CPU architecture |
| Fedora / RHEL / openSUSE | Download the `.rpm` matching your CPU architecture |
| Other Linux | Download the `.AppImage` matching your CPU architecture, make it executable, and run it |

After installation, start CC Switch and confirm that its window and system-tray icon appear. See the [official installation guide](https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/1-getting-started/1.2-installation.md) for full details.

## Configure Claude Code

1. Select **Claude Code** in the application switcher at the top.
2. Click **+** in the upper-right corner, then select **App-specific provider** and **Custom**.
3. Enter these fields:

    | Field | Value |
    |---|---|
    | Name | `Lab AI API` |
    | API Key / Authentication | `<AI_API_KEY>` |
    | Base URL | `https://kjapi.botsmart.net` |
    | Model | The administrator-confirmed `<MODEL_ID>` |

4. If the form displays an authentication-field selector, keep the custom provider default. Switch between `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` only when the administrator explicitly instructs you to do so.
5. Save the provider, then click **Enable** on the `Lab AI API` card.

CC Switch writes the selected provider into the Claude Code configuration. Do not also keep the same variables in a shell startup file, because stale environment variables may override the graphical configuration.

## Configure The Codex Relay

1. Select **Codex** in the application switcher at the top.
2. Click **+** in the upper-right corner, then select **App-specific provider** and **Custom**.
3. Enter these fields:

    | Field | Value |
    |---|---|
    | Name | `Lab Codex Relay` |
    | API Key | `<AI_API_KEY>` |
    | Base URL | `https://cpa114515.somnia.ltd/v1` |
    | Wire API / Protocol | `Responses` |
    | Model | The administrator-confirmed `<MODEL_ID>` |
    | Requires OpenAI Auth | On |

4. Do not enable **Goal mode**, local routing, or protocol conversion; the lab relay uses a native Responses configuration.
5. Save the provider, then click **Enable** on the `Lab Codex Relay` card.
6. Close every running Codex process and reopen the terminal so the new configuration takes effect.

!!! note "Why the Base URL includes `/v1`"
    A custom Codex provider needs the API root path. The login-page address is for account management; the CLI configuration must use `https://cpa114515.somnia.ltd/v1`.

## Verification

1. Create an empty directory that contains no research data.
2. Start `claude` or `codex` and send a minimal test such as “Reply only with OK.”
3. Confirm that the request succeeds, and ask the administrator to check the personal usage record when necessary.
4. After the test, inspect the terminal, screenshots, and Git status to confirm that no API key was displayed or written.

## Troubleshooting

| Symptom | Action |
|---|---|
| `401` or `403` | Re-enter your personal key and ask the administrator to verify account permissions; do not send a key screenshot |
| `404` or protocol error | For Codex, check that the Base URL includes `/v1` and the protocol is `Responses`; for Claude Code, confirm that you did not use the Codex relay |
| Model unavailable | Use the administrator-confirmed model ID; do not copy another person's model name |
| The CLI still uses the old service | Exit the CLI completely; for Codex, also reopen the terminal |
| CC Switch reports an environment-variable conflict | Remove or temporarily unset stale API Base URL variables from the shell or PowerShell user environment, then restart the terminal |
| Unexpected usage | Disable the provider immediately and ask the administrator to revoke and rotate the key |

## Maintenance

- Owner: `@赖咏曦` (Yongxi Lai)
- CC Switch: [official website](https://ccswitch.io) · [source and releases](https://github.com/farion1231/cc-switch) · [provider setup manual](https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/2-providers/2.1-add.md)
- AI API: `https://kjapi.botsmart.net`
- Codex relay: `https://cpa114515.somnia.ltd`
- Last verified: 2026-08-18
```

- [ ] **Step 3: Check safety and structural parity**

Run:

```bash
rg -n 'sk-|Bearer |x-api-key|ANTHROPIC_AUTH_TOKEN=' docs/resources/cc-switch*.md
rg '^## ' docs/resources/cc-switch.md docs/resources/cc-switch.en.md
git diff --check
```

Expected: the secret-pattern search returns no matches; both pages have the same eight H2 sections; whitespace check exits 0.

- [ ] **Step 4: Commit the guide pages**

```bash
git add docs/resources/cc-switch.md docs/resources/cc-switch.en.md
git commit -m "docs: add CC Switch API setup guide"
```

### Task 3: Register Navigation And Discovery Metadata

**Files:**
- Modify: `mkdocs.yml`
- Modify: `docs/resources/index.md`
- Modify: `docs/resources/index.en.md`
- Modify: `docs/assets/data/ai-index.json`

- [ ] **Step 1: Add the bilingual navigation item**

Add this navigation entry directly after `AI API 申请与使用`:

```yaml
      - 使用 CC Switch 配置 AI API: resources/cc-switch.md
```

Add this `nav_translations` entry:

```yaml
            使用 CC Switch 配置 AI API: Configure AI APIs with CC Switch
```

- [ ] **Step 2: Add Resources index links and refresh their dates**

After the AI API list item, add:

```markdown
- **CC Switch**：[通过图形界面配置 Claude Code 和 Codex API](cc-switch.md)
```

and:

```markdown
- **CC Switch**: [Configure Claude Code and Codex APIs from a graphical interface](cc-switch.en.md)
```

Set both Resources index metadata dates to `2026-08-18`.

- [ ] **Step 3: Update AI index records**

Set `generated_at` to `2026-08-18T00:00:00Z`. Update the Resources index and AI API records to `last_verified: 2026-08-18`, then insert these reciprocal records after the AI API entries:

```json
{
  "id": "resources/cc-switch:zh",
  "language": "zh",
  "title": "使用 CC Switch 配置 AI API",
  "url": "https://lv-robotics-lab.github.io/lab-wiki/resources/cc-switch/",
  "alternate_url": "https://lv-robotics-lab.github.io/lab-wiki/en/resources/cc-switch/",
  "source_path": "docs/resources/cc-switch.md",
  "summary": "使用 CC Switch 图形界面配置 Claude Code 和 Codex 的实验室 API。",
  "keywords": ["CC Switch", "Claude Code", "Codex", "API", "中转站"],
  "maintainer_ids": ["yongxi-lai"],
  "last_verified": "2026-08-18"
},
{
  "id": "resources/cc-switch:en",
  "language": "en",
  "title": "Configure AI APIs with CC Switch",
  "url": "https://lv-robotics-lab.github.io/lab-wiki/en/resources/cc-switch/",
  "alternate_url": "https://lv-robotics-lab.github.io/lab-wiki/resources/cc-switch/",
  "source_path": "docs/resources/cc-switch.en.md",
  "summary": "Configure the lab APIs for Claude Code and Codex through the CC Switch graphical interface.",
  "keywords": ["CC Switch", "Claude Code", "Codex", "API", "relay"],
  "maintainer_ids": ["yongxi-lai"],
  "last_verified": "2026-08-18"
}
```

- [ ] **Step 4: Validate the index**

Run:

```bash
python scripts/validate_ai_index.py
```

Expected: `AI index validation passed: docs/assets/data/ai-index.json`.

- [ ] **Step 5: Commit navigation and discovery updates**

```bash
git add mkdocs.yml docs/resources/index.md docs/resources/index.en.md docs/assets/data/ai-index.json
git commit -m "docs: register CC Switch guide"
```

### Task 4: Verify The Published Documentation

**Files:**
- Verify: `docs/resources/ai-api-access.md`
- Verify: `docs/resources/ai-api-access.en.md`
- Verify: `docs/resources/cc-switch.md`
- Verify: `docs/resources/cc-switch.en.md`
- Verify: `mkdocs.yml`
- Verify: `docs/assets/data/ai-index.json`

- [ ] **Step 1: Run repository tests**

```bash
python -m unittest discover -s tests -v
```

Expected: all tests pass.

- [ ] **Step 2: Run the strict site build**

```bash
mkdocs build --strict
```

Expected: build exits 0 without warnings.

- [ ] **Step 3: Review the complete diff and worktree**

```bash
git diff HEAD~3 --check
git diff HEAD~3 --stat
git status --short
```

Expected: no whitespace errors, only the planned documentation/navigation/index files changed, and the worktree is clean.
