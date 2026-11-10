---
name: journal-adapter
description: >-
  期刊适配技能。论文需要按目标期刊调整（结构、字数、摘要格式、引用风格、
  图表政策），或更换目标期刊重新适配时使用。用户说"按某刊格式调整"
  "换期刊适配""这个刊有什么要求"时触发。以 journal.yml 为唯一配置源；
  未核验字段必须标 unverified 并推动核实，严禁凭记忆编造期刊规则。
---

# 期刊适配

## 职责

让同一篇论文高效适配不同期刊：只改呈现层约束，不重写科学内容。任何期刊的具体规则，只能来自该刊官方作者指南或编辑部的书面说明。

## 执行步骤

1. 读 `.paper/journal.yml`：确认目标期刊与各字段状态。
2. **规则核验优先**：
   - 任何 `status: unverified` 字段 → 先尝试获取作者指南（检索、抓取官方页面），核验后回填 `verified` + 来源 URL + 核验日期。
   - 无法核验 → 保持 `unverified`，列入 `submission-audit` 阻塞项。**严禁**凭训练记忆填写字数、结构或格式。
3. 适配检查（按字段逐项）：
   - article_type / 结构（IMRaD 或期刊专用结构）
   - word_limit / abstract_limit / abstract_structure
   - reference_style（顺序编码 vs 著者—年份）
   - figure_limit / table_limit / supplement_policy
   - data & code availability 声明要求
   - ethics / funding / contributions / competing interests 的声明位置
4. 呈现层调整：
   - 摘要按期刊结构重组，内容不变
   - 图表数量超限 → 给出转补充材料的优先级建议，不动科学内容
   - 引用风格转换（由 `references.yml` 驱动）
5. framing 检查：
   - Introduction 前两句是否完成 scope 定位与 novelty 陈述？
   - Cover letter 是否明确目标栏目、与刊物的契合点。
6. 输出适配报告，更新 `journal.yml` 与 `changelog.yml`。

## 输出

- 适配报告（逐字段：verified 值 / 调整动作 / 未核实阻塞项）
- 更新后的 `journal.yml`（unverified 字段随核验递减）
- 换刊时新建 `journal.<slug>.yml`，保留历史版本

## 禁止

- 编造期刊规则（任何未核实字段）。
- 为迁就字数限制删改科学内容；只能建议转补充材料或精简呈现。
- 修改 claims / results / decisions 中的科学内容。
- 把某一家期刊的默认规范（图宽、字体、色板、文章结构）当成通用标准。