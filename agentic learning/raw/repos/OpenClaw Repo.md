---
type: source
source_type: repo
title: openclaw/openclaw
url: https://github.com/openclaw/openclaw
author: OpenClaw
site: github.com
topic:
  - agent
  - coding-agent
  - gateway
  - memory
  - workflow
  - frontier
created: 2026-05-13
updated: 2026-05-13
last_checked: 2026-05-13
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[OpenClaw Repo vs Hermes Agent]]"
  - "[[Agent Harness]]"
  - "[[Coding Agent]]"
  - "[[Agent Control Plane]]"
  - "[[Tool Permissioning]]"
  - "[[Long-term Memory]]"
  - "[[Sandbox Workspace]]"
---

# OpenClaw Repo

## 为什么收

OpenClaw 是一个快速演进的开源 personal AI assistant / Agent gateway 项目。它值得放进这个 vault，不是因为它重新定义了 [[Agent]]，而是因为它把很多现代 Agent harness 能力集中在一个具体产品形态里：本地优先 Gateway、多渠道消息入口、嵌入式 Agent runtime、workspace/bootstrap files、skills、memory、sandbox、security audit、multi-agent routing、background tasks 和 companion apps。

这份 source 最适合回答两个学习问题：

1. 一个“随时能从 Telegram / Slack / WhatsApp / iMessage 等渠道被叫醒”的个人 Agent，需要哪些控制面和安全边界？
2. OpenClaw 和 [[Hermes Agent]] 这类项目同样都像 Agent harness，它们的差异究竟在 gateway、runtime、memory、skills、安全还是长期任务上？

## 主源

- GitHub repo: <https://github.com/openclaw/openclaw>
- Docs: <https://docs.openclaw.ai>
- README raw: <https://raw.githubusercontent.com/openclaw/openclaw/main/README.md>
- Gateway architecture: <https://docs.openclaw.ai/concepts/architecture>
- Agent runtime: <https://docs.openclaw.ai/concepts/agent>
- Agent workspace: <https://docs.openclaw.ai/concepts/agent-workspace>
- Memory overview: <https://docs.openclaw.ai/concepts/memory>
- Skills: <https://docs.openclaw.ai/tools/skills>
- Multi-agent routing: <https://docs.openclaw.ai/concepts/multi-agent>
- Background tasks: <https://docs.openclaw.ai/automation/tasks>
- Security: <https://docs.openclaw.ai/gateway/security>
- Sandboxing: <https://docs.openclaw.ai/gateway/sandboxing>
- Clawbot legacy alias: <https://docs.openclaw.ai/cli/clawbot>
- Latest release checked on 2026-05-13: GitHub API reported `v2026.5.7`, named `openclaw 2026.5.7`, published 2026-05-07.

## 一句话

OpenClaw 是一个本地优先的 personal AI assistant / Agent gateway：它把多渠道消息、Gateway 控制面、嵌入式 Agent runtime、workspace、skills、memory、tools、sandbox 和安全审计组合成一个可以长期运行的个人 Agent 系统。

## 关键事实

- README 将 OpenClaw 定位为运行在自己设备上的 personal AI assistant，并强调 Gateway 只是控制面，产品本体是 assistant。
- README 列出大量消息渠道和设备入口，包括 WhatsApp、Telegram、Slack、Discord、Google Chat、Signal、iMessage、Matrix、Teams、Feishu、LINE、WeChat、QQ、WebChat，以及 macOS / iOS / Android nodes。
- Gateway architecture 文档显示：单个长驻 Gateway 拥有消息 surface，CLI / macOS app / web UI / automations 通过 WebSocket 连到 Gateway；nodes 也通过 WebSocket 以 `role: node` 接入并声明能力。
- Agent runtime 文档显示：OpenClaw 运行一个 embedded agent runtime，每个 Gateway 有 agent process、workspace、bootstrap files 和 session store；session transcript 存在 `~/.openclaw/agents/<agentId>/sessions/`。
- Workspace 文档把 `AGENTS.md`、`SOUL.md`、`TOOLS.md`、`IDENTITY.md`、`USER.md`、`MEMORY.md` 和 `memory/YYYY-MM-DD.md` 等文件作为 agent context / memory 的组成部分，同时提醒 workspace 是默认 cwd，不是硬 sandbox。
- Memory 文档强调记忆写在 plain Markdown 文件里：`MEMORY.md` 是长期记忆，`memory/YYYY-MM-DD.md` 是日记忆，`DREAMS.md` 可用于 consolidation review；memory search / memory wiki 属于可插拔能力。
- Skills 文档显示 OpenClaw 使用 AgentSkills-compatible skill folders，支持 workspace、project-agent、personal-agent、managed/local、bundled、extra dirs 多层加载和 per-agent allowlist。
- Multi-agent routing 文档显示：OpenClaw 可以在一个 Gateway 里托管多个隔离 agent，每个 agent 有独立 workspace、agentDir、auth profiles 和 session store，再通过 bindings 把 channel/account/peer 路由到对应 agent。
- Security 文档明确其安全假设是 personal assistant / single trusted operator boundary，不是 hostile multi-tenant boundary；多用户或对抗性用户需要拆 gateway、credentials、OS user 或 host。
- Sandboxing 文档显示：sandbox 可选，用于限制 tool execution 和可选 browser；Gateway 留在 host 上，tools 在 docker / ssh / openshell backend 中执行；sandbox off 时 tools 在 host 上运行。
- Clawbot 文档显示 `openclaw clawbot` 只是 legacy alias namespace，目前支持的别名主要是 `openclaw clawbot qr`，迁移建议是使用现代 top-level commands。
- 2026-05-07 release notes 体现了项目易变性：plugin publishing、channels CLI、active memory、gateway sessions、auto-reply authorization hooks、Tavily credentials、agent context cache、compaction 等仍在快速修复和调整。

