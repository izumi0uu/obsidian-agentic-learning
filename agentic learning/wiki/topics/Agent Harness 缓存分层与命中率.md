---
type: map
topic:
  - agent
  - harness
  - caching
  - context
  - rag
status: active
created: 2026-05-26
updated: 2026-05-26
source:
  - "[[Agent Harness]]"
  - "[[Context Engineering]]"
  - "[[KV Cache]]"
  - "[[TTL]]"
  - "[[128 ai llm 14. KV Cache 是什么？Prompt Caching 的原理是什么？]]"
evidence:
  - "[[Agent Harness#证据锚点]]"
  - "[[Context Engineering#证据锚点]]"
  - "[[KV Cache#证据锚点]]"
  - "[[TTL#证据锚点]]"
  - "[[128 ai llm 14. KV Cache 是什么？Prompt Caching 的原理是什么？#从 KV Cache 到 Prompt Caching：同一机制的扩展]]"
related:
  - "[[Agent Harness]]"
  - "[[Context Engineering]]"
  - "[[KV Cache]]"
  - "[[TTL]]"
  - "[[RAG]]"
  - "[[Retriever]]"
  - "[[Embedding]]"
  - "[[Trace]]"
  - "[[Evaluation]]"
---

# Agent Harness 缓存分层与命中率

## 一句话总览

Agent 系统里的缓存命中率不是一个单层指标：[[KV Cache]] 属于模型推理 / serving 热路径，Prompt Caching 属于 provider serving 层，tool result、embedding、retrieval、summary 和 context cache 才更接近 [[Agent Harness]] / 应用层责任。命中率高通常说明重复计算被复用、成本和延迟下降；它不自动说明答案更正确、资料更新、权限安全或上下文更可靠。

## 为什么值得记录

Agent harness 讨论“缓存命中率”时最容易混成一句话：缓存命中是不是 harness 层做的？答案要拆层。

缓存本质上是在复用某个中间产物，但不同中间产物的控制权不同。模型内部 K/V 张量、provider 端 prompt prefix、tool API 返回值、embedding 向量、retrieval 候选、上下文摘要和 skill/resource 片段，都可能被叫 cache。它们的 key、生命周期、权限边界、失效方式和观测指标完全不同。

所以这页的学习价值是把“命中率”从一个好听的性能词拆成工程问题：命中了哪一层缓存？谁能控制 key？谁负责失效？命中后是否仍要检查权限、版本、freshness 和证据？如果这些问题没拆开，高命中率可能只是把旧错误更快地复用出去。

## 缓存分层表

| 缓存层 | 命中位置 | Harness 责任 | 主要风险 |
|---|---|---|---|
| [[KV Cache]] | 模型推理 / serving 热路径 | 通常不可直接控制，只能通过请求长度、模型/serving 选择、并发和上下文策略间接影响 | 显存 / 带宽压力；不要误当长期记忆或应用层缓存 |
| Prompt Cache / Prompt Caching | provider serving 层跨请求前缀复用 | 稳定 system / developer / tool schema / skill 前缀，把动态内容放后面，记录 `cached_tokens` / cache billing 信号 | 前缀轻微变化导致 miss；把 volatile 内容放前面会降低命中 |
| Tool Result Cache | harness / app 层 | cache key = tool + args + permission scope + user/tenant + TTL + data version | 复用过期结果、越权结果或错误参数结果 |
| Embedding Cache | RAG / indexing 层 | cache key = normalized text + embedding model id + dimension + preprocessing / chunking version | 模型、维度或切分策略变了但复用旧向量 |
| Retrieval Cache | retriever 层 | cache key = query / rewrite + index/corpus version + filters + top-k + permission scope | 知识库更新后继续返回旧候选；权限 filter 变化后返回不该看的 chunk |
| Context / Summary Cache | context engineering 层 | 复用摘要、stable context、skills、resource 片段，并记录来源、版本和更新时间 | 摘要丢关键状态、保留过期结论或掩盖来源差异 |

## 命中率怎么读

缓存命中率的最小含义是：请求中有多少比例复用了已有产物，而不是重新计算或重新查询。

```text
cache_hit_rate = cache_hits / (cache_hits + cache_misses)
```

但在 Agent harness 里，命中率要和层级一起读：

- Provider prompt cache 命中高：通常说明固定前缀稳定，可能降低输入成本和首 token 延迟。
- Tool result cache 命中高：说明重复工具请求多，可能是好事，也可能暴露 Agent loop 原地打转。
- Embedding cache 命中高：说明重复文本没有被反复 embedding，通常降低索引成本。
- Retrieval cache 命中高：说明重复 query 或 rewrite 多，可能降低延迟，但要看 corpus / permission / freshness 是否变了。
- Summary cache 命中高：说明上下文摘要被复用，但要检查摘要是否丢失最新状态。

一个很小的边界：命中率是效率指标，不是质量指标。质量还要看 [[Evaluation]]、[[Trace]]、RAG citation faithfulness、工具结果校验和任务成功率。

## Harness 能控制什么

Harness 直接能控制的是应用层缓存：tool result、retrieval、embedding、summary、context block、skill/resource loading 和 trace-derived reuse。这里 key 怎么设计、TTL 多久、是否按用户/租户/权限隔离、是否带版本号、miss 后怎么降级，都是 harness 或业务层责任。

