# Standardized Purchasing Process Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the bilingual purchasing placeholders with an actionable weekly process for group selection, submission, consolidated purchasing, package collection, photography, and inventory registration.

**Architecture:** Keep the existing administration information architecture and expand the current Chinese and English purchasing pages in place. Each page will define the same roles, weekly workflow, reusable list template, research and approval controls, delivery workflow, verification checks, exception handling, privacy boundary, maintainer role, and verification date; the administration landing pages will describe these links as active processes rather than examples.

**Tech Stack:** Markdown, Material for MkDocs, `mkdocs-static-i18n`, Git, GitHub CLI

---

### Task 1: Write the Chinese Purchasing Process

**Files:**
- Modify: `docs/administration/purchasing.md`
- Modify: `docs/administration/index.md`

- [ ] **Step 1: Replace the Chinese purchasing placeholder**

Write `docs/administration/purchasing.md` with these sections and requirements:

````markdown
# 采购流程

本流程用于统一各组的物品选型、采购提交、周末汇总、下周采购以及到货入库，减少重复采购、型号不兼容和采购后闲置。

!!! info "每周采购节奏"
    每组每周只提交一份采购清单。采购协调人在周六、周日统一汇总，通过检查的项目安排在下一周采购。

## 角色分工

| 角色 | 职责 |
|---|---|
| 各组成员 | 共同确认需求、讨论选型并完成可行性调研 |
| 各组采购提交人 | 整理本组当周唯一一份采购清单和共享购物车链接 |
| 采购协调人 | 周末汇总各组提交，检查完整性、重复采购、调研和审批状态 |
| 采购执行人 | 按确认后的清单下单，并将到货包裹放到指定公共区域 |
| 物品所属组 | 认领包裹，逐项核对、拍照并在受控资产登记系统中入库 |

## 提交前准备

- 同组成员已共同确认需求和选型，不由单人直接决定。
- 每项物品都有明确的采购目的、预计使用人和预计使用时间。
- 已核对现有库存，确认没有可复用或可共享的同类物品。
- 已完成型号、规格、数量和兼容性调研。
- 金额较高的物品已按实验室现行审批要求取得事前确认。
- 已确定用于提交清单和购物车链接的实验室受控渠道。

## 提交流程

1. 组内共同讨论需求，比较候选产品并确定型号、规格和数量。
2. 由本组采购提交人整理当周采购清单，每项均填写完整信息。
3. 将拟采购物品加入淘宝或其他供应商网站的购物车，核对型号和数量后生成共享购物车链接。
4. 通过实验室指定的受控渠道一次性提交本组清单和共享购物车链接。不要把真实记录提交到本公开 Wiki 或公开 Issue。
5. 采购协调人在周六、周日统一汇总。字段缺失、重复采购、审批未完成或可行性不足的项目退回所属组补充。
6. 采购执行人在下一周按已确认的型号、数量和商品链接下单。缺货、涨价或规格发生变化时，先由所属组重新确认，不自行替换。

## 采购清单模板

在实验室指定的受控文档中复制以下模板。每组每周只建立一份：

```text
所属组：
提交周：
采购提交人：
共享购物车链接：
```

| 物品名称 | 数量 | 型号或规格 | 商品链接 | 预计单价/小计 | 采购目的 | 调研结论 | 审批状态 |
|---|---:|---|---|---:|---|---|---|
|  |  |  |  |  |  |  |  |

“调研结论”至少说明兼容性、是否有可复用库存以及选用该型号的理由；“审批状态”填写“不需要”或已通过的审批状态，不在 Wiki 中附审批文件。

## 可行性调研要求

每项采购在提交前至少确认：

- **实际用途：** 对应的项目、实验或维护任务明确，预计使用人和时间明确。
- **兼容性：** 与现有设备、软件、接口、尺寸、电源、材料或实验方案匹配。
- **选型依据：** 已比较合理的替代型号，并说明当前型号在功能、交付、价格或维护方面的选择理由。
- **数量依据：** 数量与实际工作量、损耗和现有库存相符。
- **供应风险：** 商品链接、交付时间、售后条件和关键附件已经核对。

