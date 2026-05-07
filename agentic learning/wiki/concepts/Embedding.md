---
type: concept
topic:
  - rag
  - llm
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
  - "[[Vector Database]]"
  - "[[Retriever]]"
---

# Embedding

## 一句话

Embedding 是把文本、图片或其他对象转换成向量表示，让系统可以用距离或相似度计算“语义接近”。

## 它解决什么问题

用户的问题和文档原文不一定用同样措辞。Embedding 让系统能找“意思相近”的片段，而不只找关键词完全匹配。

## 它不是什么

Embedding 不是理解本身，也不是事实验证。

两个文本向量相似，只表示模型认为它们语义接近，不表示检索结果一定能回答问题。

## 最小例子

```text
"如何重置密码？" -> [0.12, -0.04, ...]
"忘记密码怎么办？" -> [0.11, -0.05, ...]
```

这两个向量距离近，所以可以被语义检索匹配到。

## 常见误解和风险

- 模型、语言、领域不同，embedding 质量会变。
- 长文档直接 embedding 可能稀释重点，所以需要 [[Chunking]]。
- embedding 不处理权限、时效和事实可靠性。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[Vector Database]]
- [[Retriever]]
- [[Chunking]]
