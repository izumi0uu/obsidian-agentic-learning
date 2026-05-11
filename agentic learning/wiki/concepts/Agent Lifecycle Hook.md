---
type: concept
topic:
  - agent
  - infrastructure
  - observability
status: growing
created: 2026-05-10
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[Claude Code Hooks 文档]]"
  - "[[OpenAI Agents SDK 文档]]"
  - "[[Oh My Codex Repo]]"
  - "[[LangSmith Evaluation and Observability]]"
  - "[[Langfuse Observability and Evaluation]]"
  - "[[Arize Phoenix Tracing 文档]]"
  - "[[OpenTelemetry GenAI Semantic Conventions]]"
evidence:
  - "[[Claude Code Hooks 文档#关键事实]]"
  - "[[OpenAI Agents SDK 文档#Tracing 补充]]"
  - "[[Oh My Codex Repo#一句话]]"
  - "[[Arize Phoenix Tracing 文档#关键事实]]"
  - "[[OpenTelemetry GenAI Semantic Conventions#关键事实]]"
related:
  - "[[Agent Harness]]"
  - "[[Agent Loop]]"
  - "[[Tool Calling]]"
  - "[[Observation]]"
  - "[[Trace]]"
  - "[[Observability]]"
  - "[[OpenTelemetry GenAI]]"
  - "[[Oh My Codex (OMX)]]"
---

# Agent Lifecycle Hook

## 一句话

Agent Lifecycle Hook 是 Agent runtime 在会话、用户输入、工具调用前后、上下文压缩、停止等生命周期边界触发的外部 handler，用来拦截、记录、补充反馈或恢复 agent loop。

## 概念详解

Agent lifecycle hook 把“模型输出之外但会影响任务安全和连续性”的动作放到 runtime 边界上。模型可以提出 tool call，或根据 observation 继续推理；但工具调用前是否需要权限确认、工具调用后如何记录、上下文压缩前保存什么、停止时是否允许结束，这些通常由 CLI、framework、plugin 或 harness 的 hook 处理。

它的学习价值在于把 [[ReAct]] 里模糊的 `Action -> Observation` 拆成更工程化的边界：PreToolUse 关注动作是否允许发生，PostToolUse 关注动作发生后怎样反馈和记录，SessionStart / Stop 关注任务生命周期，PreCompact / PostCompact 关注上下文被压缩时哪些状态必须保留。

因此 hook 不是 agent “更聪明”的证据，而是 agent runtime 更可控的证据。它让权限、日志、trace、checkpoint、通知、格式修复和人工接管有明确插槽，而不是全部塞进 prompt 纪律。

## 它解决什么问题

[[ReAct]] 只描述了 `Action -> Observation` 这种行动反馈关系，但真实系统还要回答：

- 工具执行前能不能做权限判断？
- 工具执行后能不能记录结果、补充诊断或触发格式化？
- 会话开始、用户提交 prompt、上下文压缩、任务停止时，系统能不能保存状态？
- 长任务中断后，能不能靠 ledger、trace、checkpoint 恢复？

Hook 把这些“模型输出之外的边界动作”放进 [[Agent Harness]]，让 agent loop 不只依赖 prompt 纪律。

## 它不是什么

Agent Lifecycle Hook 不是 LLM 自身能力。LLM 可以决定“我想调用工具”，但 `PreToolUse`、`PostToolUse` 这类 hook 的触发、执行、阻断、记录和反馈，属于本地产品 / CLI / framework / harness 的运行时能力。

它也不等于 [[Observation]]。Observation 是工具或环境返回给 agent 的反馈；hook 是 runtime 在关键边界触发的处理机会。一个 `PostToolUse` hook 可以读到 observation-like 的工具结果，但 hook 本身不是 observation。

它也不等于 [[Trace]]。Hook 可以产生日志、span 或 trace event；trace 是保存下来的观测记录。

## 最小例子

```text
LLM 生成 tool call
-> runtime 触发 PreToolUse
-> hook 检查权限 / 补充上下文 / 要求人工确认
-> tool 在本地或远程执行
-> runtime 触发 PostToolUse
-> hook 记录结果 / 补充反馈 / 生成 trace span
-> tool result 作为 Observation 回到上下文或 state
-> LLM 决定下一步
```

## 常见误解

- 误解：有 `PreToolUse` 就说明模型内部会调用本地工具。实际是 runtime 解析 tool call 后执行工具。
- 误解：OpenAI 或 Anthropic 服务器在管理你本地文件系统 hook。更稳的理解是：CLI / 插件 / harness 在本地触发 handler，并把需要的上下文交给模型或用户界面。
- 误解：`PostToolUse` 可以撤销所有副作用。它发生在工具成功执行后，通常只能反馈、记录、替换给模型看的输出或触发补救；阻断副作用要放在 `PreToolUse` 或权限层。
- 误解：有 trace 就等于有 hook。trace 可以由 SDK 自动生成，也可以由 hook 补充；两者是相邻层，不是同义词。

