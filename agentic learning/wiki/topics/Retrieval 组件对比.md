---
type: map
topic:
  - rag
  - retrieval
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-16
source:
  - "[[Retriever]]"
  - "[[Hybrid Search]]"
  - "[[Reranking]]"
  - "[[Vector Database]]"
  - "[[Embedding]]"
  - "[[TF-IDF]]"
  - "[[Sparse Retrieval]]"
  - "[[BM25]]"
  - "[[Multi-Route Retrieval]]"
  - "[[Document Ingestion]]"
  - "[[RAG]]"
  - "[[Microsoft RAG 官方文档]]"
  - "[[Agent 工程基础设施主源]]"
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]"
  - "[[Dense Retrieval]]"
  - "[[Multi-Query Retrieval]]"
  - "[[Reciprocal Rank Fusion]]"
  - "[[Cross-Encoder]]"
  - "[[Parent-Child Chunking]]"
evidence:
  - "[[Retriever#证据锚点]]"
  - "[[Hybrid Search#证据锚点]]"
  - "[[Reranking#证据锚点]]"
  - "[[Vector Database#证据锚点]]"
  - "[[Embedding#证据锚点]]"
  - "[[TF-IDF#证据锚点]]"
  - "[[Sparse Retrieval#证据锚点]]"
  - "[[BM25#证据锚点]]"
  - "[[Multi-Route Retrieval#证据锚点]]"
  - "[[Document Ingestion#证据锚点]]"
  - "[[RAG#证据锚点]]"
  - "[[Dense Retrieval#证据锚点]]"
  - "[[Multi-Query Retrieval#证据锚点]]"
  - "[[Reciprocal Rank Fusion#证据锚点]]"
  - "[[Cross-Encoder#证据锚点]]"
  - "[[Parent-Child Chunking#证据锚点]]"
related:
  - "[[RAG 主题]]"
  - "[[RAG 类型对比]]"
  - "[[Context RAG Memory 对比]]"
  - "[[RAG Evaluation]]"
  - "[[常用向量数据库对比]]"
  - "[[TF-IDF]]"
  - "[[Sparse Retrieval]]"
  - "[[BM25]]"
  - "[[Multi-Route Retrieval]]"
  - "[[Dense Retrieval]]"
  - "[[Multi-Query Retrieval]]"
  - "[[Reciprocal Rank Fusion]]"
  - "[[Cross-Encoder]]"
  - "[[Parent-Child Chunking]]"
---

# Retrieval 组件对比

## 一句话总览

这页回答：Retrieval 链路里的 Document Ingestion、Chunking/Parent-Child Chunking、Embedding/Dense Retrieval、TF-IDF、Sparse Retrieval、BM25、Vector Database、Retriever、Multi-Route Retrieval、Hybrid Search、Reranking 分别负责什么。

最小边界：[[Document Ingestion]] 决定资料怎样进库；[[Embedding]] 把内容变成语义向量；[[Dense Retrieval]] 用向量相似度召回；[[TF-IDF]] 帮你理解稀疏词项权重；[[Sparse Retrieval]] 是词法/稀疏检索家族；[[BM25]] 是常见关键词检索打分代表；[[Vector Database]] 存和搜向量；[[Retriever]] 从索引里找候选；[[Multi-Route Retrieval]] 组织多条召回路线并融合候选；[[Multi-Query Retrieval]] 扩展 query 视角；[[Reciprocal Rank Fusion]] 融合多路排序；[[Hybrid Search]] 把向量和关键词/全文信号结合；[[Reranking]] 在候选集上重新排序，[[Cross-Encoder]] 是常见精排结构。它们共同服务 [[RAG]]，但没有一个单独等于 RAG 本身。

## 为什么这组值得对比

