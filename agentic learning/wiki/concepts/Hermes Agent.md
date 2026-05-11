---
type: concept
topic:
  - agent
  - coding-agent
  - memory
  - workflow
  - frontier
status: seed
created: 2026-05-11
updated: 2026-05-11
last_checked: 2026-05-11
freshness: volatile
conflicts: []
source:
  - "[[Hermes Agent Repo]]"
evidence:
  - "[[Hermes Agent Repo#为什么收]]"
  - "[[Hermes Agent Repo#关键事实]]"
  - "[[Hermes Agent Repo#证据锚点候选]]"
related:
  - "[[Agent Harness]]"
  - "[[Coding Agent]]"
  - "[[Agent Workflow]]"
  - "[[Long-term Memory]]"
  - "[[Tool Calling]]"
  - "[[MCP]]"
  - "[[Durable Execution]]"
  - "[[Multi-agent Orchestration]]"
---

# Hermes Agent

## 深度级别

- 级别：volatile
- 为什么是这个级别：Hermes Agent 是快速演进的具体开源项目 / 产品化 Agent runtime，release、平台适配、模型 provider、skills、security 策略和 `/goal` 实现都会变。
- 本次缺口：只完成 source-level 录入和概念边界卡；还没有本地安装、跑任务或做代码级审计。

## 一句话

Hermes Agent 是 Nous Research 的开源 self-improving AI agent runtime，把模型调用、工具执行、记忆、skills、消息平台、MCP、调度、delegation、安全审批和长期目标循环组织成一个具体的 [[Agent Harness]]。

## 概念详解

Hermes Agent 出现的背景，是单纯的聊天式 LLM 不能自然完成长期、跨平台、带工具和带记忆的任务。一个用户可能希望同一个 Agent 在 CLI 里改代码，在 Telegram 或 Slack 里接收指令，记住长期偏好，调用外部工具，定时运行任务，必要时分派子 Agent，并且在危险命令前要求确认。Hermes Agent 把这些需求集中到一个 runtime 里，而不是只提供一个 prompt pattern。

从架构上看，它的核心不是“某个更聪明的模型”，而是围绕 `AIAgent` 的执行壳：入口层有 CLI、messaging gateway、ACP、batch runner、API server 和 Python library；中间层有 prompt builder、provider resolution、tool dispatch；工具层有 central tool registry、toolsets、terminal/browser/web/MCP/file/vision 等后端；状态层有 SQLite + FTS5 session storage、记忆文件和 session search。这个组合让 Hermes Agent 更像一个可部署的个人/云端 Agent 系统，而不是一段一次性的 Agent demo。

它的“self-improving”主要体现在两个方向：一是 memory 和 session search 让系统跨会话保留偏好、环境事实和过去对话；二是 skills 系统把可复用流程写成按需加载的知识文档，并允许 agent 创建或更新技能。这里需要小心：这不是模型权重更新，也不是自动保证经验正确。它更接近 [[Long-term Memory]]、[[Memory Reflection]] 和 procedural skill library 这一层的 harness 能力。

2026-05-07 的 v0.13.0 release 把 Hermes Agent 的前沿关注点暴露得很清楚：durable multi-agent Kanban、`/goal` 式跨 turn 持续执行、checkpoints v2、gateway session auto-resume、安全修复、provider plugin、MCP 改进和 i18n。这些说明它正在往“长任务 + 多入口 + 多 Agent + 可恢复 + 可治理”的方向演进。学习它时，最有价值的是拆它的工程边界：哪些能力由模型决定，哪些由 runtime 执行，哪些由安全层阻断，哪些由 trace / state / memory 支撑。

## 它解决什么问题

Hermes Agent 解决的是“LLM 如何变成可运行、可恢复、可接入多平台的个人/工程 Agent”的问题。没有这类 runtime，模型即使会规划，也常卡在真实执行边界：工具怎么注册和调用、终端环境在哪里、跨会话怎么找回上下文、危险动作谁批准、消息平台用户怎么授权、长任务怎么继续、失败后怎么恢复。

它也帮助学习者观察一个具体项目如何把许多分散概念组合起来：[[Tool Calling]] 负责模型发出结构化调用意图，[[MCP]] 负责接入外部工具服务，[[Long-term Memory]] 负责跨会话信息，[[Agent Workflow]] / `/goal` 负责持续推进，[[Agent Harness]] 负责把这些能力装进可执行边界。

## 它不是什么

- 不是 Agent 的通用定义。它是一个具体项目，不能反过来规定所有 Agent 都必须有 Telegram、skills hub、cron 或 gateway。
- 不是模型训练方法。它的 self-improvement 多数发生在 memory、skills、session search 和 workflow 层，不等于修改底层模型权重。
- 不是安全保证。它有 approval、sandbox、allowlist、credential filtering 等机制，但真实风险仍取决于配置、运行环境、工具权限和人类审核。
- 不是 [[MCP]] 或 [[Tool Calling]] 的替代品。它会使用这些能力，把它们接到 runtime 里。

## 最小例子

