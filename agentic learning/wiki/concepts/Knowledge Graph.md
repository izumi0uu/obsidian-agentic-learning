---
type: concept
topic:
  - rag
  - graph
  - knowledge-base
status: growing
created: 2026-05-12
updated: 2026-05-16
last_checked: 2026-05-12
freshness: watch
source:
  - "[[Neo4j GraphRAG 官方文档]]"
  - "[[GraphRAG]]"
  - "[[Neo4j]]"
  - "[[RAG 类型对比]]"
evidence:
  - "[[Neo4j GraphRAG 官方文档#为什么收]]"
  - "[[Neo4j GraphRAG 官方文档#一句话]]"
  - "[[Neo4j GraphRAG 官方文档#边界提醒]]"
  - "[[GraphRAG#证据锚点]]"
  - "[[Neo4j#证据锚点]]"
  - "[[RAG 类型对比#核心区别表]]"
related:
  - "[[RAG]]"
  - "[[GraphRAG]]"
  - "[[Neo4j]]"
  - "[[Retriever]]"
  - "[[Vector Database]]"
  - "[[Hybrid Search]]"
---

# Knowledge Graph

## 一句话

Knowledge Graph 是把实体和实体之间的关系显式组织成图结构的知识表示方式；在 RAG 里，它常用于让检索利用关系、多跳路径和结构化查询，而不只依赖文本相似度。

## 概念详解

Knowledge Graph 出现，是因为很多知识不是孤立段落，而是对象之间的关系：人物属于团队，论文提出方法，项目使用框架，疾病有症状，公司拥有产品。普通向量检索擅长找“文本语义相似”的 chunk，但不天然保存这些实体关系、路径和约束。Knowledge Graph 把知识拆成节点和边，让系统可以围绕实体、关系、路径、社区或结构化查询组织上下文。

在 RAG 语境里，Knowledge Graph 的价值通常体现在 [[GraphRAG]]：先从文档中抽取实体、关系、事件或主题，把它们与原始 chunk / source 连接起来；查询时再结合向量检索、全文检索、图遍历或 Cypher 等结构化查询，把关系上下文带给生成模型。[[Neo4j GraphRAG 官方文档]] 的 source note 明确把 Neo4j 放在知识图谱、向量搜索、全文搜索和图遍历增强 RAG 的工程实现线上；[[Neo4j]] 概念卡也强调它是 GraphRAG 的实现生态，而不是 GraphRAG 本身。

证据边界：source notes 支持 Knowledge Graph 在 GraphRAG / Neo4j 生态中的工程位置；本卡把它抽象成学习概念，用来区分“图结构知识表示”和“向量相似检索”。具体图 schema、实体抽取算法、Text2Cypher、社区检测和图数据库 API 属于易变实现细节，需要按具体文档复查。

在 RAG 学习里，Knowledge Graph 的关键不是“用了图数据库”，而是知识被组织成可追踪的实体、关系、属性和来源。它能支持多跳关系、实体中心检索、社区/路径摘要和结构化约束，但构图成本、schema 设计和更新维护都很高。现代 GraphRAG 会把 graph 与 dense/sparse retrieval 组合，而不是把所有文本都强行变成图。
## 它解决什么问题

它解决“关系型知识不容易靠相似文本检索表达”的问题。比如：

- 多个文档里提到同一个实体，但名称、别名或上下文不同。
- 问题需要跨实体关系做多跳推理。
- 需要按组织、时间、项目、人物、依赖关系等结构过滤或扩展上下文。
- 需要把 chunk 与 source、实体、关系和权限一起管理。

## 它不是什么

Knowledge Graph 不是 [[RAG]] 本身。它可以作为 RAG 的外部知识结构之一，但没有生成和证据使用流程时，只是一个知识表示 / 查询层。

Knowledge Graph 也不是 [[Vector Database]]。向量库主要处理 embedding 相似搜索；知识图谱主要处理实体和关系。现代系统可以把二者结合，例如图节点带向量索引，或者先向量召回再图遍历扩展。

Knowledge Graph 也不是自动真理库。实体抽取、关系抽取、去重、schema 设计和来源追踪都可能出错。

## 最小例子

```text
文档："Alice 在 Project X 中使用 LangGraph 构建客服 Agent。"

节点：Alice、Project X、LangGraph、客服 Agent
关系：Alice --参与--> Project X
     Project X --使用--> LangGraph
     Project X --构建--> 客服 Agent
```

