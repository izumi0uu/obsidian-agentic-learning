---
type: source
source_type: docs
title: "LangSmith Evaluation and Observability"
url: "https://docs.langchain.com/langsmith/evaluation"
author: LangChain
site: docs.langchain.com
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
  - "[[Eval Harness]]"
  - "[[Trace]]"
  - "[[LLM-as-Judge]]"
  - "[[Trajectory Evaluation]]"
---

# LangSmith Evaluation and Observability

## 为什么收

LangSmith 是 Agent/RAG 应用中 tracing、dataset、evaluator、online/offline evaluation 的代表性平台，适合理解 observability 和 eval harness 如何连接。

## 一句话

LangSmith 把 trace、dataset、evaluator、experiment 和 production monitoring 组织成一个评测与观测闭环。

## 先读什么

- Evaluation overview：offline / online evaluation。
- Evaluators：human review、code rules、LLM-as-judge、trajectory evaluator。
- Observability：trace 每一步工具、模型和决策。

## 可以拆成概念卡

- [[Observability]]
- [[Eval Harness]]
- [[LLM-as-Judge]]
- [[Trajectory Evaluation]]

## 我的疑问

- 哪些 eval 应该离线跑，哪些应该线上监控？
- 失败 trace 如何转化成新的 regression eval？

## 边界提醒

Observability 只说明“发生了什么”，evaluation 才判断“好不好”。两者需要连起来，不然 trace 只是更漂亮的日志。
