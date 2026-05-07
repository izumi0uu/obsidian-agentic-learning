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
  - "[[Corrective Retrieval Augmented Generation]]"
evidence:
  - "[[Corrective Retrieval Augmented Generation#为什么收]]"
related:
  - "[[RAG]]"
  - "[[Retriever]]"
  - "[[Evaluation]]"
  - "[[Agentic Retrieval]]"
---

# Corrective RAG

## 一句话

Corrective RAG 是先评估检索证据质量，再决定直接生成、改写查询、重检索或走外部检索补救的 RAG 模式。

## 它解决什么问题

RAG 的答案质量高度依赖检索质量。检索到错误、过少或不相关文档时，模型会基于坏证据生成看似合理的错答案。

Corrective RAG 把“检索质量判断”加入流程，让系统能在证据差时修正。

## 它不是什么

Corrective RAG 不是简单多搜几次。

关键在于 retrieval evaluator 和基于评分的分支动作。

## 最小例子

用户问一个项目细节：

1. 初次检索只找到旧文档。
2. evaluator 判断证据不足。
3. 系统改写 query，并加入最新日期过滤。
4. 再检索后生成答案。

## 常见误解 / 风险 / 边界细节

- evaluator 本身会错。
- 外部 web fallback 可能引入不可信来源。
- 分支越多，trace 越重要。
- Corrective RAG 更适合高准确性场景，不一定适合低延迟问答。

## 证据锚点

- Source: [[Corrective Retrieval Augmented Generation]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[Retriever]]
- [[Agentic Retrieval]]
- [[Evaluation]]
