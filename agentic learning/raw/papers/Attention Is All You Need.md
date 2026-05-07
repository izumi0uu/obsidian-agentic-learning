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
updated: 2026-05-07
last_checked: 2026-05-07
freshness: stable
conflicts: []
status: growing
source:
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

目标：只建立 [[Transformer]] 作为 [[LLM]] 架构地基的理解，不做深度数学推导。

### 必读

- Abstract：抓住“去掉 recurrence 和 convolution，只靠 attention”的主张。
- 1 Introduction：理解为什么 RNN 的顺序计算限制并行训练。
- 3 Model Architecture：只看 encoder-decoder、encoder stack、decoder stack 的整体结构。
- 3.2 Attention：理解 query、key、value 和 weighted sum。
- 3.2.2 Multi-Head Attention：理解为什么需要多个 head。
- 3.5 Positional Encoding：理解为什么没有 recurrence/convolution 后必须注入位置。
- 4 Why Self-Attention：理解 self-attention 相比 recurrent/convolutional layer 的三个比较维度。

### 选读

- Table 1：只看三列含义：复杂度、顺序操作数、最大路径长度。
- Figure 1：只看 Transformer 由 encoder/decoder stack 组成。
- Figure 2：只看 Scaled Dot-Product Attention 和 Multi-Head Attention 的关系。

### 可以先跳过

- 训练细节、BLEU 结果、参数表。
- 公式推导细节。
- Appendix 的 attention visualization。

### 读完要能回答

- [[Transformer]] 为什么能比 RNN 更适合并行训练？
- [[Self-Attention]] 解决的是哪类序列依赖问题？
- [[Multi-Head Attention]] 为什么不是多个 Agent？
- [[Positional Encoding]] 为什么不是长期记忆？
- 这篇论文为什么不直接教我做 [[Agent]]？

### 读完要更新

- [[LLM]]
- [[Transformer]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Positional Encoding]]

## 一句话

Transformer 用 attention 机制替代传统循环结构，让模型可以更高效地处理序列中的依赖关系。

## 已提取文件

- PDF：`assets/Attention Is All You Need.pdf`
- 抽取正文：`extracted/Attention Is All You Need.extracted.md`

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
