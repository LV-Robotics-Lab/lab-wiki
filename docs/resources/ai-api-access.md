# AI API 申请与使用

!!! info "使用 API 前请确认"
    请使用个人获批的 API key，切勿在 Wiki、代码或聊天中粘贴凭据。

!!! danger "地址与凭据边界"
    只有经过 Wiki 维护者批准的公开服务地址可以写入页面。API key、访问 token、密码、Cookie、请求头、内网地址、账号池身份和个人用量明细一律不得公开。

## 用途

为已获批准的实验室科研项目申请和使用实验室管理的 AI API，并让 Agent 能够区分不同协议、端点和故障责任边界。

## 当前服务入口

| 服务 | 地址 | 申请或咨询 |
|---|---|---|
| 实验室 AI API | [https://kjapi.botsmart.net](https://kjapi.botsmart.net) | `@赖咏曦` |
| 实验室 Codex 中转站 | [https://cpa114515.somnia.ltd](https://cpa114515.somnia.ltd) | `@赖咏曦` |
| 实验室自有 OpenRouter | 由维护者通过安全渠道提供，不在公开 Wiki 写入部署地址 | Lab Resources Maintainer |

配置 Claude Code 或 Claude Desktop 时，Agent 必须继续读取[使用 CC Switch 配置实验室自有 OpenRouter](cc-switch.md)，不得仅凭本页猜测客户端字段。

## 实验室自有 OpenRouter

实验室自有 OpenRouter 是独立部署的 AI 推理路由平台。它可以管理多个协议入口、模型映射、可调度账号组和经审计的上游账号。平台名称不代表所有入口都兼容 Claude：客户端必须选择与其协议匹配的推理端点。

### 调用链路

```text
Claude Code / Claude Desktop
  -> CC Switch 管理的供应商配置
  -> Anthropic Messages 兼容端点
  -> 可选的本地兼容适配器
  -> 可调度账号组
  -> 经审计的 Anthropic 上游
```

### 端点边界

| 值 | 用途 | Agent 规则 |
|---|---|---|
| `<LAB_OPENROUTER_ADMIN_URL>` | 管理控制台 | 只供维护者管理账号组，不得作为客户端 Base URL |
| `<LAB_OPENROUTER_ANTHROPIC_BASE_URL>` | Anthropic Messages 推理入口 | 用于 Claude Code；具体尾部路径以维护者提供值为准 |
| `<LAB_OPENROUTER_OPENAI_BASE_URL>` | OpenAI 兼容推理入口 | 用于 Chat Completions 或 Responses 客户端，不得直接填入 Claude Messages 配置 |
| `<LAB_OPENROUTER_API_KEY>` | 使用者的个人访问凭据 | 只允许使用者在本机 CC Switch 或获批密钥管理器中输入 |
| `<LOCAL_CLAUDE_GATEWAY_URL>` | Claude Desktop 可选的本地兼容入口 | 仅在 Desktop 需要协议适配时使用，不是远程管理地址 |

以下判断必须保持独立：

- 管理控制台可登录，不代表推理端点健康。
- `/models` 能列出模型，不代表该模型能够完成真实推理。
- OpenAI 兼容入口能调用带有 Claude 名称的模型，不代表该入口实现了 Anthropic Messages 协议。
- 本地适配器存活，不代表服务端账号池存在可调度账号。

## 前置条件

- 已加入明确的实验室科研项目，并获得项目负责人同意。
- 已从维护者处获得个人 key、正确的协议端点和获批模型范围。
- 已估算模型类型、调用规模、预计周期和是否需要高并发或多 Agent。
- 已阅读实验室的数据安全、代码提交和凭据管理要求。

## 申请信息

| 字段 | 说明 |
|---|---|
| 项目 | 所属科研项目及负责人角色 |
| 用途 | 计划完成的研究任务 |
| 客户端 | Claude Code、Claude Desktop、Codex 或其他工具 |
| 协议 | Anthropic Messages、OpenAI Responses 或 Chat Completions |
| 模型需求 | 所需模型类别或能力，不填写密钥 |
| 数据边界 | 是否包含未公开研究数据或其他受限内容 |
| 申请人 | 个人账户标识；每人使用独立凭据 |

## 操作步骤

1. 联系 `@_嗯` 或 `@赖咏曦`，提交上表信息。
2. 管理员确认科研用途、额度、协议、模型权限和数据边界。
3. 通过获批的密码管理器或一次性安全渠道接收个人 key 和对应 Base URL。
4. 在本机 CC Switch 或获批的密钥管理系统中填写 `<LAB_OPENROUTER_API_KEY>`；不要把真实值发给 Agent。
5. 让 Agent 按 [CC Switch Runbook](cc-switch.md) 识别操作系统、配置供应商并执行最小验证。
6. 确认真实推理调用成功且计入正确的个人用量记录后，再开始正式任务。

## 使用规范

- 凭据按用户分配并进行流量监控，禁止共享、转发或代他人使用。
- 仅用于获批科研项目，禁止用于与项目无关的日常任务。
- 多 Agent、长时间运行和高并发任务可能快速消耗额度，启动前应评估预算并取得批准；不要使用 Goal 模式。
- 不得把未脱敏的个人信息、受限数据或未公开材料发送给未经批准的模型服务。
- 不得在 Notebook、Shell 历史、训练日志、错误截图或 Git 提交中保留 key。
- 维护者未批准的模型和思考强度不得通过别名或手工请求绕过。

## 验证

- 客户端使用的协议与 Base URL 类型一致。
- 最小真实推理返回预期结果；只有 `/models` 成功不算完成。
- Claude Desktop 使用本地适配器时，token-count 与 Messages 流程均正常。
- 管理员侧能够看到对应个人账户的用量记录。
- 终端、日志、截图和 Git 状态中没有凭据或未批准的内网地址。

## 故障排查

| 现象 | 处理方式 |
|---|---|
| `401` 或 `403` | 检查本机凭据是否加载，并联系管理员确认权限；不要发送 key 截图 |
| Messages 路由返回 `404` | 检查是否误用了 OpenAI 兼容端点或错误的 Base URL 尾部路径 |
| `/count_tokens` 返回 `404` | 这是 Desktop 兼容能力问题，不应直接判断为 key 错误；检查本地适配器 |
| `429` 或额度不足 | 降低并发、停止非必要任务，并申请额度复核 |
| `503 No available accounts` | 服务端没有可调度上游账号；不要重装客户端，交由维护者检查账号池 |
| `/models` 成功但真实推理失败 | 记录模型 ID、时间和请求 ID，由维护者检查模型映射与账号组资格 |
| 用量异常或凭据疑似泄露 | 立即停止调用、吊销并轮换 key，随后审计近期使用记录 |

## 维护信息

- 负责人：`@_嗯`、`@赖咏曦`、Lab Resources Maintainer
- AI API：[https://kjapi.botsmart.net](https://kjapi.botsmart.net)
- Codex 中转站：[https://cpa114515.somnia.ltd](https://cpa114515.somnia.ltd)
- 实验室自有 OpenRouter：部署地址通过受控渠道提供
- 最后核验：2026-09-11
