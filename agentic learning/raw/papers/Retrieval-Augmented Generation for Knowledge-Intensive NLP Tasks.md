---
type: source
source_type: paper
title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
url: "https://arxiv.org/abs/2005.11401"
pdf: "assets/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf"
extracted: "extracted/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.extracted.md"
author:
  - Lewis et al.
site: arXiv
topic:
  - rag
  - retrieval
created: 2026-05-05
updated: 2026-05-07
last_checked: 2026-05-07
freshness: stable
conflicts: []
status: growing
source:
related:
  - "[[RAG]]"
  - "[[LLM]]"
  - "[[Parametric Memory]]"
  - "[[Non-Parametric Memory]]"
  - "[[Retriever]]"
---

# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## 为什么收

这是 RAG 的经典论文来源之一。它帮助我理解“模型参数里的知识”和“外部检索知识”之间的边界。

## 先读什么

- Abstract
- Introduction
- Method

## 需要我读的内容

目标：理解 [[RAG]] 的原始边界：生成模型参数里的知识和外部可检索知识如何结合。

### 必读

- Abstract：抓住 parametric memory 与 non-parametric memory 的组合。
- 1 Introduction：理解只依赖模型参数的缺点：难更新、难溯源、可能 hallucination。
- Figure 1：看 RAG 的整体流程：query -> retriever -> document index -> generator。
- 2 Methods：只理解 retriever 和 generator 两个组件。
- 2.1 Models：只抓 RAG-Sequence 和 RAG-Token 的区别，不深入公式。
- 2.5 Retriever：理解 dense vector index 和 top-K retrieval。
- 6 Discussion / Conclusion：看作者如何描述知识更新和检索边界。

### 选读

- Ablation 相关段落：看 learned retrieval 为什么重要。
- Human evaluation：看 RAG 是否更 factual/specific。

### 可以先跳过

- 详细概率公式。
- 每个数据集的实验表格。
- Appendix 的训练细节。

### 读完要能回答

- [[Parametric Memory]] 和 [[Non-Parametric Memory]] 分别是什么？
- [[Retriever]] 在 RAG 里具体负责什么？
- RAG 为什么能更新知识，但仍不能保证正确？
- RAG 和 [[Memory]] 为什么不能画等号？
- 这篇论文里的 RAG 和现在的 [[Agentic RAG]] 差在哪里？

### 读完要更新

- [[RAG]]
- [[Retriever]]
- [[Parametric Memory]]
- [[Non-Parametric Memory]]
- [[Memory]]

## 一句话

RAG 把检索器和生成模型结合起来，让模型在回答时使用外部文档作为知识来源。

## 已提取文件

- PDF：`assets/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`
- 抽取正文：`extracted/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.extracted.md`

## Ingest 摘要

这篇论文对当前学习的价值，是把 [[RAG]] 的核心边界讲清楚：模型参数里的知识是 [[Parametric Memory]]，外部可检索知识是 [[Non-Parametric Memory]]。

核心主张：

- 预训练模型可以在参数里存事实，但难以精确更新、引用和解释来源。
- RAG 把生成模型和 [[Retriever]] 连接起来，让生成过程可以条件化在检索到的文档上。
- RAG 不是纯 prompt 技巧，而是一种把参数化模型和外部知识索引结合的架构。
- 外部索引可以更新，因此比只依赖模型参数更适合知识变化的场景。

## 可以拆成概念卡

- [[RAG]]
- [[Retriever]]
- embedding
- vector database
- hallucination
- [[Parametric Memory]]
- [[Non-Parametric Memory]]

## 我的疑问

- 检索错误时，生成模型会怎样放大错误？
- RAG 和 Agent 的 memory 有什么区别？

## 边界提醒

RAG 能增强知识访问，但不自动保证事实正确。
