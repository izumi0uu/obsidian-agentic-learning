---
type: concept
topic:
  - agent
  - evaluation
  - reproducibility
  - observability
status: growing
created: 2026-05-24
updated: 2026-05-24
last_checked: 2026-05-24
freshness: watch
conflicts: []
aliases:
  - agent rollout
  - rollout record
source:
  - "[[Rollout Cards - A Reproducibility Standard for Agent Research]]"
evidence:
  - "[[Rollout Cards - A Reproducibility Standard for Agent Research#需要我读的内容]]"
  - "[[Rollout Cards - A Reproducibility Standard for Agent Research#论文主张]]"
  - "[[Rollout Cards - A Reproducibility Standard for Agent Research#边界提醒]]"
related:
  - "[[Trajectory]]"
  - "[[Trace]]"
  - "[[Trajectory Evaluation]]"
  - "[[Replay]]"
  - "[[Eval Harness]]"
  - "[[Task Success Rate]]"
relations:
  - type: related_to
    target: "[[Trajectory]]"
    note: "Rollout 关注一次实际执行 episode / run；trajectory 关注这次执行中的路径序列。"
  - type: related_to
    target: "[[Trace]]"
    note: "Trace 是系统记录下来的过程数据；rollout record 要把一次执行的任务、环境、动作、状态、失败和元数据保存成可复用证据。"
  - type: related_to
    target: "[[Trajectory Evaluation]]"
    note: "Trajectory Evaluation 可以读取 rollout / rollout record 来判断过程质量，而不只看最终分数。"
  - type: related_to
    target: "[[Replay]]"
    note: "保存足够完整的 rollout record 后，后续才能 replay、re-score 或比较 reporting rule。"
---

# Rollout

## 一句话

Rollout 是 Agent 或强化学习系统在某个任务环境里实际跑出的一次 episode / run；在评测语境里，它通常是比最终分数更底层的过程证据单位。

## 概念详解

Rollout 出现的原因，是能行动的系统不能只用“最后答对没答对”来理解。Agent 会观察环境、调用工具、接收反馈、更新状态、处理错误，最后到达成功、失败、超时、取消或跳过等终止状态。把这一次完整执行保留下来，就是 rollout 进入评测和复现语境的价值。

在强化学习里，rollout 常指从当前 policy 采样出来的一条 episode / trajectory，用来估计回报、训练或评估。在 LLM Agent 里，它更常被当作一次 agent-environment interaction 的运行证据：环境配置、传给 Agent 的 observation、模型输出、tool call、tool result、状态变化、耗时、成本、失败类型和 terminal status 都可能属于这次 rollout。

这和 [[Trajectory]] 很接近，但侧重点不同。Trajectory 强调“路径本身”：状态、动作、观察、工具结果的序列。Rollout 强调“这一次实际跑出来的 episode / run”，通常绑定了模型、prompt、harness、环境、预算、随机性和报告规则。一个 rollout 可以包含一条 trajectory；一个 rollout record 则是把这次运行保存成可审计、可重算、可重放的记录对象。

[[Rollout Cards - A Reproducibility Standard for Agent Research]] 这类工作把问题推到更具体的一层：论文和 benchmark 如果只发布 headline score，而不保留 rollout records、reporting rules 和 drops manifest，后续读者就很难知道失败、报错、跳过、成本和计分规则如何影响最终结论。

## 它解决什么问题

Rollout 帮助把 Agent 评测从“报告一个分数”推进到“保存一次执行的证据”。这让人可以追问：

- 同一个任务是顺利完成、工具失败、超时，还是被跳过？
- 分数是从哪些字段算出来的，哪些字段被视图或 reporting rule 忽略了？
- 失败和错误有没有被计入总数，还是在报告前被丢掉了？
- 后续能不能基于同一批运行重新评分、重放或比较新的 evaluator？

没有 rollout / rollout record，很多 Agent 评测只能停留在结果表格，难以复现和审计。

## 它不是什么

Rollout 不是最终答案。最终答案只是一次 rollout 的可能输出之一。

Rollout 也不是 [[Reasoning Trace]]。显式推理文字可能是一次 rollout 的一部分，但 rollout 还包括 tool call、observation、environment state、错误、成本和终止状态。

Rollout 也不等于 [[Trace]]。Trace 偏“系统如何记录过程”；rollout 偏“这一次实际执行 episode / run”。当 trace 足够完整时，它可以成为 rollout record 的主要材料；当 trace 缺字段时，rollout 发生过，但可复用证据不足。

Rollout Card 也不是 Rollout 本身。Rollout 是一次运行；rollout card 是一种发布 / 复现 bundle，用来保存 rollout record、视图、报告规则和丢弃清单。

