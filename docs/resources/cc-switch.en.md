# Configure the Lab Self-hosted OpenRouter with CC Switch

!!! info "Runbook for agents"
    This page is primarily for an agent executing a configuration task. A member supplies the operating system, target client, and maintainer-issued endpoint details, then personally enters the individual key in a local credential field.

!!! danger "Agents do not receive credentials"
    An agent must not ask the user to paste an API key, password, cookie, or complete authorization header into chat, terminal output, screenshots, or Git. Hand login, password, and permission prompts back to the user.

## Agent Execution Contract

Follow this order. Do not skip topology detection and paste a generic configuration:

1. Identify Windows, macOS, native Linux, or a Windows host plus WSL topology.
2. Confirm whether the target is Claude Code, Claude Desktop, or both; their configurations are separate.
3. Distinguish the administrative URL, Anthropic Messages endpoint, and OpenAI endpoint in the maintainer-supplied information.
4. Preserve unrelated CC Switch providers; add or update only `Lab Self-hosted OpenRouter`.
5. Have the user enter the key in CC Switch or an approved local credential field; do not read or repeat it.
6. Apply the model and thinking-effort allowlists on this page.
7. Inspect configuration, then perform a real minimal inference request; `/models` alone does not complete verification.
8. When client configuration is correct but server scheduling fails, stop reinstalling and route the issue to the maintainer.

## Required Inputs

| Input | Source | Purpose |
|---|---|---|
| Operating system and deployment topology | Agent detection, confirmed by the user | Select the Windows, macOS, Linux, or WSL branch |
| Target client | User | Claude Code, Claude Desktop, or both |
| `<LAB_OPENROUTER_ADMIN_URL>` | Maintainer | Maintainer administration only; normal setup does not open it |
| `<LAB_OPENROUTER_ANTHROPIC_BASE_URL>` | Maintainer | Anthropic Messages endpoint for Claude Code |
| `<LAB_OPENROUTER_OPENAI_BASE_URL>` | Maintainer | OpenAI-compatible clients; never a substitute for the Messages endpoint |
| `<LAB_OPENROUTER_API_KEY>` | User enters locally | Individual authentication; never send it to an agent |
| `<LOCAL_CLAUDE_GATEWAY_URL>` | Agent detects or local maintainer supplies | Used when Claude Desktop needs compatibility adaptation |

## Platform And Deployment-Topology Decision

```text
Where does CC Switch run?
├─ Windows, with Claude on Windows -> Windows branch
├─ macOS, with Claude on macOS -> macOS branch
├─ Linux desktop, with Claude on Linux -> Linux branch
└─ CC Switch on Windows, Claude Code inside WSL -> WSL branch
```

Do not infer the platform from terminal appearance. Inspect the operating system and the environment containing the Claude executable, then report the selected branch. Enabling a provider in Windows CC Switch does not prove that Claude Code inside WSL reads the same configuration.

## Install CC Switch

