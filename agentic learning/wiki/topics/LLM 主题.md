---
type: map
topic:
  - llm
status: active
created: 2026-05-05
updated: 2026-05-10
related:
  - "[[LLM]]"
  - "[[Transformer]]"
  - "[[LLM 基础结构对比]]"
  - "[[Agent 知识地图]]"
---

# LLM 主题

这个主题页聚合所有 `topic` 包含 `llm` 的笔记。

## 概念卡

```dataview
TABLE status, updated, related
FROM "wiki/concepts"
WHERE contains(topic, "llm")
SORT file.name ASC
```

## 下一批概念

- [ ] Token
- [ ] context window
- [ ] prompt
- [ ] hallucination
- [ ] temperature

## 推理和提示

- [[Zero-shot CoT]]
- [[Plan-and-Solve Prompting]]
- [[Reasoning Trace]]

## Transformer 地基

- [[LLM 基础结构对比]]：先用一张边界页切开 Transformer、self-attention、multi-head attention 和 positional encoding。
- [[Transformer]]
- [[Self-Attention]]
- [[Multi-Head Attention]]
- [[Positional Encoding]]

## 训练和后训练

- [[LLM Training Pipeline]]
- [[Toolformer]]
- [[Scaling Laws for Neural Language Models]]
- [[Training Compute-Optimal Large Language Models]]
- [[Training Language Models to Follow Instructions with Human Feedback]]
- [[Constitutional AI - Harmlessness from AI Feedback]]
- [[DeepSeek-R1 - Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]]
- [[The Llama 3 Herd of Models]]

## 关键边界

LLM 是生成能力，Agent 是行动系统。学习 LLM 时先抓限制，再看 Agent 如何补足限制。

Transformer 是 LLM 的架构地基之一，但不是 Agent 能力本身。
