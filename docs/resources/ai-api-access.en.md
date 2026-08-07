# AI API Access and Usage

!!! info "Confirm before using the API"
    The laboratory AI API Base URL is **[https://kjapi.botsmart.net](https://kjapi.botsmart.net)**. Use only your individually approved API key, and never paste credentials into the Wiki, source code, or chat.

!!! danger "Addresses may be public; credentials may not"
    The Wiki may record API Base URLs, service homepages, and maintainers, but must never record API keys, access tokens, passwords, cookies, request headers, or personal usage details.

## Purpose

Request and use lab-managed AI APIs for approved research projects within an individually attributable usage quota.

## Current Service Endpoints

| Service | Address | Request or support |
|---|---|---|
| Laboratory AI API | [https://kjapi.botsmart.net](https://kjapi.botsmart.net) | `@_嗯`, `@赖咏曦` (Yongxi Lai) |
| Laboratory Codex relay | [https://goaihz.com/](https://goaihz.com/) | `@赖咏曦` (Yongxi Lai) |

!!! note "Personal keys"
    API keys are issued per user and traffic is monitored. The Base URL is public on this page, but each key must still be requested individually and must never be shared.

## Prerequisites

- You are participating in a defined laboratory research project and have project-owner approval.
- You have confirmed that the task requires the laboratory API; use personal tools for personal learning and routine work.
- You have estimated the model class, call volume, expected duration, and whether high concurrency or multiple agents are required.
- You have read the laboratory requirements for data security, code commits, and credential handling.

## Request Information

| Field | Description |
|---|---|
| Project | Research project and project-owner role |
| Purpose | Research task to be completed |
| Model requirement | Required model class or capability; do not include credentials |
| Usage estimate | Expected request volume, concurrency, and usage period |
| Data boundary | Whether unpublished research data or other restricted content is involved |
| Requester | Personal account identifier; each user receives separate credentials |

## Procedure

1. Contact `@_嗯` or `@赖咏曦` (Yongxi Lai) and submit the information above.
2. The administrator confirms the research purpose, quota, model permissions, and data boundary.
3. Receive the personal key through an approved password manager or one-time secure channel.
4. Configure credentials only in local environment variables or an approved secret manager, for example:

    ```bash
    export LAB_AI_BASE_URL="https://kjapi.botsmart.net"
    export LAB_AI_API_KEY="<AI_API_KEY>"
    ```

5. Use the administrator-provided minimal test template without printing request headers or environment variables.
6. Confirm that the test call is attributed to your personal usage record before starting the full task.

## Usage Rules

- Credentials are assigned per user and monitored; never share, forward, or use them on behalf of another person.
- Use the service only for approved research projects, not unrelated daily work.
- Goal mode, multi-agent, long-running, and high-concurrency workloads can consume quota rapidly; estimate the budget and obtain approval before launch.
- Do not send unredacted personal information, restricted data, or unpublished material to an unapproved model service.
- Never leave keys in notebooks, shell history, training logs, error screenshots, or Git commits.

## Verification

- The minimal test returns the expected model result without exposing credentials in the terminal or logs.
- The administrator can see the call in the correct personal usage record.
- Code and documentation may record `https://kjapi.botsmart.net`, but the key must remain a placeholder such as `<AI_API_KEY>`.

## Troubleshooting

| Symptom | Action |
|---|---|
| `401` or `403` | Check whether local variables are loaded and ask the administrator to verify permissions; do not send a key screenshot |
| `429` or exhausted quota | Reduce concurrency, stop nonessential work, and request a quota review |
| Request timeout | Record the time, model, and request ID, check the network, and then report the issue |
| Unexpected usage | Stop calls immediately, revoke and rotate the key, and audit recent usage |
| Credential committed to Git | Notify the administrator and rotate it immediately; deleting the current file does not remove history exposure |

## Maintenance

- Owners: `@_嗯`, `@赖咏曦` (Yongxi Lai)
- AI API: [https://kjapi.botsmart.net](https://kjapi.botsmart.net)
- Codex relay: [https://goaihz.com/](https://goaihz.com/)
- Last verified: 2026-08-07
