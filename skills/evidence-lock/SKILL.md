---
name: evidence-lock
description: >-
  证据锁定 Skill。当需要把论文将使用的每个数字绑定到可核验来源
  （results.yml R-id + evidence 文件 + 哈希）、清除数字漂移、或校验
  "正文数字是否全部可追溯"时使用。用户说"锁定数字""核对数值来源"
  "这个数字哪来的""检查数字漂移"时触发。G2 批准前，任何正文起草禁止开始。
---

# Evidence Lock — 证据锁定

## 职责

保证**论文里出现的每个数字都能追溯到一份可核验的文件**，且全文只有一个
数值口径。这是"数字漂移"的唯一拦截层。

## 执行步骤

1. 读 `.paper/workflow.yml`：G1 未批准时可核对来源、准备候选修正和审批材料；正式锁定须 G1 批准。G2 已批准后发生输入变化，应列影响范围并请求重新确认，不静默沿用。
2. 盘点 `.paper/results.yml`：
   - 每条 `verified: pending` / `partial` → 打开 `source_file` 精确读取，
     回填精确值（保持源精度，不做正文格式化），改 `verified: true`；
     无法核验 → 标记 `verified: false` 并列入"不得进入正文"清单。
3. **双向核对**：
   - claims.yml 引用的每个 R-id 在 results.yml 存在且 verified。
   - figures.yml / tables.yml 引用的 R-id 同上。
   - 复现入口与外部验收目录存在（evidence/README.md 的路径逐条检查）。
4. **红线审计**：扫描历史稿件数值；凡与登记册冲突，列对照表，
   以登记册为准；确认无历史稿数值流入登记册。
5. **精度与呈现分离**：results.yml 保留源精度；正文呈现格式只按
   terminology.yml number_format 转换，且不得改变含义。
6. 更新 `changelog.yml`；呈报作者批准 **G2**。

## 输出

- 更新后的 results.yml（全部 verified: true / false）
- "不得进入正文"数字清单（verified: false 者）
- 冲突对照表（历史稿 vs 登记册）
- G2 批准请求

## 判定规则

- 数字在 evidence/ 或外部验收目录中**找不到** → 不得进入正文，无例外。
- 文稿与 CSV 不同 → 先核对验收版本、模型、样本和单位；格式不决定权威。未解决的冲突保留并报告，不自动覆盖。
- "差不多""约" → 不是数值；必须给出源精度或标 pending。

## 禁止

- 不创作、不估算、不"合理推测"任何数字。
- 不批准自己的 G2。
- 不在数字未锁定时开始起草（drafting 被 G2 阻塞）。
