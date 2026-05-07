---
type: concept
topic:
  - rag
  - evaluation
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Self-RAG - Learning to Retrieve Generate and Critique]]"
evidence:
  - "[[Self-RAG - Learning to Retrieve Generate and Critique#为什么收]]"
related:
  - "[[RAG]]"
  - "[[Agentic Retrieval]]"
  - "[[Corrective RAG]]"
  - "[[Evaluation]]"
---

# Self-RAG

## 一句话

Self-RAG 是让模型自适应判断是否检索、如何生成、证据是否支持答案的一类 RAG 方法。

## 它解决什么问题

固定检索策略会浪费成本，也会在不需要检索时引入噪音。Self-RAG 想让模型根据任务需要选择检索，并批判生成内容是否被证据支持。

## 它不是什么

Self-RAG 不是简单在 prompt 里写“请自我反思”。

原始论文强调通过 reflection tokens 学习 retrieve、generate、critique 的控制信号。工程实现可以近似，但不能把名字泛化到所有自检 RAG。

## 最小例子

问题：“Transformer 论文是哪一年？”

模型可能判断需要检索，找到论文来源后生成答案，并检查证据是否足以支持年份。

问题：“把这句话改得更通顺。”

模型可能判断不需要外部检索。

## 常见误解 / 风险 / 边界细节

- 自我判断不等于真实可靠。
- 如果底层模型没训练过类似控制信号，prompt 近似效果有限。
- 对企业知识库，是否检索可能应由 policy 或任务类型决定。
- Self-RAG 和 [[Corrective RAG]] 都关注证据质量，但机制不同。

## 证据锚点

- Source: [[Self-RAG - Learning to Retrieve Generate and Critique]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[Agentic Retrieval]]
- [[Corrective RAG]]
- [[Evaluation]]
