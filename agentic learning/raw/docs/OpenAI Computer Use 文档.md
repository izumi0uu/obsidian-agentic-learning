---
type: source
source_type: docs
title: OpenAI Computer Use
url: https://developers.openai.com/api/docs/guides/tools-computer-use
author: OpenAI
site: developers.openai.com
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
  - "[[Sandbox Workspace]]"
---

# OpenAI Computer Use 文档

## 为什么收

OpenAI Computer Use 是理解 CUA、浏览器/桌面操作 loop、安全确认和 sandbox 的主源之一。

## 一句话

Computer Use 让模型通过截图理解环境，并返回 click、type、scroll 等动作，由宿主代码执行后再把新截图反馈给模型。

## 先读什么

- How it works：screenshot/action loop。
- Setting up your environment：sandbox browser 或 VM。
- Risk and safety：human-in-the-loop、allowlist、隔离环境。

## 可以拆成概念卡

- [[Computer Use]]
- [[Browser Agent]]
- [[GUI Grounding]]
- [[Approval Gate]]
- [[Sandbox Workspace]]

## 我的疑问

- 哪些任务应该用 computer use，哪些应该写确定性 API/script？
- 截图和可访问性树哪个更适合给模型？

## 边界提醒

Computer Use 能碰到真实站点、表单和登录态，因此它是安全边界，不只是自动化便利功能。
