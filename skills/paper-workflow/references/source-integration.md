# 外部来源与取舍

本工作流的方法来源分三类：完全自写的模块、从上游开源技能改编的模块、以及整份安装的第三方技能。改编不等于复制：只取方法骨架，规则与措辞由本项目重写；未复制上游脚本，也不声称完整复现其评测效果。

| 来源 | 落入模块 | 保留 | 排除 |
|---|---|---|---|
| WenyuChiou/academic-writing-skills | 架构、起草、对齐、评审、总控 | 论证链、段落证据计划、双向校验、修订传播 | 不以它的流程替代本工作流的 Gate |
| felixschrimpff/academic-writing-skill | scientific-prose | 学科与章节校准、过度删减检查 | 不引入个人标点偏好，不把语料频率当期刊指标 |
| Boom5426/Nature-Paper-Skills | figure-planner、citation-verifier、rebuttal-response、submission-audit | 图文证据关系、引文分层核验、回复与实际改稿绑定 | 不导入 Nature 默认期刊、图宽、字体、色板或文章结构 |
| Kiterlin/anti-defensive-writing | anti-defensive-writing | 完整技能文件 | 保留原文件与授权信息 |
| larashero3-dotcom/lieflat-less-ai-tone | lieflat-less-ai-tone | 完整技能文件（MIT） | 作为第三方组件单独存放，保留其 LICENSE |

上游关于语料规模与效果的描述是原作者的报告，本工作流没有独立复核。后续如需同步上游更新，按来源重新核对差异，不自动覆盖本地规则。

## 版本与追溯

每个外部来源在引入时记录仓库、路径与核对日期；本次整理对应的核对日期见仓库 `docs/attribution.md`。改动规则时同步更新该表，避免“记得改过”但无法追溯的情况。