# AI API Access and Usage

!!! info "Confirm before using the API"
    Use only your individually approved API key, and never paste credentials into the Wiki, source code, or chat.

!!! danger "Endpoint and credential boundary"
    Only service addresses approved by the Wiki maintainers may appear publicly. API keys, access tokens, passwords, cookies, request headers, internal addresses, account-pool identities, and personal usage details must never be published.

## Purpose

Request and use lab-managed AI APIs for approved research projects, while enabling an agent to distinguish protocols, endpoint types, and failure ownership.

## Current Service Endpoints

| Service | Address | Request or support |
|---|---|---|
| Laboratory AI API | [https://kjapi.botsmart.net](https://kjapi.botsmart.net) | `@赖咏曦` (Yongxi Lai) |
| Laboratory Codex relay | [https://cpa114515.somnia.ltd](https://cpa114515.somnia.ltd) | `@赖咏曦` (Yongxi Lai) |
| Lab Self-hosted OpenRouter | Supplied by a maintainer through a secure channel; its deployed address is not published here | Lab Resources Maintainer |

When configuring Claude Code or Claude Desktop, the agent must continue to [Configure the Lab Self-hosted OpenRouter with CC Switch](cc-switch.en.md) instead of guessing client fields from this page alone.

## Lab Self-hosted OpenRouter

The Lab Self-hosted OpenRouter is an independently deployed AI inference-routing platform. It can manage several protocol endpoints, model mappings, schedulable account groups, and audited upstream accounts. The platform name does not make every endpoint Claude-compatible: the client must use the inference endpoint matching its wire protocol.

### Request Flow

```text
Claude Code / Claude Desktop
  -> CC Switch managed provider
  -> Anthropic Messages-compatible endpoint
  -> optional local compatibility adapter
  -> schedulable account group
  -> audited Anthropic upstream
```

### Endpoint Boundary

| Value | Purpose | Agent rule |
|---|---|---|
| `<LAB_OPENROUTER_ADMIN_URL>` | Administrative console | Maintainers manage account groups here; never use it as a client Base URL |
| `<LAB_OPENROUTER_ANTHROPIC_BASE_URL>` | Anthropic Messages inference endpoint | Use for Claude Code; preserve the exact trailing path supplied by the maintainer |
| `<LAB_OPENROUTER_OPENAI_BASE_URL>` | OpenAI-compatible inference endpoint | Use for Chat Completions or Responses clients; never put it directly in a Claude Messages profile |
| `<LAB_OPENROUTER_API_KEY>` | Individual access credential | The user enters it only in local CC Switch or an approved secret manager |
| `<LOCAL_CLAUDE_GATEWAY_URL>` | Optional local Claude Desktop compatibility endpoint | Use only when Desktop needs protocol adaptation; it is not the remote admin address |

Keep these findings separate:

- Reaching the administrative console does not prove that inference is healthy.
- Listing a model through `/models` does not prove that the model can complete a real inference request.
- Calling a Claude-named model through an OpenAI schema does not prove Anthropic Messages compatibility.
- A live local adapter does not prove that the server-side account pool has an eligible account.

## Prerequisites

- You are participating in a defined laboratory research project and have project-owner approval.
- A maintainer has supplied your personal key, the correct protocol endpoint, and your approved model scope.
- You have estimated the model class, call volume, expected duration, and whether high concurrency or multiple agents are required.
- You have read the laboratory requirements for data security, code commits, and credential handling.

## Request Information

| Field | Description |
|---|---|
| Project | Research project and project-owner role |
| Purpose | Research task to be completed |
| Client | Claude Code, Claude Desktop, Codex, or another tool |
| Protocol | Anthropic Messages, OpenAI Responses, or Chat Completions |
| Model requirement | Required model class or capability; do not include credentials |
| Data boundary | Whether unpublished research data or other restricted content is involved |
| Requester | Personal account identifier; each user receives separate credentials |

## Procedure

1. Contact `@_嗯` or `@赖咏曦` (Yongxi Lai) and submit the information above.
2. The administrator confirms the research purpose, quota, protocol, model permissions, and data boundary.
3. Receive the personal key and corresponding Base URL through an approved password manager or one-time secure channel.
4. Enter `<LAB_OPENROUTER_API_KEY>` in local CC Switch or an approved secret manager; never send the real value to an agent.
5. Have the agent follow the [CC Switch runbook](cc-switch.en.md) to detect the operating system, configure the provider, and perform minimal verification.
6. Confirm that a real inference call succeeds and is attributed to the correct personal usage record before starting the full task.

## Usage Rules

- Credentials are assigned per user and monitored; never share, forward, or use them on behalf of another person.
- Use the service only for approved research projects, not unrelated daily work.
- Multi-agent, long-running, and high-concurrency tasks can consume quota rapidly; estimate the budget and obtain approval before launch. Do not use Goal mode.
- Do not send unredacted personal information, restricted data, or unpublished material to an unapproved model service.
- Never leave keys in notebooks, shell history, training logs, error screenshots, or Git commits.
- Do not bypass the approved model and thinking-effort policy through aliases or handcrafted requests.

## Verification

- The client protocol matches the Base URL type.
- A minimal real inference request returns the expected result; `/models` alone is not completion evidence.
- When Claude Desktop uses a local adapter, both token-count and Messages flows work.
- The administrator can see the call in the correct personal usage record.
- No credential or unapproved internal address appears in terminals, logs, screenshots, or Git status.

## Troubleshooting

| Symptom | Action |
|---|---|
| `401` or `403` | Check local credential loading and ask the administrator to verify permissions; do not send a key screenshot |
| A Messages route returns `404` | Check for an OpenAI-compatible endpoint or an incorrect trailing Base URL path |
| `/count_tokens` returns `404` | Treat this as a Desktop compatibility gap, not immediate evidence of a bad key; inspect the local adapter |
| `429` or exhausted quota | Reduce concurrency, stop nonessential work, and request a quota review |
| `503 No available accounts` | No upstream account is currently schedulable; do not reinstall the client, and route the issue to the maintainer |
| `/models` succeeds but real inference fails | Record the model ID, time, and request ID so the maintainer can inspect mapping and account-group eligibility |
| Unexpected usage or suspected exposure | Stop calls immediately, revoke and rotate the key, and audit recent usage |

## Maintenance

- Owners: `@_嗯`, `@赖咏曦` (Yongxi Lai), Lab Resources Maintainer
- AI API: [https://kjapi.botsmart.net](https://kjapi.botsmart.net)
- Codex relay: [https://cpa114515.somnia.ltd](https://cpa114515.somnia.ltd)
- Lab Self-hosted OpenRouter: deployment details are supplied through a controlled channel
- Last verified: 2026-09-11
