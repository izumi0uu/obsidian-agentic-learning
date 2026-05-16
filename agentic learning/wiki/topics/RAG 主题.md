---
type: map
topic:
  - rag
status: active
created: 2026-05-05
updated: 2026-05-16
source:
  - "[[RAG]]"
  - "[[RAG 类型对比]]"
  - "[[Retrieval 组件对比]]"
  - "[[常用向量数据库对比]]"
  - "[[Context RAG Memory 对比]]"
  - "[[Parallel Search and Explicit Merging 检索模式]]"
  - "[[Sparse Retrieval]]"
  - "[[BM25]]"
  - "[[Multi-Route Retrieval]]"
  - "[[Microsoft RAG 官方文档]]"
  - "[[Neo4j GraphRAG 官方文档]]"
evidence:
  - "[[RAG#证据锚点]]"
  - "[[Retriever#证据锚点]]"
  - "[[Retrieval 组件对比#证据锚点]]"
  - "[[TF-IDF#证据锚点]]"
  - "[[Sparse Retrieval#证据锚点]]"
  - "[[BM25#证据锚点]]"
  - "[[Multi-Route Retrieval#证据锚点]]"
  - "[[常用向量数据库对比#证据锚点]]"
  - "[[RAG 类型对比#证据锚点]]"
  - "[[Context RAG Memory 对比#证据锚点]]"
  - "[[Parallel Search and Explicit Merging 检索模式#证据锚点]]"
  - "[[RAG Evaluation#证据锚点]]"
related:
  - "[[RAG]]"
  - "[[Retriever]]"
  - "[[TF-IDF]]"
  - "[[Sparse Retrieval]]"
  - "[[BM25]]"
  - "[[Multi-Route Retrieval]]"
  - "[[RAG 类型对比]]"
  - "[[Context RAG Memory 对比]]"
  - "[[Retrieval 组件对比]]"
  - "[[常用向量数据库对比]]"
  - "[[RAG Evaluation]]"
  - "[[RAG Citation Faithfulness]]"
  - "[[RAG Access Control]]"
  - "[[Query Rewrite]]"
  - "[[Query Planning]]"
  - "[[Parallel Search and Explicit Merging 检索模式]]"
  - "[[Graph Construction Evaluation]]"
  - "[[Entity Resolution]]"
  - "[[RAG 可靠性与治理对比]]"
  - "[[Query Rewrite Query Planning Agentic Retrieval 对比]]"
  - "[[GraphRAG 构图与评估对比]]"
  - "[[GraphRAG]]"
  - "[[Knowledge Graph]]"
  - "[[Obsidian + LLM Wiki]]"
---

# RAG 主题

## 一句话总览

RAG 主题的学习主线不是“向量库 + LLM”，而是：**外部资料如何进入知识库、如何被检索、如何被排序和装配进上下文、答案如何被证据约束和评估**。

最小边界：[[RAG]] 是检索增强生成的架构模式；[[Retriever]]、[[Embedding]]、[[Dense Retrieval]]、[[TF-IDF]]、[[Sparse Retrieval]]、[[BM25]]、[[Vector Database]]、[[Top-K]]、[[Multi-Route Retrieval]]、[[Multi-Query Retrieval]]、[[Reciprocal Rank Fusion]]、[[Hybrid Search]]、[[Reranking]]、[[Cross-Encoder]] 是 retrieval 组件 / 参数；[[GraphRAG]]、[[Agentic RAG]]、[[Corrective RAG]]、[[Self-RAG]] 是在不同位置改造 RAG 链路的类型；[[RAG Evaluation]] 负责检查检索排序指标（Hit@K / Recall@K / MRR / nDCG）、上下文、引用和答案质量。

## 先看这个

