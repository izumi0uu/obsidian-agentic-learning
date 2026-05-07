---
type: source
source_type: article
title: "OWASP Top 10 for LLM Applications 2025"
url: "https://owasp.org/www-project-top-10-for-large-language-model-applications"
author: OWASP
site: owasp.org
topic:
  - security
  - agent
  - frontier
created: 2026-05-06
updated: 2026-05-07
last_checked: 2026-05-07
freshness: volatile
conflicts: []
status: seed
source:
related:
  - "[[Prompt Injection]]"
  - "[[Indirect Prompt Injection]]"
  - "[[Least Privilege Tools]]"
  - "[[Tool Poisoning]]"
---

# OWASP LLM Top 10 2025

## 为什么收

OWASP LLM Top 10 是 LLM 应用安全的主参考之一，其中 prompt injection、excessive agency、sensitive information disclosure、vector/embedding weakness 等都直接影响 Agent。

## 一句话

OWASP LLM Top 10 用风险分类帮助开发者识别和治理 LLM 应用中的安全问题。

## 先读什么

- LLM01 Prompt Injection。
- LLM06 Excessive Agency。
- LLM08 Vector and Embedding Weaknesses。
- LLM03 Supply Chain / LLM04 Data and Model Poisoning。

## 可以拆成概念卡

- [[Prompt Injection]]
- [[Indirect Prompt Injection]]
- [[Least Privilege Tools]]
- [[Tool Poisoning]]

## 我的疑问

- OWASP LLM 风险和 OWASP Agentic 风险如何映射？
- 对个人 Agent 项目，哪些控制措施最小但有效？

## 边界提醒

Prompt injection 不是“提示词写得不够好”这么简单。只要模型把外部内容当作可能影响行为的文本读入，就出现了安全边界问题。
