---
type: concept
topic:
  - security
  - agent
  - tool
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[OWASP LLM Top 10 2025]]"
  - "[[OWASP Agentic Applications Top 10]]"
  - "[[MCP Tool Poisoning Threat Model]]"
evidence:
  - "[[OWASP LLM Top 10 2025#为什么收]]"
  - "[[OWASP Agentic Applications Top 10#为什么收]]"
  - "[[MCP Tool Poisoning Threat Model#为什么收]]"
related:
  - "[[Prompt Injection]]"
  - "[[Indirect Prompt Injection]]"
  - "[[Tool Poisoning]]"
  - "[[Least Privilege Tools]]"
---

# Data Exfiltration

## 一句话

Data Exfiltration 是敏感数据被 Agent、工具、检索结果或模型输出带出安全边界的风险。

## 它解决什么问题

这是安全概念，不是功能概念。它提醒我：Agent 一旦能读私有数据、联网、发消息或调用外部 API，就可能被诱导把不该泄露的信息送出去。

## 它不是什么

Data Exfiltration 不只是“模型说出了秘密”。

它还可能通过工具参数、日志、网页请求、邮件、插件、MCP server、trace 或通知 webhook 发生。

## 最小例子

```text
网页隐藏指令 -> Agent 读取本地文件 -> 调用外部 URL -> 把文件内容作为 query 参数发送
```

## 常见误解和风险

- 只过滤最终回答不够，工具调用也可能泄露。
- 日志和 trace 也可能存下敏感内容。
- prompt injection 经常以数据外泄作为最终目标。

## 证据锚点

- Source: [[OWASP LLM Top 10 2025]]
- Source: [[OWASP Agentic Applications Top 10]]
- Source: [[MCP Tool Poisoning Threat Model]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Prompt Injection]]
- [[Indirect Prompt Injection]]
- [[Tool Poisoning]]
- [[Least Privilege Tools]]
