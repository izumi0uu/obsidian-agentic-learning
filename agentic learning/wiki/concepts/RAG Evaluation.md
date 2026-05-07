---
type: concept
topic:
  - rag
  - evaluation
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[RAG]]"
  - "[[Evaluation]]"
  - "[[Reranking]]"
  - "[[Retriever]]"
---

# RAG Evaluation

## 一句话

RAG Evaluation 是评估检索、上下文、引用和最终回答质量的一组方法。

## 它解决什么问题

RAG 系统失败可能发生在很多层：没检到、检错了、排序错了、上下文太脏、模型误读、引用不支持答案。只看最终回答很难定位问题。

代表工具包括 Ragas、DeepEval、Phoenix、Promptfoo 等。

## 它不是什么

RAG Evaluation 不是只问“答案对不对”。

它也不是只靠 LLM-as-Judge。关键任务需要人工样本、规则、引用校验和回归集。

## 最小例子

```text
问题集 -> retrieve -> 检查 recall / context precision -> answer -> faithfulness / citation check
```

## 常见误解和风险

- judge 模型可能偏向流畅答案。
- 没有标准答案时，指标会更不稳定。
- 只评生成不评检索，会错过根因。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[Agent 工程基础设施主源]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[Evaluation]]
- [[Retriever]]
- [[Reranking]]
