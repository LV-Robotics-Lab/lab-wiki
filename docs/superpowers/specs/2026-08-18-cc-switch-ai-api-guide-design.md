# CC Switch AI API Guide Design

## Goal

Add a bilingual, cross-platform CC Switch tutorial at the same Resources navigation level as **AI API Access and Usage**. The guide should let a lab member configure both the general lab AI API for Claude Code and the dedicated Codex relay without manually editing CLI configuration files.

## Scope

- Add `docs/resources/cc-switch.md` and `docs/resources/cc-switch.en.md`.
- Add both pages to the Chinese and English Resources navigation immediately after the existing AI API guide.
- Add a short link from each AI API access page to the matching CC Switch guide.
- Synchronize `ai-api-access.en.md` with the latest Chinese source on GitHub `main`, including the current Codex relay endpoint, application fields, usage warning, contacts, and verification date.
- Update the Chinese and English Resources index pages and AI index metadata for discovery.

The guide will not cover CC Switch features unrelated to provider setup, such as MCP, prompts, skills, local routing, failover, or cloud sync.

## Page Structure

Each language version will use the same section order:

1. Purpose and credential-safety warning.
2. Prerequisites and supported operating systems.
3. Installation on Windows, macOS, and Linux using official CC Switch distribution channels.
4. Configure the lab AI API as a custom Claude Code provider.
5. Configure the lab Codex relay as a custom Codex provider.
6. Enable the provider and verify it with a minimal CLI request.
7. Troubleshoot authentication, endpoint, model, stale-process, and environment-variable conflicts.
8. Maintenance details, upstream references, and last-verified date.

## Provider Configuration

The Claude Code procedure will use a custom provider named `Lab AI API`, the published Base URL `https://kjapi.botsmart.net`, the user's individual key, and a model ID supplied or confirmed by the administrator. It will explain the corresponding `ANTHROPIC_BASE_URL` and authentication fields without exposing a real credential.

The Codex procedure will use a custom provider named `Lab Codex Relay`, Base URL `https://cpa114515.somnia.ltd/v1`, the user's individual key, the `Responses` wire protocol, and a model ID supplied or confirmed by the administrator. The `/v1` suffix is included because the public endpoint responds on `/v1/models`; no authenticated model list will be copied into the Wiki.

The guide will keep the two providers separate rather than using CC Switch's unified-provider feature. This makes their different protocols and endpoints explicit and prevents a user from accidentally sending a Claude Code request to the Codex-only relay.

## Safety And Accuracy

- Use `<AI_API_KEY>` and `<MODEL_ID>` placeholders only.
- Do not include API keys, tokens, request headers, screenshots containing account details, or personal usage data.
- Link only to CC Switch's official website, GitHub repository, releases, and user manual.
- State that the administrator is the authority for enabled models and account permissions.
- Note that CC Switch stores provider credentials locally and writes the active provider into the managed CLI configuration.
- Keep CLI test prompts content-free so no restricted research data is sent during verification.

## Navigation And Discovery

The new guide will appear under Resources directly after the AI API guide in both language navigation trees. The Resources index pages will add a one-line entry for it. `docs/assets/data/ai-index.json` will gain matching Chinese and English records with aligned URLs, summaries, keywords, maintainers, and `last_verified: 2026-08-18`; its generation timestamp will also be refreshed.

## Verification

- Compare the Chinese and English headings and procedures for structural parity.
- Check that all public endpoints and official CC Switch links resolve without authentication.
- Run the AI-index validator and repository tests.
- Run `mkdocs build --strict`.
- Review the final diff for secrets, unintended files, and navigation mismatch.

