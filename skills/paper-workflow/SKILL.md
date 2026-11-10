---
name: paper-workflow
description: 科研论文写作总控。按阶段管理选题架构、证据锁定、正文起草、语言校准、模拟审稿、期刊适配与投稿审计；用于继续论文、检查进度、判断下一步该调用哪个模块。
---

# 论文工作流（总控）

读项目根的 `.paper/paper.yml`、`.paper/workflow.yml`，以及本技能的[模块契约](references/module-contracts.md)。

只有一个用户入口：`paper-workflow`。按用户意图与已存在的成果选择模块，不要求用户记住模块名。

项目根按以下顺序定位：用户明确给出的路径 → 环境变量 `PAPER_PROJECT_ROOT` → 当前目录逐级向上查找 `.paper/`。明确路径无法定位时报告，不悄悄改用其他项目。

可运行 `python scripts/check_gates.py <项目路径>` 获取只读状态报告（依赖 PyYAML）。脚本返回 0 只代表 YAML 可读、未发现结构冲突，**不代表**任何 Gate 已通过，也不代表科学结论成立。没有运行环境时直接读 YAML，不跳过审批。

## 阶段与门控

| Gate | 名称 | 通过后允许 |
|---|---|---|
| G1 | 架构批准 | 依据问题—主张—证据映射开始锁定证据 |
| G2 | 证据锁定 | 正文起草（Methods/Results/Discussion 等） |
| G3 | 对齐批准 | 语言层（润色、去 AI 味、去防御性表达） |
| G4 | 意见处置 | 按作者逐条决定执行修订 |
| G5 | 投稿审计通过 | 冻结待提交版本 |
| G6 | 提交授权 | 实际对外提交 |

`workflow.yml` 是唯一的阶段状态来源。目录存在、报告已生成、数字标了 verified，都不等于作者批准。未批准 Gate 只阻止受限的下游产出，不阻止为审批而做的核验、冲突报告与候选方案。

## 调度与权限

- 遵守既有 G1–G6 与 `decisions.yml`，不擅自新增人工 Gate。
- 用户已有的明确批准可以记录；其余不得代批。
- 按模块契约先准备可审阅成果，再请求必需的作者决定；只问仍缺失的决定。
- 只调用当前任务必要的模块；多种审稿视角不等于启动多个代理。
- 只读审计（`statistical-results-lock`、`causal-inference-audit`、`climate-counterfactual-audit`、`citation-verifier`）发现问题时输出清单与补丁建议；登记册的实际更新由 `evidence-lock` 负责。
- 实质修改追加 `changelog.yml`；不把本轮工具升级记成论文阶段完成。

## 路由

先识别任务，再检查依赖：

| 现状 | 下一步 |
|---|---|
| 没有 `.paper/` 或登记册不完整 | `paper-bootstrap` |
| 有证据但缺论证图/提纲 | `scientific-architecture` |
| 主张已定、数字未绑定来源 | `evidence-lock` |
| 需要复核统计口径与单位 | `statistical-results-lock` |
| 需要审查推断与因果措辞 | `causal-inference-audit` |
| 涉及气候/暴露反事实与外推 | `climate-counterfactual-audit` |
| G1/G2 已批准，要起草正文 | `evidence-drafting` |
| 正文已成，需方法—结果互检 | `methods-results-alignment` |
| G3 已批准，要做语言层处理 | `scientific-prose`（可组合 `anti-defensive-writing`、`lieflat-less-ai-tone`） |
| 需要图表证据布局 | `figure-planner` |
| 已有图件，要写/核图注 | `figure-legend` |
| 引用完整性、身份或支撑关系存疑 | `citation-verifier` |
| 全文完成，投稿前模拟评审 | `reviewer-red-team` |
| 收到真实审稿意见 | `rebuttal-response` |
| 换目标期刊、按刊调整 | `journal-adapter` |
| 准备投稿前的全项检查 | `submission-audit` |

组合润色的顺序：有新增文献时先 `citation-verifier` → `anti-defensive-writing` → `scientific-prose` → `lieflat-less-ai-tone`。三者只改明确命中规则的表达，未命中原文保留，细则见[组合契约](references/writing-composition.md)。

修订后重新核验受影响的证据、对齐与引用，不直接沿用过期报告。G5/G6 均获批准且无阻塞项才可记录发布；实际提交需用户明确授权。

## 每次输出

项目、当前阶段、相关 Gate、已完成成果、仍缺的证据或决定、下一步模块，并给出具体文件位置。

报告写入项目 `audits/`（有实际报告时才创建），写明所审输入路径、SHA256、核验时间、发现及覆盖缺口；输入变化即需重核受影响结论。