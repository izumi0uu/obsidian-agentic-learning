---
type: source
source_type: docs
title: AGENTS.md and Codex Agent Loop
url: https://developers.openai.com/codex/guides/agents-md
author: OpenAI
site: openai.com
topic:
  - agent
  - coding
  - frontier
created: 2026-05-06
updated: 2026-05-07
last_checked: 2026-05-07
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[AGENTS.md]]"
  - "[[Coding Agent]]"
  - "[[Repo Context]]"
  - "[[Sandbox Workspace]]"
---

# AGENTS.md and Codex Agent Loop

## 为什么收

OpenAI 的 AGENTS.md 指南说明了 Codex 如何使用仓库级说明。OpenAI 对 Codex agent loop 的拆解也说明了本地 coding agent 如何组装系统/开发者/用户/项目文档/环境上下文，以及 AGENTS.md 如何成为 repo-level instructions 的一部分。

辅助来源：<https://openai.com/index/unrolling-the-codex-agent-loop/>

## 一句话

AGENTS.md 是给代码 Agent 的仓库级操作说明，会进入 Agent 的上下文并影响它如何探索、编辑和验证代码。

## 先读什么

- Unrolling the Codex agent loop：看 Codex 如何构建 prompt 和工具列表。
- Codex repo 的 AGENTS.md docs：看文件范围、优先级和层级。
- 真实项目的 AGENTS.md：看测试命令、代码规范和安全边界怎么写。

## 可以拆成概念卡

- [[AGENTS.md]]
- [[Coding Agent]]
- [[Repo Context]]
- [[Sandbox Workspace]]

## 我的疑问

- AGENTS.md 应该多短，哪些细节应该链接到别的文档？
- 多层 AGENTS.md 冲突时，如何确保 Agent 不误读边界？

## 边界提醒

AGENTS.md 不是 README 的替代品。它更像“给 Agent 的操作规程”，应该包含命令、边界、验证方式和项目惯例。