- 混淆风险：很多 RAG 失败被笼统归因成“向量库不好”或“模型幻觉”，实际可能出在 ingestion、chunk、embedding、召回、融合、rerank 或上下文组织。
- 共同问题域：它们都影响外部资料能否被找到、排序、引用并送入模型上下文。
- 不同介入点：有的是离线入库，有的是在线召回，有的是基础设施，有的是排序质量层。
- 证据密度：相关概念卡均已有 source note 和工程综合锚点，[[RAG 类型对比]] 也已沉淀部分 retrieval 边界。
- 复习价值：能帮助排查 RAG pipeline，而不是一遇到错误就换模型或加更复杂的 Agent loop。

边界：本页比较 retrieval 组件，不比较 GraphRAG、Agentic RAG、Corrective RAG 等 RAG 类型；那些属于 [[RAG 类型对比]]。

## 共同问题域

共同问题是：外部资料必须先被整理成可检索单元，再通过合适的检索策略找回，并把最有用的证据排到上下文预算前面。

```text
raw docs
  -> Document Ingestion
  -> chunk + metadata
  -> Embedding / sparse features ([[TF-IDF]] / [[BM25]])
  -> Vector Database / search index
  -> Retriever
  -> Multi-Route Retrieval / Hybrid Search / filters
  -> Reranking
  -> context for generation
```

这条链路里，上游质量会限制下游上限：ingestion 丢掉表格结构，embedding 和 reranking 都无法恢复；初召回没有命中正确证据，reranker 只能在错误候选里排序。

## 核心区别表

