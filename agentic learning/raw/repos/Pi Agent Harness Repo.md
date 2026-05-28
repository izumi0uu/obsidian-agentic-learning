---
type: source
source_type: repo
title: earendil-works/pi
url: https://github.com/earendil-works/pi
author: earendil-works
site: github.com
topic:
  - agent
  - coding-agent
  - workflow
  - frontier
created: 2026-05-28
updated: 2026-05-28
last_checked: 2026-05-28
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Agent Harness]]"
  - "[[Coding Agent]]"
  - "[[Agent Framework]]"
  - "[[Managed Agent Harness]]"
  - "[[Oh My Codex Repo]]"
  - "[[Claude Code CLI Repo]]"
---

# Pi Agent Harness Repo

## 为什么收

Pi 是一个很适合放进这座 vault 的 coding-agent repo source，因为它把 “Agent Harness 不一定要做成厚重编排平台” 这条边界说得很明确。它把自己定位成 minimal terminal coding harness：默认给模型 `read`、`write`、`edit`、`bash` 这四类核心工具，再通过 sessions、prompt templates、skills、extensions、themes 和 SDK / RPC 模式把可扩展性留给使用者。

这份 source 最适合回答三类学习问题：

1. 一个终端 coding harness 的最小闭环需要哪些运行部件？
2. coding agent、agent runtime、unified provider API 和 TUI library 在一个 mono repo 里应该怎么分层？
3. 为什么有些项目会故意不内建 sub-agents / plan mode，而把这些工作流能力留给用户或第三方扩展？

## 主源

- GitHub repo: <https://github.com/earendil-works/pi>
- Docs: <https://pi.dev/docs/latest>
- Root README: <https://raw.githubusercontent.com/earendil-works/pi/main/README.md>
- Coding agent README: <https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/README.md>
- Agent runtime README: <https://raw.githubusercontent.com/earendil-works/pi/main/packages/agent/README.md>
- Unified AI API README: <https://raw.githubusercontent.com/earendil-works/pi/main/packages/ai/README.md>
- Providers docs: <https://raw.githubusercontent.com/earendil-works/pi/main/packages/coding-agent/docs/providers.md>
- Latest release checked on 2026-05-28: GitHub release `v0.76.0`, published 2026-05-27.
- npm latest check on 2026-05-28: `@earendil-works/pi-coding-agent` version `0.76.0`.

## 一句话

Pi 是一个把 interactive coding CLI、agent runtime 和 unified multi-provider LLM API 放在同一 mono repo 里的 minimal terminal coding harness，不是一个新的通用 Agent 理论概念。

## 关键事实

- Root README 把这个仓库定义为 `Pi Agent Harness Mono Repo`，并把用户最直接接触到的产物定位成 `@earendil-works/pi-coding-agent` interactive coding agent CLI。
- `packages/coding-agent/README.md` 把 Pi 描述成 minimal terminal coding harness，强调 “adapt pi to your workflows” 而不是反过来适应平台预设。
- Coding agent README 明确说 Pi 默认跳过 sub agents 和 plan mode；这些不是它的概念前提，而是留给用户通过 extensions、skills、prompt templates、themes 和 pi packages 自己补的工作流能力。
- 默认工具集合是 `read`、`write`、`edit`、`bash`。这说明 Pi 的最小产品假设是 “让模型能在本地代码工作区里读、写、改、跑”，而不是先内建复杂多 Agent 编排。
- Pi 同时提供 interactive mode、print / JSON mode、RPC mode 和 SDK embedding，这说明它既是面向终端用户的 CLI，也尝试做可嵌入的 harness substrate。
- `@earendil-works/pi-agent-core` 的 package / README 把核心层定义为带 tool execution、event streaming、state management、context transform、beforeToolCall / afterToolCall hooks 的通用 agent runtime。
- `@earendil-works/pi-ai` 的 package / README 把底层模型接入层定义为 unified LLM API，只收录支持 tool calling 的模型，并负责 provider/model discovery、context persistence、handoff、token/cost tracking。
- Providers 文档显示 Pi 同时支持 OAuth subscription 和 API key provider，并且内置一组 tool-capable models。这进一步说明它偏向 “让 coding harness 站在多 provider 之上”，而不是绑定单一模型厂商。

## 可以拆成概念卡 / topic

- [[Agent Harness]]
- [[Coding Agent]]
- [[Agent Framework]]
- [[Managed Agent Harness]]

暂不创建稳定 `[[Pi]]` 或 `[[Pi Agent]]` 概念卡。原因：当前学习价值主要来自它作为具体 repo / harness 样本展示的工程边界，而不是作为一个跨来源复用的通用概念。

## 学习时先看

1. 先读 root README，确认 mono repo 分层和项目定位。
2. 再读 `packages/coding-agent/README.md`，理解默认工具、sessions、commands、provider support 和 extensibility philosophy。
3. 然后读 `packages/agent/README.md`，拆 event flow、tool execution mode、hooks、state management 和 message flow。
4. 最后读 `packages/ai/README.md` 与 `docs/providers.md`，看多 provider abstraction、tool-capable model gating 和 auth / provider boundary。

## 边界提醒

Pi 不是一个新的 Agent 方法论，也不是 “Pi agent” 这四个字本身就成立的稳定概念卡。更准确的学习位置是：它是一个具体的 coding-agent / harness repo source。

Pi 也不是 [[Managed Agent Harness]]。它主要假设的是本地或开发者控制的终端 / SDK 使用面，而不是平台托管的 session + environment + events 基础设施。

Pi 和 [[Agent Framework]] 有交叉，但不应简单等号。它的 repo 同时含有 runtime library 与 API abstraction，可被开发者嵌入；但用户最直接面对的是 coding harness CLI，而不是纯粹的 workflow framework 选型对象。

Pi 不把 sub-agents / plan mode 当默认能力，这一点很重要。它提醒我们：这些是某些 harness 的产品选择，不是 “只要是 coding agent 就必须具备” 的定义条件。

## 证据锚点候选

- `README.md`：mono repo 定位、包结构、share sessions、development / supply-chain hardening。
- `packages/coding-agent/README.md`：minimal terminal coding harness、自定义 philosophy、默认工具、interactive / JSON / RPC / SDK 模式、sessions、skills、extensions、pi packages。
- `packages/coding-agent/package.json`：`pi` CLI、默认 config dir、`read/write/edit/bash` 描述、依赖分层。
- `packages/agent/README.md`：stateful agent、tool execution、event streaming、hooks、parallel/sequential tool execution。
- `packages/ai/README.md`：tool-capable model gate、multi-provider abstraction、context persistence、handoff、token/cost tracking。
- `packages/coding-agent/docs/providers.md`：OAuth subscriptions、API key providers、auth file 与 provider resolution order。
- GitHub release `v0.76.0` 与 npm version `0.76.0`：说明该项目仍在快速迭代，应视为 `volatile` source。

## 我的疑问

- Pi 故意保持 “minimal harness” 后，哪些长期任务能力最适合通过扩展补齐，哪些反而应该保持在 core runtime？
- Pi 的 SDK / RPC / CLI 三种承载方式里，哪一种最能代表它对外的稳定学习价值？
- 如果要把 Pi 放进 coding-agent 选型对比，它与 [[Claude Code CLI Repo]]、[[Oh My Codex Repo]] 这类项目最关键的比较维度应该是 runtime thickness、workflow opinionation、provider abstraction，还是 extensibility model？
