# Lab OpenRouter Agent Runbook Design

## Goal

Extend the existing bilingual AI API and CC Switch documentation so an AI agent can configure and troubleshoot the lab's self-hosted OpenRouter for Claude Code and Claude Desktop. The runbook should be deterministic enough for an agent to follow without requiring a lab member to read the full guide, while retaining concise human-readable safety notices and escalation points.

The public product name is **Lab Self-hosted OpenRouter** in English and **实验室自有 OpenRouter** in Chinese. The documentation must not publish the deployed host, internal IP address, credentials, account identifiers, or personal usage data.

## Existing Pages And Plugin

The work will modify the existing structure rather than introduce a parallel guide:

- `docs/resources/ai-api-access.md`
- `docs/resources/ai-api-access.en.md`
- `docs/resources/cc-switch.md`
- `docs/resources/cc-switch.en.md`
- `docs/resources/codex-cli.md`
- `docs/resources/codex-cli.en.md`
- `docs/resources/index.md`
- `docs/resources/index.en.md`
- `docs/assets/data/ai-index.json`
- `plugins/lv-lab-wiki/skills/ask-wiki/SKILL.md`

Navigation will remain unchanged because the runbook expands existing Resources pages. The Chinese and English pages will keep matching section order and operational meaning.

## Audience And Agent Contract

The primary consumer is an AI agent invoked through the existing `ask-wiki` Skill. A human may inspect the page, but the operational content will be optimized for exact retrieval and execution.

Each relevant page will expose:

1. Purpose and scope.
2. Required inputs using named placeholders.
3. Safety constraints and actions that require human participation.
4. A platform decision branch.
5. Ordered configuration steps.
6. Machine-checkable success criteria.
7. Symptom-to-cause troubleshooting decisions.
8. Escalation conditions, maintainer role, and last-verified date.

The agent must never request that a user paste a credential into chat. It must direct the user to enter the individual credential in CC Switch or another approved local credential field. The agent may inspect non-secret configuration and status, but must redact tokens, passwords, headers, account identifiers, and personal usage before displaying output.

## Platform Architecture

The AI API page will introduce the Lab Self-hosted OpenRouter as a distinct platform and describe the following conceptual flow:

```text
Claude Code or Claude Desktop
        -> CC Switch managed provider
        -> Anthropic-compatible inference endpoint
        -> local compatibility adapter when required
        -> schedulable account group
        -> audited Anthropic-capable upstream
```

The page will distinguish:

- the administrative console from the client inference endpoint;
- Anthropic Messages-compatible endpoints from OpenAI-compatible Chat Completions or Responses endpoints;
- a model appearing in `/models` from that model completing a real inference request;
- local client health from server-side account-pool availability.

Endpoint values will use these placeholders:

- `<LAB_OPENROUTER_ADMIN_URL>`
- `<LAB_OPENROUTER_ANTHROPIC_BASE_URL>`
- `<LAB_OPENROUTER_OPENAI_BASE_URL>`
- `<LAB_OPENROUTER_API_KEY>`
- `<LOCAL_CLAUDE_GATEWAY_URL>`

Only a maintainer-approved operational endpoint may replace a placeholder in a later change. Secrets may never replace credential placeholders in the repository.

## CC Switch And Operating-System Flow

The existing CC Switch guide will be reorganized around a shared provider definition with platform-specific setup and restart branches.

### Shared Provider Definition

The provider will be named `Lab Self-hosted OpenRouter`. The agent will configure the Claude Code provider with the maintainer-supplied Anthropic-compatible base URL and the user's individual key. It will not reuse an OpenAI-only provider for Claude requests.

The runbook will explain that CC Switch manages Claude Code configuration, while Claude Desktop may require a separate inference-gateway profile and a compatibility adapter. It will explicitly prevent an agent from assuming that a successful Claude Code setup automatically configures Claude Desktop.

### Windows

Windows is the primary and most detailed path. It will cover installing CC Switch from an official distribution, selecting the Claude Code application, adding and activating the custom provider, closing stale Claude processes, reopening the client, and validating both model discovery and minimal inference.

If Claude Desktop needs a local compatibility adapter, the agent will verify the loopback listener, its startup mechanism, and the Desktop inference profile without printing the credential. Persistent startup guidance may use a per-user startup mechanism and must include a recovery check after process termination.

### macOS

The macOS branch will use the official CC Switch package or Homebrew cask, the same shared provider fields, and macOS-specific application restart and shell-environment checks. If a local adapter is required, persistence will use a per-user LaunchAgent rather than a system-wide service.

### Linux

The Linux branch will cover the supported `.deb`, `.rpm`, or AppImage distribution, the same shared provider fields, desktop-session or shell restart behavior, and stale environment-variable checks. WSL will be treated as a Linux execution environment with a Windows-hosted CC Switch only when that is the actual deployment topology. If a local adapter is required on native Linux, persistence will use a systemd user service when available.

The agent must detect the operating system and deployment topology before selecting a branch. It must not copy Windows paths or service mechanisms into macOS, native Linux, or WSL.

