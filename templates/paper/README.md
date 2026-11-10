# .paper 登记册模板

把这 12 个文件复制到论文项目根目录下的 `.paper/`。它们是工作流的唯一事实来源：正文、图表、引用都必须能回溯到这里的条目。

| 文件 | 管什么 | 谁写 |
|---|---|---|
| `paper.yml` | 题目、作者、研究问题、目标期刊 | 作者 |
| `workflow.yml` | 阶段与 G1–G6 门控状态 | 作者批准，模块记录 |
| `claims.yml` | 每条结论的强度与语言锁定 | 架构阶段 |
| `results.yml` | 每个数字的 R-id、来源文件、核验状态 | 证据锁定 |
| `methods.yml` | 每个模型的 M-id、样本、必现句子 | 起草阶段 |
| `decisions.yml` | 已锁定的方法学与写作决策 | 作者 |
| `terminology.yml` | 术语与数字格式 | 作者 |
| `references.yml` | 文献条目与核验状态 | 引文核验 |
| `figures.yml` | 图与 panel 的证据绑定 | 图表规划 |
| `tables.yml` | 表与证据绑定 | 图表规划 |
| `journal.yml` | 目标期刊规则与核验状态 | 期刊适配 |
| `changelog.yml` | 实质修改记录 | 所有模块 |

约定：条目 id 稳定、不复用；`verified` 只表示“已对照来源文件核验”，不表示科学成立；任何 Gate 的 `approved` 只能由作者填写。