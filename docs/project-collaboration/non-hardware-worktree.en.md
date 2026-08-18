# Unified Collaboration for Non-Hardware Teams

## One-Line Principle

> One project, one organization repository, and one shared `main`; one personal worktree per member, with all project content kept inside the worktree and mature results merged into `main` regularly.

## Purpose

This policy manages code, experiment configurations, scripts, notes, and staged results for non-hardware team projects. It reduces migration and cleanup risks caused by personal clones, temporary directories outside the repository, and unpushed commits.

## Scope

- This policy applies to all non-hardware teams.
- It currently covers collaboration in the world-model and simulation teams.
- Any future non-hardware team uses this policy by default unless its project lead publishes an approved supplement.
- Hardware teams have additional boundaries for devices, calibration, real-time control, and experiment data; this page does not replace those requirements.

## Prerequisites

- The project uses one organization repository and has identified a repository maintainer and project lead.
- A shared workspace is available for the shared `main`, Git metadata, and public resources.
- Each member has a personal project workspace, personal branch, and the required repository permissions.
- The project lead has confirmed that large data, checkpoints, caches, and run results use the worktree-root `data/` directory and has agreed on its manifest fields.
- The repository `.gitignore` uses the root-anchored `/data/` rule for that directory without excluding same-named source subdirectories.

## Directory and Branch Model

The shared directory contains only the shared `main`, Git metadata, and public resources:

```text
/home/<SHARED_ACCOUNT>/workspace/<REPO>/
```

Each member uses an independent worktree in their own workspace:

```text
/home/<MEMBER_NAME>/<REPO>/  ->  worktree/<MEMBER_NAME>
```

In this model:

- `/home/<SHARED_ACCOUNT>/workspace/<REPO>/` is the project's only shared repository entry point and is not used for personal experiments.
- `/home/<MEMBER_NAME>/<REPO>/` is the member's daily worktree; personal code and experiment materials stay there.
- `worktree/<MEMBER_NAME>` is an example personal branch name; names must remain unique and traceable within the repository.
- Do not create a personal GitHub repository for the project or maintain a separate long-lived clone.

## Daily Workflow

1. Create or update the personal worktree and branch from the shared `main`; before working, confirm that the remote and current branch point to the correct organization repository.
2. Complete code, experiment configurations, scripts, notes, and staged results inside the personal worktree. Do not place project files in temporary directories outside the repository, Documents, or a personal clone.
3. Commit each reviewable change promptly and push the personal branch to the organization repository. Commit messages should identify the change purpose or experiment stage.
4. Regularly fetch updates from `main` and integrate them by the project's agreed merge or rebase method. Re-run affected checks and experiments after synchronization.
5. Submit a pull request for shared `main` only after the reusable functionality has been verified.
6. Keep unfinished experiments, hypothesis-specific scripts, and unstable configurations on the personal branch instead of putting them into `main` because they are temporarily usable.

## Large Files and Experiment Artifacts

- Large datasets, checkpoints, caches, and run results do not go directly into Git; keep them under the ignored `data/` directory in the project worktree, and do not create alternative top-level directories for the same payloads.
- Use `.gitignore` for local artifacts. Do not replace `data/` with a location outside the repository, and do not treat an ignored file as the only backup.
- For each important dataset or result, keep a tracked manifest recording its source, version or generating commit, file count and total size, checksum, owner, license or access boundary, storage location, and last verification date.
- To share or reproduce an experiment, commit the configuration, scripts, README, and manifest; do not commit the data itself, authentication material, or private download links.
- Important local data must have a project-approved centralized copy or backup. Before cleaning a personal worktree, confirm that the backup is readable and matches the manifest.

## Criteria for Merging into `main`

Before entering the shared `main`, a change must satisfy all of the following:

- The code, configuration, or documentation has been reviewed by the project lead or designated maintainer.
- Relevant checks, a minimal reproduction experiment, or an evaluation have passed, with the required environment and results recorded.
- The change has clear reuse value for the team and is not merely the temporary state of an unfinished experiment.
- It contains no authentication credentials, personal identifying information, restricted data, or unapproved internal addresses.
- Large artifacts are excluded by `.gitignore`, and the manifest, checksums, and source description are in Git.
- The merge will not break a stable workflow used by other members; document migration steps in the project change record when needed.

## Pre-Cleanup Checks

Before deleting an old directory, branch, or experiment material, complete all of these checks:

1. Run `git status --short` in the target worktree and confirm that no project files are uncommitted.
2. Inspect local and remote branch relationships. Confirm that unique commits have been pushed and are covered by an active branch or `main`.
3. Check manifests, checksums, and backup status for `data/` and any historical ignored directories; retire legacy locations after migration.
4. Ask the project lead to confirm that no other member, task, or reproduction experiment still uses the directory, branch, or material.
5. Record the cleanup target, approver, and date. If any item cannot be confirmed, pause cleanup and retain the original material.

## Verification Checklist

For every handoff, migration, or milestone closeout, confirm that:

- Members can locate the project's single organization repository and shared `main`.
- Every member can locate their personal worktree, personal branch, and remote branch.
- `git remote -v` points to the organization repository, with no personal repository or long-lived second clone.
- Code, configurations, scripts, and notes are inside the personal worktree and have been committed and pushed by stage.
- Large local artifacts are inside the worktree's `data/` directory and do not appear as accidentally tracked files.
- Important data has a manifest, checksum, source description, and verifiable backup.
- Functionality intended for `main` has been verified, while unfinished experiments remain on personal branches.

## Troubleshooting

- **An accidental personal clone exists:** Stop developing in the second clone. Compare its remote, unpushed commits, and untracked local data, then migrate to the assigned worktree. After coverage is confirmed, do not maintain the second clone long term.
- **Files are outside the worktree:** Pause cleanup and migration. First gather project files, configurations, and notes into the personal worktree, and add a manifest or backup for large data. Do not treat a temporary directory as project storage.
- **The personal branch is far behind `main`:** Fetch the latest `main`, integrate it using the project's agreed merge or rebase method, resolve conflicts item by item, and rerun affected checks. Do not overwrite another member's commits.
- **A large file was tracked by mistake:** Keep a recoverable local copy first, add `.gitignore` and a manifest, then remove it from the Git index or history using a maintainer-approved method. Do not delete the only copy before the backup is confirmed.
- **An unpushed commit is found during cleanup:** Stop deletion immediately. Inspect the commit and its sensitive-information status, push it to the personal remote branch, confirm it is visible remotely, and repeat the coverage check.
- **The owner, commit coverage, or data backup cannot be confirmed:** Pause the operation and contact the project lead or repository maintainer through the controlled directory. Do not delete, force-overwrite, or publish data before confirmation.

## Maintenance

- Maintainers: non-hardware team project leads and repository maintainers
- Contact entry: `<CONTROLLED_CONTACT_DIRECTORY_URL>`
- Last verified: 2026-08-15
