---
type: concept
topic:
  - rag
  - frontier
  - graph
status: seed
created: 2026-05-05
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[前沿主源清单]]"
  - "[[Neo4j GraphRAG 官方文档]]"
evidence:
  - "[[前沿主源清单#RAG 进化]]"
  - "[[Neo4j GraphRAG 官方文档#为什么收]]"
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

## 它解决什么问题

普通向量检索擅长找语义相似片段，但在跨文档、多跳关系、实体关系和整体主题总结上容易弱。

GraphRAG 试图让检索不只依赖“相似文本”，还利用“概念之间的关系”。

## 它不是什么

GraphRAG 不是普通 RAG 的替代品。

GraphRAG 也不是只要用了图数据库就自动更好。图构建、实体抽取、关系质量和查询方式都会影响结果。

## 最小例子

问题：某个公司和哪些研究方向、人物、项目相关？

GraphRAG 可能先从文档里抽取实体和关系，再通过图遍历找到相关社区，最后生成回答。

## 边界细节

看到 GraphRAG 时要问：图是用来组织知识，还是用来编排 RAG pipeline？

还要问：图是方法层面的 GraphRAG，还是 [[Neo4j]] 这类图数据库实现？[[Neo4j]] 很重要，但它是工具生态，不是 GraphRAG 的定义本身。

## 证据锚点

- Source: [[前沿主源清单]]
- Source: [[Neo4j GraphRAG 官方文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[Memory]]
- [[Agentic RAG]]
- [[RAG 类型对比]]
- [[Neo4j]]
- [[Neo4j GraphRAG 官方文档]]
