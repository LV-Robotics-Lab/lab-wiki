# Compute Resource Requests and Selection

!!! warning "Configuration snapshot"
    The table below comes from the Master Course “设备情况” sheet updated on 2026-08-03. Host availability, GPU occupation, pricing, and project authorization change over time; verify them with `tailscale status`, `nvidia-smi`, and the current allocation record before launch.

## Purpose

Select an appropriate laboratory compute resource based on visualization needs, run duration, GPU count, and distributed-training scale.

## Contacts and Resource Entry Points

| Need | Contact |
|---|---|
| Headscale enrollment and visual workstations | `@nilou` (Ye Zheng) |
| AutoDL single-node workloads, normally up to eight GPUs | `@赖咏曦` (Yongxi Lai) |
| Always-on single-GPU resources | `@赵浩宇-Postdoc` or the Compute Administrator |
| Alibaba Cloud DLC training beyond eight GPUs | Contact the Compute Administrator in advance |

## Prerequisites

- The project, code repository, data location, and responsible owner are defined.
- GPU type, memory, count, runtime, and storage needs have been estimated.
- A minimal run has succeeded locally or in a single-GPU environment.
- The project owner and Compute Administrator have approved any usage-billed resource.

## Resource Selection

| Task requirement | Recommended resource | Pre-launch requirement |
|---|---|---|
| Intensive visualization, real-time interaction, or remote GUI | Authorized laboratory workstation | Complete Headscale enrollment for the personal work computer |
| Standard training or temporary single-node GPU | Usage-billed platforms such as AutoDL | Estimate cost; normally no more than eight GPUs on one node, subject to current platform limits |
| Continuously running single-GPU workload | Three always-on shared single-GPU servers | Request a time window, storage, and responsible owner |
| Distributed training beyond one node | Alibaba Cloud DLC or another distributed platform | Complete a smoke test and prepare a one-line launch command in a single-GPU development environment |
| No GPU requirement | CPU, local, or low-cost development environment | Do not occupy scarce GPU resources |

## Current Device Inventory

| Tailscale device | Tailscale IP | Device type | Compute | Current allocation | Location |
|---|---|---|---|---|---|
| `sg-ai-gateway` | `100.64.0.1` | VPS central host; not for development | No GPU | — | Cloud |
| `boris-pc-z890` | `100.64.0.32` | Shared laboratory workstation | RTX 4090 | TacHarness evaluation setup | COM4-05-01 |
| `dm-26zj-008` | `100.64.0.3` | Daimeng collaboration host | RTX 5090 | — | Daimeng company |
| `dm-26zj-020` | `100.64.0.7` | Daimeng collaboration host | RTX 5060 | — | Daimeng company |
| `autodl-container-nhpaq5ml8z-8b8d996b` | `100.64.0.33` | AutoDL server | A800 | UMI WAM | Cloud |
| `boris-pc` | `100.64.0.4` | Shared laboratory laptop | RTX 3070 Ti | Franka physical-robot control | E2-01-06 |
| `lvrobotics-System-Product-Name` | `100.64.0.34` | Shared laboratory workstation | RTX 4060 Ti | Nero physical-robot control | E2-01-06 |
| `agilex` | `100.64.0.27` | Shared laboratory workstation | RTX 4060 | Cobot physical-robot control | E2-01-06 |
| `gmlab-System-Product-Name` | `100.64.0.39` | Shared laboratory workstation | RTX 3080 | Piper physical-robot control | E2-01-06 |
| `jingxiang-B850M-C` | `100.64.0.6` | Shared laboratory workstation | RTX 5090 | Lerobot physical-robot control | E2-01-06 |
| `yuhang-B850M-C` | `100.64.0.9` | Shared laboratory workstation | RTX 5090 | UMI algorithm testing | E2-01-06 |
| `shaol-PC` | `100.64.0.5` | Shared laboratory workstation | RTX 4090 | Ego algorithm testing | COM2-01-04 |

!!! info "Access note"
    These IPs are reachable only inside the laboratory Tailscale/Headscale network. The table is a configuration and allocation snapshot, not a claim that a device is currently online or idle. AutoDL is usage-billed and is not kept online. AnyDesk device codes and login passwords are remote-access credentials and are not stored in the Wiki; request time-limited authorization through the maintainer-controlled register when remote desktop access is needed.

## Request Information

- Project and project-owner role
- Target host or resource type and whether the current allocation must change
- Repository, target branch, and reproducible environment instructions
- GPU model, count, expected duration, and requested start time
- Desktop visualization, external network, data-mount, or cross-node requirements
- Single-GPU smoke-test evidence, checkpoint strategy, and one-line launch command
- Budget source and the person responsible for shutdown

## Procedure

1. Select a resource category and submit the request to the corresponding contact.
2. The administrator confirms live reachability, GPU occupation, cost, permissions, and data paths.
3. Run a small smoke test to validate dependencies, data loading, logs, and checkpoint writes.
4. Start the full job only after approval, recording the job ID, responsible owner, and expected end time.
5. Monitor GPUs, logs, cost, and checkpoints; stop scaling or high-cost jobs when abnormal behavior appears.
6. After completion, shut down usage-billed resources and confirm that data and checkpoints are safely stored.

## Usage Rules

- Start usage-billed resources only when needed and shut them down immediately after use; never leave an ownerless idle job running.
- A host being online does not grant authorization; re-confirm the project allocation each time.
- Do not treat a successful launch as proof of healthy large-scale training; verify real processes, GPUs, logs, and checkpoints.
- Hostnames, IPs, and GPU specifications may be documented; passwords, API keys, tokens, private keys, and unattended-access passwords must not appear in commands, environment files, logs, or the Wiki.
- Use approved remote-desktop channels and never store unattended-access passwords in the Wiki.

## Verification

- The target device name and IP in `tailscale status` match the table and are currently reachable.
- `nvidia-smi` reports the approved GPU model, count, and current occupation.
- The smoke test completes at least one valid step and produces the expected log or checkpoint.
- GPU count, process topology, and task configuration match the approved request.
- Usage-billed resources are shut down after completion, with cost and artifacts confirmed by the responsible owner.

## Troubleshooting

- Device offline or IP mismatch: treat live Headscale state as authoritative and report the difference so this page can be updated.
- No GPU available: reduce scale, change the schedule, or ask the administrator to reallocate resources.
- Multi-GPU communication fails: retain the error summary and job ID, then confirm that the platform supports the requested topology.
- Remote desktop unavailable: verify the network path, then contact `@nilou` or the on-site maintainer.
- Data or checkpoints cannot be written: stop the full run and validate permissions and free space before resuming.
- Unexpected cost: stop the job immediately and notify the project owner and Compute Administrator.

## Maintenance

- Headscale and workstations: `@nilou` (Ye Zheng)
- AutoDL: `@赖咏曦` (Yongxi Lai)
- Always-on resources: `@赵浩宇-Postdoc` and the Compute Administrator
- Configuration source: Master Course → 设备情况
- Last verified: 2026-08-03
