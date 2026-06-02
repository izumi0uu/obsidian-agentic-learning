---
type: map
topic:
  - agent
  - rag
  - retrieval
  - tools
  - comparison
  - frontier
status: active
created: 2026-06-02
updated: 2026-06-02
source:
  - "[[Search as Code]]"
  - "[[Tool Calling]]"
  - "[[Agentic Retrieval]]"
  - "[[Code Execution Sandbox]]"
  - "[[Perplexity - Rethinking Search as Code Generation]]"
evidence:
  - "[[Search as Code#证据锚点]]"
  - "[[Tool Calling#证据锚点]]"
  - "[[Agentic Retrieval#证据锚点]]"
  - "[[Perplexity - Rethinking Search as Code Generation#关键事实]]"
  - "[[Perplexity - Rethinking Search as Code Generation#例子：CVE 聚合]]"
  - "[[Perplexity - Rethinking Search as Code Generation#基准结果]]"
related:
  - "[[Agent 主题]]"
  - "[[RAG 主题]]"
  - "[[Tool 接口层对比]]"
  - "[[Query Rewrite Query Planning Agentic Retrieval 对比]]"
  - "[[Parallel Search and Explicit Merging 检索模式]]"
  - "[[Search as Code]]"
  - "[[Tool Calling]]"
  - "[[Agentic Retrieval]]"
---

# 传统 Tool-Calling 搜索 vs Perplexity SaC 对比

## 一句话总览

传统 tool-calling 搜索把“搜索”暴露成一个固定 endpoint，模型通过串行的 `search(...)` 请求去驱动它；Perplexity 的 [[Search as Code]] 则把 search stack 继续拆成 primitives，让模型在 sandbox 中写代码来编排 retrieval、fanout、filter、merge 和 rendering。

## 结构图

![[tool-calling-search-vs-search-as-code.svg]]

上图是学习重绘，不是官方原图。它主要综合了 Perplexity 文章里的 Figure 1 和 Figure 4，用来帮助记住“固定 search endpoint”与“programmable search primitives”之间的控制边界差异。

## 为什么这组值得对比

- 两边解决的是同一个问题：Agent 需要访问新鲜、可操作、可组合的外部知识。
- 真正变化的不是“有没有 search”，而是“控制权在哪一层结束”。
- 这个边界会直接影响并发能力、token 成本、中间状态噪声、trace 粒度，以及系统能否把 domain knowledge 变成实际搜索动作。
- 很多工程讨论会把“tool-calling search 不够用”误听成“tool calling 没用”；其实问题常常不在 tool calling 本身，而在 search interface 是否过于 monolithic。

## 共同问题域

共同问题域是：当 agent 任务变成多源、多步、长时、宽搜索时，模型到底应该如何控制搜索过程。

```text
同一个任务可能同时需要：
- source-specific query 模板
- 并行 fan-out
- 去重和 coverage 检查
- custom filter / regex / aggregation
- 紧凑 evidence package
```

差别在于，这些动作是继续放在“多轮模型可见 tool turn”里做，还是尽量下沉到 deterministic compute 中完成。

## 核心区别表

