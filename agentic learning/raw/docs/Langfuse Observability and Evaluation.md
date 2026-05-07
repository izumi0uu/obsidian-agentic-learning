---
type: source
source_type: docs
title: "Langfuse Overview"
url: "https://langfuse.com/docs"
author: Langfuse
site: langfuse.com
topic:
  - evaluation
  - observability
  - frontier
created: 2026-05-06
updated: 2026-05-07
last_checked: 2026-05-07
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Observability]]"
  - "[[Trace]]"
  - "[[LLM-as-Judge]]"
---

# Langfuse Observability and Evaluation

## 为什么收

Langfuse 是开源 LLM engineering platform 的代表，覆盖 trace、session、prompt management、evaluation、score 和 dashboard，适合补全观测层概念。

## 一句话

Langfuse 用 trace 和 score 把 LLM/Agent 应用的调试、监控和评测连起来。

## 先读什么

- Observability：trace、session、latency、cost。
- Evaluation：LLM-as-judge、user feedback、manual labeling、custom evals。
- Scores：把质量判断绑定到 trace、observation、session 或 dataset run。

## 可以拆成概念卡

- [[Observability]]
- [[Trace]]
- [[LLM-as-Judge]]

## 我的疑问

- score 应该绑定到整条 trace，还是绑定到某个 retrieval/tool span？
- 自托管 observability 如何处理敏感数据和采样？

## 边界提醒

Langfuse 是平台，不是概念本身。要学习的是 trace -> score -> experiment -> regression 的工作流。
