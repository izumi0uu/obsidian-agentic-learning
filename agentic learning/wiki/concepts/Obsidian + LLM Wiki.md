---
type: concept
topic:
  - obsidian
  - llm-wiki
status: growing
created: 2026-05-05
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[LLM Wiki 工作流]]"
  - "[[字段规范]]"
evidence:
  - "[[LLM Wiki 工作流#三层结构]]"
  - "[[字段规范#evidence]]"
related:
  - "[[index]]"
  - "[[04 页面目录]]"
  - "[[05 Query 写回队列]]"
  - "[[06 Wiki 健康检查]]"
  - "[[Agent]]"
  - "[[RAG]]"
  - "[[Memory]]"
---

# Obsidian + LLM Wiki

## 一句话

Obsidian + LLM Wiki 是一个由 [[双链]] 笔记组织、由 LLM 辅助提问和整理的个人知识系统。

## 概念详解

Obsidian + LLM Wiki 的问题背景是把“临时问答”变成可复用的学习系统。Obsidian 提供长期笔记、双链和地图；LLM 提供抽取、改写、提问、连接和维护建议。当前 vault 的工作流把 raw、wiki、maps 分层：raw 保存来源证据，wiki 保存沉淀后的概念卡，maps 保存导航、问题池、写回队列和健康检查。

## 它解决什么问题

普通笔记容易变成资料堆积。Obsidian 的 [[双链]] 让概念之间形成网络，LLM 可以帮助我总结、提问、找连接和生成复习材料。

## 它不是什么

它不是让 LLM 替我学习。

它也不是把所有资料复制进笔记。真正重要的是把外部资料变成自己的概念卡、问题和实验记录。

## 最小例子

用户收集一篇 Agent 资料后，先把原文保存在 `raw/`，再把可复述的概念写进 `wiki/concepts/`，最后在 `maps/` 里更新导航和复习问题。

## 最小结构

```text
首页 -> 学习路线 -> 术语表 -> 概念卡 -> 问题池 -> 实验记录
```

## Obsidian 负责什么

- 保存长期笔记。
- 用 [[双链]] 连接概念。
- 让知识可以被重新发现。
- 形成自己的知识地图。

## LLM 负责什么

- 把长内容压缩成概念。
- 帮我发现模糊之处。
- 生成测试问题。
- 建议哪些笔记应该互相链接。
- 把我的口头理解整理成清楚文字。

## 我的边界规则

LLM 生成的内容必须经过我确认。只要我不能用自己的话解释，就不算真正进入知识库。

## 当前 vault 的实践状态

这个项目已经是一个早期可用的 LLM Wiki，而不是普通 Obsidian 笔记。

判断依据：

- `raw/` 保存来源证据。
- `wiki/concepts/` 保存结构化理解。
- `maps/` 保存导航、路线、问题池、页面目录、写回队列和健康检查。
- [[AGENTS.md]]、[[LLM Wiki 工作流]] 和 [[字段规范]] 共同约束 LLM 如何 ingest、query、lint。
- [[log]] 记录每次维护轨迹。

但它还不是全自动知识编译系统。当前更准确的状态是：人工监督的 LLM 学习 wiki。

## 还没完全自动化的部分

- query 后的好答案需要写入 [[05 Query 写回队列]] 或直接写回概念卡。
- source freshness 和 contradiction check 通过 [[06 Wiki 健康检查]] 周期处理。
- 概念卡已有 source note 级证据锚点，但段落、页码、claim 级证据需要精读时继续补。

## 边界细节

边界是学习 ownership：LLM 可以维护结构和提出解释，但用户能否用自己的话复述才是学习完成标准。raw 不能被概念卡替代，reviews 也不能当 source evidence。

## 现代性状态

current-practice / seed-lite。它是本 vault 的学习工作流概念，不是外部前沿协议。稳定价值是 raw/wiki/maps 分层和证据边界；具体插件和自动化方式可变化。

## 证据锚点

- Evidence type: source evidence — [[LLM Wiki 工作流#三层结构]]；[[字段规范#evidence]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[LLM Wiki 工作流]]；[[字段规范]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- raw、wiki、maps 三层分别保存什么？
- 为什么 LLM 写进 wiki 不等于我已经学会？

## 相关链接

- [[index]]
- [[Agent]]
- [[RAG]]
- [[Memory]]
- [[双链]]
- [[04 页面目录]]
- [[05 Query 写回队列]]
- [[06 Wiki 健康检查]]

## 常见误解

- 以为 LLM 写进 wiki 就等于自己学会了。
- 把 raw 资料复制成概念卡，导致证据层和理解层混在一起。
- 让双链数量取代真实边界理解：链接多不代表能复述。
