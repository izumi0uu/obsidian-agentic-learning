---
type: source
source_type: paper
title: GQA - Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints
url: https://arxiv.org/abs/2305.13245
pdf: assets/GQA - Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.pdf
arxiv: https://arxiv.org/abs/2305.13245
doi:
author:
  - Joshua Ainslie
  - James Lee-Thorp
  - Michiel de Jong
  - Yury Zemlyanskiy
  - Federico Lebron
  - Sumit Sanghai
site: arXiv
venue: arXiv preprint, 2023
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
source: https://arxiv.org/abs/2305.13245
related:
  - "[[KV Cache]]"
  - "[[Multi-Head Attention]]"
  - "[[LLM 上下文限制与突破条件]]"
---

# GQA - Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints

## 原文信息

- 论文标题：GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints
- 作者：Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebron, Sumit Sanghai
- 发表位置 / 年份：arXiv preprint, 2023
- URL：https://arxiv.org/abs/2305.13245
- PDF：https://arxiv.org/pdf/2305.13245
- 本地 PDF：`assets/GQA - Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.pdf`
- extracted：未抽取

边界：这一页是 raw source note，只回答“论文原文说了什么、哪些概念可由它支持”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把个人推断写成论文结论。

## 为什么收

这篇论文给出 Grouped-Query Attention 的来源证据。它连接 MHA 和 MQA：不是让所有 head 共享一组 K/V，而是让一组 query heads 共享一组 K/V，从而在 KV cache 节省和模型质量之间做折中。

## 一句话

GQA 把 Multi-Head Attention 和 Multi-Query Attention 连成连续光谱：用更少的 K/V 组降低推理 cache 成本，同时尽量保留多头表示质量。

## 先读什么

- Abstract：理解为什么 GQA 是 MHA 与 MQA 的折中。
- Method：看 multi-head checkpoint 如何被转成 grouped-query 模型。
- Experiments：看质量、速度和 K/V head 数之间的关系。

## 需要我读的内容

### 必读

> 使用规则：必读部分要直接提取证据。短内容可以摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / GQA motivation

- 位置：arXiv abstract / 2305.13245
- 为什么必读：这里支撑 GQA 的核心定位：在 MHA 质量和 MQA 速度之间折中。
- 原文短摘：
  > uses an intermediate number of key-value heads
- 中文概括：
  - GQA 不是完全共享 K/V，也不是保留每个 head 独立 K/V。
  - 它通过 K/V group 数控制 KV cache 规模和质量之间的权衡。
- 我需要理解的机制：
  1. grouped key/value heads
  2. speed-quality tradeoff
  3. checkpoint conversion
- 支撑概念：
  - [[KV Cache]]
  - [[Multi-Head Attention]]
- 证据边界：
  - 这段支持 GQA 是结构层折中；不说明 serving 层如何做分页、调度或 cache eviction。

#### 必读块 2：MHA-MQA-GQA spectrum

- 位置：paper method / model variants
- 为什么必读：这里支撑“GQA 通过减少 K/V 组数降低 KV cache 压力”的机制边界。
- 原文短摘：
  > multi-query attention uses a single key-value head
- 中文概括：
  - MHA 有多组 K/V，MQA 只有一组 K/V，GQA 在两者之间使用若干组 K/V。
  - 对 [[KV Cache]] 来说，K/V 组数越少，同样上下文和 batch 下需要常驻的 K/V 张量越少。
- 我需要理解的机制：
  1. K/V group count
  2. checkpoint uptraining
  3. cache memory reduction
- 支撑概念：
  - [[KV Cache]]
  - [[Multi-Head Attention]]
- 证据边界：
  - 这支持 GQA 降低 K/V cache 压力；具体模型采用多少组 K/V 是架构选择，不是固定常数。

### 选读

- 各配置实验结果。
- uptraining 数据和成本。

### 可以先跳过

- 与当前 KV Cache 学习无关的训练超参。

### 读完要能回答

- GQA 和 MQA 的最小区别是什么？
- 为什么 GQA 常被现代模型作为默认折中？
- GQA 省的是哪一部分 KV Cache？

### 读完要更新

- [[KV Cache]]
- [[Multi-Head Attention]]
- [[LLM 上下文限制与突破条件]]

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| GQA 在 MHA 与 MQA 之间引入 K/V 分组折中。 | arXiv abstract / method | high | [[KV Cache]] |
| 减少 K/V group 数可以减少推理时需要缓存和读取的 K/V。 | method / model variants | high | [[KV Cache]] |

边界：没有精读到页码时，先写 source note 小节，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：把 query heads 分组，每组共享一套 K/V heads。
- 输入 / 输出：从多头 attention checkpoint 出发，训练成 grouped-query 模型。
- 关键步骤：减少 K/V heads，保留多个 query heads。
- 和相邻方法的差别：MQA 是极端共享；GQA 是折中；PagedAttention 是 KV cache allocator；FlashAttention 是 attention kernel 优化。

## 实验 / 证据

- 数据集 / benchmark：待精读。
- 指标：质量、速度、K/V head 数和训练成本。
- 关键结果：待精读表格后补。
- 作者给出的局限：待精读。

## 现代性 / 前沿性初判

- current-practice：GQA 是现代 LLM 架构中常见的推理效率折中。
- 今天仍然稳定的部分：K/V group 数影响 KV cache 的内存占用。
- 已被现代系统吸收或替代的部分：部分模型进一步采用 MLA 或其他 latent KV 压缩路线。
- 需要 freshness 复查的部分：具体模型家族使用 GQA、MQA 或 MLA 会随版本变化。

## 已提取文件

- PDF：`assets/GQA - Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.pdf`
- Extracted Markdown：未抽取
- 抽取质量提醒：后续精读应回到 arXiv PDF。

## Ingest 摘要

- 已沉淀到 wiki 的概念：[[KV Cache]]
- 已更新的 topic / map：[[资料收集索引]], [[LLM 主题]], [[Agent 知识地图]], [[04 页面目录]]。
- 还没处理的证据：GQA 实验表格、checkpoint conversion 细节。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[KV Cache]] | GQA 解释 K/V head 数如何影响 cache 体积。 | Abstract / method | P1 |
| Grouped-Query Attention | 后续若系统学习模型结构优化，可单独建卡；本轮先作为 [[KV Cache]] 边界证据。 | method | P2 |

## 我的疑问

- GQA group 数如何与模型规模、任务类型和上下文长度共同选择？
- GQA 和 MLA 的工程取舍如何比较？

## 边界提醒

- GQA 是 attention 结构层优化，不是 prompt caching。
- GQA 减少 K/V 组数，但不消除 KV Cache。
- 本页是 paper source note，稳定解释回到 [[KV Cache]]。
