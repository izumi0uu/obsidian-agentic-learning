---
type: concept
topic:
  - rag
  - agent
  - workflow
  - frontier
status: review
created: 2026-05-06
updated: 2026-05-16
last_checked: 2026-05-16
freshness: watch
conflicts:
  - "RAGGraph 不是稳定统一术语，可能被误当作 GraphRAG。"
source:
  - "[[前沿主源清单]]"
  - "[[RAG 类型对比]]"
evidence:
  - "[[前沿主源清单#RAG 进化]]"
  - "[[RAG 类型对比#最容易混淆的边界]]"
relations:
  - type: related_to
    target: "[[RAG]]"
    note: "RAGGraph 讨论的是 RAG pipeline 可能被图式编排，但这个命名不稳定；当前不把它写成 RAG 的 strict taxonomy 子类。"
  - type: contrasts_with
    target: "[[GraphRAG]]"
    note: "GraphRAG 是图结构参与检索和上下文构造；RAGGraph 更可能指 RAG 执行流程图或项目名，二者不能互当别名。"
  - type: related_to
    target: "[[Agentic RAG]]"
    note: "若 RAGGraph 指带分支和循环的检索工作流，它更接近 Agentic RAG / workflow graph 的实现语境，而不是独立稳定方法族。"
related:
  - "[[RAG]]"
  - "[[GraphRAG]]"
  - "[[Agentic RAG]]"
  - "[[Agent Loop]]"
---

# RAGGraph

## 一句话

RAGGraph 是一个不稳定说法，通常可能指“把 RAG pipeline 编排成图工作流”，也可能指“用图结构组织知识并做检索”。

## 概念详解

RAGGraph 在本库里应该被当成待复查术语，而不是稳定概念。它的问题是命名容易和 [[GraphRAG]] 混淆：GraphRAG 通常指知识图谱、实体关系或图结构参与检索；RAGGraph 更可能指把 RAG 流程本身做成图工作流，例如 query rewrite、retrieve、grade、rerank、answer、fallback 这些节点组成一个有分支和循环的执行图。

普通 RAG 常被画成一条线：query -> retrieve -> answer。但真实系统往往需要条件分支：检索结果不好就改写 query；证据不足就重检索或拒答；引用不支持就回到证据检查；用户权限不足就过滤或请求确认。这类“RAG pipeline as graph”可以用 LangGraph、workflow engine 或自定义状态机实现。它强调的是执行流程图，而不是知识库本身是图数据库。

边界是这张卡的核心价值。看到 RAGGraph 这个词，要先问它来自哪里：是某个 GitHub 项目名、某篇博客的图工作流叫法，还是把 GraphRAG 写反了？如果它指知识图谱检索，应该并入 [[GraphRAG]]；如果它指 RAG workflow 编排，则应和 [[Agentic RAG]]、[[Corrective RAG]]、[[Agent Loop]] 放在一起理解；如果只是项目命名，就不应把它提升成稳定方法。

现代性上，RAGGraph 是 frontier / volatile-ish 的术语，而不是成熟类别。图工作流本身是 current-practice，但“RAGGraph”这个词的语义不稳定。它适合作为混淆提醒卡，帮助学习时不要把 workflow graph、knowledge graph 和 graph database 混为一谈。

## 它解决什么问题

普通 RAG 常被画成一条线：

```text
query -> retrieve -> answer
```

但真实 RAG 往往有分支、循环和质量检查：

```text
query -> rewrite -> retrieve -> grade -> rerank -> answer
                         ^                    |
                         |------ retry -------|
```

RAGGraph 这类说法想表达：RAG 不一定是一条直线，它也可以是一个由节点、边、条件和循环组成的工作流。

## 它不是什么

RAGGraph 不是一个稳定统一的学术概念。

它也不等于 [[GraphRAG]]。[[GraphRAG]] 更常指用实体、关系、社区或知识图谱增强检索；RAGGraph 更可能指 RAG 流程本身被编排成图。

它也不是只要用了 LangGraph、流程图或 DAG 就自动更高级。关键仍然是检索结果是否更可靠、上下文是否更干净、答案是否可验证。

## 最小例子

```text
用户问题
  -> query rewrite
  -> retrieve
  -> evidence grading
  -> enough? yes -> answer
  -> enough? no  -> web search / reretrieve / ask human
```

这个图描述的是 RAG 的“执行流程”，不一定说明知识库本身是图数据库。

## 常见误解 / 风险

- 误解：RAGGraph 和 [[GraphRAG]] 是同义词。
- 误解：把流程画成图，效果就会变好。
- 风险：节点太多会让系统难调试，trace 和 eval 跟不上。
- 风险：每一步都让 LLM 判断，成本和不确定性都会上升。
- 风险：概念名来自不同 GitHub 项目时，含义可能完全不同。

## 边界细节

看到 RAGGraph 这个词时，先问三个问题：它说的是 RAG 流程图，还是知识图谱检索？它是通用概念，还是某个项目的命名？它带来的收益是更好召回、更好验证，还是只是更复杂？

和 [[GraphRAG]] 的边界：GraphRAG 是图结构参与知识检索；RAGGraph 更可能是 RAG 执行流程被图编排。

和 [[Agentic RAG]] 的边界：Agentic RAG 强调 Agent 决定检索行为；RAGGraph 强调这些行为可能被实现成图节点和边。

本轮关系写回结论：RAGGraph 只保留 `related` / `relations`，不写 `up: [[RAG]]`。如果以后遇到具体项目或论文把 RAGGraph 稳定定义为某个 RAG 方法族，再重新进入候选台账；在当前证据下，它是混淆提醒卡，不是 taxonomy child。

## 现代性状态

- 判定：frontier / volatile terminology。
- 稳定部分：RAG workflow 可以被实现成图、状态机或有条件循环。
- 易变部分：RAGGraph 这个词的含义、项目指向和社区用法不稳定。
- freshness: watch。
- last_checked: 2026-05-16。
- 复查点：遇到具体 RAGGraph 项目时，先确认它是 workflow graph、GraphRAG 变体，还是项目名。

## 现代系统怎么吸收 RAGGraph 的价值

现代系统吸收的是“把 RAG 流程显式成可观察图”的价值：每个节点有输入输出、错误处理、重试和评估。不要吸收不稳定术语本身；应该把具体模式落到 [[Agentic RAG]]、[[Corrective RAG]]、[[GraphRAG]] 或 workflow graph 的边界里。

## 证据锚点

- Source: [[前沿主源清单]]
- Anchor: [[前沿主源清单#RAG 进化]]
- Source: [[RAG 类型对比]]
- Anchor: [[RAG 类型对比#最容易混淆的边界]]
- Evidence type: frontier source map + local comparison map + engineering synthesis.
- Confidence: medium
- Boundary: sources support that RAGGraph/GraphRAG is a confusion boundary; the workflow-graph explanation is a cautious synthesis, not a claim that RAGGraph is a stable academic term.

## 复习触发

- RAGGraph 和 GraphRAG 最容易混淆在哪里？
- 一个 RAG workflow 图增加节点后，必须补哪些 trace/eval？
- 遇到新项目名时，为什么不能直接把它升格成稳定概念？

## 相关链接

- [[RAG]]
- [[GraphRAG]]
- [[Agentic RAG]]
- [[RAG 类型对比]]
- [[Agent Loop]]
