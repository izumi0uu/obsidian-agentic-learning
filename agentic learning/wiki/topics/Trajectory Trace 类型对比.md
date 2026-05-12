---
type: map
topic:
  - agent
  - evaluation
  - observability
  - comparison
status: active
created: 2026-05-10
updated: 2026-05-12
source:
  - "[[Trajectory]]"
  - "[[Trace]]"
  - "[[Reasoning Trace]]"
  - "[[Trajectory Evaluation]]"
  - "[[Replay]]"
  - "[[Observability]]"
evidence:
  - "[[Trajectory#证据锚点]]"
  - "[[Trace#证据锚点]]"
  - "[[Reasoning Trace#证据锚点]]"
  - "[[Trajectory Evaluation#证据锚点]]"
  - "[[Replay#证据锚点]]"
related:
  - "[[Agent 主题]]"
  - "[[Trajectory]]"
  - "[[Trace]]"
  - "[[Reasoning Trace]]"
  - "[[Trajectory Evaluation]]"
  - "[[Replay]]"
  - "[[Observability]]"
  - "[[Evaluation]]"
---

# Trajectory Trace 类型对比

## 一句话总览

这页回答：Trajectory、Trace、Reasoning Trace、Trajectory Evaluation 和 Replay 到底差在哪里。核心边界：[[Trajectory]] 是任务路径本身；[[Trace]] 是系统记录下来的过程数据；[[Reasoning Trace]] 是模型显式写出的推理文字；[[Trajectory Evaluation]] 是对过程好坏的判断；[[Replay]] 是用记录复现过程。

最小判断：trajectory 是路线，trace 是路线记录，reasoning trace 是路上的想法，evaluation 是事后评分，replay 是按记录重放。

## 为什么这组值得对比

- 混淆风险高：trace / trajectory / reasoning trace 在 Agent 论文、框架和观测工具里经常混用。
- 共同问题域相同：都围绕“Agent 是怎么走到结果的，以及我们如何复盘它”。
- 介入点不同：有的是过程本身，有的是记录，有的是推理文本，有的是评价，有的是重放机制。
- 证据足够：相关概念卡已有 ReAct、Reflexion、LangSmith、Langfuse、OpenAI Agents SDK 等证据锚点。
- 现代工程价值高：能帮助区分调试、评估、审计、训练数据和回归测试的不同对象。

边界：这页是 ontology 对比页，不是观测平台使用教程。

## 共同问题域

共同问题是：Agent 不是一次性输出答案，而是经历目标、模型判断、工具调用、环境反馈、状态变化和最终输出。为了理解成功或失败，我们需要区分“发生了什么”“记录了什么”“模型说自己为什么这么做”“过程好不好”“能不能复现”。

```text
actual run -> trajectory
instrumentation -> trace
model text -> reasoning trace
judge/rubric -> trajectory evaluation
saved trace -> replay
```

## 核心区别表

