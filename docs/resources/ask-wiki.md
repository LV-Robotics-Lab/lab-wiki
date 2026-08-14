# 用 AI 查询 Wiki

## 用途

`ask-wiki` Skill 让 AI 在回答实验室流程和资源问题时实时读取已部署的 Wiki，引用完整页面，并在公开资料不足时给出对应负责人。

!!! info "无需克隆 Wiki"
    本地只安装轻量 Skill。Wiki 索引和正文始终从公开网页读取，不需要安装 Git、Python、MkDocs，也不需要下载 Wiki 仓库。

## 前置条件

- Codex 客户端支持 Skills，并已提供 `skill-installer`。
- 当前网络可以访问 `https://lv-robotics-lab.github.io/lab-wiki/`。
- 只使用公开 Wiki 查询；Skill 不登录内部系统，也不读取受控通讯录内容。

## 安装

在 Codex 对话中直接粘贴：

```text
$skill-installer https://github.com/LV-Robotics-Lab/lab-wiki/tree/main/plugins/lv-lab-wiki/skills/ask-wiki
```

安装完成后开始一个新对话，使 Codex 重新加载 Skills。通过 `/skills` 确认列表中出现 `ask-wiki`。

如果实验室已在 ChatGPT 工作区启用 `lv-lab-wiki` Plugin，无需单独安装本地 Skill；在对话中选择 `@ask-wiki`。

## 使用

Codex 中显式调用：

```text
$ask-wiki Codex CLI 如何使用官方订阅的设备码登录？
```

也可以询问跨页面问题：

```text
$ask-wiki 我在实验室外使用 GPU 前，需要完成哪些算力申请和远程接入步骤？
```

Codex 支持 `$ask-wiki` 和 `/skills` 中的 Skill 选择器。普通 Skill 不能注册任意顶层 `/ask_wiki` 命令，因此不要把 `/ask_wiki` 作为入口。

## 回答与负责人升级

正常回答应包含直接步骤、引用页面 URL 和页面的最后核验日期。Skill 会先读取紧凑索引，再读取一至三个相关完整页面；不会只根据搜索摘要作答。

以下情况会停止推断并给出负责人：

- Wiki 没有直接支持答案的页面；
- 页面冲突、明显过期或无法确认实时状态；
- 问题需要审批、授权、例外处理或内部资源权限；
- 问题涉及密码、API key、token、Cookie、私钥或认证码。

只有角色名称公开时，回答会提示通过实验室受控通讯录联系，不会猜测个人联系方式。

## 验证

安装后运行：

```text
$ask-wiki Codex CLI 如何使用官方订阅的设备码登录？
```

回答应包含 `codex login --device-auth`、Codex CLI Wiki 页面链接和 `2026-08-14` 核验日期。若只有命令而没有线上引用，视为未正确加载 Skill。

## 更新与移除

- Plugin 用户通过客户端的 Plugin 管理界面更新或移除 `lv-lab-wiki`。
- 独立 Skill 用户先通过客户端的 Skill 管理界面移除已有 `ask-wiki`，再从同一公开 GitHub 目录安装更新版本。
- 更新或移除后开始新对话，让客户端重新加载 Skills。

## 故障排查

| 现象 | 处理方式 |
|---|---|
| `/skills` 中找不到 `ask-wiki` | 重新运行安装指令，确认没有安装报错，然后开始新对话 |
| Wiki 页面无法访问 | 检查公开 HTTPS 网络；Skill 会说明无法实时核验，不会用旧内容猜测 |
| 紧凑索引返回 `404` | Skill 会降级读取站点 sitemap 和搜索索引，并在回答中标明降级状态 |
| 回答找不到负责人 | 根据回答中的参考页联系 Wiki Team，通过受控通讯录确认页面维护者 |
| 回答要求提供凭据 | 不要粘贴凭据；按对应 Wiki 页面联系负责人申请或处理泄露 |

## 维护信息

- **维护者：** Wiki Team、Lab Resources Maintainer
- **最后核验：** 2026-08-14
