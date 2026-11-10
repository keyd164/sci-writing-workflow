# 科研论文写作工作流（Paper Workflow Skills）

一套把"写论文"拆成可核对状态机的技能集合：19 个技能（18 个自写 + 1 个第三方）+ 12 个登记册模板，覆盖从立项清点、证据锁定、正文起草、语言校准、模拟审稿到投稿审计的全过程。适用于 Claude Skills / Codex Skills 这类以 `SKILL.md` 为入口的智能体环境。

核心主张：**模型不替你决定科学结论，只负责让每个数字有来源、每句结论有强度、每次修改有痕迹。**

## 解决什么问题

一次性生成整篇论文，问题不在文笔，而在无法定位错误：

- 正文里的数字和输出文件对不上，没人知道哪个是对的；
- 摘要写了结论，但结果里并没有支撑它的证据；
- Results 出现 Methods 从未定义的模型；
- 换刊改格式时顺手删了科学内容；
- 审稿意见回复里写了"已修改第 12 页"，其实没改。

这套流程用两道约束解决它们：**登记册**（数字与主张的唯一事实来源）与**门控**（没有作者批准就不进入下游）。

## 六个门控

```
清点建档 → 架构 ─G1→ 证据锁定 ─G2→ 起草 → 对齐 ─G3→ 语言层
        → 模拟审稿 ─G4→ 修订 → 期刊适配 → 投稿审计 ─G5→ 提交授权 ─G6
```

| 门 | 拦住的事 |
|---|---|
| G1 架构批准 | 结论先行、分析拼盘、标题预写未做的发现 |
| G2 证据锁定 | 数字无法追溯、旧稿数值倒灌、单位口径混用 |
| G3 对齐批准 | Results 有而 Methods 无的模型、样本数不一致 |
| G4 意见处置 | AI 自行改稿、拒绝意见却写进回复 |
| G5 投稿审计 | 字数超限、声明缺项、引用断裂 |
| G6 提交授权 | 未经确认对外提交 |

未批准只阻止下游产出，不阻止为审批做核验、列冲突、准备候选方案。详见 [docs/workflow.md](docs/workflow.md)。

## 技能清单

| 技能 | 作用 | 写入边界 |
|---|---|---|
| `paper-workflow` | 总控：读状态、选模块、报下一步 | 只调度，不改内容 |
| `paper-bootstrap` | 扫描项目、建立 `.paper/` 登记册、标冲突 | 不写正文 |
| `scientific-architecture` | 问题—缺口—贡献—主张—证据映射与提纲 | 需 G1 |
| `evidence-lock` | 每个数字绑定来源文件与哈希 | 核实后更新登记册 |
| `statistical-results-lock` | 数字、单位、CI、模型口径一致性 | 只读 |
| `causal-inference-audit` | 识别假设、生态学推断、因果措辞边界 | 只读 |
| `climate-counterfactual-audit` | 反事实与情景外推的可比性 | 只读 |
| `evidence-drafting` | 按证据顺序写 Methods/Results/Discussion | 不改数字与结论 |
| `methods-results-alignment` | 方法—结果双向覆盖检查 | 需 G3 |
| `scientific-prose` | 语言层校准，去模板化与过度强调 | 需 G3，不改科学内容 |
| `anti-defensive-writing` | 去掉过度设防、重复辩解与谦辞 | 保留必要限定 |
| `lieflat-less-ai-tone` | 按编号白名单去除 AI 写作痕迹（第三方） | 未命中逐字保留 |
| `figure-planner` | 图与 panel 的证据绑定、主文/补充分配 | 只规划 |
| `figure-legend` | 图注撰写与核验，去 Methods 重复 | 不补造检验 |
| `citation-verifier` | 本地/身份/支持三层引文核验 | 默认只读 |
| `reviewer-red-team` | 四个视角模拟审稿，只评论不改稿 | 作者作 G4 决定 |
| `rebuttal-response` | 审稿意见拆解为子问题、决策与改稿位置 | 不代作决定 |
| `journal-adapter` | 按目标期刊调整呈现，规则须核验 | 不编造期刊规则 |
| `submission-audit` | 投稿前全项 pass/fail 审计 | 只审计，不提交 |

## 目录结构

```
sci-writing-workflow/
├─ skills/                     # 18 个自写技能，各自含 SKILL.md
│  └─ paper-workflow/
│     ├─ references/           # 模块契约、来源整合、语言层组合契约、段落证据计划
│     └─ scripts/check_gates.py  # 只读状态报告
├─ third_party/
│  └─ lieflat-less-ai-tone/    # 第三方技能，保留其 MIT LICENSE
├─ templates/paper/            # 12 个登记册模板
├─ docs/
│  ├─ workflow.md              # 门控与产出边界
│  ├─ registries.md            # 登记册完整性规则
│  ├─ design-notes.md          # 设计取舍与局限
│  └─ attribution.md           # 上游来源与授权
├─ CHANGELOG.md
└─ LICENSE
```

## 安装

```bash
# 1. 克隆
git clone <repo-url> sci-writing-workflow

# 2. 复制技能到你的技能目录（按环境选择实际路径）
cp -r sci-writing-workflow/skills/* ~/.claude/skills/            # Claude Skills
# 或项目级：cp -r sci-writing-workflow/skills/* <project>/.agents/skills/

# 3. 第三方技能单独放置
cp -r sci-writing-workflow/third_party/lieflat-less-ai-tone ~/.claude/skills/

# 4. 可选：状态报告脚本依赖 PyYAML
python -m pip install pyyaml
```

## 快速开始

```bash
mkdir my-paper && cd my-paper
cp -r ../sci-writing-workflow/templates/paper .paper
python ../sci-writing-workflow/skills/paper-workflow/scripts/check_gates.py .
```

然后在智能体里说：

```text
继续 my-paper 的论文工作。先跑 paper-bootstrap，清点现有稿件、结果和图表，
建立 .paper/ 登记册，把发现的冲突列成清单给我确认。
```

后续只需说目标（"写 Methods""检查方法结果一致吗""模拟审稿""按目标期刊调整"），总控会选对应模块，不必记模块名。

## 判据

使用本工作流时，以下四条最能检验它是否真的在工作：

1. 正文里能不能找出一个没有 R-id 的数字？（能，就说明 G2 没落实）
2. 摘要里最"外向"的那句结论，能不能追到一条强度匹配的 C-id？
3. 图注里的误差线，读者能不能据此判断是 CI、SD 还是模型范围？
4. 换刊后，被删掉的内容是呈现还是证据？

## 已知局限

- 依赖登记册质量：登记册错了，后续检查会一致地错；它拦数字漂移，不拦科学判断错误。
- 不替代领域专家：两个审计技能只做边界检查，不判断识别策略是否成立。
- 期刊规则会过期：`journal.yml` 的 `verified` 带核验日期，投稿前需重新确认。
- 以英文稿件为主，中文期刊适配需自行补充结构规范。
- 不做投稿与版权事务，实际提交必须由作者完成。

## 来源与授权

本仓库规则文本采用 [MIT](LICENSE)。方法骨架参考了若干开源写作技能，第三方技能 `lieflat-less-ai-tone` 按原 MIT 授权存放，来源与取舍见 [docs/attribution.md](docs/attribution.md)。

## 版本

当前 1.0.0，变更记录见 [CHANGELOG.md](CHANGELOG.md)。