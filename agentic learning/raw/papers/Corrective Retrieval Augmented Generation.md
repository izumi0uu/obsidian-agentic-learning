---
type: source
source_type: paper
title: "Corrective Retrieval Augmented Generation"
url: "https://arxiv.org/abs/2401.15884"
pdf: "assets/Corrective Retrieval Augmented Generation.pdf"
extracted: "extracted/Corrective Retrieval Augmented Generation.extracted.md"
author: Shi-Qi Yan, Jia-Chen Gu, Yun Zhu, Zhen-Hua Ling
site: arxiv.org
topic:
  - rag
  - evaluation
  - frontier
created: 2026-05-06
updated: 2026-05-15
last_checked: 2026-05-11
freshness: stable
conflicts: []
status: seed
source: "https://arxiv.org/abs/2401.15884"
related:
  - "[[Corrective RAG]]"
  - "[[RAG]]"
  - "[[Retriever]]"
---

# Corrective Retrieval Augmented Generation

## 为什么收

CRAG 是“检索结果不可靠时怎么办”的代表方法。它把 retrieval evaluator、重检索、web search fallback 和 decompose/recompose 连接起来，适合理解 RAG 可靠性。

## 一句话

Corrective RAG 先评估检索质量，再决定直接生成、修正检索或扩展检索。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| CRAG 引入轻量 retrieval evaluator 来判断检索文档质量。 | arXiv abstract | high | [[Corrective RAG]] |
| CRAG 在低质量检索时可使用 web search 扩展知识来源。 | arXiv abstract | high | [[Agentic Retrieval]] |

边界：这张 source note 只记录论文证据与定位；稳定解释仍应写入 `wiki/concepts/`，并回链到本页小节或 PDF / section。

## 现代性 / 前沿性初判

- current-practice：检索质量评估和分支式纠错已经进入现代 RAG workflow。
- 稳定部分：检索质量不可靠时需要 evaluator 或 guardrail。
- 易变部分：具体 evaluator、web fallback 和重排策略依产品/场景变化。
- freshness：stable for paper；若追具体框架实现可设 watch。

## 先读什么

- Abstract：RAG 对检索质量的依赖。
- Retrieval evaluator：如何判断文档质量。
- Corrective actions：低置信度时如何触发补救。

## 需要我读的内容

目标：理解 CRAG 如何在检索质量不足时触发纠错分支，而不是把 RAG 失败全推给生成模型。

### 必读

> 使用规则：必读部分要直接提取证据。短内容摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / 检索评估器

- 位置：arXiv abstract / 2401.15884 / last checked 2026-05-11
- 为什么必读：这里是 CRAG 的核心：先评估检索结果质量，再决定是否纠错。
- 原文短摘：
  > a lightweight retrieval evaluator is designed to assess the overall quality of retrieved documents for a query
- 中文概括：
  - CRAG 不默认检索结果总是可靠，而是显式给检索质量打分或分类。
  - 这个 evaluator 决定后续是直接生成、使用修正知识，还是启动更大范围检索。
- 我需要理解的机制：
  1. retrieval evaluator
  2. confidence-aware routing
  3. retrieval quality assessment
- 支撑概念：
  - [[Corrective RAG]]
  - [[Retriever]]
  - [[Evaluation]]
- 证据边界：
  - 这段证明 CRAG 的入口是检索质量评估；不能外推为所有 RAG 都必须使用同一种 evaluator。

#### 必读块 2：Abstract / web search fallback 与知识修正

- 位置：arXiv abstract / 2401.15884 / last checked 2026-05-11
- 为什么必读：这里说明 CRAG 的纠错动作不是简单重试，而是引入外部检索和知识重组。
- 原文短摘：
  > large-scale web searches are utilized as an extension for augmenting the retrieval results
- 中文概括：
  - 当本地检索不足时，CRAG 可以把 web search 当作补充知识源。
  - 它还会对检索文档做分解、过滤和重组，避免把整段噪声直接塞给生成模型。
- 我需要理解的机制：
  1. web fallback
  2. decompose-then-recompose
  3. noise filtering
- 支撑概念：
  - [[Corrective RAG]]
  - [[Agentic Retrieval]]
  - [[RAG]]
- 证据边界：
  - web fallback 在企业私有知识库或安全场景可能不可用；这段不是对开放互联网检索的安全背书。

### 选读

- 实验表格、ablation 或 benchmark 细节：用于确认效果边界，不作为第一轮理解入口。
- appendix / prompt 模板 / 训练细节：等核心机制理解后再补。

### 可以先跳过

- 与当前 Agent / LLM / RAG 学习目标无关的长表格、完整推导或重复实验设置。

### 读完要能回答

- CRAG 的 evaluator 应该评估文档相关性、事实覆盖，还是答案可支持性？
- 企业 RAG 场景里 web fallback 何时是风险而不是增强？

### 读完要更新

- [[Corrective RAG]]
- [[Retriever]]
- [[Evaluation]]
- [[Agentic Retrieval]]
- [[RAG]]

## 已提取文件

- PDF：`assets/Corrective Retrieval Augmented Generation.pdf`
- Extracted Markdown：`extracted/Corrective Retrieval Augmented Generation.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## 可以拆成概念卡

- [[Corrective RAG]]
- [[Retriever]]
- [[Evaluation]]

## 我的疑问

- retrieval evaluator 应该是小模型、规则、还是 LLM-as-judge？
- web fallback 在企业私有知识库场景是否安全？

## 边界提醒

Corrective RAG 不是“多检索几次”。它的核心是检索质量评估和基于置信度的分支动作。
