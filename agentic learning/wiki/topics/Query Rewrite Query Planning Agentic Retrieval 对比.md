---
type: map
topic:
  - rag
  - retrieval
  - agent
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-16
source:
  - "[[Retriever]]"
  - "[[Query Rewrite]]"
  - "[[Query Planning]]"
  - "[[Agentic Retrieval]]"
  - "[[Azure AI Search Agentic Retrieval]]"
  - "[[Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging]]"
evidence:
  - "[[Retriever#证据锚点]]"
  - "[[Query Rewrite#证据锚点]]"
  - "[[Query Planning#证据锚点]]"
  - "[[Agentic Retrieval#证据锚点]]"
  - "[[Parallel Search and Explicit Merging 检索模式#证据锚点]]"
related:
  - "[[RAG 主题]]"
  - "[[Retrieval 组件对比]]"
  - "[[RAG 类型对比]]"
  - "[[Agentic RAG]]"
  - "[[Parallel Search and Explicit Merging 检索模式]]"
---

# Query Rewrite Query Planning Agentic Retrieval 对比

## 一句话总览

[[Query Rewrite]] 改写一个查询，[[Query Planning]] 把一个复杂问题拆成检索计划，[[Agentic Retrieval]] 让检索层具备规划、子查询、来源选择和结果整合能力；它们都改善 retrieval，但介入粒度从“改一句 query”逐步上升到“管理一次检索任务”。

## 为什么这组值得对比

这组概念容易混，因为产品文档和工程实现常把“rewrite、decompose、plan、agentic search、多轮 retrieval”混在一起说。学习时需要先切开三个问题：

- 语言表达问题：用户 query 太短、太口语、指代不清，需要 [[Query Rewrite]]。
- 任务结构问题：问题本身有多个子问题、条件或来源，需要 [[Query Planning]]。
- 执行控制问题：系统需要选择数据源、重试、评价证据、合并结果，需要 [[Agentic Retrieval]]。

## 共同问题域

共同问题域是 retrieval 前后的“查询决策层”：它不直接生成最终答案，而是决定系统应该查什么、怎么查、查几次、查哪个索引、怎样把候选证据交给后续上下文。

```text
user question -> rewrite / decompose / plan -> retrieve -> rerank -> context -> answer
```

对于 deep search / agentic RAG，还要单独看一组中间控制点：同一个 reasoning step 是否要发多个 query，以及 retrieval 后是否要显式合并证据。这个边界见 [[Parallel Search and Explicit Merging 检索模式]]。

## 核心区别表

