# Hardware Resource Center Expansion Design

## Goal

Replace the current Hardware Resource Center status page with a useful bilingual resource guide while keeping all internal URLs, credentials, account identifiers, host details, and internal paths out of the public repository.

## Scope

Update only the existing bilingual page pair:

- `docs/resources/hardware.md`
- `docs/resources/hardware.en.md`

No new navigation section or page is required. The Chinese and English pages must retain matching section order and equivalent content.

## Page Structure

Both pages use the repository's operational-guide structure:

1. Purpose
2. Prerequisites
3. Resource Catalog
4. Access Configuration References
5. Procedure
6. Verification
7. Troubleshooting
8. Maintainer and last-verified metadata

A warning at the top states that placeholders must never be replaced with real secrets in the Wiki. Actual secrets belong only in an approved password manager or another access-controlled system.

## Resource Catalog

### Realhand

- Internal resource folder: `<REALHAND_RESOURCE_FOLDER_URL>`
- Public LinkerHand teleoperation repository: `https://gitee.com/ericbrunt/linkerhand_telop_python`

### AgileX

Three supplied AgileX support documents did not include usable titles. Preserve their existence without guessing their contents:

- `<AGILEX_SUPPORT_DOCUMENT_1_URL>` — `Requires maintainer review`
- `<AGILEX_SUPPORT_DOCUMENT_2_URL>` — `Requires maintainer review`
- `<AGILEX_SUPPORT_DOCUMENT_3_URL>` — `Requires maintainer review`

Use descriptive placeholders for identified documents:

- TRACER 2.0 user manual: `<AGILEX_TRACER_2_USER_MANUAL_URL>`
- NERO user manual: `<AGILEX_NERO_USER_MANUAL_URL>`
- NERO CAN protocol: `<AGILEX_NERO_CAN_PROTOCOL_URL>`
- Robot-arm communication protocol: `<AGILEX_ARM_COMMUNICATION_PROTOCOL_URL>`

Do not publish the supplied Yuque URLs.

### Daimon and TacClaw

- Internal resource folder: `<DAIMON_RESOURCE_FOLDER_URL>`
- Host: `<TACCLAW_HOST>`
- Username: `<TACCLAW_USERNAME>`
- Password reference: `<TACCLAW_PASSWORD>`
- Service path: `<TACCLAW_SERVICE_PATH>`
- SSH command template: `ssh <TACCLAW_USERNAME>@<TACCLAW_HOST>`

Do not include the supplied host address, username, password, or service path.

### UDEXREAL Data Gloves

- Internal documentation: `<UDEXREAL_DATAGLOVES_DOCUMENT_URL>`

Do not publish the supplied Feishu URL.

### WUJI

- Public documentation: `https://docs.wuji.tech/docs/zh/wuji-hand/latest/`

### Franka

- GELLO single-arm teleoperation guide: `<FRANKA_GELLO_SINGLE_ARM_GUIDE_URL>`

### YAM

Use **YAM**, not the supplied **YUM** spelling. The associated public repository describes YAM arms.

- Internal resource folder: `<YAM_RESOURCE_FOLDER_URL>`
- Public i2rt repository: `https://github.com/i2rt-robotics/i2rt`

### HigVR

- Vendor manual: `https://higvr.com/en-cn/pages/user-manual`

### LeRobot Chinese Tutorial

- Internal tutorial: `<LEROBOT_CHINESE_TUTORIAL_URL>`

Do not publish the supplied Feishu URL.

## Credential and Account References

The page may identify required credential types only through these exact placeholders:

- GitHub API token: `<GITHUB_API_TOKEN>`
- Hugging Face API token: `<HUGGINGFACE_API_TOKEN>`
- Weights & Biases API key: `<WANDB_API_KEY>`
- Laboratory shared password: `<LAB_SHARED_PASSWORD>`
- MISUMI account ID: `<MISUMI_ACCOUNT_ID>`
- ME Control Lab username: `<ME_CONTROL_LAB_USERNAME>`
- ME Control Lab password: `<ME_CONTROL_LAB_PASSWORD>`
- Franka administrator username: `<FRANKA_ADMIN_USERNAME>`
- Franka administrator password: `<FRANKA_ADMIN_PASSWORD>`
- Franka safety-officer username: `<FRANKA_SAFETY_USERNAME>`
- Franka safety-officer password: `<FRANKA_SAFETY_PASSWORD>`

The guide must direct readers to an approved password manager or the maintainer for access. It must explicitly prohibit replacing these placeholders with real values in Markdown.

## Procedure

The safe workflow is:

1. Identify the relevant hardware category.
2. Use an explicit public documentation or repository link when provided.
3. For a placeholder URL, request the approved internal destination from the maintainer.
4. For credentials or device access, retrieve the authorized value from the approved password manager; never copy it into the Wiki.
5. Follow the vendor's current safety and operating documentation before controlling hardware.

## Verification and Troubleshooting

Verification tells readers to confirm that public documentation opens, internal access is authorized, and the expected product/model is shown before following instructions.

Troubleshooting directs readers to:

- Check whether a placeholder still requires maintainer review.
- Confirm organization or document-sharing permissions.
- Contact the relevant hardware maintainer for missing links or access.
- Revoke and rotate any credential accidentally exposed in documentation or chat.
- Never work around access control by embedding secrets in the Wiki.

## Privacy and Redaction

- Do not include any supplied API key, token, password, account identifier, private host address, private SSH target, or internal service path.
- Do not include the supplied Google Drive, Yuque, or Feishu URLs.
- Do not reproduce sensitive source material in specifications, implementation plans, commands, commit messages, or test output.
- Use generic prefix and structure checks that report file names or failure status without printing matching secret values.
- Keep all descriptive placeholders until a maintainer explicitly approves a safe replacement.

## Validation

- Confirm the Chinese and English page headings and resource categories align.
- Confirm all exact placeholders listed in this design appear in both languages where applicable.
- Confirm only the approved public Gitee, WUJI, GitHub, and HigVR URLs appear.
- Run a silent sensitive-pattern audit over the changed pages without printing matches.
- Review `git diff --check` and the full content diff.
- Run `mkdocs build --strict` and require a zero exit status.
