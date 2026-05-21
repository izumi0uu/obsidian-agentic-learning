---
type: concept
topic:
  - agent
  - evaluation
  - reliability
  - security
status: growing
created: 2026-05-17
updated: 2026-05-18
last_checked: 2026-05-18
freshness: watch
conflicts: []
aliases:
  - Agent 鲁棒性
  - Agent 稳健性
  - 智能体鲁棒性
  - 智能体稳健性
  - Agentic Robustness
  - Robustness of Planning and Reasoning
  - 规划与推理的鲁棒性
  - Agent 鲁棒性指标
  - 智能体鲁棒性指标
source:
  - "[[raw/repos/agent_java_offer/questions/176 01_AI 06_评测与监控 在评估一个 Agent 的任务完成情况时，除了最终结果的正确性，还有哪些过程指标是值得关注的？（例如：效率、成本、鲁棒性）]]"
  - "[[raw/repos/agent_java_offer/questions/174 01_AI 06_评测与监控 你了解哪些专门用于评估 Agent 能力的基准测试？这些基准通常如何构建测试环境和任务？]]"
  - "[[raw/repos/agent_java_offer/questions/183 01_AI 06_评测与监控 还有一个是鲁棒性层面的指标。就是说系统在调用工具，工具会出现一些异常超时或者返回信息不符合预期的时候，系统会怎么样？思考推理进行下一步的动作。以及当外界条件出现一些噪声的时 7c989c]]"
  - "[[Beyond Cooperative Simulators - Generating Realistic User Personas for Robust Evaluation of LLM Agents]]"
  - "[[Rollout Cards - A Reproducibility Standard for Agent Research]]"
evidence:
  - "[[raw/repos/agent_java_offer/questions/176 01_AI 06_评测与监控 在评估一个 Agent 的任务完成情况时，除了最终结果的正确性，还有哪些过程指标是值得关注的？（例如：效率、成本、鲁棒性）#题目正文]]"
  - "[[raw/repos/agent_java_offer/questions/174 01_AI 06_评测与监控 你了解哪些专门用于评估 Agent 能力的基准测试？这些基准通常如何构建测试环境和任务？#题目正文]]"
  - "[[raw/repos/agent_java_offer/questions/183 01_AI 06_评测与监控 还有一个是鲁棒性层面的指标。就是说系统在调用工具，工具会出现一些异常超时或者返回信息不符合预期的时候，系统会怎么样？思考推理进行下一步的动作。以及当外界条件出现一些噪声的时 7c989c#题目正文]]"
  - "[[Beyond Cooperative Simulators - Generating Realistic User Personas for Robust Evaluation of LLM Agents#为什么收]]"
  - "[[Beyond Cooperative Simulators - Generating Realistic User Personas for Robust Evaluation of LLM Agents#论文主张]]"
  - "[[Rollout Cards - A Reproducibility Standard for Agent Research#为什么收]]"
related:
  - "[[Evaluation]]"
  - "[[Task Success Rate]]"
  - "[[Trajectory Evaluation]]"
  - "[[Trace]]"
  - "[[Guardrails]]"
  - "[[Tool Calling]]"
relations:
  - type: related_to
    target: "[[Task Success Rate]]"
    note: Agent Robustness 常用扰动条件下的成功率下降幅度来观察；Task Success Rate 是被观察指标，不是鲁棒性本身。
  - type: related_to
    target: "[[Trajectory Evaluation]]"
    note: 工具超时、异常返回、噪声输入和恢复动作都需要看 trajectory，而不只看最终输出。
  - type: related_to
    target: "[[Guardrails]]"
    note: Guardrails 可以提高部分扰动下的可控性，但安全拦截机制不等于鲁棒性指标。
---

# Agent Robustness

## 一句话

Agent Robustness 是 Agent 在工具失败、观察噪声、用户行为变化、检索污染、计划偏离或攻击性输入下，仍能保持可接受任务推进、恢复策略和安全边界的系统级稳健性。

## 概念详解

Agent Robustness 不是在问“这次任务有没有成功”，而是在问“条件变坏之后，系统表现下降得多快、能不能恢复、会不会为了成功越界”。一个 Agent 平时能完成任务，但工具一超时就陷入循环，网页返回格式稍变就读错 observation，用户表达不耐烦就放弃澄清，检索里混进旧资料就照单全收，这些都说明它的 robustness 不够。

它是系统级概念。普通模型鲁棒性常看模型对 prompt 格式、选项顺序、扰动样本或对抗输入是否稳定；Agent Robustness 还要覆盖 loop、tool、state、memory、retrieval、permission、fallback、human escalation 和 trace/eval。模型更强只能改善一部分，不能自动解决工具超时、幂等、回滚、权限和可复现评测。

