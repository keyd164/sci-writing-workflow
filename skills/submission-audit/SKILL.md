---
name: submission-audit
description: >-
  投稿前审计技能。论文准备投稿、需要机器式全项检查时使用：稿件结构、
  编号系统、引用完整性、DOI、声明项（伦理/数据/代码/资助/贡献/利益冲突）、
  期刊字数限制、因果语言终扫、报告规范映射。用户说"投稿前检查一遍"
  "submission audit""核对投稿材料"时触发。输出 pass/fail 报告；
  任何 release blocker 未清空不得进入 G6 提交授权。
---

# 投稿前审计

## 职责

投稿前最后一道机器式检查。输出 pass / fail 清单，fail 项分三级：release blocker（必须清空）/ warning（应清空）/ note（记录）。

## 审计清单

### 1. 稿件完整性
- [ ] title（与 `paper.yml` 候选一致；无未核实模块写入）
- [ ] abstract（结构符合 `journal.yml` 的 abstract_structure；无预写结论）
- [ ] keywords
- [ ] manuscript 各节齐全（Methods/Results/Discussion/Conclusion）
- [ ] 字数在 `journal.yml` 已核实的 word_limit 内（unverified → blocker）

### 2. 编号系统
- [ ] 图编号连续；每图有图注；图内数值绑定 R-id
- [ ] 表编号连续；每表有题注；表内数值绑定 R-id
- [ ] 补充材料编号连续，与正文引用一一对应
- [ ] 正文引用编号连续无缺；`references.yml` 无 missing 被引用项

### 3. 引用与来源
- [ ] 每条引用状态已在 `citation-verifier` 中核验；DOI/URL 可解析
- [ ] 数据来源写明版本与检索日期
- [ ] 报告规范（如 STROBE、GATHER、PRISMA，按研究设计选择）位置映射表存在

### 4. 声明项
- [ ] ethics（含豁免依据）
- [ ] data availability
- [ ] code availability（复现入口、哈希、软件版本）
- [ ] funding
- [ ] author contributions
- [ ] competing interests
- [ ] 临床试验、预注册等不适用项的 N/A 声明

### 5. 科学边界终扫（最高优先）
- [ ] 全稿对 `claims.yml` 的 `global_language_lock.forbidden` 零命中
- [ ] `mandatory_sentences` 全部就位
- [ ] 无跨层换算错误（把率当人数、把条件差当可避免病例等）
- [ ] 跨零区间保留；主结果与敏感性成对出现
- [ ] 无未登记主张（每个结论可追溯到 C-id）
- [ ] 术语符合 `terminology.yml`

### 6. 复现性
- [ ] 运行入口、哈希、软件版本在正文或补充材料中可找到
- [ ] 主数值与证据目录抽样一致

## 执行

先取 `figure-planner` 的图文核对结果、`citation-verifier` 的三层状态；有返修时并入 `rebuttal-response` 的子问题与实际改稿对应表。报告必须针对拟提交的具体文件版本；旧报告不能覆盖新版新增的引用或结果。

1. 逐项检查，记录证据（文件 + 位置）。
2. 汇总：`X blockers / Y warnings / Z notes`。
3. blockers > 0 → 列出清空路径（哪个模块、哪个动作），**不得标记 G5 通过**。
4. blockers = 0 → 呈报作者，等待 **G5/G6** 批准。

## 禁止

- 自行清零 blocker。
- 以“审稿人不会发现”为由放行。
- 修改稿件内容（只报告；修复交回 `evidence-drafting` 等对应模块）。