金额较高的物品还必须更充分地比较备选方案、验证关键兼容性并写明使用计划，在提交前按实验室现行审批要求取得确认。Wiki 不另行规定金额阈值；以当前有效的实验室审批规则为准。

## 到货、认领与入库

1. 采购执行人将到货包裹放到实验室指定公共区域，并保留可供所属组识别的组别或订单信息。
2. 物品所属组自行认领包裹，逐项核对物品名称、型号、数量和外观状态。
3. 所属组为清单中的每项物品拍照，并在受控资产登记系统中填写对应记录。
4. 确认照片和登记记录与实物一致后，完成入库并将物品移至指定存放位置。

采购照片、订单信息和资产登记记录仅保存在批准的受控系统中，不上传到公开 Wiki。

## 核验清单

- [ ] 本组本周只提交了一份采购清单。
- [ ] 每项物品的名称、数量、型号或规格、链接、价格、用途、调研结论和审批状态完整。
- [ ] 购物车中的型号和数量与清单一致，共享链接可由采购协调人访问。
- [ ] 金额较高的物品已完成加强调研和所需的事前审批。
- [ ] 到货物品与订单一致，并已逐项拍照和登记入库。

## 异常处理

- **错过周末汇总或材料不完整：** 补齐后进入下一次每周采购周期；紧急需求由采购协调人按现行规则处理。
- **共享链接无法访问：** 由所属组重新生成链接并核对商品、型号和数量。
- **商品缺货、涨价或规格变化：** 暂停该项采购，退回所属组重新确认，不直接购买替代品。
- **重复采购或已有可用库存：** 暂停该项，确认共享或复用方案后再决定是否采购。
- **到货错发、漏发或破损：** 暂停入库，保留包装和物品照片，通过采购执行人联系供应商处理。
- **包裹无法认领或资产无法登记：** 保持物品原状，联系采购协调人核对所属组和记录。

## 信息安全

真实购物车分享链接、订单、报价、付款信息、个人地址、审批文件和采购照片只通过实验室批准的受控渠道保存和传递，不提交到公开 Wiki、公开 Issue 或公开聊天记录。

## 维护信息

- **维护者：** 采购流程维护者
- **最后核验：** 2026-08-11
````

- [ ] **Step 2: Make the Chinese administration index describe active procedures**

In `docs/administration/index.md`, replace `## 当前示例` with `## 当前流程`. Keep the two existing links and the sentence describing required procedure sections unchanged.

- [ ] **Step 3: Verify required Chinese content**

Run:

```bash
rg -n '^# |^## |每组每周只提交一份|周六、周日|下一周采购|共享购物车链接|可行性调研|逐项拍照|受控资产登记|维护者|最后核验' docs/administration/purchasing.md docs/administration/index.md
```

Expected: the purchasing page contains the complete weekly workflow and the index reports `## 当前流程`; every search phrase appears at least once in the relevant file.

- [ ] **Step 4: Check the Chinese diff and commit**

Run:

```bash
git diff --check
git diff -- docs/administration/purchasing.md docs/administration/index.md
git add docs/administration/purchasing.md docs/administration/index.md
git commit -m "docs: standardize Chinese purchasing process"
```

Expected: no whitespace errors; the commit contains only the two Chinese administration pages.

### Task 2: Mirror the Process in English

**Files:**
- Modify: `docs/administration/purchasing.en.md`
- Modify: `docs/administration/index.en.md`

- [ ] **Step 1: Replace the English purchasing placeholder**

Write `docs/administration/purchasing.en.md` as a faithful translation of the Chinese page. It must contain these matching sections:

````markdown
# Purchasing Process

This process standardizes item selection, purchase submission, weekend consolidation, purchasing in the following week, and inventory registration across all groups. It is intended to reduce duplicate purchases, incompatible models, and items that remain unused after purchase.

!!! info "Weekly purchasing schedule"
    Each group submits only one purchase list per week. The Purchasing Coordinator consolidates submissions on Saturday and Sunday, and approved items are scheduled for purchase in the following week.

## Roles and Responsibilities

