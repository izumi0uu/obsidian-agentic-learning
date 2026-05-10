---
type: map
topic:
  - agent
status: active
created: 2026-05-05
updated: 2026-05-10
related:
  - "[[Agent]]"
  - "[[ReAct]]"
  - "[[Coding Agent]]"
  - "[[Agent 知识地图]]"
  - "[[Environment Observation 类型对比]]"
  - "[[Trajectory Trace 类型对比]]"
---

# Agent 主题

这个主题页聚合所有 `topic` 包含 `agent` 的笔记。

## 概念卡

```dataview
TABLE status, updated, related
FROM "wiki/concepts"
WHERE contains(topic, "agent")
SORT file.name ASC
```

## 待处理资料

```dataview
TABLE source_type, site, created, status
FROM "raw"
WHERE contains(topic, "agent") AND status = "inbox"
SORT created DESC
```

## 相关地图

- [[Agent 知识地图]]
- [[Environment Observation 类型对比]]
- [[Trajectory Trace 类型对比]]
- [[03 前沿追踪]]
- [[oh-my-codex 使用教程]]

## 论文进入的关键概念

- [[ReAct]]
- [[Reflexion]]
- [[Plan-and-Solve Prompting]]
- [[Reasoning Trace]]
- [[Observation]]
- [[Coding Agent]]
- [[Repo Context]]
- [[Patch Validation]]

## 工程工具教程

- [[oh-my-codex 使用教程]]
- [[Oh My Codex (OMX)]]
- [[OMX $ 指令]]
