---
type: concept
topic:
  - security
  - agent
  - tool
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
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

## 概念详解

Data Exfiltration 在 Agent 系统里的问题不是“模型知道秘密”这么简单，而是模型可能被诱导把它能访问到的秘密带出边界。Agent 一旦接入文件系统、浏览器、数据库、邮件、MCP server 或企业 SaaS，prompt injection、tool poisoning、过宽权限和错误工具选择都可能把读取能力变成泄露能力。

机制上，数据外泄通常需要三个条件：有敏感数据、Agent 或工具能访问它、存在一个输出通道。输出通道可以是聊天回复、HTTP 请求、邮件、表单、日志、第三方工具参数或看似无害的摘要。OWASP LLM Top 10 和 Agentic Top 10 把 prompt injection、excessive agency、sensitive information disclosure、工具误用和供应链风险放在同一个安全图谱里；MCP tool poisoning source note 又提醒工具描述/返回值也可能诱导模型读取并传出秘密。

它和 [[Prompt Injection]] 的区别是层级：prompt injection 是一种诱导手段，data exfiltration 是可能造成的结果。它和普通“回答错了”也不同，因为外泄会越过信任边界并产生真实损害。治理重点不是让模型承诺不泄密，而是最小权限、数据分级、输出通道限制、审批、审计和对外部内容的来源标记。

对 Agent 学习来说，data exfiltration 是把多个安全概念串起来的结果节点：prompt injection 可能提供诱导，tool poisoning 可能伪造工具理由，过宽权限提供读取能力，缺少 approval/output policy 提供外送通道。因此修复它不能只修一个点，而要从输入来源、工具权限、数据范围、输出目的地和日志审计同时收窄。


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

## 边界细节

Data Exfiltration 是结果风险，不是单一攻击技术。判断时要问：敏感数据在哪里、Agent 是否可读、输出通道是什么、是否跨出了授权边界。只在模型输出端过滤，无法覆盖工具参数、日志和外部请求。

## 现代性状态

current-practice / watch。数据外泄是稳定安全风险，在 Agent 场景里因工具和跨系统行动被放大。风险分类和厂商控制会更新，所以按 watch 复查。

## 证据锚点

- Evidence type: source evidence — [[OWASP LLM Top 10 2025#为什么收]]；[[OWASP Agentic Applications Top 10#为什么收]]；[[MCP Tool Poisoning Threat Model#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[OWASP LLM Top 10 2025]]；[[OWASP Agentic Applications Top 10]]；[[MCP Tool Poisoning Threat Model]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- 判断 data exfiltration 风险时要找哪三个条件？
- 为什么只拦聊天输出不够？

## 相关链接

- [[Prompt Injection]]
- [[Indirect Prompt Injection]]
- [[Tool Poisoning]]
- [[Least Privilege Tools]]
