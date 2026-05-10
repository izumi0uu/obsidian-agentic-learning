---
type: concept
topic:
  - evaluation
  - agent
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[LangSmith Evaluation and Observability]]"
  - "[[OpenAI Agents SDK 文档]]"
evidence:
  - "[[LangSmith Evaluation and Observability#为什么收]]"
  - "[[LangSmith Evaluation and Observability#先读什么]]"
  - "[[LangSmith Evaluation and Observability#边界提醒]]"
  - "[[OpenAI Agents SDK 文档#Tracing 补充]]"
related:
  - "[[Evaluation]]"
  - "[[Trajectory]]"
  - "[[Trace]]"
  - "[[Eval Harness]]"
  - "[[Agent Loop]]"
  - "[[LLM-as-Judge]]"
  - "[[Approval Gate]]"
---

# Trajectory Evaluation

## 一句话

Trajectory Evaluation 是评价 Agent 的行动轨迹，而不是只评价最终答案：它关心过程是否安全、有效、合规、经济、可恢复。

## 它解决什么问题

Agent 最终答对了，也可能过程危险、成本过高、调用了不该用的工具、泄露了数据，或者靠偶然路径成功。只看 final answer 会漏掉这些风险。

Trajectory Evaluation 把“怎么做到的”纳入评估：工具顺序是否合理，检索是否必要，是否遵守权限，是否在高风险动作前请求确认，是否在失败后停止或求助。这对能行动的 Agent 比对普通问答更重要。

## 它不是什么

它不是 chain-of-thought 打分。Trajectory 包括工具调用、观察、检索、环境状态、动作顺序和中间结果，不只是模型显式写出的推理文本。

它也不是 [[Trace]] 本身。Trace 记录过程；Trajectory Evaluation 判断这条 [[Trajectory]] 是否安全、有效、合规、经济。

它也不是只靠 [[LLM-as-Judge]] 的主观评分。LLM judge 可以辅助，但高风险动作、权限、隐私和成本往往需要规则、人审或业务指标一起判断。

## 最小例子

评估一个订票 Agent：

- 最终是否找到合适票。
- 是否访问了允许的网站。
- 是否在付款前请求确认。
- 是否避免读取无关个人信息。
- 是否在失败时退出或求助。
- 是否没有为了成功而绕过预算、时间或安全约束。

如果它最后订到了票，但没有付款确认，这条 trajectory 仍然应该判为失败或高风险。

## 常见误解 / 风险

- 误解：最终答案正确就代表轨迹正确。对于 Agent，过程可能违反权限、泄露数据或产生不可接受副作用。
- 误解：有 trace 就自动完成 trajectory evaluation。trace 只是材料，还要有 rubric、规则、judge、人审或业务指标。
- 风险：轨迹里可能含敏感数据，不能直接丢给外部 judge。
- 风险：只设计“成功路径”评测，会漏掉工具失败、检索为空、人类拒绝、权限不足等真实场景。

## 边界细节

Trajectory Evaluation 至少要切开三层：

1. [[Trajectory]]：Agent 实际走过的路径。
2. [[Trace]]：系统记录下来的路径证据。
3. Evaluation：对这条路径做判断的规则、rubric、judge 或人工 review。

它和普通 output evaluation 的区别：output evaluation 看最终答案；trajectory evaluation 看路径是否可接受。两者都需要，不能互相替代。

它和 [[Approval Gate]] 的关系：approval gate 是运行时阻断/确认机制；trajectory evaluation 可以在事后检查是否应该触发 gate、是否真的触发了、用户是否确认。

## 现代性状态

- 判定：current-practice / frontier-adjacent
- 为什么：Agent/RAG 平台已经把 trace、dataset、evaluator、online/offline evaluation 连接起来；但 trajectory evaluator 的最佳 rubric、隐私处理和自动化程度仍在演进。
- 稳定部分：过程评价必须依赖 trace/trajectory 材料，并和最终答案评价互补。
- 易变部分：平台 evaluator 类型、judge prompt、score schema、在线监控能力和隐私策略。
- 复查点：当主流 eval 平台对 trajectory evaluator、agent evaluator 或 process supervision 有新稳定抽象时更新。

## 现代系统怎么吸收 Trajectory Evaluation 的价值 / 局限

现代系统通常把它做成评测闭环：

- tracing 平台收集 trajectory 证据。
- eval harness 把代表性成功/失败轨迹组织成 dataset。
- evaluator 用规则、代码、LLM judge 或人工 review 打分。
- regression 测试检查新 prompt、模型、工具或工作流是否引入更差路径。
- 对高风险动作，把评估发现反推到 guardrails、approval gate 和 tool permissioning。

局限是：trajectory evaluation 更贵、更复杂，也更容易碰到隐私问题。因此不一定每条线上请求都完整评估，常见做法是抽样、规则先筛、高风险场景重点评估。

## 证据锚点

- Source: [[LangSmith Evaluation and Observability]]
- Anchor: [[LangSmith Evaluation and Observability#为什么收]] / [[LangSmith Evaluation and Observability#先读什么]] / [[LangSmith Evaluation and Observability#边界提醒]]
- Source: [[OpenAI Agents SDK 文档]]
- Anchor: [[OpenAI Agents SDK 文档#Tracing 补充]]
- Evidence type: official docs/source notes + engineering synthesis.
- Confidence: medium
- Boundary: 具体 evaluator 名称和平台能力会变化；“过程也要被评估”是本卡的稳定核心。

## 复习触发

- 给一个“最终答对但轨迹失败”的 Agent 例子。
- 解释 [[Trace]]、[[Trajectory]]、[[Trajectory Evaluation]] 三者的关系。
- 什么时候应该用规则评估轨迹，什么时候可以用 LLM-as-judge，什么时候必须人工 review？

## 相关链接

- [[Trace]]
- [[Trajectory]]
- [[Evaluation]]
- [[Eval Harness]]
- [[Agent Loop]]
- [[LLM-as-Judge]]
- [[Approval Gate]]