| 概念 | 介入点 | 时序 / loop | 输入 | 输出 | 主要风险 | 证据锚点 |
|---|---|---|---|---|---|---|
| [[Query Rewrite]] | 单次 query 表达 | 通常在 retrieve 前一次性发生 | 原始问题、会话上下文、领域词表 | 改写后的 query / 多个 query 变体 | 改写偏题、丢失约束、过度扩展 | [[Query Rewrite#证据锚点]] |
| [[Query Planning]] | 子问题和检索步骤 | 可一次性规划，也可随结果调整 | 复杂问题、目标、可用索引/工具 | 检索计划、子查询、依赖顺序 | 分解错误、计划成本过高、来源选择错误 | [[Query Planning#证据锚点]] |
| [[Parallel Search and Explicit Merging 检索模式]] | 多 query 执行与证据归并 | 同一 reasoning step 并行检索，retrieval 后 merge | 当前 reasoning state、多视角 query、候选文档 | 去噪后的中间证据包 | query 数/Top-K 过大引入噪声，merge 漏掉关键证据 | [[Parallel Search and Explicit Merging 检索模式#证据锚点]] |
| [[Agentic Retrieval]] | 检索执行控制 | 多轮：plan -> search -> inspect -> refine | 任务、检索工具、候选结果、预算 | 多源证据包、检索 trace、综合上下文 | loop 不可控、延迟高、评估困难 | [[Agentic Retrieval#证据锚点]] |
| [[Agentic RAG]] | 端到端问答/研究流程 | Agent 决定何时检索、何时生成或重查 | 用户任务、工具、memory、retriever | 最终答案、工具轨迹、证据引用 | 把 retrieval 错误和生成错误耦合 | [[Agentic RAG#证据锚点]] |

## 最容易混淆的边界

### Query Rewrite vs Query Planning

[[Query Rewrite]] 主要改“怎么问”，例如把“它多少钱”改成“产品 A 2026 企业版价格”；[[Query Planning]] 改“先问什么、再问什么”，例如先查产品版本，再查价格页，再查地区限制。rewrite 可以是 planning 里的一个步骤，但 planning 不等于多写几个同义 query。

### Query Planning vs Agentic Retrieval

[[Query Planning]] 是计划本身；[[Agentic Retrieval]] 是带执行控制的检索层，可以运行计划、观察结果、调整子查询、选择不同 source。没有执行 loop 的静态计划不一定是 agentic retrieval。

### Parallel Search / Explicit Merging vs Query Planning

[[Query Planning]] 决定检索任务如何拆；Parallel Search 决定当前推理步是否从多个视角同时检索；Explicit Merging 决定 retrieval 后如何把候选证据压缩成下一步推理可用的信息。它们可以连续出现，但不要把“多发几个 query”直接等同于完整 planning。

### Agentic Retrieval vs Agentic RAG

[[Agentic Retrieval]] 的边界更窄，重点在检索层决策；[[Agentic RAG]] 更端到端，包含是否检索、怎样生成、是否反思、是否调用其它工具。一个系统可以只做 agentic retrieval，把生成交给普通 RAG prompt。

### Retriever vs Query 决策层

[[Retriever]] 是找到候选证据的组件；query rewrite / planning 是驱动 retriever 的策略层。把复杂 query 决策塞进 retriever 内部可以简化接口，但学习时要问清：谁改写 query？谁记录计划？谁评估中间结果？

## 执行时序 / 机制差异

```text
simple RAG:
question -> retrieve -> rerank -> answer

rewrite-enhanced RAG:
question -> rewrite -> retrieve -> rerank -> answer

planned retrieval:
question -> plan subqueries -> retrieve per subquery -> merge/rerank -> answer

parallel search with explicit merging:
question + reasoning state -> generate query A/B/C -> retrieve in parallel -> merge evidence -> answer or next search

agentic retrieval:
question -> plan -> retrieve -> inspect evidence -> refine/retrieve again -> package evidence -> answer
```

边界细节：越往 agentic retrieval 走，越需要 [[Trace]]、预算限制、失败样本和 [[RAG Evaluation]]，否则“聪明检索”会变成不可复现的高延迟黑箱。

## 学习类比（非证据）

可以把检索决策类比成问图书馆：Query Rewrite 是把问题说清楚，Query Planning 是决定要查哪些书架和顺序，Agentic Retrieval 是边查边看结果、必要时改路线。

类比边界：这只是学习类比（非证据），不代表论文、官方文档或具体产品内部真的按这个类比实现。

## 现代系统如何吸收或限制

现代企业搜索和 RAG 平台正在把 query rewrite、query decomposition、source selection、multi-query retrieval 和 result grounding 做成检索层能力。现代性状态是 **current-practice + frontier/watch**：简单 rewrite 和 hybrid search 已是常见工程实践；自动 query planning、跨源 agentic retrieval 和动态证据评价仍然依赖具体平台、数据源质量和 observability。

工程综合 / inference：当系统面对的是短问句、同义词和指代时，优先尝试 rewrite；当问题有明显子任务和多源依赖时，再引入 planning；当系统需要基于中间证据调整路径时，才值得进入 agentic retrieval。

## 什么时候用哪个判断

- 用户 query 模糊但任务简单：[[Query Rewrite]]。
- 问题需要多跳、多条件、多文档对比：[[Query Planning]]。
- 当前推理步需要覆盖多个表述、概念扩展或子问题证据：[[Parallel Search and Explicit Merging 检索模式]]。
- 检索过程需要观察结果、重试、切换数据源：[[Agentic Retrieval]]。
- 任务还需要工具调用、memory、反思或最终回答策略：[[Agentic RAG]] / [[Agent Workflow]]。
- 检索候选足够但排序差：先看 [[Reranking]]，不要误把排序问题当 planning 问题。

## 它们共同不是什么

- 不是事实校验本身；检索计划找到证据后仍要做 [[RAG Evaluation]] 和 citation 检查。
- 不是越 agentic 越好；简单 FAQ 引入多轮 planning 只会增加成本和不可控性。
- 不是替代 ingestion、chunking、metadata 和权限过滤的魔法层。
- 不是完整 Agent framework；它们只是 retrieval 决策/执行的一部分。

## 证据锚点

- 概念卡：[[Retriever#证据锚点]], [[Query Rewrite#证据锚点]], [[Query Planning#证据锚点]], [[Agentic Retrieval#证据锚点]], [[Agentic RAG#证据锚点]], [[Reranking#证据锚点]]。
- source notes：[[Azure AI Search Agentic Retrieval]], [[Microsoft RAG 官方文档]], [[Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging]]。
- 主题锚点：[[Retrieval 组件对比#证据锚点]], [[RAG 类型对比#证据锚点]], [[RAG 主题#证据锚点]], [[Parallel Search and Explicit Merging 检索模式#证据锚点]]。
- 证据边界：本页的“什么时候用哪个”是工程综合 / inference；具体平台对 agentic retrieval 的 API、限制和可观测字段需要复查官方文档。

- Evidence type: retrieval concept cards + Azure/Microsoft/source notes + engineering synthesis.
- Confidence: high for conceptual boundaries; medium for platform-specific agentic retrieval APIs.
- Boundary: 本页的使用建议是工程综合 / inference，不替代 Azure AI Search 或其他产品的具体能力边界。
## 复习触发

1. “把用户问题改得更清楚”和“把问题拆成多个检索步骤”有什么最小区别？
2. 一个 query planning 系统没有观察结果后重试的能力，为什么还不一定算 agentic retrieval？
3. 如果正确文档已经召回但排在第 30 位，应优先补 query planning 还是 reranking？为什么？
4. 多 query 并行检索为什么还需要 explicit merging？

## 相关链接

- [[RAG 主题]]
- [[Retriever]]
- [[Query Rewrite]]
- [[Query Planning]]
- [[Agentic Retrieval]]
- [[Agentic RAG]]
- [[Parallel Search and Explicit Merging 检索模式]]
- [[Hybrid Search]]
- [[Reranking]]
- [[RAG Evaluation]]
