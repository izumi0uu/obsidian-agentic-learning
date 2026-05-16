---
type: concept
topic:
  - rag
  - retrieval
status: growing
created: 2026-05-06
updated: 2026-05-16
last_checked: 2026-05-15
freshness: watch
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[RAG 类型对比]]"
  - "[[Microsoft RAG 官方文档]]"
  - "[[Azure Search OpenAI Demo Repo]]"
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？]]"
  - "[[TF-IDF]]"
  - "[[Sparse Retrieval]]"
  - "[[BM25]]"
evidence:
  - "[[Agent 工程基础设施主源#RAG / 检索基础设施]]"
  - "[[RAG 类型对比#一张表先抓住]]"
  - "[[Microsoft RAG 官方文档#一句话]]"
  - "[[Azure Search OpenAI Demo Repo#一句话]]"
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第三层：召回优化]]"
  - "[[TF-IDF#概念详解]]"
  - "[[Sparse Retrieval#证据锚点]]"
  - "[[BM25#证据锚点]]"
up:
  - "[[Retriever]]"
relations:
  - type: composes_with
    target: "[[Sparse Retrieval]]"
    note: "Hybrid Search 通常把 sparse retrieval / BM25 作为一路候选。"
  - type: composes_with
    target: "[[Dense Retrieval]]"
    note: "Hybrid Search 通常把 dense retrieval 作为另一条语义召回。"
  - type: related_to
    target: "[[Multi-Route Retrieval]]"
    note: "Hybrid Search 是多路召回最常见的双路形态，但多路召回更宽。"
related:
  - "[[RAG]]"
  - "[[Vector Database]]"
  - "[[Retriever]]"
  - "[[Reranking]]"
  - "[[Agentic Retrieval]]"
  - "[[RAG Evaluation]]"
  - "[[TF-IDF]]"
  - "[[Sparse Retrieval]]"
  - "[[BM25]]"
  - "[[Multi-Route Retrieval]]"
  - "[[Dense Retrieval]]"
  - "[[Reciprocal Rank Fusion]]"
aliases:
  - "混合检索"
  - "hybrid search"
  - "hybrid retrieval"
---

# Hybrid Search

## 一句话

Hybrid Search 是把向量语义检索和关键词/全文检索结合起来的检索方式。

## 概念详解

Hybrid Search 出现的原因是：单一检索信号通常不够。向量检索 / dense retrieval 擅长语义相似，可以把“忘记密码怎么办”和“如何重置密码”匹配起来；但它可能漏掉精确实体、错误码、版本号、函数名、合同条款编号或专有名词。关键词、[[BM25]]、全文索引或 [[Sparse Retrieval]] 擅长精确词面匹配，却不理解同义表达和上下文含义。这里的 [[Sparse Retrieval]] 是总称，不是 [[TF-IDF]] 的别名；在现代工程里，[[BM25]] 更常被当作 sparse retrieval 的代表，而 [[TF-IDF]] 是更基础的词项加权方法。Hybrid Search 把这些信号组合起来，让系统既能理解语义，也能保住精确匹配。

在 RAG pipeline 中，hybrid search 常用于初召回：同一个 query 同时进入 vector search 和 [[BM25]] / fulltext search，两边各取一批候选，再合并、去重、过滤、融合排序，必要时交给 [[Reranking]] 重新排序。它不是简单把两个列表拼在一起，因为不同检索器的分数尺度不同，向量相似度和 BM25 分数不能直接相加；重复文档需要合并，metadata filter 和权限过滤要在正确阶段生效，排序策略也会影响最终上下文。

常见融合方式包括加权归一化和 [[Reciprocal Rank Fusion|RRF]]（Reciprocal Rank Fusion，倒数排名融合）。RRF 的学习价值在于：它主要看各路结果里的排名，而不是直接比较原始分数，因此适合把分数量纲不同的检索器结果合在一起。具体用哪种融合策略不是 Hybrid Search 的定义本身，而是工程实现和评估问题。

Hybrid Search 的边界是检索召回与初排。它能提高“找得到相关资料”的概率，但不能保证答案忠实，也不能替代 citation check、RAG evaluation 或人工审核。如果向量和关键词召回都没有找到正确证据，reranker 和 generator 也只能在错误候选里工作。

证据边界：[[RAG 类型对比]] 支持 hybrid RAG 作为向量检索和关键词检索互补的检索模式；[[Agent 工程基础设施主源]] 支持现代检索基础设施会同时涉及向量数据库、搜索引擎和 RAG eval；Microsoft source note 和 Azure demo source note 支持企业 RAG 的索引、搜索和检索质量边界；xiaolinnote RAG source note 支持多路召回、BM25 和 RRF 作为工程解释。具体融合算法、权重和产品能力是工程实现，不是概念定义。

## 它解决什么问题

向量检索懂语义，但可能漏掉专有名词、编号、错误码、函数名、代码符号和短查询里的关键信息。关键词检索能抓精确词，但不懂语义。Hybrid Search 让两者互补，降低单一路径漏召回的概率。

## 它不是什么

Hybrid Search 不是简单把两个结果列表拼起来，也不是“向量数据库的另一个名字”。

真实系统还要处理权重或 RRF、去重、排序、过滤、权限、rerank 和引用。它也不是 [[Multi-Route Retrieval]] 的完整同义词：Hybrid Search 常是 dense/vector + sparse/BM25 的常见双路形态，而 Multi-Route Retrieval 还可以包含多 Query、图检索、metadata filter、不同索引粒度或多个 retriever。它也不是 [[Agentic Retrieval]]：Hybrid Search 合并检索信号，Agentic Retrieval 规划多个信息需求和检索动作。

