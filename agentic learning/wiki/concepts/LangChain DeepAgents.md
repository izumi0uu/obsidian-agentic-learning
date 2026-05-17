---
type: concept
topic:
  - agent
  - framework
  - workflow
  - frontier
status: seed
created: 2026-05-11
updated: 2026-05-16
up:
  - "[[Agent Framework]]"
last_checked: 2026-05-11
freshness: volatile
conflicts:
  - Deep Agent 不是统一标准名；本卡只讨论 LangChain / LangGraph 生态里的 deepagents / Deep Agents SDK。
source:
  - "[[LangChain Deep Agents 官方文档]]"
  - "[[LangGraph 官方文档]]"
evidence:
  - "[[LangChain Deep Agents 官方文档#一句话]]"
  - "[[LangChain Deep Agents 官方文档#关键事实]]"
  - "[[LangChain Deep Agents 官方文档#边界提醒]]"
  - "[[LangGraph 官方文档#一句话]]"
related:
  - "[[Agent Harness]]"
  - "[[Agent Framework]]"
  - "[[Agent State]]"
  - "[[Durable Execution]]"
  - "[[Planning]]"
  - "[[Long-term Memory]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Tool Permissioning]]"
---

# LangChain DeepAgents

## 一句话

LangChain DeepAgents 是 LangChain 在 LangGraph 之上封装的长任务 Agent harness：LangGraph 管有状态编排和运行时，`deepagents` 提供 planning、filesystem、subagents、memory、permissions 等开箱脚手架。

## 概念详解

普通 tool-calling agent 往往像一个短循环：模型看上下文，决定是否调用工具，工具返回 observation，再继续下一步。这个结构能做简单任务，但遇到长任务时会暴露问题：计划容易丢、上下文会膨胀、中间产物没有稳定存放位置、子任务没有隔离、工具动作缺少权限边界，失败后也很难恢复。LangChain DeepAgents 试图把这些长任务里的常见工程问题预先包进一个 harness。

分层看更清楚：[[Agent Framework]] 层的 LangChain 提供模型、工具、消息和 agent 组件；LangGraph 提供有状态图、checkpoint、durable execution、streaming、human-in-the-loop 等 runtime / orchestration 能力；DeepAgents 则是更靠上的 [[Agent Harness]] 模板，把“长任务 Agent 常用的组合件”装好。它不是替代 LangGraph，而是在 LangGraph 上提供更高层的默认结构。

这张卡里说的 DeepAgents，特指 LangChain / LangGraph 生态的 `deepagents` SDK。官方文档把 Deep Agents SDK 描述为建立在 LangGraph 上的 harness，并强调 planning、subagents、持久上下文和学习/记忆等能力。这里的“deep”不是模型架构更深，而是任务执行更深：能跨多步、多文件、多子任务、多轮校验地推进，而不是只做一两次工具调用。

它的工程吸收方式很典型：把过去可能写在 prompt 里的“先列 todo、把中间结果存好、必要时派子 agent、执行前问权限、失败后继续”的约束，挪到 runtime 和 harness 里。模型仍然负责判断和生成，harness 负责让判断有工作区、有状态、有边界、有 trace。这个边界很重要：模型变强可以让 planning 更好，但不会自动替代 filesystem、checkpoint、permissions、human approval 和 observability。

## 它解决什么问题

DeepAgents 解决的是“长任务 Agent 脚手架重复建设”的问题。

如果每个项目都手写 todo 管理、虚拟文件系统、subagent 调度、memory 注入、权限中断和状态恢复，很容易产生一堆隐含约定：有些放 prompt，有些放临时代码，有些放聊天历史。DeepAgents 把这些常见结构变成可复用 harness，让开发者更快从普通工具调用升级到可运行、可观测、可恢复的长任务 Agent。

它尤其适合用来理解三类任务：

- 研究任务：需要拆问题、存资料、派子任务、合并证据。
- 代码任务：需要读写文件、跑测试、保存 patch 过程。
- 企业流程任务：需要权限、审批、暂停恢复和长期上下文。

## 它不是什么

LangChain DeepAgents 不是一个新基础模型，也不是“用了更深神经网络的 Agent”。

它不是 [[ReAct]] 的同义词。ReAct 更像 reasoning / action / observation 的行动思想；DeepAgents 是把长任务执行需要的状态、文件、子任务、权限和持久化包起来的 harness。

它也不是 MCP、A2A 或 ACP 这类协议。协议回答“系统之间怎么连接或通信”；DeepAgents 回答“一个 LangGraph-based Agent 怎么被组织和运行”。

它也不是 RUC-NLPIR 的 DeepAgent 论文/项目名。后者关注通用推理 Agent 和可扩展工具集，是另一个来源边界；本卡不把它并入 LangChain `deepagents`。

## 最小例子

一个最小心智模型：

```python
from deepagents import create_deep_agent

agent = create_deep_agent(
    tools=[search_web, read_file, write_file],
    instructions="Research the topic, keep notes, and verify claims.",
)

result = agent.invoke({"messages": [{"role": "user", "content": "整理 deep agent 的边界"}]})
```

