# Lab Resources Design

## Goal

Add a bilingual resource hub to the public Lab Wiki without exposing internal spreadsheet identifiers, authentication material, account identifiers, or unreviewed operational details.

## Scope

The change adds a top-level **Lab Resources** navigation section with:

- A bilingual resource directory.
- A bilingual Hardware Resource Center placeholder page.
- Aligned Chinese and English navigation labels.

It does not copy spreadsheet contents, publish internal URLs, document credentials, or invent missing hardware procedures.

## Information Architecture

Create these matching page pairs:

- `docs/resources/index.md` and `docs/resources/index.en.md`
- `docs/resources/hardware.md` and `docs/resources/hardware.en.md`

Add a new top-level navigation section after Administration and before How to Contribute:

- Lab Resources overview
- Hardware Resource Center

The Chinese pages remain the default navigation source. English labels are supplied through `nav_translations` in `mkdocs.yml`.

## Resource Directory Content

The overview page groups the approved resources by purpose:

- Intern and visiting-member administration: `<INTERN_VISITING_TRACKER_URL>`
- Purchasing and asset records: `<PURCHASE_ASSET_REGISTER_URL>`
- Code repositories: `https://github.com/orgs/LV-Robotics-Lab/repositories`
- Romoya-related resources: `<ROMOYA_RESOURCE_SHEET_URL>`
- Hardware Resource Center: link to the local bilingual hardware page

Each placeholder name must describe the destination clearly. A visible note explains that maintainers must replace placeholders only after confirming that publication is appropriate. The GitHub link may remain explicit because it identifies a public organization page; the page warns that individual repositories may still require organization access.

## Hardware Resource Center Content

The Hardware Resource Center page is intentionally a content placeholder because the supplied source contained only a title and timestamp. It states the intended purpose and lists the missing information that a maintainer must review, such as inventory scope, access procedure, usage rules, and support contact. It must display `Requires maintainer review` and must not imply that an unverified procedure is ready for use.

Because this is a status and contribution page rather than an operational guide, it will not present fabricated prerequisites, procedures, verification steps, or troubleshooting instructions. Once reviewed operational instructions are available, the page must adopt the repository's required operational-guide sections.

## Privacy and Redaction

- Do not include Google backup codes, account email addresses, authentication instructions, or other credentials.
- Do not include the supplied Google Sheet IDs, URLs, or Notion page IDs.
- Do not inspect or summarize spreadsheet rows for this change.
- Do not infer that a linked resource is safe to publish because it was shared in the source material.
- Keep the descriptive URL placeholders until a maintainer explicitly approves replacement.

## Validation

- Confirm every Chinese page has a matching `.en.md` page with the same section structure.
- Confirm `mkdocs.yml` contains matching Chinese navigation entries and English translations.
- Search the changed files for the supplied account identifier, credential material, Google Sheet IDs, and Notion page IDs.
- Review `git diff` before any commit.
- Run `mkdocs build --strict` and require a zero exit status.

