---
type: map
topic:
  - rag
  - comparison
status: active
created: 2026-05-06
updated: 2026-05-06
source:
  - "[[RAG]]"
  - "[[GraphRAG]]"
  - "[[Agentic RAG]]"
  - "[[Agentic Retrieval]]"
  - "[[Corrective RAG]]"
  - "[[Self-RAG]]"
  - "[[Neo4j GraphRAG 官方文档]]"
related:
  - "[[RAG 主题]]"
  - "[[前沿主源清单]]"
  - "[[Retriever]]"
  - "[[Neo4j]]"
---

# RAG 类型对比

这页专门回答：不同 RAG 到底差在哪里。

核心边界：有些是 RAG 方法，有些是检索模式，有些是工程工具。不要把 [[GraphRAG]]、[[Self-RAG]]、[[Neo4j]]、向量数据库混成同一层级。

## 一张表先抓住

| 类型 | 核心变化 | 主要解决什么问题 | 最适合的场景 | 它不是什么 |
|---|---|---|---|---|
| [[RAG]] | 检索外部资料，再生成回答 | 模型知识过时、不可引用、不能访问私有资料 | 文档问答、知识库问答、个人笔记问答 | 不是长期记忆全部，也不能保证答案正确 |
| Vector RAG | 用 embedding 做语义相似检索 | 用户问法和文档措辞不同 | FAQ、语义相近的文档检索 | 不是“语义相似就一定正确” |
| Hybrid RAG | 向量检索 + 关键词/全文检索 | 语义检索漏关键词，关键词检索不懂语义 | 专有名词、代码、产品文档、法律/医疗文本 | 不是简单把两个结果拼一起 |
| Reranked RAG | 初检后用 reranker 重新排序 | top-k 里有相关材料但排序不好 | 高准确问答、长文档检索 | 不是扩大召回本身 |
| [[GraphRAG]] | 用实体、关系、社区或知识图谱增强检索 | 多跳关系、跨文档实体关系、全局总结 | 组织知识、人物/公司/项目关系、复杂知识网络 | 不是用了图数据库就自动更好 |
| [[Neo4j]] GraphRAG | 用 Neo4j 图数据库、Cypher、向量/全文/图遍历做 GraphRAG | 把图结构落到可查询、可维护的工程系统 | 已有实体关系、需要可视化/可查询图谱、Graph + Vector 混合 | 不是一个新 RAG 概念，而是实现生态 |
| [[Agentic RAG]] | Agent 决定何时检索、检索什么、是否重查 | 复杂任务需要规划、多轮检索、证据判断 | 多步骤研究、比较任务、工具型 Agent | 不是加一个 Agent 就变强 |
| [[Agentic Retrieval]] | 检索层做 query planning、子问题分解、多源检索 | 单次 query / top-k 不够 | 企业搜索、多源知识库、复杂问题拆解 | 不是完整 Agent |
| [[Corrective RAG]] | 检索后评估证据质量，不够好就补救 | 坏检索导致坏答案 | 高准确问答、需要质量门的 RAG | 不是多搜几次 |
| [[Self-RAG]] | 模型判断是否检索、如何生成、证据是否支持答案 | 固定检索浪费或引入噪音 | 需要自适应检索和证据批判的任务 | 不是 prompt 里说“请反思” |

## 按问题选型

### 我只是想让模型回答我的文档

先用普通 [[RAG]]。

最小流程：

```text
文档 -> chunk -> embedding -> vector search -> LLM answer
```

不要一开始就上 GraphRAG 或 Agentic RAG。先验证：文档是否切得好，检索结果是否相关，答案是否引用来源。

### 我的问题包含实体关系和多跳关联

考虑 [[GraphRAG]] 或 [[Neo4j]] GraphRAG。

适合例子：

- 某公司和哪些人物、项目、技术路线有关？
- 一个代码库里模块之间怎样调用？
- 一个研究主题有哪些子领域和代表论文？

不适合例子：

- 单段 FAQ。
- 简单事实查询。
- 图关系抽取质量很差的资料。

### 我的问题很复杂，需要多次查资料

考虑 [[Agentic RAG]] 或 [[Agentic Retrieval]]。

典型问题：

> 比较 LangGraph、OpenAI Agents SDK 和 AutoGen 在 memory、trace、human-in-the-loop 上的差异。

这种问题不是一次 top-k 就能解决，需要拆维度、分来源检索、判断证据是否够。

### 我担心检索结果不可靠

考虑 [[Corrective RAG]]。

它的重点是 retrieval evaluator：

```text
retrieve -> grade evidence -> enough? -> answer / rewrite / retrieve again / fallback
```

### 我想让模型自己判断是否需要检索

看 [[Self-RAG]]。

但要注意：原始 Self-RAG 是论文方法，核心是训练和 reflection tokens。工程上用 prompt 模拟自检，只能算近似。

## Neo4j 应该放在哪一层

[[Neo4j]] 属于 GraphRAG 的工程实现层。

它能提供：

- 图数据库：节点、关系、属性。
- Cypher 查询：结构化图查询。
- 向量索引：支持 vector search。
- 全文搜索：支持关键词/全文检索。
- 图遍历：沿关系扩展上下文。
- LLM Knowledge Graph Builder：从非结构文本抽取实体、关系和 chunk。

但它不自动解决：

- 实体抽取质量。
- 图 schema 设计。
- 关系是否真实。
- 检索策略是否适合问题。
- 生成答案是否忠实引用证据。

## 最容易混淆的边界

- [[GraphRAG]] vs [[Neo4j]]：前者是模式/方法，后者是图数据库和工具生态。
- [[GraphRAG]] vs [[RAGGraph]]：GraphRAG 通常指图增强检索；RAGGraph 可能只是把 RAG pipeline 做成图工作流。
- [[Agentic RAG]] vs [[Agentic Retrieval]]：前者是整个 RAG 系统的决策模式；后者更偏检索层。
- [[Corrective RAG]] vs [[Self-RAG]]：前者偏工程流程里的检索质量评估；后者来自模型自适应检索/生成/批判论文线。
- Hybrid RAG vs [[GraphRAG]]：Hybrid 解决向量/关键词互补；GraphRAG 解决实体关系和图结构上下文。

## 对我的学习建议

当前阶段先按这个顺序学：

1. [[RAG]]：理解最小流程。
2. [[Retriever]]：理解检索错误如何影响回答。
3. Vector / Hybrid / Reranking：理解检索质量的基础工程。
4. [[GraphRAG]] + [[Neo4j GraphRAG 官方文档]]：理解图结构什么时候值得引入。
5. [[Agentic RAG]] / [[Agentic Retrieval]]：理解复杂任务里的检索决策。
6. [[Corrective RAG]] / [[Self-RAG]]：理解证据质量和自适应检索。

## 相关链接

- [[RAG 主题]]
- [[RAG]]
- [[GraphRAG]]
- [[RAGGraph]]
- [[Agentic RAG]]
- [[Agentic Retrieval]]
- [[Corrective RAG]]
- [[Self-RAG]]
- [[Neo4j]]
- [[Neo4j GraphRAG 官方文档]]
