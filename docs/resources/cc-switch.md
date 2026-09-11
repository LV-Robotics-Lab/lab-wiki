# 使用 CC Switch 配置实验室自有 OpenRouter

!!! info "给 Agent 的 Runbook"
    本页的主要读者是执行配置任务的 Agent。成员只需要提供操作系统、目标客户端和维护者发放的端点信息，并在本机凭据字段中亲自输入个人 key。

!!! danger "Agent 不接收凭据"
    Agent 不得要求用户把 API key、密码、Cookie 或完整认证头粘贴到聊天、终端输出、截图或 Git。遇到登录、密码或权限提示时，将界面交还用户完成。

## Agent 执行契约

按以下顺序执行，不能跳过判断直接复制配置：

1. 识别 Windows、macOS、原生 Linux 或 Windows 主机 + WSL 的真实拓扑。
2. 确认目标是 Claude Code、Claude Desktop，还是两者都需要；两者配置不共享。
3. 从维护者提供的信息中区分管理地址、Anthropic Messages 端点和 OpenAI 端点。
4. 保留 CC Switch 中无关的现有供应商；只新增或更新 `Lab Self-hosted OpenRouter`。
5. 让用户在 CC Switch 或获批的本地凭据字段中输入 key，Agent 不读取、不复述。
6. 使用本页的模型和思考强度白名单。
7. 先检查配置，再进行真实最小推理；只查看 `/models` 不算验证完成。
8. 客户端配置正确但出现服务端调度故障时，停止重装并转给维护者。

## 必需输入

| 输入 | 来源 | 用途 |
|---|---|---|
| 操作系统和运行拓扑 | Agent 检测并由用户确认 | 选择 Windows、macOS、Linux 或 WSL 分支 |
| 目标客户端 | 用户 | Claude Code、Claude Desktop 或两者 |
| `<LAB_OPENROUTER_ADMIN_URL>` | 维护者 | 仅供维护者管理；普通配置流程不打开 |
| `<LAB_OPENROUTER_ANTHROPIC_BASE_URL>` | 维护者 | Claude Code 的 Anthropic Messages 端点 |
| `<LAB_OPENROUTER_OPENAI_BASE_URL>` | 维护者 | OpenAI 兼容客户端使用，不得替代 Messages 端点 |
| `<LAB_OPENROUTER_API_KEY>` | 用户本地输入 | 个人认证；不得发送给 Agent |
| `<LOCAL_CLAUDE_GATEWAY_URL>` | Agent 检测或本机维护者提供 | Claude Desktop 需要兼容适配时使用 |

## 平台与部署拓扑判断

```text
CC Switch 在哪里运行？
├─ Windows，Claude 也在 Windows -> Windows 分支
├─ macOS，Claude 也在 macOS -> macOS 分支
├─ Linux 桌面，Claude 也在 Linux -> Linux 分支
└─ CC Switch 在 Windows，Claude Code 在 WSL -> WSL 分支
```

不要根据终端外观猜测。Agent 应检查操作系统和 Claude 可执行文件所在环境，并向用户报告选中的分支。Windows CC Switch 成功启用供应商，不自动证明 WSL 内的 Claude Code 已读取同一配置。

## 安装 CC Switch

