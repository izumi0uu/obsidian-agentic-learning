---
type: concept
topic:
  - agent
  - reasoning
  - tool-use
status: growing
created: 2026-05-05
updated: 2026-05-12
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models]]"
  - "[[Anthropic - Building Effective Agents]]"
  - "[[OpenAI - A Practical Guide to Building Agents]]"
  - "[[LangGraph 官方文档]]"
  - "[[OpenAI Agents SDK 文档]]"
evidence:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]]"
  - "[[Anthropic - Building Effective Agents#为什么收]]"
  - "[[OpenAI - A Practical Guide to Building Agents#为什么收]]"
  - "[[LangGraph 官方文档#为什么收]]"
  - "[[OpenAI Agents SDK 文档#为什么收]]"
related:
  - "[[Agent Loop]]"
  - "[[Tool Calling]]"
  - "[[Reasoning Trace]]"
  - "[[Observation]]"
  - "[[Environment Observation 类型对比]]"
  - "[[Planning]]"
  - "[[Agent Harness]]"
  - "[[Agent Lifecycle Hook]]"
  - "[[Guardrails]]"
  - "[[Evaluation]]"
  - "[[ReAct Plan-and-Solve Reflexion 对比]]"
---

# ReAct

## 一句话

ReAct 是让语言模型交替生成 reasoning traces 和 actions 的 Agent 模式。

## 概念详解

ReAct 的核心贡献，是把语言模型的推理文本和外部行动放进同一条轨迹：模型先写出当前判断，再选择 Action，环境或工具返回 [[Observation]]，新的 observation 又影响下一轮判断。它解决的不是“让模型多想几步”这么简单，而是把推理从封闭文本空间拉到外部世界里校准。纯 CoT 可能把错误假设写得很流畅；纯工具调用又可能缺少为什么调用、下一步如何决定的解释。ReAct 把二者连接起来。

证据边界要分清：ReAct 论文支持的是 reasoning/action/observation 交替范式；用户提供和本 vault 重绘的图帮助理解 LLM、Tools、Environment、runtime loop 的工程分工；Anthropic、OpenAI、LangGraph、Agents SDK 等现代来源说明，这个范式今天通常不会以裸文本 parser 运行，而会被 tool schema、state graph、trace、guardrails、approval 和 eval 包住。

所以 ReAct 是理解 Agent Loop 的地基卡，而不是生产系统模板。它保留下来的价值是“行动要被观察校正，观察要回到下一轮决策”；被现代系统吸收的局限是“Action 格式、工具执行、状态保存、权限、停止条件不能只靠 prompt”。学习时要把 ReAct 放在 [[Zero-shot CoT]]、[[Tool Calling]]、[[Observation]]、[[Agent Harness]] 之间比较，才能看清它既不是普通推理提示，也不是完整 Agent 平台。

还有一个容易忽略的边界：ReAct 的 reasoning trace 不一定应该完整暴露给最终用户，也不一定应该被当成事实证据。工程系统更关心的是 action 是否合规、observation 是否可信、下一步决策是否使用了正确反馈、最终答案是否可验证。换句话说，ReAct 的教学价值在于展示 loop 结构；生产价值在于启发 runtime 设计，而不是要求每个 Agent 都把完整 Thought 文本写出来。
## 它解决什么问题

纯推理容易脱离外部事实并产生幻觉；纯行动又缺少可解释的计划和状态跟踪。ReAct 把“想”和“做”交替起来，让工具或环境反馈修正后续推理。

## 它不是什么

ReAct 不是完整的生产级 Agent 平台。

它也不是所有 Agent 都必须采用的固定格式。真实系统可能隐藏推理、改用结构化 planner，或把行动循环封装在框架里。

更细一点：ReAct 不是“Agent 的同义词”。它是理解 [[Agent Loop]] 的经典模式之一，但现代系统常把可预测部分做成 workflow，只把不可预测、需要环境反馈和动态决策的部分交给 agent loop。

## 最小例子

```text
Thought: 我需要查资料。
Action: Search[问题]
Observation: 搜索结果
Thought: 结果不够，换关键词。
Action: Search[新关键词]
```

## 常见误解

不要把 ReAct 理解成“LLM 自己在内部调用工具”。LLM 通常只是输出下一步意图或结构化 tool call，真正执行工具、拿回 Observation、写入上下文、决定是否继续循环的是外部框架或 [[Agent Harness]]。

也不要把 ReAct 等同于所有 Agent。很多生产系统会把稳定路径写成 [[Agent Workflow]]，只在需要动态决策、环境反馈或工具探索的部分使用 agent loop。

## 边界细节

ReAct 的价值在于揭示 [[Agent Loop]] 的核心：行动不是一次性输出，而是和观察反馈绑定在一起。

用户提供的 `reAct.png` 可以作为 ReAct 工程分工的最小外部视角：[[LLM]] 负责生成下一步 reasoning/action，Tools 是可调用能力集合，Environment 是动作发生并返回状态变化的外部世界。真正的 loop 不在这三个盒子之一，而是由外部框架或 [[Agent Harness]] 驱动。

