---
type: concept
topic:
  - agent
  - framework
  - rag
  - data
status: growing
created: 2026-05-12
updated: 2026-05-16
up:
  - "[[Agent Framework]]"
last_checked: 2026-05-12
freshness: watch
source:
  - "[[LlamaIndex Agents 官方文档]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
evidence:
  - "[[LlamaIndex Agents 官方文档#必读块 1：agent loop 与 tool 选择]]"
  - "[[LlamaIndex Agents 官方文档#必读块 2：pre-built workflows 与多 Agent patterns]]"
  - "[[Agent Framework 全量选型对比 2026-05#LlamaIndex vs LangGraph]]"
related:
  - "[[RAG]]"
  - "[[Agentic RAG]]"
  - "[[Retriever]]"
  - "[[Agent Workflow]]"
---

# Data-first Agent Framework

## 一句话

Data-first Agent Framework 是从数据连接、索引、检索、query engine 和 RAG 生态进入 Agent 的框架路线，适合知识密集型任务，但不等于所有 Agent 控制流都应该由 RAG 框架主导。

## 概念详解

许多 Agent 失败不是因为缺少“自主性”，而是缺少可靠上下文：文档在哪里、如何切分、怎样检索、哪个 query engine 更适合、工具返回的知识如何进入回答。Data-first Agent Framework 的第一抽象不是 multi-agent team 或 state graph，而是把数据、索引、检索和查询能力变成 Agent 可以调用的工具或 workflow。

[[LlamaIndex Agents 官方文档]] 的 source note 明确说明 LlamaIndex Agents 以数据/RAG 生态为底盘：agent 可以选择函数、query engine 等工具，多 Agent 可通过 AgentWorkflow 等 pattern 组织，尤其适合知识密集型应用。这和 [[State Graph Runtime]] 的边界不同：LangGraph 更强调任意控制流和恢复，LlamaIndex 更强调 data/RAG/query engine 与 Agent 的衔接。

工程综合：Data-first Agent Framework 的核心问题是“模型应该基于哪些外部知识行动”，而不是“有几个 Agent 协作”。

这种框架的强项是把“数据接入和查询”做成 Agent 能稳定使用的能力：文档解析、索引、retriever、query engine、tool wrapper 和 response synthesis 形成一条数据优先路径。它适合知识密集任务、企业文档问答和 agentic RAG；但如果任务核心是复杂状态机、长事务恢复或多人审批，单靠 data-first 抽象会不够，需要与 state graph、control plane 或 eval harness 组合。
## 它解决什么问题

- Agent 回答依赖大量外部文档或企业知识库。
- 手写 RAG pipeline 与 tool loop 分离，导致检索结果难以被 Agent 正确使用。
- query engine、retriever、index 和 agent workflow 缺少统一接口。

## 它不是什么

- 不是普通向量数据库。它可能使用 vector database，但还包括 query engine、tool wrapper、workflow 和 evaluation。
- 不是所有 Agent 的最佳底层 runtime。非知识密集、强流程控制任务可能更适合 state graph/workflow framework。
- 不是事实正确保证。检索召回错误、文档过期和引用污染仍需要评估。

## 最小例子

```text
Build index over policy docs
-> expose query_engine as agent tool
-> agent receives customer question
-> agent calls query_engine
-> answer cites retrieved policy sections
```

## 常见误解 / 风险

- 误解：有 RAG 就是 Agent。RAG 只解决上下文来源，不自动处理行动、权限和长期状态。
- 误解：data-first 框架可以替代 workflow。复杂审批和副作用仍要显式流程。
- 风险：把 query engine 作为万能工具，导致 Agent 过度检索或引用不相关内容。

## 边界细节

Data-first Agent Framework 与 [[Agentic RAG]] 相邻：Agentic RAG 描述 RAG pipeline 中由 Agent 做查询规划/纠错/工具选择的形态；Data-first Agent Framework 是实现这类能力的软件框架路线。它与 [[State Graph Runtime]] 可以组合：数据检索作为 graph 节点或 tool，状态图负责恢复和审批。

## 现代性状态

- 判定：current-practice。
- 稳定部分：把 query engine / retriever / index 作为 Agent tool 或 workflow 节点，是知识密集型 Agent 常见做法。
- 易变部分：LlamaIndex 具体 AgentWorkflow API、LlamaCloud 能力和多 Agent pattern。

## 现代系统怎么吸收 Data-first Agent Framework 的价值 / 局限

现代系统会把 data-first 框架放在知识层：负责 ingestion、index、retrieval、query tools 和 RAG evaluation；再用 workflow/harness 管理权限、审批、状态和 trace。局限是数据层再强，也不能自动解决行动安全和业务流程。

## 证据锚点

- [[LlamaIndex Agents 官方文档#必读块 1：agent loop 与 tool 选择]]：agent 可调用函数和 query engine 等工具。
- [[LlamaIndex Agents 官方文档#必读块 2：pre-built workflows 与多 Agent patterns]]：AgentWorkflow / FunctionAgent / 多 Agent pattern。
- [[Agent Framework 全量选型对比 2026-05#LlamaIndex vs LangGraph]]：data/RAG-first 与 state graph 的边界。

- Evidence type: official LlamaIndex docs + framework comparison map + engineering synthesis.
- Boundary: Data-first Agent Framework 强调数据/RAG 入口，不等于所有 Agent Framework，也不自动解决 workflow runtime、权限治理或长期状态。
## 复习触发

1. 为什么 data-first agent framework 不等于 vector database？
2. LlamaIndex 和 LangGraph 都能接工具，为什么一个更偏 data/RAG，一个更偏 state graph？
3. 什么时候应该先固定成普通 RAG workflow，而不是让 Agent 自由选择检索？

## 相关链接

- [[RAG]]
- [[Agentic RAG]]
- [[Retriever]]
- [[Agent Workflow]]
- [[Agent Framework 全量选型对比 2026-05]]
