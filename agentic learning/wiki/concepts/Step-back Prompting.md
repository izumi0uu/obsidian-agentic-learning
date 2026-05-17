---
type: concept
topic:
  - rag
  - retrieval
  - prompting
  - reasoning
status: growing
created: 2026-05-17
updated: 2026-05-17
last_checked: 2026-05-17
freshness: stable
aliases:
  - Step Back Prompting
  - step-back prompting
  - Step-back
  - Step Back
  - 后退提问
  - 后退一步提问
source:
  - "[[raw/repos/xiaolinnote/questions/025 ai rag 12. 如何润色用户的 Query（Query Rewrite）？目的是什么？]]"
  - "https://arxiv.org/abs/2310.06117"
evidence:
  - "[[raw/repos/xiaolinnote/questions/025 ai rag 12. 如何润色用户的 Query（Query Rewrite）？目的是什么？#方法三：Step-back Prompting（后退提问）]]"
  - "https://arxiv.org/abs/2310.06117"
related:
  - "[[Query Rewrite]]"
  - "[[HyDE]]"
  - "[[Multi-Query Retrieval]]"
  - "[[Query Planning]]"
  - "[[Prompt]]"
  - "[[Plan-and-Solve Prompting]]"
  - "[[RAG Evaluation]]"
---

# Step-back Prompting

## 一句话

Step-back Prompting 是让模型先把具体问题“后退一步”抽象成更高层的问题、概念或第一性原理，再用这些背景知识帮助回答原问题的 prompting / retrieval strategy。

## 概念详解

有些问题不是缺少同义词，也不是 query 太口语，而是太具体：知识库里可能没有“这个具体 bug 为什么在这个版本出现”的直接答案，但有相关背景原理、组件机制或政策条款。Step-back Prompting 的做法是先生成一个更抽象、更通用的 step-back question，例如从“LangGraph 的 interrupt 为什么能恢复人工审批”后退成“可恢复执行系统如何通过 checkpoint 保存状态”。系统先检索或推理这个背景问题，再回到原问题。

论文《Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models》把 Step-back Prompting 描述为一种让 LLM 从带有具体细节的实例中抽象出高层概念和第一性原理的技术，再用这些概念和原理引导推理。它的原始论文重点不只在 RAG，而是在 reasoning-intensive tasks；RAG 工程吸收的是其中的“先抽象背景，再带回具体问题”的查询侧价值。

在检索系统里，Step-back Prompting 可以作为 [[Query Rewrite]] 的相邻子策略：它不只是换一个说法，而是把查询目标提升到背景层。这个边界很容易被忽略：如果 step-back 后只查到宽泛背景，却没有把原问题的实体、版本、条件带回来，答案会变得正确但不贴题。

一个可靠的 step-back 链路通常分成两条线：一条保留原始 query，负责约束实体、版本、时间、否定词和用户真正的问题；另一条生成 step-back question，负责检索背景概念、机制或原则。最终回答必须把两条线重新合并：背景证据解释“为什么”，原始 query 约束“这次具体怎么答”。如果只有背景线，系统容易产出泛泛而谈的解释；如果只有原始线，系统又可能找不到足够的原理材料。

Step-back 的学习价值在于提醒我们：检索失败不总是“表达不规范”或“Top-K 太小”。有时是问题的抽象层级不对。用户问的是一个具体症状，但知识库按原理、政策、架构层组织；这时直接生成更多同层 query 可能仍然围着症状打转，而后退一步能把检索带到更可解释的背景文档。

## 它解决什么问题

它解决“具体问题没有直接匹配文档，但背景知识能帮助回答”的问题。对技术文档、政策说明、原理型问答和多跳推理，step-back query 可以先找原理、定义、约束或上下文，再用它们解释具体案例。

## 它不是什么

Step-back Prompting 不是 [[HyDE]]。HyDE 生成的是假设文档/答案用于 embedding 检索；Step-back 生成的是更抽象的背景问题或原则问题。