## 最小例子

```text
query
  -> vector search top 50
  -> BM25/fulltext top 50
  -> merge with RRF / weights
  -> deduplicate + metadata / permission filter
  -> rerank
  -> answer
```

更小的判断例子：用户问“ERR_CONNECTION_RESET 在 Chrome 里怎么处理”。向量检索可能找到“网络故障排查”这类语义相近文档，BM25/fulltext 能精确命中错误码。两路合并后，再由 reranker 判断哪段最能回答这个具体问题。

## 常见误解 / 风险

- 关键词权重太高会退化成传统搜索。
- 向量权重太高会漏掉精确实体。
- 合并策略不透明时很难排查检索失败。
- 不做去重会让同一文档占满上下文预算。
- 权限过滤如果放错阶段，可能把不该看的候选带入 trace 或上下文。
- hybrid search support 是产品能力，不能只看宣传页；要用目标语料做召回和排序评估。
- hybrid search 提升召回，不等于最终答案一定忠实。

## 边界细节

和 [[Embedding]] 的边界：embedding 是语义表示；hybrid search 是把语义检索和词法检索组合的检索策略。

和 [[Reranking]] 的边界：hybrid search 负责召回和初排；reranking 在候选集上重新判断相关性。

和 [[GraphRAG]] 的边界：hybrid search 解决向量/关键词互补；GraphRAG 解决实体关系、图结构和多跳上下文。

和 [[Sparse Retrieval]] / [[BM25]] / [[TF-IDF]] 的边界：sparse retrieval 是稀疏词法检索的总称，BM25 是常见工程代表；TF-IDF 是更早期的词项权重方法，不应直接等同于 sparse retrieval 本身。

和 [[Agentic Retrieval]] 的边界：hybrid search 不负责拆解复杂问题，也不决定查几个知识源；它只是一次或多次检索动作内部的信号融合。Agentic Retrieval 可以调用 hybrid search，但两者不在同一层。

和 [[Multi-Route Retrieval]] 的边界：hybrid search 是常见的多信号融合方式；Multi-Route Retrieval 是更宽的召回组织模式，可以把 hybrid search 当作一路或一个子策略。

和 [[RAG Evaluation]] 的边界：hybrid search 是否有用，要看目标问题集上的 recall、hit rate、rerank 前后变化、citation 支持率和延迟成本；不能只看某个 demo 的 top-k 样例。

## 现代性状态

- 判定：current-practice。
- 稳定部分：生产 RAG 常需要语义检索与关键词/全文检索互补。
- 易变部分：融合算法、搜索产品能力、向量索引、sparse/dense 模型和 reranker 组合会变化。
- freshness: watch。
- last_checked: 2026-05-15。
- 复查点：当数据里有大量专有名词、代码或编号时，必须评估 hybrid search，而不是只看向量召回。

## 现代系统怎么吸收 Hybrid Search 的价值

现代系统通常把 hybrid search 放在 retrieval 层，并把权重或 RRF、去重、metadata filter、权限过滤、rerank、trace 和 eval 连起来。一次检索失败要能看到：向量候选是什么、关键词候选是什么、合并后丢了什么、哪个 filter 移除了候选、reranker 为什么把某个 chunk 排到前面。

它的学习价值足够稳定：只要 RAG 资料里存在产品名、错误码、函数名、缩写、表格字段、法规条款、票据编号或中英混排，纯向量检索就容易出现盲区。Hybrid Search 是理解生产检索质量的基础边界之一，应该和 [[Retriever]]、[[Top-K]]、[[Vector Database]]、[[Reranking]] 一起复习。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: [[Agent 工程基础设施主源#RAG / 检索基础设施]]
- Source: [[RAG 类型对比]]
- Anchor: [[RAG 类型对比#一张表先抓住]]
- Source: [[Microsoft RAG 官方文档]]
- Anchor: [[Microsoft RAG 官方文档#一句话]]
- Source: [[Azure Search OpenAI Demo Repo]]
- Anchor: [[Azure Search OpenAI Demo Repo#一句话]]
- Source: [[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？]]
- Anchor: [[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第三层：召回优化]]
- Source: [[TF-IDF]]
- Anchor: [[TF-IDF#证据锚点]]
- Source: [[Sparse Retrieval]]
- Anchor: [[Sparse Retrieval#证据锚点]]
- Source: [[BM25]]
- Anchor: [[BM25#证据锚点]]
- Evidence type: infrastructure source note + local comparison map + official/docs repo source notes + RAG engineering source note + engineering synthesis.
- Confidence: medium
- Boundary: sources 支持 hybrid search 的工程必要性和边界；RRF/BM25 细节来自工程解释和实践综合，具体分数融合、权重、产品 API 和默认参数不是稳定概念定义。

## 复习触发

- 为什么向量检索和关键词检索会互补？
- Hybrid Search 为什么不是两个 top-k 列表相加？RRF 解决的是什么问题？
- 如果系统漏掉错误码或函数名，应该优先检查哪一层？
- Hybrid Search、Reranking、Agentic Retrieval 分别改造 retrieval 链路的哪一段？

## 相关链接

- [[RAG]]
- [[Vector Database]]
- [[Reranking]]
- [[Retriever]]
- [[Agentic Retrieval]]
- [[RAG Evaluation]]
- [[TF-IDF]]
- [[Sparse Retrieval]]
- [[BM25]]
