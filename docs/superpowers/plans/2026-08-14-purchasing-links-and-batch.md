# 采购表格入口与周批次流程实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将两个已确认的 Notion 表格入口和严格的周批次采购规则同步到中英文 Lab Wiki 页面。

**Architecture:** 保留现有行政流程信息架构，在采购流程页提供“采购需求表”和“已下单表”两个入口，并在资源总览中提供快捷入口。采购页面以每组每周一份 Excel 和一个总购物车分享链接为唯一申请单位，描述周末汇总、下一周采购、对应周 Notion 更新、申请组到货责任、货比三家、SG199 包邮和退回机制；同步更新 AI 索引的核验日期。

**Tech Stack:** Markdown, Material for MkDocs, `mkdocs-static-i18n`, Git

---

### Task 1: 更新中文采购流程页

**File:** `docs/administration/purchasing.md`

- [ ] 在每周节奏提示后加入两个用户确认的 Notion 完整链接，并说明第一张表接收每组每周一份 Excel，第二张表记录下单和到货照片。
- [ ] 将提交流程改为每组每周唯一一份 Excel；每项包含物品名称、数量、型号、金额、用途、商品链接和申请组别；表级填写采购周和总购物车分享链接。
- [ ] 明确周六或周日统一提交给采购协调人，个人文字、聊天或其他零散需求不受理。
- [ ] 明确本周汇总、下一周独立采购、不同周不混合；下单后更新对应周的已下单表；到货后申请组拆包、逐项拍照、更新 Notion 并负责本组物品。
- [ ] 加入货比三家、用途/兼容性/配件完整性/可行性、`SG199` 包邮和例外说明规则；不合规申请退回完善。
- [ ] 更新维护日期为 `2026-08-15`，运行 `rg` 关键词检查和 `git diff --check`。

### Task 2: 同步英文采购流程页

**File:** `docs/administration/purchasing.en.md`

- [ ] 用 `Purchase Requirements Table` 和 `Ordered Items Table` 标注两个相同 Notion 链接。
- [ ] 镜像 Excel 唯一提交单位、字段、`Total shared cart link`、周末提交给 `Purchasing Coordinator` 和拒绝零散需求规则。
- [ ] 镜像周批次隔离、下单后更新对应周、owning group 到货拍照与责任、供应商比较、可行性、配件完整性和 `SG199` free shipping 规则。
- [ ] 更新维护日期并运行英文关键词检查。

### Task 3: 更新资源总览入口

**Files:** `docs/resources/index.md`, `docs/resources/index.en.md`

- [ ] 将采购资源占位符替换为两个相同的 Notion 实际入口和用途说明。
- [ ] 在双语访问权限提示中说明两个表由 Notion 控制访问，更新维护日期为 `2026-08-15`。
- [ ] 检查中英文资源页各有两个入口且不再包含采购占位符。

### Task 4: 同步索引并验证

**File:** `docs/assets/data/ai-index.json`

- [ ] 将 `administration/purchasing:zh`, `administration/purchasing:en`, `resources/index:zh` 和 `resources/index:en` 的 `last_verified` 同步为 `2026-08-15`。
- [ ] 运行 `./.venv/bin/python -m unittest discover -s tests -v`，确保索引覆盖测试通过。
- [ ] 运行 `./.venv/bin/mkdocs build --strict`，确保双语构建无警告。
- [ ] 审阅最终 diff，仅暂存本计划列出的文件，并提交：

```bash
git add docs/administration/purchasing.md docs/administration/purchasing.en.md \
  docs/resources/index.md docs/resources/index.en.md \
  docs/assets/data/ai-index.json \
  docs/superpowers/plans/2026-08-14-purchasing-links-and-batch.md
git commit -m "docs: add purchasing table links and batch rules"
```