- [[RAG]]：先建立“参数记忆 / 非参数记忆 + retriever-generator”的地基。
- [[Retrieval 组件对比]]：区分 ingestion、chunk、embedding、vector database、retriever、hybrid search、reranking 的 pipeline 位置。
- [[常用向量数据库对比]]：记录 Chroma、FAISS、pgvector、Qdrant、Milvus、Weaviate、Pinecone、Elasticsearch/OpenSearch、Neo4j 的类别边界和选型刀口。
- [[RAG 类型对比]]：区分基础 RAG、GraphRAG、Agentic RAG、Corrective RAG、Self-RAG 等类型的介入点。
- [[Context RAG Memory 对比]]：区分 context engineering、RAG、memory、repo context 和 retriever 的上下文供给边界。
- [[RAG Evaluation]]：学习 RAG 失败时如何拆检索、上下文、引用和生成。
- [[RAG 可靠性与治理对比]]：把 [[RAG Citation Faithfulness]]、[[RAG Access Control]]、trace、audit 和 evaluation 放到同一张治理地图里。
- [[Query Rewrite Query Planning Agentic Retrieval 对比]]：区分“改写 query”“规划检索步骤”和“检索层 agentic loop”。
- [[Parallel Search and Explicit Merging 检索模式]]：学习 deep search / agentic RAG 中“多 query 并行检索 + 显式证据合并”的信噪比边界。
- [[GraphRAG 构图与评估对比]]：区分 [[Knowledge Graph]]、[[Entity Resolution]]、[[Graph Construction Evaluation]]、[[GraphRAG]] 和 [[Neo4j]]。
- [[Neo4j GraphRAG 官方文档]] / [[Neo4j]]：GraphRAG / Knowledge Graph RAG 的重要工程主源与实现生态。

## 学习路线

1. **先学最小 RAG**：读 [[RAG]]、[[Parametric Memory]]、[[Non-Parametric Memory]]，理解为什么外部知识库能补模型参数知识，但不能保证答案正确。
2. **再学 retrieval pipeline**：读 [[Document Ingestion]]、[[Chunking]]、[[Parent-Child Chunking]]、[[Embedding]]、[[Dense Retrieval]]、[[TF-IDF]]、[[Sparse Retrieval]]、[[BM25]]、[[Vector Database]]、[[Retriever]]、[[Top-K]]、[[Multi-Route Retrieval]]、[[Multi-Query Retrieval]]、[[Reciprocal Rank Fusion]]、[[Hybrid Search]]、[[Reranking]]、[[Cross-Encoder]]，训练自己按链路定位失败，而不是笼统说“RAG 不准”。
3. **再学 RAG 类型边界**：读 [[RAG 类型对比]]，把 [[GraphRAG]]、[[Agentic RAG]]、[[Agentic Retrieval]]、[[Corrective RAG]]、[[Self-RAG]] 放到“改造哪一段链路”的坐标里。
4. **最后学治理和评估**：读 [[RAG Evaluation]]、[[RAG Citation Faithfulness]]、[[RAG Access Control]]、[[RAG 可靠性与治理对比]]、[[Context Engineering]]、[[Indirect Prompt Injection]]，理解 citation、权限、上下文污染、prompt injection、trace 和回归测试为什么是生产 RAG 的关键。

小边界：如果一个问题用 3 篇文档就能回答，先手工整理上下文或做最小 RAG；不要一开始就上 GraphRAG、Agentic RAG 或复杂多轮检索。

## RAG pipeline 分层

```text
source -> ingest/clean -> chunk + metadata -> embed/index
      -> retrieve/filter -> hybrid merge -> rerank -> context assembly
      -> generate with evidence -> cite/verify/evaluate -> monitor/update
```