只从 [CC Switch 官网](https://ccswitch.io) 或 [GitHub Releases](https://github.com/farion1231/cc-switch/releases/latest) 获取安装包。

### Windows

1. 使用 `.msi` 安装；需要免安装版本时使用 `Windows-Portable.zip`。
2. 启动 CC Switch，确认窗口和托盘图标存在。
3. Agent 可以检查版本和窗口状态，但安装确认、管理员权限和安全提示由用户处理。
4. 修改供应商后完全退出旧 Claude 进程，再重新打开目标客户端。

### macOS

1. 使用 `brew install --cask cc-switch`，或从官方发布页安装 `.dmg`。
2. 首次启动若出现系统安全确认，由用户处理。
3. 修改供应商后退出并重新打开 CC Switch 与 Claude。
4. 检查 `~/.zshrc`、`~/.bashrc` 和启动服务中是否残留旧的 Claude Base URL；只报告变量是否存在，不打印值。

### Linux

1. Debian/Ubuntu 使用与架构匹配的 `.deb`；Fedora/RHEL/openSUSE 使用 `.rpm`；其他发行版使用 `.AppImage`。
2. 确认 CC Switch 和 Claude Code 由同一用户运行，且配置目录可写。
3. 修改供应商后重新启动终端会话和 Claude Code。
4. 检查 Shell 配置与用户服务是否覆盖 CC Switch 写入的环境变量，但不显示密钥值。

### WSL

1. 分别记录 CC Switch 所在的 Windows 主机和 Claude Code 所在的 WSL 发行版。
2. 先在 Windows CC Switch 中建立供应商，再检查 WSL 中 Claude Code 实际读取的配置路径和环境变量。
3. 不把 Windows 路径、计划任务或回环地址直接照搬成 Linux 路径；先验证 WSL 是否能访问目标地址。
4. 如果只在 WSL 运行 Claude Code，不需要修改 Claude Desktop 配置。
5. 修改后关闭旧 WSL Shell，重新打开并执行最小验证。

完整安装细节见 [CC Switch 官方安装指南](https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/zh/1-getting-started/1.2-installation.md)。

## 配置 Claude Code

1. 在 CC Switch 顶部选择 **Claude Code**。
2. 点击 **+**，选择**应用专属供应商**和**自定义**。
3. 填写：

    | 字段 | 值 |
    |---|---|
    | 名称 | `Lab Self-hosted OpenRouter` |
    | API Key / Authentication | `<LAB_OPENROUTER_API_KEY>`，由用户本地输入 |
    | Base URL | `<LAB_OPENROUTER_ANTHROPIC_BASE_URL>` |
    | 默认模型 | `claude-sonnet-5` |
    | 默认思考强度 | `medium` |

4. 只有维护者明确要求时才在 `ANTHROPIC_API_KEY` 与 `ANTHROPIC_AUTH_TOKEN` 之间切换认证字段。
5. 保存并启用供应商。
6. 检查生成配置中的非敏感 Base URL、模型和供应商名；不要输出认证字段的值。
7. 删除或临时取消会覆盖该供应商的旧 Base URL 环境变量，然后重新打开 Claude Code。

不要把 `<LAB_OPENROUTER_OPENAI_BASE_URL>` 填入 Claude Code 的 Anthropic Messages 配置。Codex 的 OpenAI `Responses` 配置见 [Codex CLI 多 Profile 与订阅登录](codex-cli.md)。

## 配置 Claude Desktop

Claude Desktop 的自定义推理网关配置与 Claude Code 独立。不要因为 CC Switch 中 Claude Code 已成功就跳过本节。

1. 先确认 Desktop 是否可以直接使用 `<LAB_OPENROUTER_ANTHROPIC_BASE_URL>`；如果 Desktop 还会调用中转站不支持的辅助路由，使用经过审核的本地兼容适配器。
2. Desktop 推理 Profile 至少包含以下非秘密字段；真实 key 由用户在本机填写：

    ```json
    {
      "inferenceProvider": "gateway",
      "inferenceGatewayBaseUrl": "<LOCAL_CLAUDE_GATEWAY_URL>",
      "inferenceGatewayAuthScheme": "bearer",
      "inferenceGatewayApiKey": "<LAB_OPENROUTER_API_KEY>",
      "inferenceModels": [
        "claude-sonnet-5",
        "claude-sonnet-4-6",
        "claude-opus-5",
        "claude-opus-4-8",
        "claude-opus-4-7",
        "claude-fable-5"
      ]
    }
    ```

3. 本地适配器必须转发 Messages 调用，并对 Desktop 的 token-count 请求提供兼容处理；远端 `/count_tokens` 缺失不应导致本地账号被永久判定为无效。
4. 持久运行使用每用户机制：Windows 使用登录时启动并可自动重试的用户任务，macOS 使用 LaunchAgent，原生 Linux 优先使用 systemd 用户服务。不要在未经批准时创建系统级服务。
5. 重启 Desktop 后确认模型选择器只显示获批模型，并执行真实最小对话。

## 模型白名单

| 优先级 | 模型 ID | 使用策略 |
|---|---|---|
| 默认 | `claude-sonnet-5` | 日常编码和 Agent 任务 |
| 兼容回退 | `claude-sonnet-4-6` | Sonnet 5 不可用或不兼容时 |
| 强推理 | `claude-opus-5` | 高难度任务的首选升级 |
| Opus 回退 | `claude-opus-4-8` | Opus 5 不可用时 |
| Opus 回退 | `claude-opus-4-7` | 进一步兼容回退 |
| 长程专用 | `claude-fable-5` | 只有任务确实需要且预算允许时 |

Agent 不得根据 `/models` 输出自行加入其他模型，也不得使用浮动模型别名绕过白名单。

## 思考强度策略

| 强度 | 是否允许 | 使用条件 |
|---|---|---|
| `low` | 允许 | 提取、格式化、重复性任务 |
| `medium` | 允许，默认 | 日常编码和一般 Agent 工作 |
| `high` | 允许 | 困难调试、多步推理或高风险修改 |
| `xhigh` | 允许，最高 | `high` 不足或任务确实异常复杂；界面可显示为 Extra High |
| `max` | 禁止 | 超出实验室配置上限 |
| `ultra` | 禁止 | 超出实验室配置上限 |

质量允许时，先降低思考强度或改用 Sonnet，再升级到更昂贵的模型。任何未列出的强度都视为未批准。

## 验证

- [ ] CC Switch 显示 `Lab Self-hosted OpenRouter` 已启用。
- [ ] 生成配置中的 Base URL、模型和协议正确，检查过程未打印 key。
- [ ] 没有旧环境变量覆盖 CC Switch 配置。
- [ ] 端点支持时，`/models` 能发现目标模型；该结果只用于发现。
- [ ] 对所选模型发送不含研究数据的 `Reply OK` 最小请求并获得成功响应。
- [ ] Claude Desktop 同时通过 `/count_tokens` 和 Messages 流程。
- [ ] 终端、日志、截图和 Git 状态中没有凭据。

## 故障排查决策树

| 现象 | 归属 | Agent 动作 |
|---|---|---|
| `401` 或 `403` | 本地凭据或账号权限 | 只检查凭据是否存在；不显示值。仍失败则联系维护者 |
| Messages 路由 `404` | 协议或 Base URL | 确认使用 Anthropic Messages 端点，而不是 OpenAI 端点或管理地址 |
| `/count_tokens` 返回 `404` | Desktop 兼容层 | 检查本地适配器的 token-count 兼容处理；不要判定 key 无效 |
| `429` | 配额或并发 | 降低并发并暂停非必要调用；申请额度复核 |
| `503 No available accounts` | 服务端调度 | 停止客户端重装；维护者检查账号健康和可调度状态 |
| `/models` 成功但推理失败 | 模型映射或账号组 | 记录模型、时间和请求 ID；维护者执行最小推理并检查账号组资格 |
| 上游错误后账号反复停用 | 服务端错误隔离 | 维护者检查健康状态、调度开关和 Pool Mode；普通成员不得修改 |
| `<LOCAL_CLAUDE_GATEWAY_URL>` 无法连接 | 本机适配器 | 检查用户级启动机制、监听状态和进程自动恢复，再处理远端账号池 |

Pool Mode、账号分组、上游账号启停和模型映射都是维护者操作。公开 Runbook 只定义诊断边界，不提供管理员凭据或特权控制台的逐步操作。

## 维护信息

- 负责人：Lab Resources Maintainer、`@赖咏曦`
- CC Switch：[官网](https://ccswitch.io) · [源代码与版本发布](https://github.com/farion1231/cc-switch) · [供应商配置手册](https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/zh/2-providers/2.1-add.md)
- 平台与凭据申请：[AI API 申请与使用](ai-api-access.md)
- 最后核验：2026-09-11