## 可以拆成概念卡 / topic

- [[OpenClaw Repo vs Hermes Agent]]
- [[Agent Harness]]
- [[Agent Control Plane]]
- [[Coding Agent]]
- [[Long-term Memory]]
- [[Sandbox Workspace]]
- [[Tool Permissioning]]
- [[Agent Lifecycle Hook]]

暂不创建稳定 `[[OpenClaw]]` 概念卡。原因：OpenClaw 当前更像 volatile 项目 / 产品 source，学习价值在于观察具体 harness 组合和边界；如果后续多次复用，再考虑创建项目卡。

## 学习时先看

1. README：先理解 OpenClaw 的产品定位、渠道入口、安装方式和安全默认值。
2. Gateway architecture：拆 Gateway、clients、nodes、WebSocket protocol、pairing 和 remote access。
3. Agent runtime / Agent workspace：看 agent process、workspace、bootstrap files、sessions 和工具上下文如何被组织。
4. Memory / Skills / Multi-agent routing：看 OpenClaw 如何把长期记忆、skill library 和多 persona / 多账号路由变成 runtime 能力。
5. Security / Sandboxing：确认它的 trust model、sandbox 限制、工具权限和 shared inbox 风险，不要只看功能亮点。
6. Release notes：只把版本变化写入前沿追踪，不把某个 release 的 CLI/API 细节当成稳定概念定义。

## 边界提醒

OpenClaw 不是 Agent 的通用定义，也不是多租户安全边界。它是一个具体的 personal assistant / gateway / harness 项目。稳定学习价值是观察“多渠道入口 + 本地 Gateway + agent runtime + workspace memory + tools + sandbox/security”如何组合；易变层是 CLI 命令、配置字段、渠道适配、插件/skills 机制、memory 后端、security audit 项目和 release behavior。

“Claw Bot”不应单独录成概念卡。官方文档里 `clawbot` 是 legacy alias namespace；学习时应按 OpenClaw / OpenClaw Repo 处理。

## 证据锚点候选

- `README.md`：项目定位、personal assistant、渠道列表、local-first Gateway、security defaults、sandbox model、operator quick refs。
- `docs.openclaw.ai/concepts/architecture`：Gateway daemon、clients、nodes、WS protocol、pairing、remote access、invariants。
- `docs.openclaw.ai/concepts/agent`：embedded agent runtime、workspace、bootstrap files、built-in tools、skills、runtime boundaries、sessions。
- `docs.openclaw.ai/concepts/agent-workspace`：workspace as agent home、bootstrap file map、workspace is not hard sandbox。
- `docs.openclaw.ai/concepts/memory`：plain Markdown memory、`MEMORY.md`、daily notes、memory search、memory wiki、dreaming。
- `docs.openclaw.ai/tools/skills`：AgentSkills-compatible folders、load precedence、per-agent allowlists、ClawHub、安全提醒。
- `docs.openclaw.ai/concepts/multi-agent`：isolated agents、workspace/state/session/auth profile boundaries、bindings。
- `docs.openclaw.ai/automation/tasks`：background task ledger、ACP/subagent/cron/CLI task records、terminal statuses。
- `docs.openclaw.ai/gateway/security`：personal assistant trust model、gateway/node trust、shared inbox risk、audit checks。
- `docs.openclaw.ai/gateway/sandboxing`：sandbox modes、scope、backend、what is and is not sandboxed。
- `docs.openclaw.ai/cli/clawbot`：`clawbot` legacy alias boundary。
- GitHub latest release API: `v2026.5.7`, checked 2026-05-13。

## 我的疑问

- OpenClaw 的 Gateway + node trust model 在家庭/团队共享场景里，最小可接受隔离边界应该怎么画？
- OpenClaw 的 Markdown memory / memory wiki / dreaming 和 [[Hermes Agent]] 的 memory + session search + skills 相比，哪一层更适合作为“可审计长期记忆”样本？
- 当 OpenClaw 把多渠道消息、tools、skills、background tasks 和 sandbox 放在同一个 personal assistant 产品里时，最容易被用户误解的安全边界是什么？
