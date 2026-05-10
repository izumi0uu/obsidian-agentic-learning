---
type: concept
topic:
  - observability
  - evaluation
  - frontier
status: growing
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

## 概念详解

Observability 解决的是“系统内部发生了什么”这个问题。普通软件里，我们用 logs、metrics、traces 看请求路径、错误率和延迟；Agent 系统里，失败原因还会跨越模型调用、prompt、tool call、retrieval、memory、guardrail、human approval 和外部环境。因此 Agent observability 的核心不是多打印日志，而是把一次任务的关键步骤关联成可解释的执行图。

它通常依赖 [[Trace]] 作为骨架：每次 LLM call、tool call、retrieval、handoff、exception、score、用户反馈都可以成为 span 或 event。然后 observability 平台再提供搜索、过滤、聚合、可视化、在线监控、失败样本收集和 eval 数据集回流。这样团队不仅能看到“这次答错了”，还能看到错在检索、工具参数、模型选择、权限拒绝、上下文污染还是成本/延迟异常。

对 evaluation harness 来说，observability 是证据来源，不是判分本身。Harness 可以从 trace 里抽取失败样本、运行 evaluator、比较 prompt 版本；observability 则帮助理解为什么指标变化、哪些 span 最常失败、哪些工具最贵或最慢。


Agent observability 还必须处理“版本”问题。一次失败 trace 只有和 prompt 版本、模型版本、工具 schema、检索索引版本、workflow graph、guardrail 配置和部署环境绑定起来，才有复盘价值。否则今天看到的错误，明天可能因为索引更新或模型切换而无法解释。成熟的 observability 因此会把 trace、dataset、experiment、evaluator 和 release metadata 连接起来。

另一个学习重点是在线与离线的转换。线上 observability 负责捕捉真实分布里的慢、贵、错和危险；离线 evaluation harness 负责把这些样本变成可重复的测试。两者之间的桥通常是 trace 标注、失败聚类、数据集采样和 replay。没有这座桥，observability 只能“看见问题”，很难证明修复。

## 它解决什么问题

Agent 失败通常不是单点错误：可能是检索差、工具参数错、模型选择错、权限被拒、上下文污染、成本暴涨。Observability 让我们看到过程，而不是只看到最终答案。

它还支持线上/离线闭环：线上 trace 暴露真实失败，离线 eval harness 把失败变成 regression case，再用新的 prompt、模型或工作流验证修复是否有效。

## 它不是什么

Observability 不是普通日志。

普通日志只记录事件；Agent observability 还要把 LLM call、tool call、retrieval、span、trace、score、用户反馈和实验版本关联起来。

它也不是 [[Evaluation]]。Observability 记录和展示发生了什么；Evaluation 判断结果或过程好不好。没有评分的 trace 只是可见，不等于可评估。

## 最小例子

一次 RAG Agent 回答错误，observability 可以显示：

- query rewrite 生成了错误子问题。
- retriever 返回了旧文档。
- reranker 把相关文档排到后面。
- 模型没有引用来源。

如果同时有 evaluator 分数和用户反馈，团队就能把这条 trace 加入失败数据集，下次修改检索策略后重跑。

## 常见误解 / 风险 / 边界细节

- 记录越多越好是错的，敏感数据会进入 trace。
- 没有评分的 trace 只是可见，不等于可评估。
- 线上监控和离线 eval 应该互相反馈。
- 采样率、数据保留和脱敏是产品化边界。
- 把 observability 当成安全控制也不够；允许/拒绝动作仍要靠 guardrails、policy 和 approval。

## 边界细节

可以用一个问题区分邻近概念：

- [[Trace]]：这次执行留下了哪些结构化记录？
- Observability：我如何搜索、聚合、可视化、告警和分析这些记录？
- [[Evaluation]]：这次执行或一组执行到底好不好？
- [[Audit Log]]：哪些关键行动需要长期可追责？
- [[OpenTelemetry GenAI]]：这些 span/event/attribute 如何跨系统标准化？

Observability 的边界还包括隐私和成本。完整记录 prompt、工具返回和用户数据会让调试更方便，但也可能让敏感信息进入第三方平台或长期存储。因此生产系统通常需要采样、脱敏、字段分级、保留周期和访问控制。

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
- Anchor: [[LangSmith Evaluation and Observability#为什么收]] / [[Langfuse Observability and Evaluation#为什么收]] / [[OpenAI Agents SDK 文档#为什么收]] / [[Arize Phoenix Tracing 文档#关键事实]] / [[OpenTelemetry GenAI Semantic Conventions#关键事实]]
- Evidence type: platform/source notes + engineering synthesis.
- Confidence: medium
- Boundary: “用 trace/span/metrics 看清 Agent 过程”是稳定方向；平台 UI、SDK API、OTel 字段和脱敏实践需要持续复查。

## 复习触发

- 为什么 observability 不等于 evaluation？
- 一次 RAG Agent 失败时，你会希望 trace 里至少看到哪 5 类 span 或 event？
- 如果 observability 平台记录了完整 prompt 和工具返回，隐私边界在哪里？

## 相关链接

- [[Trace]]
- [[Agent Lifecycle Hook]]
- [[Eval Harness]]
- [[Replay]]
- [[OpenTelemetry GenAI]]
- [[LLM-as-Judge]]
- [[Trajectory Evaluation]]
