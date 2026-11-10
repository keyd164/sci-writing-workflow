# 变更记录

格式参考 Keep a Changelog，版本号遵循语义化版本。

## [1.0.0] - 2026-11-10

### 新增

- 从个人论文项目中的写作技能整理出可公开分发的技能集合：18 个技能、12 个登记册模板。
- `paper-workflow` 总控：G1–G6 门控、模块路由表、只读状态脚本 `scripts/check_gates.py`。
- 证据链路：`evidence-lock`（数字绑定）、`statistical-results-lock`（口径核对）、`causal-inference-audit` 与 `climate-counterfactual-audit`（推断边界）。
- 写作链路：`scientific-architecture`、`evidence-drafting`、`methods-results-alignment`。
- 语言层：`scientific-prose`、`anti-defensive-writing`、`lieflat-less-ai-tone`（第三方）与组合契约。
- 收尾链路：`figure-planner`、`figure-legend`、`citation-verifier`、`reviewer-red-team`、`rebuttal-response`、`journal-adapter`、`submission-audit`。
- 文档：门控说明、登记册完整性规则、设计取舍与局限、来源与授权。

### 变更（相对原始内部版本）

- 移除具体研究项目的私有内容：项目名、内部决策编号、特定数据集与期刊名、项目绝对路径、个人审计记录路径。
- 门控命名改为通用表述，路由表按"现状 → 下一步"重写，不再依赖单一项目的既定方向。
- 期刊适配、审稿红队、投稿审计中的领域限定改为可配置：规则来源必须是已核验的 `journal.yml`，不再内置某家期刊的默认规范。
- 语言层组合契约去除项目专属条款，保留顺序、边界与记录要求。
- 补充 MIT 授权、来源表与第三方组件说明。

### 移除

- 项目专属图注适配文件与个人审计快照；第三方技能改为 `third_party/` 独立存放。