| 类型 | 主要介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[Trajectory]] | 实际任务路径 | 任务执行全过程 | 用户目标、模型动作、工具结果、状态变化 | 一次成功/失败路径 | [[Trajectory#证据锚点]] |
| [[Trace]] | 对 trajectory 的系统记录 | 执行时同步记录，事后查看 | span、事件、tool call、observation、metadata | 可调试/可观测记录 | [[Trace#证据锚点]] |
| [[Reasoning Trace]] | 模型显式推理文字 | 行动前或行动中 | prompt、上下文、模型中间文本 | Thought / rationale / plan text | [[Reasoning Trace#证据锚点]] |
| [[Trajectory Evaluation]] | 对路径进行评分或判断 | 执行后或执行中评估 | trajectory、trace、rubric、judge | 过程质量、风险、成功/失败原因 | [[Trajectory Evaluation#证据锚点]] |
| [[Replay]] | 用保存记录复现过程 | 事后调试或回归测试 | trace、输入、环境快照、版本信息 | 可复现失败或对比修复结果 | [[Replay#证据锚点]] |

## 最容易混淆的边界

- [[Trajectory]] vs [[Trace]]：前者是任务路径本身，后者是路径的记录。没记录也发生过 trajectory；记录不完整也不等于 trajectory 不存在。
- [[Trajectory]] vs [[Reasoning Trace]]：trajectory 包含行动、观察、工具结果和状态变化；reasoning trace 只是显式推理文字。
- [[Trace]] vs [[Audit Log]]：trace 偏调试和观测，可能非常细；audit log 偏合规和关键动作留痕。
- [[Trace]] vs [[Evaluation]]：trace 记录发生了什么；evaluation 判断好不好。
- [[Trajectory Evaluation]] vs final answer evaluation：前者评价过程，后者只评价最终输出。
- [[Replay]] vs retry：replay 是复现或比较，不是简单重新跑一次。

## 执行时序 / 机制差异

```text
User goal
  -> model output / reasoning trace
  -> action / tool call
  -> observation / state change
  -> next action ...
  => trajectory

Runtime instrumentation records this as trace.
Evaluator scores trajectory / trace.
Replay uses saved trace and environment assumptions to reproduce or compare behavior.
```

这个时序说明：reasoning trace 可以成为 trajectory 的一部分，但它永远不是完整 trajectory。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文或官方文档证据。

把一次 Agent 任务想成“你从家出发去一家陌生餐厅吃饭”：

| Agent 概念 | 生活中的对应物 | 类比边界 |
|---|---|---|
| [[Trajectory]] | 你真实走过的路线：出门、换乘、走错路、问路、到店 | 实际发生，不依赖记录是否完整 |
| [[Trace]] | 手机定位、刷卡记录、聊天记录、付款记录 | 记录可能完整，也可能漏掉细节 |
| [[Reasoning Trace]] | 你一路上的自言自语：“这条路堵，我换另一条” | 显式想法不等于全部原因 |
| [[Trajectory Evaluation]] | 事后评价：是否准时、安全、绕路、花太多钱 | 是判断，不是记录本身 |
| [[Replay]] | 根据记录重新复盘哪里走错 | 依赖记录和环境可复现性 |

## 现代系统如何吸收或限制

### 来源支持的稳定部分

- [[Trajectory]] 和 [[Reflexion]] 相关证据支持：失败路径可以进入 evaluator，再生成 reflection / experience。
- [[Trace]] 相关证据支持：现代 observability 工具记录模型调用、工具调用、输入输出、成本、延迟和错误，供调试和评估。
- [[Trajectory Evaluation]] 相关证据支持：Agent 不能只看最终答案，还要看过程是否安全、合规、有效和经济。

### 工程综合 / inference

现代 Agent 系统通常会把 trace 当作“可观测事实层”，把 evaluation 当作“判断层”，把 replay 当作“回归验证层”。这三层可以互相依赖，但不能互相替代：没有 trace，evaluation 难以定位；没有 evaluation，trace 只是日志；没有 replay，修复是否有效很难证明。

## 什么时候用哪个判断

| 问题 | 更应该看哪个概念 | 为什么 | 风险 |
|---|---|---|---|
| 我想知道 Agent 到底怎么走到结果 | [[Trajectory]] | 关心完整路径和状态变化 | 不要只看模型文字 |
| 我想调试系统哪一步出错 | [[Trace]] | 需要输入、参数、工具结果、耗时、错误 | trace 可能采样或漏字段 |
| 我想理解模型显式说自己为什么这么做 | [[Reasoning Trace]] | 关心中间解释和计划文本 | 不等于模型真实内心，也不一定应暴露 |
| 我想判断过程是否安全有效 | [[Trajectory Evaluation]] | 需要对路径评分，而不只看最终答案 | judge/rubric 可能偏差 |
| 我想复现失败并验证修复 | [[Replay]] | 需要用保存记录重放或对比 | 环境不可复现会降低可信度 |

## 它们共同不是什么

- 都不是最终答案本身。
- 都不是模型真实内心的完整证明。
- 都不是单独的生产可靠性保证；需要权限、状态、测试、评估和 human-in-the-loop 配合。
- Trace / audit / replay 也不是同一件事：一个偏观测，一个偏合规，一个偏复现。

## 证据锚点

- Concept anchors: [[Trajectory#证据锚点]], [[Trace#证据锚点]], [[Reasoning Trace#证据锚点]], [[Trajectory Evaluation#证据锚点]], [[Replay#证据锚点]]
- Source examples: [[ReAct - Synergizing Reasoning and Acting in Language Models]], [[Reflexion - Language Agents with Verbal Reinforcement Learning]], [[LangSmith Evaluation and Observability]], [[Langfuse Observability and Evaluation]], [[OpenAI Agents SDK 文档]]
- Evidence type: concept-card synthesis + paper/docs source notes + engineering synthesis + learning analogy.
- Confidence: high for ontology boundary; medium for modern stack layering because具体工具实现会变化。
- Boundary: 类比只帮助理解，不是来源证据；不同框架对 trace / span / run / trajectory 的命名可能不同，需回到具体文档。

## 复习触发

1. 为什么 Reasoning Trace 不是完整 Trajectory？
2. Trace 能记录过程，为什么还需要 Trajectory Evaluation？
3. 一个 Agent 最终答对但越权访问数据，应该看 final answer evaluation 还是 trajectory evaluation？
4. Replay 为什么依赖 trace，却不等于 trace 本身？
5. 如果 trace 缺少 tool input，你还能完整评价 trajectory 吗？为什么？

## 相关链接

- [[Agent 主题]]
- [[Trajectory]]
- [[Trace]]
- [[Reasoning Trace]]
- [[Trajectory Evaluation]]
- [[Replay]]
- [[Observability]]
- [[Evaluation]]
- [[Audit Log]]
- [[Agent Loop]]
