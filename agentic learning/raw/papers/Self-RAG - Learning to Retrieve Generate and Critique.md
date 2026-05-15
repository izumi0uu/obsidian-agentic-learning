---
type: source
source_type: paper
title: "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection"
url: "https://arxiv.org/abs/2310.11511"
pdf: "assets/Self-RAG - Learning to Retrieve Generate and Critique.pdf"
extracted: "extracted/Self-RAG - Learning to Retrieve Generate and Critique.extracted.md"
author: Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, Hannaneh Hajishirzi
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
source: "https://arxiv.org/abs/2310.11511"
related:
  - "[[Self-RAG]]"
  - "[[RAG]]"
  - "[[Agentic Retrieval]]"
---

# Self-RAG - Learning to Retrieve Generate and Critique

## 为什么收

Self-RAG 是“模型自己判断是否检索、如何使用证据、如何批判生成内容”的经典 RAG 进化论文，虽然不是 2026 新论文，但仍是理解 agentic retrieval 和 self-reflective RAG 的基础概念。

## 一句话

Self-RAG 训练模型通过 reflection tokens 自适应地检索、生成和批判证据使用。

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| Self-RAG 学习按需检索，而不是固定检索。 | arXiv abstract | high | [[Self-RAG]] |
| Self-RAG 使用 reflection tokens 控制检索、生成和批判。 | arXiv abstract | high | [[Evaluation]] |

边界：这张 source note 只记录论文证据与定位；稳定解释仍应写入 `wiki/concepts/`，并回链到本页小节或 PDF / section。

## 现代性 / 前沿性初判

- foundation / current-practice：Self-RAG 是 agentic retrieval 和 self-reflective RAG 的重要基础。
- 稳定部分：检索应被评估、控制和批判。
- 工程吸收：现代 RAG 常用 router、evaluator、reranker 和 graph workflow 近似实现。
- freshness：stable。

## 先读什么

- Abstract：为什么固定 top-k 检索不够。
- Method：retrieval token 和 critique token。
- Experiments：事实性、引用准确性和开放域 QA。

## 需要我读的内容

目标：理解 Self-RAG 把检索、生成和批判做成训练出的控制能力，而不只是 prompt 里的自我反思。

### 必读

> 使用规则：必读部分要直接提取证据。短内容摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / adaptive retrieval

- 位置：arXiv abstract / 2310.11511 / last checked 2026-05-11
- 为什么必读：这里支撑 Self-RAG 与固定 top-k RAG 的边界：检索是否发生由模型自适应控制。
- 原文短摘：
  > adaptively retrieves passages on-demand
- 中文概括：
  - Self-RAG 不把每个输入都固定塞入同样数量文档。
  - 模型学习判断何时需要检索，以及检索结果是否支持生成。
- 我需要理解的机制：
  1. adaptive retrieval
  2. retrieve-on-demand
  3. evidence-conditioned generation
- 支撑概念：
  - [[Self-RAG]]
  - [[Agentic Retrieval]]
  - [[RAG]]
- 证据边界：
  - 这段不等于所有工程 RAG 都需要训练新 token；闭源 API 场景常用 workflow 近似。

#### 必读块 2：Abstract / reflection tokens

- 位置：arXiv abstract / 2310.11511 / last checked 2026-05-11
- 为什么必读：这里说明 Self-RAG 的“self-reflection”是训练出的特殊控制信号。
- 原文短摘：
  > special tokens, called reflection tokens
- 中文概括：
  - Reflection tokens 让模型显式控制检索、证据支持度和生成质量判断。
  - 这些 token 是训练和推理机制的一部分，不是简单让模型回答后“检查一下”。
- 我需要理解的机制：
  1. reflection token
  2. critique signal
  3. generation control
- 支撑概念：
  - [[Self-RAG]]
  - [[Evaluation]]
- 证据边界：
  - reflection tokens 是论文方法的具体实现；现代工程系统可能用 judge、router、graph node 或 eval step 实现相似功能。

### 选读

- 实验表格、ablation 或 benchmark 细节：用于确认效果边界，不作为第一轮理解入口。
- appendix / prompt 模板 / 训练细节：等核心机制理解后再补。

### 可以先跳过

- 与当前 Agent / LLM / RAG 学习目标无关的长表格、完整推导或重复实验设置。

### 读完要能回答

- Self-RAG 的 reflection tokens 和 LangGraph 里的 evaluator node 有什么共同点和差别？
- 按需检索可能漏掉哪些必须检索的事实？

### 读完要更新

- [[Self-RAG]]
- [[Agentic Retrieval]]
- [[RAG]]
- [[Evaluation]]

## 已提取文件

- PDF：`assets/Self-RAG - Learning to Retrieve Generate and Critique.pdf`
- Extracted Markdown：`extracted/Self-RAG - Learning to Retrieve Generate and Critique.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## 可以拆成概念卡

- [[Self-RAG]]
- [[Agentic Retrieval]]

## 我的疑问

- Self-RAG 的训练式方法和工程上的 LangGraph self-reflective RAG 有什么区别？
- reflection tokens 在闭源模型 API 场景里如何近似实现？

## 边界提醒

Self-RAG 不是简单“让模型反思一下”。它的核心是训练和控制信号，而不是在 prompt 里加一句自我检查。
