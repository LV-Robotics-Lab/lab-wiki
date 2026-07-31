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
