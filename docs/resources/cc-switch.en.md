# Configure AI APIs with CC Switch

!!! info "Scope"
    This guide uses the CC Switch graphical interface to manage the lab API configuration for Claude Code and Codex on Windows, macOS, and Linux.

!!! danger "Enter only your personal key"
    Every member must use their own API key. Never paste a key into the Wiki, source code, chat, screenshots, or Git commits.

## Purpose

Configure the lab AI API and Codex relay as separate CC Switch providers, then switch between providers without manually editing CLI configuration files.

## Prerequisites

- You have received a personal API key and model permissions through [AI API Access and Usage](ai-api-access.en.md).
- You have installed the required [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) or [Codex CLI](https://github.com/openai/codex).
- You have confirmed the available `<MODEL_ID>` with the administrator; do not guess a model name from another person's configuration.
- Your system meets the CC Switch requirements: Windows 10+, macOS 12+, or a supported mainstream Linux distribution.

## Install CC Switch

Download CC Switch only from the [official website](https://ccswitch.io) or [GitHub Releases](https://github.com/farion1231/cc-switch/releases/latest).

| System | Recommended method |
|---|---|
| Windows | Download the `.msi`; use `Windows-Portable.zip` if you need a portable build |
| macOS | Run `brew install --cask cc-switch`, or download the `.dmg` |
| Debian / Ubuntu | Download the `.deb` matching your CPU architecture |
| Fedora / RHEL / openSUSE | Download the `.rpm` matching your CPU architecture |
| Other Linux | Download the `.AppImage` matching your CPU architecture, make it executable, and run it |

After installation, start CC Switch and confirm that its window and system-tray icon appear. See the [official installation guide](https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/1-getting-started/1.2-installation.md) for full details.

## Configure Claude Code

1. Select **Claude Code** in the application switcher at the top.
2. Click **+** in the upper-right corner, then select **App-specific provider** and **Custom**.
3. Enter these fields:

    | Field | Value |
    |---|---|
    | Name | `Lab AI API` |
    | API Key / Authentication | `<AI_API_KEY>` |
    | Base URL | `https://kjapi.botsmart.net` |
    | Model | The administrator-confirmed `<MODEL_ID>` |

4. If the form displays an authentication-field selector, keep the custom provider default. Switch between `ANTHROPIC_API_KEY` and `ANTHROPIC_AUTH_TOKEN` only when the administrator explicitly instructs you to do so.
5. Save the provider, then click **Enable** on the `Lab AI API` card.

CC Switch writes the selected provider into the Claude Code configuration. Do not also keep the same variables in a shell startup file, because stale environment variables may override the graphical configuration.

## Configure The Codex Relay

1. Select **Codex** in the application switcher at the top.
2. Click **+** in the upper-right corner, then select **App-specific provider** and **Custom**.
3. Enter these fields:

    | Field | Value |
    |---|---|
    | Name | `Lab Codex Relay` |
    | API Key | `<AI_API_KEY>` |
    | Base URL | `https://cpa114515.somnia.ltd/v1` |
    | Wire API / Protocol | `Responses` |
    | Model | The administrator-confirmed `<MODEL_ID>` |
    | Requires OpenAI Auth | On |

4. Do not enable **Goal mode**, local routing, or protocol conversion; the lab relay uses a native Responses configuration.
5. Save the provider, then click **Enable** on the `Lab Codex Relay` card.
6. Close every running Codex process and reopen the terminal so the new configuration takes effect.

!!! note "Why the Base URL includes `/v1`"
    A custom Codex provider needs the API root path. The login-page address is for account management; the CLI configuration must use `https://cpa114515.somnia.ltd/v1`.

## Verification

1. Create an empty directory that contains no research data.
2. Start `claude` or `codex` and send a minimal test such as “Reply only with OK.”
3. Confirm that the request succeeds, and ask the administrator to check the personal usage record when necessary.
4. After the test, inspect the terminal, screenshots, and Git status to confirm that no API key was displayed or written.

## Troubleshooting

| Symptom | Action |
|---|---|
| `401` or `403` | Re-enter your personal key and ask the administrator to verify account permissions; do not send a key screenshot |
| `404` or protocol error | For Codex, check that the Base URL includes `/v1` and the protocol is `Responses`; for Claude Code, confirm that you did not use the Codex relay |
| Model unavailable | Use the administrator-confirmed model ID; do not copy another person's model name |
| The CLI still uses the old service | Exit the CLI completely; for Codex, also reopen the terminal |
| CC Switch reports an environment-variable conflict | Remove or temporarily unset stale API Base URL variables from the shell or PowerShell user environment, then restart the terminal |
| Unexpected usage | Disable the provider immediately and ask the administrator to revoke and rotate the key |

## Maintenance

- Owner: `@赖咏曦` (Yongxi Lai)
- CC Switch: [official website](https://ccswitch.io) · [source and releases](https://github.com/farion1231/cc-switch) · [provider setup manual](https://github.com/farion1231/cc-switch/blob/main/docs/user-manual/en/2-providers/2.1-add.md)
- AI API: `https://kjapi.botsmart.net`
- Codex relay: `https://cpa114515.somnia.ltd`
- Last verified: 2026-08-18
