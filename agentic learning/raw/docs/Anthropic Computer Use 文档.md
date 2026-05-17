---
type: source
source_type: docs
title: Anthropic Computer Use Tool
url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool
author: Anthropic
site: docs.claude.com
topic:
  - agent
  - tools
  - computer-use
  - frontier
created: 2026-05-06
updated: 2026-05-07
last_checked: 2026-05-07
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Computer Use]]"
  - "[[Browser Agent]]"
  - "[[GUI Grounding]]"
  - "[[Approval Gate]]"
---

# Anthropic Computer Use 文档

## 为什么收

Anthropic 是 computer use 能力的重要主源之一，文档包含工具版本、reference implementation、agent loop、工具 token 开销和安全提醒。

## 一句话

Anthropic computer use 让 Claude 通过预定义工具与计算机环境交互，并由开发者实现执行环境和反馈 loop。

## 先读什么

- Computer use tool。
- Reference implementation。
- Prompt injection 和权限相关提醒。

## 可以拆成概念卡

- [[Computer Use]]
- [[Browser Agent]]
- [[GUI Grounding]]

## 我的疑问

- 浏览器工具、文件编辑工具、shell 工具应该共用一个 approval policy 吗？
- Computer use 的安全评估应该怎样设计测试集？

## 边界提醒

Computer use 的失败不一定是模型“不会推理”，也可能是 UI 状态、坐标、登录态、弹窗、权限或页面变化导致。
