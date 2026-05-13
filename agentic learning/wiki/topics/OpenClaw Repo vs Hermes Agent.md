---
type: map
topic:
  - agent
  - coding-agent
  - gateway
  - memory
  - security
  - comparison
  - frontier
status: active
created: 2026-05-13
updated: 2026-05-13
last_checked: 2026-05-13
freshness: volatile
source:
  - "[[OpenClaw Repo]]"
  - "[[Hermes Agent Repo]]"
  - "[[Hermes Agent]]"
evidence:
  - "[[OpenClaw Repo#关键事实]]"
  - "[[OpenClaw Repo#证据锚点候选]]"
  - "[[Hermes Agent Repo#关键事实]]"
  - "[[Hermes Agent#边界细节]]"
  - "[[Hermes Agent#现代性状态]]"
related:
  - "[[Agent Harness]]"
  - "[[Coding Agent]]"
  - "[[Agent Control Plane]]"
  - "[[Long-term Memory]]"
  - "[[Tool Permissioning]]"
  - "[[Sandbox Workspace]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Durable Execution]]"
  - "[[Coding Agent 执行边界对比]]"
---

# OpenClaw Repo vs Hermes Agent

## 一句话总览

[[OpenClaw Repo]] 和 [[Hermes Agent]] 都是 volatile 的具体 Agent harness / personal assistant runtime 样本，但观察重点不同：OpenClaw 更像“本地优先 Gateway + 多渠道入口 + workspace / memory / skills / sandbox / node control plane”；Hermes Agent 更像“self-improving tool-using agent runtime + skills / memory / MCP / delegation / `/goal` long-task loop”。

最小边界：两者都不是 Agent 通用定义，也不是稳定行业标准。它们的共同学习价值是把 [[Agent Harness]]、[[Tool Permissioning]]、[[Long-term Memory]]、[[Sandbox Workspace]]、gateway、sessions、skills 和 long-running tasks 放进真实项目里观察；差异在于 OpenClaw 更强调消息/设备/Gateway 控制面，Hermes 更强调 agent runtime 自改进、MCP/tools 和持续目标循环。

## 为什么这组值得对比

- 混淆风险高：两者都被描述成“能长期运行、能接消息、能用工具、能记忆的 Agent”，容易被误读成同一类产品。
- 共同问题域清楚：它们都试图把聊天模型变成一个能跨会话、跨工具、跨入口运行的 personal / coding agent harness。
- 介入点不同：OpenClaw 首先从 Gateway、channels、nodes、workspace 和安全配置切入；Hermes 首先从 `AIAgent` runtime、skills、memory、MCP、security approval 和 `/goal` 切入。
- 证据密度足够：OpenClaw 有官方 repo/docs source note；Hermes 已有 repo source note 和 volatile 项目卡。
- 复习价值高：这组对比可以训练“产品功能看起来都很 Agent，但工程责任层不同”的判断力。

边界：这页不是二者优劣排名、star 数统计、安装教程或安全审计。它只沉淀学习边界；具体版本、CLI、配置字段和安全默认值都需要按官方文档复查。

## 共同问题域

共同问题是：一个真正可用的个人/代码 Agent 不能只靠模型多轮对话。它需要入口、身份、状态、工具、记忆、权限、隔离、任务记录和停止条件。

```text
user/channel/CLI
  -> gateway or runtime entrypoint
  -> session/workspace/context/memory
  -> model decides/tool call/workflow
  -> tool execution with permission/sandbox
  -> logs/tasks/trace/session history
  -> memory or skills reuse
  -> continue, ask, stop, or hand off
```

OpenClaw 和 Hermes 都在这条链路上做工程包装；不同的是，OpenClaw 把“入口和控制面”放得更前，Hermes 把“agent 自身如何持续执行和积累经验”放得更前。

## 核心区别表

