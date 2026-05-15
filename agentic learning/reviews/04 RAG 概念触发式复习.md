---
type: review
topic:
  - rag
  - review
  - feynman
status: active
created: 2026-05-14
updated: 2026-05-14
source:
  - "[[RAG]]"
  - "[[RAG 主题]]"
  - "[[Retrieval 组件对比]]"
  - "[[RAG 类型对比]]"
  - "[[Context RAG Memory 对比]]"
  - "[[RAG Evaluation]]"
related:
  - "[[reviews/复习记录索引]]"
  - "[[RAG]]"
  - "[[RAG 主题]]"
  - "[[Document Ingestion]]"
  - "[[Retriever]]"
  - "[[Vector Database]]"
  - "[[Hybrid Search]]"
  - "[[Reranking]]"
  - "[[RAG Evaluation]]"
  - "[[Agentic RAG]]"
  - "[[GraphRAG]]"
  - "[[Context Engineering]]"
  - "[[Memory]]"
  - "[[02 问题池]]"
  - "[[05 Query 写回队列]]"
---

# 04 RAG 概念触发式复习

日期：2026-05-14

这页记录 [[RAG]] 的概念触发式复习：先保留我的原始解释，再用追问检查我能不能把 RAG 从“向量库 + LLM”推进到“可诊断、可引用、可评估的外部知识 pipeline”。它不是 raw evidence，也不替代 [[RAG]] 概念卡。

## 触发概念

- 概念：[[RAG]]
- 触发原因：RAG 已经有基础概念卡、主题页和组件 / 类型对比页；现在需要检查我是否真的能说清 pipeline、边界、失败诊断和复杂 RAG 形态的取舍。

## 目标

用费曼方式检查我是否真的理解 RAG：不是背 Retrieval-Augmented Generation 的缩写，而是能解释资料如何进入知识库、如何被检索和排序、如何进入上下文、答案如何被证据约束，以及为什么 RAG 仍然会错。

## 复习节奏规则

- 默认只做一轮追问：用来暴露主要误解和边界缺口。
- 如果第一轮仍有关键卡点，最多追加一轮第二轮追问；第二轮只聚焦 1-3 个最影响理解的缺口。
- 第二轮之后必须收束：只做总结、写回候选、补概念卡或加入 [[02 问题池]] / [[05 Query 写回队列]]，不再生成第三轮追问。
- 如果还没懂，说明材料或概念卡需要重写，而不是继续加问。

## 作答前最小边界

先不要把 RAG 解释成“接一个向量数据库”。更稳的入口是：

```text
source -> ingest / chunk / metadata / permission
      -> embedding / index
      -> retrieve / filter / hybrid search
      -> rerank / context assembly
      -> generate with evidence
      -> citation / evaluation / monitor
```

小边界：RAG 能把外部资料带入模型上下文，但不能保证资料完整、检索正确、排序合理、引用支持结论，或模型一定不会误读证据。

## 我的原始解释

>


## 我已经说对的点

- 待我回答后补。

## 需要更精确的点

- 待我回答后补。

## 第一轮追问

1. 请不用“向量库 + LLM”这句话，按资料入库、检索、上下文装配、生成 / 引用四步解释 RAG。
2. 为什么有 [[Vector Database]] 不等于有可靠 [[RAG]]？请举一个“向量库工作正常但答案仍然错”的例子。
3. [[Parametric Memory]]、[[Non-Parametric Memory]] 和 [[Retriever]] 在 RAG 里分别是什么角色？它们和 [[Memory]] / [[Context Engineering]] 的边界在哪里？
4. 如果一个 RAG 答案漏掉了 PDF 表格里的关键条件，你会按哪些层排查？先看模型、检索、chunking，还是 ingestion？为什么？
5. 什么时候普通 RAG 足够，什么时候才值得升级到 [[Agentic RAG]]、[[GraphRAG]] 或 [[Corrective RAG]]？请各给一个最小触发条件。

## 我的费曼回答区

### Q1：请不用“向量库 + LLM”这句话，按资料入库、检索、上下文装配、生成 / 引用四步解释 RAG。

我的回答：


反馈：


写回：


### Q2：为什么有 Vector Database 不等于有可靠 RAG？请举一个“向量库工作正常但答案仍然错”的例子。

我的回答：


反馈：


写回：


### Q3：Parametric Memory、Non-Parametric Memory 和 Retriever 在 RAG 里分别是什么角色？它们和 Memory / Context Engineering 的边界在哪里？

我的回答：


反馈：


写回：


### Q4：如果一个 RAG 答案漏掉了 PDF 表格里的关键条件，你会按哪些层排查？先看模型、检索、chunking，还是 ingestion？为什么？

我的回答：


反馈：


写回：


### Q5：什么时候普通 RAG 足够，什么时候才值得升级到 Agentic RAG、GraphRAG 或 Corrective RAG？请各给一个最小触发条件。

我的回答：


反馈：


写回：


## 写回候选

- [ ] 如果 Q1 只能说“向量库 + LLM”，回到 [[RAG]] / [[Retrieval 组件对比]] 补 pipeline 复述。
- [ ] 如果 Q2 卡住，把“向量库只是基础设施，不等于可靠 RAG”写回 [[Vector Database]] 或 [[Retrieval 组件对比]] 的复习材料。
- [ ] 如果 Q3 混淆 RAG / Memory / Context Engineering，回看 [[Context RAG Memory 对比]]，必要时把新的边界例子写回该页。
- [ ] 如果 Q4 不能分层诊断，把“RAG 错误排查路径”写入 [[02 问题池]] 或更新 [[RAG 主题#失败诊断路径]]。
- [ ] 如果 Q5 把高级 RAG 当成越复杂越好，回看 [[RAG 类型对比]]，把“升级触发条件”写成更短的判断卡。

## 第二轮触发（可选）

只有第一轮暴露关键误解时才追加第二轮。第二轮最多聚焦 1-3 个问题，例如：

> 我能不能在 60 秒内说清：RAG 的错误到底可能来自 ingestion、chunking、retrieval、reranking、context assembly、generation、citation、权限或 freshness 中的哪一层？

## 校准版（作答后对照）

RAG 是一种把外部可检索知识接入生成模型的架构模式。它的基本问题不是“让模型变聪明”，而是让模型能够使用参数以外、可更新、可引用、可治理的资料。经典边界是 [[Retriever]] + generator：用户问题先触发检索，从外部索引取回候选证据，再把这些证据组织进上下文，最后由模型生成回答。

现代 RAG 的学习重点是 pipeline，而不是单点组件。[[Document Ingestion]] 决定资料是否正确进库；[[Chunking]] 和 metadata 决定证据单元是否完整；[[Embedding]] / [[Vector Database]] / [[Hybrid Search]] / [[Retriever]] 决定候选能否被召回；[[Reranking]] 决定正确证据能否进入上下文预算；[[RAG Evaluation]]、citation faithfulness 和 access control 决定答案是否能被证据和权限约束。

RAG 的关键局限是：它把“模型不知道”转成“外部知识检索与上下文治理”问题。检索漏召回、chunk 切坏、权限标签丢失、rerank 排错、引用不支持结论、资料过期或检索内容带 prompt injection，都会让 RAG 生成更自信但仍然错误的答案。