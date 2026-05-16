---
type: map
topic:
  - rag
  - graph
  - evaluation
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-16
source:
  - "[[GraphRAG]]"
  - "[[Knowledge Graph]]"
  - "[[Entity Resolution]]"
  - "[[Graph Construction Evaluation]]"
  - "[[Neo4j GraphRAG 官方文档]]"
evidence:
  - "[[GraphRAG#证据锚点]]"
  - "[[Knowledge Graph#证据锚点]]"
  - "[[Entity Resolution#证据锚点]]"
  - "[[Graph Construction Evaluation#证据锚点]]"
related:
  - "[[RAG 主题]]"
  - "[[RAG 类型对比]]"
  - "[[Neo4j]]"
---

# GraphRAG 构图与评估对比

## 一句话总览

[[GraphRAG]] 的难点不只是“把图接到 RAG”，而是先把文本里的实体、关系、社区/路径和属性构成可信的 [[Knowledge Graph]]，再用 [[Graph Construction Evaluation]] 检查实体抽取、[[Entity Resolution]]、关系质量、覆盖率和下游回答收益。

## 为什么这组值得对比

GraphRAG 相关术语容易混，因为学习者常把“图数据库”“知识图谱”“图检索”“GraphRAG 方法”和“构图质量评估”当成同一件事。实际工程里，GraphRAG 的失败可能发生在三个不同层：

- 构图层：实体抽取错、关系类型错、同一实体没有合并。
- 检索层：图遍历、社区摘要、向量/全文/图混合检索没有找到合适上下文。
- 生成层：模型误读图上下文或 citation 不支持结论。

## 共同问题域

共同问题域是“文本知识如何被结构化为实体-关系图，并在 RAG 中提供比普通 chunk 检索更好的多跳/全局/关系型上下文”。

```text
source documents -> entity/relation extraction -> entity resolution -> graph store
                -> graph query / community / path retrieval -> context -> answer/eval
```

## 核心区别表

