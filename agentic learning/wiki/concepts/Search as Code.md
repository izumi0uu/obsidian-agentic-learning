---
type: concept
topic:
  - agent
  - rag
  - retrieval
  - tools
  - frontier
status: seed
created: 2026-06-02
updated: 2026-06-02
last_checked: 2026-06-02
freshness: watch
aliases:
  - SaC
  - 搜索即代码
source:
  - "[[Perplexity - Rethinking Search as Code Generation]]"
evidence:
  - "[[Perplexity - Rethinking Search as Code Generation#关键事实]]"
  - "[[Perplexity - Rethinking Search as Code Generation#例子：CVE 聚合]]"
  - "[[Perplexity - Rethinking Search as Code Generation#基准结果]]"
  - "[[Perplexity - Rethinking Search as Code Generation#边界提醒]]"
related:
  - "[[Tool Calling]]"
  - "[[Tool Use]]"
  - "[[Agentic Retrieval]]"
  - "[[Query Planning]]"
  - "[[Code Execution Sandbox]]"
  - "[[Agent Skills]]"
  - "[[Parallel Search and Explicit Merging 检索模式]]"
  - "[[传统 Tool-Calling 搜索 vs Perplexity SaC 对比]]"
---

# Search as Code

## 一句话

Search as Code 是一种把 search stack 暴露成 SDK primitives，让模型在 secure sandbox 中生成并执行代码、按任务即时编排 retrieval pipeline 的 search architecture。

## 概念详解

传统 AI-facing search 常把搜索当成一个 monolith：模型只负责给出 query 或少量参数，search system 跑完预定义 pipeline，再把处理后的结果集回给模型。[[Search as Code]] 试图把这个控制边界继续下沉。模型不再只是说“帮我搜什么”，而是能直接决定“我需要哪些 search primitives、按什么顺序、并发多少、怎样 merge 和 filter、哪些中间状态值得回到 token 空间”。

Perplexity 在 `2026-06-01` 的文章里把这个思路产品化成 `SaC`。它的具体实现由三层组成：模型作为 control plane 负责按任务生成搜索程序；secure compute sandbox 提供确定性代码执行环境；Agentic Search SDK 把 retrieval、ranking、filtering、fanout、rendering 等 search building blocks 暴露成可组合 primitives。这样做的结果不是“模型又多了一个工具”，而是“搜索本身变成了可编程执行面”。

这个概念之所以重要，是因为 agent 任务和传统 human search 的需求已经不一样了。人类浏览器用户更适合一个固定结果页；而 coding / research / computer-use agent 经常会在几分钟内发起数百上千次 retrieval，并且同一个任务内部可能同时需要厂商模板查询、去重、coverage 统计、source-specific filters、条件跳转和并发聚合。若这些动作都被迫通过一轮轮 model-visible tool turns 完成，延迟、token、context noise 和 control loss 都会急剧上升。

从工程视角看，SaC 把“代码”同时用成两种东西：

- orchestrator：把已有 search primitives 组织成任务特定 pipeline
- gap filler：当 search syntax 自带能力不够时，用普通代码补 deterministic 过滤、聚合、regex、join、coverage analysis 等缺口

但要注意：这张概念卡沉淀的是一种架构边界，不是说所有 search system 都必须长成 Perplexity 的样子。它目前仍然是 frontier / watch 概念。

## 它解决什么问题

Perplexity 的文章把 monolithic search 对 agent 的三个典型失败模式说得很清楚：

- coarse context：固定 pipeline 可能把很多对当前任务没价值的结果塞回模型，既贵又脏。
- failure to leverage domain knowledge：模型明明知道这次该偏 lexical、偏 semantic、偏某类 source 或按某个 key 聚合，但 rigid interface 没法把这些判断变成实际搜索动作。
- inefficient control flow and context pollution：很多复杂搜索天然需要 fan-out、并行、去重、筛选和中间汇总；如果每一步都必须过一轮 tool turn，模型上下文会充满 noisy intermediate state。

SaC 的作用就是把这些 deterministic retrieval-side 操作尽量放进 code + sandbox，而不是全都留给 token-space reasoning。

## 它不是什么

它不是“把普通 Search API 放进 Python 里”。

文章特别强调，这套实现不是把一个旧的 monolithic search endpoint 简单塞进 shell 或 runtime，而是先把 search stack 重新拆成 composable primitives，再让模型调用这些 primitives。

它也不等于 [[Tool Calling]]。

[[Tool Calling]] 解决的是“模型如何结构化地提出一次调用请求”；Search as Code 解决的是“搜索控制边界要不要继续下沉到 primitives，并由代码编排 many-step search workflow”。一个系统可以同时有 tool calling 和 SaC，但两者不是一个层级。

它也不等于 [[Agentic Retrieval]]。

[[Agentic Retrieval]] 是更宽的检索层模式，强调 query planning、多源检索、执行控制和结果合并；SaC 是一种更具体的架构实现，把这些控制通过 sandbox + SDK primitives 暴露给模型。

它也不是“搜索已经被完全标准化”。

目前公开最直接的实现和评测都来自 Perplexity 自己的 infra、SDK、skill tuning 和 benchmark 设置，不能直接外推成所有厂商的一般事实。

## 最小例子

文章里的代表性例子是高危 CVE 聚合。

