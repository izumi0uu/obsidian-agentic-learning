---
type: concept
topic:
  - rag
  - retrieval
  - evaluation
  - llm
status: growing
created: 2026-05-15
updated: 2026-05-15
last_checked: 2026-05-15
freshness: stable
conflicts: []
source:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]"
  - "[[Azure AI Search Agentic Retrieval]]"
  - "[[Self-RAG - Learning to Retrieve Generate and Critique]]"
evidence:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#必读块 2：Figure 1 / retriever + generator 流程]]"
  - "[[Retriever#概念详解]]"
  - "[[Vector Database#概念详解]]"
  - "[[Reranking#概念详解]]"
  - "[[RAG Evaluation#概念详解]]"
  - "[[Self-RAG - Learning to Retrieve Generate and Critique#必读块 1：Abstract / adaptive retrieval]]"
related:
  - "[[Retriever]]"
  - "[[Vector Database]]"
  - "[[Reranking]]"
  - "[[RAG Evaluation]]"
  - "[[Self-RAG]]"
  - "[[Token]]"
---

# Top-K

## 一句话

Top-K 是“按分数排序后取前 K 个”的选择规则；在 RAG 检索里，它通常表示取前 K 个候选 chunk / passages，而在生成解码里，top-k 表示只从概率最高的 K 个 token 中采样。

## 概念详解

Top-K 本身不是某个数据库或 RAG 方法，而是一个非常小但很常见的排序/预算控制概念。系统先给候选对象打分，例如向量相似度、关键词相关性、reranker 分数或 token 概率，然后只保留分数最高的 K 个。K 是一个整数预算：它决定后续系统最多看多少候选。

在 RAG 里，Top-K 最常出现在 retrieval 阶段。[[Retriever]] 或 [[Vector Database]] 根据 query 找到相似候选，返回 top-k passages / chunks；随后系统可能再做 [[Reranking]]、去重、权限过滤、上下文装配和引用校验。经典 RAG source note 里，retriever + document index 会找 top-K 文档，再让 generator 基于检索文档生成答案。这说明 Top-K 是 RAG 地基流程的一部分，但它只负责候选截取，不负责证明证据足够。

K 的取值会影响召回、噪音、延迟、成本和上下文预算。K 太小，正确证据可能根本没进入候选集；K 太大，候选里会混入很多相似但不能回答问题的片段，后续 reranker、context builder 和 LLM 都要承担更多噪音。很多系统会先 retrieve top 50，再 rerank top 5 或 top 8；这个流程体现了“先扩大候选，再精排压缩”的工程取舍。

还要切开另一个混淆：retrieval Top-K 和 decoding top-k 不是一回事。retrieval Top-K 选择的是文档、chunk、passage 或记忆候选；decoding top-k 选择的是模型生成下一个 token 时允许参与采样的 token 候选。二者都叫 top-k，是因为形式上都是“取前 K 个”，但介入层完全不同。

## 它解决什么问题

Top-K 解决的是候选太多时的预算控制问题。检索系统不能把所有文档都塞进 prompt，生成模型也不能无限制地考虑所有可能输出。Top-K 用一个简单参数限制后续处理范围，让召回、排序、生成和评估可以在有限成本内运行。

## 它不是什么

Top-K 不是答案正确性的保证。相似度最高的 K 个候选可能都不能回答问题，也可能包含过期、无权限或被切坏的上下文。

Top-K 也不是 [[Reranking]]。Top-K 是取多少候选；reranking 是对候选重新排序。二者常连用，但责任不同。

Top-K 也不是 Hit@K。Top-K 是系统返回前 K 个候选的操作；Hit@K 是评估时检查正确证据是否出现在前 K 个候选里的指标。

## 最小例子

```text
query -> vector search top 20 -> rerank top 5 -> context -> answer
```

如果某次向量检索的相似度排序是：

| 候选 chunk | 相似度 |
|---|---:|
| A | 0.91 |
| B | 0.86 |
| C | 0.80 |
| D | 0.55 |

当 `top_k = 2` 时，只取 A 和 B。C 即使可能包含关键证据，也不会进入后续流程。

## 常见误解 / 风险

