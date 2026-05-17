---
type: source
source_type: docs
title: Prefect Workflow Control Points
url: https://docs.prefect.io/
author: Prefect
site: docs.prefect.io
topic:
  - workflow
  - durable-execution
  - guardrails
  - infrastructure
created: 2026-05-14
updated: 2026-05-14
last_checked: 2026-05-14
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Workflow Guardrails]]"
  - "[[Workflow Guardrails 与 Prefect 控制点映射]]"
  - "[[Durable Execution]]"
  - "[[Agent Workflow]]"
---

# Prefect Workflow Control Points

## 为什么收

Prefect 文档通常不把这些能力叫做 guardrails，但 state change hooks、transactions 和 automations 可以承载 workflow guardrail 的一部分工程语义：失败回写、通知、补偿、阻断副作用、commit/rollback、幂等和事件驱动治理。

这页作为证据层，只记录 Prefect 能提供哪些 workflow control points；“如何映射成 guardrail”写到 [[Workflow Guardrails 与 Prefect 控制点映射]]。

## 一句话

Prefect 的 hooks、transactions 和 automations 不是 LLM guardrail 产品，但它们可以作为 workflow guardrails 的状态边界、副作用边界和运行时观测/处置边界。

## 需要我读的内容

### 必读块 1：state change hooks

- 位置：State change hook how-to：<https://docs-3.prefect.io/v3/how-to-guides/workflows/state-change-hooks>
- 为什么必读：支撑 flow/task 在进入 Completed、Failed、Cancelling、Crashed、Running 等状态时执行逻辑。
- 中文概括：`on_completion`、`on_failure`、`on_cancellation`、`on_crashed`、`on_running` 可绑定在 flow 或 task 状态变化上，用于通知、审计、错误处理或补偿入口。
- 支撑概念：[[Workflow Guardrails]], [[Durable Execution]], [[Audit Log]]。
- 证据边界：state hook 负责状态边界，不等于内容安全检测；检测结果仍需要业务代码、model guardrail、validator 或 policy engine 产生。

### 必读块 2：transactions

- 位置：Transactions：<https://docs-3.prefect.io/v3/advanced/transactions>
- 为什么必读：支撑副作用 guardrail，特别是写 DB、写文件、调用外部服务之前后的 commit / rollback 语义。
- 中文概括：Prefect transactions 支持 transactional semantics、rollback、commit 生命周期和 idempotency；适合把“通过验证才提交副作用”写成 workflow 结构。
- 支撑概念：[[Workflow Guardrails]], [[Durable Execution]], [[Patch Validation]]。
- 证据边界：transaction 保护的是任务副作用的一致性和恢复，不自动判断 LLM 输出是否真实或合规。

### 必读块 3：automations

- 位置：Automations：<https://docs.prefect.io/latest/guides/automations/>
- 为什么必读：支撑运行时 observability guardrail：事件触发通知、暂停/恢复 schedule 或 work pool、创建 flow run 等动作。
- 中文概括：Prefect automations 可在事件触发时执行动作，适合处理失败告警、超时、异常状态和运行治理。
- 支撑概念：[[Workflow Guardrails]], [[Observability]], [[Agent Workflow]]。
- 证据边界：automation 更像运行治理和事件响应，不是模型内容过滤器。

## 可以拆成概念卡

- 暂不单独建 “Prefect Guardrails” 卡。Prefect docs 本身没有把这些能力定义成 guardrails。
- 值得写入的是 [[Workflow Guardrails 与 Prefect 控制点映射]]：把 hooks / transactions / automations 映射到 guardrail 承载点。

## 我的疑问

- 对 LLM 输出写 DB 这类任务，validation failure 应该表现为 task failure、custom state，还是业务表里的 FAILED 状态？
- retry / reask / human review 的边界应放在 Prefect retry policy、LLM validator on_fail，还是单独的 review flow？
- 对不可逆外部 API 调用，transaction 能覆盖到哪一步，哪些仍必须靠业务幂等键和补偿任务？

## 边界提醒

Prefect control points 只能承载 guardrail 结果，不能替代 guardrail 判断本身。对 LLM workflow 来说，schema validator、policy engine、Bedrock ApplyGuardrail、人工审批和业务校验仍要和 Prefect 状态/事务/事件配合。
