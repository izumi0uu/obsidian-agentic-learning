---
type: source
source_type: article
title: Rethinking Search as Code Generation
url: https://research.perplexity.ai/articles/rethinking-search-as-code-generation
author: Perplexity
site: research.perplexity.ai
topic:
  - agent
  - rag
  - retrieval
  - tools
  - frontier
created: 2026-06-02
updated: 2026-06-02
last_checked: 2026-06-02
freshness: watch
conflicts: []
status: seed
source:
related:
  - "[[Search as Code]]"
  - "[[Tool Calling]]"
  - "[[Agentic Retrieval]]"
  - "[[Query Planning]]"
  - "[[Code Execution Sandbox]]"
  - "[[Agent Skills]]"
  - "[[Parallel Search and Explicit Merging 检索模式]]"
  - "[[传统 Tool-Calling 搜索 vs Perplexity SaC 对比]]"
---

# Perplexity - Rethinking Search as Code Generation

## 为什么收

这篇文章适合录入一个新边界：在 agent 时代，搜索不一定继续暴露成一个固定 `search()` endpoint；Perplexity 主张把 search stack 下沉成可编排 primitives，让模型直接在 harness 里写检索程序。

它的学习价值不只是“Perplexity 又发了一个产品名词”，而是它把很多已有判断连到一起了：[[Tool Calling]] 的控制边界、[[Agentic Retrieval]] 的检索规划、[[Code Execution Sandbox]] 的确定性执行层、[[Agent Skills]] 的可教性，以及为什么复杂 research / computer-use 任务会逼迫搜索接口继续拆细。

## 先读什么

- Introduction
- Failure Modes from Rigidity
- Designing a Programmable Search Architecture
- Case Study: CVE Vendor Advisories
- Comparative Performance / Cost-Performance Frontier

## 一句话

Perplexity 认为 agent 时代的搜索应该从“模型串行调用固定 search endpoint，再吃回结果”演进到“模型在 secure sandbox 中生成并执行代码，按任务即时编排 retrieval / ranking / filtering / fanout / rendering primitives”。

## 关键事实

- 文章发布日期是 `2026-06-01`。
- 文中把 [[Search as Code]] 定义为 Perplexity 的“new reference search architecture”。
- 文章明确说这套架构正在跨产品落地；公开直接点名的是 `Perplexity Computer` 和 `Agent API`。
- Perplexity 认为传统 AI-facing search 的默认接口是 function calling / MCP 风格的单次 search roundtrip，而这套接口对复杂 agent 任务已经太粗。
- 文中给出 monolithic search 的三个 recurring failure modes：
  - coarse context
  - failure to leverage domain knowledge
  - inefficient control flow and context pollution
- SaC 的核心做法不是“把旧 search API 包进一个 shell”，而是把 search stack 重构成一个 `Agentic Search SDK`，向模型暴露更原子化的 retrieval primitives。
- 文章强调模型可以直接控制 retrieval、ranking、filtering、fanouts、rendering，以及候选列表、ranking signals 等中间状态。
- Figure 4 把 SaC 拆成三层：
  - models 作为 control plane
  - secure compute sandboxes 负责 deterministic compute
  - Agentic Search SDK 暴露 composable primitives
- 文章提到跨 turn 状态管理测试过两条路：
  - persistent filesystem + explicit serde
  - REPL-style persistent runtime
- 他们暂时偏向 filesystem-based serde，因为长轨迹下可靠性更好。
- 文中说模型通常需要专门的 Agent Skills 才能把这类自定义 SDK 用好；Perplexity 把 root `SKILL.md` 控制在 2000 tokens 以内，重点放在组合模式和 few-shot guidance。

## 例子：CVE 聚合

- 文章给的 case study 是收集并刻画 `2023-2025` 间 `200+` 个高危 CVE。
- 任务要求每条记录都引用 vendor 自己的 advisory，并抽出 product、fix version 和与特定 CVE 的绑定关系。
- 文中给出的轨迹片段展示了 SaC 的三个能力：
  - 先按厂商 advisory 格式 fan-out 生成大量 source-specific queries。
  - 用并发 search primitive 拉回候选，再在确定性代码里做 vendor 过滤、去重和 coverage 统计。
  - 对 sparse vendor-year 自动合成新的 refinement 逻辑，而不是把所有中间结果都塞回模型上下文。
- 这说明 SaC 的强点不是“一个更强的 search box”，而是“搜索 orchestration 可以变成代码问题”。

## 基准结果

- 文章评了五个 benchmark：`DSQA`、`BrowseComp`、`HLE`、`WideSearch`、`WANDR`。
- 文中结论是：
  - SaC 在 `4/5` benchmark 上领先。
  - 在 `HLE` 上几乎与 OpenAI Responses 并列第一。
  - 在 `WANDR` 上比 next-best system 高 `2.5x`。
- 对比同样底层基础设施但不用 SaC 的 Perplexity baseline：
  - `DSQA` 最大绝对增益：`+19.77 pp (29%)`
  - `WANDR` 最大相对增益：`+12.00 pp (45%)`
- CVE case study 的数字更极端：
  - 准确率 `100%`
  - token 用量从 `288.7K` 降到 `42.9K`
  - 总 token 降幅 `85.1%`

## 可以拆成概念卡

- [[Search as Code]]
- `Agentic Search SDK`
- `search primitives`
- `search orchestration by code`

后面三个还不够稳定，暂时先不单独建卡。

## 我的疑问

- 这套能力里，哪些收益来自“接口变了”，哪些收益来自 Perplexity 自家的 search infra 和 skill tuning？
- 一个可迁移到其它 Agent 平台的最小 SaC primitive set 会长什么样？
- 对绝大多数普通搜索任务来说，高层 search endpoint 什么时候仍然比 primitive-level control 更划算？

## 边界提醒

- 这篇文章首先是 Perplexity 自己的 architecture / benchmark 论证，不是跨厂商通用标准。
- `Search as Code` 在这里既是架构边界，也是 Perplexity 的产品化实现；学习时要保留“可迁移抽象”和“Perplexity 特定实现”两层。
- 公开能直接确认接入 SaC 的是 `Perplexity Computer` 和 `Agent API`；`Search API` 共享底层 search 基础设施，但公开文档没有说它把同样的 primitive SDK surface 暴露给外部开发者。
- 截至 `2026-06-02`，Perplexity 官方 `Search API` quickstart 仍把它定位成“raw, ranked web results”接口，并把“LLM-generated summaries”引导到 `Agent API` 或 `Sonar API`；这进一步支持“Search API 是更高层结果接口，不等于公开 SaC surface”的边界判断。
- “用代码调搜索”不自动等于 SaC。文章特别强调，他们不是简单把传统 search API 放进 Python 里，而是先把 search stack 重构成 composable primitives。