Obtain CC Switch only from the [official website](https://ccswitch.io) or [GitHub Releases](https://github.com/farion1231/cc-switch/releases/latest).

### Windows

1. Install the `.msi`, or use `Windows-Portable.zip` for a portable build.
2. Start CC Switch and confirm that its window and system-tray icon appear.
3. The agent may inspect the version and window state; the user handles installation confirmation, administrator prompts, and security prompts.
4. After changing a provider, fully exit stale Claude processes and reopen the target client.

### macOS

1. Run `brew install --cask cc-switch`, or install the `.dmg` from the official release page.
2. The user handles any first-launch system security prompt.
3. After changing a provider, exit and reopen both CC Switch and Claude.
4. Check `~/.zshrc`, `~/.bashrc`, and launch services for a stale Claude Base URL. Report only whether a variable exists; never print its value.

### Linux

1. Use the architecture-matched `.deb` on Debian/Ubuntu, `.rpm` on Fedora/RHEL/openSUSE, or `.AppImage` on another supported distribution.
2. Confirm that CC Switch and Claude Code run as the same user and can write the configuration directory.
3. Restart the terminal session and Claude Code after changing the provider.
4. Check shell configuration and user services for variables that override CC Switch without displaying credential values.

### WSL

1. Record the Windows host that runs CC Switch and the WSL distribution that runs Claude Code separately.
2. Create the provider in Windows CC Switch, then inspect the configuration path and environment variables that Claude Code actually reads inside WSL.
3. Do not copy Windows paths, scheduled tasks, or loopback addresses directly into Linux configuration; first verify that WSL can reach the intended endpoint.
4. If only Claude Code runs inside WSL, do not modify Claude Desktop.
5. Close the old WSL shell, reopen it, and perform minimal verification.

See the [official CC Switch installation guide](https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/1-getting-started/1.2-installation.md) for full installation details.

## Configure Claude Code

1. Select **Claude Code** at the top of CC Switch.
2. Click **+**, then choose **App-specific provider** and **Custom**.
3. Enter:

    | Field | Value |
    |---|---|
    | Name | `Lab Self-hosted OpenRouter` |
    | API Key / Authentication | `<LAB_OPENROUTER_API_KEY>`, entered locally by the user |
    | Base URL | `<LAB_OPENROUTER_ANTHROPIC_BASE_URL>` |
    | Default model | `claude-sonnet-5` |
    | Default thinking effort | `medium` |

4. Switch between `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` only when the maintainer explicitly requires it.
5. Save and enable the provider.
6. Inspect the generated non-secret Base URL, model, and provider name; never output the authentication value.
7. Remove or temporarily unset a stale Base URL variable that overrides this provider, then reopen Claude Code.

Do not put `<LAB_OPENROUTER_OPENAI_BASE_URL>` in a Claude Code Anthropic Messages profile. See [Codex CLI Profiles and Subscription Login](codex-cli.en.md) for the Codex OpenAI `Responses` configuration.

## Configure Claude Desktop

Claude Desktop's custom inference-gateway profile is separate from Claude Code. Do not skip this section merely because the Claude Code provider works in CC Switch.

1. Check whether Desktop can use `<LAB_OPENROUTER_ANTHROPIC_BASE_URL>` directly. When Desktop calls auxiliary routes that the relay lacks, use an approved local compatibility adapter.
2. The Desktop inference profile contains at least these non-secret fields; the user enters the real key locally:

    ```json
    {
      "inferenceProvider": "gateway",
      "inferenceGatewayBaseUrl": "<LOCAL_CLAUDE_GATEWAY_URL>",
      "inferenceGatewayAuthScheme": "bearer",
      "inferenceGatewayApiKey": "<LAB_OPENROUTER_API_KEY>",
      "inferenceModels": [
        "claude-sonnet-5",
        "claude-sonnet-4-6",
        "claude-opus-5",
        "claude-opus-4-8",
        "claude-opus-4-7",
        "claude-fable-5"
      ]
    }
    ```

3. The local adapter must forward Messages calls and provide compatible handling for Desktop's token-count request. A missing remote `/count_tokens` route must not permanently classify a local account as invalid.
4. Use a per-user persistence mechanism: a logon-start user task with retry on Windows, a LaunchAgent on macOS, and a systemd user service on native Linux when available. Do not create a system-wide service without approval.
5. Restart Desktop, confirm that the model selector contains only approved models, and perform a real minimal conversation.

## Model Allowlist

| Priority | Model ID | Policy |
|---|---|---|
| Default | `claude-sonnet-5` | Routine coding and agent tasks |
| Compatibility fallback | `claude-sonnet-4-6` | When Sonnet 5 is unavailable or incompatible |
| Strong reasoning | `claude-opus-5` | Preferred escalation for difficult tasks |
| Opus fallback | `claude-opus-4-8` | When Opus 5 is unavailable |
| Opus fallback | `claude-opus-4-7` | Further compatibility fallback |
| Long-horizon specialist | `claude-fable-5` | Only when the task needs it and the budget permits |

The agent must not add another model from `/models` output or bypass the allowlist with a floating model alias.

## Thinking-Effort Policy

| Effort | Allowed | Use condition |
|---|---|---|
| `low` | Yes | Extraction, formatting, and repetitive work |
| `medium` | Yes, default | Routine coding and general agent work |
| `high` | Yes | Difficult debugging, multi-step reasoning, or high-risk changes |
| `xhigh` | Yes, maximum | When `high` is insufficient or the task is unusually complex; the UI may label it Extra High |
| `max` | No | Above the lab profile limit |
| `ultra` | No | Above the lab profile limit |

When quality permits, reduce effort or use Sonnet before escalating to a more expensive model. Treat every unlisted effort as unapproved.

## Verification

- [ ] CC Switch shows `Lab Self-hosted OpenRouter` as enabled.
- [ ] The generated Base URL, model, and protocol are correct, and inspection did not print the key.
- [ ] No stale environment variable overrides the CC Switch provider.
- [ ] When supported, `/models` discovers the target model; this is discovery only.
- [ ] A content-free `Reply OK` request completes successfully with the selected model.
- [ ] Claude Desktop completes both `/count_tokens` and Messages flows.
- [ ] No credential appears in terminal output, logs, screenshots, or Git status.

## Troubleshooting Decision Tree

| Symptom | Owner | Agent action |
|---|---|---|
| `401` or `403` | Local credential or account permission | Check only that a credential exists, without displaying it. Escalate if the error persists |
| Messages route returns `404` | Protocol or Base URL | Confirm the Anthropic Messages endpoint, not an OpenAI endpoint or admin address |
| `/count_tokens` returns `404` | Desktop compatibility layer | Inspect token-count handling in the local adapter; do not classify the key as invalid |
| `429` | Quota or concurrency | Reduce concurrency, pause nonessential calls, and request quota review |
| `503 No available accounts` | Server scheduler | Stop reinstalling the client; the maintainer checks account health and schedulability |
| `/models` succeeds but inference fails | Model mapping or account group | Record model, time, and request ID; the maintainer performs minimal inference and checks eligibility |
| Accounts repeatedly disable after an upstream error | Server error isolation | The maintainer checks health, scheduling, and Pool Mode; members must not change them |
| `<LOCAL_CLAUDE_GATEWAY_URL>` is unreachable | Local adapter | Check the user startup mechanism, listener, and process recovery before changing the remote pool |

Pool Mode, account groups, upstream account activation, and model mappings are maintainer operations. The public runbook defines the diagnostic boundary without providing admin credentials or a privileged-console walkthrough.

## Maintenance

- Owners: Lab Resources Maintainer, `@赖咏曦` (Yongxi Lai)
- CC Switch: [official website](https://ccswitch.io) · [source and releases](https://github.com/farion1231/cc-switch) · [provider setup manual](https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/2-providers/2.1-add.md)
- Platform and credential requests: [AI API Access and Usage](ai-api-access.en.md)
- Last verified: 2026-09-11
