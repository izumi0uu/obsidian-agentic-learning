---
type: concept
topic:
  - agent
  - protocol
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[Agent2Agent Protocol]]"
evidence:
  - "[[Agent2Agent Protocol#为什么收]]"
related:
  - "[[MCP]]"
  - "[[ACP]]"
  - "[[Agent]]"
  - "[[Tool Registry]]"
---

# A2A

## 一句话

A2A 是面向 Agent 与 Agent 之间通信和互操作的开放协议。

## 概念详解

A2A 的问题背景是：当两个 Agent 不在同一个框架、同一个运行时或同一个公司系统里时，不能只靠“我在 prompt 里说你是另一个 Agent”来协作。它需要一种可被发现、可描述能力、可传递任务状态和消息的互操作层。source note 把 A2A 的核心对象指向 Agent Card、task、message、streaming 等，这说明它关注的是“一个 Agent 如何把另一个 Agent 当成协作者”，而不是把远端能力压扁成一个普通函数。

机制上，A2A 更像跨系统协作协议：一方先了解对方能做什么，再把任务、上下文、消息和状态交给对方处理。工程上仍然需要本地 orchestrator 决定什么时候委派、怎样处理失败、如何限制权限、怎样记录 trace，以及如何评价协作结果。A2A 解决互操作入口，不解决 Agent 是否可靠、是否安全、是否完成任务。

和 [[MCP]] 的关键区别是对象不同：MCP 主要连接工具、资源和上下文服务；A2A 连接的是具有任务处理能力的 Agent。和多 Agent 框架的区别是层级不同：框架负责本地编排和状态机，A2A 负责跨边界通信。学习这张卡时要抓住“Agent 对 Agent”的边界，而不是记某个版本里的字段名。

一个实用判断是看委派对象是否需要保持自己的任务状态。如果远端只返回一次函数结果，普通 API/MCP 工具就够；如果远端会分解任务、持续运行、流式回报、请求澄清或交付 artifact，它就更接近 A2A 想描述的 Agent。这个边界也解释了为什么 A2A 不能单独保证协作质量：协议能让双方说同一种任务语言，但不能保证对方的计划能力、证据质量或安全策略。


## 它解决什么问题

如果每个 Agent 都只暴露私有 API，多 Agent 协作会很难标准化。A2A 尝试让不同系统中的 Agent 能发现彼此能力、发送任务、交换消息、跟踪长任务状态。

## 它不是什么

A2A 不是多 Agent 框架。

它也不是 [[MCP]] 的替代品。粗略理解：MCP 偏 Agent 连接工具和数据源；A2A 偏 Agent 与另一个 Agent 交互。

## 最小例子

一个研究 Agent 需要图表：

- 它通过 A2A 找到一个可做数据可视化的 Agent。
- 发送任务和上下文。
- 对方返回中间状态、结果和可能的追问。

## 常见误解 / 风险 / 边界细节

- Agent 之间通信越自由，权限和身份越重要。
- 不可信 Agent 可能返回恶意指令或污染上下文。
- 多 Agent 协作可能增加延迟和失败面。
- 协议解决互操作，不自动解决任务分工质量。

## 边界细节

A2A 连接的是远端 Agent 能力，不是本地工具 schema。它需要身份、权限、任务状态和失败恢复，但这些通常由 host/orchestrator 负责。边界判断：如果对方只是一个函数或数据源，更像 MCP/API；如果对方有自己的任务处理和状态语义，才更像 A2A。

## 现代性状态

frontier / volatile。A2A 代表 Agent 互操作的前沿协议层，问题稳定但具体协议对象、生态治理和实现细节仍在变化。学习时优先记“Agent-to-Agent 互操作边界”，不要把当前字段当作长期不变。

## 证据锚点

- Evidence type: source evidence — [[Agent2Agent Protocol#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[Agent2Agent Protocol]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- 什么时候一个远端能力应被建模为 Agent，而不是普通工具？
- A2A 和 MCP 的对象边界分别是什么？

## 相关链接

- [[MCP]]
- [[ACP]]
- [[Agent]]
- [[Policy Engine]]
