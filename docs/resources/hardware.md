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
