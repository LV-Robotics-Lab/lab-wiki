# 远程接入与自组网申请

!!! danger "禁止发布网络清单"
    Wiki 不保存控制服务器地址、tailnet IP、主机名、设备清单、预授权密钥、Auth ID、SSH 目标、远程控制码或密码。

## 用途

将获批准的个人工作电脑接入实验室自托管远程网络，以访问分配给项目的工作站或服务。

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
| 访问目标 | 需要访问的资源类别，不填写内部地址 |
| 用途 | 可视化、开发、推理、文件访问或运维支持 |
| 期限 | 预计开始和结束日期 |

## 客户端安装与登录

### macOS

1. 从 Tailscale 官方渠道安装客户端并按系统提示允许网络扩展。
2. 在客户端设置中添加管理员提供的自定义控制服务器，或在已配置命令行的终端运行：

    ```bash
    tailscale login --login-server=<HEADSCALE_URL>
    ```

3. 不要把控制服务器地址、浏览器注册页面或终端完整输出粘贴到公开聊天或 Issue。

### Windows

1. 从 Tailscale 官方渠道安装客户端，并在受控的管理员说明下添加自定义控制服务器。
2. 在 PowerShell 中运行：

    ```powershell
    tailscale login --login-server=<HEADSCALE_URL>
    ```

3. 如果命令未加入 `PATH`，使用已安装客户端的界面完成登录，或联系网络管理员确认本机安装方式。

### Linux

1. 按 [Tailscale 官方 Linux 安装说明](https://tailscale.com/docs/install/linux) 安装与启动客户端。
2. 运行：

    ```bash
    sudo tailscale up --login-server=<HEADSCALE_URL>
    ```

3. 不要将控制服务器地址写入公开脚本、镜像或仓库。

## Auth ID 注册

1. 运行登录命令后，浏览器或终端会显示一次性注册信息。
2. 只通过受控渠道向网络管理员提交 **Auth ID**、建议设备名、所属项目和访问期限；不要转发完整页面或日志。
3. 管理员将 Auth ID 注册到正确的成员身份，并按项目范围配置访问规则。
4. 注册完成后重新连接客户端，确认设备名唯一且未复用其他节点身份。
5. Auth ID 和预授权密钥均不得发布到 Wiki；非交互式接入必须单独审批。

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

通过受控渠道提交公钥、申请的资源类别、项目、期限和目标账户角色。管理员通过受控配置或自动化完成授权；Wiki 不公开服务器路径、真实账户或 `authorized_keys` 位置。

### 验证 SSH

```bash
ssh -o BatchMode=yes -o PasswordAuthentication=no <SSH_USERNAME>@<AUTHORIZED_HOSTNAME> hostname
```

OpenSSH 公钥授权与 Tailscale SSH 是两套不同机制。是否启用 Tailscale SSH 由网络管理员和访问规则决定，成员不要自行更改服务器配置。

## 操作步骤

1. 通过受控通讯录联系 **网络管理员** 并提交申请信息。
2. 管理员确认设备、项目权限和允许访问的资源范围。
3. 通过一次性或短期有效的安全渠道获取接入信息；禁止转发。
4. 按对应操作系统完成客户端登录和 Auth ID 注册。
5. 如需 SSH，提交本人独立公钥并等待目标资源授权。
6. 接入后仅验证已授权的目标，不扫描或尝试访问其他节点。
7. 项目结束、设备更换或人员离组时，主动申请撤销旧设备和公钥权限。

## 使用规范

- 自组网仅用于科研协作和获批资源访问，不得用于无关流量中转。
- 禁止共享节点身份、预授权密钥、SSH 私钥或无人值守访问密码。
- 不要把完整的网络状态、IP、主机名或错误截图贴到公开 Issue 和 Wiki。
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
- 未在终端输出、截图和文档中泄露网络清单或凭据。

## 故障排查

- 登录命令没有产生 Auth ID：确认控制服务器占位值已从受控渠道正确填写，并检查客户端版本和网络状态。
- 设备显示为其他节点：停止使用并重新以独立状态注册，避免断开正在运行的同名设备。
- 能看到节点但无法交互：检查当前直连、中继和目标服务端口，不要仅依据“在线”判断。
- SSH 仍要求密码：检查提交的是正确公钥、目标账户已获授权且本机正在使用对应私钥；不要把密码写进脚本。
- 远程桌面卡顿：记录时间和连接类型，联系网络管理员检查路径。
- 设备丢失或离组：立即撤销节点和相关临时凭据。
- 需要线下协助：通过受控通讯录联系当日值班维护者，不在公开页面写个人位置。

## 参考资料

- [Headscale 节点注册说明](https://headscale.net/stable/ref/registration/)
- [Tailscale 自定义控制服务器说明](https://tailscale.com/docs/how-to/set-up-custom-control-server)
- [Tailscale Linux 安装说明](https://tailscale.com/docs/install/linux)

## 维护信息

- 负责人：网络管理员
- 联系入口：`<CONTROLLED_CONTACT_DIRECTORY_URL>`
- 最后核验：2026-08-03
