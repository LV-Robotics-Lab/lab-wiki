# Codex CLI Profiles and Subscription Login

!!! info "These are two different problems"
    `--profile` switches configuration such as the model, relay, approval policy, or sandbox. It does not switch the ChatGPT account. To use multiple ChatGPT subscription accounts on one machine, give each account a separate `CODEX_HOME`.

!!! danger "Credential boundary"
    Never commit an API key, `auth.json`, device code, cookie, or complete environment-variable value to Git, the Wiki, an issue, a chat record, or a screenshot. All secrets and endpoints in this guide are placeholders.

## Purpose

This guide gives laboratory members copy-ready patterns for:

- creating a separate profile for each OpenAI-compatible relay;
- signing in to Codex CLI with a ChatGPT subscription instead of treating subscription credentials as an API key;
- using device-code login and separate state directories on headless hosts or when multiple accounts are needed.

## Prerequisites

- A recent Codex CLI that responds to `codex --version`.
- Either an approved relay endpoint and personal API key, or a ChatGPT subscription account with Codex access.
- Bash or Zsh. Windows users should translate the environment-variable and function examples to PowerShell.
- A machine and working directory that you are authorized to operate.

## Understand the configuration layers first

Codex uses `~/.codex` as its default user configuration directory. You can override it with `CODEX_HOME`. With `--profile relay`, Codex reads:

```text
~/.codex/config.toml
~/.codex/relay.config.toml
```

The profile file overlays the base file, so it only needs to contain differences. Trusted project `.codex/config.toml` files, CLI flags, and `--config` overrides have higher precedence.

`--profile` changes configuration only. It does not isolate:

- ChatGPT or API-key credentials;
- session history, logs, or caches;
- other local state under `CODEX_HOME`.

