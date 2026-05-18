---
type: concept
topic:
  - llm
  - inference
  - context
status: growing
created: 2026-05-17
updated: 2026-05-17
last_checked: 2026-05-17
freshness: watch
source:
  - "[[128 ai llm 14. KV Cache 是什么？Prompt Caching 的原理是什么？]]"
  - "[[Fast Transformer Decoding - One Write-Head is All You Need]]"
  - "[[GQA - Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints]]"
  - "[[Efficient Memory Management for Large Language Model Serving with PagedAttention]]"
  - "[[FlashAttention - Fast and Memory-Efficient Exact Attention with IO-Awareness]]"
evidence:
  - "[[128 ai llm 14. KV Cache 是什么？Prompt Caching 的原理是什么？#KV Cache：单次推理内的优化]]"
  - "[[128 ai llm 14. KV Cache 是什么？Prompt Caching 的原理是什么？#KV Cache 的显存代价]]"
  - "[[Fast Transformer Decoding - One Write-Head is All You Need#论文主张]]"
  - "[[GQA - Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints#论文主张]]"
  - "[[Efficient Memory Management for Large Language Model Serving with PagedAttention#论文主张]]"
  - "[[FlashAttention - Fast and Memory-Efficient Exact Attention with IO-Awareness#论文主张]]"
aliases:
  - Key-Value Cache
  - Key Value Cache
  - K/V Cache
  - K/V cache
  - KV cache
  - KV 缓存
  - 键值缓存
related:
  - "[[LLM]]"
  - "[[Transformer]]"
  - "[[Self-Attention]]"
  - "[[Multi-Head Attention]]"
  - "[[Context Window]]"
  - "[[LLM 上下文限制与突破条件]]"
---

# KV Cache

## 深度级别

- 级别：qualified
- 为什么是这个级别：KV Cache 是现代自回归 LLM 推理的基础机制，同时牵动长上下文、显存、吞吐、batching、prompt caching 和服务端调度。
- 本次缺口：没有直接本地抽取 PDF 页码；论文证据先使用 paper source note 的 abstract / method 级锚点，后续精读可补 PDF page / section。

## 一句话

KV Cache 是自回归 LLM 推理时把历史 token 在每一层算出的 Key / Value 表示缓存起来，让新 token 只计算自己的投影并复用历史 K/V 的推理优化机制。

## 概念详解

LLM 逐 token 生成文本。生成第 `t` 个 token 时，模型需要让这个新位置关注前面已经出现的 token；如果每一步都重新计算整段前缀的 K/V，前面 token 的表示会被一遍遍重复算，长序列推理会变得不可用。KV Cache 的核心动作就是：在每一层 attention 中，把已经生成或已处理 token 的 Key / Value 张量保存下来。下一步生成时，新 token 只需要计算自己的 Q/K/V，然后用自己的 Q 去和缓存里的历史 K/V 做 attention。

这个机制把“重复计算历史前缀”的问题换成“常驻保存历史 K/V”的问题。它让自回归解码速度可接受，但显存占用会随 batch、序列长度、层数、K/V head 数、head 维度和 dtype 线性增长。也就是说，KV Cache 不是免费加速；它把瓶颈从纯计算转移到 GPU 显存容量和内存带宽上。长上下文和高并发部署里，KV Cache 往往比模型权重之外的其他临时张量更容易成为吞吐瓶颈。

相关论文各自从不同角度吸收这个问题。Multi-Query Attention 把多个 query head 共享同一组 K/V，直接减少要缓存的 K/V 份数；Grouped-Query Attention 在 MHA 和 MQA 之间折中，用少量 K/V 组保留较多质量；PagedAttention 把 KV cache 切成块并用类似虚拟内存的方式管理，减少碎片和浪费；FlashAttention 不是 KV Cache 本身，而是 attention 计算的 IO-aware 实现优化，常和 KV Cache / GQA / batching 一起进入推理栈。

关于“KV Cache 为什么通常不放 CPU”，关键边界是：KV Cache 处在每个 token 解码的热路径上。新 token 的 attention 需要马上读取历史 K/V，如果频繁从 CPU 内存通过 PCIe / NVLink 拉回 GPU，会把延迟和带宽瓶颈放大。CPU offload 可以作为显存不够时的降级或分层存储方案，但主流高吞吐推理会优先把热 KV 留在 GPU 显存，并通过分页、量化、GQA/MQA、调度和 cache eviction 控制成本。

## 它解决什么问题

没有 KV Cache，自回归生成每一步都会重复计算已经处理过的前缀。序列越长，重复计算越夸张，生成延迟会快速放大。

KV Cache 解决的是推理时“历史上下文已经算过，下一步能不能复用”的问题。它让 decoder-only LLM 可以逐 token 连续生成，并让 prompt prefix、system prompt、few-shot 示例和历史上下文在一次请求内被复用。

## 它不是什么

KV Cache 不是 [[Memory]]。它只保存当前模型前向传播需要的 K/V 张量，不保存用户事实、长期偏好或可检索知识。

KV Cache 也不是 [[RAG]]。RAG 负责从外部资料中选证据进入上下文；KV Cache 负责已经进入模型上下文后的推理复用。

KV Cache 不是 Prompt Caching 的同义词。Prompt Caching 是跨请求复用相同前缀计算结果的 API / serving 机制；KV Cache 是单次推理内的底层 attention cache。两者相关，但不是同一个产品层概念。

