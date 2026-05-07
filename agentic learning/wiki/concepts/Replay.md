---
type: concept
topic:
  - evaluation
  - observability
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
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[Eval Harness]]"
---

# Replay

## 一句话

Replay 是用保存的输入、工具结果、检索结果或环境快照重放 Agent 执行过程。

## 它解决什么问题

Agent 失败后，如果不能复现，就很难知道修复是否有效。Replay 让一次失败可以变成可调试、可比较、可回归测试的样本。

## 它不是什么

Replay 不是重新问模型同一个问题。

真正的 replay 要尽量控制变量：相同输入、相同工具返回、相同检索材料、相同环境状态，或者明确标注哪些部分被重新采样了。

## 最小例子

一次 Browser Agent 点错按钮：

- 保存截图序列。
- 保存每次 action。
- 保存 DOM 或 accessibility snapshot。
- 修复策略后重放，检查它是否还会点错。

## 常见误解 / 风险 / 边界细节

- 外部网站变化会破坏 replay。
- 工具结果如果没有固定，会让结果不可比较。
- replay 数据可能包含敏感内容。
- replay 更适合调试失败，不等于完整可靠性评估。

## 证据锚点

- Source: [[LangSmith Evaluation and Observability]]
- Source: [[Langfuse Observability and Evaluation]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Trace]]
- [[Observability]]
- [[Eval Harness]]
- [[Sandbox Workspace]]
