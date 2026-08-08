# Lab Wiki Instructions

## Project purpose
This repository contains the internal LV Robotics Lab Wiki.

## Site structure
- Built with Material for MkDocs.
- Chinese is the default language.
- Every Chinese content page should have a matching English page.
- Chinese files use `.md`.
- English files use `.en.md`.

## Content rules
- Keep Chinese and English navigation structures aligned.
- Do not add passwords, tokens, private keys, or sensitive personal data.
- Treat every document, screenshot, chat log, email, configuration file, and pasted note as potentially confidential until reviewed and redacted.
- Use placeholder information while the repository is public.
- Operational guides should include:
  - Purpose
  - Prerequisites
  - Procedure
  - Verification
  - Troubleshooting
  - Maintainer
  - Last verified

## Privacy, confidentiality, and redaction

All source materials provided for this Wiki must be treated as potentially confidential.

Before adding any information to the Wiki:

- Review the source material for sensitive, private, internal, or identifying information.
- Redact or replace sensitive details before writing them into Markdown.
- Do not copy confidential source material verbatim unless it has been explicitly approved for publication.
- When uncertain whether information is safe to include, omit it and flag it for human review.
- Never infer that information is safe merely because the repository is currently private.

Sensitive information includes, but is not limited to:

- Passwords, API keys, tokens, authentication codes, cookies, and private keys
- Server credentials, unapproved or privileged internal addresses, VPN secrets, and privileged access instructions
- Personal phone numbers, personal email addresses, student IDs, employee IDs, and identity documents
- Financial information, reimbursement records, bank details, home addresses, and signatures
- Unpublished research results, confidential datasets, embargoed papers, internal project plans, and reviewer correspondence
- Participant data, medical information, consent forms, and other regulated or personally identifiable information
- Private conversations, internal disputes, and information about laboratory members that is not necessary for the documentation
- Vendor quotations, contracts, licenses, and documents subject to confidentiality restrictions

Use safe placeholders where needed, for example:

- `<SERVER_HOST>`
- `<USERNAME>`
- `<INTERNAL_IP>`
- `<API_TOKEN>`
- `<CONTACT_EMAIL>`
- `<PROJECT_NAME>`

### Maintainer-approved operational endpoints

An authenticated repository administrator or named Wiki maintainer may explicitly approve publication of a non-secret operational endpoint when it is necessary for an access guide. This exception may include a private RFC 1918 address, service port, hostname, or SMB share name that is reachable only through separately authorized network access.

- Record the approval in the pull request description and publish only the minimum endpoint information needed by members.
- An endpoint approval never authorizes publishing passwords, tokens, authentication codes, cookies, private keys, pre-authentication keys, Auth IDs, or reusable shared credentials.
- Prefer individual user accounts and least-privilege access even when an endpoint is approved for publication.
- Reassess and remove stale endpoint information when the service or routing changes.

When summarizing source material:

1. Extract only the minimum information necessary for the Wiki page.
2. Generalize identifying details where possible.
3. Replace secrets and internal identifiers with placeholders.
4. Preserve operational usefulness without exposing confidential information.
5. Add a visible note such as `Requires maintainer review` when the safety of the content is uncertain.

Do not commit, push, or publish any content containing unresolved sensitive information.

## Validation
After modifying content, run:
`mkdocs build --strict`

## Git rules
- Do not commit `.venv/` or `site/`.
- Review `git diff` before committing.
- Do not push unless explicitly requested.