| 维度 | [[OpenClaw Repo]] | [[Hermes Agent]] | 学习刀口 |
|---|---|---|---|
| 首要定位 | 运行在自己设备上的 personal AI assistant / local-first Gateway | Nous Research 的 self-improving tool-using AI agent runtime | OpenClaw 看入口/控制面；Hermes 看 runtime/经验复用 |
| 主入口 | Gateway、CLI、macOS/web/admin clients、nodes、多消息渠道 | CLI、gateway、ACP、batch runner、API server、Python library | 两者都有多入口，但 OpenClaw 的 channel/node 叙事更强 |
| Gateway 角色 | 单个长驻 Gateway 拥有 messaging surfaces，并通过 WS 管理 clients/nodes | messaging gateway 是入口之一，服务 agent runtime | OpenClaw 更像 Gateway-first；Hermes 更像 Agent-runtime-first |
| Workspace / context | `AGENTS.md`、`SOUL.md`、`TOOLS.md`、`USER.md`、`MEMORY.md` 等 bootstrap files 注入上下文 | memory files、skills、session search 进入 prompt / tool dispatch | 两者都把文件系统当 agent context，但文件分层不同 |
| Memory | Plain Markdown memory：`MEMORY.md`、daily notes、memory search、memory wiki、dreaming | `MEMORY.md` / `USER.md`、SQLite FTS5 session search、external memory providers | OpenClaw 更像可审计 wiki/memory 文件层；Hermes 更强调 session search + memory injection |
| Skills / plugins | AgentSkills-compatible skill folders，多层 precedence、per-agent allowlist、ClawHub | skills 是按需加载知识文档，支持创建/更新技能，兼容 agentskills.io | 都用 skills，但风险都是把错误流程长期固化 |
| Tools / MCP | README 和 docs 关注 first-class tools、browser/canvas/nodes/cron/sessions/Discord/Slack actions；MCP 不是唯一核心叙事 | central tool registry、terminal/browser/web/MCP/file/vision backends | Hermes 更适合看 MCP/tool registry；OpenClaw 更适合看 channels/nodes/tool policy |
| Security model | 明确 personal assistant trust model，不是 hostile multi-tenant boundary；有 security audit、pairing、allowlists、sandboxing | approval、sandbox、credential filtering、context scanning、cross-session isolation 等 | OpenClaw 的安全文档更直接训练“单用户 trust boundary” |
| Sandboxing | 可选 sandbox，工具执行进 docker / ssh / openshell；Gateway 留在 host；workspace 本身不是硬 sandbox | 有 container isolation / approval / backends 等安全层 | 二者都不能被理解成自动安全；配置和 trust boundary 决定风险 |
| Multi-agent | 一个 Gateway 可托管多个 isolated agents，各自 workspace、agentDir、auth profiles、sessions，再由 bindings 路由 | durable multi-agent Kanban、delegation、subagent / goal 方向 | OpenClaw 更偏多 persona / 多账号路由；Hermes 更偏任务执行协作 |
| Long-running tasks | background tasks 记录 ACP/subagent/cron/CLI operations；cron / heartbeat / tasks 分工明确 | `/goal` 持续循环、judge loop、durable Kanban、checkpoints | OpenClaw 适合看任务记录和推送；Hermes 适合看持续目标验收 |
| Clawbot 边界 | `clawbot` 是 legacy alias namespace，现代入口是 `openclaw` top-level commands | 不适用 | 不要创建稳定 `[[Claw Bot]]` 概念卡 |

## 最容易混淆的边界

### OpenClaw vs Hermes：都是 Agent Harness，但不是同一个抽象中心

[[Agent Harness]] 是抽象运行外壳；OpenClaw 和 Hermes 都是具体实现。OpenClaw 的抽象中心更靠近 Gateway / channel / node / workspace / security config；Hermes 的抽象中心更靠近 `AIAgent` / tool registry / memory / skills / MCP / `/goal`。因此“它们都能接消息和跑工具”不能说明它们同层。

### Gateway-first vs Runtime-first

