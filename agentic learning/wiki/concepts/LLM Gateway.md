---
type: concept
topic:
  - llm
  - infrastructure
  - observability
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[LLM]]"
  - "[[Observability]]"
  - "[[Policy Engine]]"
  - "[[Evaluation]]"
---

# LLM Gateway

## 一句话

LLM Gateway 是统一管理模型调用的网关层，负责路由、重试、fallback、限流、成本、日志和供应商切换。

## 它解决什么问题

生产 Agent 往往不只调用一个模型。不同任务需要不同模型、价格、延迟、上下文长度和可用性。Gateway 把这些策略集中管理。

代表生态包括 LiteLLM、Portkey、OpenRouter、Vercel AI Gateway。

## 它不是什么

LLM Gateway 不是模型本身。

它也不能自动保证回答质量。它解决的是调用治理，不是推理正确性。

## 最小例子

```text
agent request -> gateway -> choose model -> retry/fallback -> log cost/latency -> return
```

## 常见误解和风险

- fallback 到弱模型可能改变行为。
- 日志里可能包含敏感 prompt。
- 多供应商路由需要处理数据合规和模型差异。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[Agent 工程基础设施主源]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[LLM]]
- [[Observability]]
- [[Policy Engine]]
- [[Evaluation]]
