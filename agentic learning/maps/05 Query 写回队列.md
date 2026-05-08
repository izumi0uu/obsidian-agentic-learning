---
type: map
topic:
  - query
  - llm-wiki
status: active
created: 2026-05-07
updated: 2026-05-08
related:
  - "[[LLM Wiki 工作流]]"
  - "[[02 问题池]]"
  - "[[04 页面目录]]"
---

# 05 Query 写回队列

这页收集“聊天里已经产生了有用理解，但还没写回 wiki”的内容。

## 使用规则

- 如果回答产生了新定义、新边界、新对比、新操作流程，必须进入这里或直接写进概念卡。
- 每周维护时处理 pending 项。
- 写回后把状态改成 `done`，并链接目标页面。

## 队列

| 日期 | 状态 | 问题 | 应写入 | 处理 |
|---|---|---|---|---|
| 2026-05-07 | done | “我现在这个项目践行了 LLM Wiki 吗？” | [[Obsidian + LLM Wiki]], [[LLM Wiki 工作流]] | 已写回“早期可用版 / 人工监督的 LLM 学习 wiki”边界 |
| 2026-05-07 | done | “$ralplan 底层是在做什么？” | [[Oh My Codex (OMX)]], [[oh-my-codex 使用教程]] | 已写回 prompt routing + state + plan artifact + stop hook |
| 2026-05-08 | done | “现在的 agent 都在使用 ReAct 范式吗？ReAct 的局限现在怎么解决？” | [[ReAct]], [[Agent Loop]], [[Agent Harness]] | 已写回 ReAct 作为行动循环思想、不是所有 Agent 固定模板的边界 |
| 2026-05-08 | done | “现在框架是怎么更好地接管 ReAct / Plan-and-Solve 这类 prompt pattern？” | [[Agent Framework]], [[Agent Harness]], [[Tool Calling]] | 已写回框架接管 prompt loop 的工具、状态、流程、执行、权限、观测六层 |

## 写回模板

```md
| YYYY-MM-DD | pending | 问题 | `目标页面` | 处理动作 |
```