从评测角度看，Agent Robustness 通常要用“正常集 + 扰动集”观察，而不是只看一个总分。扰动集可以包括工具 5xx/timeout、空检索、低质量网页、噪声 observation、用户突然改目标、恶意 prompt injection、长尾任务、环境状态变化、第三方 API 返回 schema 漂移。关键不是扰动越多越好，而是每类扰动都能对应一个清楚问题：系统应该重试、换工具、重新规划、拒绝、降级、升级给人类，还是停止。

一个容易忽略的细节：鲁棒性更像“指标曲线的斜率”，不是单点指标。两个 Agent 正常任务成功率都 80%，但 A 在工具超时注入后降到 75%，B 降到 30%，它们的 [[Task Success Rate]] 正常值相同，Agent Robustness 完全不同。

## 它解决什么问题

它解决的是 Agent 上线前后最难被 demo 看出来的问题：系统遇到局部失败和分布变化时会怎样。

- 工具失败：timeout、限流、返回空值、schema 变化、权限错误。
- 环境噪声：网页加载失败、检索命中旧资料、观察里夹杂无关信息。
- 用户变化：用户表达含糊、不配合、插入新约束或中途改目标。
- 安全扰动：prompt injection、越权请求、工具滥用、敏感数据诱导。
- 长任务漂移：计划跑偏、循环、过早宣称完成、恢复后状态不一致。

## 它不是什么

Agent Robustness 不是宽泛的“可靠性”同义词。可靠性可以包括可用性、SLA、监控、部署稳定、数据一致性；Agent Robustness 更聚焦 Agent 行为在扰动和异常下是否稳定、可恢复、可控。

它也不是安全性或 [[Guardrails]] 的替代词。安全测试和红队可以构成 robustness 测试的一部分，但鲁棒性还包括非恶意失败，例如工具超时、网页格式变化、用户表达不清和检索噪声。

它也不是 [[Task Success Rate]]。成功率是结果指标；Agent Robustness 看的是成功率、成本、错误恢复、权限违规、人工接管等指标在压力条件下是否保持稳定。

它也不是“多加 retry”。重试只能处理部分瞬时故障；如果参数错、权限错、工具语义错或状态已经污染，盲目重试会放大成本和副作用。

## 最小例子

一个订票 Agent 在正常环境下 100 个任务成功 80 个：

```text
normal set:        80 / 100 success
tool-timeout set:  72 / 100 success
noisy-user set:    68 / 100 success
injection set:     20 / 100 safe success
```

这里不能只报告“正常成功率 80%”。如果 injection set 下大量越权或错误执行，即使最终订到了票，也说明 Agent Robustness 和 safety trajectory eval 都失败。

## 常见误解 / 风险

- 误解：模型能力强，Agent 就自然鲁棒。风险是忽略工具、状态、权限、回滚和环境的系统问题。
- 误解：只要最终成功，就算鲁棒。风险是靠偶然路径、无限重试、越权工具或人工兜底把成功率撑高。
- 误解：鲁棒性只靠线上监控。风险是线上才发现长尾失败，已经产生副作用；离线必须有故障样本和回归集。
- 风险：扰动集设计得太“玩具化”。如果只改几个字，不模拟真实工具失败、用户行为和外部环境变化，结果会虚高。
- 风险：把裸 `鲁棒性 / Robustness` 全部映射到本卡。模型鲁棒性、RAG 鲁棒性、benchmark robustness 和 Agent Robustness 相邻但不等价。
- 术语边界：裸 `Robustness`、`鲁棒性`、`稳健性` 只有在上下文明确是 Agent 系统、工具异常、trajectory、评估扰动或任务成功率稳定性时才指向本卡；否则先保留为原文术语或写入待判定队列。

## 边界细节

Agent Robustness 至少要拆成四层看：

1. 输入扰动：用户表达、恶意内容、检索噪声、上下文污染。
2. 执行扰动：工具超时、错误码、schema 漂移、权限不足、环境变化。
3. 状态扰动：计划偏离、重复循环、恢复后 state 不一致、memory 污染。
4. 评测扰动：用户模拟器过于合作、只报告成功 rollouts、跳过失败或 errored runs。

和相邻概念的边界：

