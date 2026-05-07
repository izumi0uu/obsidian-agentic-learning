---
type: concept
topic:
  - rag
  - ingestion
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[RAG]]"
  - "[[Embedding]]"
  - "[[Document Ingestion]]"
---

# Chunking

## 一句话

Chunking 是把长文档切成适合检索和放入上下文的小片段。

## 它解决什么问题

LLM 一次能看的上下文有限，向量检索也需要可比较的片段。切分太大，检索不准；切分太小，语义不完整。

## 它不是什么

Chunking 不是随便按固定字数切。

它也不是越小越好。好的 chunk 要保留标题、层级、表格含义、引用来源和上下文边界。

## 最小例子

```text
一份 30 页 PDF
-> 按章节/标题/段落切分
-> 每个 chunk 保存 source、page、section、text
-> embedding 和索引
```

## 常见误解和风险

- 表格、代码、公式和图片说明很容易被切坏。
- chunk overlap 可以补上下文，但会增加重复和成本。
- 没有 source metadata，后面很难引用和排错。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[Embedding]]
- [[Document Ingestion]]
- [[Retriever]]
