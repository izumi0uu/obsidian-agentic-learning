---
type: map
topic:
  - rag
  - comparison
status: active
created: 2026-05-06
updated: 2026-05-12
source:
  - "[[RAG]]"
  - "[[Retriever]]"
  - "[[Hybrid Search]]"
  - "[[Reranking]]"
  - "[[GraphRAG]]"
  - "[[Agentic RAG]]"
  - "[[Agentic Retrieval]]"
  - "[[Corrective RAG]]"
  - "[[Self-RAG]]"
  - "[[Neo4j GraphRAG 官方文档]]"
evidence:
  - "[[RAG#证据锚点]]"
  - "[[GraphRAG#证据锚点]]"
  - "[[Agentic RAG#证据锚点]]"
  - "[[Agentic Retrieval#证据锚点]]"
  - "[[Corrective RAG#证据锚点]]"
  - "[[Self-RAG#证据锚点]]"
  - "[[Hybrid Search#证据锚点]]"
  - "[[Reranking#证据锚点]]"
  - "[[Neo4j#证据锚点]]"
related:
  - "[[RAG 主题]]"
  - "[[前沿主源清单]]"
  - "[[Retriever]]"
  - "[[Neo4j]]"
  - "[[RAG Evaluation]]"
---

# RAG 类型对比

## 一句话总览

这页回答：不同 RAG 形态到底差在哪里。核心边界不是“哪个更高级”，而是它们分别改造了 RAG 链路的不同位置：文档处理、检索方式、排序、图关系、检索决策、证据纠错或生成时自检。

最小判断：[[RAG]] 是基本模式；Vector / Hybrid / Reranked RAG 改检索质量；[[GraphRAG]] 改知识结构；[[Agentic RAG]] / [[Agentic Retrieval]] 改检索决策；[[Corrective RAG]] / [[Self-RAG]] 改证据评估和自适应控制。

## 为什么这组值得对比

- 混淆风险高：GraphRAG、Agentic RAG、Self-RAG、Corrective RAG 都容易被说成“更高级的 RAG”。
- 共同问题域相同：都围绕“如何把外部知识带入生成，并让答案更可证据化”。
- 介入点不同：有的改 retrieve，有的改 rank，有的改知识结构，有的加 evaluator，有的让模型决定是否检索。
- 证据密度足够：相关概念卡已有 paper / docs / source note 锚点。
- 现代工程价值高：能帮助判断什么时候只要普通 RAG，什么时候才值得引入图、agent、纠错或自检。

边界：这页不替代每张概念卡，也不声称这些 RAG 类型构成严格谱系；它只用于学习时切开工程介入点。

## 共同问题域

共同问题是：模型参数里没有、过时、不可引用或私有的知识，如何从外部资料中取回，并在生成时正确使用。

RAG 链路可以粗略拆成：

```text
source -> ingest/chunk -> index -> retrieve -> rank/filter -> generate -> verify/evaluate
```

不同 RAG 类型的差异，往往不是“有没有检索”，而是它改造了这条链路的哪一段。

## 核心区别表

