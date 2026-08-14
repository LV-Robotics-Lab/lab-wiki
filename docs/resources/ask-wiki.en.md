# Ask the Wiki with AI

## Purpose

The `ask-wiki` Skill makes AI read the deployed Wiki at question time, cite full pages, and identify the responsible maintainer when public documentation is insufficient.

!!! info "No Wiki checkout required"
    Only the lightweight Skill is installed locally. The index and page content remain on the public website; Git, Python, MkDocs, and a Wiki repository checkout are not required.

## Prerequisites

- A Codex client with Skills support and the `skill-installer` Skill available.
- Network access to `https://lv-robotics-lab.github.io/lab-wiki/`.
- A question about public Wiki content; the Skill does not sign into internal systems or read the controlled directory.

## Installation

Paste this directly into a Codex conversation:

```text
$skill-installer https://github.com/LV-Robotics-Lab/lab-wiki/tree/main/plugins/lv-lab-wiki/skills/ask-wiki
```

After installation, start a new conversation so Codex reloads its Skills. Use `/skills` to confirm that `ask-wiki` appears.

If the lab has enabled the `lv-lab-wiki` Plugin in a ChatGPT workspace, no standalone local installation is needed; select `@ask-wiki` in the conversation.

## Usage

Invoke the Skill explicitly in Codex:

```text
$ask-wiki How do I use device-code login for an official Codex subscription?
```

It can also answer cross-page questions:

```text
$ask-wiki What compute allocation and remote-access steps apply before I use a GPU from outside the lab?
```

Codex supports `$ask-wiki` and the Skill selector under `/skills`. A regular Skill cannot register an arbitrary top-level `/ask_wiki` command, so do not use `/ask_wiki` as the entry point.

## Answers and Maintainer Escalation

A normal answer includes direct steps, the cited page URL, and the page's last-verified date. The Skill reads the compact index and then one to three relevant full pages; it does not answer from search summaries alone.

It stops inferring and identifies the maintainer when:

- no page directly supports the answer;
- pages conflict, appear stale, or cannot establish current state;
- the question requires approval, authorization, an exception, or restricted access; or
- the question involves a password, API key, token, cookie, private key, or authentication code.

When only a role is public, the answer directs the user to the lab controlled directory instead of inventing personal contact details.

## Verification

After installation, run:

```text
$ask-wiki How do I use device-code login for an official Codex subscription?
```

The answer should include `codex login --device-auth`, the Codex CLI Wiki page URL, and the verification date `2026-08-14`. An answer with only a command and no live citation indicates that the Skill was not loaded correctly.

## Updating and Removing

- Plugin users update or remove `lv-lab-wiki` through the client Plugin manager.
- Standalone Skill users remove the existing `ask-wiki` through the client Skill manager first, then install the updated version from the same public GitHub directory.
- Start a new conversation after an update or removal so the client reloads Skills.

## Troubleshooting

| Symptom | Action |
|---|---|
| `ask-wiki` is absent from `/skills` | Run the installation prompt again, check for an installation error, and start a new conversation |
| Wiki pages are unreachable | Check public HTTPS access; the Skill reports that live verification is unavailable instead of guessing from old content |
| The compact index returns `404` | The Skill falls back to the sitemap and search index and discloses degraded discovery |
| The answer cannot identify a maintainer | Use the cited page to contact Wiki Team through the controlled directory and confirm the page owner |
| An answer requests a credential | Do not paste it; use the relevant Wiki page to request access or report exposure to its maintainer |

## Maintenance

- **Maintainers:** Wiki Team, Lab Resources Maintainer
- **Last verified:** 2026-08-14
