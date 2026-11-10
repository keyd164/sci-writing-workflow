# 来源与授权

## 本项目自写

`paper-workflow`、`paper-bootstrap`、`scientific-architecture`、`evidence-lock`、`statistical-results-lock`、`causal-inference-audit`、`climate-counterfactual-audit`、`evidence-drafting`、`methods-results-alignment`、`figure-planner`、`citation-verifier`、`reviewer-red-team`、`journal-adapter`、`submission-audit`、`rebuttal-response` 的规则文本为本仓库编写，采用 MIT 授权（见根目录 `LICENSE`）。

`scientific-prose`、`figure-legend`、`anti-defensive-writing` 的方法骨架来自下列开源项目，规则与措辞经重写；`lieflat-less-ai-tone` 为整份第三方技能，按原授权存放。

## 上游来源与取舍

| 来源 | 落入模块 | 保留 | 排除 |
|---|---|---|---|
| [WenyuChiou/academic-writing-skills](https://github.com/WenyuChiou/academic-writing-skills) | 架构、起草、对齐、评审 | 论证链、段落证据计划、双向校验、修订传播 | 不用其流程替代本仓库的门控 |
| [felixschrimpff/academic-writing-skill](https://github.com/felixschrimpff/academic-writing-skill) | scientific-prose | 学科与章节校准、过度删减检查 | 不引入个人标点偏好，不把语料频率当期刊指标 |
| [Boom5426/Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills) | figure-planner、citation-verifier、rebuttal-response、submission-audit | 图文证据关系、引文分层核验、回复与改稿绑定 | 不导入 Nature 默认期刊、图宽、字体、色板与文章结构 |
| [Kiterlin/anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) | anti-defensive-writing | 技能文件与其规则 | — |
| [larashero3-dotcom/lieflat-less-ai-tone](https://github.com/larashero3-dotcom/lieflat-less-ai-tone) | third_party/lieflat-less-ai-tone | 整份技能，含其 MIT LICENSE 与 README | 不改写其规则；如需调整，另建适配说明 |

上游对语料规模、区分度与效果的描述均为原作者报告，本仓库未独立复核，转载时不要当作已验证结论。

## 第三方组件

`third_party/lieflat-less-ai-tone` 保留原始 `LICENSE`（MIT，Copyright © 2026 shiujan）与 `README.md`。分发本仓库时请一并保留这两个文件。`anti-defensive-writing` 若上游另有授权声明，以其原始仓库为准。

## 引用建议

若在文章或课程中介绍本工作流，建议引用本仓库地址与版本号（见 `CHANGELOG.md`），并说明上游来源，避免把改编成果表述为原创方法。