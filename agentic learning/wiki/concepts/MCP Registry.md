---
type: concept
topic:
  - tool
  - protocol
  - infrastructure
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: watch
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Model Context Protocol 官方文档]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[Model Context Protocol 官方文档#为什么收]]"
related:
  - "[[MCP]]"
  - "[[Tool Registry]]"
  - "[[Tool Poisoning]]"
  - "[[Least Privilege Tools]]"
---

# MCP Registry

## 一句话

MCP Registry 是用于发现、发布和分发 MCP server 的注册表基础设施。

## 它解决什么问题

MCP server 越多，Agent 应用越需要知道工具从哪里来、版本是什么、是否可信、怎么安装、如何更新。Registry 提供发现和分发入口。

## 它不是什么

MCP Registry 不是安全保证。

注册表里能发现工具，不代表工具一定可信、权限合理或没有 tool poisoning 风险。

## 最小例子

```text
host -> search registry -> install MCP server -> inspect tools -> grant permissions -> use
```

## 常见误解和风险

- 工具描述可能诱导模型错误调用。
- 供应链更新可能引入风险。
- registry 解决发现，不解决权限和审计。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[Model Context Protocol 官方文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[MCP]]
- [[Tool Registry]]
- [[Tool Poisoning]]
- [[Least Privilege Tools]]