这里真正值得注意的不是函数名，而是分层：

- tools 仍然是外部动作能力。
- instructions 给模型任务和风格边界。
- `deepagents` 装配长任务 harness。
- LangGraph 在底层承接状态图、执行、streaming、checkpoint 和 human-in-the-loop。

## 常见误解和风险

- 误解：用了 DeepAgents 就自动变成可靠自主 Agent。实际上它只是给出 harness；任务定义、工具权限、评测、数据隔离和人工验收仍要设计。
- 误解：DeepAgents 等于 LangGraph。更准确地说，DeepAgents 建在 LangGraph 上；LangGraph 是更底层的 orchestration / runtime。
- 误解：subagents 越多越好。子 Agent 会带来上下文分裂、成本上升、trace 变长和责任归属不清的问题。
- 风险：filesystem / memory 如果没有权限和数据生命周期设计，容易把临时中间结果误当成可信长期记忆。
- 风险：默认 harness 容易让人低估生产治理：审批、审计、幂等、副作用恢复和安全隔离仍是系统责任。

## 边界细节

和 [[Agent Harness]] 的关系：DeepAgents 是一个具体 harness。[[Agent Harness]] 是通用概念，指包住模型、工具、状态、权限、运行环境、trace 和评测逻辑的执行外壳。

和 [[Agent Framework]] 的关系：LangChain / LangGraph 是框架和 runtime 生态；DeepAgents 是在这个生态上的长任务默认封装。用 DeepAgents 不代表不用 LangGraph，而是少写一部分重复图编排和长任务脚手架。

和 [[Durable Execution]] 的关系：DeepAgents 借助 LangGraph 生态吸收 durable execution 的价值，但它本身不是 durable execution 的一般定义。恢复、checkpoint、interrupt 和 resume 的具体行为要回到当前 LangGraph / DeepAgents 文档核对。

和 [[Multi-agent Orchestration]] 的关系：DeepAgents 提供 subagents，但 subagents 只是多 Agent 编排的一种局部机制。真正可靠的多 Agent 编排还需要 ownership、通信、集成权威和验证标准。

和通用 “deep agent” 的关系：通用说法强调能做长程复杂任务的 Agent 形态；LangChain DeepAgents 是这种趋势的一个具体 SDK / harness 实现。

## 现代性状态

- 判定：frontier / volatile 的具体 SDK；其背后的模式属于 current-practice。
- 稳定部分：长任务 Agent 需要 planning、state、filesystem / workspace、tool permissions、trace、memory 和 verification，这已经是当前工程实践。
- 易变部分：`deepagents` 包的 API、默认工具、memory 设计、subagent 语义、LangGraph 集成方式和生产推荐写法都可能快速变化。
- 复查策略：优先更新 [[LangChain Deep Agents 官方文档]] 的 `last_checked` 和本卡的 API 边界；不要因为某次 SDK 更新就改写 [[Agent Harness]] 或 [[Agent Framework]] 的通用定义。

## 现代系统怎么吸收 DeepAgents 的价值

现代 Agent 系统越来越少把“复杂任务怎么持续推进”完全交给 prompt。它们会把任务状态、文件、权限、恢复、人工确认和 trace 放进 harness / runtime，让模型只在明确边界内做判断。

DeepAgents 的价值在于把这套长任务结构做成默认模板：模型可以计划，harness 保存计划；模型可以调用工具，runtime 执行并记录；模型可以派子任务，系统保留结果和边界；用户可以中断或审批，执行状态不会只消失在聊天上下文里。

这也解释了它的局限：它让复杂 Agent 更容易搭出来，但不会替你证明任务成功。真正上线仍要补 [[Evaluation]]、[[Trace]]、[[Tool Permissioning]]、数据隔离、成本控制和人类验收。

## 证据锚点

- Source: [[LangChain Deep Agents 官方文档]]
- Source: [[LangGraph 官方文档]]
- Anchor: [[LangChain Deep Agents 官方文档#一句话]], [[LangChain Deep Agents 官方文档#关键事实]], [[LangChain Deep Agents 官方文档#边界提醒]], [[LangGraph 官方文档#一句话]]
- Evidence type: official docs source note + framework/runtime source note + engineering synthesis.
- Confidence: medium-high
- Boundary: “DeepAgents 是 LangGraph 上的 harness”由官方文档支撑；“它体现长任务 Agent harness 工程化趋势”是本 vault 的综合理解。具体 API 与默认能力必须按当前版本复查。

## 复习触发

- 为什么说 DeepAgents 不是独立 orchestration runtime，而是建在 LangGraph 上的 harness？
- 如果一个项目已经手写 LangGraph graph，什么时候还值得用 DeepAgents？
- DeepAgents 的 filesystem / memory / subagents 分别解决什么问题，又分别会带来什么风险？

## 相关链接

- [[Agent Harness]]
- [[Agent Framework]]
- [[Agent State]]
- [[Durable Execution]]
- [[Planning]]
- [[Long-term Memory]]
- [[Multi-agent Orchestration]]
- [[Tool Permissioning]]
- [[LangChain Deep Agents 官方文档]]
- [[LangGraph 官方文档]]
