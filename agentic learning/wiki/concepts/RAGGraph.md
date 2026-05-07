---
type: concept
topic:
  - rag
  - agent
  - workflow
  - frontier
status: review
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[前沿主源清单]]"
  - "[[RAG 类型对比]]"
evidence:
  - "[[前沿主源清单#RAG 进化]]"
  - "[[RAG 类型对比#一张表先抓住]]"
related:
  - "[[RAG]]"
  - "[[GraphRAG]]"
  - "[[Agentic RAG]]"
  - "[[Agent Loop]]"
---

# RAGGraph

## 一句话

RAGGraph 是一个不稳定说法，通常可能指“把 RAG pipeline 编排成图工作流”，也可能指“用图结构组织知识并做检索”。

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

一个 RAGGraph 工作流可能是：

```text
用户问题
  -> query rewrite
  -> retrieve
  -> evidence grading
  -> enough? yes -> answer
  -> enough? no  -> web search / reretrieve / ask human
```

这个图描述的是 RAG 的“执行流程”，不一定说明知识库本身是图数据库。

## 常见误解和风险

- 误解：RAGGraph 和 [[GraphRAG]] 是同义词。
- 误解：把流程画成图，效果就会变好。
- 风险：节点太多会让系统难调试，trace 和 eval 跟不上。
- 风险：每一步都让 LLM 判断，成本和不确定性都会上升。
- 风险：概念名来自不同 GitHub 项目时，含义可能完全不同。

## 学习边界

看到 RAGGraph 这个词时，先问三个问题：

1. 它说的是 RAG 流程图，还是知识图谱检索？
2. 它是通用概念，还是某个项目的命名？
3. 它带来的收益是更好召回、更好验证，还是只是更复杂？

## 证据锚点

- Source: [[前沿主源清单]]
- Source: [[RAG 类型对比]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[RAG]]
- [[GraphRAG]]
- [[Agentic RAG]]
- [[RAG 类型对比]]
- [[Agent Loop]]