## 边界细节

在你当前这台机器上，可以把 Codex / OMX 的 hook 现象拆成两层：

- 事件槽：`~/.codex/hooks.json` 注册了 `SessionStart`、`UserPromptSubmit`、`PreToolUse`、`PostToolUse`、`PreCompact`、`PostCompact`、`Stop` 等事件。
- handler：这些事件当前指向 `oh-my-codex/dist/scripts/codex-native-hook.js`，所以具体增强逻辑来自 OMX 本地 harness。

可观测数据也分层：

- 本地 raw artifact：`.omx/logs/turns-*.jsonl`、`.omx/metrics.json`、`.omx/state/session.json`、`.omx/state/subagent-tracking.json`、`.omx/goals/.../ledger.jsonl`。
- Trace / span：把模型调用、工具调用、handoff、guardrail、错误、延迟和 token 记录成结构化执行轨迹。
- Dashboard / OTLP：把 trace 送到 LangSmith、Langfuse、Phoenix、OpenAI Agents tracing 或 OpenTelemetry collector，做实时观察、调试、评估和成本分析。

因此更准确的说法是：`PreToolUse` / `PostToolUse` 这种生命周期边界不是模型能力；在你的环境里，事件配置属于 Codex 本地 hook 配置，行为增强主要由 OMX handler 承接。

## 现代性状态

Agent Lifecycle Hook 是基础软件思想 + 当前 Agent 工程实践。

- 基础地基：hook 是软件系统里长期存在的生命周期扩展点思想。
- 当前工程实践：代码 Agent / Agent framework 用 hook、trace、approval gate、guardrails 和 state artifact 接管 ReAct loop 的工具执行边界。
- 前沿 / 易变：具体产品的 hook 事件名、JSON schema、权限字段、UI 行为和 dashboard 集成会快速变化，需要 `freshness: watch/volatile`。

小判断：`Agent Lifecycle Hook` 不是一篇旧论文范式，而是现代 Agent 产品和框架吸收 ReAct 局限时常用的运行时控制点。

## 现代系统怎么吸收 ReAct 的局限

ReAct 的弱点之一是 action 格式、权限、失败恢复和循环停止都容易压在 prompt 上。生命周期 hook 把这些地方移到 runtime：

- `PreToolUse` 接管“工具能不能执行、参数是否安全、是否需要人工确认”。
- `PostToolUse` 接管“工具执行后如何记录、反馈、补救和生成 trace”。
- `Stop` / `PreCompact` / `PostCompact` 接管“任务能不能结束、上下文压缩前后要保存什么”。
- `.omx/`、LangSmith、Langfuse、Phoenix、OpenTelemetry 等观测层接管“发生了什么、为什么慢、哪里错、如何复现”。

所以现代系统不是让 LLM 更努力遵守 `Thought/Action/Observation` 文本模板，而是把关键边界做成可拦截、可审计、可恢复的运行时事件。

## 证据锚点

- Evidence type: official docs note — [[Claude Code Hooks 文档]]，支持 hook event / handler 这种本地生命周期扩展点。
- Evidence type: official docs note — [[OpenAI Agents SDK 文档]]，主要支持 tracing / agent framework 侧的运行可观测性语境。
- Evidence type: local repo / engineering evidence — [[Oh My Codex Repo]] 与本地 hook 配置，用于说明当前环境里 OMX handler 承接 hook 行为。
- Evidence type: observability docs — [[LangSmith Evaluation and Observability]]、[[Langfuse Observability and Evaluation]]、[[Arize Phoenix Tracing 文档]]、[[OpenTelemetry GenAI Semantic Conventions]]，用于支持 trace / span / dashboard / OTLP 边界。
- Local evidence: `~/.codex/hooks.json` 注册了 hook event，并指向 `oh-my-codex/dist/scripts/codex-native-hook.js`。
- Local evidence: `.omx/logs/turns-2026-05-10.jsonl`、`.omx/metrics.json`、`.omx/state/session.json`、`.omx/state/subagent-tracking.json`、`.omx/goals/autoresearch/.../ledger.jsonl` 存在本地可观测 artifact。
- Boundary: 本卡把多个来源综合成 runtime 边界解释；不同 CLI / SDK 的 hook 事件名、字段和安全语义需要回到对应官方文档确认。
- Confidence: medium。

## 复习触发

- 为什么 `PreToolUse` 更适合阻断危险动作，而 `PostToolUse` 更适合记录和补救？
- Hook、Observation、Trace 三者分别处在哪一层？
- 如果一个 Agent 在上下文压缩后继续任务，hook 需要帮助保存哪些信息？

## 相关链接

- [[Agent Harness]]
- [[Agent Loop]]
- [[Tool Calling]]
- [[Observation]]
- [[Trace]]
- [[Observability]]
- [[OpenTelemetry GenAI]]
- [[Oh My Codex (OMX)]]
