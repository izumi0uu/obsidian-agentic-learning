---
type: concept
topic:
  - evaluation
  - observability
  - frontier
status: seed
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
  - "[[前沿主源清单#RAG 进化]]"
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
- 误解：把模型 chain-of-thought 存下来就是 trace。实际生产 trace 更关注可审计事件、工具结果、状态变化和错误边界；显式推理文本还可能有隐私、安全或可靠性问题。
- 风险：trace 可能包含用户数据、密钥片段、工具返回的敏感内容或内部路径，不能不加筛选地外发给评估模型或第三方平台。
- 风险：只采样成功 trace 会让评估集失真；失败 trace 才常常是最有价值的 regression 材料。

## 边界细节

Trace 是 [[Observability]] 的基础，也是 [[Eval Harness]] 复现失败的重要材料。

一个实用边界：trace 记录“发生了什么”，score / eval 才判断“好不好”。不要把完整 trace 等同于质量评估。

另一个边界：trajectory 是被记录对象，trace 是记录形式，[[Reasoning Trace]] 是其中的推理文本切片。

和普通日志的最小区别：普通日志常按系统输出文本；trace 通常按一次请求或任务组织出 span 树，例如 model span、retrieval span、tool span、handoff span、guardrail span。

## Hook 数据和 Trace 的关系

[[Agent Lifecycle Hook]] 是 trace 的一个上游来源。比如 `PreToolUse` 可以记录“模型想调用什么工具、参数是什么、权限判断是什么”；`PostToolUse` 可以记录“工具返回了什么、耗时多少、是否失败、是否补充反馈”。

但 hook 不等于 trace。Hook 是事件处理入口；trace 是把这些事件和模型调用、工具调用、状态变化、错误、token、成本、延迟串起来的观测记录。一个系统可以没有显式 hook 也自动生成 trace；也可以用 hook 补充更细的 trace span。

## 现代性状态

- 判定：current-practice / frontier-adjacent
- 为什么：trace 作为 observability 基础已经是当前工程实践；但 OpenTelemetry GenAI、各平台 schema、SDK tracing API 和跨工具标准仍在快速演进。
- 稳定部分：记录输入输出、工具调用、状态变化、错误、延迟、成本，并把失败转成调试/评估材料。
- 易变部分：具体字段名、平台 UI、OTel semantic conventions、SDK 自动追踪范围、隐私过滤机制。
- 复查点：当 OpenTelemetry GenAI 或主流 Agent SDK 对 trace/span 语义有重大变化时，更新本卡和 [[OpenTelemetry GenAI]]。

## 现代系统怎么吸收 Trace 的价值 / 局限

现代 Agent 系统通常把 trace 放在三条链路里：

- 开发调试：从失败 trace 定位哪个 prompt、tool、retriever、guardrail 或 state transition 出错。
- 线上观测：监控 latency、token、cost、error、tool failure、user feedback 和异常路径。
- 评测闭环：把代表性 trace 放进 dataset，用 evaluator、规则或人工 review 做 regression。

局限也很明确：trace 不是自动修复器。它能暴露过程，但仍需要 evaluator、工程规则、人类判断或测试来决定问题是否重要、如何修复。

## 证据锚点

- Source: [[LangSmith Evaluation and Observability]]
- Anchor: [[LangSmith Evaluation and Observability#一句话]] / [[LangSmith Evaluation and Observability#边界提醒]]
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
