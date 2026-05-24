---
type: source
source_type: repo
title: agents-best-practices
url: https://github.com/DenisSergeevitch/agents-best-practices
author: Denis Sergeevitch
site: github.com
topic:
  - agent
  - harness
  - workflow
  - engineering-practice
created: 2026-05-24
updated: 2026-05-24
last_checked: 2026-05-24
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Agent Harness]]"
  - "[[Agent Workflow]]"
  - "[[Tool Permissioning]]"
  - "[[Workflow Guardrails]]"
  - "[[Agent Skills]]"
  - "[[Progressive Disclosure]]"
  - "[[Context Engineering]]"
  - "[[Observability]]"
  - "[[Evaluation]]"
  - "[[Trace]]"
  - "[[Trajectory Evaluation]]"
  - "[[Trajectory Trace 类型对比]]"
---

# Agents Best Practices Repo

## 为什么收

`agents-best-practices` 是一个面向 Agent harness 设计、审计和工程落地的 best-practices skill / reference repo。它的价值不在于提供又一个框架，而在于把现代 Agent 开发中容易散落的工程责任收束成一组检查面：loop、工具、权限、规划、目标、上下文压缩、memory、skills、MCP / connector、prompt caching、observability、eval 和 launch gate。

这份资料适合补强“工程化 Agent 开发实践”：当学习从“什么是 Agent”进入“怎样安全、可复现、可评估地做 Agent harness”时，它能作为 checklist / blueprint / audit 入口。

## 主源

- GitHub repo: <https://github.com/DenisSergeevitch/agents-best-practices>
- README: <https://github.com/DenisSergeevitch/agents-best-practices/blob/main/README.md>
- Skill entry: <https://github.com/DenisSergeevitch/agents-best-practices/blob/main/SKILL.md>
- References directory: <https://github.com/DenisSergeevitch/agents-best-practices/tree/main/references>
- GitHub contents API checked on 2026-05-24: root includes `README.md`, `SKILL.md`, and `references/`.

## 一句话

它是一个 provider-neutral 的 Agent harness 工程实践包：帮助从 MVP blueprint、现有 harness audit、工具权限设计、上下文/记忆/压缩、skills/connectors、观测评测和上线门禁等角度检查 Agent 系统。

## 学习时先看

1. `SKILL.md`：看它如何把 agentic harness 任务拆成 architecture、loop、tools、permissions、context、memory、planning、goals、skills、connectors、security、evals 和 observability。
2. `references/mvp-agent-blueprint.md`：用于新建领域 Agent 的 MVP 设计骨架。
3. `references/architecture.md` 和 `references/agentic-loop.md`：用于理解 harness component boundary 和 provider-neutral loop。
4. `references/tools-and-permissions.md`：用于连接 [[Tool Permissioning]]、approval、sandbox 和 structured tool result。
5. `references/context-memory-compaction.md` 与 `references/prompt-caching-and-cost.md`：用于连接 [[Context Engineering]]、compaction、cache-aware context layout 和成本治理。
6. `references/security-evals-observability.md` 与 `references/checklists.md`：用于连接 [[Workflow Guardrails]]、[[Observability]]、[[Evaluation]] 和 launch gate。

## Evaluation / Trajectory 边界

这份 repo 明确包含 evaluation：`SKILL.md` 和 `references/security-evals-observability.md` 都把 evals、trace events、launch criteria、failure probes 和 regression eval 作为 Agent harness 的组成部分。

它也覆盖 [[Trajectory]] 的核心使用场景，但更常用的入口词是 [[Trace]]、trace grading、tool calls and decisions after the run。也就是说，它不是一份“Trajectory 概念定义”资料，而是一份把 Agent run 的过程记录、过程评分和失败回放纳入工程 checklist 的资料。写回时更适合连接 [[Trajectory Evaluation]] 和 [[Trajectory Trace 类型对比]]，而不是把它当成只讲 trajectory 的主源。

## 可以写回的既有概念

优先作为这些既有概念的工程例子和 checklist 证据，不急着新建概念卡：

- [[Agent Harness]]
- [[Agent Workflow]]
- [[Tool Permissioning]]
- [[Workflow Guardrails]]
- [[Agent Skills]]
- [[Progressive Disclosure]]
- [[Context Engineering]]
- [[Observability]]
- [[Evaluation]]
- [[Trace]]
- [[Trajectory Evaluation]]
- [[Trajectory Trace 类型对比]]

## 边界提醒

它不是 Agent 行业标准，也不是 OpenAI / Anthropic / MCP 的官方规范。repo 中引用了多个 provider 和协议方向，具体 API、产品能力、prompt caching 规则、MCP 版本和安全建议都需要回到官方文档复查。

它也不是“prompt 安全策略”。资料中的核心边界更接近当前 vault 已经沉淀的判断：模型不直接执行动作，真正的工具调用、权限、审批、沙箱、trace、预算和停止条件应该由 [[Agent Harness]] / runtime 承担。

## 我的疑问

- 这份 checklist 和 [[OpenAI - A Practical Guide to Building Agents]]、[[Anthropic - Building Effective Agents]] 的边界有哪些重合和差异？
- 是否值得把其中的 launch gate / harness audit 思路沉淀成一个单独 topic，例如“Agent 工程最佳实践清单”？
- 其中 provider-specific 的建议哪些已经被现有官方文档覆盖，哪些只是工程综合判断？
