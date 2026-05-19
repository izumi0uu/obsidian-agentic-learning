---
type: source
source_type: docs
title: "Agent Network Protocol"
url: https://www.agent-network-protocol.com/
github: https://github.com/agent-network-protocol/AgentNetworkProtocol
site: Agent Network Protocol
topic:
  - agent
  - protocol
  - frontier
created: 2026-05-18
updated: 2026-05-18
last_checked: 2026-05-18
freshness: watch
conflicts: []
status: seed
source:
  - https://www.agent-network-protocol.com/
  - https://github.com/agent-network-protocol/AgentNetworkProtocol
related:
  - "[[ANP]]"
  - "[[A2A]]"
  - "[[MCP]]"
  - "[[A2A MCP ANP 对比]]"
---

# Agent Network Protocol

## 为什么收

ANP 是 Agent 互联协议方向的一个前沿主源。它把 Agent 放进更开放的网络语境里讨论：Agent 需要身份、描述、发现、安全通信，以及在异构协议之间协商怎么交互。

学习价值在于补齐 [[A2A]] 和 [[MCP]] 之间没有覆盖的一层：A2A 更像 Agent-to-Agent 任务协作协议，MCP 更像 AI 应用连接工具/资源/context server 的协议；ANP 关心的是 Agent 在网络中怎样被标识、被发现、被描述，并通过元协议协商通信方式。

## 一句话

Agent Network Protocol 是一个面向 Agent 网络互联的开放协议方向，核心关注 Agent identity、discovery、description、安全通信和 meta-protocol negotiation。

## 主源事实

- 项目官网把 ANP 定位为面向 Agent 互联的协议集合，包含 Agent 描述、发现、通信等规范入口。
- GitHub / white paper 把 ANP 的技术路线和 W3C DID、去中心化身份、加密通信、Agent Description Document、meta-protocol 等对象放在一起讨论。
- Technical white paper 把 ANP 拆成三层：identity and secure communication layer、meta-protocol layer、application protocol layer。
- Agent Communication Meta-Protocol 规范的学习价值在于：它不是只定义一个固定 message schema，而是让 Agent 在通信前描述和协商可用协议、交互流程和能力边界。
- Agent Description Protocol 规范的学习价值在于：远端 Agent 要被发现和调用，必须先有可读、可验证、可解析的能力描述。

## 主源链接

- 官网：<https://www.agent-network-protocol.com/>
- GitHub：<https://github.com/agent-network-protocol/AgentNetworkProtocol>
- Technical white paper：<https://github.com/agent-network-protocol/AgentNetworkProtocol/blob/main/01-agentnetworkprotocol-technical-white-paper.md>

## 可以拆成概念卡

- [[ANP]]
- agent identity / DID for agents
- agent discovery
- agent description
- communication meta-protocol

## 边界提醒

ANP 不是 [[MCP]] 的替代品。MCP 的主对象是 tools、resources、prompts 和 server/client/host 连接；ANP 的主对象是网络中的 Agent 身份、发现、描述和通信协商。

ANP 也不是 [[A2A]] 的同义词。A2A 更聚焦 Agent-to-Agent 协作中的 Agent Card、task、message、artifact 和状态流转；ANP 更偏 Agentic Web / network protocol 方向，把 DID identity、encrypted communication 和 protocol negotiation 放在核心位置。

## 需要我读的内容

1. White Paper：先确认 ANP 为什么把 Agent 网络化问题拆成身份、发现、描述和通信。
2. Agent Description Protocol：看 Agent Description Document 如何描述能力、接口和元数据。
3. Agent Communication Meta-Protocol：看通信前如何协商协议和交互流程。
4. 和 A2A / MCP 对照阅读：只记对象边界，不背 volatile 字段。
