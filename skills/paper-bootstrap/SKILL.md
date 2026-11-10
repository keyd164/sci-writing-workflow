---
name: paper-bootstrap
description: >-
  论文项目引导 Skill。当开始一个论文写作项目、.paper/ 约束体系尚未建立，
  或需要扫描既有论文项目（代码库、稿件、结果文件）并建立/校验 source of
  truth 时使用。用户说"初始化论文项目""扫描这个论文目录""建立 paper 体系"
  "看看这个项目里有什么"时触发。本 skill 只扫描、建档、标记冲突，不写正文。
---

# Paper Bootstrap — 项目引导

## 职责

第一次面对论文项目时：**扫描文件 → 识别真实状态 → 建立/校验 `.paper/` →
标记冲突**。绝不写任何正文。

## 输入

项目根目录（含或应含 `.paper/`）。若用户只给了分析代码库路径，在**同级目录**建立独立的写作项目目录（例如 `my-paper/`），不污染代码库。

## 执行步骤

1. **定位与清点**：列出项目树（代码、数据、结果输出、稿件、图表、文档），
   区分：分析代码库 / 结果交付包 / 历史稿件 / 图表资产。
2. **读取权威文档**（若存在）：README、docs/ 下的模型字典、决策日志、
   结果报告、框架文档。这些是 `.paper/` 内容的事实来源。
3. **建立或校验 `.paper/`**：
   - 不存在 → 按 OS 模板创建全部 12 个文件（paper/claims/results/methods/
     decisions/terminology/references/figures/tables/journal/workflow/changelog），
     数值只从可核验来源填入，无来源的标 `verified: pending`。
   - 已存在 → 校验一致性与完整性，列出漂移。
4. **数字来源审计**：扫描历史稿件（初稿等）中的数值，**只记录冲突，
   不把任何历史稿数值写入 results.yml**。发现历史稿与登记册
   冲突 → 以登记册为准并写入 changelog.yml。
5. **冲突报告**：输出扫描报告——缺失项、冲突项、待作者裁决项。
6. **更新 workflow.yml**：bootstrap 阶段标记 completed（日期），
   记录 notes.bootstrap_findings；不得批准任何 Gate。

## 输出

- `.paper/` 体系（新建或校验报告）
- 冲突与缺失清单（按 必须补 / 推荐补 / 加分补 分级）
- `changelog.yml` 追加一行

## 禁止

- 不写 manuscript/ 任何内容。
- 不用历史稿件数值填充登记册。
- 不批准 G1–G6 任何 Gate。
- 不删除、移动、重命名任何既有文件。
