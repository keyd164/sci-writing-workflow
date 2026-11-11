# 变更记录

格式参考 Keep a Changelog，版本号遵循语义化版本。

## [1.2.0] - 2026-11-11

### 变更

- 博客站点迁出到独立仓库 `keyd164.github.io`，站点地址变为 `https://keyd164.github.io/`，不再使用带仓库名的项目页路径。
- 移除本仓库的 `site/` 与 `.github/workflows/pages.yml`，本仓库只承载技能、模板与文档。
- `scripts/check_repo.py` 的站点检查改为仓库边界检查：出现 `site/` 或 `pages.yml` 即报错。
- `docs/publishing.md` 重写为两个仓库的分工、改文章/改技能流程与常见失败处理。

## [1.1.0] - 2026-11-11

### 新增

- `site/`：Jekyll 站点（minima 主题、`lang: zh-CN`），首页与长文文章，供 GitHub Pages 渲染。
- `.github/workflows/pages.yml`：构建 `site/` 并部署到 GitHub Pages。
- `.github/workflows/verify.yml`：推送与 PR 时跑结构自检，并拦截私有项目痕迹。
- `scripts/check_repo.py`：本地结构自检（技能 frontmatter、模板 YAML、站点 front matter、相对链接、工作流 YAML）。
- `docs/publishing.md`：推送、启用 Pages 的完整步骤与常见失败处理。

### 说明

- 站点文章与仓库外的博客稿同源，正文不含 H1（由布局生成）。

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