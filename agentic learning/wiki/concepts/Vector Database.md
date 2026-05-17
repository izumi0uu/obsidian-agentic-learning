---
type: concept
topic:
  - rag
  - infrastructure
status: growing
created: 2026-05-06
updated: 2026-05-16
last_checked: 2026-05-16
freshness: watch
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Microsoft RAG 官方文档]]"
  - https://alexgarcia.xyz/sqlite-vec/
  - https://github.com/asg017/sqlite-vec
evidence:
  - "[[Agent 工程基础设施主源#RAG / 检索基础设施]]"
  - "[[Microsoft RAG 官方文档#一句话]]"
  - "sqlite-vec docs: vector search SQLite extension, vec0 virtual table, pure SQL KNN example"
related:
  - "[[RAG]]"
  - "[[Embedding]]"
  - "[[Retriever]]"
  - "[[Hybrid Search]]"
  - "[[常用向量数据库对比]]"
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

## Agent / RAG 选型边界

这个问题应沉淀为“类别级选型边界”，而不是给 Qdrant、pgvector、Chroma、FAISS、Milvus、Weaviate、Pinecone、sqlite-vec 等每个名字都建稳定概念卡。原因是：产品能力、API、价格、托管方式和性能数据变化很快；更稳定的学习价值是看清它们分别属于本地索引、SQLite 嵌入式扩展、Postgres 扩展、专用向量服务、搜索系统向量检索、图数据库 + 向量/全文索引这些不同层。

| 场景 | 常用选择 | 为什么 | 不要误用 |
|---|---|---|---|
| 本地 demo / 学习 | Chroma、FAISS | 接入快，适合先跑通 RAG / memory 的最小闭环 | 不要把本地 demo 的便利性误当成生产治理能力 |
| 本地单文件 / 嵌入式应用 | SQLite + sqlite-vec | sqlite-vec 是 SQLite 的 vector search extension，可以用 `vec0` virtual table 在 SQLite 内存储向量并做 KNN 查询；适合桌面、移动、边缘、个人知识库和小型本地 RAG / memory | 不要把它当成独立向量数据库服务；embedding 生成、权限、多用户隔离、hybrid search、rerank 和评测仍要另行设计；也不要把 sqlite-vec、sqlite-vss、SQLite 官方 Vec1 混成同一个项目 |
| 小中型产品 / 后端已有 Postgres | PostgreSQL + pgvector | 结构化数据、metadata、权限字段和向量检索可放在同一套数据库里，少一层同步和运维 | 如果向量规模、QPS、过滤复杂度或多租户隔离上来，可能需要专用搜索/向量服务 |
| 生产级专用向量服务 | Qdrant、Milvus、Weaviate、Pinecone | 更聚焦向量索引、过滤、扩展、服务化、客户端生态和部署形态 | 不要只按“哪个最 AI”排序；要看数据规模、更新频率、filter、hybrid search、成本、运维和数据边界 |
| 已经有搜索系统 | Elasticsearch / OpenSearch vector search | 可以把关键词检索、全文检索、向量检索和部分 hybrid search 放在同一搜索栈里 | 如果只是小型语义检索 demo，引入完整搜索系统可能过重 |
| 关系密集 / GraphRAG | Neo4j + 向量 / 全文索引，或图数据库 + 向量库组合 | 适合实体关系、路径遍历、多跳关系和向量召回组合 | Neo4j 不是“更高级的向量库”；构图质量、实体消歧和关系维护才是主要成本 |

### Agent 长期记忆的存储边界

Agent 长期记忆不应该理解成“所有东西都塞进向量库”。用户偏好、配置、权限、账户状态、当前任务状态、审批状态、删除/保留策略等信息，通常更适合关系库、KV、事件日志或明确的 state store；它们需要确定性读写、权限控制、审计和精确更新。向量数据库更适合语义召回：对话摘要、文档 chunk、经验片段、案例片段、用户过去表达过的自然语言偏好等。

面试式回答可以压缩成：Agent 里的向量数据库主要用于 RAG 和长期记忆的语义检索；学习/原型用 Chroma 或 FAISS，本地单文件 / 嵌入式应用可看 sqlite-vec，真实项目 MVP 若已有 Postgres 可优先 pgvector，数据量/QPS/filter/服务化要求上来再看 Qdrant、Milvus、Weaviate、Pinecone，已有搜索系统时评估 Elasticsearch/OpenSearch，关系密集或 GraphRAG 场景再考虑 Neo4j + 向量/全文/图遍历组合。选型看数据规模、过滤条件、更新频率、运维成本、权限和 hybrid search，而不是看哪个名字更像 AI 基础设施。

## 现代性状态

- 判定：current-practice。
- 稳定部分：RAG 常需要向量索引来做语义召回。
- 易变部分：具体数据库、SQLite/Postgres/search 扩展、索引算法、过滤能力、混合检索支持和托管产品 API。
- 复查点：选型时看数据规模、更新频率、metadata/权限需求、hybrid search 和评测，而不是只看相似度 demo。

## 现代系统怎么吸收 Vector Database 的价值

现代系统把 vector database 放在 retrieval infrastructure 层，并配套 ingestion、metadata schema、权限同步、删除更新、trace 和 RAG eval。它是 RAG 的底座之一，不是质量保证本身。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: [[Agent 工程基础设施主源#RAG / 检索基础设施]]
- Source: [[Microsoft RAG 官方文档]]
- Anchor: [[Microsoft RAG 官方文档#一句话]]
- External check: sqlite-vec docs and GitHub checked on 2026-05-16; project positions it as a vector search SQLite extension that runs without a separate server and uses SQL / `vec0` virtual tables for KNN search.
- Evidence type: infrastructure source note + official docs source note + official/project docs checked on 2026-05-16 + engineering synthesis.
- Confidence: medium
- Boundary: sources 支持向量数据库作为检索基础设施；选型表是类别级工程综合，具体厂商能力、性能、价格和 API 是易变实现细节。

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
- [[常用向量数据库对比]]