OpenClaw 的官方架构先讲 Gateway 拥有消息 surface、clients/nodes 通过 WebSocket 接入、pairing 和 remote access 等控制面问题。Hermes 的 source note 先讲 `AIAgent`、prompt builder、provider resolution、tool dispatch、session storage 和 toolsets。最小刀口：OpenClaw 先问“谁能从哪里叫醒 agent，进入哪个 agent/workspace”；Hermes 先问“agent 如何执行、记忆、调用工具和持续完成目标”。

### Memory file vs Memory capability

OpenClaw 强调 memory 写在 plain Markdown 文件里，并且可通过 memory search / memory wiki / dreaming 扩展；Hermes 强调 `MEMORY.md` / `USER.md`、session search 和 skills。两者都不是模型权重更新。它们都属于外部记忆 / procedural reuse，而不是 LLM 内部能力。

### Skills 不等于安全能力

两者都有 skills，并且都可能把可复用流程变成长期能力。但 skill 更像“按需加载的操作知识”，不是权限控制。真正的风险边界要看 allowlist、sandbox、approval、audit、credential filtering、context visibility 和 human review。

### Multi-agent 不等于多租户安全

OpenClaw 的 multi-agent routing 可以隔离 workspace、state directory、auth profiles 和 sessions，但官方安全文档仍强调它不是 hostile multi-tenant boundary。Hermes 的 delegation / multi-agent Kanban 也不自动保证隔离。看到“multi-agent”时要先问：是协作编排，还是安全隔离？

## 执行时序 / 机制差异

### OpenClaw 典型路径

```text
1. 用户从 Telegram / Slack / WhatsApp / iMessage / WebChat 等入口发消息。
2. Gateway 处理 channel auth、pairing、allowlist、session routing。
3. Binding 选择 agent / workspace / session。
4. Embedded runtime 组装 bootstrap files、memory、skills、tools。
5. 模型产生 action，tool policy / sandbox 决定如何执行。
6. Gateway 记录 events / tasks / sessions，并把结果发回 channel 或等待后续 heartbeat。
```

### Hermes Agent 典型路径

```text
1. 用户从 CLI / gateway / ACP / API / messaging 入口发起任务。
2. AIAgent 组装 prompt、memory、skills 和 provider。
3. 模型通过 tool registry 调用 terminal/browser/web/MCP/file/vision 等工具。
4. Security approval / sandbox / credential filtering 约束副作用。
5. Session storage / memory / skills 保存可复用经验。
6. /goal 或 Kanban 让长任务跨 turn 继续推进，直到 judge / budget / human 停止。
```

这两个路径都是工程综合：它们来自对应 source note 和官方 docs 的结构化理解，不是某个单一文档给出的统一标准。

## 现代系统如何吸收或限制

### 来源支持的稳定部分

- [[OpenClaw Repo]] 支持：现代 personal assistant agent 需要 Gateway、channel routing、workspace/context files、memory、skills、task ledger、security audit 和 sandbox 这些外部 runtime 责任。
- [[Hermes Agent Repo]] 支持：现代 agent runtime 可以把 tool registry、MCP、memory、skills、session search、approval、delegation 和 persistent goals 组合起来。
- [[Hermes Agent]] 支持：这类项目的 self-improving 更接近 memory / skills / workflow reuse，而不是模型训练。

### 工程综合 / inference

OpenClaw 和 Hermes 都说明一个共同趋势：Agent 产品的竞争点不只是“模型调用”，而是 agent 周边系统。真正让 Agent 可用的是：入口治理、上下文组织、工具边界、长期记忆、任务追踪、安全审计、sandbox 和恢复/停止机制。

### 仍需警惕的外推

不要把任一项目的配置项当成长期概念边界。OpenClaw 的 channels、nodes、skills、memory backend、sandbox backend 和 CLI；Hermes 的 provider、MCP、skills、security approval、goal judge 和 Kanban 都会随 release 改动。学习时应保留 project-level `freshness: volatile`。

## 什么时候用哪个判断

