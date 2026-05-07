---
type: concept
topic:
  - security
  - agent
  - evaluation
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[OpenAI Agents SDK 文档]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[OpenAI Agents SDK 文档#为什么收]]"
related:
  - "[[Policy Engine]]"
  - "[[Approval Gate]]"
  - "[[Prompt Injection]]"
  - "[[Tool Permissioning]]"
---

# Guardrails

## 一句话

Guardrails 是限制、检查或修正模型输入、输出和工具动作的安全/质量边界。

## 它解决什么问题

Agent 可能输出不合规内容、误用工具、泄露数据、忽略格式、执行高风险动作。Guardrails 把部分规则放到模型调用前后或工具调用前后。

代表生态包括 NVIDIA NeMo Guardrails、OpenAI Agents SDK guardrails、Guardrails AI、Llama Guard 类模型。

## 它不是什么

Guardrails 不是绝对安全。

它也不是只写一句 system prompt。真实 guardrails 可能包括规则、分类器、schema validation、policy engine、人类审批和审计。

## 最小例子

```text
user input -> input guardrail -> agent -> tool call guardrail -> output guardrail -> response
```

## 常见误解和风险

- guardrail 本身也会误判。
- 只拦输出不拦工具动作，仍可能造成损害。
- 过严会让系统不可用，过松会形同虚设。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[OpenAI Agents SDK 文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Policy Engine]]
- [[Approval Gate]]
- [[Prompt Injection]]
- [[Tool Permissioning]]
