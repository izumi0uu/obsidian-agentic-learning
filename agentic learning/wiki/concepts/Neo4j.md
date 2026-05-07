---
type: concept
topic:
  - rag
  - graph
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: watch
conflicts: []
source:
  - "[[Neo4j GraphRAG 官方文档]]"
  - "[[RAG 类型对比]]"
evidence:
  - "[[Neo4j GraphRAG 官方文档#为什么收]]"
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

## 它解决什么问题

普通向量 RAG 主要靠“文本片段语义相似”找上下文，但很多问题真正依赖实体关系、多跳关联和结构化查询。

Neo4j 让 RAG 可以多一层图结构：

- 用节点和关系保存实体、文档、chunk、事件、项目、人物等对象。
- 用 Cypher 查询结构化关系。
- 用向量索引做语义召回。
- 用全文索引补关键词召回。
- 用图遍历扩展相关上下文。
- 用 LLM Knowledge Graph Builder 或 GraphRAG Python Package 把非结构资料转成图谱和检索器。

## 它不是什么

Neo4j 不是 [[GraphRAG]] 本身。

它也不是所有 RAG 系统的必选项。只有当问题真的需要关系结构、图遍历、实体级查询或知识图谱维护时，它才值得引入。

Neo4j 也不会自动保证抽取出的实体和关系是真的。LLM 抽图、schema 设计、去重、评估和引用校验仍然要单独处理。

## 最小例子

问题：

> 某个研究方向和哪些论文、作者、项目、公司有关？这些关系分别来自哪些来源？

一个 Neo4j GraphRAG 方案可能是：

```text
PDF/网页 -> Document/Chunk 节点 -> 抽取 Entity/Relation -> 存 Neo4j
问题 -> 向量召回相关 Chunk -> Cypher 扩展实体关系 -> LLM 基于证据回答
```

这里 Neo4j 的价值不是“替模型回答”，而是保存和查询关系网络。

## 为什么前沿知识要包括它

Neo4j 代表 GraphRAG 从论文/概念走向工程系统的一条重要路线。

它把几件事放到同一个生态里：知识图谱构建、图数据库、向量检索、全文检索、图遍历、Text2Cypher、GraphRAG Python Package、LLM Knowledge Graph Builder，以及和 LangChain、LlamaIndex、Semantic Kernel 等框架的集成。

所以在我的知识体系里，Neo4j 应该被放在“GraphRAG 工程实现层”，而不是和 [[Self-RAG]]、[[Corrective RAG]] 平级的“RAG 方法层”。

## 常见误解和风险

- 误解：用了 Neo4j 就是 GraphRAG。实际要看检索是否真的利用了图关系。
- 误解：LLM 自动抽图就能得到可靠知识图谱。实际需要 schema、去重、人工抽查和评估。
- 风险：图谱构建成本高，尤其是长文档、表格、图片和噪声资料。
- 风险：Text2Cypher 可能生成错误查询，必须限制权限并验证结果。
- 风险：关系扩展太多会让上下文变脏，答案反而更差。

## 学习顺序

1. 先理解 [[GraphRAG]] 和 [[RAG 类型对比]]。
2. 再读 [[Neo4j GraphRAG 官方文档]]，知道 Neo4j 在 GraphRAG 里放在哪一层。
3. 最后做一个最小实验：3-5 篇文档，抽实体和关系，再用一个关系型问题测试普通向量 RAG 和 Neo4j GraphRAG 的差异。

## 证据锚点

- Source: [[Neo4j GraphRAG 官方文档]]
- Source: [[RAG 类型对比]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[GraphRAG]]
- [[RAG]]
- [[Retriever]]
- [[RAG 类型对比]]
- [[Neo4j GraphRAG 官方文档]]
