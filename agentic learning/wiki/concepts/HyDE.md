---
type: concept
topic:
  - rag
  - retrieval
  - query
status: growing
created: 2026-05-17
updated: 2026-05-17
last_checked: 2026-05-17
freshness: stable
aliases:
  - Hypothetical Document Embeddings
  - Hypothetical Document Embedding
  - 假设文档嵌入
  - 假想文档嵌入
source:
  - "[[raw/repos/xiaolinnote/questions/025 ai rag 12. 如何润色用户的 Query（Query Rewrite）？目的是什么？]]"
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？]]"
  - "[[raw/repos/agent_java_offer/questions/077 01_AI 03_RAG 除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？]]"
  - https://arxiv.org/abs/2212.10496
evidence:
  - "[[raw/repos/xiaolinnote/questions/025 ai rag 12. 如何润色用户的 Query（Query Rewrite）？目的是什么？#方法二：HyDE（Hypothetical Document Embeddings）]]"
  - "[[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第二层：查询优化]]"
  - "[[raw/repos/agent_java_offer/questions/077 01_AI 03_RAG 除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？#2. 子问题：除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？]]"
  - https://arxiv.org/abs/2212.10496
related:
  - "[[Query Rewrite]]"
  - "[[Dense Retrieval]]"
  - "[[Embedding]]"
  - "[[Retriever]]"
  - "[[Multi-Query Retrieval]]"
  - "[[Step-back Prompting]]"
  - "[[RAG Evaluation]]"
---

# HyDE

## 一句话

HyDE（Hypothetical Document Embeddings）是先让 LLM 根据 query 生成一段“假设文档 / 假设答案”，再嵌入这段文本去检索真实文档的 query-side retrieval 策略。

## 概念详解

普通向量检索常把用户问题直接编码成 query embedding，再去找相似文档。但问题文本和知识库文档往往不是同一种文体：用户问的是“怎么退货”，文档写的是“售后服务流程”；用户问的是问题句，文档是陈述句。HyDE 的核心直觉是先让 LLM 生成一个看起来像目标文档的假设性文本，再用这个“更像文档”的文本作为检索代理。

论文《Precise Zero-Shot Dense Retrieval without Relevance Labels》把 HyDE 放在 zero-shot dense retrieval 场景里：没有相关性标注时，先用 instruction-following LLM 生成 hypothetical document，再用无监督对比学习得到的 encoder 把这段文档编码成向量，最后在真实语料库的 embedding space 里找邻近文档。这个机制的关键不是“相信假设文档的事实”，而是利用它捕捉相关性模式；错误细节应该在真实语料检索和后续证据校验中被过滤。

在 RAG 工程里，HyDE 通常被吸收到 [[Query Rewrite]] / query transformation 家族：它不是简单把 query 写得更规范，而是把问题临时转成“可能的答案/文档形态”。因此它适合处理问题文本和文档文本风格差异很大的场景；如果领域很开放、LLM 生成方向容易跑偏，HyDE 反而可能把检索带向错误邻域。

HyDE 的实际链路通常有四步：保留原始 query；用 LLM 生成一个短的 hypothetical document；对这段文本做 embedding；用该向量检索真实文档。成熟实现还会把原始 query route 和 HyDE route 一起跑，再用去重、RRF、rerank 或 citation check 收敛证据。这样做的原因是 HyDE 的优势和风险来自同一个地方：它能补齐 query 没写出的“答案形态”，也可能把模型脑补的错误方向放大成检索偏置。

它和普通 query expansion 的差别在输出粒度。query expansion 可能只是补关键词、同义词或多个短 query；HyDE 的输出更像一段文档，因此更适合 dense retrieval 的文体对齐。这个区别也解释了为什么 HyDE 不一定适合所有检索系统：如果系统主要依赖 BM25、代码符号、精确 ID 或强 metadata filter，生成一段自然语言假设答案未必比保留原始词项更好。

## 它解决什么问题

HyDE 解决的是“query 和 document 在向量空间里不够近”的问题，尤其是问题句、口语化表达、短 query 和长文档段落之间的文体差异。它让检索从“用问题找答案”变成“用一个像答案的代理文本找真实答案文档”。

## 它不是什么

HyDE 不是答案生成。它生成的 hypothetical document 只是检索代理，不应该被当作最终事实。

HyDE 不是 [[Multi-Query Retrieval]]。Multi-query 是生成多个查询视角；HyDE 是生成一段假设文档并嵌入它。两者可以组合，但机制不同。

