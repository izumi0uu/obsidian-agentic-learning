---
type: source
source_type: article
title: "Context Rot: How Increasing Input Tokens Impacts LLM Performance"
url: https://www.trychroma.com/research/context-rot
author:
  - Kelly Hong
  - Anton Troynikov
  - Jeff Huber
site: Chroma
topic:
  - llm
  - context
  - long-context
  - evaluation
created: 2026-05-18
updated: 2026-05-18
last_checked: 2026-05-18
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Context Rot]]"
  - "[[Context Window]]"
  - "[[Context Engineering]]"
  - "[[Long-Horizon Context Engineering]]"
  - "[[LLM 上下文限制与突破条件]]"
---

# Chroma - Context Rot 技术报告

## 为什么收

这份 Chroma research report 给 [[Context Rot]] 提供了一个明确 evidence anchor：长上下文问题不只是“窗口够不够大”，还包括输入变长、噪声变多、干扰项接近任务时，模型是否还能稳定使用上下文。

学习价值在于补齐 [[Context Window]] 的反面边界：窗口变大只是容量改善，不等于模型会均匀、可靠、同等优先级地处理窗口里的所有 token。它也能支撑 [[Context Engineering]]、[[GSSC Pipeline]] 和 [[Long-Horizon Context Engineering]] 为什么仍然需要筛选、排序、结构化、压缩和证据治理。

## 一句话

Chroma 把 Context Rot 描述成一种长输入可靠性退化现象：随着输入 token 增加，模型在简单任务和长记忆评测上的表现会变得更不稳定，说明长窗口不是上下文质量保证。

## 报告主张

- 报告挑战了“模型能均匀处理上下文中任意位置 token”的默认假设。
- Chroma 评估了 18 个 LLM，覆盖 GPT-4.1、Claude 4、Gemini 2.5、Qwen3 等模型族。
- 主要结论是：模型并不会统一地使用整个上下文；输入长度增加后，性能和可靠性会出现明显波动。
- 这个问题不只发生在复杂 reasoning 中；报告强调即使是简单任务，也可能随输入长度和干扰条件变化而失稳。

## 实验 / 证据

- Needle in a Haystack 扩展：检查模型能否在长 haystack 中找出 needle，并分析 needle-question similarity、distractor、haystack structure 等因素。
- LongMemEval：用更接近长期记忆/长上下文问答的任务观察不同模型家族在长输入中的稳定性。
- Repeated Words：用看似简单的重复词计数/定位类任务测试模型在长序列中的位置和计数稳定性。
- LLM judge alignment：报告使用 LLM judge 评估 NIAH 和 LongMemEval 输出，并用人工标注子集校准 judge 与人类判断的一致性。
- Models Tested：报告列出 Anthropic、OpenAI、Google、Alibaba 模型族；同时说明不是每个模型都能进入每个实验，受 context window 或 thinking budget 等约束影响。

## 可以拆成概念卡

- [[Context Rot]]
- long-context reliability
- long-context evaluation
- Needle in a Haystack extensions
- distractor sensitivity

## 边界提醒

这是一份 Chroma technical report / research report，不是同行评审论文。它足以支撑 `Context Rot` 作为 watch 状态概念卡，但后续如果术语在论文、官方 benchmark 或主流框架中形成不同定义，需要复查命名和边界。

`Context Rot` 不应被泛化成所有“模型变差”。它特指上下文输入变长、噪声/干扰项增加或结构不佳时，模型对已在窗口内信息的使用质量下降。模型训练退化、memory 持续更新退化、RAG 索引质量下降和服务端性能下降都只是相邻问题。

## 需要我读的内容

1. 先读 Introduction / Related Work，理解报告为什么把问题命名为 Context Rot。
2. 再看 Needle in a Haystack Extension，尤其是 distractor 和 similarity 对结果的影响。
3. 再看 LongMemEval 和 Repeated Words，区分真实长记忆任务和简单序列任务里的退化形态。
4. 最后看 Limitations / Future Work 和 Models Tested，避免把这份报告过度外推成所有模型的稳定结论。

## 引用信息

```bibtex
@techreport{hong2025context,
  title = {Context Rot: How Increasing Input Tokens Impacts LLM Performance},
  author = {Hong, Kelly and Troynikov, Anton and Huber, Jeff},
  year = {2025},
  month = {July},
  institution = {Chroma},
  url = {https://trychroma.com/research/context-rot},
}
```