RAG 查询“Project X 依赖哪些 Agent framework？”时，系统可以先找到 Project X 节点，再沿关系找到 LangGraph 和相关 source chunk，最后让模型基于证据回答。

## 常见误解 / 风险

- 误解：有知识图谱就一定比向量 RAG 准。图谱质量差时，关系错误会被系统放大。
- 误解：用了 [[Neo4j]] 就自动拥有 GraphRAG 能力。关键要看检索是否真的使用了实体关系和图遍历。
- 误解：LLM 自动抽图可以替代 schema 设计。实际仍要处理实体规范化、别名、关系类型、去重和来源。
- 风险：图构建成本高，简单 FAQ 或小语料可能不值得。
- 风险：图遍历扩展太宽会引入噪音，污染上下文。
- 风险：结构化查询或 Text2Cypher 如果权限不受限，可能暴露不该查询的数据。

## 边界细节

和 [[GraphRAG]] 的边界：Knowledge Graph 是图结构知识表示；GraphRAG 是让图结构参与检索和生成的 RAG 模式。

和 [[Neo4j]] 的边界：Neo4j 是图数据库和 GraphRAG 工程生态；Knowledge Graph 是更通用的知识结构概念。

和 [[Hybrid Search]] 的边界：Hybrid Search 解决向量和关键词/全文信号互补；Knowledge Graph 解决实体关系、路径和结构约束。

和 [[Retriever]] 的边界：retriever 可以调用知识图谱作为一个知识源，也可以只调用向量库或全文索引。知识图谱不是 retriever 的全部。

## 现代性状态

- 判定：foundation / current-practice / frontier-watch。
- 稳定部分：用节点和边表达实体关系，是知识表示的基础思想；在 GraphRAG 中，它能补足纯向量检索的关系结构弱点。
- 当前工程实践：Neo4j 等图数据库、向量索引、全文索引和 LLM 抽图工具正在把 knowledge graph 纳入 RAG pipeline。
- 易变部分：自动构图、关系抽取、Text2Cypher、图社区摘要、GraphRAG package、评估方法和托管产品 API。
- 复查点：当 GraphRAG 文档更新时，优先检查“图结构如何参与检索”和“实体/关系质量如何评估”，不要只记录产品功能。

## 现代系统怎么吸收 Knowledge Graph 的价值 / 局限

现代 RAG 系统通常不会用 Knowledge Graph 替代全部检索，而是把它作为 retrieval strategy 的一层：向量检索找语义入口，全文检索补精确匹配，图遍历扩展关系上下文，reranking 和 RAG Evaluation 再检查证据是否真的支持答案。

它的价值是关系结构、实体对齐和多跳上下文；局限是构图成本、抽取错误、schema 维护、查询权限和图扩展噪音。可靠系统要把图中每个关系尽量回链到 source chunk，而不是让图谱成为无来源的“第二个幻觉层”。

## 证据锚点

- Source: [[Neo4j GraphRAG 官方文档]]
- Anchor: [[Neo4j GraphRAG 官方文档#为什么收]]
- Anchor: [[Neo4j GraphRAG 官方文档#一句话]]
- Anchor: [[Neo4j GraphRAG 官方文档#边界提醒]]
- Concept anchor: [[GraphRAG#证据锚点]]
- Concept anchor: [[Neo4j#证据锚点]]
- Topic anchor: [[RAG 类型对比#核心区别表]]
- Evidence type: official docs source note + existing concept-card synthesis + engineering synthesis.
- Boundary: 本卡不声称某个具体图数据库、抽图工具或 Text2Cypher 实现代表 Knowledge Graph 的全部。

## 复习触发

1. 为什么 Knowledge Graph 解决的是“关系结构”问题，而不是普通向量相似度问题？
2. [[Knowledge Graph]]、[[GraphRAG]] 和 [[Neo4j]] 三者分别在哪一层？
3. 如果 LLM 自动抽出的实体关系有错，RAG 答案会发生什么？
4. 什么时候普通 [[Hybrid Search]] + [[Reranking]] 可能比 GraphRAG 更合适？

## 相关链接

- [[RAG]]
- [[RAG 主题]]
- [[RAG 类型对比]]
- [[Retrieval 组件对比]]
- [[GraphRAG]]
- [[Neo4j]]
- [[Retriever]]
- [[Vector Database]]
- [[Hybrid Search]]
