---
type: concept
topic:
  - evaluation
  - observability
  - frontier
status: growing
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[前沿主源清单]]"
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models]]"
  - "[[LangSmith Evaluation and Observability]]"
  - "[[Langfuse Observability and Evaluation]]"
  - "[[OpenAI Agents SDK 文档]]"
  - "[[Claude Code Hooks 文档]]"
evidence:
  - "[[前沿主源清单#评测与观测]]"
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]]"
  - "[[LangSmith Evaluation and Observability#为什么收]]"
  - "[[LangSmith Evaluation and Observability#边界提醒]]"
  - "[[Langfuse Observability and Evaluation#一句话]]"
  - "[[Langfuse Observability and Evaluation#OpenTelemetry 补充]]"
  - "[[OpenAI Agents SDK 文档#Tracing 补充]]"
  - "[[Claude Code Hooks 文档#关键事实]]"
related:
  - "[[Evaluation]]"
  - "[[Observability]]"
  - "[[Agent Loop]]"
  - "[[Tool Calling]]"
  - "[[Agent Lifecycle Hook]]"
  - "[[Trajectory Trace 类型对比]]"
  - "[[Trajectory]]"
  - "[[Reasoning Trace]]"
  - "[[Replay]]"
---

# Trace

## 一句话

Trace 是对 Agent / LLM 应用执行过程的结构化可观察记录，包括输入、模型调用、工具调用、工具结果、状态变化、错误、成本、延迟和最终结果。

## 概念详解

Trace 出现的原因，是 Agent 失败往往不是最终答案那一刻才发生。错误可能来自错误计划、坏检索、工具参数、权限拒绝、观察误读、上下文污染、成本爆炸或中途异常。Trace 把一次执行拆成有时间顺序和层级关系的记录，让人能沿着过程回看。

一个好的 trace 通常由多个 span 或 event 组成：用户输入、LLM request、retrieval、rerank、tool call、tool result、guardrail、handoff、exception、evaluator score 和最终输出。它不只是“日志很多”，而是有 run id、span id、父子关系、metadata、latency、token/cost 和错误信息。这样 trace 才能被 [[Observability]] 平台搜索、聚合、可视化，也才能被 [[Eval Harness]] 用来生成失败数据集、回归样本或 trajectory evaluator 输入。

Trace 的学习价值在于它把“系统为什么这样表现”从猜测变成证据。你可以问：失败是否发生在 tool call 前？模型是否看到了正确 observation？检索是否返回了旧文档？高风险动作是否经过 approval？这些问题都需要 trace 材料，而不是只读 final answer。


Trace 还承担“关联上下文”的职责。同一个错误如果不能关联到 prompt 版本、model/provider、tool schema、retrieval index、user/session、workflow node 和 deployment version，就很难判断是模型退化、工具接口变化、检索数据过期，还是某个实验分支引入问题。好的 trace 不只是记录步骤，还记录足够的 metadata，让失败能被聚类、比较和回归。

另一个边界是“记录粒度”。开发期可以保存更详细 span 帮助调试；生产期可能因为隐私、成本和合规只保存摘要、采样 trace 或脱敏字段。粒度降低会影响 evaluation harness 能做什么：如果没有工具参数和 observation，trajectory evaluator 就很难判断权限和过程质量。

## 它解决什么问题

Agent 失败时，单看最终答案很难知道哪里错了。Trace 让我们能看到每一步，定位是计划错、工具错、检索错、权限错、状态错，还是模型误读了观察结果。

Trace 还把一次失败变成可复盘材料：可以重放、标注、打分、转成 regression eval，或者定位某个工具 span 的延迟和成本。没有 trace，Agent 调试常常只能靠猜。

## 它不是什么

Trace 不是日志的简单堆积。日志可以是散乱文本；好的 trace 应该有层级、时间顺序、输入输出、span、metadata，并能支持调试、重放、评测和成本/延迟分析。

Trace 也不等于 [[Trajectory]]。Trajectory 偏“任务实际走过的路径”；Trace 偏“系统把这条路径保存下来的记录”。记录不完整时，trace 只能看到 trajectory 的一部分。

[[Reasoning Trace]] 是 trace 的一种子类型。它关注模型显式写出的推理过程；完整 trace 还应该包括工具调用、工具结果、状态变化、错误和最终结果。

## 最小例子

一个 RAG Agent 的 trace 可能包括：

1. 用户问题。
2. query rewrite。
3. 检索请求。
4. 返回的文档片段。
5. rerank 结果。
6. 生成答案。
7. 引用来源。
8. evaluator 或人工反馈给出的 score。

如果第 7 步引用了错误来源，trace 可以帮助判断问题发生在检索、rerank、生成还是引用拼接。

