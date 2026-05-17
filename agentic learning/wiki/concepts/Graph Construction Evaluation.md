---
type: concept
topic:
  - rag
  - graph
  - evaluation
status: growing
created: 2026-05-12
updated: 2026-05-16
up:
  - "[[Evaluation]]"
last_checked: 2026-05-12
freshness: watch
source:
  - "[[GraphRAG]]"
  - "[[Knowledge Graph]]"
  - "[[Neo4j GraphRAG 官方文档]]"
  - "[[RAG Evaluation]]"
evidence:
  - "[[GraphRAG#常见误解 / 风险]]"
  - "[[Knowledge Graph#常见误解 / 风险]]"
  - "[[Neo4j GraphRAG 官方文档#边界提醒]]"
  - "[[RAG Evaluation#概念详解]]"
related:
  - "[[GraphRAG]]"
  - "[[Knowledge Graph]]"
  - "[[Entity Resolution]]"
  - "[[RAG Evaluation]]"
---

# Graph Construction Evaluation

## 一句话

Graph Construction Evaluation 是评估 GraphRAG / Knowledge Graph 构图质量的过程，重点检查实体、关系、schema、source grounding 和图扩展是否可靠。

## 概念详解

GraphRAG 的风险不只发生在检索时，也发生在图被建出来的那一刻。LLM 或抽取工具可能漏掉实体、合并错别名、抽出不存在的关系、把时间条件丢掉、把同名不同实体混成一个节点，或者创建过宽的关系类型。只要图谱污染，后续图遍历会把错误关系当成结构化证据放大。

Graph Construction Evaluation 把评估前移到构图阶段：抽样检查实体识别准确率、关系真实性、source chunk 回链、schema 约束、实体去重、关系方向、时间/版本条件、权限 metadata 和图扩展噪音。它和普通 [[RAG Evaluation]] 互补：RAG eval 看最终检索/回答链路，构图评估看图谱本身是否值得被检索使用。

证据边界：[[GraphRAG]]、[[Knowledge Graph]] 和 [[Neo4j GraphRAG 官方文档]] 都提示图构建、实体关系质量和 schema 是 GraphRAG 的关键风险；本卡把这些风险组织成评估概念，属于工程综合。

图构建评估关注的是“图本身是否可信”，而不是最终问答是否看起来合理。一个 GraphRAG 系统可能回答准确，但图中存在大量错误实体、漏关系或冲突属性；这些问题在下一批数据或多跳问题里会暴露。评估应抽样检查 entity extraction、relation extraction、schema compliance、entity resolution、provenance 和下游任务收益，并把错误类型反馈给抽取 prompt、规则、人工审核或 schema 设计。
## 它解决什么问题

它解决“图看起来很高级，但实体关系不可靠”的问题。没有构图评估，GraphRAG 可能比普通 RAG 更危险，因为错误被包装成结构化关系。

## 它不是什么

它不是只评最终答案。

它也不是只看节点和边数量。图很大不代表有用；边越多也可能只是噪音越多。

## 最小例子

```text
抽取关系："Alice --创始人--> Project X"
source chunk："Alice joined Project X as a consultant."
```

构图评估应判定这条关系不被 source 支持。

## 常见误解 / 风险

- 误解：LLM 抽图比人工 schema 更省事，所以可以不评估。
- 误解：图谱节点越多越好。过度抽取会污染检索。
- 风险：实体去重错误会把同名人、同名产品或缩写混在一起。
- 风险：关系没有 source grounding，图谱变成无来源事实库。
- 风险：图扩展过宽，正确答案被噪音淹没。

## 边界细节

和 [[RAG Evaluation]] 的边界：RAG Evaluation 看 query-time 检索和答案；Graph Construction Evaluation 看 index/build-time 的图谱质量。

和 [[Entity Resolution]] 的边界：Entity Resolution 是构图评估中的关键子问题；它只处理实体对齐/去重，不覆盖关系真实性和 schema。

和 [[GraphRAG]] 的边界：GraphRAG 是使用图增强检索的模式；构图评估是让这个模式可靠的质量控制层。

## 现代性状态

- 判定：frontier / current-practice。
- 稳定部分：图谱构建必须检查实体、关系和来源支持。
- 易变部分：自动抽图、社区检测、Text2Cypher、图评测指标和工具链仍在演进。
- 复查点：GraphRAG 工具升级时，优先看是否提供抽取质量评估、source grounding 和人工校验流程。

## 现代系统怎么吸收 Graph Construction Evaluation 的价值 / 局限

现代系统会把构图当成可测试数据管线：固定样本文档、期望实体/关系、抽取结果 diff、人工抽样、source grounding 检查和 downstream RAG eval。图谱更新后，要跑回归，而不是只看 demo 查询。

局限是图质量很依赖领域 schema 和标注样本；通用自动指标难完全覆盖业务语义。高价值图谱通常需要人机协作和持续维护。

## 证据锚点

- Concept anchor: [[GraphRAG#常见误解 / 风险]]
- Concept anchor: [[Knowledge Graph#常见误解 / 风险]]
- Source anchor: [[Neo4j GraphRAG 官方文档#边界提醒]]
- Concept anchor: [[RAG Evaluation#概念详解]]
- Evidence type: existing concept/source synthesis + engineering inference.

- Boundary: Graph Construction Evaluation 评估构图质量，不等于 RAG answer evaluation、图数据库性能测试或只看节点/边数量。
## 复习触发

1. 为什么 GraphRAG 的评估不能只看最终答案？
2. 构图阶段最容易出现哪三类错误？
3. source grounding 对知识图谱为什么重要？

## 相关链接

- [[GraphRAG]]
- [[Knowledge Graph]]
- [[Entity Resolution]]
- [[RAG Evaluation]]
- [[GraphRAG 构图与评估对比]]
