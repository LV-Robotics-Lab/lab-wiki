# Codex CLI 多 Profile 与订阅登录

!!! info "这篇指南解决两个不同问题"
    `--profile` 用于切换模型、中转站、审批策略等配置；它不会切换 ChatGPT 账户。需要同时使用多个 ChatGPT 订阅账户时，必须为每个账户使用独立的 `CODEX_HOME`。

!!! danger "凭据边界"
    不要把 API key、`auth.json`、设备码、Cookie 或完整的环境变量内容提交到 Git、Wiki、Issue、聊天记录或截图中。本文所有密钥和地址均使用占位符。

## 用途

为实验室成员提供一套可以直接复制和修改的 Codex CLI 配置方法：

- 为不同的 OpenAI 兼容中转站创建独立 profile。
- 使用 ChatGPT 订阅登录 Codex CLI，而不是把订阅凭据当成 API key。
- 在无浏览器、远程服务器或多账户场景下使用设备码登录和独立认证目录。

## 前置条件

- 已安装较新的 Codex CLI，并能在终端执行 `codex --version`。
- 已有一个获批的中转站地址和个人 API key，或者有可使用 Codex 的 ChatGPT 订阅账户。
- 使用 Bash 或 Zsh；Windows 用户请把示例改写为 PowerShell 环境变量和函数。
- 已确认工作目录和机器属于自己有权操作的环境。

## 先理解配置层级

Codex 的用户配置目录默认是 `~/.codex`，也可以由 `CODEX_HOME` 指定。使用 `--profile relay` 时，Codex 会先读取：

```text
~/.codex/config.toml
~/.codex/relay.config.toml
```

后者覆盖前者，因此 profile 文件只需要写差异项。项目目录中的可信 `.codex/config.toml`、命令行参数和 `--config` 覆盖的优先级更高。

`--profile` 只改变配置层，不会隔离以下状态：

- ChatGPT 或 API key 认证缓存；
- 会话历史、日志和缓存；
- `CODEX_HOME` 下的其他本地状态。