| Role | Responsibility |
|---|---|
| Group members | Confirm the need together, discuss product selection, and complete feasibility research |
| Group Purchasing Submitter | Prepare the group's single weekly purchase list and shared shopping-cart link |
| Purchasing Coordinator | Consolidate group submissions over the weekend and check completeness, duplicates, research, and approval status |
| Purchasing Executor | Place orders from the confirmed lists and put delivered packages in the designated common area |
| Owning group | Collect its packages, verify each item, take photographs, and register the items in the controlled asset register |

## Prerequisites

- Group members have jointly confirmed the need and selection; the selection was not made by one person alone.
- Every item has a clear purchasing purpose, expected users, and expected usage period.
- Existing inventory has been checked and no suitable item can be reused or shared.
- The model, specification, quantity, and compatibility research is complete.
- Higher-value items have received prior confirmation under the lab's current approval requirements.
- The lab-controlled channel for submitting the list and shopping-cart link has been identified.

## Submission Procedure

1. Discuss the need within the group, compare candidate products, and agree on the model, specification, and quantity.
2. The Group Purchasing Submitter prepares the week's purchase list and completes every field for every item.
3. Add the proposed items to a Taobao or other supplier cart. Verify the models and quantities, then generate a shared shopping-cart link.
4. Submit the group's list and shared shopping-cart link together through the lab's designated controlled channel. Do not post real records to this public Wiki or a public issue.
5. The Purchasing Coordinator consolidates submissions on Saturday and Sunday. Items with missing fields, duplicate requests, incomplete approvals, or insufficient feasibility research are returned to the owning group.
6. The Purchasing Executor orders confirmed models and quantities from the confirmed product links in the following week. If an item is unavailable or its price or specification changes, return it to the owning group for confirmation instead of substituting it directly.

## Purchase List Template

Copy this template into the lab's designated controlled document. Create only one list per group per week:

```text
Group:
Submission week:
Purchasing submitter:
Shared shopping-cart link:
```

| Item name | Quantity | Model or specification | Product link | Estimated unit price/subtotal | Purchasing purpose | Research conclusion | Approval status |
|---|---:|---|---|---:|---|---|---|
|  |  |  |  |  |  |  |  |

The research conclusion must at least cover compatibility, whether existing inventory can be reused, and why this model was selected. For approval status, enter “Not required” or the current approved status; do not attach approval records to the Wiki.

## Feasibility Research Requirements

Confirm at least the following before submitting each item:

- **Practical use:** The related project, experiment, or maintenance task and the expected users and usage period are clear.
- **Compatibility:** The item matches existing equipment, software, interfaces, dimensions, power, materials, or the experimental plan.
- **Selection rationale:** Reasonable alternatives have been compared, with a rationale based on function, delivery, price, or maintenance.
- **Quantity rationale:** The quantity matches the actual workload, expected loss, and current inventory.
- **Supplier risk:** The product link, lead time, after-sales terms, and critical accessories have been checked.

Higher-value items also require a more thorough comparison of alternatives, verification of critical compatibility, a written usage plan, and prior confirmation under the lab's current approval requirements. The Wiki does not set a separate monetary threshold; follow the currently effective lab approval rules.

## Delivery, Collection, and Inventory Registration

1. The Purchasing Executor puts delivered packages in the lab's designated common area and retains enough group or order information for the owning group to identify them.
2. The owning group collects its packages and checks each item's name, model, quantity, and physical condition.
3. The owning group photographs every item on the list and creates the matching entry in the controlled asset register.
4. After confirming that the photographs and registration match the physical items, complete inventory registration and move the items to their designated storage location.

Purchase photographs, order details, and asset records must remain in approved controlled systems and must not be uploaded to the public Wiki.

## Verification Checklist

- [ ] The group submitted only one purchase list this week.
- [ ] Every item includes a name, quantity, model or specification, link, price, purpose, research conclusion, and approval status.
- [ ] Models and quantities in the cart match the list, and the Purchasing Coordinator can open the shared link.
- [ ] Higher-value items have completed enhanced research and required prior approval.
- [ ] Delivered items match the order and have been photographed and registered individually.

## Troubleshooting