它不是 [[Query Planning]] 的全部。Step-back 可以成为 query plan 的一个步骤，但它本身不负责多源选择、依赖顺序、循环重试或结果合并。

它也不是简单“把问题说得更泛”。抽象必须能回到原始约束，否则会丢题。

## 最小例子

```text
原始问题：为什么这个 API 在异步任务里需要 checkpoint 才能人工审批？
step-back question：可恢复执行系统为什么需要把任务状态持久化？
检索：查 durable execution / checkpoint / human-in-the-loop 背景
回答：再回到原 API 的异步任务与人工审批语境
```

## 常见误解 / 风险

- 误解：越抽象越聪明。抽象过头会丢掉用户真正问的实体、版本和限制。
- 误解：Step-back 是 RAG 专用技术。它首先是一种抽象式 prompting 技术，只是在 RAG 中可用来生成背景检索问题。
- 风险：背景文档很权威，但和原问题不完全对应，导致答案看似有理却不贴证据。
- 风险：把 step-back question 替代原始 query，而不是与原 query 一起保留和对齐。

## 边界细节

和 [[Query Rewrite]] 的边界：Query Rewrite 通常改表达；Step-back 改抽象层级。它可以归入广义 query-side strategy，但不是 Query Rewrite 的普通同义改写。

和 [[Multi-Query Retrieval]] 的边界：Multi-query 生成多个同层视角；Step-back 生成更高层背景视角。一个系统可以同时发原 query、step-back query 和多个同层 query，但合并时要记录每条 evidence 回答的是哪个层级的问题。

和 [[Plan-and-Solve Prompting]] 的边界：Plan-and-Solve 先显式规划求解步骤；Step-back 先抽象背景原理。一个强调任务步骤，一个强调概念/原理层级。

## 现代性状态

- 判定：current-practice / research-informed。
- 为什么：Step-back Prompting 有 ICLR 2024 论文支撑，并被工程实践吸收为复杂问答的 query/reasoning trick；但它不是所有任务的默认检索策略。
- 稳定部分：先抽象高层问题或原则，再用背景指导具体回答。
- 易变部分：step-back question 的生成方式、是否检索、如何与原 query 合并、如何评价“抽象是否有用”。
- 复查点：在生产 RAG 中应比较 step-back route 对复杂问答准确率、引用支持和延迟的净收益。

## 现代系统怎么吸收 Step-back Prompting 的价值 / 局限

现代系统更适合把 Step-back 当作可观测 route：trace 里记录原 query、step-back query、背景证据和最终答案中哪些结论来自背景证据。这样失败时能判断是抽象层级错了，还是背景证据正确但没有回到原问题。

它的局限是“背景正确不等于回答正确”。检索到原理后，还要把原问题中的实体、版本、权限、时间和例外条件重新带回来；否则系统会产生通用但不够 grounded 的答案。

## 证据锚点

- Source anchor: [[raw/repos/xiaolinnote/questions/025 ai rag 12. 如何润色用户的 Query（Query Rewrite）？目的是什么？#方法三：Step-back Prompting（后退提问）]]
- Paper: Zheng et al., “Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models”, arXiv:2310.06117 / ICLR 2024, <https://arxiv.org/abs/2310.06117>。
- Evidence type: paper abstract + interview raw source note + engineering synthesis.
- Confidence: high for mechanism; medium for RAG-specific production benefit without local eval.
- Boundary: 论文支持的是 abstraction-guided reasoning；本卡的 RAG 用法是把该思想吸收到 query-side retrieval strategy 中。

## 复习触发

1. Step-back Prompting 和 HyDE 分别生成什么？
2. 为什么 step-back 后必须回到原始 query 的约束？
3. 什么场景更适合 step-back，而不是普通 rewrite 或 multi-query？

## 相关链接

- [[Query Rewrite]]
- [[HyDE]]
- [[Multi-Query Retrieval]]
- [[Query Planning]]
- [[Plan-and-Solve Prompting]]
- [[RAG Evaluation]]