| 类型 | 主要介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[RAG]] | 最小检索增强生成模式 | `query -> retrieve -> generate` | 用户问题、外部文档 | 带上下文的回答 | [[RAG#证据锚点]] |
| Vector RAG | 向量相似检索 | ingest 后索引，query 时相似搜索 | embedding、向量库 | top-k 相似 chunk | [[Vector Database]], [[Embedding]] |
| [[Hybrid Search]] | 向量 + 关键词/全文互补 | retrieve 阶段并行或融合 | query、embedding、关键词 | 更稳的候选集合 | [[Hybrid Search#证据锚点]] |
| [[Reranking]] | 初检后的重新排序 | retrieve 后、generate 前 | 候选 chunk、query | 重新排序后的证据 | [[Reranking#证据锚点]] |
| [[GraphRAG]] | 实体/关系/社区结构 | ingest 建图，query 时图遍历/图上下文 | 文档、实体、关系 | 图增强上下文 | [[GraphRAG#证据锚点]] |
| [[Neo4j]] GraphRAG | 图数据库实现层 | 图存储、Cypher、向量/全文/遍历组合 | 节点、关系、向量索引 | 可查询图谱 + RAG 上下文 | [[Neo4j#证据锚点]] |
| [[Agentic RAG]] | Agent 决定检索策略 | 多轮 plan / retrieve / judge / retry | 复杂任务、多源资料 | 多步检索与综合答案 | [[Agentic RAG#证据锚点]] |
| [[Agentic Retrieval]] | 检索层 query planning | retrieve 前拆问题、多源检索 | 企业搜索问题、多源索引 | 分解后的检索结果 | [[Agentic Retrieval#证据锚点]] |
| [[Corrective RAG]] | 检索后证据质量门 | retrieve -> grade -> repair / answer | 检索结果、质量判断 | 纠错后的证据路径 | [[Corrective RAG#证据锚点]] |
| [[Self-RAG]] | 生成时自适应检索/批判 | decide retrieve / generate / critique | query、模型判断、证据 | 自适应检索和证据批判 | [[Self-RAG#证据锚点]] |

## 最容易混淆的边界

- [[GraphRAG]] vs [[Neo4j]]：前者是图增强检索模式，后者是图数据库和工程生态。
- [[GraphRAG]] vs [[RAGGraph]]：GraphRAG 通常强调图结构知识；RAGGraph 可能只是把 RAG pipeline 编排成 graph workflow。
- [[Agentic RAG]] vs [[Agentic Retrieval]]：前者是整个 RAG 系统进入 Agent 决策；后者更偏检索层 query planning、多源检索和子问题分解。
- [[Corrective RAG]] vs [[Self-RAG]]：前者偏工程流程里检索质量评估和补救；后者来自模型自适应检索 / 生成 / 批判论文线。
- [[Hybrid Search]] vs [[GraphRAG]]：Hybrid 解决语义和关键词互补；GraphRAG 解决实体关系和图结构上下文。
- [[Reranking]] vs 扩大 top-k：reranking 主要重排候选，不等于扩大召回本身。

## 执行时序 / 机制差异

```text
Basic RAG:       Query -> Retrieve -> Generate
Hybrid/Rerank:   Query -> Retrieve many ways -> Rerank/Filter -> Generate
GraphRAG:        Query -> Entity/Relation/Community context -> Generate
Agentic RAG:     Goal -> Plan/Search -> Evaluate evidence -> Re-search/Answer
Corrective RAG:  Retrieve -> Grade evidence -> Correct/Retrieve again -> Generate
Self-RAG:        Generate-time decisions: retrieve? evidence enough? critique?
```

这组时序是学习综合，不是所有论文或产品共享的统一实现。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文或官方文档证据。

把 RAG 想成“写旅行攻略前找资料”：

| RAG 类型 | 生活中的对应物 | 类比边界 |
|---|---|---|
| [[RAG]] | 先拿旅游书，再写攻略 | 说明外部资料进入回答，不说明资料一定正确 |
| Vector RAG | 按“意思相近”找资料 | 语义相似不等于事实支持 |
| [[Hybrid Search]] | 既按意思找，也按地名/票价等关键词找 | 互补检索，不是简单拼接结果 |
| [[Reranking]] | 先拿一摞资料，再把最有用的排前面 | 排序不是召回本身 |
| [[GraphRAG]] | 先画人物/地点/交通关系图 | 图关系质量决定效果 |
| [[Agentic RAG]] | 让助理自己决定先查什么、再比较什么 | 助理决策需要 trace/eval 约束 |
| [[Corrective RAG]] | 发现资料不靠谱就换资料或补查 | 关键是证据质量门 |
| [[Self-RAG]] | 写作时边写边判断“这句要不要查证” | 工程 prompt 模拟不等于论文训练方法 |

## 现代系统如何吸收或限制

### 来源支持的稳定部分

- [[RAG]] 卡和 source note 支持“检索外部资料再生成”的基本模式。
- [[Hybrid Search]]、[[Reranking]] 和 [[Retriever]] 相关卡支持“检索质量是独立工程层”的判断。
- [[GraphRAG]] / [[Neo4j]] 相关卡支持“实体关系和图数据库可以增强检索”的工程边界。
- [[Corrective RAG]] 和 [[Self-RAG]] 的 paper/source note 支持“证据质量判断”和“自适应检索/批判”是 RAG 可靠性的关键问题。

### 工程综合 / inference

现代 RAG 系统通常不是只选一个标签，而是组合多层：先做好 ingestion / chunking / hybrid retrieval / reranking，再按任务复杂度选择 GraphRAG、Agentic Retrieval 或 corrective loop。把所有高级词都堆上去，常常比最小 RAG 更难调试。

## 什么时候用哪个判断

| 场景 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 文档问答、个人知识库问答 | [[RAG]] | 最小链路足够先验证切分、检索和引用 | 不要一开始过度工程化 |
| 专有名词、代码、产品文档 | [[Hybrid Search]] + [[Reranking]] | 语义和关键词互补，排序改善证据质量 | 融合策略可能带来噪音 |
| 多跳实体关系、跨文档网络 | [[GraphRAG]] / [[Neo4j]] | 图结构表达关系和全局上下文 | 图抽取错误会污染上下文 |
| 多步骤研究、多源比较 | [[Agentic RAG]] / [[Agentic Retrieval]] | 需要分解问题、决定查什么和是否重查 | Agent 决策需要预算、trace、eval |
| 高准确任务，坏检索代价高 | [[Corrective RAG]] | 检索结果先过质量门 | evaluator 错误会导致过度补救或错杀证据 |
| 模型需要判断是否检索和证据是否支持 | [[Self-RAG]] | 自适应检索/生成/批判 | prompt 近似不等于论文训练机制 |

## 它们共同不是什么

- 都不是“加了检索就不会幻觉”。
- 都不是长期记忆的全部；RAG 更偏外部知识检索，记忆还涉及写入、更新、遗忘和权限。
- 都不是越复杂越好；复杂 RAG 会增加调试、成本、延迟和证据污染风险。
- 都不自动保证引用忠实；还需要 [[RAG Evaluation]]、trace、答案-证据一致性检查和人工抽检。

## 证据锚点

- Concept anchors: [[RAG#证据锚点]], [[GraphRAG#证据锚点]], [[Agentic RAG#证据锚点]], [[Agentic Retrieval#证据锚点]], [[Corrective RAG#证据锚点]], [[Self-RAG#证据锚点]], [[Hybrid Search#证据锚点]], [[Reranking#证据锚点]], [[Neo4j#证据锚点]]
- Source examples: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]], [[Microsoft RAG 官方文档]], [[Neo4j GraphRAG 官方文档]], [[Azure AI Search Agentic Retrieval]], [[Corrective Retrieval Augmented Generation]], [[Self-RAG - Learning to Retrieve Generate and Critique]]
- Evidence type: concept-card synthesis + paper/docs source notes + learning analogy.
- Confidence: medium-high for layer distinctions; medium for specific “when to use” judgments because they depend on corpus quality、latency、成本和评测目标。
- Boundary: 表格里的 Vector / Hybrid / Reranked RAG 是工程模式标签；不是每个都有同等级论文来源。类比只用于学习，不是来源证据。

## 复习触发

1. 如果一个系统用了 Neo4j，它一定是 GraphRAG 吗？为什么？
2. Hybrid Search 和 Reranking 分别改造 RAG 链路的哪一段？
3. Agentic RAG 和 Agentic Retrieval 的最小区别是什么？
4. Corrective RAG 和 Self-RAG 都会“检查证据”，它们的检查位置有什么不同？
5. 给一个简单 FAQ 场景，说明为什么不应该一开始就上 GraphRAG / Agentic RAG。

## 相关链接

- [[RAG 主题]]
- [[RAG]]
- [[Retriever]]
- [[Hybrid Search]]
- [[Reranking]]
- [[GraphRAG]]
- [[RAGGraph]]
- [[Agentic RAG]]
- [[Agentic Retrieval]]
- [[Corrective RAG]]
- [[Self-RAG]]
- [[Neo4j]]
- [[RAG Evaluation]]
- [[Neo4j GraphRAG 官方文档]]