Harness 通常不能直接控制模型内部 [[KV Cache]]。它可以通过上下文长度、并发、模型和服务栈选择影响 KV cache 压力，但不能把 KV cache 当成可查询的长期记忆。

Prompt Caching 介于两者之间：真正的命中发生在 provider serving 层，但 harness 能显著影响命中概率。常见做法是把稳定、长期复用的 system / developer 指令、tool schema、输出格式和静态 skill 描述放在前缀，把用户输入、检索结果、tool result、时间敏感材料和随机顺序内容放在后面。这样做的目标是复用前缀计算，而不是让 prompt 更“聪明”。

## 高命中率的风险

- Stale hit：缓存命中了，但命中的是旧知识、旧索引、旧价格、旧权限或旧 tool result。
- Permission leak：cache key 没有包含 user / tenant / permission scope，导致 A 用户的结果被 B 用户复用。
- Version drift：embedding model、chunking、query rewrite、tool schema 或 corpus 版本变了，但 key 没有变。
- Loop masking：Agent 反复发同一个 query / tool call，命中率很好看，但其实没有获得新信息。
- Evaluation blind spot：只看 latency / cost，不检查答案是否基于当前证据。

因此生产系统里更该记录“命中后是否仍可信”，而不是只记录“命中了多少”。

## 观测指标

| 指标 | 说明 | 典型用途 |
|---|---|---|
| cache hit rate | 命中次数占总访问次数比例 | 看复用效率 |
| stale hit rate | 命中后被判为过期、版本不匹配或需刷新比例 | 看 freshness 风险 |
| cache savings | 省下的 tokens、embedding 调用、tool 调用、retrieval 延迟或成本 | 看 ROI |
| cache key cardinality | key 种类数量和热点分布 | 判断 key 是否过细或过粗 |
| permission-scoped hit rate | 带 user / tenant / role scope 的命中率 | 避免跨权限复用 |
| miss reason | prefix changed、TTL expired、version changed、permission changed、cold start 等 | 定位为什么没有复用 |
| answer quality after hit | 命中缓存后的 answer faithfulness、task success、人工抽样结果 | 防止效率指标掩盖质量退化 |

## 最小例子

一个 RAG Agent 的缓存 key 可以这样拆：

```text
embedding_cache_key =
  sha256(normalized_chunk_text)
  + embedding_model_id
  + embedding_dimension
  + chunking_version
  + preprocessing_version

retrieval_cache_key =
  sha256(normalized_query_or_rewrite)
  + corpus_version
  + metadata_filters
  + permission_scope
  + top_k

tool_result_cache_key =
  tool_name
  + canonical_json(args)
  + user_or_tenant_scope
  + tool_schema_version
  + ttl_bucket
```

如果其中任何一个维度变化，cache miss 反而可能是正确行为。好的 harness 不追求无限高命中率，而是追求“该复用的复用，该失效的失效”。

## 边界细节

和 [[KV Cache]] 的边界：KV cache 是模型推理时保存 K/V 张量的热路径机制；Agent harness 看到的“缓存命中率”多半是 prompt cache billing signal、tool/retrieval/embedding/cache store 指标或 context reuse 指标。它们可以相关，但不是同一层指标。

和 [[Context Engineering]] 的边界：context engineering 负责装配本轮模型可见的信息；cache-aware context ordering 只是其中一个成本优化手段。上下文是否可信，仍取决于来源、权限、freshness、排序、压缩和引用约束。

和 [[RAG]] 的边界：RAG 里的 embedding / retrieval cache 只优化表示和召回成本，不替代 chunking、reranking、citation faithfulness 或 RAG evaluation。

和 [[TTL]] 的边界：TTL 是缓存 freshness 的最小生命周期控制，但不是事实校验、权限校验或强一致性保证。高风险知识还需要版本号、主动失效、人工审核或重新抓取。

## 证据锚点

- [[KV Cache#证据锚点]]：支撑 KV cache 是推理时 K/V 张量复用机制，不是长期记忆或 RAG。
- [[128 ai llm 14. KV Cache 是什么？Prompt Caching 的原理是什么？#从 KV Cache 到 Prompt Caching：同一机制的扩展]]：支撑 Prompt Caching 是跨请求相同前缀复用，并强调固定内容在前、动态内容在后。
- [[Agent Harness#证据锚点]]：支撑 harness 负责工具、状态、权限、trace、评测和停止边界。
- [[Context Engineering#证据锚点]]：支撑上下文装配、来源、顺序、预算和压缩属于工程治理。
- [[TTL#证据锚点]]：支撑缓存、memory 和 RAG freshness 的生命周期边界。
- Evidence type: existing concept/source synthesis + engineering boundary note.
- Confidence: medium-high for layer boundary; medium for具体 provider cache metrics，因为厂商实现和计费字段会变化。

## 复习触发

1. 一个系统说“cache hit rate 很高”，你会先问它命中了哪一层缓存？
2. 为什么 prompt cache 命中高不等于回答正确？
3. Tool result cache 的 key 为什么必须包含权限 scope 和版本？
4. Embedding cache 在模型、维度或 chunking 变化后为什么应该 miss？
5. Agent loop 重复调用同一个工具时，高命中率可能掩盖什么问题？

## 相关链接

- [[Agent Harness]]
- [[Context Engineering]]
- [[KV Cache]]
- [[TTL]]
- [[RAG]]
- [[Retriever]]
- [[Embedding]]
- [[Trace]]
- [[Evaluation]]
