---
type: source
source_type: docs
title: Microsoft Agent Framework Overview
url: https://learn.microsoft.com/en-us/agent-framework/overview/
author: Microsoft
site: learn.microsoft.com
topic:
  - agent
  - framework
  - microsoft
  - multi-agent
created: 2026-05-12
updated: 2026-05-12
last_checked: 2026-05-12
freshness: volatile
conflicts:
  - Microsoft Learn 当前把 Agent Framework 标为 public preview；同时官方 blog 将其描述为 Semantic Kernel / AutoGen 的 successor。生产判断需持续复查 GA 状态。
status: seed
source:
  - https://devblogs.microsoft.com/agent-framework/semantic-kernel-and-microsoft-agent-framework/
related:
  - "[[Microsoft Agent Framework]]"
  - "[[AutoGen]]"
  - "[[Agent Framework]]"
  - "[[Agent Framework 编排范式对比]]"
  - "[[Agent Framework 全量选型对比 2026-05]]"
---

# Microsoft Agent Framework 官方文档

## 为什么收

Microsoft Agent Framework 是理解微软 Agent 框架路线的关键：它把 AutoGen 的 agent / multi-agent patterns 和 Semantic Kernel 的企业工程特性合并，并引入 workflow、state、telemetry、middleware 等生产化能力。用户提到“比如微软的”时，最应该纳入对比的是这条继任路线，而不是只停留在 AutoGen 旧范式。

## 先读什么

- Microsoft Agent Framework Overview
- Agents overview
- Workflows overview
- Migration Guide from AutoGen / Semantic Kernel
- Semantic Kernel and Microsoft Agent Framework blog

## 一句话

Microsoft Agent Framework 是微软把 AutoGen 与 Semantic Kernel 经验合并后的下一代 Agent 框架：它区分 agent 与 workflow，并把多 Agent 执行路径、状态、middleware、telemetry 和 human-in-the-loop 等能力放进统一 SDK。

## 需要我读的内容

### 必读

#### 必读块 1：Agent vs workflow 边界

- 位置：Microsoft Learn Overview / When to use agents vs workflows
- 为什么必读：支撑 Microsoft Agent Framework 概念卡里“不是所有任务都要 Agent”的判断。
- 原文短摘：官方表格区分 open-ended/conversational task 与 well-defined steps，并提醒如果函数能处理，就用函数而不是 AI agent。
- 中文概括：微软路线强调 agent 和 workflow 都是一等对象：开放任务适合 agent，有明确步骤的流程适合 workflow；这能防止把所有编排问题都写成自由多 Agent 对话。
- 支撑概念：[[Microsoft Agent Framework]], [[Agent Workflow]], [[Agent Framework]]
- 证据边界：这是 Microsoft Learn 当前 docs 的产品语义；具体 API 与 preview/GA 状态会变。

#### 必读块 2：AutoGen + Semantic Kernel successor

- 位置：Microsoft Learn Overview / Why Agent Framework；Microsoft Agent Framework blog
- 为什么必读：支撑“微软框架不应只看 AutoGen”的边界。
- 原文短摘：官方说明 Agent Framework 结合 AutoGen 的简单 agent 抽象与 Semantic Kernel 的企业特性，并称其为二者下一代 / direct successor。
- 中文概括：AutoGen 更像 conversation / multi-agent pattern 的重要来源；Semantic Kernel 提供企业 SDK、类型、安全、telemetry 等经验；Microsoft Agent Framework 尝试把二者收敛成统一入口。
- 支撑概念：[[Microsoft Agent Framework]], [[AutoGen]], [[Agent Framework 编排范式对比]]
- 证据边界：不能因此说 AutoGen/Semantic Kernel 立刻消失；只能说明微软官方路线已经把 MAF 作为新统一框架。

## 可以拆成概念卡

- [[Microsoft Agent Framework]]
- [[AutoGen]]
- [[Agent Framework 编排范式对比]]
- agent vs workflow
- framework migration boundary

## 我的疑问

- Microsoft Agent Framework 从 preview 到 GA 后，AutoGen 与 Semantic Kernel 的定位会如何变化？
- 它和 LangGraph 的 workflow/state graph 抽象在哪些层重叠，哪些层属于 Microsoft/Azure 生态整合？

## 边界提醒

Microsoft Agent Framework 是 product/framework 生态，`freshness` 必须保持 volatile。当前可稳定吸收的是“agent vs workflow 边界”和“AutoGen + Semantic Kernel 继任整合路线”；不要把 preview API 或营销名词写成长期概念。