| 概念 | 角色 | 输入 | 输出 | 主要失败 | 证据锚点 |
|---|---|---|---|---|---|
| [[Knowledge Graph]] | 结构化知识表示层 | 实体、关系、属性、来源 | 可查询的实体-关系网络 | schema 不清、关系缺证据、更新困难 | [[Knowledge Graph#证据锚点]] |
| [[Entity Resolution]] | 合并同一现实实体 | 实体候选、别名、上下文、ID | canonical entity / merge decision | 误合并、漏合并、跨租户污染 | [[Entity Resolution#证据锚点]] |
| [[Graph Construction Evaluation]] | 构图质量检查 | 抽取结果、人工样本、schema、下游任务 | precision/recall、错误类型、修复优先级 | 只看图规模、不看正确性 | [[Graph Construction Evaluation#证据锚点]] |
| [[GraphRAG]] | 图结构参与 RAG 的方法族 | 文档、图、retriever、LLM | 图增强上下文和答案 | 构图成本高、检索路径错、答案仍幻觉 | [[GraphRAG#证据锚点]] |
| [[Neo4j]] | 图数据库/生态实现线 | 节点、关系、索引、查询 | 图存储、Cypher/向量/全文组合 | 把工具能力误当方法保证 | [[Neo4j#证据锚点]] |

## 最容易混淆的边界

### Knowledge Graph vs GraphRAG

[[Knowledge Graph]] 是结构化知识表示；[[GraphRAG]] 是把图结构用于检索增强生成的方法/架构。可以有知识图谱但没有 GraphRAG，也可以在 GraphRAG 里使用轻量实体图而不是完整企业知识图谱。

### Entity Resolution vs Graph Construction Evaluation

[[Entity Resolution]] 是构图过程里的一个具体任务：判断“OpenAI”“Open AI”“OpenAI, Inc.”是否是同一实体。[[Graph Construction Evaluation]] 是更大的质量检查，覆盖实体抽取、关系抽取、resolution、schema、覆盖率和下游效果。

### Graph Construction Evaluation vs RAG Evaluation

[[Graph Construction Evaluation]] 评估图本身是否可信；[[RAG Evaluation]] 评估问答链路是否基于证据答对。构图质量高不保证最终答案好；最终答案好也不证明图谱无误。

### Neo4j vs GraphRAG

[[Neo4j]] 是图数据库和 GraphRAG 工程生态的重要实现选项，不是 GraphRAG 概念本身。使用 Neo4j 不自动获得高质量构图、评估或答案忠实度。

## 执行时序 / 机制差异

```text
1. document ingestion: 保留来源、段落、权限和版本
2. extraction: 抽实体、关系、属性、时间和证据 span
3. resolution: 合并别名、去重、建立 canonical ID
4. graph validation: 抽样检查实体/关系/schema/coverage
5. retrieval: 图遍历、社区摘要、向量/全文/图混合
6. answer eval: citation faithfulness、RAG correctness、trace 回放
```

关键边界：GraphRAG 的 evaluation 不能只在最终答案层做。若构图错误进入图数据库，后续检索会稳定地把错误结构当成事实来源。

## 学习类比（非证据）

可以把 GraphRAG 生产线类比成“先建城市地图，再规划路线，再检查地图有没有画错”：Knowledge Graph 是地图，Entity Resolution 是把同一个地点合并，Graph Construction Evaluation 是查地图质量，GraphRAG 是用地图辅助回答。

类比边界：这只是学习类比（非证据），不代表论文、官方文档或具体产品内部真的按这个类比实现。

## 现代系统如何吸收或限制

现代 GraphRAG 系统通常把图与向量/全文检索结合：向量负责语义召回，图负责关系、路径、社区和实体约束，全文负责精确名称匹配。现代性状态是 **current-practice + frontier/watch**：知识图谱和实体消歧是成熟数据工程概念；LLM 自动构图、社区摘要、图增强 RAG 的最佳评估方法仍在快速演化。

工程综合 / inference：当数据天然有实体网络、依赖关系、组织/产品/人物/法规关系时，GraphRAG 更可能带来收益；当数据只是少量 FAQ 或短文档时，构图评估成本可能超过收益。

## 什么时候用哪个判断

- 需要明确实体、关系、路径和多跳推理：看 [[Knowledge Graph]] / [[GraphRAG]]。
- 发现同一实体被拆成多个节点或不同实体被合并：看 [[Entity Resolution]]。
- 图看起来很大但问答质量不稳定：看 [[Graph Construction Evaluation]]，不要只调 prompt。
- 已有图数据库但不知道是否改善 RAG：同时跑构图评估和 [[RAG Evaluation]]。
- 只是需要存储和查询关系数据：看 [[Neo4j]]，不必把它包装成 GraphRAG。

## 它们共同不是什么

- 不是“用了图就不会幻觉”。
- 不是“图节点越多越好”。
- 不是“LLM 自动抽图就不需要 schema 和抽样评估”。
- 不是普通向量检索的万能升级；它用更高复杂度换关系结构能力。
- 不是把所有 chunk 都连成图就能产生可信知识。

## 证据锚点

- 概念卡：[[GraphRAG#证据锚点]], [[Knowledge Graph#证据锚点]], [[Entity Resolution#证据锚点]], [[Graph Construction Evaluation#证据锚点]], [[RAG Evaluation#证据锚点]], [[Neo4j#证据锚点]]。
- source notes：[[Neo4j GraphRAG 官方文档]], [[Microsoft RAG 官方文档]], [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]。
- 主题锚点：[[RAG 类型对比#证据锚点]], [[RAG 主题#证据锚点]]。
- 证据边界：本页的构图流程和判断表是工程综合 / inference；不同 GraphRAG 实现对 community、path、schema 和索引的命名可能不同，需要看具体官方文档。

- Evidence type: concept cards + Neo4j/Microsoft source notes + engineering synthesis.
- Confidence: high for local concept boundaries; medium for implementation-specific GraphRAG practices.
- Boundary: 不同 GraphRAG 实现对 community、path、schema、index 的命名不同，本页不替代具体官方文档。
## 复习触发

1. 为什么 “GraphRAG 答错” 不能只看最终答案，而要先检查实体抽取、关系抽取和 entity resolution？
2. Knowledge Graph、GraphRAG、Neo4j 三者的最小边界分别是什么？
3. 如果图谱规模很大但 relation precision 很低，可能对 RAG 造成什么稳定性问题？

## 相关链接

- [[RAG 主题]]
- [[GraphRAG]]
- [[Knowledge Graph]]
- [[Entity Resolution]]
- [[Graph Construction Evaluation]]
- [[Neo4j]]
- [[RAG Evaluation]]
- [[RAG Citation Faithfulness]]