任务不是简单“搜一下 CVE-2024-xxxx”，而是要覆盖 `2023-2025` 间 `200+` 个高危 CVE，并且每条都必须落到厂商自己的 advisory、产品名和 fix version。用传统 tool-calling 搜索做这件事，模型通常要反复做：

1. 生成一批 query
2. 每个 query 单独调一次 search
3. 把大批结果回填给模型
4. 再让模型做厂商过滤、coverage 判断和 refinement

而 SaC 的做法是把 fan-out、并发 search、vendor filtering、去重、coverage summary、定制 refinement 写进代码，在 sandbox 里直接运行，只把更紧凑的 evidence package 回给模型。这就是“search orchestration 变成代码问题”的最小直觉。

## 常见误解 / 风险

- 更可编排不等于天然更可靠。错误的 plan 一旦放大到大规模 fan-out，会更快地产生大规模错误。
- 价值不只来自“代码执行”四个字。真正的收益还依赖 sandbox、SDK 可教性、search primitive 粒度、trace 能见度和 skill tuning。
- benchmark 领先不代表可无损迁移。文章里的优势是模型、sandbox、search infra、SDK 和 skill 共同设计的结果，不是单一 API 风格带来的纯增益。
- 不是所有任务都值得下沉到 primitive 层。很多简单搜索任务，一个高层 endpoint 已经足够。

## 边界细节

和 [[Tool Calling]] 的边界：

[[Tool Calling]] 的默认形态是“模型请求一次调用，runtime 执行，再把结果回填”；SaC 更像“模型写一个搜索程序，程序在单次或少量 turns 内 orchestrate 很多 retrieval-side operations”。前者的控制单位通常是 call；后者的控制单位更接近 search workflow。

和 [[Agentic Retrieval]] 的边界：

[[Agentic Retrieval]] 讲的是检索层变聪明；SaC 讲的是把这种聪明如何落到一个具体的可编程接口上。可以把 SaC 理解成 agentic retrieval 的一种更极端、更 code-first 的工程化形态。

和 [[Code Execution Sandbox]] 的边界：

sandbox 提供的是确定性执行环境、状态持久化和安全边界；它让 SaC 可行，但 sandbox 本身不定义 retrieval semantics。

和 [[Parallel Search and Explicit Merging 检索模式]] 的边界：

parallel search + explicit merging 是一种检索模式；SaC 是能把这种模式内建到模型生成代码里的架构。前者是 pattern，后者是 programmable surface。

## 现代性状态

- 判定：frontier / watch。
- 稳定部分：agent 时代的搜索越来越需要可控的 fan-out、merge、filter、aggregation 和 compact context packaging。
- 易变部分：SDK 运行时、skill 设计、状态管理方案、公开产品边界、benchmark 和 cost-performance 数字都会变化。
- 复查点：当前公开最明确的接入面是 `Perplexity Computer` 和 `Agent API`；截至 `2026-06-02`，官方 `Search API` quickstart 仍把自己定位成 raw ranked results 接口，而不是公开的 SaC primitive surface。如果以后 Search API 公开暴露相同 primitive surface，需要回头修正边界。

## 现代系统怎么吸收 Search as Code 的价值 / 局限

现代系统能吸收的核心价值不是“都去学 Perplexity 的命名”，而是两件事：

1. 把 fan-out、去重、source-specific filtering、aggregation、coverage checking 这些 deterministic retrieval-side 操作尽量下沉到代码或 workflow runtime。
2. 只把对下一步 reasoning 真有价值的紧凑 evidence 包回填给模型，而不是把所有中间结果都塞进上下文。

局限也很明确：如果系统没有可靠的 sandbox、search primitive、trace 和 eval，只把接口改成“可写代码”很容易把复杂度和错误一起放大。对简单问题来说，一个高层 search endpoint 往往更便宜、更稳、更易治理。

## 证据锚点

- Source note: [[Perplexity - Rethinking Search as Code Generation#关键事实]]
- Source note: [[Perplexity - Rethinking Search as Code Generation#例子：CVE 聚合]]
- Source note: [[Perplexity - Rethinking Search as Code Generation#基准结果]]
- Source note: [[Perplexity - Rethinking Search as Code Generation#边界提醒]]
- Learning redraw: [[传统 Tool-Calling 搜索 vs Perplexity SaC 对比]] 内嵌 `tool-calling-search-vs-search-as-code.svg`，它是基于文章 Figure 1 / Figure 4 的学习重绘，不是官方原图。
- Evidence type: Perplexity 官方研究文章 + 工程综合。
- Confidence: medium。
- Boundary: 公开证据足以支持“Perplexity SaC 是一种具体架构实现”；更广泛的“search as code 会成为普遍标准”仍是推断。

## 复习触发

1. 为什么 Search as Code 不是“更强一点的 search tool call”？
2. 它为什么要依赖 sandbox，而不是只靠模型多轮调用 search？
3. “代码既是 orchestrator，也是 gap filler” 这句话具体是什么意思？
4. 什么任务还不值得进入 SaC 这种 primitive-level controllability？

## 相关链接

- [[Tool Calling]]
- [[Tool Use]]
- [[Agentic Retrieval]]
- [[Query Planning]]
- [[Code Execution Sandbox]]
- [[Agent Skills]]
- [[Parallel Search and Explicit Merging 检索模式]]
- [[传统 Tool-Calling 搜索 vs Perplexity SaC 对比]]
