---
type: concept
topic:
  - agent
  - protocol
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
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

## 证据锚点

- Source: [[Agent2Agent Protocol]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[MCP]]
- [[ACP]]
- [[Agent]]
- [[Policy Engine]]
