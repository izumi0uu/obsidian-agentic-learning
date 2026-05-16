---
type: concept
topic:
  - rag
  - retrieval
  - search
status: growing
created: 2026-05-16
updated: 2026-05-16
last_checked: 2026-05-16
freshness: stable
aliases:
  - 多路召回
  - 多路检索
  - multi-route retrieval
  - multi-retriever retrieval
source:
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？]]"
  - "[[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？]]"
evidence:
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#什么是多路召回？]]"
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#第一路：向量检索（Dense Retrieval）]]"
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#第二路：BM25 关键词检索（Sparse Retrieval）]]"
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#第三路：多 Query 扩展召回]]"
  - "[[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#结果融合：RRF 算法]]"
  - "[[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？#混合检索：两者结合]]"
up:
  - "[[Retriever]]"
relations:
  - type: composes_with
    target: "[[Hybrid Search]]"
    note: "Hybrid Search 通常是多路召回的一种常见两路形态，但多路召回还可以包括多 Query、图检索、metadata filter、不同索引粒度或多 retriever。"
  - type: composes_with
    target: "[[Sparse Retrieval]]"
    note: "多路召回常把 sparse retrieval / BM25 作为精确词面一路。"
  - type: composes_with
    target: "[[Reranking]]"
    note: "多路结果通常先融合成候选集合，再交给 reranker 精排；reranking 不是召回路线本身。"
related:
  - "[[Retriever]]"
  - "[[Hybrid Search]]"
  - "[[Sparse Retrieval]]"
  - "[[BM25]]"
  - "[[Query Rewrite]]"
  - "[[Reranking]]"
  - "[[Dense Retrieval]]"
  - "[[Multi-Query Retrieval]]"
  - "[[Reciprocal Rank Fusion]]"
  - "[[Cross-Encoder]]"
---

# Multi-Route Retrieval

## 一句话

Multi-Route Retrieval（多路召回）是在 RAG 的召回阶段同时走多条检索路线，再把候选结果合并、去重、融合排序，目标是减少单一路线的漏召回。

## 概念详解

多路召回出现的原因是：没有一种检索方式能覆盖所有查询。纯向量检索擅长语义相似，可以处理“退货”和“申请售后”这类不同说法，但对产品型号、错误码、函数名、数字、缩写等精确词面信号不稳定。[[BM25]] / [[Sparse Retrieval]] 正好相反：它们擅长精确命中词面，却不理解同义表达和换一种问法后的语义关系。

因此，多路召回把“找候选证据”拆成多个互补路线。xiaolinnote 的 source note 给出的典型三路是：一路向量检索负责语义覆盖；一路 BM25 关键词检索负责精确词面；一路多 Query 扩展把用户问题改写成多个角度分别检索。三路各自召回候选后，需要合并去重，并用 RRF 这类排名融合方法把不同分数体系下的结果变成一个统一候选列表，后面再交给 [[Reranking]] 精排。

这张卡选择 `Multi-Route Retrieval` 作为 canonical name，是为了保留中文工程语境里的“多路召回”边界，同时避免把它过窄地等同为 [[Hybrid Search]]。Hybrid Search 通常指 dense/vector + sparse/BM25 的混合检索，是多路召回中最常见、最稳定的一种形态；但多路召回还可以扩展到多 Query、不同 chunk 粒度、metadata filter、图检索、SQL / 搜索引擎 / 向量索引多源并行，或多个 retriever 的候选合并。

证据边界：当前主要证据来自 xiaolinnote 的 RAG 面试题 source note，支持“向量检索 + BM25 + 多 Query 扩展 + RRF + rerank”的工程解释。`Multi-Route Retrieval` 作为英文 canonical 是对中文工程术语的稳定化命名；它不像 BM25 或 TF-IDF 那样是单一算法名，也不像 Hybrid Search 那样已有更明确的产品/社区词，因此本卡重点沉淀边界，而不是声称这是唯一英文标准叫法。

## 它解决什么问题

它解决的是单路召回的盲区问题。只扩大 [[Top-K]] 常常只是把更多相似但无关的 chunk 塞进候选集，不一定能把缺失路线上的正确证据找回来。多路召回的思路是：与其要求一个 retriever 全能，不如让不同 retriever 分别覆盖不同失败模式。

典型场景包括：产品型号、错误码、代码符号需要 BM25 / sparse route；同义表达和语义相似需要 dense route；用户问法和文档写法角度差异很大时，需要多 Query route；关系路径或实体网络明显时，可以引入 graph route。

## 它不是什么

Multi-Route Retrieval 不是 [[Hybrid Search]] 的同义词。Hybrid Search 常是向量检索和关键词/全文检索的双路融合；多路召回是更宽的策略，可以包含 hybrid search，也可以包含多 Query、图检索、metadata filter 或多源 retriever。

它也不是 [[Reranking]]。多路召回负责扩大和补足候选集合；reranking 负责在候选集合里重新排序。如果某一路完全没有召回正确证据，reranker 无法凭空创造它。

它也不是简单调大 [[Top-K]]。Top-K 只改变单一路线取多少候选；多路召回改变的是候选从哪些路线来。

