---
type: concept
topic:
  - llm
  - agent
  - rag
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[Agent 工程基础设施主源#RAG / 检索基础设施]]"
related:
  - "[[LLM]]"
  - "[[RAG]]"
  - "[[Memory]]"
  - "[[Agent Harness]]"
---

# Context Engineering

## 一句话

Context Engineering 是设计进入模型上下文的信息结构、顺序、预算、来源和更新方式。

## 概念详解

Context Engineering 解决的是“模型这一轮到底看见什么”的工程问题。早期 prompt engineering 更像写一段指令；Context Engineering 则把系统指令、用户目标、历史摘要、工具 schema、检索证据、memory、trace 摘要、权限约束和输出格式一起看成运行时信息环境。模型能力再强，如果上下文里混入无关资料、缺少关键证据、优先级混乱或来源不可追溯，结果仍会不稳定。

在 RAG 场景里，Context Engineering 连接 [[Retriever]] 和 generator：检索到的 chunk 不应直接堆进 prompt，而要经过筛选、去重、排序、压缩、引用标注和权限检查。它决定哪些 source 进入上下文、放在什么位置、是否保留标题层级、是否显示 metadata、是否给模型明确的证据使用规则。对 Agent 来说，它还包括当前 plan、工具结果、observation、memory 和安全规则如何进入下一轮。

它的边界是上下文治理，不是单纯扩大 context window。长上下文可以容纳更多内容，但不能自动解决噪声、冲突、过期资料、prompt injection 或证据优先级。Context Engineering 的成熟做法通常会配合 trace 和 evaluation：记录每次上下文里有哪些材料，检查答案是否真的基于这些材料，并用失败样本改进检索和上下文组织。

证据边界：[[Agent 工程基础设施主源]] 支持 RAG / 检索基础设施、评测观测、Agent 框架和安全治理都是 production agent 系统必须处理的工程层；本卡把这些层综合为“上下文环境治理”。具体上下文模板、预算策略和压缩算法是工程综合，不是 source note 原文定义。

## 它解决什么问题

Agent 的表现不只取决于 prompt，还取决于它看到什么：系统指令、工具说明、用户目标、历史状态、检索材料、记忆、trace 摘要和安全约束。

## 它不是什么

Context Engineering 不只是 prompt engineering。

Prompt 更像写指令；context engineering 更像管理模型运行时能看到的整个信息环境。

它也不是把所有资料塞进长上下文。上下文越多，噪声、冲突和注入风险也可能越大。

## 最小例子

```text
system rules
-> task brief
-> current plan
-> selected memories
-> retrieved evidence with source anchors
-> tool schemas
-> recent trace summary
```

## 常见误解 / 风险

- 上下文越多不一定越好。
- 无关资料会稀释注意力。
- 外部资料可能包含 prompt injection。
- 长上下文仍然需要结构和优先级。

## 边界细节

和 [[RAG]] 的边界：RAG 负责检索外部资料；Context Engineering 负责决定这些资料如何进入上下文并被模型使用。

和 [[Memory]] 的边界：memory 是可保存的信息；context engineering 决定本轮选哪些 memory、如何摘要和排序。

和 prompt engineering 的边界：prompt engineering 关注指令文本；context engineering 关注运行时信息装配。

## 现代性状态

- 判定：current-practice。
- 稳定部分：LLM/Agent 系统需要管理上下文来源、顺序、预算和证据边界。
- 易变部分：具体 context window、压缩策略、memory selection、retrieval packaging 和框架 API。
- 复查点：当模型长上下文能力提高时，仍要检查上下文治理是否减少噪声和注入，而不是假设 runtime 责任消失。

## 现代系统怎么吸收 Context Engineering 的价值

现代系统通常把 context assembly 做成显式步骤：retrieval -> filter -> rerank -> compress -> cite -> answer；Agent 系统还会把 state、tools、memory、guardrails 和 trace 摘要分层放入上下文。这样上下文不只是文本堆叠，而是可解释、可评估、可回放的运行时输入。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Anchor: [[Agent 工程基础设施主源#为什么收]]
- Anchor: [[Agent 工程基础设施主源#RAG / 检索基础设施]]
- Evidence type: infrastructure source note + engineering synthesis.
- Confidence: medium
- Boundary: source note 支持 agent/RAG production infrastructure 的多层责任；“context engineering”作为总称和具体装配策略是本 vault 的工程综合。

## 复习触发

- Context Engineering 和 prompt engineering 的区别是什么？
- 为什么长上下文不能自动替代 RAG 和证据治理？
- 一个 RAG 答案错误时，哪些上下文装配问题可能是根因？

## 相关链接

- [[LLM]]
- [[RAG]]
- [[Memory]]
- [[Agent Harness]]
