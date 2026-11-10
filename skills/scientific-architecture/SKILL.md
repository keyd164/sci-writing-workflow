---
name: scientific-architecture
description: >-
  科学架构技能。需要回答"这篇论文到底在讲什么"、建立或校验
  Research Question → Knowledge Gap → Contribution → Claim → Evidence 映射，
  或重构故事线与提纲时使用。用户说"梳理逻辑""搭提纲""检查故事线"
  "结构有问题"时触发。产出架构图与主张映射，须经作者批准（G1）后才能锁定。
---

# 科学架构

## 职责

把论文组织成一条相互衔接的问题层级，而不是分析的堆砌。产出：Question → Claim → Evidence 映射表、故事线校验、`claims.yml` 草案。

## 执行步骤

读取[段落证据计划](references/paragraph-plan.md)，产出论证图与扩展提纲；二者是后续起草与审查的输入。

1. 读 `.paper/paper.yml`、`.paper/workflow.yml`，确认当前允许进入本阶段（bootstrap 已完成、G1 未批准）。
2. 读项目权威文档（研究框架、立项说明、决策日志）与 `.paper/claims.yml`。
3. 构建或校验映射：

```
Research Question
      ↓
Knowledge Gap
      ↓
Contribution
      ↓
Claim 1 ← Evidence 1 (R-id)
      ↓
Claim 2 ← Evidence 2 (R-id)
      ↓ ...
```

   每个 Claim 必须能回答：属于哪个 Q、强度（association / descriptive / counterfactual / scenario / interpretation）、支撑 Evidence、图/表落点。
4. 故事线校验：
   - 相邻环节之间有没有逻辑连接，还是几个独立分析拼盘？
   - 每个“更外向”的结论（归因、情景、政策含义）是否明确依赖“更内向”的假设？
   - 标题与摘要有没有预写尚无数据支持的结论？
   - 并列的多个不平等/异质性维度是否被合并成一句结论？
5. 更新 `.paper/claims.yml`（新结论登记、强度与语言锁定修订），并在 `changelog.yml` 记录。
6. 输出架构报告，呈报作者批准 **G1**。G1 批准前可以核验来源、准备证据冲突报告，但不正式锁定、不进入下游写作。

## 检查清单（输出需逐项回答）

- [ ] 每个 Q 有对应 C-id；每个 C-id 有 R-id 或明确标 planned
- [ ] 无“结论先行”（没有证据的 claim）
- [ ] 关联/描述/反事实/情景/解释五类强度未混用
- [ ] 并列的分析维度未被合并叙述
- [ ] 标题候选与故事线一致，无未核实模块写入标题

## 禁止

- 不写正文段落（那是 `evidence-drafting` 的职责）。
- 不批准自己的 G1。
- 不为了“故事好看”建议增加无证据的结论。