## 最小例子

```text
query
  -> dense vector search top 30
  -> BM25 / sparse search top 30
  -> LLM rewrite into 3 query variants, each search top 10
  -> merge + deduplicate
  -> RRF / weighted fusion
  -> rerank top 8
  -> context for generation
```

最小判断场景：用户问“RTX 4090 显卡功耗”。如果知识库里精确写着 `RTX 4090`，BM25 可能比向量检索更稳；如果用户问“怎么申请售后”，向量检索可能比 BM25 更容易找到写着“退货流程”的文档；如果用户问法和文档角度不同，多 Query 扩展可能把正确表述召回来。

## 常见误解 / 风险

- 误解：多路召回就是 hybrid search。风险是把多 Query、图检索、多源检索和不同索引粒度都漏掉。
- 误解：多路越多越好。路线越多，延迟、成本、重复候选、融合调参和 trace 复杂度越高。
- 误解：RRF 后就不用 rerank。RRF 适合粗融合，不等于深度相关性判断。
- 误解：召回多就一定更准。噪声候选也会占用上下文预算，可能稀释正确证据。
- 风险：不同路线的权限过滤、metadata filter 和去重顺序不一致，可能导致候选泄露、重复或不可复现。

## 边界细节

和 [[Retriever]] 的边界：Retriever 是找候选的组件或流程；Multi-Route Retrieval 是一种 retriever 设计策略，让多个路线一起贡献候选。

和 [[Hybrid Search]] 的边界：Hybrid Search 是常见双路或多信号融合方式，通常强调 dense + sparse / vector + keyword；Multi-Route Retrieval 是更宽的召回组织模式。

和 [[Query Rewrite]] 的边界：Query Rewrite 改写查询本身；Multi-Route Retrieval 可以把多 Query 扩展作为一路，但不等于所有 query rewrite。

和 [[Agentic Retrieval]] 的边界：Agentic Retrieval 强调 query planning、多源选择、检索动作控制和 grounding data 合并；Multi-Route Retrieval 可以作为其中的执行策略，但本身不要求完整 agentic loop。

和 [[Reranking]] 的边界：多路召回先扩大候选覆盖，reranking 后判断候选谁更该进上下文。

## 现代性状态

- 判定：current-practice。
- 稳定部分：生产 RAG 常需要多种召回信号互补，特别是 dense 与 sparse 的互补。
- 易变部分：具体路线数量、RRF/权重融合、reranker、向量库/搜索产品能力、是否引入 LLM query expansion 或 graph route 会随系统和产品变化。
- freshness: stable。
- 复查点：当新的检索产品或 agentic retrieval 文档把多路检索能力产品化时，更新具体工程例子，而不是改写这个边界。

## 现代系统怎么吸收 Multi-Route Retrieval 的价值

现代 RAG 系统会把多路召回做成可观测 pipeline：每一路的 query、filter、top-k、候选、分数或排名、去重结果、融合结果、rerank 前后变化都写入 trace。这样当答案缺证据时，可以判断是某一路没有召回、融合策略把正确候选压低、filter 过早删除，还是 reranker 排错。

工程上，它通常不是“所有路线都上满”，而是按失败模式加路线：精确词漏召回先加 BM25 / sparse；表述角度差异大再加多 Query；关系查询多再考虑 graph route；正确候选已在集合里但排序差，再加 reranking 和评估。

## 证据锚点

- Source: [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？]]
- Anchor: [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#什么是多路召回？]]
- Anchor: [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#第一路：向量检索（Dense Retrieval）]]
- Anchor: [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#第二路：BM25 关键词检索（Sparse Retrieval）]]
- Anchor: [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#第三路：多 Query 扩展召回]]
- Anchor: [[raw/repos/xiaolinnote/questions/026 ai rag 13. 什么是多路召回？具体怎么做？#结果融合：RRF 算法]]
- Source: [[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？]]
- Anchor: [[raw/repos/xiaolinnote/questions/024 ai rag 11. 请你介绍一下向量检索和关键词检索的区别？#混合检索：两者结合]]
- Evidence type: interview/source note + engineering synthesis.
- Confidence: medium-high for the Chinese engineering concept boundary; medium for the English canonical label because source evidence supports the pattern more strongly than one universal English term.
- Boundary: 当前不把 RRF、Multi-Query Retrieval 或 Dense Retrieval 直接建成子卡；它们仍可作为后续候选，根据证据密度再拆。

## 复习触发

1. 为什么调大 Top-K 不能替代多路召回？
2. Multi-Route Retrieval 和 Hybrid Search 的最小区别是什么？
3. 向量检索、BM25、多 Query 扩展分别补哪类漏召回？
4. RRF 和 Reranking 分别在多路召回后解决什么问题？
5. 一个 RAG 系统增加新召回路线前，应该先看哪些 trace 和评估指标？

## 相关链接

- [[Retriever]]
- [[Hybrid Search]]
- [[Sparse Retrieval]]
- [[BM25]]
- [[Query Rewrite]]
- [[Query Planning]]
- [[Agentic Retrieval]]
- [[Reranking]]
- [[Top-K]]