| 层 | 关键概念 | 主要问题 | 常见失败 |
|---|---|---|---|
| 资料入口 | [[Document Ingestion]], [[Chunking]] | 原始资料怎样被解析、切分、去重、标注 metadata / 权限 | 表格丢结构、chunk 断开条件、权限标签丢失 |
| 表示与索引 | [[Embedding]], [[Dense Retrieval]], [[TF-IDF]], [[Sparse Retrieval]], [[BM25]], [[Vector Database]] | 内容怎样变成可检索表示并被快速搜索 | 语义相似但事实不支持、精确词项漏召回、分词/倒排索引问题、索引过期、metadata filter 不可用 |
| 召回与融合 | [[Retriever]], [[Top-K]], [[Query Rewrite]], [[Multi-Query Retrieval]], [[Query Planning]], [[Multi-Route Retrieval]], [[Reciprocal Rank Fusion]], [[Hybrid Search]], [[Parallel Search and Explicit Merging 检索模式]] | query 如何找到候选证据，是否需要改写、分解、规划或并行多视角检索 | [[Top-K]] 漏掉关键文档、专有名词/编号匹配失败、query rewrite 偏题、query plan 过度复杂、多 query 引入重复和噪声 |
| 排序与上下文 | [[Reranking]], [[Cross-Encoder]], [[Context Engineering]] | 哪些证据进入上下文、按什么顺序、带哪些引用 | 正确证据排太后、上下文太噪、引用和 chunk 对不上 |
| 生成与校验 | [[RAG]], [[RAG Evaluation]], [[Context Recall]], [[Context Precision]], [[RAG Citation Faithfulness]] | 模型如何基于证据回答，答案是否被引用支持 | 有证据但模型误读、答案编造、citation 不支持结论 |
| 高级改造 | [[GraphRAG]], [[Entity Resolution]], [[Graph Construction Evaluation]], [[Agentic RAG]], [[Corrective RAG]], [[Self-RAG]] | 是否需要图结构、检索决策、证据质量门、自适应检索或构图评估 | 复杂度、延迟、trace/eval 成本上升，错误更难定位 |

## 组件入口

| 入口 | 先问的问题 | 学习重点 |
|---|---|---|
| [[Document Ingestion]] | 资料有没有正确进入知识库？ | 解析、清洗、结构保真、metadata、权限、版本 |
| [[Chunking]] | 一个证据单元是否完整？ | chunk 大小、重叠、标题层级、表格/代码/条件是否被切断 |
| [[Embedding]] | 语义表示适不适合这个领域？ | 相似不等于正确；专有名词、代码、编号需要额外策略 |
| [[TF-IDF]] | 我是否需要稀疏词项/关键词信号？ | 词频、逆文档频率、sparse vector；适合理解 BM25 和 hybrid search 的词面匹配边界 |
| [[Dense Retrieval]] | 我的检索是否需要语义相似和向量召回？ | 向量检索路线；不是整个 Retriever，也不替代 BM25 |
| [[Sparse Retrieval]] | 我的检索是否需要词面、编号、代码符号和倒排索引信号？ | 稀疏/词法检索家族；不是 TF-IDF 或 BM25 的别名 |
| [[BM25]] | 关键词命中的候选应该怎样排序？ | 搜索引擎和 RAG sparse side 的常见代表；适合精确词，不能替代语义检索 |
| [[Vector Database]] | 我需要什么样的向量索引和过滤能力？ | 存储/搜索向量，不等于完整 RAG；选型看数据规模、filter、更新频率、hybrid search、运维和现有技术栈 |
| [[Retriever]] | 系统怎样找到候选证据？ | query rewrite、filter、[[Top-K]]、召回、去重、多源检索；进一步读 [[Query Rewrite]] / [[Query Planning]] |
| [[Top-K]] | 一次检索先取多少候选？ | K 太小会漏证据，K 太大引入噪音和成本；还要切开 retrieval Top-K 与 decoding top-k |
| [[Multi-Query Retrieval]] | 单一 query 角度是否太窄？ | 用多个 query 变体扩大覆盖；属于 query rewrite/多路召回的策略 |
| [[Multi-Route Retrieval]] | 是否需要多条召回路线互补？ | 向量、BM25、多 Query、图检索、metadata filter 或多 retriever 的候选合并；不要等同于 Hybrid Search |
| [[Hybrid Search]] | 纯向量是否漏掉精确匹配？ | 向量 + 关键词/全文互补，尤其适合实体名、错误码、产品编号 |
| [[Reciprocal Rank Fusion]] | 多路结果怎么粗融合？ | 用排名倒数融合不同分数体系；通常在 rerank 前 |
| [[Reranking]] | 找到的候选谁更该进上下文？ | rerank 只能重排已召回候选，不能凭空找回漏掉的证据 |
| [[RAG Evaluation]] | 怎么知道 RAG 错在哪里？ | retrieval ranking metrics（Hit@K / Recall@K / MRR / nDCG）、context、generation、citation 分层评估；进一步读 [[RAG Citation Faithfulness]] |

