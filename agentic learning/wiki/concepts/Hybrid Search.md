---
type: concept
topic:
  - rag
  - retrieval
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[RAG 类型对比]]"
  - "[[Microsoft RAG 官方文档]]"
evidence:
  - "[[Agent 工程基础设施主源#RAG / 检索基础设施]]"
  - "[[RAG 类型对比#一张表先抓住]]"
  - "[[Microsoft RAG 官方文档#一句话]]"
related:
  - "[[RAG]]"
  - "[[Vector Database]]"
  - "[[Retriever]]"
  - "[[Reranking]]"
---

# Hybrid Search

## 一句话

Hybrid Search 是把向量语义检索和关键词/全文检索结合起来的检索方式。

## 概念详解

Hybrid Search 出现的原因是：单一检索信号通常不够。向量检索擅长语义相似，可以把“忘记密码怎么办”和“如何重置密码”匹配起来；但它可能漏掉精确实体、错误码、版本号、函数名、合同条款编号或专有名词。关键词/全文检索擅长精确匹配，却不理解同义表达和上下文含义。Hybrid Search 把两者组合起来，让系统既能理解语义，也能保住精确匹配。

在 RAG pipeline 中，hybrid search 常用于初召回：同一个 query 同时进入 vector search 和 BM25/fulltext search，两边各取一批候选，再合并、去重、过滤、归一化评分，必要时交给 [[Reranking]] 重新排序。它不是简单把两个列表拼在一起，因为不同检索器的分数尺度不同，重复文档需要合并，metadata filter 和权限过滤要在正确阶段生效，排序策略也会影响最终上下文。

Hybrid Search 的边界是检索召回与初排。它能提高“找得到相关资料”的概率，但不能保证答案忠实，也不能替代 citation check、RAG evaluation 或人工审核。如果向量和关键词召回都没有找到正确证据，reranker 和 generator 也只能在错误候选里工作。

证据边界：[[RAG 类型对比]] 支持 hybrid RAG 作为向量检索和关键词检索互补的检索模式；[[Agent 工程基础设施主源]] 支持现代检索基础设施会同时涉及向量数据库、搜索引擎和 RAG eval；Microsoft source note 支持企业 RAG 的索引、检索质量和评估边界。具体融合算法、权重和产品能力是工程实现，不是概念定义。

## 它解决什么问题

向量检索懂语义，但可能漏掉专有名词、编号、错误码、函数名。关键词检索能抓精确词，但不懂语义。Hybrid Search 让两者互补。

## 它不是什么

Hybrid Search 不是简单把两个结果列表拼起来。

真实系统还要处理权重、去重、排序、过滤、rerank 和引用。

## 最小例子

```text
query
  -> vector search top 50
  -> BM25/fulltext top 50
  -> merge + deduplicate + filter
  -> rerank
  -> answer
```

## 常见误解 / 风险

- 关键词权重太高会退化成传统搜索。
- 向量权重太高会漏掉精确实体。
- 合并策略不透明时很难排查检索失败。
- hybrid search 提升召回，不等于最终答案一定忠实。

## 边界细节

和 [[Embedding]] 的边界：embedding 是语义表示；hybrid search 是把语义检索和词法检索组合的检索策略。

和 [[Reranking]] 的边界：hybrid search 负责召回和初排；reranking 在候选集上重新判断相关性。

和 [[GraphRAG]] 的边界：hybrid search 解决向量/关键词互补；GraphRAG 解决实体关系、图结构和多跳上下文。

## 现代性状态

- 判定：current-practice。
- 稳定部分：生产 RAG 常需要语义检索与关键词/全文检索互补。
- 易变部分：融合算法、搜索产品能力、向量索引和 reranker 组合会变化。
- 复查点：当数据里有大量专有名词、代码或编号时，必须评估 hybrid search，而不是只看向量召回。

## 现代系统怎么吸收 Hybrid Search 的价值

现代系统通常把 hybrid search 放在 retrieval 层，并把权重、去重、metadata filter、rerank、trace 和 eval 连起来。一次检索失败要能看到：向量候选是什么、关键词候选是什么、合并后丢了什么、reranker 为什么把某个 chunk 排到前面。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: [[Agent 工程基础设施主源#RAG / 检索基础设施]]
- Source: [[RAG 类型对比]]
- Anchor: [[RAG 类型对比#一张表先抓住]]
- Source: [[Microsoft RAG 官方文档]]
- Anchor: [[Microsoft RAG 官方文档#一句话]]
- Evidence type: infrastructure source note + local comparison map + official docs source note + engineering synthesis.
- Confidence: medium
- Boundary: sources 支持 hybrid search 的工程必要性和边界；具体分数融合、权重和产品 API 不是稳定概念定义。

## 复习触发

- 为什么向量检索和关键词检索会互补？
- Hybrid Search 为什么不是两个 top-k 列表相加？
- 如果系统漏掉错误码或函数名，应该优先检查哪一层？

## 相关链接

- [[RAG]]
- [[Vector Database]]
- [[Reranking]]
- [[Retriever]]