HyDE 也不是 [[Reranking]]。它改变候选召回的 query representation；reranking 只重排已经召回的候选。

## 最小例子

```text
原始问题：怎么申请退款？
HyDE 生成的假设文档：用户可以在订单详情页提交售后申请，选择退款原因并上传凭证...
检索动作：embed(假设文档) -> dense retrieval -> 找到真实的售后流程文档
```

关键边界：这段假设文档即使写错了某些细节，也不能直接进入答案；它只负责把检索带到可能相关的真实文档附近。

## 常见误解 / 风险

- 误解：HyDE 生成的内容越详细越好。实际风险是细节越多，越可能把检索带向错误事实。
- 误解：HyDE 能替代证据。它只改检索入口，最终回答仍要基于真实文档。
- 风险：开放域、跨主题或用户约束很强的问题里，LLM 的假设答案可能过度补全意图。
- 风险：如果只检索 HyDE 文本、不保留原始 query，可能丢掉实体名、版本号、否定词或权限限制。

## 边界细节

和 [[Query Rewrite]] 的边界：HyDE 是 Query Rewrite / query transformation 家族里的一个子策略，但不是 Query Rewrite 的同义词。普通 rewrite 改“问法”；HyDE 生成“像答案/文档的代理文本”。

和 [[Step-back Prompting]] 的边界：HyDE 把问题转成假设答案；Step-back 把问题抽象成背景问题。前者处理文体/表示差异，后者处理“具体问题缺直接文档、需要背景原理”的差异。

和 [[Dense Retrieval]] 的边界：HyDE 常服务 dense retrieval，因为它依赖 embedding space 中的邻近关系；但 dense retrieval 是检索路线，HyDE 是 query-side 生成代理。

## 现代性状态

- 判定：current-practice / transitional。
- 为什么：HyDE 是已有论文支持、也常被 RAG 工程吸收的检索前策略；它不是前沿噱头，但效果高度依赖领域、生成模型和 embedding encoder。
- 稳定部分：先生成 hypothetical document，再用其 embedding 检索真实文档。
- 易变部分：生成 prompt、生成长度、是否与原 query 合并、encoder 类型、是否 rerank 和评估方式。
- 复查点：如果系统引入更强 embedding、hybrid search 或 reranker，要重新比较 HyDE 对 recall / precision / latency 的净收益。

## 现代系统怎么吸收 HyDE 的价值 / 局限

现代 RAG 系统通常不会只相信 HyDE 的输出，而会把原始 query、HyDE query、召回结果、rerank 分数和最终引用都写入 trace。上线前应做 A/B eval：原 query、普通 rewrite、HyDE、多 query 分别对 recall、precision、引用忠实性和延迟有什么影响。

更稳的实现会把 HyDE 当成候选 route：原 query 保留，HyDE route 只增加召回覆盖，后面用去重、RRF、rerank 和 citation check 控制噪声。这个小边界很重要：HyDE 是“多找一些可能证据”的工具，不是“先编一个答案再相信它”的工具。

## 证据锚点

- Source anchor: [[raw/repos/xiaolinnote/questions/025 ai rag 12. 如何润色用户的 Query（Query Rewrite）？目的是什么？#方法二：HyDE（Hypothetical Document Embeddings）]]
- Source anchor: [[raw/repos/xiaolinnote/questions/027 ai rag 14. RAG 检索优化策略有哪些？#第二层：查询优化]]
- Source anchor: [[raw/repos/agent_java_offer/questions/077 01_AI 03_RAG 除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？#2. 子问题：除了基础的向量检索，你还知道哪些可以提升 RAG 检索质量的技术？]]
- Paper: Gao et al., “Precise Zero-Shot Dense Retrieval without Relevance Labels”, arXiv:2212.10496, <https://arxiv.org/abs/2212.10496>。
- Evidence type: paper abstract + interview raw source notes + engineering synthesis.
- Confidence: high for mechanism; medium for production benefit without local eval.
- Boundary: 本卡把 HyDE 当作 retrieval/query-side strategy；论文的 zero-shot dense retrieval setting 不等于所有 RAG 系统都应该默认开启 HyDE。

## 复习触发

1. HyDE 为什么不应该把生成文本当作答案？
2. HyDE 和 Multi-Query Retrieval 的最小机制差异是什么？
3. 什么场景下 HyDE 会把检索带偏？

## 相关链接

- [[Query Rewrite]]
- [[Step-back Prompting]]
- [[Multi-Query Retrieval]]
- [[Dense Retrieval]]
- [[Retriever]]
- [[RAG Evaluation]]