向量库选型小边界：学习和快速原型可先用 Chroma / FAISS；已有 PostgreSQL 的 MVP 可优先评估 pgvector；规模、QPS、过滤、多租户或服务化要求上来后，再比较 Qdrant / Milvus / Weaviate / Pinecone；已有 Elasticsearch / OpenSearch 时，优先评估同栈 vector + keyword / full-text / hybrid search；关系密集或 GraphRAG 场景再考虑 Neo4j 的图遍历 + 向量 / 全文索引组合。这个判断属于工程综合，不是某个 vendor 的永久排名。 详见 [[常用向量数据库对比]]。

## 类型入口

| 类型 | 改造位置 | 什么时候值得看 | 边界提醒 |
|---|---|---|---|
| 基础 [[RAG]] | `retrieve -> generate` | 文档问答、知识库问答、带引用回答 | 不保证检索完整或答案忠实 |
| Vector / Hybrid / Reranked RAG | retrieval quality | 普通 RAG 检索不稳、专有名词多、正确证据排序靠后 | 它们改善检索质量，不自动解决生成误读 |
| [[GraphRAG]] | 知识结构 / 图关系 | 多跳关系、实体网络、跨文档关系、全局总结 | 图谱质量和构图成本可能超过收益 |
| [[Knowledge Graph]] + [[Entity Resolution]] + [[Neo4j]] | 图数据库 / 知识图谱实现层 | 需要显式实体、关系、Cypher / 图遍历、向量 + 全文 + 图组合 | Neo4j 是实现生态，不是 GraphRAG 定义本身；构图质量需看 [[Graph Construction Evaluation]] |
| [[Agentic Retrieval]] | 检索层 query planning / query execution control | 复杂企业搜索、多源检索、子问题分解 | 更偏 retrieval 层，不等于完整 Agentic RAG；边界见 [[Query Rewrite Query Planning Agentic Retrieval 对比]] |
| [[Parallel Search and Explicit Merging 检索模式]] | retrieval-during-reasoning 的多 query 执行与证据合并 | 多跳 QA、复杂研究、证据分散且单 query 覆盖不足 | 并行检索必须配合 merge、trace、budget 和 evaluation；不等于 Hybrid Search 或 Reranking |
| [[Agentic RAG]] | Agent 决定何时查、查哪里、是否重查 | 多步骤研究、多源比较、需要计划和回退 | 需要 trace、预算和 evaluation 约束 |
| [[Corrective RAG]] | 检索后证据质量门 | 坏检索代价高，需要判断证据够不够 | evaluator 错误会导致错杀或过度补救 |
| [[Self-RAG]] | 生成时自适应检索/批判 | 研究 self-reflection / adaptive retrieval 论文线 | prompt 模拟不等于论文训练机制 |

## 边界判断

- [[RAG]] 不是 [[Memory]] 的全部：RAG 偏外部知识检索；memory 还包括用户偏好、任务状态、历史轨迹、反思和遗忘策略。
- [[RAG]] 不是 [[Context Engineering]] 的全部：RAG 找资料；context engineering 决定哪些资料、工具结果、memory、trace 摘要和安全规则进入本轮上下文。
- [[Vector Database]] 不是 RAG：向量库只是存储和搜索 embedding 的基础设施；没有 ingestion、retrieval、rerank、citation 和 evaluation，仍然可能只是一个相似度 demo。
- [[GraphRAG]] 不是 [[Neo4j]]：GraphRAG 是图结构参与检索和上下文构造的模式；Neo4j 是常见图数据库和工程生态。
- [[Agentic RAG]] 不是“所有 RAG 都加 Agent”：只有当系统会计划、选择知识源、重查、评价证据或多步综合时，才值得进入 agentic 边界。
- RAG 不是事实正确性保险：资料可能错、检索可能漏、排序可能错、模型可能误读、引用可能不支持结论。

## 失败诊断路径

