# Research Data Storage and Archiving

!!! info "Confirm storage status live"
    The currently approved lab NAS address is `192.168.1.213`, and its SMB share name is `vols`. The endpoint may be recorded in the Wiki, but availability, capacity, and permissions must still be confirmed live.

## Purpose

Reduce the risk of datasets being scattered across personal computers and temporary training nodes, and establish a traceable process for collection, training, sharing, and archiving.

## Prerequisites

- The data owner, project, data type, and authorized members are defined.
- Personal information, participant data, unpublished results, and license-restricted content have been identified.
- The target storage and permissions have been approved; do not infer paths from old chat messages.
- Data volume, growth, retention period, and backup needs have been estimated.

## Storage Principles

- Personal computers and temporary GPU nodes hold only necessary working copies and are never the sole archive.
- Final datasets, metadata, and critical checkpoints belong in project-approved centralized storage.
- Raw data, intermediate outputs, and publishable releases should be separated with clear naming.
- Do not publish real internal addresses, paths, or share names without explicit maintainer approval. Access tokens, mount passwords, and private share links must never be published.
- Apply least privilege to restricted data and revoke access when a member leaves or a project ends.

## Accessing an Approved NAS over SMB

### Prerequisites

- Obtain an individual SMB account from the Data Storage Administrator. The current NAS address is `192.168.1.213`, its share name is `vols`, and the examples below use `<NAS_USERNAME>` for the individual account.
- For remote access, connect the device to the lab Tailscale/Headscale network and ensure that the administrator has approved the required subnet route and access rules.
- Prefer the administrator-provided IP address for remote access. Use a local name such as `.lan` only when the administrator confirms that cross-network DNS is available.
- Do not enable insecure guest access on Windows or share NAS accounts. If authentication fails, ask the administrator to verify local SMB permissions.

### macOS

1. In Finder, select **Go → Connect to Server**, or press `Command + K`.
2. Enter:

    ```text
    smb://192.168.1.213/vols
    ```

3. Select “Registered User” and enter your NAS username and password. Save the credential in Keychain only on a personally managed device.
4. You can also open the share from Terminal:

    ```bash
    open 'smb://192.168.1.213/vols'
    ```

### Windows

1. Enter the following in the File Explorer address bar:

    ```text
    \\192.168.1.213\vols
    ```

2. If Windows automatically selects a school, company, or Microsoft account, choose **More choices → Use a different account** and enter your NAS account.
3. To assign a drive letter, select **Map network drive** under “This PC,” enter the same UNC path, and select **Connect using different credentials** when required.
4. If Windows cached an incorrect credential, run the following in PowerShell or Command Prompt:

    ```powershell
    net use * /delete /y
    cmdkey /delete:192.168.1.213
    net use Z: \\192.168.1.213\vols /user:<NAS_USERNAME> *
    ```

    The trailing `*` prompts for the password interactively so that it is not stored in command history.

### Linux

Desktop file managers can open:

```text
smb://192.168.1.213/vols
```

For a command-line mount, first install the distribution-provided CIFS utilities, then run:

```bash
sudo mkdir -p /mnt/lab-nas
sudo mount -t cifs //192.168.1.213/vols /mnt/lab-nas \
  -o username=<NAS_USERNAME>,vers=3.0
```

The command prompts for the password interactively. For persistent mounts, use a credential file with mode `0600` or the operating system's secret store. Never place a plaintext password in `/etc/fstab`, scripts, or repositories.

### Network and Service Verification

Confirm the route first, then the required service port:

=== "macOS / Linux"

    ```bash
    ping 192.168.1.213
    nc -vz 192.168.1.213 445
    ```

=== "Windows PowerShell"

    ```powershell
    ping 192.168.1.213
    Test-NetConnection 192.168.1.213 -Port 445
    ```

If a Linux Tailscale client does not automatically accept an approved subnet route, run the following after confirming with the administrator:

```bash
sudo tailscale set --accept-routes=true
```

macOS and Windows normally accept approved subnet routes automatically. If traffic still uses the local default gateway, capture the route lookup and ask the network administrator to verify the route's `Approved`, `Available`, and `Serving` states in Headscale.

## Procedure

1. Submit the project, data type, capacity, and member information to the **Data Storage Administrator**.
2. The administrator confirms the target storage, permissions, directory owner, and backup policy.
3. Create a README or manifest recording source, license, version, owner, and generation method.
4. Upload a small sample and validate read, write, and permission behavior before the full transfer.
5. After transfer, compare file count, total size, and sampled checksums.
6. Remove temporary copies only after the centralized copy and backup have been confirmed.

## Verification

- The project owner and authorized members can access the data, while unauthorized members cannot.
- File count, size, and sampled checksums match the source.
- Documentation records source, version, owner, license, and last verification date.
- Critical data does not exist only on a personal device or temporary compute node.

## Troubleshooting

- Storage unreachable: confirm the service's current state and network authorization instead of repeatedly trying an old address.
- Remote access times out: confirm that Tailscale is online and the client accepted the subnet route, then ask the network administrator to verify that the route is in the `Serving` state.
- Windows says organizational policy blocks unauthenticated guest access: choose **Use a different account** and enter NAS credentials; do not weaken the guest-access security policy.
- The IP responds but the share does not open: check TCP port `445`, the share name, and SMB service status. Network reachability does not grant file permissions.
- Permission denied: ask the Data Storage Administrator to correct project access; never share another person's account.
- Insufficient space: stop bulk transfer and submit capacity and growth estimates before expansion or archiving.
- File mismatch: retain the source copy, retransmit failed files, and recheck checksums.
- Sensitive data shared accidentally: revoke access immediately, record the affected scope, and notify the project owner.

## Maintenance

- Owner: Data Storage Administrator
- Contact: `<CONTROLLED_CONTACT_DIRECTORY_URL>`
- Last verified: 2026-08-08
