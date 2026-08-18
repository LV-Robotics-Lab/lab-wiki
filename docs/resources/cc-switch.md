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
    | Base URL | `https://kjapi.botsmart.net/v1` |
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