| 症状 | 优先检查 | 不要急着做什么 |
|---|---|---|
| 回答缺关键事实 | [[Document Ingestion]], [[Chunking]], [[Retriever]] 的召回样本 | 不要先换更大模型 |
| 检到相关文档但答错 | [[Context Engineering]], [[RAG Evaluation]] 的 faithfulness / citation 检查 | 不要只扩大 top-k |
| 专有名词、函数名、错误码找不到 | [[Sparse Retrieval]]、[[BM25]]、[[Hybrid Search]]、metadata filter、关键词/全文索引 | 不要只调 embedding 相似度 |
| 正确文档在候选里但没进 prompt | [[Reranking]]、去重、上下文预算 | 不要把所有候选都塞进长上下文 |
| 多跳关系或实体关联答不好 | [[Knowledge Graph]], [[GraphRAG]], [[Neo4j]] | 不要假设图数据库自动变准 |
| 答案引用不支持结论 | [[RAG Evaluation]]、citation 检查、人工抽样 | 不要只看最终答案是否流畅 |
| 检索资料含恶意指令 | [[Indirect Prompt Injection]], [[Prompt Injection]], [[Guardrails]] | 不要把检索内容当系统指令 |
| 用户看到不该看的资料 | 权限 metadata、检索前过滤、审计日志 | 不要只在生成后做遮盖 |

## 什么时候先不要上复杂 RAG

- 资料集很小、稳定且可以直接放入上下文时，先用清晰的 [[Context Engineering]]。
- 只是 FAQ 或单文档问答时，先做基础 [[RAG]] + 引用 + [[RAG Evaluation]]。
- 检索质量尚未评估时，先补 [[Retrieval 组件对比]] 里的 pipeline 可观测性；不要直接上 [[Agentic RAG]]。
- 没有实体/关系质量要求时，先不要引入 [[Knowledge Graph]] / [[GraphRAG]]，否则构图、去重和查询成本可能大于收益。
- 没有 trace、预算和失败样本时，先不要让 Agent 多轮自主检索；复杂 loop 会让错误更难复现。

## 概念卡

```dataview
TABLE status, updated, related
FROM "wiki/concepts"
WHERE contains(topic, "rag")
SORT file.name ASC
```

## 已完成概念入口

- [x] [[RAG]]
- [x] [[Parametric Memory]] / [[Non-Parametric Memory]]
- [x] [[Document Ingestion]]
- [x] [[Chunking]]
- [x] [[Parent-Child Chunking]]
- [x] [[Embedding]]
- [x] [[Dense Retrieval]]
- [x] [[TF-IDF]]
- [x] [[Sparse Retrieval]]
- [x] [[BM25]]
- [x] [[Vector Database]]
- [x] [[Retriever]]
- [x] [[Top-K]]
- [x] [[Multi-Route Retrieval]]
- [x] [[Multi-Query Retrieval]]
- [x] [[Reciprocal Rank Fusion]]
- [x] [[Hybrid Search]]
- [x] [[Reranking]]
- [x] [[Cross-Encoder]]
- [x] [[RAG Evaluation]]
- [x] [[Context Recall]] / [[Context Precision]]
- [x] [[RAG 类型对比]]
- [x] [[Retrieval 组件对比]]
- [x] [[常用向量数据库对比]]
- [x] [[Context RAG Memory 对比]]
- [x] [[Knowledge Graph]]
- [x] [[GraphRAG]]
- [x] [[Neo4j]]
- [x] [[Agentic RAG]] / [[Agentic Retrieval]]
- [x] [[Corrective RAG]] / [[Self-RAG]]
- [x] [[RAGGraph]]
- [x] [[RAG Citation Faithfulness]]
- [x] [[RAG Access Control]]
- [x] [[Query Rewrite]] / [[Query Planning]]
- [x] [[Graph Construction Evaluation]] / [[Entity Resolution]]
- [x] [[RAG 可靠性与治理对比]]
- [x] [[Query Rewrite Query Planning Agentic Retrieval 对比]]
- [x] [[Parallel Search and Explicit Merging 检索模式]]
- [x] [[GraphRAG 构图与评估对比]]

## 下一批概念 / 问题

- [ ] RAG 权限评估样本：是否需要给 [[RAG Access Control]] 建一个最小测试集模板？
- [ ] Citation faithfulness judge：LLM-as-judge、规则检查和人工抽样如何组合？
- [ ] GraphRAG 构图指标：是否需要把 entity/relation precision/recall、coverage、downstream answer gain 拆成评估模板？

