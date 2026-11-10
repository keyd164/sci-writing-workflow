---
name: figure-planner
description: 为本论文规划主图、panel、图注及 Results 的证据关系，处理图表过载和主文补充材料分配；不负责低层绘图。
---
# Figure Planner
读取 paper-workflow、claims/results/figures/tables 登记册及目标图文。
选择性参考 Nature-Paper-Skills 的 figure-planner；来源见 ../paper-workflow/references/source-integration.md。

为每图指定一个主导科学结论及 C-id；每 panel 绑定实际 R-id、比较对象、样本和单位，区分主证据、方法定义、敏感性和补充说明。若图无法支持所述结论，缩小结论或列缺证据，不增造 panel。
输出 manuscript/figure-plan.md：图号/主张/panel 功能/证据/主文或补充/对应段落/图注必要信息/待核项。
图注核对不确定性含义、统计方法、缩写、样本与 panel 字母；Results 与图注不得强于实际图示。不能把会改变解释的敏感性或负结果藏入补充。
G1/G2 前只产候选方案，登记册锁定项变更提出建议；获准的图文更新需同步图号和引用。
制作实际科研图时再使用可用 nature-figure 技能；遵守其后端选择流程。规划阶段不要求先选 Python/R。
不默认 Nature 尺寸/字体/配色；生产要求由 journal.yml 中已核实的目标期刊规则决定。

已有图件的图注撰写、精简和逐项核验由 figure-legend 承接；仅修改图注不触发绘图后端选择。实际图件更新后，再由 figure-legend 复核面板、统计解释和引用。

