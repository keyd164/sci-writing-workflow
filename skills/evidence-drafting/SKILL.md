---
name: evidence-drafting
description: >-
  证据驱动写作技能。G1/G2 已批准、需要起草或修订正文
  （Methods / Results / Discussion / Conclusion / Abstract）时使用。
  用户说"写 Methods""改 Results""起草讨论""按审稿意见修订"时触发。
  严格按 Evidence → Claim → Paragraph → Section 顺序写作，
  Results 只做 finding → magnitude → uncertainty → comparison。
---

# 证据驱动写作

## 职责

把已锁定的证据与主张写成正文。方向永远是 **Evidence → Claim → Paragraph → Section**，而不是“写一段漂亮英文”。

## 前置检查（每次必做）

1. `.paper/workflow.yml`：G1、G2 已批准；当前阶段允许 drafting。G2 未批准 → 停止并报告阻塞。
2. 读 `.paper/claims.yml`（写什么）、`.paper/results.yml`（数字）、`.paper/methods.yml`（模型定义与必现句子）、`.paper/terminology.yml`（术语）。

## 分节规则

起草前读取 `manuscript/argument-map.md` 与 `extended-outline.md`；缺失则先由 `scientific-architecture` 准备，不因为“当前阶段已通过”就推定计划存在。每段履行已计划的功能、证据和推断边界。

Results 结构修订模式：先反向列出原段落的功能、C-id/R-id 与比较关系，再按“问题—发现—量级—不确定性”重排；保留负结果、敏感性分析和全部必要数值，不按 panel 数量机械拆段。

修订后列出受影响的摘要、结论、图注、补充材料、元数据和回复信；同步已授权改动，并重新核验受影响项。

### Methods
- 每个模型或分析在 `methods.yml` 有 M-id；样本按模型分别报告。
- `mandatory_sentences` 逐字出现。
- 不声称未做的分析（如未做的稳健性检验、未采用的估计方法）。

### Results（纪律最严）
每段只做四件事：**finding → magnitude → uncertainty → comparison**。
- 数字必须带 R-id 来源；跨零区间原样报告。
- 主结果与敏感性成对报告，不隐藏不稳定性。
- 不写 Discussion 语言（“This finding highlights the urgent need for…”）。
- 并列的分析维度分块叙述，不合并成一句总结。

### Discussion
- 主要发现 → 既往研究 → 竞争解释 → 有条件扩展 → 政策含义 → 局限。
- 同一个系数或机制的衍生解释，不得重复当作第二条独立证据。
- 政策段落不推算个体风险或可避免病例数。
- `mandatory_sentences` 逐字出现。

### Conclusion / Abstract
- 结论两三句；分组或异质性结论须有对应结果支持。
- 摘要最后起草（Discussion 之后）。
- `mandatory_sentences` 逐字出现。

### Revision（G4 后）
- 只执行作者标记 accept 的意见；reject/defer 的不动。
- 修订不得违反 `claims.yml` / `decisions.yml`；意见与约束冲突时停止并呈报，不擅自改约束。

## 语言边界

本模块负责**科学正确性**；语言层由 `scientific-prose` 等负责。起草时即遵守 `global_language_lock`，但不做风格化改写。

## 输出

- `manuscript/<section>.md` 更新
- `changelog.yml` 追加一行
- 每段末尾以 HTML 注释标注依据：`<!-- C01/R01 -->`

## 禁止

- 无 R-id 的数字。
- 无 C-id 的结论。
- 越权修改 `decisions.yml` 中的锁定决策。