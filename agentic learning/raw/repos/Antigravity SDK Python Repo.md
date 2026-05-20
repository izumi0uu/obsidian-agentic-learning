---
type: source
source_type: repo
title: "Google Antigravity SDK Python"
url: https://github.com/google-antigravity/antigravity-sdk-python
author: google-antigravity
site: github.com
topic:
  - agent
  - agent-framework
  - sdk
  - runtime
created: 2026-05-20
updated: 2026-05-20
last_checked: 2026-05-20
freshness: volatile
conflicts:
  - "GitHub HEAD and DeepWiki indexed commit differed on 2026-05-20; use GitHub source for current API details."
status: seed
source:
  - https://github.com/google-antigravity/antigravity-sdk-python
  - https://deepwiki.com/google-antigravity/antigravity-sdk-python
related:
  - "[[Agent Framework]]"
  - "[[Agent Harness]]"
  - "[[Tool Calling]]"
  - "[[Tool Permissioning]]"
  - "[[MCP]]"
  - "[[Agent State]]"
  - "[[Trace]]"
---

# Antigravity SDK Python Repo

## 为什么收

这个仓库适合当作 [[Agent Framework]] / Agent SDK runtime 的源码学习样本。README 将它定位为用于构建 Antigravity 和 Gemini 驱动 AI agents 的 Python SDK，并强调它提供 secure、scalable、stateful 的基础设施层来抽象 agentic loop。

它和 `claude-code-cli` 的关键差异是：这里的主角不是一个已经做好的终端 Coding Agent 产品，而是一套给开发者构建 Agent 的 SDK / runtime 抽象。它把 `Agent`、`Conversation`、`Connection`、tools、hooks、policies、MCP、triggers 和 local harness 拆成可组合模块。

## 一句话

`antigravity-sdk-python` 是开发者侧 Agent SDK / runtime framework 样本，用来观察“如何把 agentic loop 做成可复用 Python API”。

## 主源

- GitHub repo: <https://github.com/google-antigravity/antigravity-sdk-python>
- GitHub API / README checked: 2026-05-20；default branch 为 `main`，HEAD 为 `287894d3b5689b99fcea97900d05cfa7fe93fcbf`。
- PyPI package name from README: `google-antigravity`。
- DeepWiki / Devin docs: <https://deepwiki.com/google-antigravity/antigravity-sdk-python>
- DeepWiki indexed commit: `38cae443`，generated at 2026-05-19。

## DeepWiki 导读价值

DeepWiki 适合当作源码地图，而不是替代 README 或源码。它把这个 SDK 切成了几条很适合学习的线：

- `SDK Architecture: Three-Layer Design`：对应 README 的三层架构，`Agent` 是高层入口，`Conversation` 管 session/history/streaming，`Connection` 抽象 transport/backend。
- `Agent Class and Lifecycle`：看 SDK 如何把 binary discovery、tool wiring、hook registration 和 policy defaults 包进 Agent 生命周期。
- `Conversation Session Management`：看 step history、turn count、ChatResponse 和 streaming 如何构成 stateful session。
- `Local Connection and localharness`：看 Python SDK 如何依赖本地 compiled runtime binary 执行 harness 责任。
- `Hooks System` / `Policy System`：看 tool call 之前如何做 allow / deny / ask_user 这类 runtime governance。
- `Tools and MCP Integration`：看 Python function tools 与 MCP server tools 如何被统一暴露给 Agent。
- `Triggers`：看外部事件或定时任务如何主动把消息推入 Agent。

## 可以拆给哪些概念用

- [[Agent Framework]]：把 agent loop、tools、state、hooks、policies、MCP 和 triggers 做成 SDK 抽象。
- [[Agent Harness]]：local harness / binary runtime 承担工具执行和本地环境管理。
- [[Agent State]]：Conversation 的 history、step、turn 和 response stream 是状态边界入口。
- [[Tool Calling]]：Python functions 和 MCP tools 都被包装成模型可调用能力。
- [[Tool Permissioning]]：默认 read-only、capabilities 和 declarative policies 体现权限分层。
- [[MCP]]：SDK 支持连接 MCP servers 并把外部 tools 暴露给 Agent。
- [[Trace]]：step history、tool call stream 和 policy decisions 可以作为轨迹证据入口。

## 边界提醒

这个仓库是快速变化的 SDK / runtime 层，适合保持 `freshness: volatile`。当前稳定可学的是工程分层：`Agent -> Conversation -> Connection`，以及 hooks / policies / local harness / MCP integration 如何一起构成 Agent runtime。

具体 API、wheel packaging、local harness binary、policy helper 名称和 release 流程都可能变化；写概念卡时不要把这些实现名当作长期概念。

## 复习触发

- 为什么 `antigravity-sdk-python` 更像 Agent SDK / runtime framework，而不是具体 Agent 产品？
- `Agent`、`Conversation`、`Connection` 三层分别承担什么责任？
- 默认 read-only、capabilities 和 policies 如何体现 Agent 工程中的权限设计？
- MCP tools 和 Python function tools 在 SDK 中为什么可以被看成同一类 tool surface？
