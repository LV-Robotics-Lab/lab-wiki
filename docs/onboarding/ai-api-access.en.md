# AI API Access and Usage

!!! danger "Never publish credentials"
    The Wiki records only the request process and usage rules. API Base URLs, API keys, accounts, usage details, and internal service addresses must be obtained through approved controlled channels and must never be written in the Wiki, code repositories, tickets, screenshots, or group chats.

## Purpose

Request and use lab-managed AI APIs for approved research projects within an individually attributable usage quota.

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

1. Contact the **AI Service Administrator** through the controlled laboratory directory and submit the information above.
2. The administrator confirms the research purpose, quota, model permissions, and data boundary.
3. Receive the Base URL and personal key through an approved password manager or one-time secure channel.
4. Configure credentials only in local environment variables or an approved secret manager, for example:

    ```bash
    export LAB_AI_BASE_URL="<AI_API_BASE_URL>"
    export LAB_AI_API_KEY="<AI_API_KEY>"
    ```

5. Use the administrator-provided minimal test template without printing request headers or environment variables.
6. Confirm that the test call is attributed to your personal usage record before starting the full task.

## Usage Rules

- Credentials are assigned per user and monitored; never share, forward, or use them on behalf of another person.
- Use the service only for approved research projects, not unrelated daily work.
- Multi-agent, long-running, and high-concurrency workloads can consume quota rapidly; estimate the budget and obtain approval before launch.
- Do not send unredacted personal information, restricted data, or unpublished material to an unapproved model service.
- Never leave keys in notebooks, shell history, training logs, error screenshots, or Git commits.

## Verification

- The minimal test returns the expected model result without exposing credentials in the terminal or logs.
- The administrator can see the call in the correct personal usage record.
- Code and documentation contain only placeholders such as `<AI_API_BASE_URL>` and `<AI_API_KEY>`.

## Troubleshooting

| Symptom | Action |
|---|---|
| `401` or `403` | Check whether local variables are loaded and ask the administrator to verify permissions; do not send a key screenshot |
| `429` or exhausted quota | Reduce concurrency, stop nonessential work, and request a quota review |
| Request timeout | Record the time, model, and request ID, check the network, and then report the issue |
| Unexpected usage | Stop calls immediately, revoke and rotate the key, and audit recent usage |
| Credential committed to Git | Notify the administrator and rotate it immediately; deleting the current file does not remove history exposure |

## Maintenance

- Owner: AI Service Administrator
- Contact: `<CONTROLLED_CONTACT_DIRECTORY_URL>`
- Last verified: 2026-08-03
