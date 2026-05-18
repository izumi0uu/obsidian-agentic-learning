---
type: source
source_type: repo
title: NousResearch/hermes-agent
url: https://github.com/NousResearch/hermes-agent
author: Nous Research
site: github.com
topic:
  - agent
  - coding-agent
  - memory
  - workflow
  - frontier
created: 2026-05-11
updated: 2026-05-18
last_checked: 2026-05-11
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Hermes Agent]]"
  - "[[Agent Harness]]"
  - "[[Coding Agent]]"
  - "[[Long-term Memory]]"
  - "[[Tool Calling]]"
  - "[[MCP]]"
  - "[[Durable Execution]]"
  - "[[Progressive Disclosure]]"
---

# Hermes Agent Repo

## 为什么收

Hermes Agent 是 Nous Research 维护的开源 Agent 项目。它适合放进这个 vault 的原因，不是因为它重新定义了 Agent，而是因为它把很多现代 Agent harness 能力放在一个具体实现里：CLI / messaging gateway / API server / ACP 入口、tool registry、MCP、memory、skills、cron、delegation、terminal backends、security approval、session persistence 和 `/goal` 式持续执行。

这是一份前沿工程项目 source，主要用来观察“一个个人/云端 AI Agent 产品把记忆、工具、消息平台、技能和长期任务组织到一起时，边界长什么样”。

## 主源

- GitHub repo: <https://github.com/NousResearch/hermes-agent>
- 官方文档: <https://hermes-agent.nousresearch.com/docs/>
- Architecture docs: <https://hermes-agent.nousresearch.com/docs/developer-guide/architecture>
- Memory docs: <https://hermes-agent.nousresearch.com/docs/user-guide/features/memory>
- Skills docs: <https://hermes-agent.nousresearch.com/docs/user-guide/features/skills>
- Security docs: <https://hermes-agent.nousresearch.com/docs/user-guide/security>
- Persistent Goals docs: <https://hermes-agent.nousresearch.com/docs/user-guide/features/goals>
- MCP docs: <https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp>
- Latest release checked on 2026-05-11: GitHub API reported `v2026.5.7`, named `Hermes Agent v0.13.0 (2026.5.7)`.

## 一句话

Hermes Agent 是一个以 Nous Research 生态为中心的 self-improving / tool-using AI agent runtime：它把模型、工具、终端环境、消息网关、记忆、skills、MCP、调度、delegation 和安全审批整合成一个可运行的 Agent harness。

## 关键事实

- README 把 Hermes Agent 定位为 Nous Research 构建的 self-improving AI agent，并强调内置学习循环、skills、记忆、会话搜索、用户建模、多平台消息入口和任意模型提供商接入。
- Architecture docs 显示它有多个入口：CLI、gateway、ACP、batch runner、API server 和 Python library；核心运行路径进入 `AIAgent`，再经过 prompt builder、provider resolution 和 tool dispatch。
- Architecture docs 把工具系统写成 central tool registry、toolsets、terminal/browser/web/MCP/file/vision 等后端，并把会话状态放在 SQLite + FTS5 session storage。
- Memory docs 把记忆拆成 `MEMORY.md` 和 `USER.md` 两类短记忆，并说明 session search 用 SQLite FTS5 检索历史会话。
- Skills docs 把 skill 定义为按需加载的知识文档，使用 progressive disclosure，兼容 agentskills.io open standard。
- Security docs 把安全模型拆成用户授权、危险命令审批、容器隔离、MCP credential filtering、context file scanning、cross-session isolation 和 input sanitization。
- `/goal` docs 把 persistent goals 描述为一个跨 turn 保持目标的 Ralph loop：每轮后由轻量 judge 判断是否继续，直到完成、暂停、清除或预算耗尽。
- 2026-05-07 v0.13.0 release 突出 durable multi-agent Kanban、`/goal`、checkpoints v2、gateway session auto-resume、安全修复、provider plugins、MCP 改进和 i18n。

## 可拆概念卡

- [[Hermes Agent]]
- [[Agent Harness]]
- [[Long-term Memory]]
- [[Memory Reflection]]
- [[Tool Calling]]
- [[MCP]]
- [[Agent Workflow]]
- [[Durable Execution]]
- [[Multi-agent Orchestration]]
- [[Progressive Disclosure]]

## 学习时先看

1. 先看 README 和官方 docs 首页，理解它的项目定位。
2. 再看 Architecture docs，拆入口、agent loop、provider、tool registry、session storage、gateway 和 backends。
3. 然后看 Memory、Skills、MCP、Security 和 Persistent Goals，这些最能对应本 vault 里的 Agent 工程概念。
4. 最后看 release notes，只把版本变化写入前沿追踪，不把某个 release 的能力误当成稳定概念定义。

## 边界提醒

Hermes Agent 是具体项目，不是 Agent 概念本身，也不是通用行业标准。它的稳定学习价值在于观察现代 Agent harness 的组成方式；具体命令、平台适配、模型列表、release 功能和安全策略属于易变层。

不要把 README 里的能力描述直接当成生产可靠性结论。真正评估它要看任务类型、权限边界、工具调用日志、sandbox、approval、测试覆盖、失败恢复和人工接管设计。

## 证据锚点候选

- `README.md`：项目定位、模型提供商、多平台 gateway、skills、memory、terminal backends、research-ready。
- `website/docs/developer-guide/architecture.md`：entry points、AIAgent、tool registry、session storage、gateway、terminal/browser/web/MCP backends。
- `website/docs/user-guide/features/memory.md`：`MEMORY.md` / `USER.md`、frozen snapshot、session search、external memory providers。
- `website/docs/user-guide/features/skills.md`：progressive disclosure、`~/.hermes/skills/`、skill slash commands、agentskills.io 兼容。
- `website/docs/user-guide/security.md`：seven-layer security model、approval modes、hardline blocklist、gateway authorization。
- `website/docs/user-guide/features/goals.md`：persistent goal、judge loop、turn budget、persistence、Codex `/goal` attribution。
- GitHub latest release API: `v2026.5.7` / v0.13.0, checked 2026-05-11。

## 我的疑问

- Hermes Agent 的 self-improving skill loop 在真实长期任务中如何评估质量，而不是只积累越来越多的技能文档？
- 它的 memory / session search / external memory provider 之间，哪些进入 system prompt，哪些只在需要时检索？
- 多平台 gateway 带来的权限边界，和 CLI 本地 agent 的权限边界，有哪些本质差异？