- [[Evaluation]]：定义怎么测；Agent Robustness 是被测的系统性质之一。
- [[Trajectory Evaluation]]：提供过程证据；Agent Robustness 需要它来判断恢复、回退、停止和越权。
- [[Task Success Rate]]：提供结果信号；Agent Robustness 看结果信号在扰动下的稳定性。
- [[Observability]] / [[Trace]]：记录发生了什么；它们不是鲁棒性本身。
- [[Guardrails]]：运行时控制点；它能提升安全扰动下的表现，但不是唯一机制。

## 现代性状态

- 判定：current-practice / frontier-adjacent。
- 为什么：生产 Agent 已经普遍需要故障注入、回归评测、trace、guardrails、human escalation 和线上 bad-case 回流；但“Agent robustness”作为统一指标体系仍在快速演化，尤其是用户模拟、rollout 记录、过程评分和安全压力测试。
- 稳定部分：Agent 不能只看正常任务成功率；必须看异常、噪声和分布变化下的表现。
- 易变部分：具体 benchmark、扰动集、用户模拟器、trajectory evaluator、平台字段和行业标准。
- 复查点：当 Agent evaluation benchmark、rollout 标准、红队框架或主流 Agent 平台出现稳定 robustness 指标时更新。

## 现代系统怎么吸收 Agent Robustness 的价值 / 局限

现代系统通常用组合机制吸收这个概念：

- 离线：建立正常集、边界集、故障集、攻击集和回归集，比较版本间退化。
- 运行时：对工具调用加 timeout、幂等、错误分类、fallback、policy、approval gate 和状态恢复。
- 观测：保存 trace、tool result、error type、retry、human escalation、cost、latency 和最终 outcome。
- 复盘：把线上 bad case 回流成 regression case，不让同类失败反复出现。
- 发布：让高风险改动必须通过扰动集，而不只通过 happy path。

局限是：鲁棒性永远只能相对于某个扰动分布成立。没有覆盖到的真实变化仍可能让系统失效；因此它不是“一劳永逸的保证”，而是一套持续扩充故障样本和评测协议的工程习惯。

## 证据锚点

- Interview evidence: [[raw/repos/agent_java_offer/questions/176 01_AI 06_评测与监控 在评估一个 Agent 的任务完成情况时，除了最终结果的正确性，还有哪些过程指标是值得关注的？（例如：效率、成本、鲁棒性）#题目正文]] 把鲁棒性列为 Agent 过程指标，并举工具错误、网页失败、噪声信息下成功率下降。
- Interview evidence: [[raw/repos/agent_java_offer/questions/183 01_AI 06_评测与监控 还有一个是鲁棒性层面的指标。就是说系统在调用工具，工具会出现一些异常超时或者返回信息不符合预期的时候，系统会怎么样？思考推理进行下一步的动作。以及当外界条件出现一些噪声的时 7c989c#题目正文]] 直接提出工具异常、超时、返回不符预期和外界噪声下成功率是否稳定。
- Interview evidence: [[raw/repos/agent_java_offer/questions/174 01_AI 06_评测与监控 你了解哪些专门用于评估 Agent 能力的基准测试？这些基准通常如何构建测试环境和任务？#题目正文]] 把可复现交互式 benchmark 的价值扩展到规划、工具使用和鲁棒性，而不只看最终文本质量。
- Paper source: [[Beyond Cooperative Simulators - Generating Realistic User Personas for Robust Evaluation of LLM Agents#为什么收]] 支持“合作型模拟用户会高估真实部署稳健性”的评测分布边界。
- Paper source: [[Rollout Cards - A Reproducibility Standard for Agent Research#为什么收]] 支持“不能只看 headline score，需要 rollout record 暴露失败、错误和跳过运行”的过程证据边界。
- Evidence type: interview raw source + paper source note + engineering synthesis.
- Confidence: medium-high for Agent evaluation boundary; medium for frontier paper generalization because相关论文仍是 2026 arXiv / watch 状态。
- Boundary: 本卡沉淀 Agent 系统级鲁棒性；不把所有 `robustness / 鲁棒性` 命中都当作本卡别名。

## 复习触发

- 为什么两个 Agent 正常 [[Task Success Rate]] 相同，Agent Robustness 可能完全不同？
- 给一个“最终成功但鲁棒性失败”的 trajectory 例子。
- 工具 timeout、schema 漂移、用户不配合、prompt injection 分别应该触发什么恢复策略？
- 为什么 cooperative simulator 会高估 Agent Robustness？

## 相关链接

- [[Evaluation]]
- [[Task Success Rate]]
- [[Trajectory Evaluation]]
- [[Trace]]
- [[Observability]]
- [[Guardrails]]
- [[Tool Calling]]
- [[Tool Permissioning]]
