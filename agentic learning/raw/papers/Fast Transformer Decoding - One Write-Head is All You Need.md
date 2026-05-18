---
type: source
source_type: paper
title: Fast Transformer Decoding - One Write-Head is All You Need
url: https://arxiv.org/abs/1911.02150
pdf: assets/Fast Transformer Decoding - One Write-Head is All You Need.pdf
arxiv: https://arxiv.org/abs/1911.02150
doi:
author:
  - Noam Shazeer
site: arXiv
venue: arXiv preprint, 2019
topic:
  - llm
  - inference
  - attention
  - kv-cache
created: 2026-05-17
updated: 2026-05-17
last_checked: 2026-05-17
freshness: stable
conflicts: []
status: seed
source: https://arxiv.org/abs/1911.02150
related:
  - "[[KV Cache]]"
  - "[[Multi-Head Attention]]"
  - "[[LLM 上下文限制与突破条件]]"
---

# Fast Transformer Decoding - One Write-Head is All You Need

## 原文信息

- 论文标题：Fast Transformer Decoding: One Write-Head is All You Need
- 作者：Noam Shazeer
- 发表位置 / 年份：arXiv preprint, 2019
- URL：https://arxiv.org/abs/1911.02150
- PDF：https://arxiv.org/pdf/1911.02150
- 本地 PDF：`assets/Fast Transformer Decoding - One Write-Head is All You Need.pdf`
- extracted：未抽取

边界：这一页是 raw source note，只回答“论文原文说了什么、哪些概念可由它支持”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把个人推断写成论文结论。

## 为什么收

这篇论文是 Multi-Query Attention 的经典来源之一，直接解释为什么在增量解码时减少 K/V head 可以降低内存带宽和 KV cache 压力。它为 [[KV Cache]] 的“缓存不是免费，K/V 份数决定推理资源”提供论文证据。

## 一句话

论文提出在多头注意力中让所有 query head 共享一组 key/value head，用更少的 K/V 读写换取更快的自回归解码。

## 先读什么

- Abstract：先看为什么 decoder inference 会受 memory bandwidth 约束。
- Method：看 one write-head / multi-query attention 如何共享 K/V。
- Experiments：看速度收益和质量代价。

## 需要我读的内容

### 必读

> 使用规则：必读部分要直接提取证据。短内容可以摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / decoding bottleneck

- 位置：arXiv abstract / 1911.02150
- 为什么必读：这里支撑 MQA 的原始动机：incremental decoding 的瓶颈不只是算力，也包括内存带宽。
- 原文短摘：
  > incremental decoding is memory-bandwidth-bound
- 中文概括：
  - 自回归解码每步都要读取历史 K/V，长上下文和大 batch 会放大内存读写压力。
  - 论文的目标不是改变语言模型任务，而是减少 decoder inference 中需要读写的 attention K/V 状态。
- 我需要理解的机制：
  1. incremental decoding
  2. memory bandwidth bottleneck
  3. key/value sharing
- 支撑概念：
  - [[KV Cache]]
  - [[Multi-Head Attention]]
- 证据边界：
  - 这段支持 MQA 的推理效率动机；不能外推出所有模型都应无条件使用单组 K/V。

#### 必读块 2：Multi-query attention / shared key-value heads

- 位置：arXiv paper / method sections
- 为什么必读：这里支撑“减少 K/V head 数量会直接减少 KV cache 体积和读取量”的机制。
- 原文短摘：
  > keys and values are shared
- 中文概括：
  - 普通 MHA 每个 head 有独立 K/V；MQA 让多个 query head 共享同一组 K/V。
  - 这种结构会减少需要缓存和读取的 K/V 张量，但可能带来质量损失或表达能力下降。
- 我需要理解的机制：
  1. shared K/V
  2. query heads vs key/value heads
  3. speed-quality tradeoff
- 支撑概念：
  - [[KV Cache]]
  - [[Multi-Head Attention]]
- 证据边界：
  - 这支持 MQA 是结构层优化；它不是 PagedAttention 那样的 cache allocator，也不是 FlashAttention 那样的 kernel / IO 实现优化。

### 选读

- 训练设置和模型规模：用于判断结论外推边界。
- 实验表格：用于比较速度收益和质量损失。

### 可以先跳过

- 和当前 KV Cache 学习无关的任务细节。

### 读完要能回答

- 为什么 KV Cache 压力和 K/V head 数相关？
- MQA 为什么能省显存 / 带宽？
- MQA 和 GQA 的取舍是什么？

### 读完要更新

- [[KV Cache]]
- [[Multi-Head Attention]]
- [[LLM 上下文限制与突破条件]]

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| Incremental decoding can be memory-bandwidth-bound, so减少 K/V 读写是推理优化核心。 | arXiv abstract | high | [[KV Cache]] |
| Multi-query attention 让多个 query head 共享 K/V，从结构上减少解码时缓存和读取的 K/V。 | method sections | high | [[KV Cache]] |

边界：没有精读到页码时，先写 source note 小节，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：让多个 query attention heads 共享较少的 key/value heads。
- 输入 / 输出：输入仍是 Transformer attention 计算；输出仍是 attention 层表示。
- 关键步骤：保留多 query head 表达能力，同时减少 K/V 投影、缓存和读取份数。
- 和相邻方法的差别：GQA 是 MHA 与 MQA 的折中；PagedAttention 管理 KV cache 内存块；FlashAttention 优化 attention kernel 的 IO。

## 实验 / 证据

- 数据集 / benchmark：待精读。
- 指标：速度、质量指标与模型任务表现待精读。
- 关键结果：待精读表格后补。
- 作者给出的局限：待精读。

## 现代性 / 前沿性初判

- current-practice / foundation：MQA 是理解 GQA、MLA 和现代推理显存优化的基础路线。
- 今天仍然稳定的部分：共享 K/V 可以降低 KV cache 压力。
- 已被现代系统吸收或替代的部分：许多现代模型更常用 GQA 或其他折中方案，而不是纯 MQA。
- 需要 freshness 复查的部分：新模型是否采用 MQA/GQA/MLA 取决于具体架构。

## 已提取文件

- PDF：`assets/Fast Transformer Decoding - One Write-Head is All You Need.pdf`
- Extracted Markdown：未抽取
- 抽取质量提醒：后续精读应回到 arXiv PDF。

## Ingest 摘要

- 已沉淀到 wiki 的概念：[[KV Cache]]
- 已更新的 topic / map：[[资料收集索引]], [[LLM 主题]], [[Agent 知识地图]], [[04 页面目录]]。
- 还没处理的证据：实验表格、速度 / 质量 tradeoff 细节。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[KV Cache]] | 论文解释 K/V 读写和 cache 压力为什么是推理瓶颈。 | Abstract / method | P1 |
| Multi-Query Attention | 若后续系统学习 MQA/GQA/MLA 结构优化，可单独建卡；本轮先作为 [[KV Cache]] 边界证据。 | method | P2 |

## 我的疑问

- 纯 MQA 在哪些任务上质量损失最大？
- GQA 的最佳 group 数如何随模型规模变化？

## 边界提醒

- MQA 是 attention 结构层优化，不是 serving 内存分页。
- MQA 的目标是减少 K/V 读写，不等于无损提升所有模型。
- 本页是 paper source note，稳定解释回到 [[KV Cache]]。
