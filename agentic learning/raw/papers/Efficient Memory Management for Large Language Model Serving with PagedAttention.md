---
type: source
source_type: paper
title: Efficient Memory Management for Large Language Model Serving with PagedAttention
url: https://arxiv.org/abs/2309.06180
pdf: assets/Efficient Memory Management for Large Language Model Serving with PagedAttention.pdf
arxiv: https://arxiv.org/abs/2309.06180
doi:
author:
  - Woosuk Kwon
  - Zhuohan Li
  - Siyuan Zhuang
  - Ying Sheng
  - Lianmin Zheng
  - Cody Hao Yu
  - Joseph E. Gonzalez
  - Hao Zhang
  - Ion Stoica
site: arXiv
venue: SOSP 2023 / arXiv, 2023
topic:
  - llm
  - inference
  - serving
  - kv-cache
created: 2026-05-17
updated: 2026-05-17
last_checked: 2026-05-17
freshness: stable
conflicts: []
status: seed
source: https://arxiv.org/abs/2309.06180
related:
  - "[[KV Cache]]"
  - "[[LLM 上下文限制与突破条件]]"
---

# Efficient Memory Management for Large Language Model Serving with PagedAttention

## 原文信息

- 论文标题：Efficient Memory Management for Large Language Model Serving with PagedAttention
- 作者：Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, Ion Stoica
- 发表位置 / 年份：SOSP 2023 / arXiv, 2023
- URL：https://arxiv.org/abs/2309.06180
- PDF：https://arxiv.org/pdf/2309.06180
- 本地 PDF：`assets/Efficient Memory Management for Large Language Model Serving with PagedAttention.pdf`
- extracted：未抽取

边界：这一页是 raw source note，只回答“论文原文说了什么、哪些概念可由它支持”。不要在这里替代 `wiki/concepts/` 的稳定理解，也不要把个人推断写成论文结论。

## 为什么收

这是 vLLM / PagedAttention 的核心论文，直接把 [[KV Cache]] 从“模型内部缓存”推进到“serving 系统里最重要的内存管理对象”。它适合作为理解长上下文、并发、显存碎片和 prompt prefix sharing 的系统证据。

## 一句话

PagedAttention 把 KV cache 切成块并通过类似虚拟内存的映射管理，让 LLM serving 在多请求、变长序列和并发场景下更高效使用 GPU 显存。

## 先读什么

- Abstract：看论文把 LLM serving 的主要内存问题定位到 KV cache。
- PagedAttention method：看 block / page table 式管理。
- vLLM serving results：看吞吐和内存利用的系统收益。

## 需要我读的内容

### 必读

> 使用规则：必读部分要直接提取证据。短内容可以摘 1-3 句原文并概括；长内容只摘最关键原话，其余用中文概括。原文证据和自己的概括必须分开标注。

#### 必读块 1：Abstract / KV cache as serving bottleneck

- 位置：arXiv abstract / 2309.06180
- 为什么必读：这里支撑 KV cache 是 LLM serving 内存管理的核心对象，而不是一个无关实现细节。
- 原文短摘：
  > near-zero waste in KV cache memory
- 中文概括：
  - LLM 服务端会同时处理大量变长请求，每个请求都需要维护自己的 KV cache。
  - KV cache 的显存占用、碎片和预留浪费会限制并发吞吐。
- 我需要理解的机制：
  1. KV cache memory
  2. variable-length requests
  3. serving throughput
- 支撑概念：
  - [[KV Cache]]
  - [[LLM 上下文限制与突破条件]]
- 证据边界：
  - 这段支持 serving 侧内存管理问题；不说明 attention 数学公式发生变化。

#### 必读块 2：PagedAttention / block-based cache management

- 位置：paper method / PagedAttention
- 为什么必读：这里支撑 PagedAttention 是 KV cache 管理策略，而不是新的模型记忆或 RAG。
- 原文短摘：
  > inspired by the classical virtual memory and paging techniques
- 中文概括：
  - PagedAttention 将每个请求的 KV cache 分成固定大小 block。
  - 逻辑 token block 可以映射到非连续物理显存 block，从而减少连续分配、预留和碎片浪费。
