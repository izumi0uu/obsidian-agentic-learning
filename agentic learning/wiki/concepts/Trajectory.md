---
type: concept
topic:
  - agent
  - evaluation
  - observability
status: growing
created: 2026-05-10
updated: 2026-05-10
source:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models]]"
  - "[[Reflexion - Language Agents with Verbal Reinforcement Learning]]"
  - "[[LangSmith Evaluation and Observability]]"
evidence:
  - "[[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]]"
  - "[[Reflexion - Language Agents with Verbal Reinforcement Learning#Ingest 摘要]]"
  - "[[LangSmith Evaluation and Observability#为什么收]]"
last_checked: 2026-05-10
freshness: stable
conflicts: []
related:
  - "[[Trajectory Trace 类型对比]]"
  - "[[Trace]]"
  - "[[Reasoning Trace]]"
  - "[[Trajectory Evaluation]]"
  - "[[Agent Loop]]"
  - "[[Observation]]"
  - "[[Reflexion]]"
  - "[[Replay]]"
---

# Trajectory

## 一句话

Trajectory 是一次 Agent 任务从开始到结束走过的行动路径，包括中间状态、动作、观察、工具结果、推理痕迹和最终结果。

## 概念详解

Trajectory 是“过程本身”的概念。Agent 不只是一次输入一次输出，而是在环境里反复观察、判断、行动、读取反馈、修正方向。把这些步骤连起来，就是这次任务实际走过的路径。它可以成功，也可以失败；可以安全，也可以危险；可以高效，也可以绕远。

在 ReAct 中，trajectory 常表现为多轮 `Thought -> Action -> Observation`。在 Reflexion 中，trajectory 会被 evaluator 读取，生成 feedback，再进入 self-reflection 和 experience。到了现代 Agent 平台，trajectory 不一定暴露完整推理文本，但仍然包括 tool call、observation、state transition、error、retry、human approval、cost 和 final output。

它和 evaluation/observability 的关系很关键：[[Trace]] 是系统对 trajectory 的记录，[[Trajectory Evaluation]] 是对 trajectory 的质量判断，[[Replay]] 是尝试重现某条 trajectory 或它的关键条件。没有 trajectory，Agent 评测只能看最终答案；有 trajectory，才能讨论“过程是否可接受”。


学习 trajectory 时，最容易忽略的是“未记录不等于未发生”。Agent 真实做过的路径可能比 trace 里呈现的更丰富：有些内部状态、隐藏重试、被脱敏字段或外部环境变化没有被记录。评估时要记住，trajectory 是概念上的执行路径，trace 是可见证据，两者之间可能有缺口。

## 它解决什么问题

只看最终答案，很难知道 Agent 是怎么成功或失败的。Trajectory 把“怎么走到这里”的过程保留下来，让后续可以调试、复盘、评估、重放，或者像 [[Reflexion]] 那样把失败经验总结出来。

它还帮助区分不同失败类型：计划错、工具错、观察误读、环境变化、权限不足、恢复策略差，还是最终生成错。

## 它不是什么

Trajectory 不等于 [[Trace]]。

Trajectory 偏“真实发生过的任务路径”；Trace 偏“系统把这条路径记录下来的可观察数据”。可以粗略理解为：trajectory 是过程本身，trace 是过程的记录。

Trajectory 也不等于 [[Reasoning Trace]]。Reasoning Trace 只关注模型显式写出的推理文字；trajectory 还包括工具调用、外部 [[Observation]]、环境状态变化、错误、重试、成本和最终输出。

## 最小例子

```text
User asks task
-> LLM decides to search
-> Tool call: search(query)
-> Observation: search results
-> LLM decides to open one page
-> Tool call: browser.open(url)
-> Observation: page content
-> LLM generates answer
-> Final result
```

这整条路径是 trajectory；系统把每一步保存成结构化记录，就是 [[Trace]]；其中 LLM 写出的“我为什么要搜索/打开页面”的文字，才是 [[Reasoning Trace]]。

## 常见误解

不要把 trajectory 只理解成 chain-of-thought。很多现代系统不会暴露完整推理文本，但仍然可以记录工具调用、状态变化、输入输出和结果，从而形成可评价的 trajectory。

也不要把“有 trajectory”理解成“质量一定可评估”。trajectory 只是过程材料，真正判断好坏还需要 [[Trajectory Evaluation]]、规则、人工审查或 LLM-as-judge。

## 边界细节

三者可以这样区分：

```text
Trajectory: 任务执行路径本身
Trace: 对这条路径的记录和观测数据
Reasoning Trace: 路径中模型显式推理文字的那一部分
```

在 [[ReAct]] 里，一条 trajectory 往往由多轮 `Thought -> Action -> Observation` 组成；在 [[Reflexion]] 里，trajectory 会进入 evaluator，产生 feedback，再被 self-reflection 总结成经验。

Evaluation harness 需要的不是“trajectory 这个词”，而是可读取的过程材料：动作、观察、结果、错误、权限、成本和时间。如果这些材料没有被 trace 捕获，trajectory evaluation 就只能停留在人工回忆。

## 现代性状态

- 判定：foundation / current-practice。
- 为什么：trajectory 是 ReAct、Reflexion 等 Agent 论文里的基础过程概念；现代 Agent 平台继续用它支撑 trace、replay、evaluation 和 memory。
- 稳定部分：Agent 的质量不能只看最终答案，还要看执行路径。
- 易变部分：平台如何记录、压缩、展示或隐藏 trajectory 细节会变化，尤其是 reasoning trace 和隐私字段。

## 现代系统怎么使用 Trajectory

现代 Agent 系统通常会把 trajectory 用在几个地方：

- 调试：定位失败发生在计划、工具、检索、权限还是环境反馈。
- 评测：用 [[Trajectory Evaluation]] 判断过程是否安全、合规、低成本，而不是只看最终答案。
- 重放：用 [[Replay]] 复现失败路径，减少“线上偶发问题无法解释”。
- 记忆：把有价值的任务轨迹提炼成 [[Episodic Memory]] 或 Reflexion 里的 experience。
- 训练：把高质量工具使用轨迹作为行为克隆、SFT 或 agent 能力训练的数据。

## 证据锚点

- Source: [[ReAct - Synergizing Reasoning and Acting in Language Models]]
- Source: [[Reflexion - Language Agents with Verbal Reinforcement Learning]]
- Source: [[LangSmith Evaluation and Observability]]
- Anchor: [[ReAct - Synergizing Reasoning and Acting in Language Models#为什么收]] / [[Reflexion - Language Agents with Verbal Reinforcement Learning#Ingest 摘要]] / [[LangSmith Evaluation and Observability#为什么收]]
- Evidence type: paper/source notes + Agent evaluation synthesis.
- Confidence: medium
- Boundary: trajectory 是过程本身；可观察程度取决于 trace/harness，而不是概念自动保证。

## 复习触发

- 为什么 Trajectory 不是 [[Trace]]？
- 用 ReAct 的 `Thought -> Action -> Observation` 说明 trajectory、trace、reasoning trace 的区别。
- 一个最终成功但 trajectory 不合格的 Agent 例子是什么？

## 相关链接

- [[Trace]]
- [[Trajectory Trace 类型对比]]
- [[Reasoning Trace]]
- [[Trajectory Evaluation]]
- [[Agent Loop]]
- [[Observation]]
- [[Reflexion]]
- [[Replay]]
