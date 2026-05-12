---
type: concept
topic:
  - agent
  - framework
  - workflow
  - infrastructure
status: growing
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
conflicts: []
source:
  - "[[LangGraph 官方文档]]"
  - "[[LangChain Deep Agents 官方文档]]"
evidence:
  - "[[LangGraph 官方文档#一句话]]"
  - "[[LangGraph 官方文档#边界提醒]]"
  - "[[LangChain Deep Agents 官方文档#需要我读的内容]]"
related:
  - "[[Agent Framework]]"
  - "[[Agent Workflow]]"
  - "[[Agent State]]"
  - "[[Durable Execution]]"
  - "[[LangChain DeepAgents]]"
  - "[[Agent Framework 编排范式对比]]"
---

# LangGraph

## 一句话

LangGraph 是 LangChain 生态里的低层 Agent orchestration runtime：它用状态图建模长任务 Agent，把节点、边、状态、循环、checkpoint、human-in-the-loop 和 durable execution 做成显式工程对象。

## 概念详解

LangGraph 的核心思想不是“再包一层聊天 agent”，而是把 Agent 执行流程写成 graph。每个节点可以是 LLM 调用、工具执行、人工审批、router、evaluator 或普通函数；边决定下一步走向；state 保存跨节点共享的运行事实。这样，循环、分支、重试、等待人工确认、从 checkpoint 恢复这些原本散落在 prompt 和脚本里的控制逻辑，都可以进入显式 runtime。

这使它和 AutoGen / CAMEL 的学习入口不同。AutoGen 先让我们看多个 agent 的消息协作；CAMEL 先让我们看角色设定和 inception prompting；LangGraph 先让我们看任务路径和状态更新。对于生产系统来说，LangGraph 的价值在于把“模型下一步怎么走”从自然语言提示中抽出来，变成节点、边和 state schema，让开发者能审计、恢复、测试和限制执行路径。

现有 source note 还提示一个重要分层：LangGraph 是 runtime / orchestration 层，LangChain DeepAgents 是建在 LangGraph 上的 harness。也就是说，DeepAgents 可以把 planning、filesystem、subagents、memory、permissions 等长任务脚手架封装好；LangGraph 则提供更底层的状态图、持久化、streaming、human-in-the-loop 和 durable execution。学习时不要把 LangGraph、LangChain agents、LangSmith、DeepAgents 都混成一个“LangChain 框架”。

## 它解决什么问题

LangGraph 解决的是复杂 Agent workflow 的显式控制问题：长任务需要分支、循环、状态、暂停恢复、人工确认和多节点协作时，线性 chain 或自由 agent loop 很快会变得不可控。

它尤其适合理解：Plan-and-execute、Reflection loop、多 Agent handoff、RAG query planning、human approval、checkpoint recovery、失败后从某个节点恢复等工程模式。

## 它不是什么

LangGraph 不是模型，也不是简单 prompt 模板。它也不是 DeepAgents harness；DeepAgents 是更高层的长任务 Agent 脚手架，LangGraph 是底层 runtime / state graph。

LangGraph 也不等于“所有任务都要画图”。如果任务是单次确定性调用，普通函数、chain 或固定 workflow 可能更简单。

## 最小例子

```text
State: {question, draft, tool_results, approval_status}
Node: planner -> retriever -> writer -> reviewer
Edges: if reviewer says pass -> end; if fail -> writer; if risky -> human approval
Checkpoint: save state after every node
```

最小例子的重点是 state + node + edge，而不是 agent 角色名称。

## 常见误解 / 风险

- 误解：LangGraph 是“更复杂的 LangChain chain”。风险是只把它当流程图工具，忽略 state 和 checkpoint。
- 误解：用了 graph 就可靠。风险是节点判断、状态合并、工具副作用和终止条件仍然可能错。
- 风险：把 DeepAgents / LangGraph / LangSmith / LangChain agents 混成同一层。
- 风险：图过度复杂后，调试难度从 prompt 转移到 state schema 和边条件。

## 边界细节

和 [[AutoGen]]：AutoGen 更偏 team/group chat；LangGraph 更偏 state graph。AutoGen 的核心问题是“谁说话、怎么接力、何时终止”；LangGraph 的核心问题是“哪个节点执行、state 如何更新、下一条边怎么走”。

和 [[AgentScope]]：AgentScope 更像多 Agent 应用平台；LangGraph 更像低层 workflow runtime。二者都可做编排，但平台边界不同。

和 [[Microsoft Agent Framework]]：两者都重视 workflow；LangGraph 更偏 LangChain 生态的 Python/JS state graph runtime，Microsoft Agent Framework 更偏微软统一 agent + workflow SDK 与企业集成路线。

## 现代性状态

- 判定：current-practice / frontier-adjacent，`freshness: volatile`。
- 稳定部分：state graph、node/edge/state、cycles、checkpoint、human-in-the-loop、durable execution 是现代 Agent workflow 的关键工程边界。
- 易变部分：LangGraph API、LangChain 产品分层、DeepAgents harness、deployment 和 observability 集成。

## 现代系统怎么吸收 LangGraph 的价值 / 局限

现代系统吸收 LangGraph 的价值，主要是把开放式 Agent loop 放进可控图结构：固定路径由边管理，动态判断由节点里的模型或函数处理，长期任务由 checkpoint 和 state 支撑，人工确认成为显式节点。

局限是 graph 只能表达控制结构，不自动给你正确的任务分解、可靠 evaluator、幂等副作用或安全策略。LangGraph 需要和 [[Tool Permissioning]]、[[Trace]]、[[Evaluation]]、[[Guardrails]] 一起使用。

## 证据锚点

- Source: [[LangGraph 官方文档]]
- Anchor: [[LangGraph 官方文档#一句话]], [[LangGraph 官方文档#边界提醒]]
- Source: [[LangChain Deep Agents 官方文档]]
- Anchor: [[LangChain Deep Agents 官方文档#需要我读的内容]]
- Evidence type: official docs source notes + engineering synthesis.
- Confidence: medium-high for state graph / runtime boundary; medium for product-layer positioning because LangChain ecosystem changes quickly.
- Boundary: 本卡不声明最新 API 细节，只沉淀 LangGraph 作为 state graph orchestration runtime 的学习边界。

## 复习触发

1. 为什么 LangGraph 的核心不是“多 Agent 聊天”，而是 state graph？
2. DeepAgents 和 LangGraph 的层级区别是什么？
3. 一个 workflow 什么时候应该从 chain 升级成 graph？
4. LangGraph 能防循环吗？如果不能完全防，哪些边界仍需 harness / evaluation？

## 相关链接

- [[Agent Framework]]
- [[Agent Framework 编排范式对比]]
- [[LangChain DeepAgents]]
- [[AutoGen]]
- [[AgentScope]]
- [[CAMEL]]
- [[Microsoft Agent Framework]]
- [[Agent Workflow]]
- [[Agent State]]
- [[Durable Execution]]