- 我需要理解的机制：
  1. block allocation
  2. logical-to-physical mapping
  3. prefix / cache sharing
- 支撑概念：
  - [[KV Cache]]
- 证据边界：
  - PagedAttention 管理 KV cache 存储布局；它不改变 token 是否进入 context window，也不替代 RAG 证据选择。

### 选读

- vLLM scheduler 与 continuous batching。
- Prefix sharing / copy-on-write 相关实验。

### 可以先跳过

- 具体系统实现参数，除非正在做推理框架选型。

### 读完要能回答

- 为什么 KV cache 会导致 serving 显存碎片？
- PagedAttention 为什么像操作系统虚拟内存？
- PagedAttention 与 KV Cache 是什么关系？

### 读完要更新

- [[KV Cache]]
- [[LLM 上下文限制与突破条件]]

## 论文主张

| Claim | Evidence anchor | Confidence | Target concept |
|---|---|---|---|
| LLM serving 的关键资源问题之一是 KV cache memory management。 | arXiv abstract | high | [[KV Cache]] |
| PagedAttention 通过 block/page 式管理 KV cache，减少碎片并提升并发吞吐。 | method / PagedAttention | high | [[KV Cache]] |

边界：没有精读到页码时，先写 source note 小节，不伪造页码或段落级证据。

## 方法 / 机制

- 核心方法：把 KV cache 拆成固定大小 block，用映射表管理逻辑块到物理块。
- 输入 / 输出：输入是多请求 LLM serving 的 KV cache 分配需求；输出是更高显存利用和吞吐。
- 关键步骤：block allocation、logical block table、prefix sharing、copy-on-write。
- 和相邻方法的差别：GQA/MQA 减少 K/V 份数；PagedAttention 管理已经存在的 KV cache block；FlashAttention 优化 attention 计算 IO。

## 实验 / 证据

- 数据集 / benchmark：待精读。
- 指标：吞吐、显存利用、请求延迟。
- 关键结果：待精读表格后补。
- 作者给出的局限：待精读。

## 现代性 / 前沿性初判

- current-practice：vLLM / PagedAttention 是现代 LLM serving 的关键工程实践之一。
- 今天仍然稳定的部分：KV cache 的块管理和碎片控制是长上下文服务端瓶颈。
- 已被现代系统吸收或替代的部分：不同 serving 框架会有各自 scheduler、prefix cache、offload 和 cache allocator 变体。
- 需要 freshness 复查的部分：vLLM、SGLang、TGI、TensorRT-LLM 的具体 KV cache 策略快速更新。

## 已提取文件

- PDF：`assets/Efficient Memory Management for Large Language Model Serving with PagedAttention.pdf`
- Extracted Markdown：未抽取
- 抽取质量提醒：后续精读应回到 arXiv PDF。

## Ingest 摘要

- 已沉淀到 wiki 的概念：[[KV Cache]]
- 已更新的 topic / map：[[资料收集索引]], [[LLM 主题]], [[Agent 知识地图]], [[04 页面目录]]。
- 还没处理的证据：vLLM 实验、prefix sharing 和 scheduler 细节。

## 可以拆成概念卡

| Concept | Why it deserves a card | Source anchor | Priority |
|---|---|---|---|
| [[KV Cache]] | 论文把 KV cache 作为 serving 内存管理核心对象。 | Abstract / method | P1 |
| PagedAttention | 后续若学习推理 serving 系统，可单独建卡；本轮先作为 [[KV Cache]] 管理方式证据。 | method | P2 |

## 我的疑问

- PagedAttention 和 prefix caching 在 vLLM 当前版本中如何协同？
- CPU offload、KV cache quantization 和 PagedAttention 的组合代价是什么？

## 边界提醒

- PagedAttention 是 serving 内存管理，不是模型长期记忆。
- PagedAttention 不替代 [[Context Engineering]]；它只管理已经进入上下文后的 cache 状态。
- 本页是 paper source note，稳定解释回到 [[KV Cache]]。
