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
freshness: stable
conflicts: []
source:
  - "[[LangSmith Evaluation and Observability]]"
  - "[[OpenAI Agents SDK 文档]]"
evidence:
  - "[[LangSmith Evaluation and Observability#为什么收]]"
  - "[[OpenAI Agents SDK 文档#为什么收]]"
related:
  - "[[Evaluation]]"
  - "[[Trajectory]]"
  - "[[Trace]]"
  - "[[Eval Harness]]"
  - "[[Agent Loop]]"
---

# Trajectory Evaluation

## 一句话

Trajectory Evaluation 是评价 Agent 的行动轨迹，而不是只评价最终答案。

## 它解决什么问题

Agent 最终答对了，也可能过程危险、成本过高、调用了不该用的工具、泄露了数据，或者靠偶然路径成功。Trajectory Evaluation 让过程也进入评分。

## 它不是什么

它不是 chain-of-thought 打分。

Trajectory 包括工具调用、观察、检索、环境状态、动作顺序和中间结果，不只是模型显式写出的推理文本。

它也不是 [[Trace]] 本身。Trace 记录过程；[[Trajectory Evaluation]] 判断这条 [[Trajectory]] 是否安全、有效、合规、经济。

## 最小例子

评估一个订票 Agent：

- 最终是否找到合适票。
- 是否访问了允许的网站。
- 是否在付款前请求确认。
- 是否避免读取无关个人信息。
- 是否在失败时退出或求助。

## 常见误解 / 风险 / 边界细节

- 过程评价需要 trace 支持。
- LLM-as-judge 可以辅助，但不能替代规则和人工审查。
- 有些轨迹包含敏感数据，不能随意外发给评估模型。
- 轨迹好不代表最终结果一定好，两者都要看。

## 证据锚点

- Source: [[LangSmith Evaluation and Observability]]
- Source: [[OpenAI Agents SDK 文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Trace]]
- [[Trajectory]]
- [[Evaluation]]
- [[Eval Harness]]
- [[Approval Gate]]