下面这张重绘图把这个 loop 显式补出来：Action 由 runtime 执行，Observation 被写回上下文或 state，然后 LLM 再决定下一步。

![[react-agent-loop.svg]]

## 现代系统怎么吸收 ReAct 的局限

截至 2026-05-08，生产 Agent 很少只靠一段 `Thought -> Action -> Observation` 提示词裸跑。更常见的是保留“模型根据观察决定下一步”的核心，但把脆弱部分移到工程层：

- 对可预测任务，用 prompt chaining、routing、parallelization 等 workflow，让路径由代码或图结构控制。
- 对不可预测任务，用 agent loop、state graph 或 orchestrator-workers，让模型动态拆解任务，但由 [[Agent Harness]] 管住状态、权限、trace、重试和停止条件。
- 对 Action 格式问题，用 [[Tool Calling]]、JSON schema、typed output、参数校验和失败重试，减少靠自然语言解析动作。
- 对局部最优和原地循环，用 [[Planning]]、evaluator-optimizer、trajectory evaluation、最大迭代数、预算上限、checkpoint 和 [[Human-in-the-loop]]。
- 对提示词脆弱性，用版本化 prompt、回归 eval、observability trace、清晰工具文档、分层 [[Guardrails]] 和 [[Agent Lifecycle Hook]]。

还有一层更工程化的吸收方式：把 `Action` 的执行边界拆成 `PreToolUse -> tool execution -> PostToolUse`。这样工具执行前可以做权限、审批和参数校验，执行后可以记录 trace、更新 state 或补充 observation，而不是把所有稳定性都压在 prompt 模板上。

所以现代 Agent 不是“抛弃 ReAct”，而是把 ReAct 从一个 prompt 模板，降级成一个可被框架、工具协议、评测和权限系统包住的行动循环思想。

## 现代性状态

用 [[LLM Wiki 工作流#操作 6：现代性 / 前沿性判定]] 来分层：

- 基础地基：ReAct 论文提出的 reasoning/action/observation 交替，是理解 [[Agent Loop]]、[[Observation]]、[[Trajectory]] 的稳定地基。
- 历史过渡：裸 `Thought -> Action -> Observation` 文本格式和手写 action parser，更像早期 prompt-era 实现。它解释了为什么后来需要 tool schema、状态机和 trace，但不应被当成今天生产系统的默认形态。
- 当前工程实践：保留“根据环境反馈继续决策”的 loop，但由 [[Tool Calling]]、[[Agent State]]、[[Agent Workflow]]、[[Guardrails]]、[[Trace]]、[[Evaluation]]、[[Human-in-the-loop]] 和 [[Agent Harness]] 接管执行边界。
- 前沿 / 易变：具体框架或 SDK 里的 tool API、tracing API、session/memory 接口、approval gate 实现会快速变化，应追踪在对应 source note 或 [[03 前沿追踪]]，不要反向改写 ReAct 的基础定义。

小判断：当你问“ReAct 现在还用吗”，更准确的答案是“ReAct 的 loop 思想还在，裸 prompt 模板退到历史过渡层，现代实现由框架和 runtime 接管”。

## 证据锚点

- Paper source: [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Practice / official sources: [[Anthropic - Building Effective Agents]], [[OpenAI - A Practical Guide to Building Agents]], [[LangGraph 官方文档]], [[OpenAI Agents SDK 文档]]
- Asset: `agentic learning/raw/assets/reAct.png`（用户提供原始透明背景截图，2026-05-10）
- Asset: `agentic learning/raw/assets/reAct-white-bg.png`（为透明 PNG 添加白色背景，2026-05-10）
- Asset: `agentic learning/raw/assets/react-agent-loop.svg`（按 [[Reflexion]] 图风格重绘，用于说明 ReAct loop，2026-05-10）
- Anchor: [[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]], [[ReAct - Synergizing Reasoning and Acting in Language Models#Ingest 摘要]], [[Anthropic - Building Effective Agents#为什么收]], [[OpenAI - A Practical Guide to Building Agents#为什么收]], [[LangGraph 官方文档#为什么收]], [[OpenAI Agents SDK 文档#为什么收]]
- Evidence type: paper source note + official/practice source notes + user-provided visual asset + engineering synthesis.
- Confidence: medium
- Boundary: ReAct 原始证据支持 reasoning/action/observation 交替；tool schema、hook、state graph、trace、approval 等现代吸收方式来自工程来源综合，不是论文原文逐条声明。

## 复习触发

- 为什么 ReAct 不是 [[Zero-shot CoT]]？请用 Action 和 Observation 解释。
- 如果把 ReAct 的 `Action` 换成 [[Tool Calling]]，还剩哪些问题需要 harness 处理？
- 什么时候裸 `Thought -> Action -> Observation` prompt 会退化成不可靠 parser？

## 相关链接

- [[Agent Loop]]
- [[Tool Calling]]
- [[Reasoning Trace]]
- [[Observation]]
- [[Environment Observation 类型对比]]
- [[Planning]]
- [[Agent Harness]]
- [[Agent Lifecycle Hook]]
- [[Guardrails]]
- [[Evaluation]]
- [[ReAct Plan-and-Solve Reflexion 对比]]