- **Missed weekend consolidation or incomplete material:** Complete the submission for the next weekly purchasing cycle. The Purchasing Coordinator handles urgent needs under the current rules.
- **Shared link cannot be opened:** The owning group generates a new link and verifies the products, models, and quantities.
- **Item unavailable, price increase, or specification change:** Pause the item and return it to the owning group for confirmation; do not buy a substitute directly.
- **Duplicate request or usable inventory found:** Pause the item and confirm whether it can be shared or reused before purchasing.
- **Wrong, missing, or damaged delivery:** Pause inventory registration, retain photographs of the packaging and item, and ask the Purchasing Executor to contact the supplier.
- **Package cannot be identified or asset cannot be registered:** Leave the item unchanged and ask the Purchasing Coordinator to verify the owning group and record.

## Information Security

Real shopping-cart links, orders, quotations, payment information, personal addresses, approval records, and purchase photographs must be stored and shared only through lab-approved controlled channels. Do not post them to the public Wiki, public issues, or public chat records.

## Maintenance

- **Maintainer:** Purchasing Process Maintainer
- **Last verified:** 2026-08-11
````

- [ ] **Step 2: Make the English administration index describe active procedures**

In `docs/administration/index.en.md`, replace `## Current examples` with `## Current procedures`. Keep the two existing links and the sentence describing required procedure sections unchanged.

- [ ] **Step 3: Verify Chinese-English structural parity**

Run:

```bash
rg -n '^## ' docs/administration/purchasing.md docs/administration/purchasing.en.md
rg -n 'Saturday and Sunday|following week|shared shopping-cart link|Feasibility Research|photographs every item|controlled asset register|Maintainer|Last verified' docs/administration/purchasing.en.md
```

Expected: both pages have ten matching second-level sections in the same order, and every required English workflow phrase appears.

- [ ] **Step 4: Check the English diff and commit**

Run:

```bash
git diff --check
git diff -- docs/administration/purchasing.en.md docs/administration/index.en.md
git add docs/administration/purchasing.en.md docs/administration/index.en.md
git commit -m "docs: mirror purchasing process in English"
```

Expected: no whitespace errors; the commit contains only the two English administration pages.

### Task 3: Validate and Publish the Documentation Change

**Files:**
- Verify: `docs/administration/purchasing.md`
- Verify: `docs/administration/purchasing.en.md`
- Verify: `docs/administration/index.md`
- Verify: `docs/administration/index.en.md`
- Verify: `docs/superpowers/specs/2026-08-11-purchasing-process-design.md`
- Verify: `docs/superpowers/plans/2026-08-11-purchasing-process.md`

- [ ] **Step 1: Scan for incomplete or sensitive content**

Run:

```bash
rg -n 'T[B]D|T[O]DO|待[定]|待补[充]|taobao\.com|item\.taobao|https?://[^ )]+' docs/administration/purchasing.md docs/administration/purchasing.en.md
```

Expected: no output. The pages explain where links belong without publishing a real product, cart, order, or internal-system URL.

- [ ] **Step 2: Build both language variants strictly**

Run:

```bash
../.venv/bin/mkdocs build --strict
```

Expected: exit status 0 and output ending with `Documentation built` without warnings or errors. The ignored `site/` output must not be committed.

- [ ] **Step 3: Review the complete branch diff and commit history**

Run:

```bash
git diff --check main...HEAD
git diff --stat main...HEAD
git status --short --branch
git log --oneline main..HEAD
```

Expected: the branch contains the design, implementation plan, and four intended administration-page changes; the working tree is clean and no `.venv/` or `site/` file is tracked.

- [ ] **Step 4: Push the feature branch and create the pull request**

Run:

```bash
git push -u origin docs/standardize-purchasing-process
gh pr create --base main --head docs/standardize-purchasing-process --title "docs: standardize weekly purchasing process" --body-file /tmp/lab-wiki-purchasing-pr.md
```

The PR body file must summarize the bilingual process, list the strict MkDocs build under testing, state that no operational endpoint or sensitive procurement record is published, and identify the design and plan commits. Expected: GitHub returns the new pull request URL.
