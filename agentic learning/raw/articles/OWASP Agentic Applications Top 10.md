---
type: source
source_type: article
title: OWASP Top 10 for Agentic Applications
url: https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/
author: OWASP GenAI Security Project
site: genai.owasp.org
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
  - "[[Tool Poisoning]]"
  - "[[Approval Gate]]"
  - "[[Policy Engine]]"
  - "[[Least Privilege Tools]]"
---

# OWASP Agentic Applications Top 10

## 为什么收

Agentic Applications Top 10 把风险从“LLM 应用”推进到“能规划、调用工具、跨系统行动的 Agent”。这能帮助我理解为什么 Agent 安全不只是 prompt 安全。

## 一句话

OWASP Agentic Top 10 关注自主 Agent 在目标、工具、身份、供应链、记忆、通信和人类信任上的新攻击面。

## 先读什么

- Agent goal hijack / prompt injection。
- Tool misuse / excessive agency。
- Agentic supply chain。
- Memory and context poisoning。
- Insecure inter-agent communication。

## 可以拆成概念卡

- [[Prompt Injection]]
- [[Tool Poisoning]]
- [[Approval Gate]]
- [[Policy Engine]]
- [[Least Privilege Tools]]

## 我的疑问

- 对一个学习型 Obsidian Agent，哪些风险是真实的，哪些暂时只是企业级风险？
- Agent 的 audit log 应该记录哪些最小字段？

## 边界提醒

Agent 安全不是单个过滤器可以解决的。它更像一组系统控制：权限、隔离、审批、审计、内容来源标记、eval 和人工接管。