## 常见误解 / 风险

- 误解：trace 越完整，系统质量越高。实际 trace 只说明可观察性，不自动说明答案正确。
- 误解：把模型 chain-of-thought 全量保存就是 trace。完整 trace 还包括工具、状态、观察和结果；而完整推理文本可能不适合保存或展示。
- 风险：trace 里可能包含 prompt、用户数据、工具返回、密钥片段或业务数据，需要脱敏和访问控制。
- 风险：不同平台 trace schema 不一致，导致跨系统比较和 eval 回流困难。

## 边界细节

最重要的三分法：

```text
Trajectory = 任务实际走过的路径
Trace = 系统记录下来的可观察过程数据
Evaluation = 对结果或过程做质量判断
```

Trace 是 evaluation harness 的材料，不是 evaluator 本身。Harness 可以读取 trace，判断工具顺序是否合理、是否发生越权、是否符合 latency/cost 预算；但这些判断来自 rubric、代码 checker、LLM-as-judge 或人工 review。

Trace 也不自动等于 replay。要 replay，还需要固定输入、工具返回、检索结果、环境快照或随机性。Trace 可以告诉你发生过什么，但未必足够重建当时环境。

## Hook 数据和 Trace 的关系

[[Agent Lifecycle Hook]] 常常是生成 trace 的入口：在模型调用前后、工具调用前后、session start/stop、错误和压缩等边界写事件。

但 hook event 只是原始材料。要变成高质量 trace，还需要：

- correlation id：把同一次任务的事件串起来。
- span hierarchy：知道哪个 LLM call 触发哪个 tool call。
- schema：字段名稳定，例如 model、tool、latency、tokens、cost、error。
- redaction：不要把敏感 prompt、secrets、PII 原样保存。
- sampling / retention：决定哪些 trace 长期保存。

## 现代性状态

- 判定：current-practice / frontier-adjacent。
- 为什么：trace 作为 observability 基础已经是当前工程实践；但 OpenTelemetry GenAI、各平台 schema、SDK tracing API 和跨工具标准仍在快速演进。
- 稳定部分：记录过程以支持调试、评估、回放和成本/延迟分析。
- 易变部分：具体 span 字段、平台 API、OTel 语义约定、隐私默认值和 UI 能力。
- 复查点：当 OpenTelemetry GenAI 或主流 Agent SDK 对 trace/span 语义有重大变化时，更新本卡和 [[OpenTelemetry GenAI]]。

## 现代系统怎么吸收 Trace 的价值 / 局限

现代 Agent 平台通常把 trace 放进三条闭环：

- 调试闭环：开发者查看失败 trace，定位 prompt、tool、retrieval 或 state 问题。
- 评测闭环：trace 被标注、打分、加入 dataset，再通过 eval harness 回归测试。
- 运营闭环：线上监控 latency、token cost、error rate、tool failure 和用户反馈。

局限是：trace 只能记录被系统捕获的内容。没有 hook、没有 span、被脱敏掉或没有 correlation id 的部分，都不会自动出现在 trace 里。因此 trace 的质量取决于 harness 设计。

## 证据锚点

- Source: [[前沿主源清单]]
- Anchor: [[前沿主源清单#评测与观测]]
- Source: [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Anchor: [[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]]
- Source: [[LangSmith Evaluation and Observability]]
- Anchor: [[LangSmith Evaluation and Observability#为什么收]] / [[LangSmith Evaluation and Observability#边界提醒]]
- Source: [[Langfuse Observability and Evaluation]]
- Anchor: [[Langfuse Observability and Evaluation#一句话]] / [[Langfuse Observability and Evaluation#OpenTelemetry 补充]]
- Source: [[OpenAI Agents SDK 文档]]
- Anchor: [[OpenAI Agents SDK 文档#Tracing 补充]]
- Source: [[Claude Code Hooks 文档]]
- Anchor: [[Claude Code Hooks 文档#关键事实]]
- Evidence type: official docs/source notes + engineering synthesis.
- Confidence: medium
- Boundary: hook/span/platform 字段属于易变实现；“记录过程以支持调试和评估”是稳定概念。

## 复习触发

- 为什么说 trace 记录“发生了什么”，evaluation 才判断“好不好”？
- 用一个工具调用失败的例子说明 [[Trajectory]]、[[Trace]]、[[Reasoning Trace]] 的区别。
- 如果 trace 里包含敏感数据，你会在评估闭环里怎么处理？

## 相关链接

- [[Evaluation]]
- [[Observability]]
- [[Agent Loop]]
- [[Tool Calling]]
- [[Agent Lifecycle Hook]]
- [[Trajectory Trace 类型对比]]
- [[Trajectory]]
- [[Reasoning Trace]]
- [[Replay]]