| 学习问题 | 优先看 | 为什么 | 风险 |
|---|---|---|---|
| 多渠道消息如何进入同一个 Agent 系统 | [[OpenClaw Repo]] | Gateway / channel / node / binding 是主线 | 容易忽略 DM / group / shared inbox 的授权风险 |
| personal assistant 的 trust boundary 怎么画 | [[OpenClaw Repo]] | 官方 security docs 明确 single trusted operator model | 不要把它误当 hostile multi-tenant 隔离 |
| Agent 如何用 skills / memory 形成经验复用 | 两者都看 | OpenClaw 看 Markdown memory / memory wiki；Hermes 看 skills + session search | 经验复用可能固化错误 |
| MCP / tool registry / terminal/browser tools 如何组合 | [[Hermes Agent]] | Hermes source note 的 tool registry / MCP 证据更集中 | 工具多不等于权限治理好 |
| 长任务如何持续推进和验收 | [[Hermes Agent]] | `/goal`、judge loop、Kanban、checkpoints 是主线 | “会继续做”不等于“会正确停” |
| 多 persona / 多账号消息路由如何隔离 | [[OpenClaw Repo]] | multi-agent routing 强调 workspace、agentDir、session/auth profile boundary | routing key 不是强安全边界 |
| 比较 coding-agent 执行风险 | [[Coding Agent 执行边界对比]] + 本页 | OpenClaw/Hermes 是具体样本；执行边界页给通用框架 | 不要用产品 README 替代验证和审计 |

## 它们共同不是什么

- 都不是 [[Agent]] 的通用定义；它们只是具体项目。
- 都不是模型训练方法；memory、skills、session search 和 goals 都属于外部 runtime / harness 能力。
- 都不是自动安全保证；sandbox、approval、allowlist、audit 和 trust boundary 配置才决定风险。
- 都不是完整生产可靠性证明；没有本地安装、任务评测、代码审计和安全测试时，只能作为 source-level 学习样本。
- 都不应被 star 数、README 热词或 release 亮点直接包装成稳定概念。

## 证据锚点

- OpenClaw source: [[OpenClaw Repo#关键事实]], [[OpenClaw Repo#证据锚点候选]]
- Hermes source: [[Hermes Agent Repo#关键事实]], [[Hermes Agent Repo#证据锚点候选]]
- Hermes concept: [[Hermes Agent#边界细节]], [[Hermes Agent#现代性状态]]
- Related boundaries: [[Agent Harness#证据锚点]], [[Tool Permissioning#证据锚点]], [[Long-term Memory#证据锚点]], [[Sandbox Workspace#证据锚点]], [[Coding Agent 执行边界对比#证据锚点]]
- Evidence type: official repo/docs source notes + existing concept-card synthesis + engineering comparison.
- Confidence: medium-high for documented positioning and architecture; medium for comparative evaluation because neither project has been locally installed or benchmarked in this vault.
- Boundary: 本页不声称 OpenClaw 或 Hermes 在真实任务完成率、安全性、成本或生产可靠性上优于对方；这些需要单独实验。

## 复习触发

1. 为什么 `clawbot` 不应该被单独建成稳定概念卡？
2. OpenClaw 的 Gateway-first 路线和 Hermes 的 runtime-first 路线，在安全风险上分别最容易出问题的地方是什么？
3. 如果一个项目有 memory 和 skills，为什么仍不能说它在“训练自己”？
4. 多 agent routing、delegation、多租户隔离这三个词的边界怎么切？
5. 你想做一个个人 coding assistant 时，哪些需求更像 OpenClaw，哪些更像 Hermes？

## 相关链接

- [[OpenClaw Repo]]
- [[Hermes Agent]]
- [[Hermes Agent Repo]]
- [[Agent Harness]]
- [[Coding Agent]]
- [[Agent Control Plane]]
- [[Long-term Memory]]
- [[Tool Permissioning]]
- [[Sandbox Workspace]]
- [[Code Execution Sandbox]]
- [[Multi-agent Orchestration]]
- [[Durable Execution]]
- [[Coding Agent 执行边界对比]]
