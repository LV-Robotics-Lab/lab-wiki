# Remote Access and Private-Network Enrollment

!!! danger "Never publish network inventory"
    The Wiki must not store control-server addresses, tailnet IPs, hostnames, device inventories, pre-authentication keys, Auth IDs, SSH targets, remote-control codes, or passwords.

## Purpose

Enroll an approved personal work computer in the laboratory's self-hosted private network to access workstations or services assigned to a project.

## Prerequisites

- Use only a personally managed work computer, never a public or unmanaged device.
- Obtain access approval from the project owner and Network Administrator.
- Update the operating system and enable disk encryption, screen locking, and a local account password.
- Confirm the required resource, purpose, and expected access period.
- Install an official Tailscale client; do not use packages from unknown sources.

## Request Information

| Field | Description |
|---|---|
| Project | Project and project-owner role |
| Device | Operating system, device type, and proposed unique device name |
| Access target | Required resource category; do not include internal addresses |
| Purpose | Visualization, development, inference, file access, or operational support |
| Period | Expected start and end dates |

## Client Installation and Login

### macOS

1. Install the client through an official Tailscale channel and allow the network extension when macOS prompts.
2. Add the administrator-provided custom control server in the client settings, or run this in a terminal with the CLI configured:

    ```bash
    tailscale login --login-server=<HEADSCALE_URL>
    ```

3. Do not paste the control-server address, browser registration page, or complete terminal output into public chats or Issues.

### Windows

1. Install the client through an official Tailscale channel and add the custom control server under controlled administrator guidance.
2. Run this in PowerShell:

    ```powershell
    tailscale login --login-server=<HEADSCALE_URL>
    ```

3. If the command is not on `PATH`, use the installed client UI or ask the Network Administrator to confirm the local installation method.

### Linux

1. Install and start the client using the [official Tailscale Linux instructions](https://tailscale.com/docs/install/linux).
2. Run:

    ```bash
    sudo tailscale up --login-server=<HEADSCALE_URL>
    ```

3. Do not place the control-server address in public scripts, images, or repositories.

## Auth ID Registration

1. After the login command, the browser or terminal displays one-time registration information.
2. Send only the **Auth ID**, proposed device name, project, and access period to the Network Administrator through a controlled channel; do not forward the complete page or log.
3. The administrator registers the Auth ID to the correct member identity and applies project-scoped access rules.
4. Reconnect the client and confirm that the device has a unique name and does not reuse another node's identity.
5. Never publish Auth IDs or pre-authentication keys in the Wiki; non-interactive enrollment requires separate approval.

## SSH Public-Key Authorization

### Generate a Public Key

macOS or Linux:

```bash
test -f ~/.ssh/id_ed25519.pub || ssh-keygen -t ed25519 -C "<MEMBER_OR_DEVICE_NAME>"
cat ~/.ssh/id_ed25519.pub
```

Windows PowerShell:

```powershell
ssh-keygen -t ed25519 -C "<MEMBER_OR_DEVICE_NAME>"
Get-Content "$env:USERPROFILE\.ssh\id_ed25519.pub"
```

!!! warning "Submit the public key only"
    Submit only the public key ending in `.pub`. Never upload, forward, or copy a private-key file to an administrator.

### Submit Authorization

Through a controlled channel, submit the public key, requested resource category, project, period, and target account role. The administrator grants access through controlled configuration or automation; the Wiki does not publish server paths, real accounts, or `authorized_keys` locations.

### Verify SSH

```bash
ssh -o BatchMode=yes -o PasswordAuthentication=no <SSH_USERNAME>@<AUTHORIZED_HOSTNAME> hostname
```

OpenSSH public-key authorization and Tailscale SSH are separate mechanisms. Tailscale SSH is enabled only through administrator and access-policy decisions; members must not change server configuration themselves.

## Procedure

1. Contact the **Network Administrator** through the controlled directory and submit the request information.
2. The administrator confirms the device, project permissions, and allowed resource scope.
3. Receive enrollment information through a one-time or short-lived secure channel; never forward it.
4. Complete the client login and Auth ID registration for the relevant operating system.
5. If SSH is required, submit your own independent public key and wait for authorization on the target resource.
6. After enrollment, verify only authorized targets and do not scan or attempt to access other nodes.
7. Revoke the old device and public-key access when the project ends, the device changes, or the member leaves.

## Usage Rules

- Use the private network only for research collaboration and approved resource access, not unrelated traffic forwarding.
- Never share node identities, pre-authentication keys, SSH private keys, or unattended-access passwords.
- Do not paste complete network status, IPs, hostnames, or error screenshots into public Issues or the Wiki.
- Confirm the current path and authorization before remote-desktop use; network reachability does not authorize device operation.
- After temporary support, close sharing, revoke one-time permissions, and review the remote session.

## Verification

```bash
tailscale status
tailscale ip -4
tailscale netcheck
tailscale ping <AUTHORIZED_HOSTNAME>
```

- The administrator sees the device as an independent node with the expected identity.
- Only approved resources are reachable, and the project service, SSH, or remote desktop works as expected.
- SSH verification does not fall back to password authentication.
- No network inventory or credentials appear in terminal output, screenshots, or documentation.

## Troubleshooting

- The login command does not produce an Auth ID: confirm that the controlled control-server value was entered correctly, then check the client version and network state.
- The device appears as another node: stop using it and re-enroll with independent state to avoid disconnecting an active device.
- A node is visible but not interactive: validate the current direct or relay path and target service ports; do not rely on the online label alone.
- SSH still requests a password: confirm that the correct public key was submitted, the target account is authorized, and the matching local private key is in use; never place a password in a script.
- Remote desktop is slow: record the time and connection type, then ask the Network Administrator to inspect the path.
- Device lost or member leaving: revoke the node and related temporary credentials immediately.
- On-site support required: use the controlled directory to contact the duty maintainer; do not publish personal locations.

## References

- [Headscale node-registration documentation](https://headscale.net/stable/ref/registration/)
- [Tailscale custom control-server documentation](https://tailscale.com/docs/how-to/set-up-custom-control-server)
- [Tailscale Linux installation](https://tailscale.com/docs/install/linux)

## Maintenance

- Owner: Network Administrator
- Contact: `<CONTROLLED_CONTACT_DIRECTORY_URL>`
- Last verified: 2026-08-03
