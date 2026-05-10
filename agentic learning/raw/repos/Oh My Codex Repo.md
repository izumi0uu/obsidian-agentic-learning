---
type: source
source_type: repo
title: "oh-my-codex (OMX)"
url: "https://github.com/Yeachan-Heo/oh-my-codex"
author: Yeachan-Heo
site: github.com
topic:
  - agent
  - coding-agent
  - workflow
  - frontier
created: 2026-05-06
updated: 2026-05-07
last_checked: 2026-05-10
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Oh My Codex (OMX)]]"
  - "[[oh-my-codex 使用教程]]"
  - "[[Agent Harness]]"
  - "[[Agent Lifecycle Hook]]"
  - "[[Coding Agent]]"
  - "[[Sandbox Workspace]]"
  - "[[Trace]]"
---

# Oh My Codex Repo

## 为什么收

oh-my-codex, 简称 OMX, 是 OpenAI Codex CLI 上的一层多 Agent 编排和运行时增强。它很适合用来理解 [[Agent Harness]]、[[Coding Agent]]、tmux team、git worktree、hooks、state、logs 和 workflow skill 之间的关系。

这不是 Agent 基础概念的地基资料，而是“代码 Agent 工程化运行壳”的前沿实践资料。

## 主源

- GitHub repo: <https://github.com/Yeachan-Heo/oh-my-codex>
- 官方文档: <https://oh-my-codex.dev/docs.html>
- 官方站点: <https://oh-my-codex.dev/index.html>
- v0.16.0 release notes: <https://newreleases.io/project/github/Yeachan-Heo/oh-my-codex/release/v0.16.0>
- npm latest check: 2026-05-06 本地 `npm view oh-my-codex version` 显示 `0.16.0`。

## 一句话

OMX 不替代 Codex。它把 Codex 包进一套工程工作流：clarify -> plan -> execute -> verify，并用 `.omx/`、hooks、tmux、git worktree 和 MCP 工具保存状态、分派任务和追踪执行。

## 可拆概念

- [[Oh My Codex (OMX)]]
- [[Agent Harness]]
- [[Coding Agent]]
- [[Sandbox Workspace]]
- [[Trace]]
- [[Observability]]
- [[Tool Registry]]

## 学习时先看

1. 先看 [[Oh My Codex (OMX)]]，理解它是什么、不是什么。
2. 再看 [[oh-my-codex 使用教程]]，照着跑安装和 smoke test。
3. 最后看 team/worktree 部分，理解并行 Agent 为什么需要隔离工作区。

## 边界提醒

OMX 的关键价值是编排和运行时纪律，不是让底层模型本身更聪明。

`--madmax` / `--yolo` 这类强权限模式适合受控开发环境，不适合未知仓库、生产凭据、不可逆操作或你还没理解风险的时候直接使用。

## 本地 hook / 可观测性补充

本仓库当前环境里，`~/.codex/hooks.json` 把 `SessionStart`、`UserPromptSubmit`、`PreToolUse`、`PostToolUse`、`PreCompact`、`PostCompact`、`Stop` 等 Codex native hook 事件指向 `oh-my-codex/dist/scripts/codex-native-hook.js`。

`.omx/` 下可以看到 `logs/turns-*.jsonl`、`metrics.json`、`state/session.json`、`state/subagent-tracking.json`、`goals/.../ledger.jsonl` 等 artifact。它们是理解 [[Agent Lifecycle Hook]]、[[Trace]] 和 [[Observability]] 的本地证据，但不是上游 Codex/OpenAI 的通用规范。
