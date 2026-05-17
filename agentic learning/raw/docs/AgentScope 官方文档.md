---
type: source
source_type: docs
title: AgentScope Documentation
url: https://doc.agentscope.io/
author: AgentScope / Alibaba
site: doc.agentscope.io
topic:
  - agent
  - framework
  - multi-agent
  - agentscope
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
conflicts: []
status: seed
source:
  - https://arxiv.org/abs/2402.14034
related:
  - "[[AgentScope]]"
  - "[[Agent Framework]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Agent Framework 编排范式对比]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
---

# AgentScope 官方文档

## 为什么收

AgentScope 代表“多 Agent 工程平台 / 生命周期管理 / 可部署运行时”的框架路线。它不只是 role-playing 或 group chat 示例，而是把 agent、message、tool、memory、orchestration、observability、deployment 和 distributed mode 放进同一套开发平台。

## 先读什么

- What is AgentScope?
- Basic Concepts: Agent / Message
- Building blocks: Orchestration
- Deploy & serve / OTel / multi-language support
- 论文：AgentScope: A Flexible yet Robust Multi-Agent Platform（arXiv:2402.14034）

## 一句话

AgentScope 是偏工程平台的多 Agent framework：以 message 作为 agent / user / tool 之间的信息交换基础，提供 orchestration、tools、memory、observability、deployment 和分布式运行支持。

## 需要我读的内容

### 必读

#### 必读块 1：AgentScope 的平台定位

- 位置：AgentScope docs homepage / What is AgentScope
- 为什么必读：支撑 AgentScope 概念卡里“production-ready / easy-to-use agent framework”的定位。
- 原文短摘：官方把 AgentScope 描述为 production-ready、easy-to-use agent framework，并列出 tools、memory、observability、MCP、A2A、message hub、deployment 等能力。
- 中文概括：AgentScope 的核心卖点是把开发、编排、观测和部署打包成平台，而不是只提供一种多 Agent 对话提示词。
- 支撑概念：[[AgentScope]], [[Agent Framework]], [[Observability]], [[Handoff]]
- 证据边界：官网表述偏产品定位；能力成熟度仍需按具体版本和代码验证。

#### 必读块 2：Message / distributed mode

- 位置：AgentScope Basic Concepts / Message；旧版 docs Distribution；AgentScope paper abstract
- 为什么必读：支撑“message exchange 是通信核心，分布式能力是工程特色”。
- 原文短摘：文档说明 Msg 是 AgentScope 中交换信息的基础数据结构；论文摘要称 AgentScope 以 message exchange 为核心通信机制，并设计 actor-based distribution framework。
- 中文概括：AgentScope 更像一个多 Agent 应用平台：消息结构、agent 方法、工具调用、memory、deployment 和分布式转换都属于它试图统一管理的工程面。
- 支撑概念：[[AgentScope]], [[Agent State]], [[Multi-agent Orchestration]]
- 证据边界：这里使用 docs + paper abstract 作为来源；不声称所有分布式部署都可无代价扩展。

## 可以拆成概念卡

- [[AgentScope]]
- [[Agent Framework 编排范式对比]]
- message exchange
- distributed multi-agent deployment

## 我的疑问

- AgentScope 的新 docs 与旧 docs / paper 中 distributed mode 的抽象是否完全连续？
- 它更适合应用开发平台、仿真平台，还是生产服务框架？不同版本可能答案不同。

## 边界提醒

AgentScope 的稳定学习价值是“message-centered multi-agent engineering platform”；具体 deployment、OTel、A2A、MCP、skills、serverless/K8s 能力属于快速变化实现层，需保持 `freshness: volatile`。