如果要隔离账户或全部本地状态，请看[多订阅账户隔离](#multi-subscription-accounts)。

## 创建中转站 Profile

以下示例把 profile 命名为 `relay`。profile 名只能使用字母、数字、连字符和下划线。

### 1. 创建文件

```bash
mkdir -p ~/.codex
nano ~/.codex/relay.config.toml
```

把下面内容复制到文件中，然后按实际服务修改四个占位项：

```toml
# ~/.codex/relay.config.toml
model = "gpt-5.6-sol"
model_provider = "relay"
model_reasoning_effort = "low"

[model_providers.relay]
name = "Approved Relay"
base_url = "<RELAY_BASE_URL>/v1"
env_key = "BOTSMART_API_KEY"
wire_api = "responses"
```

需要修改的地方：

| 配置 | 含义 |
|---|---|
| `relay` | provider 的内部 ID；同一文件中的 `model_provider` 必须一致 |
| `Approved Relay` | CLI 中显示的名称，可自行命名 |
| `<RELAY_BASE_URL>/v1` | 负责人提供的 OpenAI 兼容 Base URL |
| `BOTSMART_API_KEY` | 保存 key 的环境变量名，不是 key 本身 |

如果使用实验室已批准的服务，请先查看 [AI API 申请与使用](ai-api-access.md)，并使用管理员为你分配的个人 key。不要把真实地址、key 或审批记录粘贴到本页。

### 2. 配置 API key 环境变量

临时配置（只对当前终端有效）：

```bash
export BOTSMART_API_KEY="<YOUR_PERSONAL_API_KEY>"
```

长期配置可以写入 `~/.bashrc` 或 `~/.zshrc`，但仍然不要把该文件提交到仓库：

```bash
printf '\nexport BOTSMART_API_KEY="<YOUR_PERSONAL_API_KEY>"\n' >> ~/.bashrc
source ~/.bashrc
```

不要用 `echo $BOTSMART_API_KEY` 验证，因为这会把 key 打到终端历史或录屏中。使用只显示状态的检查：

```bash
if [ -n "${BOTSMART_API_KEY:-}" ]; then
  echo "BOTSMART_API_KEY is set"
else
  echo "BOTSMART_API_KEY is missing"
fi
```

### 3. 启动和执行任务

```bash
codex --profile relay
codex exec --profile relay "检查当前项目的测试并总结失败原因"
```

可选：为交互式终端创建快捷命令：

```bash
printf "\nalias codex-relay='codex --profile relay'\n" >> ~/.bashrc
source ~/.bashrc
codex-relay
```

如果使用 `codex exec`、脚本或 CI，请优先使用显式的 `--profile relay`，避免 shell alias 在非交互环境中失效。

### 4. 创建第二个中转站

复制配置文件，只保留与默认配置不同的值：

```bash
cp ~/.codex/relay.config.toml ~/.codex/relay2.config.toml
nano ~/.codex/relay2.config.toml
codex --profile relay2
```

不要在 `config.toml` 中新增旧式的 `[profiles.relay]` 表。当前 Codex 使用 `~/.codex/<profile-name>.config.toml`；旧版配置需要迁移到这种文件布局。

## 使用 ChatGPT 订阅登录

ChatGPT 登录和 API key 登录是两条不同的认证路径。订阅登录的用量和可用功能由 ChatGPT 账户或工作区权限决定；API key 登录则按 OpenAI Platform 的 API 用量计费。本文的“官方订阅”指下面的 ChatGPT 登录，不是中转站 key。

### 浏览器可用时

在终端执行：

```bash
codex login
```

在打开的浏览器中选择 ChatGPT 登录并完成授权。随后检查认证方式：

```bash
codex login status
```

正常情况下，状态会显示当前使用的是 ChatGPT 会话，而不是 API key。

### 远程或无头设备：设备码登录

官方文档将设备码认证标记为 beta。使用前需要：

1. 个人账户：在 ChatGPT 的安全设置中启用设备码登录。
2. 工作区账户：由工作区管理员在权限设置中启用设备码登录。
3. 确认当前终端可以访问 Codex 登录服务。

然后在运行 Codex 的终端执行：

```bash
codex login --device-auth
```

按终端输出打开登录链接，在浏览器登录 ChatGPT，并输入一次性设备码。完成后回到终端验证：

```bash
codex login status
```

设备码登录不可用时，官方提供两种后备方案：在有浏览器的机器上运行 `codex login` 后，把认证缓存安全复制到远程机器；或者通过 SSH 转发默认的本地回调端口 `1455`。复制 `auth.json` 前必须确认传输链路和目标机器可信，并把它当作密码处理。

### 认证缓存和退出

CLI 和 IDE 扩展共享登录缓存。Codex 可能将凭据存放在 `~/.codex/auth.json`，也可能存放在操作系统的凭据管理器中。文件存储的 `auth.json` 包含访问令牌：

- 不要提交、分享或上传它；
- 不要把它放进 Docker 镜像或公开备份；
- 怀疑泄露时立即退出并重新登录，必要时联系管理员。

退出当前认证：

```bash
codex logout
```

## 多订阅账户隔离 { #multi-subscription-accounts }

如果同一台机器需要登录两个 ChatGPT 账户，仅使用 `--profile` 不够。请为每个账户指定不同的 `CODEX_HOME`，并在登录、运行和退出时始终使用同一个目录。

为避免系统 keyring 继续共享凭据，下面的初始化命令为每个新目录启用文件凭据存储。`auth.json` 是明文敏感凭据，因此同时收紧目录和配置文件权限。只对尚未使用的新目录执行这些初始化命令；已有配置时请先手动合并 `cli_auth_credentials_store`，不要覆盖原文件。

### 方案 A：每次显式指定目录

```bash
install -d -m 700 "$HOME/.codex-subscription-a"
printf '%s\n' 'cli_auth_credentials_store = "file"' \
  > "$HOME/.codex-subscription-a/config.toml"
chmod 600 "$HOME/.codex-subscription-a/config.toml"
CODEX_HOME="$HOME/.codex-subscription-a" codex login --device-auth
CODEX_HOME="$HOME/.codex-subscription-a" codex login status
CODEX_HOME="$HOME/.codex-subscription-a" codex
```

第二个账户使用另一个目录：

```bash
install -d -m 700 "$HOME/.codex-subscription-b"
printf '%s\n' 'cli_auth_credentials_store = "file"' \
  > "$HOME/.codex-subscription-b/config.toml"
chmod 600 "$HOME/.codex-subscription-b/config.toml"
CODEX_HOME="$HOME/.codex-subscription-b" codex login --device-auth
CODEX_HOME="$HOME/.codex-subscription-b" codex login status
CODEX_HOME="$HOME/.codex-subscription-b" codex
```

### 方案 B：创建安全的 shell 函数

把下面函数加入 `~/.bashrc` 或 `~/.zshrc`，然后执行 `source ~/.bashrc`（Zsh 则执行 `source ~/.zshrc`）：

```bash
codex-sub-a() {
  CODEX_HOME="$HOME/.codex-subscription-a" codex "$@"
}

codex-sub-b() {
  CODEX_HOME="$HOME/.codex-subscription-b" codex "$@"
}
```

登录和运行：

```bash
codex-sub-a login --device-auth
codex-sub-a login status
codex-sub-a

codex-sub-b login --device-auth
codex-sub-b login status
codex-sub-b
```

### 凭据存储注意事项

上面的初始化步骤已经在各自的 `config.toml` 中设置：

```toml
cli_auth_credentials_store = "file"
```

这会把凭据写入对应目录的 `auth.json`。首次登录后分别运行 `chmod 600 "$HOME/.codex-subscription-a/auth.json"` 和 `chmod 600 "$HOME/.codex-subscription-b/auth.json"`，并禁止把它们同步到公开位置。若改回 `keyring` 或 `auto`，凭据可能进入操作系统凭据管理器；多账户隔离行为取决于操作系统和 Codex 版本，验证前不要假设已经隔离。

## 验证清单

- [ ] `codex --version` 能正常返回版本。
- [ ] 中转站 profile 能用 `codex --profile <PROFILE>` 启动。
- [ ] API key 只存在于环境变量或批准的密钥管理器中，终端检查不回显 key。
- [ ] 订阅登录用 `codex login status` 显示 ChatGPT 认证。
- [ ] 设备码登录在正确的个人账户或工作区中完成。
- [ ] 多账户使用不同的 `CODEX_HOME`，每个目录都能独立执行 `login status`。
- [ ] `auth.json`、`.bashrc`、`.zshrc` 和日志没有被提交到 Git。

## 故障排查

| 现象 | 处理方式 |
|---|---|
| `codex --profile relay` 找不到配置 | 检查文件是否确实位于 `~/.codex/relay.config.toml`，profile 名和文件名是否完全一致 |
| `401`、`403` 或 key 缺失 | 检查环境变量名称和当前 shell；不要打印 key，确认 provider 的 `env_key` 与变量名一致 |
| profile 启动了但仍使用默认 provider | 检查 profile 中的 `model_provider` 和 `[model_providers.<id>]` 是否使用同一个 ID，并确认没有更高优先级的 CLI 或项目配置覆盖 |
| `codex login` 打不开浏览器 | 改用 `codex login --device-auth`；设备码不可用时使用可信机器复制认证缓存或 SSH 回调转发 |
| 设备码选项不存在 | 在 ChatGPT 安全设置或工作区权限中启用设备码登录；仍不可用时联系管理员或 OpenAI 支持 |
| 两个账户互相覆盖 | 检查登录、运行、退出命令是否都带同一个 `CODEX_HOME`，不要只用 `--profile` 区分账户 |
| 认证状态异常或疑似泄露 | 立即运行对应 `CODEX_HOME` 下的 `codex logout`，删除暴露的缓存并重新登录；API key 则吊销并轮换 |

## 官方参考

- [OpenAI Docs: Authentication](https://learn.chatgpt.com/docs/auth)
- [OpenAI Docs: Advanced Configuration](https://learn.chatgpt.com/docs/config-file/config-advanced)
- [OpenAI Docs: Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

## 维护信息

- **维护者：** Lab Resources Maintainer
- **最后核验：** 2026-08-14
