---
type: concept
topic:
  - rag
  - frontier
  - graph
status: growing
created: 2026-05-05
updated: 2026-05-16
up:
  - "[[RAG]]"
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[前沿主源清单]]"
  - "[[Neo4j GraphRAG 官方文档]]"
  - "[[RAG 类型对比]]"
evidence:
  - "[[前沿主源清单#RAG 进化]]"
  - "[[Neo4j GraphRAG 官方文档#为什么收]]"
  - "[[Neo4j GraphRAG 官方文档#一句话]]"
  - "[[Neo4j GraphRAG 官方文档#边界提醒]]"
  - "[[RAG 类型对比#一张表先抓住]]"
related:
  - "[[RAG]]"
  - "[[Memory]]"
  - "[[Evaluation]]"
  - "[[RAG 类型对比]]"
  - "[[Neo4j]]"
---

# GraphRAG

## 一句话

GraphRAG 是用图结构增强 RAG 的方法，让实体、关系、社区或知识图谱参与检索和回答。

## 概念详解

GraphRAG 解决的是普通向量 RAG 在“关系型问题”上的弱点。向量检索擅长找语义相似片段，但很多问题需要知道实体之间的关系、跨文档的多跳连接、组织结构、人物和项目的关联，或者一个主题的全局社区结构。GraphRAG 试图让检索不只问“哪段文本和 query 最像”，还问“哪些实体、关系、路径或社区和这个问题有关”。

典型 GraphRAG 会先从文档中抽取实体、关系、事件或主题，把它们组织成知识图谱，再在检索时结合向量搜索、全文搜索、图遍历、社区摘要或结构化查询。[[Neo4j GraphRAG 官方文档]] 给出的是工程实现视角：Neo4j 可以把知识图谱、向量索引、全文搜索、Cypher、图遍历和 LLM Knowledge Graph Builder 放在同一生态里。但这说明的是一种实现路线，不等于 GraphRAG 的全部定义。

GraphRAG 的关键边界是“图是否真的参与检索和上下文构造”。如果只是把 RAG pipeline 画成一个 DAG，那更接近 [[RAGGraph]] 或 workflow graph；如果只是把文档存在图数据库里，但检索仍然只做普通向量 top-k，也不能说明系统获得了 GraphRAG 的关系检索价值。反过来，GraphRAG 也不必等同于某个数据库产品；[[Neo4j]] 是重要工程生态，但不是 GraphRAG 本身。

现代性上，GraphRAG 属于 current-practice / frontier。图增强检索的动机相对稳定：解决多跳关系、实体关联和全局总结；但构图质量、schema 设计、自动实体抽取、Text2Cypher、社区检测、成本和评估方法仍在演进。它适合关系密集资料，不适合简单 FAQ 或关系抽取质量很差的数据。

证据边界：前沿主源清单支持 GraphRAG 作为 RAG 进化方向；Neo4j source note 支持 GraphRAG 的工程实现层和边界提醒；RAG 类型对比支持 GraphRAG 与 Neo4j、RAGGraph、Hybrid Search 的层级区分。具体 Microsoft GraphRAG 或 Neo4j API 细节不在本卡里当作稳定事实。

## 它解决什么问题

普通向量检索擅长找语义相似片段，但在跨文档、多跳关系、实体关系和整体主题总结上容易弱。

GraphRAG 试图让检索不只依赖“相似文本”，还利用“概念之间的关系”。

## 它不是什么

GraphRAG 不是普通 RAG 的替代品。

GraphRAG 也不是只要用了图数据库就自动更好。图构建、实体抽取、关系质量和查询方式都会影响结果。

它也不等于 [[RAGGraph]]：GraphRAG 偏知识图谱/关系检索；RAGGraph 更可能偏 RAG workflow 编排。

## 最小例子

问题：某个公司和哪些研究方向、人物、项目相关？

GraphRAG 可能先从文档里抽取实体和关系，再通过图遍历找到相关社区，最后生成回答。

```text
文档 -> entity/relation extraction -> graph + chunks
问题 -> vector/fulltext 找入口 -> graph traversal 扩展关系 -> answer with sources
```

## 常见误解 / 风险

- 误解：用了 [[Neo4j]] 就自动是 GraphRAG。
- 误解：GraphRAG 一定比向量 RAG 更好；简单 FAQ 可能不值得构图。
- 风险：LLM 抽取实体和关系会出错，图谱错误会被放大。
- 风险：图 schema 设计不适合任务时，查询会复杂但收益很低。
- 风险：图遍历扩展过多会污染上下文。

## 边界细节

看到 GraphRAG 时要问：图是用来组织知识，还是用来编排 RAG pipeline？

还要问：图是方法层面的 GraphRAG，还是 [[Neo4j]] 这类图数据库实现？[[Neo4j]] 很重要，但它是工具生态，不是 GraphRAG 的定义本身。

和 [[Hybrid Search]] 的边界：Hybrid Search 解决向量和关键词互补；GraphRAG 解决实体关系和图结构上下文。

## 现代性状态

- 判定：current-practice / frontier。
- 稳定部分：图结构可以补足向量检索在实体关系、多跳和全局总结上的弱点。
- 易变部分：自动构图、社区检测、Text2Cypher、GraphRAG package、评估方法和图数据库集成。
- freshness: watch。
- last_checked: 2026-05-10。
- 复查点：更新 [[Neo4j]] 或 Microsoft GraphRAG 具体能力时，区分实现生态与 GraphRAG 概念边界。

## 现代系统怎么吸收 GraphRAG 的价值

现代系统会把 GraphRAG 放在 retrieval strategy 层：先判断问题是否真的需要关系结构，再选择图遍历、Cypher、社区摘要、向量搜索或全文搜索。它还需要评估实体抽取准确率、关系真实性、图扩展后的上下文噪声和最终引用支持度。

## 证据锚点

- Source: [[前沿主源清单]]
- Anchor: [[前沿主源清单#RAG 进化]]
- Source: [[Neo4j GraphRAG 官方文档]]
- Anchor: [[Neo4j GraphRAG 官方文档#为什么收]]
- Anchor: [[Neo4j GraphRAG 官方文档#一句话]]
- Anchor: [[Neo4j GraphRAG 官方文档#边界提醒]]
- Source: [[RAG 类型对比]]
- Anchor: [[RAG 类型对比#一张表先抓住]]
- Evidence type: frontier source map + official docs source note + local comparison map + engineering synthesis.
- Confidence: medium
- Boundary: Neo4j source supports one important implementation ecosystem; GraphRAG as a method is broader than Neo4j, and workflow-graph meanings belong closer to [[RAGGraph]].

## 复习触发

- GraphRAG 解决的是哪类普通向量 RAG 难题？
- 为什么 Neo4j 是实现生态，而不是 GraphRAG 的定义本身？
- 如何判断一个问题是否值得引入图结构？

## 相关链接

- [[RAG]]
- [[Memory]]
- [[Agentic RAG]]
- [[RAG 类型对比]]
- [[Neo4j]]
- [[Neo4j GraphRAG 官方文档]]
