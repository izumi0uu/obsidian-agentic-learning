---
type: source
source_type: paper
title: "Model Context Protocol Threat Modeling and Analyzing Vulnerabilities to Prompt Injection with Tool Poisoning"
url: "https://arxiv.org/abs/2603.22489"
author: Charoes Huang, Xin Huang, Ngoc Phu Tran, Amin Milani Fard
site: arxiv.org
topic:
  - security
  - mcp
  - agent
  - frontier
created: 2026-05-06
updated: 2026-05-07
last_checked: 2026-05-07
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Tool Poisoning]]"
  - "[[MCP]]"
  - "[[Prompt Injection]]"
  - "[[Tool Registry]]"
---

# MCP Tool Poisoning Threat Model

## 为什么收

MCP 让工具可发现、可组合、可远程接入，也带来工具描述、工具返回值、权限和供应链层面的新攻击面。这篇新论文适合支撑 [[Tool Poisoning]] 的前沿风险卡。

## 一句话

MCP tool poisoning 关注恶意或被污染的工具描述/结果如何诱导模型执行非预期动作。

## 先读什么

- Threat model：MCP host/client/server、LLM、external data store、authorization server。
- Prompt injection with tool poisoning：工具描述和返回内容如何影响模型。
- Mitigations：权限、确认、隔离和审计。

## 可以拆成概念卡

- [[Tool Poisoning]]
- [[MCP]]
- [[Prompt Injection]]

## 我的疑问

- Tool registry 是否需要像 package registry 一样做签名、版本和信任等级？
- 工具描述应不应该被视为不可信输入？

## 边界提醒

Tool poisoning 和 prompt injection 经常组合出现：攻击者不一定直接控制用户 prompt，而是控制工具、工具说明或工具返回的内容。
