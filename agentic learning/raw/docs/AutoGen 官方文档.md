---
type: source
source_type: docs
title: "AutoGen AgentChat Teams Documentation"
url: "https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/teams.html"
author: Microsoft / AutoGen
site: microsoft.github.io
topic:
  - agent
  - framework
  - multi-agent
  - autogen
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
conflicts:
  - "Microsoft Agent Framework 已被官方描述为 AutoGen 与 Semantic Kernel 的下一代/继任框架；AutoGen 本身仍有 stable docs，但生产选型需要同时看 Microsoft Agent Framework 迁移路线。"
status: seed
source:
related:
  - "[[AutoGen]]"
  - "[[Agent Framework]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Handoff]]"
  - "[[Agent Framework 编排范式对比]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
---

# AutoGen 官方文档

## 为什么收

AutoGen 是多 Agent 框架比较里绕不开的早期代表。它把多个可对话 agent 组织成 team / group chat，适合学习“用消息轮次和说话人选择来编排协作”的范式，也适合和 LangGraph 的 state graph、CAMEL 的 role-playing、Microsoft Agent Framework 的 workflow 继任路线做边界区分。

## 先读什么

- AgentChat Teams tutorial
- RoundRobinGroupChat / SelectorGroupChat
- Swarm / HandoffMessage
- MagenticOneGroupChat
- Termination conditions / state / observability 相关章节

## 一句话

AutoGen 的 AgentChat Teams 把多智能体系统组织成“由多个 agent 共同完成目标的 team”，核心学习点是 group chat、speaker selection、termination condition 和 handoff 这类 conversation-first orchestration。

## 需要我读的内容

### 必读

#### 必读块 1：Teams / group chat 抽象

- 位置：AutoGen Teams tutorial / 开头说明
- 为什么必读：支撑 AutoGen 概念卡里“conversation / team 编排”的定义。
- 原文短摘：官方页面说明 team 是一组 agents 共同完成共同目标。
- 中文概括：AutoGen 的多 Agent 入口不是先画全局状态图，而是把多个 agent 放进 team，让它们通过消息协作，并用 preset 或规则控制轮次。
- 支撑概念：[[AutoGen]], [[Multi-agent Orchestration]], [[Handoff]]
- 证据边界：只支持 AutoGen AgentChat 当前文档里的 team 抽象；不证明所有 AutoGen 版本或 AG2 fork 的 API 边界。

#### 必读块 2：Team presets 与复杂度提醒

- 位置：AutoGen Teams tutorial / AgentChat supports several team presets 与 Note
- 为什么必读：支撑“AutoGen 有多种 conversation orchestration preset，但多 Agent 需要更多脚手架”的边界。
- 原文短摘：官方列出 RoundRobin、SelectorGroupChat、MagenticOneGroupChat、Swarm 等 preset，并提醒复杂任务才需要 team。
- 中文概括：AutoGen 不只是“几个角色互相聊天”，还把说话顺序、speaker selection、handoff 和终止条件做成可配置对象；同时官方提醒简单任务应先优化 single agent。
- 支撑概念：[[AutoGen]], [[Agent Workflow]], [[Handoff]]
- 证据边界：本 note 只作为框架范式证据；生产路线还要看 [[Microsoft Agent Framework 官方文档]]。

## 可以拆成概念卡

- [[AutoGen]]
- [[Agent Framework 编排范式对比]]
- [[Multi-agent Orchestration]]
- [[Handoff]]

## 我的疑问

- AutoGen stable docs 与 Microsoft Agent Framework 迁移路线之间，长期学习时应该把 AutoGen 当研究/原型范式，还是仍当独立生产框架？
- AutoGen 的 graph / swarm / group chat 能力和 LangGraph 的 state graph 何时会在工程责任上重叠？

## 边界提醒

AutoGen 是重要的 conversation-first 多 Agent 框架范式，但 Microsoft 官方已经把 Microsoft Agent Framework 描述为 AutoGen 与 Semantic Kernel 的下一代整合路线。因此 AutoGen 概念卡应重点沉淀“对话式协作/团队编排”这个稳定思想，不把某个版本 API 当长期边界。
