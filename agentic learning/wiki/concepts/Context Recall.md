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
  - 上下文召回率
  - context recall
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
    target: "[[Context Precision]]"
    note: "Context Recall 看该找的信息有没有覆盖；Context Precision 看找回内容里相关信息是否靠前、噪音是否过多。"
related:
  - "[[RAG Evaluation]]"
  - "[[Context Precision]]"
  - "[[Retriever]]"
  - "[[Reranking]]"
  - "[[RAG Citation Faithfulness]]"
---

# Context Recall

## 一句话

Context Recall（上下文召回率）是 RAG evaluation 指标，用来衡量回答问题所需的信息有多少被检索结果覆盖到了。

## 概念详解

Context Recall 关注的是“该找的有没有找全”。在 RAG 中，最终答案依赖模型看到的上下文；如果关键证据没有进入上下文，生成模型再强也只能猜。Context Recall 因此把评估点放在检索结果/输入上下文上：和参考答案或标准证据相比，必要信息是否被找回。

它和传统信息检索里的 recall 有相通直觉，但落在 RAG 场景里时，更强调“生成答案所需的 supporting information 是否进入了上下文”。xiaolinnote source note 把 Context Recall 放在 RAGAS 的核心指标中，并说明低 Context Recall 通常意味着检索层没有召回正确内容，优化方向可能是改 embedding、调 [[Chunking]]、加 [[Multi-Route Retrieval]] 或补 query rewrite。

Context Recall 需要标准答案、标准证据或人工标注，否则很容易变成主观印象。它不是最终答案正确性的全部：上下文召回够高，模型仍可能误读、幻觉或引用不支持结论；这还需要 faithfulness、citation 和 generation-side evaluation。

## 它解决什么问题

它解决 RAG 排错里的“有没有把必要证据找回来”问题。答案错时，如果 Context Recall 低，优先查检索和索引链路，而不是先调 prompt 或换生成模型。

## 它不是什么

Context Recall 不是普通“召回层”的同义词，也不是候选数量越多越好。

它不是 [[Context Precision]]。Recall 看覆盖是否完整；precision 看检索结果是否相关、是否排得靠前、噪音是否过多。

它也不是 answer faithfulness。模型可能拿到了正确上下文但仍然生成不忠实答案。

## 最小例子

```text
问题：退款多久到账？
标准证据需要：退款流程 + 到账时间 + 特殊情况
检索上下文只包含：退款流程 + 特殊情况
=> Context Recall 不足，因为到账时间缺失
```

## 常见误解 / 风险

- 以为 top-k 越大 Context Recall 一定越好；过大 top-k 会带来噪音和上下文稀释。
- 没有 ground truth 就给 recall 打确定分。
- 把 Context Recall 当成最终答案质量指标，忽略模型是否忠实使用证据。
- 把“上下文召回率”误链接到普通检索路线或业务召回。

## 边界细节

和 [[Context Precision]] 的边界：Context Recall 低说明漏证据；Context Precision 低说明噪音/排序问题更明显。

和 [[Retriever]] 的边界：retriever 是找候选的组件；Context Recall 是评估候选是否覆盖必要信息的指标。

和 [[RAG Citation Faithfulness]] 的边界：Context Recall 看证据是否在上下文；citation faithfulness 看答案引用是否真正支持结论。

## 现代性状态

- 判定：current-practice。
- 稳定部分：RAG 需要分层评估检索覆盖和生成忠实性。
- 易变部分：RAGAS、ARES、TruLens 等框架的具体计算和 judge 实现会变化。

## 证据锚点

- [[raw/repos/xiaolinnote/questions/031 ai rag 18. 怎么量化你的 RAG 效果？#RAGAs：生成质量评估框架]]
- [[raw/repos/xiaolinnote/questions/031 ai rag 18. 怎么量化你的 RAG 效果？#如何根据指标定位问题？]]
- [[raw/repos/agent_java_offer/questions/094 01_AI 03_RAG 如何全面地评估一个 RAG 系统的性能？请分别从检索和生成两个阶段提出评估指标。#2. 子问题：如何全面地评估一个 RAG 系统的性能？请分别从检索和生成两个阶段提出评估指标。]]

## 复习触发

1. Context Recall 低时，优先排查哪几层？
2. 为什么 Context Recall 高不等于最终答案忠实？
3. Context Recall 和 Context Precision 怎么配合定位问题？

## 相关链接

- [[RAG Evaluation]]
- [[Context Precision]]
- [[Retriever]]
- [[RAG Citation Faithfulness]]