## 关键边界

RAG 能让 LLM 使用外部资料，但不能保证资料完整、检索正确、证据充分或模型解释无误。

另一个重要边界：[[Knowledge Graph]] / [[Neo4j]] 是 GraphRAG 的图结构和工程实现线索，不是和 [[Self-RAG]]、[[Corrective RAG]] 平级的 RAG 方法名。[[Neo4j]] 是工具生态；[[GraphRAG]] 是图结构参与检索和上下文构造的模式。

## 证据锚点

- Concept anchors: [[RAG#证据锚点]], [[Retriever#证据锚点]], [[Top-K#证据锚点]], [[Multi-Route Retrieval#证据锚点]], [[Query Rewrite#证据锚点]], [[Query Planning#证据锚点]], [[Document Ingestion#证据锚点]], [[Chunking#证据锚点]], [[Embedding#证据锚点]], [[Dense Retrieval#证据锚点]], [[TF-IDF#证据锚点]], [[Sparse Retrieval#证据锚点]], [[BM25#证据锚点]], [[Vector Database#证据锚点]], [[Hybrid Search#证据锚点]], [[Reranking#证据锚点]], [[Cross-Encoder#证据锚点]], [[RAG Evaluation#证据锚点]], [[Context Recall#证据锚点]], [[Context Precision#证据锚点]], [[RAG Citation Faithfulness#证据锚点]], [[RAG Access Control#证据锚点]], [[Knowledge Graph#证据锚点]], [[Entity Resolution#证据锚点]], [[Graph Construction Evaluation#证据锚点]], [[GraphRAG#证据锚点]], [[Neo4j#证据锚点]]。
- Topic anchors: [[Retrieval 组件对比#证据锚点]], [[RAG 类型对比#证据锚点]], [[Context RAG Memory 对比#证据锚点]], [[Evaluation 层次对比#RAG Evaluation vs Trajectory Evaluation]]。
- Source examples: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]], [[Microsoft RAG 官方文档]], [[Neo4j GraphRAG 官方文档]], [[Azure AI Search Agentic Retrieval]], [[Corrective Retrieval Augmented Generation]], [[Self-RAG - Learning to Retrieve Generate and Critique]], [[Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging]]。
- Evidence type: 本页是 topic map 综合；稳定定义来自概念卡和 source note，诊断表和选型判断属于工程综合 / inference。

## 复习触发

1. 一个 RAG 答案错了，你如何按 ingestion、chunking、retrieval、reranking、context、generation、evaluation 分层排查？
2. 为什么有 [[Vector Database]] 不等于有可靠 [[RAG]]？
3. [[Hybrid Search]] 和 [[Reranking]] 分别解决召回和排序里的什么问题？
4. [[Multi-Route Retrieval]] 为什么不等于简单调大 Top-K 或只做 Hybrid Search？
5. 什么时候 [[Knowledge Graph]] / [[GraphRAG]] 值得引入，什么时候只是增加复杂度？
6. [[RAG]]、[[Memory]]、[[Context Engineering]] 三者都给模型提供信息，它们的最小边界是什么？
7. 如果检索内容里含有 prompt injection，RAG pipeline 应该在哪些点防护？

## 相关链接

- [[Agent 知识地图]]
- [[RAG]]
- [[TF-IDF]]
- [[Sparse Retrieval]]
- [[BM25]]
- [[Multi-Route Retrieval]]
- [[RAG 类型对比]]
- [[Retrieval 组件对比]]
- [[常用向量数据库对比]]
- [[Context RAG Memory 对比]]
- [[RAG Evaluation]]
- [[RAG Citation Faithfulness]]
- [[RAG Access Control]]
- [[RAG 可靠性与治理对比]]
- [[Query Rewrite]]
- [[Query Planning]]
- [[Query Rewrite Query Planning Agentic Retrieval 对比]]
- [[Parallel Search and Explicit Merging 检索模式]]
- [[Graph Construction Evaluation]]
- [[Entity Resolution]]
- [[GraphRAG 构图与评估对比]]
- [[GraphRAG]]
- [[Knowledge Graph]]
- [[Neo4j]]
- [[Obsidian + LLM Wiki]]