For account or complete state isolation, see [Isolate multiple subscription accounts](#multi-subscription-accounts).

## Create a relay profile

This example names the profile `relay`. Profile names may contain letters, numbers, hyphens, and underscores.

### 1. Create the file

```bash
mkdir -p ~/.codex
nano ~/.codex/relay.config.toml
```

Paste the following content and replace the four placeholders for your service:

```toml
# ~/.codex/relay.config.toml
model = "gpt-5.6-sol"
model_provider = "relay"
model_reasoning_effort = "low"

[model_providers.relay]
name = "Approved Relay"
base_url = "<RELAY_BASE_URL>/v1"
env_key = "BOTSMART_API_KEY"
wire_api = "responses"
```

| Setting | Meaning |
|---|---|
| `relay` | Provider ID; `model_provider` and the provider table must match |
| `Approved Relay` | Display name shown by the CLI |
| `<RELAY_BASE_URL>/v1` | OpenAI-compatible Base URL supplied by the maintainer |
| `BOTSMART_API_KEY` | Environment-variable name, not the key itself |

For an approved laboratory service, read [AI API Access and Usage](ai-api-access.en.md) and use your individually assigned key. Do not paste a real key, approval record, or private endpoint into this page.

### 2. Configure the API-key environment variable

Temporary configuration, valid only in the current terminal:

```bash
export BOTSMART_API_KEY="<YOUR_PERSONAL_API_KEY>"
```

You may place the export in `~/.bashrc` or `~/.zshrc`, but do not commit that file:

```bash
printf '\nexport BOTSMART_API_KEY="<YOUR_PERSONAL_API_KEY>"\n' >> ~/.bashrc
source ~/.bashrc
```

Do not run `echo $BOTSMART_API_KEY`; it prints the secret to the terminal and may leave it in history or a recording. Check only whether it is set:

```bash
if [ -n "${BOTSMART_API_KEY:-}" ]; then
  echo "BOTSMART_API_KEY is set"
else
  echo "BOTSMART_API_KEY is missing"
fi
```

### 3. Start Codex or run a task

```bash
codex --profile relay
codex exec --profile relay "Inspect the current project's tests and summarize failures"
```

Optional shortcut for an interactive terminal:

```bash
printf "\nalias codex-relay='codex --profile relay'\n" >> ~/.bashrc
source ~/.bashrc
codex-relay
```

For `codex exec`, scripts, or CI, prefer an explicit `--profile relay`; shell aliases may not be loaded in non-interactive environments.

### 4. Add a second relay

Copy the file and change only the values that differ:

```bash
cp ~/.codex/relay.config.toml ~/.codex/relay2.config.toml
nano ~/.codex/relay2.config.toml
codex --profile relay2
```

Do not add a legacy `[profiles.relay]` table to `config.toml`. Current Codex uses `~/.codex/<profile-name>.config.toml`; migrate older profile settings to that file layout.

## Sign in with a ChatGPT subscription

ChatGPT sign-in and API-key sign-in are different authentication paths. Subscription usage and features follow the ChatGPT account or workspace permissions; API-key sign-in follows OpenAI Platform API usage and billing. In this guide, “official subscription” means ChatGPT sign-in, not a relay key.

### When a browser is available

Run:

```bash
codex login
```

Choose ChatGPT sign-in in the browser and complete authorization. Then verify the authentication method:

```bash
codex login status
```

The status should show ChatGPT authentication rather than an API key.

### Headless or remote host: device-code login

OpenAI's documentation labels device-code authentication as beta. Before using it:

1. For a personal account, enable device-code login in ChatGPT security settings.
2. For a workspace account, ask the workspace administrator to enable it in workspace permissions.
3. Confirm that the terminal can reach the Codex login service.

Then run this in the terminal where Codex is installed:

```bash
codex login --device-auth
```

Open the printed login link, sign in to ChatGPT in a browser, and enter the one-time device code. Verify the result:

```bash
codex login status
```

If device-code login is unavailable, OpenAI documents two fallbacks: authenticate with `codex login` on a trusted machine with a browser and securely copy the credential cache to the remote host, or forward the default localhost callback port `1455` over SSH. Treat a copied `auth.json` as a password and use only a trusted transport and destination.

### Credential cache and logout

The CLI and IDE extension share login details. Codex may store credentials in `~/.codex/auth.json` or in the operating system credential store. A file-based `auth.json` contains access tokens:

- never commit, share, or upload it;
- never place it in a Docker image or public backup;
- if exposure is suspected, log out and sign in again, and contact the administrator when needed.

To clear the current credentials:

```bash
codex logout
```

## Isolate multiple subscription accounts { #multi-subscription-accounts }

If one machine needs two ChatGPT accounts, `--profile` alone is not enough. Set a different `CODEX_HOME` for each account and use the same directory for login, normal runs, and logout.

To prevent the system keyring from continuing to share credentials, the initialization commands below enable file credential storage in each new directory. Because `auth.json` is a plaintext secret, they also restrict the directory and configuration-file permissions. Run these initialization commands only for a new, unused directory. If configuration already exists, merge `cli_auth_credentials_store` manually instead of overwriting the file.

### Option A: specify the directory each time

```bash
install -d -m 700 "$HOME/.codex-subscription-a"
printf '%s\n' 'cli_auth_credentials_store = "file"' \
  > "$HOME/.codex-subscription-a/config.toml"
chmod 600 "$HOME/.codex-subscription-a/config.toml"
CODEX_HOME="$HOME/.codex-subscription-a" codex login --device-auth
CODEX_HOME="$HOME/.codex-subscription-a" codex login status
CODEX_HOME="$HOME/.codex-subscription-a" codex
```

Use a different directory for the second account:

```bash
install -d -m 700 "$HOME/.codex-subscription-b"
printf '%s\n' 'cli_auth_credentials_store = "file"' \
  > "$HOME/.codex-subscription-b/config.toml"
chmod 600 "$HOME/.codex-subscription-b/config.toml"
CODEX_HOME="$HOME/.codex-subscription-b" codex login --device-auth
CODEX_HOME="$HOME/.codex-subscription-b" codex login status
CODEX_HOME="$HOME/.codex-subscription-b" codex
```

### Option B: create safe shell functions

Add the following to `~/.bashrc` or `~/.zshrc`, then run `source ~/.bashrc` (or `source ~/.zshrc` for Zsh):

```bash
codex-sub-a() {
  CODEX_HOME="$HOME/.codex-subscription-a" codex "$@"
}

codex-sub-b() {
  CODEX_HOME="$HOME/.codex-subscription-b" codex "$@"
}
```

Log in and run Codex:

```bash
codex-sub-a login --device-auth
codex-sub-a login status
codex-sub-a

codex-sub-b login --device-auth
codex-sub-b login status
codex-sub-b
```

### Credential-storage warning

The initialization steps above set this in each directory's `config.toml`:

```toml
cli_auth_credentials_store = "file"
```

This stores credentials in the corresponding directory's `auth.json`. After the first login, run `chmod 600 "$HOME/.codex-subscription-a/auth.json"` and `chmod 600 "$HOME/.codex-subscription-b/auth.json"`, and never sync those files to a public location. With `keyring` or `auto`, credentials may be stored in the operating-system credential manager; isolation behavior depends on the OS and Codex version, so do not assume it is isolated without checking.

## Verification checklist

- [ ] `codex --version` returns a version.
- [ ] The relay profile starts with `codex --profile <PROFILE>`.
- [ ] The API key exists only in an environment variable or approved secret manager, and the check does not print it.
- [ ] `codex login status` reports ChatGPT authentication for a subscription login.
- [ ] Device-code login was completed in the intended personal account or workspace.
- [ ] Multiple accounts use different `CODEX_HOME` directories, each with an independent `login status`.
- [ ] `auth.json`, `.bashrc`, `.zshrc`, and logs are not tracked by Git.

## Troubleshooting

| Symptom | Action |
|---|---|
| `codex --profile relay` cannot find the profile | Confirm the file is `~/.codex/relay.config.toml` and the profile name exactly matches the filename |
| `401`, `403`, or missing key | Check the environment-variable name and current shell; do not print the key, and make sure `env_key` matches it |
| The profile starts but uses the default provider | Make sure `model_provider` and `[model_providers.<id>]` use the same ID, and check for a higher-precedence CLI or project override |
| `codex login` cannot open a browser | Use `codex login --device-auth`; if unavailable, use a trusted machine to copy the credential cache or forward the SSH callback |
| The device-code option is missing | Enable device-code login in ChatGPT security settings or workspace permissions; contact the administrator or OpenAI Support if it remains unavailable |
| The two accounts overwrite each other | Ensure login, normal runs, and logout all use the same `CODEX_HOME`; do not use only `--profile` to distinguish accounts |
| Authentication is unexpected or exposed | Run `codex logout` with the affected `CODEX_HOME`, remove the exposed cache, and sign in again; revoke and rotate an API key |

## Official references

- [OpenAI Docs: Authentication](https://learn.chatgpt.com/docs/auth)
- [OpenAI Docs: Advanced Configuration](https://learn.chatgpt.com/docs/config-file/config-advanced)
- [OpenAI Docs: Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

## Maintenance

- **Maintainer:** Lab Resources Maintainer
- **Last verified:** 2026-08-14