## 最小例子

```text
prefix: A B C
step 1: 计算 A/B/C 的 K/V，并放入 KV Cache
step 2: 生成 D 时，只算 D 的 Q/K/V；D 的 Q 直接 attend 到缓存中的 A/B/C K/V
step 3: 把 D 的 K/V 追加进 KV Cache，生成 E 时复用 A/B/C/D
```

## 常见误解 / 风险

- 误解：KV Cache 只影响速度，不影响资源。实际它会大量占用 GPU 显存，长上下文和大 batch 下会直接限制并发。
- 误解：把 KV Cache 放 CPU 就能省显存且无代价。真实代价是热路径跨设备传输，可能用吞吐和延迟换容量。
- 误解：Prompt Caching 等于 KV Cache。Prompt Caching 是跨请求的前缀复用策略，命中规则、TTL、计费和服务端策略都属于 API / serving 层。
- 风险：只看模型权重大小，不估算 KV Cache，容易错误判断“某模型能不能在一张卡上跑长上下文”。

## 边界细节

和 [[Multi-Head Attention]] 的边界：MHA 描述 attention head 结构；KV Cache 描述推理时如何保存已经计算好的 K/V。MHA、MQA、GQA 决定“要缓存多少组 K/V”，KV Cache 是“缓存这些 K/V”的运行机制。

和 [[Context Window]] 的边界：context window 是一次调用能容纳多少 token；KV Cache 是让这些 token 在逐步生成中可复用的推理状态。窗口越长，KV Cache 通常越大。

和 FlashAttention 的边界：FlashAttention 优化 attention 计算的访存模式，不是长期保存历史 K/V 的缓存机制。它能和 KV Cache 同时使用，属于实现层优化。

和 PagedAttention 的边界：PagedAttention 是 KV Cache 管理方式，把 KV cache 按 block/page 管理以减少碎片、提升并发和共享效率；它不是新的 attention 语义。

## 现代性状态

- 判定：foundation + current-practice + watch。
- 为什么：KV Cache 是当前 decoder-only LLM 推理基本盘；没有它，大多数交互式生成难以达到可用延迟。
- 稳定部分：缓存历史 K/V、逐 token 复用、显存随序列和 batch 增长，是稳定边界。
- 易变部分：KV cache quantization、CPU/GPU/offload 分层、PagedAttention 变体、prefix/prompt caching 策略、服务端 cache eviction 和具体厂商计费会快速变化。
- 下一次复查点：学习 vLLM / SGLang / TGI / TensorRT-LLM 的 serving 细节时，回看当前 KV cache 管理、prefix caching 和 quantization 支持。

## 现代系统怎么吸收 KV Cache 的价值 / 局限

现代推理系统把 KV Cache 当作核心 runtime 资源管理对象，而不是普通临时变量。serving 层会围绕它做 batching、continuous batching、prefix sharing、paged/block allocation、eviction、offload、quantization 和调度。

它的局限也会被系统层吸收：显存不够时，模型可能降低 batch、缩短上下文、启用 GQA/MQA/MLA、量化 KV、把冷 KV offload，或者用 PagedAttention 这类块管理减少碎片。工程判断不是“有没有 KV Cache”，而是“热 KV 放哪里、能共享多少、何时丢弃、怎样不让它吞掉并发”。

## 证据锚点

- Source evidence: [[128 ai llm 14. KV Cache 是什么？Prompt Caching 的原理是什么？#KV Cache：单次推理内的优化]] 支撑单次推理内复用 K/V 的解释。
- Source evidence: [[128 ai llm 14. KV Cache 是什么？Prompt Caching 的原理是什么？#KV Cache 的显存代价]] 支撑显存公式和长上下文代价。
- Paper evidence: [[Fast Transformer Decoding - One Write-Head is All You Need#论文主张]] 支撑 MQA 通过共享 K/V 降低解码内存带宽 / cache 压力。
- Paper evidence: [[GQA - Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints#论文主张]] 支撑 GQA 作为 MHA 与 MQA 的折中。
- Paper evidence: [[Efficient Memory Management for Large Language Model Serving with PagedAttention#论文主张]] 支撑 PagedAttention 针对 KV cache memory management。
- Paper evidence: [[FlashAttention - Fast and Memory-Efficient Exact Attention with IO-Awareness#论文主张]] 支撑 FlashAttention 是 attention IO / memory-efficient exact attention 优化，不是 KV Cache 同义词。
- Evidence type: paper source note + interview raw source + engineering synthesis.
- Confidence: high for core mechanism; medium for serving-system implementation details because不同框架和硬件策略会变化。
- Boundary: 本卡不保存具体厂商 prompt caching 价格、cache TTL 或某模型上下文长度；这些属于易变产品参数。

## 复习触发

1. KV Cache 为什么让自回归生成可用？
2. 为什么 KV Cache 通常优先放 GPU，而不是普通 CPU 内存？
3. MQA、GQA、PagedAttention、FlashAttention 分别从哪个层面缓解 KV Cache / attention 瓶颈？
4. 为什么 Prompt Caching 相关但不等于 KV Cache？

## 相关链接

- [[LLM]]
- [[Transformer]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Context Window]]
- [[LLM 上下文限制与突破条件]]