- 误解：Top-K 越大越好。更大的 K 会增加召回机会，也会增加噪音、成本和 Lost in the Middle 风险。
- 误解：Top-K 高分候选就等于可引用证据。相似不等于支持结论。
- 误解：答案错了就把 K 调大。很多错误来自 chunking、metadata、权限、query rewrite、rerank 或生成误读。
- 风险：先 ANN 再过滤可能让 Top-K 名额被无权限或不符合 metadata 的候选占掉。
- 风险：固定 Top-K 不适合所有问题；复杂问题可能需要 query planning、多源检索或自适应检索。

## 边界细节

和 [[Retriever]] 的边界：retriever 是找候选的组件；Top-K 是 retriever 常用的候选数量参数。

和 [[Vector Database]] 的边界：向量数据库负责存储和搜索向量；Top-K 是一次向量搜索返回多少近邻。

和 [[Reranking]] 的边界：reranker 可以把 retrieve top 50 压成 rerank top 5，但如果正确证据没有被初检召回，reranker 不能凭空找回。

和 [[RAG Evaluation]] 的边界：评估时要看 retrieval recall、precision、top-k 命中和 rerank 后命中。Top-K 参数本身不是评价结果。

和 [[Self-RAG]] / [[Agentic Retrieval]] 的边界：Self-RAG 和 agentic retrieval 都是在回应固定单次 Top-K 的局限。它们让系统判断是否检索、拆出子查询、选择知识源或按需重查，而不是永远固定一次 query + top-k。

和 decoding top-k 的边界：decoding top-k 属于生成控制，限制模型下一个 token 的候选集合；retrieval Top-K 属于检索控制，限制进入上下文的外部证据候选。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：按分数取前 K 个候选，是检索、排序、评估和解码中的基础操作。
- 易变部分：K 的经验值、动态 K、fusion 策略、reranker 阈值、产品 API 参数名和具体评估指标会变化。
- 复查点：看到系统调 Top-K 时，先问它调的是 retrieval 候选数、rerank 保留数，还是 decoding token 采样范围。

## 现代系统怎么吸收 Top-K 的价值 / 局限

现代 RAG 系统不会只记录最终答案，还会在 trace 里保存 query、filter、Top-K 候选、分数、rerank 前后排序、进入上下文的最终 chunk 和引用。这样答案错时才能判断：是 K 太小漏召回、K 太大引入噪音、reranker 排错，还是生成模型忽略了证据。

更成熟的系统还会按任务动态调整 K：简单事实问题用较小 K，复杂比较问题先做 query planning 或多路召回，再用 reranking 和 evaluation 控制进入上下文的证据量。Top-K 的价值是让候选集合可控；它的局限是不能替代证据质量判断。

## 证据锚点

- Source: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]
- Anchor: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#必读块 2：Figure 1 / retriever + generator 流程]]
- Concept anchor: [[Retriever#概念详解]]
- Concept anchor: [[Vector Database#概念详解]]
- Concept anchor: [[Reranking#概念详解]]
- Concept anchor: [[RAG Evaluation#概念详解]]
- Source: [[Azure AI Search Agentic Retrieval]]
- Anchor: [[Azure AI Search Agentic Retrieval#为什么收]]
- Source: [[Self-RAG - Learning to Retrieve Generate and Critique]]
- Anchor: [[Self-RAG - Learning to Retrieve Generate and Critique#必读块 1：Abstract / adaptive retrieval]]
- Evidence type: RAG paper source note + official docs source note + existing concept-card synthesis + engineering synthesis.
- Confidence: medium-high for retrieval Top-K boundary; medium for decoding top-k boundary because本卡只做混淆提醒，不展开 generation control 全部参数。
- Boundary: 本卡不推荐固定 K 值；K 的设置应由语料、任务、context budget、latency/cost 和 RAG Evaluation 决定。

## 复习触发

1. retrieval Top-K 和 decoding top-k 的区别是什么？
2. 为什么“把 Top-K 调大”不能自动修复 RAG 错误？
3. retrieve top 50 -> rerank top 5 和直接 retrieve top 5 的差别是什么？
4. Hit@K 为什么是评估指标，而不是检索动作本身？

## 相关链接

- [[Retriever]]
- [[Vector Database]]
- [[Reranking]]
- [[RAG Evaluation]]
- [[Self-RAG]]
- [[Agentic Retrieval]]
- [[Token]]
- [[RAG 主题]]
- [[Retrieval 组件对比]]
