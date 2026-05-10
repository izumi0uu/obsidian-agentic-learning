---
type: concept
topic:
  - observability
  - evaluation
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[LangSmith Evaluation and Observability]]"
  - "[[Langfuse Observability and Evaluation]]"
  - "[[OpenAI Agents SDK 文档]]"
  - "[[Arize Phoenix Tracing 文档]]"
  - "[[OpenTelemetry GenAI Semantic Conventions]]"
evidence:
  - "[[LangSmith Evaluation and Observability#为什么收]]"
  - "[[Langfuse Observability and Evaluation#为什么收]]"
  - "[[OpenAI Agents SDK 文档#为什么收]]"
  - "[[Arize Phoenix Tracing 文档#关键事实]]"
  - "[[OpenTelemetry GenAI Semantic Conventions#关键事实]]"
related:
  - "[[Trace]]"
  - "[[Agent Lifecycle Hook]]"
  - "[[Evaluation]]"
  - "[[Eval Harness]]"
  - "[[Replay]]"
  - "[[OpenTelemetry GenAI]]"
---

# Observability

## 一句话

Observability 是让 Agent 系统的输入、输出、工具调用、延迟、成本、错误和质量信号可观察、可调试、可追踪。

## 它解决什么问题

Agent 失败通常不是单点错误：可能是检索差、工具参数错、模型选择错、权限被拒、上下文污染、成本暴涨。Observability 让我们看到过程，而不是只看到最终答案。

## 它不是什么

Observability 不是普通日志。

普通日志只记录事件；Agent observability 还要把 LLM call、tool call、retrieval、span、trace、score、用户反馈和实验版本关联起来。

## 最小例子

一次 RAG Agent 回答错误，observability 可以显示：

- query rewrite 生成了错误子问题。
- retriever 返回了旧文档。
- reranker 把相关文档排到后面。
- 模型没有引用来源。

## 常见误解 / 风险 / 边界细节

- 记录越多越好是错的，敏感数据会进入 trace。
- 没有评分的 trace 只是可见，不等于可评估。
- 线上监控和离线 eval 应该互相反馈。
- 采样率、数据保留和脱敏是产品化边界。

## 实时观测接入层

可以把 Agent observability 分成三层：

- 本地运行 artifact：例如 `.omx/logs/turns-*.jsonl`、`.omx/metrics.json`、`.omx/state/session.json`、`.omx/goals/.../ledger.jsonl`。这类数据适合恢复、审计和本地调试。
- Trace / span 数据：把 LLM call、tool call、retrieval、handoff、guardrail、exception、latency、token、cost 组织成结构化执行轨迹。
- 观测平台或协议：LangSmith、Langfuse、Phoenix、OpenAI Agents SDK tracing 可以显示和分析 trace；OpenTelemetry / OTLP 更偏跨系统传输和字段语义统一。

小边界：实时观测可以让你看到“Agent 正在做什么、慢在哪里、错在哪里”，但不自动给出“该不该允许这个动作”的答案。允许/拒绝仍要靠 [[Guardrails]]、[[Tool Permissioning]]、policy engine 或 human approval。

### OMX 的推荐路径

OMX 目前更偏“本地 operator observability”：

- 先看 `.omx/` artifacts：状态、日志、计划、notepad、goal ledger。
- 再用 `omx hud --watch` / `omx hud --json` 做实时状态面板。
- 多 worker 时用 `omx sidecar`、team status 或 tmux pane 状态看并行执行。
- 需要提醒时配 notifications；普通长任务用 Telegram / Discord / Slack / generic webhook，复杂生产通知编排再看 OpenClaw。
- 需要接入标准 observability 平台时，再把 hook / JSONL / trace 转成 OpenTelemetry / OTLP，送到 Langfuse、Phoenix 或其他平台。

小判断：OMX 社区当前默认不是“直接上 LangSmith/Langfuse/Phoenix”，而是先把本地 harness 的状态看清楚；外部平台属于第二层集成。

## 现代性状态

- 基础地基：observability 来自软件工程的 logs、metrics、traces 和 monitoring。
- 当前工程实践：LLM/Agent observability 已经是生产系统必备层，尤其用于调试工具调用、RAG 检索、成本、延迟和失败 trace。
- 前沿 / 易变：具体平台、SDK tracing API、OpenTelemetry GenAI 字段、prompt/response 脱敏策略仍在快速演进。

## 证据锚点

- Source: [[LangSmith Evaluation and Observability]]
- Source: [[Langfuse Observability and Evaluation]]
- Source: [[OpenAI Agents SDK 文档]]
- Source: [[Arize Phoenix Tracing 文档]]
- Source: [[OpenTelemetry GenAI Semantic Conventions]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Trace]]
- [[Agent Lifecycle Hook]]
- [[Eval Harness]]
- [[Replay]]
- [[OpenTelemetry GenAI]]
- [[LLM-as-Judge]]
- [[Trajectory Evaluation]]
