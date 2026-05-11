---
type: concept
topic:
  - rag
  - memory
status: growing
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]"
evidence:
  - "[[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks#为什么收]]"
related:
  - "[[RAG]]"
  - "[[Parametric Memory]]"
  - "[[Retriever]]"
  - "[[Memory]]"
---

# Non-Parametric Memory

## 一句话

Non-Parametric Memory 是模型参数外部的可检索知识存储，例如文档索引、向量库、知识库或数据库。

## 概念详解

Non-Parametric Memory 这个说法来自 RAG 论文语境：知识不只存在模型参数里，还可以存在一个外部、可检索、可更新的存储中。模型回答问题时，先由 [[Retriever]] 从外部存储取回相关 passages，再把这些内容交给生成模型使用。

它的重点是“非参数化”：知识不需要通过重新训练模型参数才能更新。相比 [[Parametric Memory]]，外部 memory 可以替换文档、删除过期内容、审查来源、记录引用，也能把模型没有见过的新资料加入系统。

在现代工程里，non-parametric memory 经常表现为向量数据库、搜索索引、文档库、知识图谱或业务数据库。但它不是 Agent memory 的全部：它更偏“外部知识材料”，不自动包含用户偏好、任务状态、历史经历、权限策略或记忆反思。

因此读 RAG 论文时要注意术语边界：论文里的 memory 主要是模型知识来源的对比；Agent 系统里的 [[Memory]] 还会讨论长期偏好、episodic memory、semantic memory、写入策略和隐私治理。

从学习角度看，它最适合用来解释“为什么外部知识库能补模型”。模型参数负责泛化语言和常识，non-parametric memory 负责把具体、可更新、可引用的材料带入当前上下文。它不保证答案正确，但给了系统一个可以检查和替换的知识来源。

它还有一个治理优势：外部知识可以按租户、权限、更新时间和来源分层。生产系统可以只检索用户有权看的文档，也可以在资料过期时重建索引。这些都不是模型参数能自然提供的能力。 这正是它在 Agent 系统中仍然重要的原因。

## 它解决什么问题

外部知识可以被更新、替换、审查和引用。RAG 使用它来补足模型参数知识难更新、难溯源的问题。

它还让系统把“答案依据”从模型内部隐含知识移到可检查的文档或数据库片段上，便于 freshness、权限和引用管理。

## 它不是什么

Non-Parametric Memory 不是 Agent 的全部记忆。它更偏知识存储，不自动包含用户偏好、任务状态、历史轨迹或安全策略。

它也不是一定等于向量库。向量库是常见实现之一；关键词索引、混合搜索、知识图谱和 SQL 数据库也可以承担外部可检索记忆的角色。

## 最小例子

把 Wikipedia 文档放进 dense vector index，再根据问题检索相关 passage，这就是 RAG 论文里的非参数记忆例子。

如果公司把内部政策文档放入搜索索引，让客服 Agent 回答时先检索政策段落，这也是 non-parametric memory 的工程形式。

## 常见误解和风险

- 误解：non-parametric memory 一定比模型参数知识正确。实际仍取决于资料质量、切分、检索和更新。
- 误解：有向量库就有完整 Agent memory。向量库只解决外部知识检索的一部分。
- 风险：外部存储过期、权限错误或检索无关内容，会把错误证据注入回答。

## 边界细节

它和 [[Memory]] 的关系是：Non-Parametric Memory 是记忆的一种实现材料，但 Agent memory 还需要写入、更新、冲突处理、过期和权限。

和 [[RAG]] 的边界：RAG 是“检索 + 生成”的方法；non-parametric memory 是被检索的外部知识来源。没有生成步骤，外部存储仍然是 memory；没有外部存储，RAG 就失去核心动机。

和 [[Parametric Memory]] 的边界：parametric memory 隐含在模型权重里，更新成本高、来源难追；non-parametric memory 在模型外部，更新和审计更直接，但需要检索质量和权限治理。

## 现代性状态

Non-Parametric Memory 是基础地基 + 当前工程实践。

RAG 论文中的术语是基础概念；现代系统把它落到 vector database、hybrid search、knowledge graph、document store 和 enterprise search 中。具体检索算法、embedding model、reranker 和数据库产品会变化，但“外部可检索知识补足模型参数知识”的边界稳定。

## 现代系统怎么吸收 Non-Parametric Memory 的价值

现代 RAG / Agent 系统通常不会只依赖模型参数回答知识密集问题，而是把外部资料做 ingestion、chunking、embedding、metadata、hybrid search 和 reranking，再把少量证据注入上下文。

这样做把知识更新、来源审查和权限控制从模型训练转移到数据和检索管线。

## 证据锚点

- Evidence type: paper source — [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]。
- Boundary: 当前卡只使用 RAG 论文里的 parametric / non-parametric memory 对比作为概念来源；现代向量数据库、混合搜索和 graph 实现是工程吸收，不等同于论文原始系统全部细节。
- Engineering synthesis: “外部知识存储需要权限、freshness、检索质量治理”是现代 RAG 工程总结。
- Confidence: medium。

## 复习触发

- Non-Parametric Memory 和向量数据库是什么关系？
- 为什么 RAG 论文要把外部知识称为 non-parametric memory？
- 它和 Agent 的 Long-term Memory 最大边界是什么？

## 相关链接

- [[RAG]]
- [[Retriever]]
- [[Parametric Memory]]
- [[Memory]]
