---
type: concept
topic:
  - agent
  - evaluation
  - observability
status: seed
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

## 它解决什么问题

只看最终答案，很难知道 Agent 是怎么成功或失败的。Trajectory 把“怎么走到这里”的过程保留下来，让后续可以调试、复盘、评估、重放，或者像 [[Reflexion]] 那样把失败经验总结出来。

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
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Trace]]
- [[Trajectory Trace 类型对比]]
- [[Reasoning Trace]]
- [[Trajectory Evaluation]]
- [[Agent Loop]]
- [[Observation]]
- [[Reflexion]]
- [[Replay]]
