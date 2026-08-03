# Research Data Storage and Archiving

!!! info "Confirm storage status live"
    The activation date, address, capacity, and mount instructions for centralized storage or NAS must be confirmed through controlled channels. This page does not claim that any particular endpoint is currently available.

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
- Never write real internal paths, access tokens, mount passwords, or private share links in the Wiki.
- Apply least privilege to restricted data and revoke access when a member leaves or a project ends.

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
- Permission denied: ask the Data Storage Administrator to correct project access; never share another person's account.
- Insufficient space: stop bulk transfer and submit capacity and growth estimates before expansion or archiving.
- File mismatch: retain the source copy, retransmit failed files, and recheck checksums.
- Sensitive data shared accidentally: revoke access immediately, record the affected scope, and notify the project owner.

## Maintenance

- Owner: Data Storage Administrator
- Contact: `<CONTROLLED_CONTACT_DIRECTORY_URL>`
- Last verified: 2026-08-03
