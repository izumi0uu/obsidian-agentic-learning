---
type: concept
topic:
  - rag
  - memory
status: seed
created: 2026-05-05
updated: 2026-05-05
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]"
evidence:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#为什么收]]"
related:
  - "[[RAG]]"
  - "[[Parametric Memory]]"
  - "[[Retriever]]"
  - "[[Memory]]"
---

# Non-Parametric Memory

## 一句话

Non-Parametric Memory 是模型参数外部的可检索知识存储，例如文档索引、向量库或知识库。

## 它解决什么问题

外部知识可以被更新、替换、审查和引用。RAG 使用它来补足模型参数知识难更新、难溯源的问题。

## 它不是什么

Non-Parametric Memory 不是 Agent 的全部记忆。

它更偏知识存储，不自动包含用户偏好、任务状态、历史轨迹或安全策略。

## 最小例子

把 Wikipedia 文档放进 dense vector index，再根据问题检索相关 passage，这就是 RAG 论文里的非参数记忆例子。

## 边界细节

它和 [[Memory]] 的关系是：Non-Parametric Memory 是记忆的一种实现材料，但 Agent memory 还需要写入、更新、冲突处理、过期和权限。

## 证据锚点

- Source: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[Retriever]]
- [[Parametric Memory]]
- [[Memory]]
