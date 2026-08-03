# Accounts and Access

## Purpose

Provide one place to request laboratory accounts, compute, remote-network access, and internal tools without transmitting credentials through group chats or public documentation.

## Prerequisites

- You are participating in a defined laboratory or course project.
- The required resource, purpose, permission scope, and usage period are known.
- You will request access with a personal account rather than sharing an identity or credential.

## Request template

| Resource | Contact | Required information | Guidance |
|---|---|---|
| GitHub | Wiki Administrator | GitHub username, project, and repository permission | Use a personal GitHub account |
| AI API | AI Service Administrator | Project, purpose, model, and usage estimate | See [AI API Access and Usage](ai-api-access.en.md) |
| Compute | Compute Administrator | GPU, count, duration, and budget source | See [Compute Resource Requests and Selection](../resources/compute-access.en.md) |
| Remote access | Network Administrator | Work device, project, target resource, and period | See [Remote Access and Private-Network Enrollment](../resources/remote-access.en.md) |
| File storage | Data Storage Administrator | Project, data type, capacity, and members | See [Research Data Storage and Archiving](../resources/data-management.en.md) |
| Internal tools | Service owner | Purpose, required permission, and period | Request through the controlled directory |

## Procedure

1. Select the resource category and prepare the required information.
2. Contact the relevant administrator through the controlled laboratory directory.
3. The administrator confirms the project, permission scope, and usage period.
4. Receive sensitive configuration through a password manager or one-time secure channel.
5. Complete a minimal verification and retain the request record without storing credentials.

## Verification

- The personal account can access the approved resource.
- Unapproved projects and services remain inaccessible.
- No real credentials appear in the Wiki, Issues, logs, or repositories.

## Troubleshooting

- Permission denied: provide the project and error summary to the relevant administrator, never a password or key.
- Project change or departure: request an access adjustment or revocation.
- Suspected credential exposure: stop using it and contact the administrator for immediate rotation.

!!! warning "Sensitive information"
    Approved service addresses, hostnames, and IPs may be documented, but never store passwords, private keys, API keys, tokens, Auth IDs, unattended-access passwords, or `.env` files in the Wiki.

<p class="wiki-meta">Owner: Onboarding Maintainer · Last verified: 2026-08-03</p>
