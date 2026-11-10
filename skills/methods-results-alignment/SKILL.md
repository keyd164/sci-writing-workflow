---
name: methods-results-alignment
description: >-
  方法—结果双向对齐技能。Methods 与 Results 需要互相校验时使用：
  Results 出现的每个模型必须在 Methods 有定义，Methods 定义的每个分析
  必须在 Results 有结果或明确角色；同时核对样本数、簇数、自由度、
  必现句子与单位口径。用户说"检查方法结果一致吗""双向对齐""跑一遍对齐"
  时触发。输出对齐报告，经作者批准（G3）后才允许进入语言层。
---

# 方法—结果双向对齐

## 职责

回答两个方向的问题，输出一张对照表：

```
Methods 侧（methods.yml M-id）          Results 侧（results.yml R-id）
M-PRIMARY   ←————————对应——————————▶  R01
M-SENS      ←——————————————————▶  R02
...
```

- **正向**：Results 中出现的每个模型/分析，Methods 有没有定义（含样本、推断、控制集）？
- **反向**：Methods 中定义的每个重要分析，Results 有没有结果？没有 → 必须标注角色（supplement / diagnostic / not_reported），不得静默缺失。

## 执行步骤

1. 前置：drafting 至少完成一轮；G3 未批准。
2. 抽取 `manuscript/methods.md` 与 `manuscript/results.md` 中所有模型/分析提及，映射到 M-id；抽取所有数字，映射到 R-id。
3. 生成对照表并逐行判定：
   - `aligned`：两侧都有，样本/推断一致
   - `methods_only`：Methods 有、Results 无 → 补结果或标角色
   - `results_only`：Results 有、Methods 无 → 补方法定义（**高危**）
   - `mismatch`：样本数、簇数、自由度或 CI 约定不一致
4. 专项核对：
   - 各模型样本数在 Methods、Results、`results.yml` 三处一致
   - 推断约定一致（聚类层级、自由度算法、稳健标准误类型）
   - `mandatory_sentences` 全部就位
   - 单位与口径一致（率的分母、暴露的时间积分、量纲换算）
   - 主结果与敏感性成对出现
5. 输出报告：对照表 + 问题清单（按 release blocker / 应修 / 建议修 分级）。
6. 问题修复后呈报作者批准 **G3**。

## 判定规则

- `results_only` 一律 release blocker：读者无法核验的模型定义是审稿重灾区。
- `methods_only` 若不是补充材料/诊断用途且无合理解释 → release blocker。
- 样本数在任一处与 `results.yml` 不一致 → release blocker。

## 全篇双向论证校验

检查 `manuscript/argument-map.md` 与 `extended-outline.md`：自上逐个研究问题追踪到方法、结果和结论；自下逐个结果追踪到解释、贡献与摘要。方法—结果匹配不是全篇论证通过的充分条件。

## 禁止

- 不修改数字（那是 `evidence-lock` 的权限）。
- 不批准自己的 G3。
- 不用“读者应该能理解”为缺失定义开脱。