## 最小例子

一个 coding agent 修 bug：

```text
Task: 修复一个测试失败
-> read repo files
-> edit implementation
-> run tests
-> observe failure
-> edit again
-> run tests
-> terminal status: pass
```

这整次执行是一个 rollout。里面的动作和观察序列是 [[Trajectory]]。系统保存下来的 span、tool calls、test logs 和 metadata 是 [[Trace]]。如果记录还包含模型版本、prompt、repo commit、权限、预算、耗时、失败状态和报告规则，它就更接近可复现的 rollout record。

## 常见误解 / 风险

- 误解：rollout 就是 trajectory 的同义词。更准确地说，trajectory 是路径，rollout 是一次实际运行；rollout record 通常包含 trajectory 加运行配置和结果元数据。
- 误解：只保存成功 rollout 就够了。失败、错误、超时和跳过运行恰恰是评估鲁棒性、复现性和 reporting bias 的关键。
- 误解：多采样几次 rollout 一定更可靠。更多 rollout 可以提高覆盖和估计稳定性，但也会增加成本，并且如果环境、prompt、工具或 reporting rule 不透明，仍然难以复现。
- 风险：rollout record 可能包含敏感输入、工具返回、文件、网页状态或业务数据，需要脱敏、访问控制和 retention 策略。

## 边界细节

可以用这组关系记：

```text
Rollout = 一次实际执行 episode / run
Trajectory = 这次执行里的状态 / 动作 / 观察路径
Trace = 系统保存的过程记录
Rollout record = rollout 的可复用证据包
Rollout batch = 多个 rollouts，用来计算某个报告分数
Reporting rule = 把 rollout batch 的某个 view 转成分数的规则
Replay = 用保存记录复现或重新比较执行
```

在论文或训练配置里看到 `rollout n = 8`，通常是在说对每个任务或样本采样 8 条运行 / 轨迹，用于训练或评估。在 Agent evaluation 里，看到 rollout 更应该追问“它保存了哪些字段、失败是否可见、能否重新评分”。

## 现代性状态

- 判定：foundation / current-practice / frontier-adjacent。
- 为什么：rollout 是 RL 和交互式任务里的基础运行概念；在现代 LLM Agent 评测里，它正在被重新强调为复现、审计和过程评估的证据单位。
- 稳定部分：能行动的 Agent 不能只看最终分数，必须保存运行过程和终止状态。
- 易变部分：rollout record 的字段、平台 schema、隐私处理、公开发布规范和是否形成通用标准仍在演进。
- 复查点：当 rollout-card、trajectory evidence schema 或主流 eval/observability 平台出现稳定字段标准时更新。

## 现代系统怎么吸收 Rollout 的价值 / 局限

现代 Agent 系统可以把 rollout 接入三条闭环：

- 评测闭环：eval harness 运行一批 rollouts，保存成功、失败、错误、跳过和成本，然后用规则或 judge 评分。
- 复现闭环：保存 rollout record，让后续可以 replay、re-score 或比较不同 reporting rules。
- 训练 / 改进闭环：把高质量或失败的 rollouts 转成行为数据、反思样本、regression cases 或 robustness tests。

局限是成本和隐私。完整 rollout record 越可复现，通常越可能包含敏感数据和环境细节；过度压缩又会失去重算、重放和错误归因能力。因此工程上要明确：哪些字段必须保留，哪些字段只保留摘要，哪些字段需要脱敏或不落盘。

## 证据锚点

- Source: [[Rollout Cards - A Reproducibility Standard for Agent Research]]
- Anchor: [[Rollout Cards - A Reproducibility Standard for Agent Research#需要我读的内容]]
- Anchor: [[Rollout Cards - A Reproducibility Standard for Agent Research#论文主张]]
- Evidence type: paper source note + extracted paper definition + engineering synthesis.
- Confidence: medium-high for rollout / rollout record boundary; medium for rollout-card publication standard because source is 2026 arXiv / watch 状态。
- Boundary: 本卡沉淀 rollout 作为运行 / 评测证据单位；不声称 Rollout Cards 已成为行业统一标准。

## 复习触发

- Rollout、[[Trajectory]]、[[Trace]] 的最小区别是什么？
- 为什么只报告 task success rate 但不保留 rollout record，会让 Agent 评测难以复现？
- 一个失败 rollout 应该至少保存哪些字段，才能支持 replay 或重新评分？

## 相关链接

- [[Trajectory]]
- [[Trace]]
- [[Trajectory Evaluation]]
- [[Replay]]
- [[Eval Harness]]
- [[Task Success Rate]]
- [[Agent Robustness]]
- [[Agent Evaluation Benchmark]]
