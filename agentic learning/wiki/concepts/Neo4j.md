---
type: concept
topic:
  - rag
  - graph
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[Neo4j GraphRAG 官方文档]]"
  - "[[RAG 类型对比]]"
evidence:
  - "[[Neo4j GraphRAG 官方文档#为什么收]]"
  - "[[Neo4j GraphRAG 官方文档#一句话]]"
  - "[[Neo4j GraphRAG 官方文档#边界提醒]]"
  - "[[RAG 类型对比#一张表先抓住]]"
related:
  - "[[GraphRAG]]"
  - "[[RAG]]"
  - "[[Retriever]]"
  - "[[Agentic RAG]]"
---

# Neo4j

## 一句话

Neo4j 是一个图数据库和 GraphRAG 工程生态，常用来把文档、chunk、实体、关系、向量索引、全文索引和 Cypher 查询放到同一个可查询的知识图谱系统里。

## 概念详解

Neo4j 在本 vault 里不是一个新的 RAG 方法名，而是 [[GraphRAG]] 的重要工程实现生态。普通向量 RAG 主要根据文本相似度找 chunk；当问题依赖实体关系、多跳关联、结构化查询或图遍历时，图数据库可以把文档、chunk、实体、关系、事件和来源组织成可查询的关系网络。

[[Neo4j GraphRAG 官方文档]] 的 source note 说明，Neo4j GraphRAG 关注如何用 Neo4j 知识图谱、向量搜索、全文搜索和图遍历增强 RAG 的检索层。它还提到 GraphRAG Python Package、LLM Knowledge Graph Builder、vector index、fulltext search 和 Text2Cypher 等生态组件。这些能力说明 Neo4j 可以承载 GraphRAG pipeline 里的多个基础设施角色：存图、查图、做向量召回、做全文召回、沿关系扩展上下文。

边界非常重要：Neo4j 不等于 GraphRAG 本身。GraphRAG 是“图结构参与检索和上下文构造”的模式；Neo4j 是可用于实现它的工具生态。用了 Neo4j，也可能只是把 chunk 存进数据库而没有真正利用关系；不用 Neo4j，也可以用其他图数据库或自定义图结构实现 GraphRAG。

现代性上，Neo4j 属于 frontier/watch 的实现生态。图数据库概念稳定，但 Neo4j 的 GraphRAG package、LLM graph builder、集成框架、API 和最佳实践会变化。概念卡应该沉淀它在 RAG 知识体系里的层级位置，而不是追逐每个版本功能。

## 它解决什么问题

普通向量 RAG 主要靠“文本片段语义相似”找上下文，但很多问题真正依赖实体关系、多跳关联和结构化查询。

Neo4j 让 RAG 可以多一层图结构：用节点和关系保存实体、文档、chunk、事件、项目、人物等对象；用 Cypher 查询结构化关系；用向量索引做语义召回；用全文索引补关键词召回；用图遍历扩展相关上下文。

## 它不是什么

Neo4j 不是 [[GraphRAG]] 本身。

它也不是所有 RAG 系统的必选项。只有当问题真的需要关系结构、图遍历、实体级查询或知识图谱维护时，它才值得引入。

Neo4j 也不会自动保证抽取出的实体和关系是真的。LLM 抽图、schema 设计、去重、评估和引用校验仍然要单独处理。

## 最小例子

```text
PDF/网页 -> Document/Chunk 节点 -> 抽取 Entity/Relation -> 存 Neo4j
问题 -> 向量召回相关 Chunk -> Cypher 扩展实体关系 -> LLM 基于证据回答
```

这里 Neo4j 的价值不是“替模型回答”，而是保存和查询关系网络。

## 常见误解 / 风险

- 误解：用了 Neo4j 就是 GraphRAG。实际要看检索是否真的利用了图关系。
- 误解：LLM 自动抽图就能得到可靠知识图谱。实际需要 schema、去重、人工抽查和评估。
- 风险：图谱构建成本高，尤其是长文档、表格、图片和噪声资料。
- 风险：Text2Cypher 可能生成错误查询，必须限制权限并验证结果。
- 风险：关系扩展太多会让上下文变脏，答案反而更差。

## 边界细节

Neo4j 应该放在 GraphRAG 工程实现层，而不是和 [[Self-RAG]]、[[Corrective RAG]] 平级的方法层。

和 [[Vector Database]] 的边界：vector database 偏语义向量召回；Neo4j 可以同时承载图关系、向量索引和全文索引，但它的差异点在关系结构。

和 [[GraphRAG]] 的边界：GraphRAG 是模式；Neo4j 是实现生态。

## 现代性状态

- 判定：frontier / current-practice implementation ecosystem。
- 稳定部分：图数据库可用于关系型检索、图遍历和 GraphRAG 实现。
- 易变部分：Neo4j GraphRAG package、LLM Knowledge Graph Builder、Text2Cypher、框架集成和产品 API。
- freshness: watch。
- last_checked: 2026-05-10。
- 复查点：Neo4j 文档更新时，优先更新 source note；概念卡保留“实现生态，不等于方法定义”的边界。

## 现代系统怎么吸收 Neo4j 的价值

现代系统会在需要关系推理时引入 Neo4j：先设计 schema 和抽取规则，再把图查询、向量召回、全文检索和 answer generation 接到同一 trace。关键验收不是“是否用了 Neo4j”，而是关系检索是否提升了可验证答案。

## 证据锚点

- Source: [[Neo4j GraphRAG 官方文档]]
- Anchor: [[Neo4j GraphRAG 官方文档#为什么收]]
- Anchor: [[Neo4j GraphRAG 官方文档#一句话]]
- Anchor: [[Neo4j GraphRAG 官方文档#边界提醒]]
- Source: [[RAG 类型对比]]
- Anchor: [[RAG 类型对比#一张表先抓住]]
- Evidence type: official docs source note + local comparison map + engineering synthesis.
- Confidence: medium
- Boundary: Neo4j source supports Neo4j as GraphRAG implementation ecosystem; it does not redefine GraphRAG itself, and specific package/API details are volatile.

## 复习触发

- 为什么 Neo4j 不是 GraphRAG 本身？
- 什么样的问题值得付出构图成本？
- 用 Neo4j 做 GraphRAG 时，哪些失败来自图谱质量而不是 LLM？

## 相关链接

- [[GraphRAG]]
- [[RAG]]
- [[Retriever]]
- [[RAG 类型对比]]
- [[Neo4j GraphRAG 官方文档]]
