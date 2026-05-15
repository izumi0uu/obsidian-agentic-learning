---
type: source
source_type: paper
title: "Attention Is All You Need"
url: "https://arxiv.org/abs/1706.03762"
pdf: "assets/Attention Is All You Need.pdf"
extracted: "extracted/Attention Is All You Need.extracted.md"
author:
  - Vaswani et al.
site: arXiv
topic:
  - llm
  - transformer
created: 2026-05-05
updated: 2026-05-15
last_checked: 2026-05-11
freshness: stable
conflicts: []
status: growing
source: "https://arxiv.org/abs/1706.03762"
related:
  - "[[LLM]]"
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
  - "[[Positional Encoding]]"
---

# Attention Is All You Need

## 为什么收

这是 Transformer 架构的基础论文。学习 Agent 前不需要完全推导公式，但要知道现代 LLM 的底座来自 attention 和 Transformer。

## 先读什么

- Abstract
- Introduction
- Model Architecture

## 需要我读的内容

目标：理解 Transformer 为什么能作为现代 LLM 的架构地基，而不是把它误读成 Agent 论文。

### 必读

> 使用规则：必读部分要直接提取证据。短内容摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / Transformer 的核心主张

- 位置：Extracted Markdown `Attention Is All You Need.extracted.md` / Page 1 / Abstract
- 为什么必读：这里直接支撑 [[Transformer]] 的定义：用 attention 取代 recurrence/convolution，成为后续 LLM 架构的基础。
- 原文短摘：
  > We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.
- 中文概括：
  - 论文的关键不是“attention 很重要”这么泛泛一句，而是提出一种主要由 attention 机制组成的序列转导架构。
  - 它把 encoder-decoder 中原本依赖循环或卷积的部分替换为 attention，从而让训练并行化能力成为架构优势。
- 我需要理解的机制：
  1. attention-only 架构主张
  2. encoder-decoder stack 的整体结构
  3. 训练并行化和序列依赖建模之间的权衡
- 支撑概念：
  - [[Transformer]]
  - [[Self-Attention]]
  - [[LLM]]
- 证据边界：
  - 这段只证明 Transformer 论文的架构主张；不能推出所有现代 LLM 都只由原版 Transformer 细节构成，也不能把 attention 权重直接等同于可解释因果。

#### 必读块 2：Introduction / 顺序计算瓶颈

- 位置：Extracted Markdown `Attention Is All You Need.extracted.md` / Page 2 / Section 1 Introduction
- 为什么必读：这里解释为什么论文要摆脱 RNN 式顺序计算：不是为了“更像人思考”，而是为了训练效率和长距离依赖。
- 原文短摘：
  > The fundamental constraint of sequential computation, however, remains.
- 中文概括：
  - RNN 把位置与时间步绑定，训练样本内部难以完全并行。
  - Transformer 的 attention 让任意位置间的依赖更直接，降低了长距离依赖学习的路径长度问题。
- 我需要理解的机制：
  1. sequential computation bottleneck
  2. global dependency
  3. parallelization within training examples
- 支撑概念：
  - [[Transformer]]
  - [[Self-Attention]]
  - [[Positional Encoding]]
- 证据边界：
  - 这段解释的是模型训练和序列建模瓶颈；它不解释工具调用、状态管理、权限、任务规划这些 Agent runtime 问题。

### 选读

- 实验表格、ablation 或 benchmark 细节：用于确认效果边界，不作为第一轮理解入口。
- appendix / prompt 模板 / 训练细节：等核心机制理解后再补。

### 可以先跳过

- 与当前 Agent / LLM / RAG 学习目标无关的长表格、完整推导或重复实验设置。

### 读完要能回答

- 为什么 Transformer 的并行化优势主要发生在训练阶段？
- 为什么 [[Multi-Head Attention]] 不是“多个 Agent”？

### 读完要更新

- [[Transformer]]
- [[Self-Attention]]
- [[LLM]]
- [[Positional Encoding]]

## 一句话

Transformer 用 attention 机制替代传统循环结构，让模型可以更高效地处理序列中的依赖关系。


## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| Transformer 用 attention 机制替代 recurrent/convolutional 结构作为主要架构。 | Page 1 / Abstract | high | [[Transformer]] |
| 论文动机之一是减少顺序计算瓶颈、提高训练并行化。 | Page 2 / Section 1 Introduction | high | [[Self-Attention]] |

边界：这张 source note 只记录论文证据与定位；稳定解释仍应写入 `wiki/concepts/`，并回链到本页小节或 PDF / section。


## 现代性 / 前沿性初判

- foundation：这是现代 LLM 架构语言的地基。
- 稳定部分：attention、encoder/decoder stack、position information 仍是理解 LLM 的核心入口。
- 已变化部分：现代模型在归一化、位置编码、长上下文、解码策略、训练数据和后训练上已经远超原始论文。
- freshness：stable；除非更新长上下文或新架构对比，不需要频繁复查。

## 已提取文件

- PDF：`assets/Attention Is All You Need.pdf`
- Extracted Markdown：`extracted/Attention Is All You Need.extracted.md`
- 抽取质量提醒：PDF 已本地保存；extracted 由 PDF 自动抽取为纯文本，公式、表格、图、脚注和双栏阅读顺序可能有损失，精读引用仍需回到 PDF 页码 / section 校验。

## Ingest 摘要

这篇论文对当前 Agent 学习的价值不是教我“怎么做 Agent”，而是解释现代 [[LLM]] 的架构地基：[[Transformer]]。

核心主张：

- 传统序列模型依赖 recurrent 或 convolutional 结构。
- Transformer 去掉 recurrence 和 convolution，主要依赖 attention。
- [[Self-Attention]] 可以让序列中任意位置之间建立直接依赖。
- [[Multi-Head Attention]] 让模型从多个表示子空间关注不同位置的信息。
- 因为没有 recurrence 或 convolution，模型需要 [[Positional Encoding]] 注入位置信息。

## 可以拆成概念卡

- [[LLM]]
- [[Transformer]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Positional Encoding]]
- token
- context window

## 我的疑问

- attention 和上下文窗口之间是什么关系？
- 为什么 Transformer 适合扩展到大模型？
- attention 权重能不能直接解释成“模型为什么这样回答”？
- position encoding 和后来的长上下文技术是什么关系？

## 边界提醒

这篇论文解释模型架构基础，不解释 Agent、工具调用或 RAG。

它也不等于“LLM 全部原理”。现代 LLM 还涉及预训练、tokenization、scaling、instruction tuning、RLHF/RLAIF、tool use、推理时计算等大量后续发展。
