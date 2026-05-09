---
type: index
topic:
  - agent
  - obsidian
status: active
created: 2026-05-05
updated: 2026-05-09
related:
  - "[[Agent 知识地图]]"
  - "[[04 页面目录]]"
  - "[[00 学习路线]]"
  - "[[资料收集索引]]"
  - "[[LLM Wiki 工作流]]"
  - "[[字段规范]]"
  - "[[插件配置]]"
---

# Agentic Learning Index

这里是这个 vault 的主入口。

目标不是收藏资料，而是把 Agent 从“听说过的前沿词”变成我能解释、能判断、能实验的知识系统。

## Vault 结构

这个 vault 只保留三层：

```text
raw/  -> 来源证据：网页、论文、文档、repo
wiki/ -> 稳定理解：概念卡、主题页、项目页
maps/ -> 导航和路线：学习路线、术语表、问题池、前沿追踪
```

小边界：raw 记录“我从哪里看到”，wiki 记录“我怎么理解”，maps 只负责“下一步去哪”。

## 快速进入

- [[Agent 知识地图]]
- [[04 页面目录]]
- [[前沿主源清单]]
- [[00 学习路线]]
- [[01 术语表]]
- [[02 问题池]]
- [[03 前沿追踪]]
- [[资料收集索引]]
- [[raw/articles/xiaolinnote/小林 Note 面试题索引]]
- [[agent_java_offer Repo]]
- [[Hello-Agents Repo]]
- [[oh-my-codex 使用教程]]
- [[2026-05-06]]
- [[LLM Wiki 工作流]]
- [[插件配置]]
- [[字段规范]]
- [[2026-05-05]]

## 当前核心概念

```dataview
TABLE topic, status, updated, related
FROM "wiki/concepts"
WHERE type = "concept"
SORT updated DESC
```

## 完整页面目录

静态目录见 [[04 页面目录]]。它用于审计、合并和发现过期页面；动态表格用于日常浏览。

```dataview
TABLE type, status, topic, updated
FROM "wiki" OR "maps" OR "raw" OR "daily"
SORT file.path ASC
```

## 主题入口

- [[Agent 主题]]
- [[LLM 主题]]
- [[RAG 主题]]
- [[前沿主源清单]]

## 待整理来源

```dataview
TABLE source_type, site, topic, created, status
FROM "raw"
WHERE type = "source" AND status = "inbox"
SORT created DESC
```

## 最近更新

```dataview
TABLE type, topic, status, updated
FROM "wiki" OR "maps" OR "daily"
WHERE updated
SORT updated DESC
LIMIT 10
```

## 30 天学习计划

从 [[2026-05-06]] 开始，到 [[2026-06-04]] 结束。每天只做一个最小动作，完整节奏见 [[00 学习路线]]。

```dataview
TABLE status, related
FROM "daily"
WHERE type = "daily"
SORT file.name ASC
```

## 今天只做一件事

从 [[02 问题池]] 里选一个问题，把答案沉淀到一张概念卡里。

## 可以直接叫 Codex 做的事

- “用 obsidian-llm-wiki ingest 某篇 raw source”
- “用 obsidian-llm-wiki query：Agent 和 workflow 的区别是什么？”
- “用 obsidian-llm-wiki lint 这个 vault”

## 我的学习循环

1. 遇到一个概念，先写一句话解释。
2. 找出它解决什么问题。
3. 写清楚它不是什么。
4. 举一个最小例子。
5. 链接到至少两个相关概念。
6. 用一个问题检查自己是否真的懂了。

## Wiki 使用规则

- 每张概念卡只讲一个概念。
- 不复制长文，只沉淀自己的理解。
- 前沿内容必须标日期和来源。
- 不懂的问题比模糊的答案更有价值。
- 每周至少整理一次孤立笔记，把它们接入概念地图。

## 一个关键边界

LLM 是会生成文本的模型；Agent 是围绕目标行动的系统。

Agent 通常包含 LLM，但还需要目标、状态、工具、决策循环和反馈修正。会聊天不等于会代理行动。