## Approved Model Policy

The runbook will publish an explicit allowlist instead of instructing users or agents to select any model returned by the router.

| Role | Canonical model ID | Policy |
|---|---|---|
| Default | `claude-sonnet-5` | Default for routine coding and agent tasks |
| Compatibility fallback | `claude-sonnet-4-6` | Use when Sonnet 5 is unavailable or incompatible |
| Strong reasoning | `claude-opus-5` | Preferred escalation for difficult tasks |
| Opus compatibility | `claude-opus-4-8` | Approved fallback |
| Opus compatibility | `claude-opus-4-7` | Approved fallback |
| Long-horizon specialist | `claude-fable-5` | Use only when its additional cost is justified |

The documentation will omit Fable 5.1, Haiku, unapproved legacy models, and floating `latest` aliases. An agent must not infer additional approval from `/models` output.

## Thinking-Effort Policy

The permitted effort values are:

```text
low
medium
high
xhigh
```

`xhigh` will be labeled **Extra High**. `max`, `ultra`, and any unlisted effort are prohibited in the lab profile.

The selection policy is:

- `medium` by default;
- `low` for simple extraction, formatting, and repetitive tasks;
- `high` for difficult coding, debugging, or multi-step reasoning;
- `xhigh` only after `high` fails or when the task is demonstrably high risk or unusually complex.

The agent must reduce effort or choose Sonnet before escalating to a more expensive model when quality requirements allow it. The Wiki will not publish personal usage totals or inferred per-user spending.

## Verification Contract

Configuration is successful only when all applicable checks pass:

1. CC Switch shows the intended provider as active.
2. The generated Claude configuration contains the expected non-secret base URL and approved model ID.
3. No stale environment variable overrides the CC Switch configuration.
4. Model discovery succeeds when the endpoint supports it.
5. A minimal content-free inference request returns success for the selected model.
6. Claude Desktop, when used, can complete its token-count and message flows through the configured gateway.
7. The credential does not appear in terminal output, screenshots, logs, Git changes, or Wiki content.

A `/models` response alone is not sufficient evidence that the model is usable.

## Troubleshooting Decision Tree

The runbook will map symptoms to ownership and next actions:

- `401` or `403`: local credential, authorization, or account permission; do not display the key.
- `404` on a Messages route: likely protocol or base-path mismatch.
- `404` on `/count_tokens`: compatibility adapter or upstream capability gap; do not classify it as a bad key.
- `429`: quota, concurrency, or rate limit; lower concurrency and escalate for quota review.
- `503 No available accounts`: server-side scheduler has no eligible upstream account; client reinstallation is not a remedy.
- model listed but inference fails: validate the account group's model mapping and perform a minimal request.
- repeated account disablement after an upstream error: a maintainer should review account health, scheduling state, error isolation, and Pool Mode.
- loopback gateway unavailable: check the per-user startup mechanism, listener, and process recovery before changing the remote account pool.

Pool Mode and account-group changes are maintainer-only actions. The public instructions will describe the diagnostic boundary without publishing account names, console credentials, privileged URLs, or a click-by-click administrative access path.

## `ask-wiki` Retrieval Behavior

The existing Skill will gain a focused routing rule for Lab Self-hosted OpenRouter, Claude Code, Claude Desktop, CC Switch, model selection, thinking effort, and the listed error signatures.

For configuration requests, the Skill will:

1. Fetch the current AI API and CC Switch pages.
2. Ask for the user's operating system or detect it when a supported local tool can do so.
3. Select the appropriate platform branch.
4. Preserve placeholders and require local credential entry.
5. Apply the approved model and effort allowlists.
6. Verify the real inference path, not only model enumeration.
7. Escalate server-side pool and scheduling failures to the documented maintainer role.

The Skill will continue to treat the deployed Wiki as the source of truth and will not embed a second copy of endpoint or credential data.

## Safety And Redaction

- Do not publish the credentials, email address, API key, internal IP addresses, account names, or personal usage figures present in the source conversation or machine configuration.
- Do not copy local absolute paths, scheduled-task identifiers, process IDs, or machine-specific profile identifiers into the Wiki.
- Use content-free test prompts such as `Reply OK`.
- Do not print authentication headers or dump full configuration objects during verification.
- Treat a previously shared credential as exposed and recommend rotation through the approved maintainer channel.
- Run a repository secret and internal-address scan before committing.

## Validation

Implementation will be accepted only after:

- Chinese and English section structures are compared for parity;
- the AI index includes aligned records and current keywords;
- repository tests pass;
- `mkdocs build --strict` succeeds;
- the rendered pages are checked for broken tables, admonitions, code blocks, and navigation;
- `git diff` is reviewed for secrets, private endpoints, unrequested content, and accidental generated files;
- the documented model and effort allowlists are checked exactly.

## Delivery

The implementation will be committed to the repository after validation. Pushing to GitHub and triggering the public GitHub Pages deployment will occur only after explicit user approval at the publication step, in accordance with the repository Git rules.