| 概念 | 介入点 | 时序 / loop | 输入 | 输出 | 证据锚点 |
|---|---|---|---|---|---|
| [[Tool Calling]] 风格搜索 | 模型通过固定 `search(...)` endpoint 请求一次搜索 | 常是 `search -> result -> 再决定是否继续 search` 的串行 loop | query、filters、mode、少量参数 | monolithic resultset、snippets、top-N 候选 | [[Tool Calling#证据锚点]] |
| Perplexity [[Search as Code]] | 模型通过代码编排 search primitives、把 deterministic 搜索控制放进 sandbox | `写程序 -> 执行 primitives -> 整理 evidence -> 再回答/再搜` | 任务目标、search SDK primitives、sandbox state、source-specific logic | compact evidence package、persisted state、下一段搜索程序或答案 | [[Search as Code#证据锚点]], [[Perplexity - Rethinking Search as Code Generation#关键事实]] |
| [[Agentic Retrieval]] 视角下的 SaC | 检索层 planning / fanout / merge 被具体接口化、程序化 | `plan -> retrieve -> inspect -> refine -> merge`，但很多中间步骤不必每次都回 token 空间 | 子查询、source choice、coverage 判断、merge strategy | 多轮检索控制 + 更紧凑的 grounding data | [[Agentic Retrieval#证据锚点]], [[Perplexity - Rethinking Search as Code Generation#例子：CVE 聚合]] |

## 最容易混淆的边界

### 传统 search tool call vs [[Tool Calling]]

“传统 tool-calling 搜索”只是 [[Tool Calling]] 的一个具体使用场景。问题不是 [[Tool Calling]] 这个接口层错了，而是如果 search 只暴露一个固定 endpoint，复杂 agent 任务会觉得可控性不够。

### Perplexity SaC vs [[Agentic Retrieval]]

[[Agentic Retrieval]] 是更宽的 retrieval pattern，强调 query planning、多源检索、执行控制和结果合并。Perplexity SaC 是一种更具体的接口/架构实现：把这些控制做成 search primitives，并放进 sandbox + codegen loop 里。

### Perplexity SaC vs “search API + code interpreter”

这不是同一件事。Perplexity 在原文里专门强调，他们不是把一个旧的 monolithic search API 简单塞进 Python，而是先把 search stack 重新拆成 composable primitives。只有“能写代码”但 search 仍然只有一个固定 endpoint，还不算这个边界。

### Perplexity SaC vs MCP

MCP 解决的是 host 如何连接外部 tools / resources / prompts。SaC 解决的是 search stack 暴露给模型的控制粒度。一个系统完全可能同时使用 MCP 和 SaC，只是它们作用在不同层。

## 执行时序 / 机制差异

传统 tool-calling 搜索更像：

```text
task
  -> model
  -> search(query, filters)
  -> fixed search pipeline
  -> top-N / processed resultset
  -> model判断是否还要再搜一轮
  -> answer / next turn
```

Perplexity SaC 更像：

```text
task
  -> model写搜索程序
  -> sandbox执行代码
  -> Agentic Search SDK primitives
  -> retrieve / rank / filter / fanout / merge / render
  -> compact evidence package + persisted state
  -> answer / next search step
```

最关键的变化是：很多原来必须跨多个 model-visible turns 才能完成的 deterministic search-side work，被下沉到了单个代码执行面里。

## 学习类比（非证据）

> 这一节只是 learning analogy，不是论文或官方文档证据。

可以把两者想成“调研团队”和“搜索实习生”的差别：

- 传统 tool-calling 搜索像你每次都口头吩咐实习生去搜一轮，然后把整包网页结果拿回来，你再决定下一句命令。
- Perplexity SaC 更像你先写一份可执行调研脚本，让团队自己按规则并行查找、去重、汇总，只把压缩后的证据包交回给你。

类比边界：这个类比只是帮助记忆“固定 endpoint vs 可编排 primitives”的控制边界，不代表 Perplexity 内部实现真的按人类团队组织。

## 什么时候用哪个判断

- 如果任务只是单次网页查证、FAQ、产品说明、少量引用回答，高层 search endpoint 往往就够了，tool-calling 搜索更简单。
- 如果任务需要上百次 source-specific fan-out、并行抓取、coverage 统计、custom filtering、deterministic aggregation，SaC 这类 architecture 才真正显出价值。
- 如果系统还没有可靠 sandbox、trace、预算控制和 eval，不要为了追“更 agentic”而过早下沉到 primitive-level orchestration。
- 如果组织的 search infra 本身仍是黑盒单体服务，那么最现实的中间态通常不是一口气做成 SaC，而是逐步拆出更细的 retrieval / ranking / filtering surface。

## 现代系统如何吸收或限制

来源支持：
Perplexity 原文明确主张，复杂 agent 任务需要把 retrieval、ranking、filtering、fanout、rendering 等控制粒度下沉到可编排 primitives，并通过 secure sandbox 中的代码执行来完成大量确定性搜索工作，而不是持续暴露为串行的 function calling / MCP 式 search turn。原文也明确说明 SaC 是从 2026 年 6 月 1 日开始面向 [[Perplexity Computer]] 和 Agent API 推出的公开架构方向。见 [[Perplexity - Rethinking Search as Code Generation#关键事实]]、[[Perplexity - Rethinking Search as Code Generation#基准结果]]。

工程综合 / inference：
现代 deep-research、coding agent、research agent 系统真正值得吸收的，不是“所有搜索都必须代码化”，而是把高频、确定性、可复现的检索控制尽量留在代码和 runtime 里，把更紧凑的证据包而不是全部中间网页噪声送回模型。这样通常更利于并发 fan-out、状态压缩、可重复聚合，以及 token 成本控制。

仍需警惕的外推：
- primitive 必须可观测，否则错误只会更难定位。
- state 必须可持久和可复盘，否则长轨迹很快失控。
- sandbox 必须足够强，否则“可编程搜索”会顺手变成“高权限任意执行”。
- 高层 shorthand endpoint 仍然要保留，因为很多简单任务不值得动用完整可编排栈。
- 这不等于所有 Agent 产品都已经公开采用 SaC；就当前公开表述，Perplexity 明确点名的是 Computer 和 Agent API，不能自动外推到所有 Search API / Sonar / 第三方 agent 平台内部也以同样方式暴露。

## 它们共同不是什么

- 都不自动保证事实正确。source 质量、ranking 质量、citation 检查和最终生成 faithful 仍然重要。
- 都不替代权限治理。能搜到什么、能看哪些 source、哪些结果可以进入上下文，仍然需要 policy 和 audit。
- 都不等于“更先进就一定更好”。简单任务常常更适合高层 endpoint；复杂任务才需要更低层控制。

## 证据锚点

- [[Search as Code#证据锚点]]
- [[Tool Calling#证据锚点]]
- [[Agentic Retrieval#证据锚点]]
- [[Perplexity - Rethinking Search as Code Generation#关键事实]]
- [[Perplexity - Rethinking Search as Code Generation#例子：CVE 聚合]]
- [[Perplexity - Rethinking Search as Code Generation#基准结果]]
- Evidence type: concept-card synthesis + Perplexity 官方文章 + learning redraw。
- Confidence: medium。
- Boundary: “Perplexity SaC 优于其它系统”的 benchmark 数字来自官方文章；“这是一条值得学习的接口演进方向”是工程综合判断。

## 复习触发

1. 传统 tool-calling 搜索里，真正固定住模型控制边界的是什么？
2. 为什么 Perplexity 会把“并行 / 去重 / 聚合”尽量放进 sandbox 代码，而不是继续做多轮 search turn？
3. `Agentic Retrieval` 和 `Search as Code` 的最小区别是什么？
4. 什么情况下高层 search endpoint 仍然比 primitive-level control 更合适？

## 相关链接

- [[Search as Code]]
- [[Tool Calling]]
- [[Agentic Retrieval]]
- [[Tool 接口层对比]]
- [[Query Rewrite Query Planning Agentic Retrieval 对比]]
- [[Parallel Search and Explicit Merging 检索模式]]
- [[RAG 主题]]
- [[Agent 主题]]
