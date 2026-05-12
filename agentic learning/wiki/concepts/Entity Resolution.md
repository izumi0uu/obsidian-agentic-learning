---
type: concept
topic:
  - rag
  - graph
  - data
status: growing
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: watch
source:
  - "[[Knowledge Graph]]"
  - "[[GraphRAG]]"
  - "[[Neo4j GraphRAG 官方文档]]"
evidence:
  - "[[Knowledge Graph#概念详解]]"
  - "[[GraphRAG#概念详解]]"
  - "[[Neo4j GraphRAG 官方文档#边界提醒]]"
related:
  - "[[Knowledge Graph]]"
  - "[[GraphRAG]]"
  - "[[Graph Construction Evaluation]]"
  - "[[Document Ingestion]]"
---

# Entity Resolution

## 一句话

Entity Resolution 是把不同文档、别名、拼写或 ID 中指向同一真实对象的实体对齐，并把同名但不同对象分开的过程。

## 概念详解

在 [[Knowledge Graph]] / [[GraphRAG]] 中，系统会从大量文档里抽取人物、组织、项目、产品、论文、函数或事件。问题是文本中的实体并不干净：同一个对象可能有多个名字、缩写、大小写、旧名称和语言版本；不同对象也可能同名。Entity Resolution 负责判断这些 mention 是否应合并成同一个节点，或保持为不同节点。

没有 Entity Resolution，图谱会出现两类典型错误：一是同一实体被拆成多个节点，导致关系断裂；二是不同实体被错误合并，导致关系污染。对 GraphRAG 来说，这会直接影响图遍历和上下文扩展：问 Project X 相关人员时，系统可能漏掉别名节点，或者把另一个同名项目的人拉进来。

证据边界：[[Knowledge Graph]] 和 [[GraphRAG]] 概念卡已经说明实体、关系和图结构是图增强检索的核心；[[Neo4j GraphRAG 官方文档]] 提醒图里的实体和关系是否可靠是关键问题。本卡把实体对齐/去重作为构图质量中的独立概念沉淀。

## 它解决什么问题

它解决知识图谱里的“同物异名”和“同名异物”问题，让检索和图遍历能围绕正确实体展开。

## 它不是什么

Entity Resolution 不是实体抽取本身。实体抽取是从文本中找 mention；entity resolution 是判断 mention 是否指向同一真实对象。

它也不是完整 [[Graph Construction Evaluation]]。构图评估还要检查关系真实性、schema、source grounding、权限和图扩展噪音。

## 最小例子

```text
"OpenAI"、"OpenAI Inc."、"Open AI" -> 可能是同一组织节点
"Apple" 水果 vs "Apple" 公司 -> 应保持不同实体
```

## 常见误解 / 风险

- 误解：名字相同就应该合并。人名、项目名和产品名经常冲突。
- 误解：embedding 相似就能解决所有实体对齐。ID、时间、上下文和来源也很重要。
- 风险：错误合并会把关系污染成结构化假事实。
- 风险：过度保守不合并会让图谱碎片化，多跳检索漏证据。

## 边界细节

和 [[Document Ingestion]] 的边界：ingestion 负责资料解析和 metadata；entity resolution 负责跨资料对齐实体。

和 [[Knowledge Graph]] 的边界：knowledge graph 是节点和关系整体；entity resolution 是保证节点身份正确的子问题。

和 [[GraphRAG]] 的边界：GraphRAG 用图做检索；entity resolution 决定图里的入口和路径是否可靠。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：实体对齐和去重是知识图谱、搜索和数据集成中的基础问题。
- 易变部分：LLM 辅助抽取、embedding-based matching、规则/模型混合和图数据库集成方式会变化。
- 复查点：GraphRAG pipeline 变化时，检查实体 ID、别名、source grounding 和人工纠错流程。

## 现代系统怎么吸收 Entity Resolution 的价值 / 局限

现代系统会混合使用规则、唯一 ID、metadata、上下文窗口、embedding 相似、LLM 判断和人工校验。高风险图谱会保留 merge/split 记录，让错误实体合并可以回滚。

局限是实体身份常常依赖业务知识；没有领域 schema 和样本，自动 resolution 容易在同名对象上犯错。

## 证据锚点

- Concept anchor: [[Knowledge Graph#概念详解]]
- Concept anchor: [[GraphRAG#概念详解]]
- Source anchor: [[Neo4j GraphRAG 官方文档#边界提醒]]
- Evidence type: graph/RAG concept synthesis + engineering inference.

## 复习触发

1. Entity extraction 和 Entity Resolution 的区别是什么？
2. 同名异物和同物异名分别会怎样破坏 GraphRAG？
3. 为什么错误合并比不合并更危险？

## 相关链接

- [[Knowledge Graph]]
- [[GraphRAG]]
- [[Graph Construction Evaluation]]
- [[Document Ingestion]]
- [[GraphRAG 构图与评估对比]]
