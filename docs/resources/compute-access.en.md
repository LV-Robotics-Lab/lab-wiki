# Compute Resource Requests and Selection

!!! warning "Dynamic resources"
    GPU count, online state, pricing, and quotas change over time. This page provides selection principles only; confirm current availability and authorization with the Compute Administrator before every launch.

## Purpose

Select an appropriate laboratory compute resource based on visualization needs, run duration, GPU count, and distributed-training scale.

## Prerequisites

- The project, code repository, data location, and responsible owner are defined.
- GPU type, memory, count, runtime, and storage needs have been estimated.
- A minimal run has succeeded locally or in a single-GPU environment.
- The project owner and Compute Administrator have approved any usage-billed resource.

## Resource Selection

| Task requirement | Recommended resource | Pre-launch requirement |
|---|---|---|
| Intensive visualization, real-time interaction, or remote GUI | Authorized laboratory workstation | Complete remote-access enrollment for the personal work computer |
| Standard training or temporary single-node GPU | Usage-billed GPU platform | Estimate cost; typically no more than eight GPUs on one node, subject to current platform limits |
| Continuously running single-GPU workload | Limited always-on shared server | Request a time window, storage, and responsible owner |
| Distributed training beyond one node | Cloud DLC or another distributed platform | Complete a smoke test and prepare a one-line launch command in a single-GPU development environment |
| No GPU requirement | CPU, local, or low-cost development environment | Do not occupy scarce GPU resources |

## Request Information

- Project and project-owner role
- Repository, target branch, and reproducible environment instructions
- GPU model, count, expected duration, and requested start time
- Desktop visualization, external network, data-mount, or cross-node requirements
- Single-GPU smoke-test evidence, checkpoint strategy, and one-line launch command
- Budget source and the person responsible for shutdown

## Procedure

1. Select a resource category from the table and submit the request to the **Compute Administrator**.
2. The administrator confirms live availability, cost, permissions, and data paths.
3. Run a small smoke test to validate dependencies, data loading, logs, and checkpoint writes.
4. Start the full job only after approval, recording the job ID, responsible owner, and expected end time.
5. Monitor GPUs, logs, cost, and checkpoints; stop scaling or high-cost jobs when abnormal behavior appears.
6. After completion, shut down usage-billed resources and confirm that data and checkpoints are safely stored.

## Usage Rules

- Start usage-billed resources only when needed and shut them down immediately after use; never leave an ownerless idle job running.
- A visible machine is not automatically authorized for use; re-confirm the project allocation each time.
- Do not treat a successful launch as proof of healthy large-scale training; verify real processes, GPUs, logs, and checkpoints.
- Never include passwords, tokens, or internal addresses in launch commands, environment files, or logs.
- Use approved remote-desktop channels and never store unattended-access passwords in the Wiki.

## Verification

- The smoke test completes at least one valid step and produces the expected log or checkpoint.
- GPU count, process topology, and task configuration match the approved request.
- Usage-billed resources are shut down after completion, with cost and artifacts confirmed by the responsible owner.

## Troubleshooting

- No GPU available: reduce scale, change the schedule, or ask the administrator to reallocate resources.
- Multi-GPU communication fails: retain the error summary and job ID, then confirm that the platform supports the requested topology.
- Remote desktop unavailable: verify the network path before contacting the Remote Access Maintainer.
- Data or checkpoints cannot be written: stop the full run and validate permissions and free space before resuming.
- Unexpected cost: stop the job immediately and notify the project owner and Compute Administrator.

## Maintenance

- Owner: Compute Administrator
- Contact: `<CONTROLLED_CONTACT_DIRECTORY_URL>`
- Last verified: 2026-08-03
