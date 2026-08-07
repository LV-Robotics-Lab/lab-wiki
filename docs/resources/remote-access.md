# 远程接入与自组网申请

!!! danger "地址可查，凭据不可公开"
    经负责人确认的控制服务器地址、tailnet IP、主机名和设备清单可以写入 Wiki。预授权密钥、Auth ID、SSH 私钥、密码、访问 token、远程控制码和无人值守访问密码不得公开。

## 用途

将获批准的个人工作电脑接入实验室自托管远程网络，以访问分配给项目的工作站或服务。

## 当前接入信息

| 项目 | 当前值 |
|---|---|
| Headscale 控制服务器 | [https://hs.jingxiangguo.com](https://hs.jingxiangguo.com) |
| 网关 / 控制平面 | `sg-ai-gateway`（`100.64.0.1`），无 GPU，不作为开发机使用 |
| 新设备接入联系人 | `@nilou`（郑烨） |
| 设备、IP 与 GPU 清单 | [算力资源申请与选择](compute-access.md) |

!!! note "动态信息"
    上表与算力页是 2026-08-03 的资料快照。实际连接前请用 `tailscale status` 核验当前设备状态；网络可达不代表已获得设备操作权限。

## 前置条件

- 仅使用本人管理的工作电脑，不接入公共电脑或不受控设备。
- 已获得项目负责人和网络管理员的访问批准。
- 操作系统已更新，并启用磁盘加密、屏幕锁和本机账户密码。
- 已确认需要访问的资源、用途和预计期限。
- 已安装官方 Tailscale 客户端；不要使用来源不明的安装包。

## 申请信息

| 字段 | 说明 |
|---|---|
| 项目 | 所属项目和负责人角色 |
| 设备 | 操作系统、设备类型和建议的唯一设备名 |
| 访问目标 | 需要访问的资源类别、主机名或 tailnet IP |
| 用途 | 可视化、开发、推理、文件访问或运维支持 |
| 期限 | 预计开始和结束日期 |

## 客户端安装与登录

### macOS

1. 从 Tailscale 官方渠道安装客户端并按系统提示允许网络扩展。
2. 如果已安装 Homebrew，也可安装独立版客户端：

    ```bash
    brew install --cask tailscale
    ```

3. 在客户端设置中添加管理员提供的自定义控制服务器，或在已配置命令行的终端运行：

    ```bash
    tailscale login --login-server=https://hs.jingxiangguo.com
    ```

4. 如果图形界面没有自定义服务器入口，可使用 App 内置 CLI：

    ```bash
    /Applications/Tailscale.app/Contents/MacOS/Tailscale login --login-server=https://hs.jingxiangguo.com
    ```

5. 控制服务器地址可以公开；浏览器注册页、Auth ID 和包含凭据的完整终端输出不得公开。

### Windows

1. 从 Tailscale 官方渠道安装客户端，并在受控的管理员说明下添加自定义控制服务器。
2. 在 PowerShell 中运行：

    ```powershell
    tailscale login --login-server=https://hs.jingxiangguo.com
    ```

3. 如果命令未加入 `PATH`，在 PowerShell 中使用安装目录里的可执行文件：

    ```powershell
    & "$env:ProgramFiles\Tailscale\tailscale.exe" login --login-server=https://hs.jingxiangguo.com
    ```

4. 固定工作站或服务器如需无人登录后保持在线，需单独确认后再启用 unattended 模式：

    ```powershell
    tailscale up --unattended=true
    ```

5. 普通个人电脑不默认启用 unattended 模式；是否启用由项目负责人和网络管理员确认。

### Linux

1. 按 [Tailscale 官方 Linux 安装说明](https://tailscale.com/docs/install/linux) 安装与启动客户端。
2. 运行：

    ```bash
    sudo tailscale up --login-server=https://hs.jingxiangguo.com
    ```

3. 可将控制服务器地址写入安装说明；不要把预授权密钥、Auth ID 或其他凭据写入脚本、镜像或仓库。

## Auth ID 注册

1. 运行登录命令后，浏览器或终端会显示一次性注册信息。
2. 只通过受控渠道向网络管理员提交 **Auth ID**、建议设备名、所属项目和访问期限；不要转发完整页面或日志。
3. 管理员将 Auth ID 注册到正确的成员身份，并按项目范围配置访问规则。当前统一注册到 Headscale 用户 `<HEADSCALE_USER>`，除非网络管理员另有说明。
4. 管理员侧使用如下形式批准节点；真实 Auth ID 只在受控渠道中短期保存，不写入 Wiki：

    ```bash
    headscale auth register --auth-id <AUTH_ID> --user <HEADSCALE_USER>
    headscale nodes list
    ```

5. 注册完成后重新连接客户端，确认设备名唯一且未复用其他节点身份。
6. Auth ID 和预授权密钥均不得发布到 Wiki；非交互式接入必须单独审批。

## SSH 公钥授权

### 生成公钥

macOS 或 Linux：

```bash
test -f ~/.ssh/id_ed25519.pub || ssh-keygen -t ed25519 -C "<MEMBER_OR_DEVICE_NAME>"
cat ~/.ssh/id_ed25519.pub
```

Windows PowerShell：

```powershell
ssh-keygen -t ed25519 -C "<MEMBER_OR_DEVICE_NAME>"
Get-Content "$env:USERPROFILE\.ssh\id_ed25519.pub"
```

!!! warning "只提交公钥"
    只提交以 `.pub` 结尾的公钥。私钥文件不得上传、转发或复制给管理员。

### 提交授权

通过受控渠道提交公钥、申请的资源类别、项目、期限和目标账户角色。管理员通过受控配置或自动化完成授权；Wiki 可记录已批准的目标主机名/IP，但不公开真实账户、凭据或 `authorized_keys` 位置。

### 验证 SSH

```bash
ssh -o BatchMode=yes -o PasswordAuthentication=no <SSH_USERNAME>@<AUTHORIZED_HOSTNAME> hostname
```

OpenSSH 公钥授权与 Tailscale SSH 是两套不同机制。是否启用 Tailscale SSH 由网络管理员和访问规则决定，成员不要自行更改服务器配置。

## 操作步骤

1. 联系 **`@nilou`（郑烨）** 并提交申请信息。
2. 管理员确认设备、项目权限和允许访问的资源范围。
3. 通过一次性或短期有效的安全渠道获取接入信息；禁止转发。
4. 按对应操作系统完成客户端登录和 Auth ID 注册。
5. 如需 SSH，提交本人独立公钥并等待目标资源授权。
6. 接入后仅验证已授权的目标，不扫描或尝试访问其他节点。
7. 项目结束、设备更换或人员离组时，主动申请撤销旧设备和公钥权限。

## 管理员交付检查

- Auth ID 来自 `https://hs.jingxiangguo.com` 的注册页，且未过期、未重复使用。
- 节点已注册到正确 Headscale 用户，并在 `headscale nodes list` 中显示为独立设备。
- 节点名清晰、唯一，能体现成员、设备或用途；不要复用其他在线节点身份。
- 新设备已获得 `100.64.0.x` 地址，并能看到或 ping 通已授权目标。
- 如需 SSH，成员只提交 `.pub` 公钥，管理员只把公钥部署到批准的目标账户。
- 验证命令使用 `BatchMode=yes` 和 `PasswordAuthentication=no`，确认不会回退到密码登录。

## 使用规范

- 自组网仅用于科研协作和获批资源访问，不得用于无关流量中转。
- 禁止共享节点身份、预授权密钥、SSH 私钥或无人值守访问密码。
- 主机名、tailnet IP 和 GPU 配置可以在 Wiki 中维护；公开错误截图前仍需检查并遮盖 Auth ID、密钥、token、账户和其他凭据。
- 使用远程桌面前确认当前网络路径和授权范围；网络可达不代表可以操作设备。
- 临时协助结束后应关闭共享、撤销一次性权限并检查远程会话。

## 验证

```bash
tailscale status
tailscale ip -4
tailscale netcheck
tailscale ping <AUTHORIZED_HOSTNAME>
```

- 设备在管理员侧显示为独立、预期的节点身份。
- 只能访问获授权的资源，且项目服务、SSH 或远程桌面按预期工作。
- SSH 验证不回退到密码登录。
- 终端输出、截图和文档中没有泄露 Auth ID、密钥、密码、token 或其他凭据。

### 判断直连或 DERP 中继

```bash
tailscale ping <AUTHORIZED_HOSTNAME>
```

- 输出包含 `via <IP>:<UDP_PORT>` 时，通常表示点对点直连，延迟更低。
- 输出包含 `via DERP(...)` 时，表示通过 DERP 中继；这仍然是正常、加密且可用的连接，只是可能更慢。
- 直连受运营商、校园网、云平台防火墙和 NAT 影响，无法由成员单方面强制。

### 可选：出口节点

只有明确需要让全部互联网流量经过批准的出口节点时才启用：

```bash
tailscale set --exit-node=<EXIT_NODE_NAME> --exit-node-allow-lan-access=true
```

停止使用出口节点：

```bash
tailscale set --exit-node=
```

!!! warning "出口节点需单独批准"
    出口节点会改变设备的互联网出口路径，不是远程接入的默认步骤。不要为了普通 SSH、远程桌面或文件访问启用出口节点。

## 故障排查

- 登录命令没有产生 Auth ID：确认控制服务器为 `https://hs.jingxiangguo.com`，并检查客户端版本和网络状态。
- 设备显示为其他节点：停止使用并重新以独立状态注册，避免断开正在运行的同名设备。
- 能看到节点但无法交互：检查当前直连、中继和目标服务端口，不要仅依据“在线”判断。
- SSH 仍要求密码：检查提交的是正确公钥、目标账户已获授权且本机正在使用对应私钥；不要把密码写进脚本。
- 远程桌面卡顿：记录时间和连接类型，联系网络管理员检查路径。
- 设备丢失或离组：立即撤销节点和相关临时凭据。
- 需要线下协助：联系 `@nilou`（郑烨）或设备维护者；公开页面可以记录实验室设备位置，但不要公开个人实时位置。

## 参考资料

- [Headscale 节点注册说明](https://headscale.net/stable/ref/registration/)
- [Tailscale 自定义控制服务器说明](https://tailscale.com/docs/how-to/set-up-custom-control-server)
- [Tailscale Linux 安装说明](https://tailscale.com/docs/install/linux)

## 维护信息

- 负责人：网络管理员
- 联系入口：`@nilou`（郑烨）
- 最后核验：2026-08-03
