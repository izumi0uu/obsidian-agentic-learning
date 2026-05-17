---
type: concept
topic:
  - rag
  - evaluation
status: growing
created: 2026-05-16
updated: 2026-05-16
last_checked: 2026-05-16
freshness: stable
aliases:
  - 上下文精确率
  - context precision
source:
  - "[[raw/repos/xiaolinnote/questions/031 ai rag 18. 怎么量化你的 RAG 效果？]]"
  - "[[raw/repos/agent_java_offer/questions/094 01_AI 03_RAG 如何全面地评估一个 RAG 系统的性能？请分别从检索和生成两个阶段提出评估指标。]]"
evidence:
  - "[[raw/repos/xiaolinnote/questions/031 ai rag 18. 怎么量化你的 RAG 效果？#RAGAs：生成质量评估框架]]"
  - "[[raw/repos/xiaolinnote/questions/031 ai rag 18. 怎么量化你的 RAG 效果？#如何根据指标定位问题？]]"
  - "[[raw/repos/agent_java_offer/questions/094 01_AI 03_RAG 如何全面地评估一个 RAG 系统的性能？请分别从检索和生成两个阶段提出评估指标。#2. 子问题：如何全面地评估一个 RAG 系统的性能？请分别从检索和生成两个阶段提出评估指标。]]"
up:
  - "[[RAG Evaluation]]"
relations:
  - type: paired_with
    target: "[[Context Recall]]"
    note: Context Precision 看检索上下文的相关性和排序质量；Context Recall 看必要信息是否被覆盖。
related:
  - "[[RAG Evaluation]]"
  - "[[Context Recall]]"
  - "[[Reranking]]"
  - "[[Retriever]]"
  - "[[RAG Citation Faithfulness]]"
---

# Context Precision

## 一句话

Context Precision（上下文精确率）是 RAG evaluation 指标，用来衡量检索上下文里相关内容是否足够靠前、噪音是否过多。

## 概念详解

Context Precision 关注的是“找到的内容是否有用，是否排在该读的位置”。RAG 不只是要把必要证据找回来，还要把上下文预算留给真正相关的片段。如果检索返回 10 个 chunk，其中 2 个相关但排在后面，前面都是相似但无用的噪音，模型很容易被稀释注意力或误导。

source note 把 Context Precision 和 [[Context Recall]] 配对：Recall 看该找的信息有没有找全；Precision 看找回来的内容是否相关、是否在前面。Context Precision 低时，优化方向通常不是盲目扩大 top-k，而是加强 [[Reranking]]、减少最终进入 LLM 的 chunk 数、改进 chunking 或过滤噪音。

这个指标需要参考答案、相关文档标注或 judge 规则支撑。没有标准证据时，Context Precision 容易变成“看起来相关”的主观判断。它也不直接证明最终回答正确；它只是证明上下文质量更适合生成。

工程上看，Context Precision 不是单纯追求少返回文档，而是追求“进入 prompt 的证据密度”。一个系统可能 recall 很高，却把必要 chunk 和大量相似噪音一起塞给模型；这会让模型在长上下文里错读优先级，甚至引用无关片段。提高 precision 的手段包括 reranking、chunk 去重、metadata 过滤、问题分解后分别检索、以及把最终上下文控制在答案真正需要的证据范围内。

因此它更像上下文治理指标，而不是单一检索器指标。

它回答的是“有限窗口里有多少是该看的证据”。
## 它解决什么问题

它解决“检索结果里噪音太多、相关证据排序不够靠前”的问题。它帮助区分：答案错是因为没找全，还是找到了但上下文太脏/排序太差。

## 它不是什么

Context Precision 不是 [[Context Recall]]。Precision 看相关性和排序；Recall 看覆盖完整性。

它不是 [[Reranking]]。Reranking 是优化排序的手段；Context Precision 是评估排序/上下文质量的指标。

它也不是最终 answer correctness。模型可能拿到高精度上下文但仍然生成错误解释。

## 最小例子

```text
query: 退款多久到账？
检索结果 top 5:
1. 退货包装要求（无关）
2. 退款到账时间（相关）
3. 售后电话（弱相关）
4. 退款异常处理（相关）
5. 会员积分说明（无关）
=> 有相关内容，但排序和噪音会拉低 Context Precision
```

## 常见误解 / 风险

- 只看有没有召回到相关 chunk，不看相关 chunk 排第几。
- 为了提高 precision 过度减少上下文，导致 recall 下降。
- 用 LLM judge 打分却没有人工抽样校准。
- 把“上下文精确率”误理解为最终答案精确率。

## 边界细节

和 [[Context Recall]] 的边界：Recall 低说明漏证据；Precision 低说明噪音多或排序差。

和 [[Reranking]] 的边界：reranking 可以提升 context precision，但不能保证 recall。

和 [[RAG Citation Faithfulness]] 的边界：context precision 看输入上下文；citation faithfulness 看输出答案和引用的支持关系。

## 现代性状态

- 判定：current-practice。
- 稳定部分：RAG 需要衡量上下文相关性、排序和噪音。
- 易变部分：指标计算、judge prompt、标注标准和平台实现会变化。

## 证据锚点

- [[raw/repos/xiaolinnote/questions/031 ai rag 18. 怎么量化你的 RAG 效果？#RAGAs：生成质量评估框架]]
- [[raw/repos/xiaolinnote/questions/031 ai rag 18. 怎么量化你的 RAG 效果？#如何根据指标定位问题？]]
- [[raw/repos/agent_java_offer/questions/094 01_AI 03_RAG 如何全面地评估一个 RAG 系统的性能？请分别从检索和生成两个阶段提出评估指标。#2. 子问题：如何全面地评估一个 RAG 系统的性能？请分别从检索和生成两个阶段提出评估指标。]]

- Evidence type: RAG evaluation interview notes + metric-boundary synthesis.
- Boundary: Context Precision 衡量上下文相关性/排序质量，不等于最终答案正确率，也不能替代 Context Recall。
## 复习触发

1. Context Precision 低但 Context Recall 高时，说明什么？
2. 为什么 reranking 常用来改善 Context Precision？
3. Context Precision 和 answer correctness 为什么不能画等号？

## 相关链接

- [[RAG Evaluation]]
- [[Context Recall]]
- [[Reranking]]
- [[RAG Citation Faithfulness]]

