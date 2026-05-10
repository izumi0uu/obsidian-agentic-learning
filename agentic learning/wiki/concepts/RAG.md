---
type: concept
topic:
  - rag
  - knowledge-base
status: seed
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]"
evidence:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#为什么收]]"
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#需要我读的内容]]"
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#Ingest 摘要]]"
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#边界提醒]]"
related:
  - "[[LLM]]"
  - "[[Memory]]"
  - "[[Evaluation]]"
  - "[[Retriever]]"
  - "[[Parametric Memory]]"
  - "[[Non-Parametric Memory]]"
  - "[[RAG Evaluation]]"
  - "[[Agentic RAG]]"
  - "[[Document Ingestion]]"
---

# RAG

## 一句话

RAG 是 Retrieval-Augmented Generation：先从外部知识库检索相关内容，再让模型基于这些内容生成回答。

## 它解决什么问题

RAG 让系统可以使用模型参数以外的知识，例如公司的文档、个人笔记、最新资料或领域数据库。

经典 RAG 论文把模型参数里的知识称为 [[Parametric Memory]]，把外部可检索知识称为 [[Non-Parametric Memory]]。RAG 的关键就是让生成模型通过 [[Retriever]] 使用外部知识，而不是只依赖训练时写进参数里的事实。

它解决的不是“让模型变聪明”这个泛问题，而是知识访问问题：知识需要更新、需要引用来源、需要接入私有语料，或者模型参数里根本没有这部分资料。

## 它不是什么

RAG 不是长期记忆的全部。RAG 通常从外部索引里检索文档；[[Memory]] 还可能包含用户偏好、会话状态、经验总结、任务轨迹或 profile。

RAG 不是把资料全部复制进 prompt。关键是检索、排序、上下文组织和生成之间的架构关系。

RAG 也不是事实正确性的保证。检索可能漏掉资料，资料本身可能过期，chunk 可能切错，rerank 可能排错，模型也可能误读检索结果。

## 最小例子

```text
用户问题 -> query rewrite -> 检索相关笔记 -> rerank -> 拼入上下文 -> LLM 生成回答 -> 引用来源或链接
```

Obsidian 场景：用户问“Agent 和 workflow 的区别是什么？”系统先检索 [[Agent]]、[[Agent Workflow]]、[[Agent Loop]] 等概念卡，再基于这些卡回答并给出双链。

## 常见误解 / 风险

- 误解：接了向量库就是 RAG。没有好的 ingestion、chunking、metadata、retrieval、reranking、引用和评估，向量库只是其中一层。
- 误解：RAG 一定比长上下文好。小资料集或一次性问题可能直接放上下文更简单；RAG 适合知识库较大、常更新、需要检索和引用的场景。
- 风险：错误文档被检索到后，模型会生成更自信的错误答案。
- 风险：私有知识库可能引入权限和数据泄露问题，尤其是 Agent 能继续行动时。

## 边界细节

经典论文边界：[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]] 强调“生成模型 + 检索器 + 外部索引”。它不是纯 prompt 技巧，而是把检索作为生成过程的一部分。

和 [[Parametric Memory]] 的边界：参数记忆在模型权重里，更新困难、溯源困难；RAG 的非参数记忆在外部索引里，更新和审计更容易，但检索链路会引入新错误。

和 [[Agent]] 的边界：RAG 本身可以只是问答架构；当系统会根据检索结果规划、调用工具、追问、写回记忆或多轮行动时，才更接近 [[Agentic RAG]] 或 Agent。

和 [[Memory]] 的边界：RAG 更偏“查知识”；memory 更偏“保存和使用过去的信息”。两者可重叠，但不要画等号。

## Obsidian 场景

如果把 Obsidian 笔记接入 LLM，好的笔记切分会很重要：

- 一张概念卡只讲一个概念。
- 标题要清楚。
- 每张卡写出“它不是什么”。
- 关键概念之间用双链连接。
- source note 和 concept card 分开，避免把原文摘录当成稳定理解。

## 现代性状态

- 判定：foundation / current-practice
- 为什么：RAG 的基础边界来自经典论文，今天仍是 LLM 应用的核心工程模式；具体检索架构、embedding、reranker、GraphRAG、agentic retrieval 和评估工具在演进。
- 稳定部分：外部知识索引 + retriever + generator 的基本组合，以及 parametric / non-parametric memory 的边界。
- 易变部分：检索模型、向量数据库、hybrid search、graph retrieval、agentic retrieval、reranking、evaluation pipeline。
- 复查点：当本库重点学习 [[Agentic RAG]]、[[GraphRAG]] 或企业搜索实现时，更新相关卡而不是重写 RAG 基础定义。

## 现代系统怎么吸收 RAG 的价值 / 局限

现代系统通常把 RAG 拆成可评估的流水线：

- ingestion 负责解析、切分、清洗、metadata 和权限。
- retrieval 负责 query rewrite、hybrid search、top-k、filter。
- reranking 负责把候选资料排序。
- generation 负责根据上下文回答并引用来源。
- evaluation 负责检查 retrieval recall、answer faithfulness、citation accuracy 和 latency/cost。
- Agentic RAG 会让 Agent 决定是否检索、检索什么、是否二次检索、是否调用工具或写回记忆。

局限是：RAG 把“知识更新”问题转移成“检索与上下文治理”问题。它减少某些 hallucination，但新增 ingestion、权限、排序、引用、评估和数据治理成本。

## 证据锚点

- Source: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]
- Anchor: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#为什么收]]
- Anchor: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#需要我读的内容]]
- Anchor: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#Ingest 摘要]]
- Anchor: [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#边界提醒]]
- Evidence type: paper source note + local synthesis.
- Confidence: medium
- Boundary: 现代 pipeline 拆分是工程综合，不是经典论文全部内容；经典论文证据主要支持 parametric / non-parametric memory 和 retriever-generator 组合。

## 复习触发

- 为什么 RAG 能更新知识，但仍不能保证回答正确？
- 用自己的话解释 [[Parametric Memory]]、[[Non-Parametric Memory]]、[[Retriever]] 在 RAG 里的关系。
- 什么时候普通 RAG 足够，什么时候才需要 [[Agentic RAG]]？

## 相关链接

- [[LLM]]
- [[Memory]]
- [[Evaluation]]
- [[Retriever]]
- [[Parametric Memory]]
- [[Non-Parametric Memory]]
- [[RAG Evaluation]]
- [[Agentic RAG]]
- [[Document Ingestion]]
