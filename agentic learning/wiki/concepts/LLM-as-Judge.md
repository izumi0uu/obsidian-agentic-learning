---
type: concept
topic:
  - evaluation
  - llm
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[LangSmith Evaluation and Observability]]"
  - "[[Langfuse Observability and Evaluation]]"
evidence:
  - "[[LangSmith Evaluation and Observability#为什么收]]"
  - "[[Langfuse Observability and Evaluation#为什么收]]"
related:
  - "[[Evaluation]]"
  - "[[Eval Harness]]"
  - "[[Trajectory Evaluation]]"
---

# LLM-as-Judge

## 一句话

LLM-as-Judge 是用另一个模型或同类模型作为评估器，对输出、引用、格式或过程进行评分。

## 它解决什么问题

很多 Agent 任务没有简单的标准答案，比如“总结是否忠实”“回答是否有帮助”“计划是否合理”。LLM-as-Judge 能把一部分主观评估自动化。

## 它不是什么

LLM-as-Judge 不是绝对裁判。

它会有偏差、漂移、被 prompt 影响，也可能被被评估内容诱导。高风险任务仍需要规则、人工和真实业务指标。

## 最小例子

评估一张概念卡：

- 是否有“一句话”。
- 是否说明“它不是什么”。
- 例子是否最小。
- 是否把 raw source 和 wiki synthesis 混在一起。

其中结构项可用规则，解释质量可用 LLM-as-Judge 辅助。

## 常见误解 / 风险 / 边界细节

- 裁判模型也需要校准和评估。
- 评分 prompt 应该版本化。
- 不要把敏感 trace 原样发给外部裁判模型。
- 最好保留 rationale 或标签，方便人工复查。

## 证据锚点

- Source: [[LangSmith Evaluation and Observability]]
- Source: [[Langfuse Observability and Evaluation]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Evaluation]]
- [[Eval Harness]]
- [[Trajectory Evaluation]]
- [[Observability]]
