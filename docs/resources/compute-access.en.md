# Compute Resource Requests and Selection

!!! warning "Public-page boundary"
    This page documents resource categories, request procedures, and safety requirements only. Device names, internal addresses, room locations, accounts, current allocations, and the contact directory belong in an organization-controlled internal inventory, not in the public Wiki.

## Purpose

Select an appropriate laboratory compute resource based on visualization needs, run duration, GPU count, and distributed-training scale.

## Resource Entry Points

| Need | Request channel |
|---|---|
| Headscale enrollment and visual workstations | Apply through the organization-internal administrator channel |
| AutoDL single-node workloads, normally up to eight GPUs | Submit an internal compute request |
| Always-on single-GPU resources | Request a time window from the current Compute Administrator |
| Alibaba Cloud DLC training beyond eight GPUs | Complete the internal project-approval process in advance |

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

## Internal Resource Inventory

The complete inventory is maintained in an organization-controlled internal document and contains live device identifiers, network addresses, locations, GPU specifications, project allocations, and responsible owners. Organization members should use that internal source; this public page does not copy the inventory or treat a historical snapshot as current authorization.

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
- Hostnames, internal addresses, locations, current allocations, and named contacts belong only in the controlled internal inventory. Passwords, API keys, tokens, private keys, and unattended-access credentials must not appear in repositories, Wikis, issues, logs, or screenshots.
- Use approved remote-desktop channels and never store unattended-access passwords in the Wiki.

## Verification

- An administrator has confirmed the target identity, reachability, and current authorization against live network state and the internal resource inventory.
- `nvidia-smi` reports the approved GPU model, count, and current occupation.
- The smoke test completes at least one valid step and produces the expected log or checkpoint.
- GPU count, process topology, and task configuration match the approved request.
- Usage-billed resources are shut down after completion, with cost and artifacts confirmed by the responsible owner.

## Troubleshooting

- Device offline or address mismatch: treat live Headscale state as authoritative and ask an administrator to update the internal inventory.
- No GPU available: reduce scale, change the schedule, or ask the administrator to reallocate resources.
- Multi-GPU communication fails: retain the error summary and job ID, then confirm that the platform supports the requested topology.
- Remote desktop unavailable: verify the network path, then contact the on-site maintainer through the internal channel.
- Data or checkpoints cannot be written: stop the full run and validate permissions and free space before resuming.
- Unexpected cost: stop the job immediately and notify the project owner and Compute Administrator.

## Maintenance

- Public-page maintainer: LV Robotics Lab
- Device, contact, and allocation source: the organization-controlled internal resource inventory
- This page is not evidence that a host is online, idle, or authorized for a particular user