| 概念 | 介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[Document Ingestion]] | 原始资料进入知识库的入口流程 | 离线或增量更新时 | PDF、网页、表格、代码、图片说明、权限信息 | 清洗后的文本、结构、metadata、待切分资料 | [[Document Ingestion#证据锚点]] |
| [[Embedding]] | 语义表示 | 入库时给 chunk 向量；查询时给 query 向量 | chunk、query、文本/图片对象 | 向量，用于相似度搜索 | [[Embedding#证据锚点]] |
| [[Dense Retrieval]] | 稠密向量召回路线 | 查询时用 query embedding 搜索近邻 chunk | query embedding、chunk embeddings、向量索引 | 语义相似候选 | [[Dense Retrieval#证据锚点]] |
| [[TF-IDF]] | 稀疏词项权重表示 | 入库/索引时建立词表和权重；查询时按词面匹配打分 | 文档、query、词表、语料统计 | sparse vector / TF-IDF feature matrix | [[TF-IDF#证据锚点]] |
| [[Sparse Retrieval]] | 稀疏/词法检索家族 | 建倒排或稀疏索引；查询时按词项命中召回 | query 词项、文档词项、索引、分词规则 | 精确词面匹配候选 | [[Sparse Retrieval#证据锚点]] |
| [[BM25]] | 关键词检索打分代表 | 查询时对词面命中的文档或 chunk 排序 | query 词项、文档词频、文档频率、长度信息 | BM25 排序候选 | [[BM25#证据锚点]] |
| [[Vector Database]] | 向量存储与近似搜索基础设施 | 入库后保存，查询时 top-k 搜索 | embedding、metadata、过滤条件 | 相似向量候选、metadata | [[Vector Database#证据锚点]] |
| [[Retriever]] | 找候选证据的组件或流程 | 生成前，可在 agentic loop 中多次调用 | query、索引、权限/filter、retrieval strategy | candidate passages / chunks / records | [[Retriever#证据锚点]] |
| [[Multi-Route Retrieval]] | 多路线候选召回与粗融合 | retrieve 阶段并行多路执行，rerank 前合并 | query、多 query 变体、dense/sparse/graph/filter route、多个索引 | 合并去重后的候选集合 | [[Multi-Route Retrieval#证据锚点]] |
| [[Multi-Query Retrieval]] | 多查询扩展召回 | 检索前生成多个 query，分别检索后合并 | 原始问题、query 变体、检索器 | 多组候选结果 | [[Multi-Query Retrieval#证据锚点]] |
| [[Reciprocal Rank Fusion]] | 多路排名融合 | 多路候选出来后、rerank 前 | 多个排序列表 | 统一粗排序候选 | [[Reciprocal Rank Fusion#证据锚点]] |
| [[Hybrid Search]] | 向量语义检索 + 关键词/全文检索融合 | retrieve 阶段并行或融合 | query、embedding、关键词、metadata filter | 语义与精确匹配互补的候选集合 | [[Hybrid Search#证据锚点]] |
| [[Reranking]] | 初检候选的精排 | retrieve 后、上下文生成前 | query、候选 chunks、业务权重或 reranker 模型 | 更适合放入上下文的排序结果 | [[Reranking#证据锚点]] |
| [[Cross-Encoder]] | 常见 reranker 结构 | rerank 小候选集时 | query + chunk pair | 相关性分数 | [[Cross-Encoder#证据锚点]] |

## 最容易混淆的边界

### Document Ingestion vs Vector Database

[[Document Ingestion]] 负责资料进入系统前后的解析、清洗、去重、metadata、权限、版本和质量检查。[[Vector Database]] 负责保存和搜索向量。

如果 PDF 表格被解析错、网页混入导航噪音、权限标签丢失，换向量库通常无法解决根因。向量库只能检索已经写进去的表示，不能自动修复脏 ingestion。

### Embedding vs Retriever

[[Embedding]] 是 dense 语义表示方法：把 query 和 chunk 变成可比较的稠密向量。[[TF-IDF]] 是 sparse 词法表示的学习入口；[[Sparse Retrieval]] 是词面检索家族；[[BM25]] 是常见关键词检索打分代表。[[Retriever]] 是组件或流程：用 embedding、关键词、metadata filter、权限规则、hybrid search 等手段找候选资料。

纯向量相似只是 retriever 的一种策略。现代 retriever 可能包含 query rewrite、metadata filter、全文检索、hybrid search、去重、权限过滤和 reranking。

### Vector Database vs RAG

[[Vector Database]] 是 retrieval infrastructure；[[RAG]] 是检索增强生成的架构模式。一个系统可以有向量库但没有可靠 RAG，例如没有 citation、没有 chunk metadata、没有权限同步、没有 rerank 或评估。

反过来，RAG 也不一定只靠向量库；[[Sparse Retrieval]]、[[BM25]] / 全文检索、hybrid search、知识图谱和 SQL 数据库都可能成为外部知识来源。

### Hybrid Search vs Reranking

[[Hybrid Search]] 增加召回信号：用语义检索和 [[Sparse Retrieval]] / [[BM25]] / 全文检索互补，避免漏掉专有名词、编号、代码符号或同义表达。

[[Reranking]] 提升候选排序：在已经召回的一批候选上，用更精细模型或规则重新判断相关性。它不能凭空创造未召回的正确证据。

### Multi-Route Retrieval vs Hybrid Search

[[Multi-Route Retrieval]] 是更宽的召回组织模式：可以同时用向量、BM25、多 Query、图检索、metadata filter、不同索引粒度或多个 retriever 召回候选，再做去重和融合。

[[Hybrid Search]] 是其中最常见的稳定形态之一，通常强调 dense/vector 与 sparse/BM25/全文信号互补。不要把“多路召回”自动等同为 Hybrid Search，否则会漏掉多 Query 扩展、图路线和多源 retriever 的设计空间。

## 执行时序 / 机制差异

```text
Offline / ingestion time:
  source -> parse/clean -> metadata/permissions -> chunk -> embedding + sparse index -> vector db / search index

Online / query time:
  query -> query embedding / rewrite -> vector search + BM25/sparse keyword search + optional multi-query route -> merge/filter -> rerank -> context

Failure diagnosis:
  bad source parse? -> ingestion
  answer split from condition? -> chunking
  semantic miss? -> embedding/retriever
  exact entity miss? -> sparse retrieval / BM25 / hybrid search
  right doc low rank? -> reranking
  right evidence not used? -> context engineering / generation / evaluation
```

这组机制差异的价值在于排错：不要用下游组件掩盖上游数据质量问题，也不要用复杂 Agent loop 替代基本 retrieval 评估。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文或官方文档证据。

把 retrieval 想成整理和查找一座资料馆：

| 概念 | 类比 | 类比边界 |
|---|---|---|
| [[Document Ingestion]] | 把新书拆封、登记、去重、贴标签、放进馆藏系统 | 整理错了，后面很难找对 |
| [[Embedding]] | 给每段内容生成“语义坐标” | 坐标相近不等于答案正确 |
| [[Dense Retrieval]] | 按语义坐标找近邻片段 | 不是整个 retriever，也不保精确词 |
| [[TF-IDF]] | 给每段内容做关键词权重索引 | 词面命中强，不等于理解同义表达 |
| [[Sparse Retrieval]] | 按词面、编号、代码符号和倒排索引找资料 | 不是语义理解，也不是只等于 TF-IDF |
| [[BM25]] | 给关键词命中的资料做更稳的相关性排序 | 是 sparse retrieval 的代表，不是整个检索系统 |
| [[Vector Database]] | 存这些语义坐标并快速找近邻的柜子 | 柜子不是整座图书馆服务 |
| [[Retriever]] | 按问题找一批可能有用的资料 | 找到候选不等于最终答案 |
| [[Multi-Route Retrieval]] | 同时走多条查找路线再合并候选 | 路线越多，越需要去重、融合、trace 和评估 |
| [[Multi-Query Retrieval]] | 同一个问题换多个问法去查 | 原始 query 要保留，避免改写偏题 |
| [[Reciprocal Rank Fusion]] | 把多路排名合成粗排序 | 不能创造未召回的证据 |
| [[Hybrid Search]] | 既按意思找，也按书名、编号、关键词找 | 融合策略需要调试 |
| [[Reranking]] | 从候选资料中重新排最该先读的 | 只能排已找到的资料 |
| [[Cross-Encoder]] | 把 query 和 chunk 放一起深度打分 | 精度高但慢，适合小候选集 |

## 现代系统如何吸收或限制

### 来源支持

- [[Document Ingestion]]、[[Chunking]]、[[Embedding]]、[[TF-IDF]]、[[Sparse Retrieval]]、[[BM25]] 支持：RAG 质量受资料入口、切分和表示限制；表示层既可能是 dense semantic vector，也可能是 sparse lexical / keyword signal。
- [[Retriever]]、[[Multi-Route Retrieval]]、[[Hybrid Search]]、[[Reranking]] 支持：检索质量可以拆成召回路线、融合和排序多个环节。
- [[Vector Database]] 支持：向量库是基础设施层，不等于完整 RAG。
- [[Microsoft RAG 官方文档]]、[[Agent 工程基础设施主源]] 和 [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]] 支持：现代 RAG 需要数据治理、索引、检索、生成和评估的组合。

### 工程综合 / inference

生产系统通常会把 retrieval 做成可观测 pipeline：记录 query rewrite、向量候选、关键词候选、filter 命中、合并去重、rerank 前后排序、进入上下文的最终 chunk 和引用。这样才能判断错误来自 ingestion、召回、排序、权限还是生成。

### 仍需警惕的外推

具体 embedding 模型、reranker、向量数据库和搜索产品能力变化较快。本页只保留稳定职责边界；选型和 API 细节应另行用最新官方文档复查。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| PDF 表格、网页结构、权限标签混乱 | [[Document Ingestion]] | 问题在资料进入系统前后的结构保真和治理 | 后续检索会在脏数据上工作 |
| 语义相近但不同措辞找不到 | [[Embedding]] / [[Retriever]] | 需要检查 query/chunk 表示和召回策略 | 语义相似仍可能找来无关资料 |
| 专有名词、编号、代码符号漏召回 | [[Sparse Retrieval]] / [[BM25]] / [[Hybrid Search]] | 需要稀疏词项或关键词/全文信号补足向量检索；[[TF-IDF]] 可作为理解词项权重的基础入口 | 分数融合和去重可能引入噪音 |
| 同一问题存在多种表述、多个来源或多种索引路线 | [[Multi-Route Retrieval]] | 需要同时覆盖 dense、sparse、多 Query、图路线或多源 retriever | 路线过多会增加成本、重复和融合调试难度 |
| 找到正确文档但排在很后 | [[Reranking]] | 候选已召回，但需要精排进入上下文预算 | 初召回缺证据时 rerank 无能为力 |
| 数据量、更新、metadata filter、权限要求上升 | [[Vector Database]] / search infra | 需要可靠索引、删除、过滤和多租户能力 | 基础设施升级不自动提升答案忠实性 |
| Agent/RAG 项目要选向量库 | [[常用向量数据库对比]] + [[Vector Database#Agent / RAG 选型边界]] | 先看现有后端/搜索栈、数据规模、QPS、metadata/权限、更新频率、hybrid search 和运维成本 | 把 Qdrant、pgvector、Chroma、FAISS、Milvus、Weaviate、Pinecone 当成同一层 vendor 排名，会忽略本地库、Postgres 扩展、专用服务、搜索系统和图数据库的层级差异 |
| 不知道 RAG 错在检索还是生成 | trace + [[RAG Evaluation]] | 需要分开看 retrieval ranking metrics（Hit@K / Recall@K / MRR / nDCG）、rerank、faithfulness、citation | 只看最终答案会误判根因 |

## 它们共同不是什么

- 都不是 [[RAG]] 的全部；RAG 还包括上下文组织、生成、引用、评估和治理。
- 都不是“防幻觉按钮”；检索链路错误会把坏上下文更稳定地送给模型。
- 都不是越复杂越好；更多检索器和 reranker 会增加延迟、成本和调试难度。
- 都不替代权限和 freshness 检查；找得到不代表有权使用或仍然有效。

## 证据锚点

- Concept anchors: [[Document Ingestion#证据锚点]], [[Embedding#证据锚点]], [[Dense Retrieval#证据锚点]], [[TF-IDF#证据锚点]], [[Sparse Retrieval#证据锚点]], [[BM25#证据锚点]], [[Vector Database#证据锚点]], [[Retriever#证据锚点]], [[Multi-Route Retrieval#证据锚点]], [[Multi-Query Retrieval#证据锚点]], [[Reciprocal Rank Fusion#证据锚点]], [[Hybrid Search#证据锚点]], [[Reranking#证据锚点]], [[Cross-Encoder#证据锚点]], [[RAG#证据锚点]]
- Topic anchor: [[RAG 类型对比#最容易混淆的边界]] / [[RAG 类型对比#证据锚点]]
- Source examples: [[Agent 工程基础设施主源]], [[Microsoft RAG 官方文档]], [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]
- Evidence type: concept-card synthesis + existing comparison topic + docs/paper/source-note evidence + engineering synthesis + learning analogy.
- Confidence: medium-high for component responsibility boundaries; medium for operational diagnosis table because实际系统会受语料、权限、产品能力和评测方法影响。
- Boundary: 本页没有证明某个具体向量库、embedding 模型或 reranker 最优；只沉淀 retrieval 组件层次。

## 复习触发

1. 为什么有 [[Vector Database]] 不等于有可靠 [[RAG]]？
2. [[Hybrid Search]] 和 [[Reranking]] 分别解决召回链路的哪一类问题？
3. [[Multi-Route Retrieval]] 和 [[Hybrid Search]] 的最小区别是什么？
4. 如果正确答案所在 PDF 表格被解析错，你会先检查哪个组件？为什么？
5. [[Embedding]] 和 [[Retriever]] 的边界是什么？
6. 初召回没有找到正确 chunk 时，为什么 [[Reranking]] 救不了？

## 相关链接

- [[Retriever]]
- [[Multi-Route Retrieval]]
- [[Hybrid Search]]
- [[Reranking]]
- [[Vector Database]]
- [[Embedding]]
- [[TF-IDF]]
- [[Sparse Retrieval]]
- [[BM25]]
- [[Document Ingestion]]
- [[Chunking]]
- [[RAG]]
- [[RAG 类型对比]]
- [[Context RAG Memory 对比]]
- [[RAG Evaluation]]
- [[LLM Wiki 工作流]]
- [[常用向量数据库对比]]
