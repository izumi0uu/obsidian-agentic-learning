---
type: concept
topic:
  - rag
  - retrieval
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[RAG 类型对比]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[RAG 类型对比#一张表先抓住]]"
related:
  - "[[RAG]]"
  - "[[Vector Database]]"
  - "[[Retriever]]"
  - "[[Reranking]]"
---

# Hybrid Search

## 一句话

Hybrid Search 是把向量语义检索和关键词/全文检索结合起来的检索方式。

## 它解决什么问题

向量检索懂语义，但可能漏掉专有名词、编号、错误码、函数名。关键词检索能抓精确词，但不懂语义。Hybrid Search 让两者互补。

## 它不是什么

Hybrid Search 不是简单把两个结果列表拼起来。

真实系统还要处理权重、去重、排序、过滤、rerank 和引用。

## 最小例子

```text
query
  -> vector search top 50
  -> BM25/fulltext top 50
  -> merge + deduplicate
  -> rerank
  -> answer
```

## 常见误解和风险

- 关键词权重太高会退化成传统搜索。
- 向量权重太高会漏掉精确实体。
- 合并策略不透明时很难排查检索失败。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[RAG 类型对比]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[Vector Database]]
- [[Reranking]]
- [[Retriever]]
