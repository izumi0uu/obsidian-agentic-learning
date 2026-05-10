---
type: concept
topic:
  - tool
  - protocol
  - infrastructure
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
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

## 概念详解

MCP Registry 的问题背景是 MCP server 数量增长后，host 不可能靠手工复制 README 来发现和维护连接器。Registry 提供发现、发布、版本、元数据和安装入口，让 AI 应用知道有哪些 MCP server、它们暴露什么能力、来自哪里、怎样接入。Agent 工程基础设施 source note 把 Official MCP Registry、registry repo 和 Docker MCP Gateway 放在工具生态里，说明 registry 是协议生态的分发层。

机制上，registry 解决“找到工具”和“描述工具”的问题，但不自动解决“信任工具”。一个 MCP server 出现在 registry 里，只说明它可被发现，不说明它适合当前任务、权限合理、描述无投毒、供应链安全或版本不会破坏旧流程。MCP 官方文档 source note 对 tool definition、inputSchema、outputSchema、annotations 的补充也提醒：工具描述和 annotations 对模型选择有影响，但客户端不能无条件信任不可信 server。

它和 [[Tool Registry]] 的边界：MCP Registry 更偏生态级、跨应用的 server 分发；Tool Registry 可以是某个 host 内部管理可用工具、权限和状态的目录。学习时不要把 registry 当成 app store 式安全背书。正确边界是：发现之后还要做来源校验、版本锁定、权限审查、sandbox、approval gate 和运行时 audit。

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

## 边界细节

MCP Registry 负责发现和分发，不负责替 host 做信任决策。server 被发现后仍要校验来源、版本、权限、schema、描述和运行环境。它和内部 Tool Registry 的职责可以重叠，但作用范围不同。

## 现代性状态

frontier / volatile。MCP registry 生态正在形成，发现/分发问题稳定，但官方 registry、签名、信任、版本和企业网关实践会快速变化。

## 证据锚点

- Evidence type: source evidence — [[Agent 工程基础设施主源#为什么收]]；[[Model Context Protocol 官方文档#为什么收]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[Agent 工程基础设施主源]]；[[Model Context Protocol 官方文档]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- MCP Registry 解决发现后，哪些安全问题仍未解决？
- 它和 Tool Registry 的范围差异是什么？

## 相关链接

- [[MCP]]
- [[Tool Registry]]
- [[Tool Poisoning]]
- [[Least Privilege Tools]]
