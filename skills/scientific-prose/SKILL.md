---
name: scientific-prose
description: >-
  科学语言层技能。科学结构与证据已锁定（G3 已批准）后，用于消除稿件中的
  AI 式表达并校准为自然的科研英语：模板化句式、过度总结、过度强调、
  因果语言越界、为"像人"而人为复杂化。用户说"润色这段""去 AI 味"
  "语言层处理""humanize"时触发。不得早于结构与证据锁定运行；
  不得改变数字、结论或科学内容。
---

# 科学语言层

## 职责

把已经科学正确的稿子校准为自然的科研英语。这是语言层，不是内容层。

## 前置铁律

- `.paper/workflow.yml` 中 G3 必须已批准；否则拒绝运行并报告。
- 输出的任何版本都**不得改变**：数字、结论（C-id）、样本或模型定义。发现科学内容有问题 → 退回 `evidence-drafting` / `evidence-lock`，不在本层修。

## 检查项（逐项执行）

先读[学科与章节校准](references/register-calibration.md)。以下检查按功能与上下文判断，不把词表命中当作删除指令；必要的第一人称、被动语态、路标、术语及限定要保留。

### ① 模板化句式
连续出现 “We assessed… We calculated… We estimated… We further examined…” → 重组句式（主语多样化、合并相关信息、主被动分工）。

### ② 过度总结
“These findings collectively demonstrate that…” 这类句子在多数正文段落中不需要；删除或改为具体的下一句内容。

### ③ 过度强调
strikingly / remarkably / importantly / substantially / compellingly / dramatically —— 无数据支持一律删除；有数据支持改为数值陈述。

### ④ 因果语言越界
逐字扫描 `claims.yml` 中 `global_language_lock.forbidden` 列出的表述，命中后核对语境与被锁定的主张；只改对本研究构成越界的陈述，改为对应的关联性、条件对比或可能性措辞，并记录修改位置。

### ⑤ 人为复杂化
长句堆叠、生僻词替换、刻意不对称结构——“像人”不等于 complicated；目标是 **natural scientific English**：清晰、具体、可核验。

### ⑥ 术语与格式
按 `terminology.yml` 统一术语，数字格式按 `number_format`，英式/美式拼写按 `journal.yml`（未核实前不擅自统一，列入待核实项）。

## 流程

1. 读目标段落 + `claims.yml` + `terminology.yml`。
2. 逐项检查并修改；每处修改注明理由（检查项编号）。
3. 输出修改前后对照（关键处）+ 修改清单。
4. 更新 `changelog.yml`。

作者要求组合润色时，按[组合契约](../paper-workflow/references/writing-composition.md)衔接 `anti-defensive-writing` 与 `lieflat-less-ai-tone`。每项修改标明实际执行模块，不能把引用补充记成纯语言修改。

## 输出格式

```
## 修改清单
- [④] L12: "caused" → "was associated with"（claims.yml C01 forbidden_language）
- [①] L15–18: 四个 "We …" 连续 → 合并为两句
...
## 未修改的科学内容声明
本层未改动任何数字与结论。
```

## 禁止

- 同义词替换式 humanize（把 associated with 换成 linked to 并无意义）。
- 改变数值、CI、p 值、样本量。
- 在 G3 批准前运行。
- 把修改扩展到科学判断（“这个结论太强”属于 red-team 的职责）。