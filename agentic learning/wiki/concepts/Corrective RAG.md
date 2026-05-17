---
type: concept
topic:
  - rag
  - evaluation
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-16
up:
  - "[[RAG]]"
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[Corrective Retrieval Augmented Generation]]"
  - "[[RAG 类型对比]]"
evidence:
  - "[[Corrective Retrieval Augmented Generation#为什么收]]"
  - "[[Corrective Retrieval Augmented Generation#一句话]]"
  - "[[Corrective Retrieval Augmented Generation#边界提醒]]"
  - "[[RAG 类型对比#一张表先抓住]]"
related:
  - "[[RAG]]"
  - "[[Retriever]]"
  - "[[Evaluation]]"
  - "[[Agentic Retrieval]]"
---

# Corrective RAG

## 一句话

Corrective RAG 是先评估检索证据质量，再决定直接生成、改写查询、重检索或走外部检索补救的 RAG 模式。

## 概念详解

Corrective RAG 解决的是 RAG 对检索质量高度依赖的问题。普通 RAG 如果检索到过期、无关或不完整文档，generator 很可能基于坏证据写出流畅但错误的答案。CRAG 这条方法线把 retrieval evaluator 放进流程：先判断检索结果是否足够可靠，再决定直接回答、改写 query、重检索、分解问题，或使用外部 web/search fallback。

它的关键不是“多搜几次”，而是基于证据质量评分的分支动作。检索结果高置信时可以生成；低置信时要补救；不确定时可能需要拆分文档、重新组合或请求其他来源。这个流程把检索失败从隐性错误变成可观察的判断节点，因此和 [[RAG Evaluation]]、trace、fallback policy 强相关。

和 [[Self-RAG]] 的边界：Self-RAG 原始论文强调模型通过 reflection tokens 学习是否检索、如何生成和批判；Corrective RAG 更偏系统流程里的 retrieval evaluator 与 corrective action。和 [[Agentic RAG]] 的边界：Corrective RAG 可以作为 Agentic RAG 的一个质量门节点，但不等于完整 agentic workflow。

现代性上，Corrective RAG 是 frontier/watch：论文方法给了清晰机制，但生产实现会根据场景选择 evaluator、阈值、fallback 来源、是否允许 web search、是否让人审。企业私有知识库尤其要注意：外部 web fallback 可能违反安全和数据边界。

## 它解决什么问题

RAG 的答案质量高度依赖检索质量。检索到错误、过少或不相关文档时，模型会基于坏证据生成看似合理的错答案。

Corrective RAG 把“检索质量判断”加入流程，让系统能在证据差时修正。

## 它不是什么

Corrective RAG 不是简单多搜几次。

关键在于 retrieval evaluator 和基于评分的分支动作。

## 最小例子

用户问一个项目细节：初次检索只找到旧文档；evaluator 判断证据不足；系统改写 query，并加入最新日期过滤；再检索后生成答案。

```text
retrieve -> grade evidence -> enough? -> answer / rewrite query / retrieve again / fallback
```

## 常见误解 / 风险

- evaluator 本身会错。
- 外部 web fallback 可能引入不可信来源。
- 分支越多，trace 越重要。
- Corrective RAG 更适合高准确性场景，不一定适合低延迟问答。

## 边界细节

Corrective RAG 的核心是“检索后质量门”，不是泛泛的多轮检索。

和 [[Reranking]] 的边界：reranking 重排候选；Corrective RAG 判断候选是否足够好，并可能触发新动作。

和 [[RAG Evaluation]] 的边界：RAG Evaluation 可以离线/在线评估整条链路；Corrective RAG 把一部分评估变成运行时控制节点。

## 现代性状态

- 判定：frontier / transitional-to-current-practice。
- 稳定部分：坏检索需要显式评估和补救，否则会放大错误。
- 易变部分：evaluator 实现、阈值、fallback 策略、web search 安全边界和框架节点。
- freshness: watch。
- last_checked: 2026-05-10。
- 复查点：当采用 CRAG-like workflow 时，要记录 evaluator 类型和 fallback 来源，不把论文机制泛化成所有重试 RAG。

## 现代系统怎么吸收 Corrective RAG 的价值

现代系统可以把 Corrective RAG 做成 retrieve 后的 gate：检查证据相关性、覆盖度、新旧程度和权限；证据不足时改写 query、扩大搜索、降级拒答或交给人工。它必须有 trace，否则补救路径无法复现。

## 证据锚点

- Source: [[Corrective Retrieval Augmented Generation]]
- Anchor: [[Corrective Retrieval Augmented Generation#为什么收]]
- Anchor: [[Corrective Retrieval Augmented Generation#一句话]]
- Anchor: [[Corrective Retrieval Augmented Generation#边界提醒]]
- Source: [[RAG 类型对比]]
- Anchor: [[RAG 类型对比#一张表先抓住]]
- Evidence type: paper source note + local comparison map + engineering synthesis.
- Confidence: medium
- Boundary: paper source supports retrieval evaluator and corrective actions; production fallback policy, thresholds and safety constraints are engineering synthesis.

## 复习触发

- Corrective RAG 为什么不是“多搜几次”？
- 它和 Self-RAG 的机制差异是什么？
- 企业私有知识库里 web fallback 有什么安全边界？

## 相关链接

- [[RAG]]
- [[Retriever]]
- [[Agentic Retrieval]]
- [[Evaluation]]
