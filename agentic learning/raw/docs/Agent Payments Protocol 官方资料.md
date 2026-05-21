---
type: source
source_type: docs
title: Agent Payments Protocol 官方资料
url: https://ap2-protocol.org/
author: Google / google-agentic-commerce
site: ap2-protocol.org
topic:
  - agent
  - protocol
  - payments
  - security
  - frontier
created: 2026-05-20
updated: 2026-05-20
last_checked: 2026-05-20
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Agent Payments Protocol]]"
  - "[[A2A]]"
  - "[[MCP]]"
  - "[[Approval Gate]]"
  - "[[Tool Permissioning]]"
  - "[[Audit Log]]"
---

# Agent Payments Protocol 官方资料

## 为什么收

AP2 是 Agent 从“调用工具”走向“代表用户发起交易/支付”时必须理解的协议边界。它把用户授权、商户验证、支付方式和审计责任从普通 tool call 中拆出来，适合和 [[A2A]]、[[MCP]]、[[Approval Gate]]、[[Tool Permissioning]] 一起学习。

## 先读什么

- Agent Payments Protocol official site / specification
- Google Cloud announcement: Powering AI commerce with the new Agent Payments Protocol
- GitHub README
- docs/specification
- samples for human-present and human-not-present scenarios

## 一句话

Agent Payments Protocol / Agentic Payment Protocol（AP2）是用于 agent-led payments / agentic commerce 的开放协议方向，核心问题是证明用户授权、交易意图和支付内容可审计。

## 关键事实

- AP2 official site 当前把协议定位为开放、支付无关、面向 agent-led transactions 的规范；spec v0.2 使用 Agentic Payment Protocol 名称。
- Google Cloud announcement 把 AP2 描述为可作为 A2A 和 MCP 扩展使用的开放协议，用于跨平台发起和处理 Agent 主导的支付。
- AP2 关注授权、真实性和责任归属：谁授权了交易、商户如何确认 agent 请求反映用户真实意图、错误或欺诈交易如何追责。
- Google announcement 使用 Mandates 和 verifiable credentials 作为信任机制：Intent / Cart / Payment 的证据链用于把用户意图、购物车内容和支付授权连接起来。
- GitHub repo 包含 docs、SDK、schemas 和 human-present / human-not-present 等样例；README 明确样例可使用 ADK / Gemini，但协议本身不要求特定 agent framework 或模型。
- AP2 生态仍在快速变化，spec 版本、repo release、FIDO 标准化、x402 / stablecoin 扩展和商户集成都需要复查。

## 可以拆成概念卡

- [[Agent Payments Protocol]]
- [[Approval Gate]]
- [[Tool Permissioning]]
- [[Audit Log]]
- [[A2A]]
- [[MCP]]

## 边界提醒

AP2 不是支付处理器，不替代风控、KYC、反欺诈、退款争议处理或商户系统。它也不是 MCP / A2A 的同义词：A2A 偏 Agent 间通信和任务协作，MCP 偏工具/资源连接，AP2 则把高风险交易动作里的授权、意图和审计证据标准化。

## 证据边界

本 note 只做 source-level 摘要。AP2 的安全性不能从协议存在直接推出；未来要结合 prompt injection、tool poisoning、replay、credential binding、merchant policy 和 human approval 做风险复查。
