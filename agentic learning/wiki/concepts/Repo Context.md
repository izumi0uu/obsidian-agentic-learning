---
type: concept
topic:
  - coding-agent
  - rag
status: seed
created: 2026-05-05
updated: 2026-05-05
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[SWE-bench]]"
evidence:
  - "[[SWE-bench#为什么收]]"
related:
  - "[[Coding Agent]]"
  - "[[RAG]]"
  - "[[Patch Validation]]"
---

# Repo Context

## 一句话

Repo Context 是代码 Agent 为解决任务需要理解的代码库上下文。

## 它解决什么问题

真实代码修改很少只依赖一个函数。Agent 需要知道文件结构、相关符号、依赖、测试、配置和项目约定。

## 它不是什么

Repo Context 不是把整个代码库一次性塞进上下文窗口。

它也不是普通文本检索的简单套用。代码库有符号关系、调用关系、测试关系和目录约定。

## 最小例子

一个 bug 出现在 API 返回值里，Agent 可能要同时读 route、service、model、test 和配置文件。

## 边界细节

Repo Context 是代码 Agent 里的 RAG 问题，但比普通文档 RAG 多了结构和执行反馈。

## 证据锚点

- Source: [[SWE-bench]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Coding Agent]]
- [[RAG]]
- [[Patch Validation]]
