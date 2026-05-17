---
type: source
source_type: paper
title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
url: https://arxiv.org/abs/2005.11401
pdf: assets/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf
extracted: extracted/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.extracted.md
author:
  - Lewis et al.
site: arXiv
topic:
  - rag
  - retrieval
created: 2026-05-05
updated: 2026-05-15
last_checked: 2026-05-11
freshness: stable
conflicts: []
status: growing
source: https://arxiv.org/abs/2005.11401
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

目标：理解 RAG 的原始边界：参数化记忆与非参数化外部记忆如何组合。

### 必读

> 使用规则：必读部分要直接提取证据。短内容摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / parametric + non-parametric memory

- 位置：Extracted Markdown `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.extracted.md` / Page 1 / Abstract
- 为什么必读：这里是 [[RAG]] 的经典定义来源：生成模型和外部检索记忆组合。
- 原文短摘：
  > models which combine pre-trained parametric and non-parametric memory for language generation
- 中文概括：
  - RAG 把预训练 seq2seq 模型作为参数化记忆，把可检索文档索引作为非参数化记忆。
  - 生成过程不是只依赖 prompt，而是条件化在检索到的文档上。
- 我需要理解的机制：
  1. parametric memory
  2. non-parametric memory
  3. retrieval-augmented generation
- 支撑概念：
  - [[RAG]]
  - [[Parametric Memory]]
  - [[Non-Parametric Memory]]
- 证据边界：
  - 这段定义的是 RAG 原始架构，不等于现代所有 RAG pipeline、agentic retrieval 或企业搜索实现。

#### 必读块 2：Figure 1 / retriever + generator 流程

- 位置：Extracted Markdown `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.extracted.md` / Page 2 / Figure 1
- 为什么必读：这里把 RAG 拆成 retriever、document index、generator，支撑后续概念卡的组件边界。
- 原文短摘：
  > We combine a pre-trained retriever (Query Encoder + Document Index) with a pre-trained seq2seq model (Generator)
- 中文概括：
  - Retriever 用 query encoder 和 document index 找 top-K 文档。
  - Generator 基于输入和检索文档生成输出；RAG-Sequence 与 RAG-Token 的差别在于文档如何参与生成。
- 我需要理解的机制：
  1. query encoder
  2. document index
  3. top-K retrieval
  4. generator conditioning
- 支撑概念：
  - [[Retriever]]
  - [[RAG]]
  - [[LLM]]
- 证据边界：
  - Figure 1 说明组件关系；不能证明检索到的文档一定正确，也不能保证最终回答有事实性。

### 选读

- 实验表格、ablation 或 benchmark 细节：用于确认效果边界，不作为第一轮理解入口。
- appendix / prompt 模板 / 训练细节：等核心机制理解后再补。

### 可以先跳过

- 与当前 Agent / LLM / RAG 学习目标无关的长表格、完整推导或重复实验设置。

### 读完要能回答

- [[Parametric Memory]] 和 [[Non-Parametric Memory]] 为什么不能混用？
- RAG 为什么能改善可更新性，却不能自动保证事实正确？

### 读完要更新

- [[RAG]]
- [[Parametric Memory]]
- [[Non-Parametric Memory]]
- [[Retriever]]
- [[LLM]]

## 一句话

RAG 把检索器和生成模型结合起来，让模型在回答时使用外部文档作为知识来源。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| RAG 组合参数化语言模型记忆和非参数化检索记忆。 | Page 1 / Abstract | high | [[RAG]] |
| RAG 使用 retriever/document index 找文档，再由 generator 生成答案。 | Page 2 / Figure 1 | high | [[Retriever]] |

边界：这张 source note 只记录论文证据与定位；稳定解释仍应写入 `wiki/concepts/`，并回链到本页小节或 PDF / section。

## 现代性 / 前沿性初判

- foundation：RAG 是外部知识增强的基础架构语言。
- 稳定部分：检索器、索引、生成器边界仍稳定。
- 已扩展部分：现代系统加入 chunking、reranking、query rewriting、citation、eval、agentic retrieval。
- freshness：stable。

## 已提取文件

- PDF：`assets/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`
- Extracted Markdown：`extracted/Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

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