一个最小理解场景：

```text
你让 Hermes Agent 在远程机器上维护一个项目：
1. 通过 Telegram 发出任务。
2. Gateway 验证用户和会话。
3. AIAgent 组装 system prompt、memory、skills 和工具说明。
4. 模型决定调用终端、文件、MCP 或浏览器工具。
5. Harness 执行工具、记录 session、必要时要求危险命令审批。
6. 如果任务较长，/goal 或 kanban 让它跨 turn 继续推进。
7. Memory / session search / skills 把可复用经验留到后续会话。
```

这个例子里，真正“会想”的部分是模型；真正“能做且可控”的部分是 Hermes Agent 的 runtime。

## 常见误解 / 风险

- 误解：self-improving 等于模型会自动变强。更准确地说，它把经验写入 memory、skills 或 session search，属于外部记忆和流程复用。
- 误解：有 messaging gateway 就适合生产。多平台入口会放大授权、身份、数据泄露和误操作风险。
- 误解：有 `/goal` 就不会跑偏。持续循环只解决“继续做”的问题，不替代任务验收、测试、human-in-the-loop 或预算控制。
- 风险：skills 和 memory 如果被污染，会变成长期 prompt injection 或错误流程的来源。
- 风险：terminal / MCP / browser 工具越强，越需要 least privilege、approval、sandbox 和 audit log。

## 边界细节

- 适用条件：适合学习现代 Agent runtime 的组成方式，也适合作为具体开源项目跟踪。
- 反例：如果只想理解 [[Agent]] 的基础定义，先看 [[Agent]]、[[Agent Loop]]、[[Tool Calling]]，不要从 Hermes 的完整功能树开始。
- 和相邻概念的最小区别：[[Agent Harness]] 是抽象运行壳；Hermes Agent 是一个具体实现。[[Long-term Memory]] 是能力类别；Hermes 的 `MEMORY.md`、`USER.md`、session search 和 external providers 是具体实现。[[MCP]] 是协议；Hermes 的 MCP integration 是把协议接入自己的工具系统。
- 工程落点：重点看入口层、agent loop、tool registry、terminal backends、gateway auth、memory injection、skills loading、approval 和 `/goal` continuation。

## 现代性状态

- 判定：frontier / volatile。
- 为什么：Hermes Agent 属于 2026 年仍快速迭代的具体 Agent runtime / coding-agent / messaging-agent 项目，最新 release、平台适配、provider、MCP、security 和 goal loop 都会变化。
- 稳定部分：它把 Agent 能力拆成 harness、tools、memory、skills、workflow、security、session storage 和 gateway 的方式，符合当前工程实践。
- 易变部分：具体命令、模型 provider 数量、gateway 平台数量、release 功能、security defaults、memory provider 插件和 `/goal` judge 细节。
- 下一次复查点：2026-06-11 前后检查 GitHub latest release、README、Architecture、Security、Memory 和 Goals docs。

## 现代系统怎么吸收 Hermes Agent 的价值 / 局限

现代 Agent 系统可以从 Hermes Agent 吸收的，不是“照抄所有功能”，而是把能力分层：模型提供决策和语言生成，runtime 负责工具执行和状态持久化，gateway 负责入口和授权，memory / skills 负责跨会话复用，security / approval 负责副作用边界，trace / session storage 负责复盘。这个分层能帮助判断一个 Agent 产品是否只是在包装聊天，还是已经有真实 harness。

它的局限也应被现代系统吸收：越多入口和越多工具，越需要最小权限；越强调 self-improving，越要评估 memory 和 skill 是否正确；越依赖长期目标循环，越要设置 stop condition、turn budget、验收和人工接管。否则“会继续做”会变成“持续放大错误”。

## 证据锚点

- Source: [[Hermes Agent Repo]]
- Anchor: [[Hermes Agent Repo#为什么收]], [[Hermes Agent Repo#关键事实]], [[Hermes Agent Repo#证据锚点候选]]
- Evidence type: official repo / official docs / GitHub release metadata / engineering synthesis。
- Confidence: medium。
- Boundary: 本卡只基于 2026-05-11 查到的官方 README、docs raw markdown、GitHub latest release API 和 release notes；没有本地安装 Hermes Agent，也没有审计其代码安全性或真实任务完成率。

## 复习触发

- Hermes Agent 的 self-improving 更接近模型训练、memory，还是 skill/workflow reuse？为什么？
- 如果一个 Agent 同时有 Telegram gateway、terminal tool、MCP 和 memory，最小安全边界应该放在哪几层？
- Hermes Agent 和 [[Oh My Codex (OMX)]] 都是 Agent harness 实践，它们最相似和最不同的地方是什么？

## 相关链接

- [[Hermes Agent Repo]]
- [[Agent Harness]]
- [[Coding Agent]]
- [[Agent Workflow]]
- [[Long-term Memory]]
- [[Memory Reflection]]
- [[Tool Calling]]
- [[MCP]]
- [[Durable Execution]]
- [[Multi-agent Orchestration]]
