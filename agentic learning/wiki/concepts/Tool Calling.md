---
type: concept
topic:
  - agent
  - llm
status: seed
created: 2026-05-05
updated: 2026-05-05
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Toolformer]]"
evidence:
  - "[[Toolformer#为什么收]]"
related:
  - "[[Agent]]"
  - "[[Agent Loop]]"
  - "[[Evaluation]]"
  - "[[Tool Use]]"
---

# Tool Calling

## 一句话

Tool Calling 是让模型输出结构化请求，由外部工具完成查询、计算、读写文件或调用 API。

## 它解决什么问题

LLM 只靠生成文本无法真正访问实时信息、运行代码或修改环境。工具调用让模型可以把一部分工作交给可靠的外部系统。

[[Toolformer]] 把工具使用推进成一种模型能力问题：模型不仅要会发出工具调用，还要知道什么时候调用、传什么参数、如何利用返回结果。

## 它不是什么

Tool Calling 不是 Agent 本身。它是 Agent 可以使用的一种能力。

会调用天气 API 的聊天机器人，不一定能自主规划旅行、比较航班、检查预算并提醒用户确认付款。

## 最小例子

用户问：“今天上海天气怎么样？”

模型不直接猜答案，而是请求调用天气工具。工具返回结果后，模型再把结果解释给用户。

## 设计边界

工具越强，权限越需要清晰。读文件、写文件、发邮件、付款、删除数据这类动作应该有不同的确认策略。

## Tool Use 视角

[[Tool Use]] 更偏“行为能力”，Tool Calling 更偏“接口形式”。一个系统可以有 tool calling API，但仍然不会可靠地使用工具。

## 证据锚点

- Source: [[Toolformer]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent]]
- [[Agent Loop]]
- [[Evaluation]]
- [[Tool Use]]
