---
type: source
source_type: paper
title: "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection"
url: "https://arxiv.org/abs/2310.11511"
author: Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, Hannaneh Hajishirzi
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
  - "[[Self-RAG]]"
  - "[[RAG]]"
  - "[[Agentic Retrieval]]"
---

# Self-RAG - Learning to Retrieve Generate and Critique

## 为什么收

Self-RAG 是“模型自己判断是否检索、如何使用证据、如何批判生成内容”的经典 RAG 进化论文，虽然不是 2026 新论文，但仍是理解 agentic retrieval 和 self-reflective RAG 的基础概念。

## 一句话

Self-RAG 训练模型通过 reflection tokens 自适应地检索、生成和批判证据使用。

## 先读什么

- Abstract：为什么固定 top-k 检索不够。
- Method：retrieval token 和 critique token。
- Experiments：事实性、引用准确性和开放域 QA。

## 可以拆成概念卡

- [[Self-RAG]]
- [[Agentic Retrieval]]

## 我的疑问

- Self-RAG 的训练式方法和工程上的 LangGraph self-reflective RAG 有什么区别？
- reflection tokens 在闭源模型 API 场景里如何近似实现？

## 边界提醒

Self-RAG 不是简单“让模型反思一下”。它的核心是训练和控制信号，而不是在 prompt 里加一句自我检查。
