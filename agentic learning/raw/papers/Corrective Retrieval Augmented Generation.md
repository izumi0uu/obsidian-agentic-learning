---
type: source
source_type: paper
title: "Corrective Retrieval Augmented Generation"
url: "https://arxiv.org/abs/2401.15884"
author: Shi-Qi Yan, Jia-Chen Gu, Yun Zhu, Zhen-Hua Ling
site: arxiv.org
topic:
  - rag
  - evaluation
  - frontier
created: 2026-05-06
updated: 2026-05-07
last_checked: 2026-05-07
freshness: stable
conflicts: []
status: seed
source:
related:
  - "[[Corrective RAG]]"
  - "[[RAG]]"
  - "[[Retriever]]"
---

# Corrective Retrieval Augmented Generation

## 为什么收

CRAG 是“检索结果不可靠时怎么办”的代表方法。它把 retrieval evaluator、重检索、web search fallback 和 decompose/recompose 连接起来，适合理解 RAG 可靠性。

## 一句话

Corrective RAG 先评估检索质量，再决定直接生成、修正检索或扩展检索。

## 先读什么

- Abstract：RAG 对检索质量的依赖。
- Retrieval evaluator：如何判断文档质量。
- Corrective actions：低置信度时如何触发补救。

## 可以拆成概念卡

- [[Corrective RAG]]
- [[Retriever]]
- [[Evaluation]]

## 我的疑问

- retrieval evaluator 应该是小模型、规则、还是 LLM-as-judge？
- web fallback 在企业私有知识库场景是否安全？

## 边界提醒

Corrective RAG 不是“多检索几次”。它的核心是检索质量评估和基于置信度的分支动作。
