---
type: concept
topic:
  - rag
  - infrastructure
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Microsoft RAG 官方文档]]"
evidence:
  - "[[Agent 工程基础设施主源#RAG / 检索基础设施]]"
  - "[[Microsoft RAG 官方文档#一句话]]"
related:
  - "[[RAG]]"
  - "[[Embedding]]"
  - "[[Retriever]]"
  - "[[Hybrid Search]]"
---

# Vector Database

## 一句话

Vector Database 是为 embedding 向量检索设计的数据库或索引系统，常用于 RAG 从大量文档片段中找语义相似内容。

## 概念详解

Vector Database 解决的是“如何存储、索引和快速搜索大量向量”的基础设施问题。RAG 会把文档 chunk 转成 [[Embedding]]，再在查询时找与问题向量相近的 chunk。少量资料可以用简单内存索引；资料规模、更新频率、metadata filter、权限、删除、监控和高可用要求上来后，就需要专门的向量数据库或带 vector index 的搜索/数据库系统。

它通常提供近似最近邻搜索、top-k 返回、metadata filter、namespace/collection、批量写入、删除更新、索引配置和向量距离度量。有些系统也支持全文搜索、hybrid search、稀疏向量、多租户、备份和权限集成。[[Agent 工程基础设施主源]] 把 Pinecone、Weaviate、Qdrant、Milvus 等列为 RAG / 检索基础设施，说明它们是工程层，不是 RAG 概念本身。

Vector Database 的常见误区是把“有向量库”当成“有 RAG”。实际上向量库只负责存和找向量；资料是否解析好、chunk 是否合理、embedding 是否适合领域、retrieval 是否结合关键词、reranking 是否有效、答案是否引用证据，都在它之外。换一个向量库通常不能修复 ingestion、chunking 或评估缺失造成的质量问题。

证据边界：基础设施 source note 支持向量数据库作为 RAG 检索基础设施；Microsoft RAG source note 支持企业 RAG 还需要数据治理、索引、检索质量、权限和评估。具体产品功能、价格和 API 很易变，所以这张卡不把某个厂商特性写成通用定义。

## 它解决什么问题

RAG 需要从外部知识库里快速找相关材料。普通数据库擅长精确查询，向量数据库擅长近似语义搜索、metadata filter、top-k 召回和大规模索引管理。

代表生态包括 Pinecone、Weaviate、Qdrant、Milvus，以及云厂商搜索/数据库里的 vector index。

## 它不是什么

Vector Database 不是 RAG 本身。

它也不是唯一检索方式。生产系统经常需要 [[Hybrid Search]]、reranking、图检索、权限过滤和引用校验。

## 最小例子

```text
文档 -> chunk -> embedding -> vector database -> top-k chunks -> LLM answer
```

## 常见误解 / 风险

- 误解：向量相似就等于答案正确。
- 误解：换一个向量库就能解决 RAG 质量问题。
- 风险：metadata filter、权限、删除和更新没有设计好，会泄露或召回旧资料。
- 风险：chunk 太差时，向量库只能更快地找出差上下文。

## 边界细节

和 [[Embedding]] 的边界：embedding 是向量表示；vector database 是保存和检索向量的系统。

和 [[Retriever]] 的边界：retriever 是检索组件或流程；vector database 是它可能调用的基础设施之一。

和 [[Hybrid Search]] 的边界：vector database 偏向向量召回；hybrid search 会把向量与关键词/全文信号合并。

## 现代性状态

- 判定：current-practice。
- 稳定部分：RAG 常需要向量索引来做语义召回。
- 易变部分：具体数据库、索引算法、过滤能力、混合检索支持和托管产品 API。
- 复查点：选型时看数据规模、更新频率、metadata/权限需求、hybrid search 和评测，而不是只看相似度 demo。

## 现代系统怎么吸收 Vector Database 的价值

现代系统把 vector database 放在 retrieval infrastructure 层，并配套 ingestion、metadata schema、权限同步、删除更新、trace 和 RAG eval。它是 RAG 的底座之一，不是质量保证本身。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: [[Agent 工程基础设施主源#RAG / 检索基础设施]]
- Source: [[Microsoft RAG 官方文档]]
- Anchor: [[Microsoft RAG 官方文档#一句话]]
- Evidence type: infrastructure source note + official docs source note + engineering synthesis.
- Confidence: medium
- Boundary: sources 支持向量数据库作为检索基础设施；具体厂商能力、性能和 API 是易变实现细节。

## 复习触发

- 为什么 Vector Database 不是 RAG 本身？
- metadata filter 和权限为什么属于向量库选型的重要边界？
- 如果 RAG 质量差，哪些问题不是换向量库能解决的？

## 相关链接

- [[RAG]]
- [[Embedding]]
- [[Chunking]]
- [[Retriever]]
- [[Hybrid Search]]
