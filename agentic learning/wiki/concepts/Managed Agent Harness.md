---
type: concept
topic:
  - agent
  - harness
  - runtime
  - cloud
status: seed
created: 2026-05-20
updated: 2026-05-20
last_checked: 2026-05-20
freshness: volatile
conflicts: []
aliases:
  - Managed Agents
  - Claude Managed Agents
  - Managed Agent Runtime
  - 托管 Agent
  - 托管 Agent Harness
  - 托管 Agent 运行时
source:
  - "[[Anthropic Managed Agents 文档]]"
  - "[[Agent Harness]]"
  - "[[AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents]]"
evidence:
  - "[[Anthropic Managed Agents 文档#关键事实]]"
  - "[[Agent Harness#证据锚点]]"
  - "[[AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents#需要我读的内容]]"
related:
  - "[[Agent Harness]]"
  - "[[Agent Skills]]"
  - "[[MCP]]"
  - "[[Sandbox Workspace]]"
  - "[[Trace]]"
  - "[[Durable Execution]]"
  - "[[Tool Permissioning]]"
---

# Managed Agent Harness

## 一句话

Managed Agent Harness 是由平台托管的 Agent 运行外壳：它替开发者提供 agent loop、工具执行、环境、session、事件流和部分安全/性能基础设施。

## 概念详解

[[Agent Harness]] 原本回答“Agent 在哪里、用什么权限、留下什么证据、如何停止或恢复”。Managed Agent Harness 则把这层运行外壳产品化：开发者不再完全自建 loop、sandbox、tool executor、session store 和 event stream，而是通过平台 API 创建 agent、environment 和 session。

Claude Managed Agents 是一个清晰样本。官方 overview 把它定位为托管基础设施里的预置可配置 harness，适合长任务和异步工作。开发者定义模型、system prompt、tools、MCP servers 和 skills；再配置环境是平台云容器还是自托管 sandbox；每次任务运行成为 session；应用和 agent 之间通过 events 交互，结果可以流式返回。

这个概念的学习价值在于：它把 “Agent 产品” 拆成更具体的托管边界。模型是 brain 的一部分，但 Managed Agent Harness 还包括 loop、工具路由、文件系统/容器、web / bash / MCP 等工具、事件日志、session 持久化、steer/interrupt、prompt caching 和 compaction。它不是让模型更聪明，而是把长任务需要的运行系统交给平台维护。

Anthropic engineering post 还给出一个重要架构切口：把 session、harness、sandbox 解耦。session 是事件日志，harness 是调用 Claude 并路由工具调用的 loop，sandbox 是运行代码和编辑文件的执行环境。解耦后，sandbox 或 harness 可以失败、替换或恢复，credentials 也不需要暴露给生成代码运行的环境。

## 它解决什么问题

Managed Agent Harness 解决的是“长任务 Agent 的基础设施由谁来建和运营”的问题。

自建 harness 时，团队要处理容器、权限、工具调用、事件流、状态持久化、恢复、网络、认证、日志和成本。托管 harness 把这些变成平台能力，适合想快速把 Agent 接到真实工作流、又不想从零搭运行外壳的团队。

## 它不是什么

Managed Agent Harness 不是模型本身。模型生成意图，harness 承载执行。

它也不是普通 SDK。SDK 可能只给开发者本地抽象；managed harness 还包含平台托管环境、session、工具执行和事件流。

它也不是正确性保证。托管基础设施不自动保证任务做对、工具权限合理、数据合规或费用可控。

## 最小例子

```text
Create agent:
  model + system prompt + tools + MCP servers + skills

Create environment:
  cloud container or self-hosted sandbox

Start session:
  user event -> agent runs tools -> event stream -> persisted history

Steer / interrupt:
  send new event or stop/re-route the session
```

## 常见误解 / 风险

- 误解：Managed Agent Harness 等于“更强模型”。它主要是运行、工具、环境和 session 基础设施。
- 误解：用了托管 harness 就不用权限设计。高风险工具、数据范围、凭证、输出通道仍要治理。
- 风险：供应商托管意味着数据、日志、网络、成本和可观测性边界要复查。
- 风险：beta 产品的 API、session 行为、工具清单和限制会变化。
- 风险：平台替你管理 harness，不代表你的任务定义、验收标准和 human gate 已经正确。

## 边界细节

Managed Agent Harness 和 [[Agent Framework]] 的边界：framework 偏开发者抽象和可组合 API；managed harness 偏托管运行系统。一个平台可以同时提供 SDK 和 managed harness，但学习时要分开“用什么写”和“在哪里由谁运行”。

Managed Agent Harness 和 [[Sandbox Workspace]] 的边界：sandbox 是执行环境；managed harness 是包住模型、session、tools、sandbox 和事件的更大运行外壳。

Managed Agent Harness 和 [[Durable Execution]] 的关系：managed harness 常需要 session 持久化、事件日志和恢复能力，但不等于所有 durable execution 问题都已解决；外部副作用、事务、重试幂等和人工审批仍需要业务设计。

## 现代性状态

- frontier / volatile：Claude Managed Agents 这类平台托管 harness 是 2026 年前后快速成形的产品化方向，API 和能力会变化。
- 当前工程趋势：Agent 基础设施从“每个应用自建 loop + sandbox + tool router”向托管 session / event / environment / tool execution 收敛。
- 稳定学习价值：把 model、harness、sandbox、session、tools 和 credentials 拆开，是理解生产 Agent 的重要边界。

## 现代系统怎么吸收 Managed Agent Harness 的价值 / 局限

价值吸收方式：把长任务执行、工具路由、session 日志、环境初始化、失败恢复和 stream 交给平台，让应用层更关注任务定义、业务工具、审批和验收。

局限吸收方式：不要把托管平台当成安全和质量的最终裁判。业务侧仍要设计最小权限、数据隔离、approval gate、审计日志、任务验收和成本预算；对自托管 sandbox、VPC、凭证代理等边界要单独复查。

## 证据锚点

- Evidence type: official docs — [[Anthropic Managed Agents 文档#关键事实]]
- Evidence type: existing concept synthesis — [[Agent Harness#证据锚点]]
- Evidence type: paper/source boundary — [[AI Harness Engineering - A Runtime Substrate for Foundation-Model Software Agents#需要我读的内容]]
- Evidence type: engineering synthesis — 本卡把托管产品文档和 harness 运行支架概念合并为“平台托管运行外壳”的学习边界。
- Boundary: Managed Agent Harness 只写成平台托管的运行外壳，不写成模型本身、普通 SDK、Agent Framework 同义词或正确性/安全性保证。
- Confidence: medium. 产品能力、beta 状态和具体 API 属于 volatile。

## 复习触发

- Managed Agent Harness 和 Agent Framework 的区别是什么？
- 为什么 session、harness、sandbox 解耦能改善恢复和安全？
- 如果 Agent 可以在托管容器里跑 bash，哪些权限和凭证边界仍不能交给模型自律？
- 托管 harness 解决了什么基础设施问题，又没有解决哪些业务验收问题？

## 相关链接

- [[Agent Harness]]
- [[Agent Skills]]
- [[MCP]]
- [[Sandbox Workspace]]
- [[Trace]]
- [[Durable Execution]]
- [[Tool Permissioning]]
