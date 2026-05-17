---
type: concept
topic:
  - rag
  - agent
  - frontier
status: growing
created: 2026-05-05
updated: 2026-05-16
up:
  - "[[RAG]]"
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[前沿主源清单]]"
  - "[[Azure AI Search Agentic Retrieval]]"
  - "[[RAG 类型对比]]"
evidence:
  - "[[前沿主源清单#RAG 进化]]"
  - "[[Azure AI Search Agentic Retrieval#为什么收]]"
  - "[[Azure AI Search Agentic Retrieval#一句话]]"
  - "[[RAG 类型对比#一张表先抓住]]"
related:
  - "[[RAG]]"
  - "[[Agent]]"
  - "[[Planning]]"
  - "[[Evaluation]]"
  - "[[Agentic Retrieval]]"
---

# Agentic RAG

## 一句话

Agentic RAG 是让 Agent 主动决定何时检索、检索什么、是否改写问题、是否重试和如何使用证据的 RAG 模式。

## 概念详解

Agentic RAG 出现的原因是：普通 RAG 往往是一条固定流水线，用户问题进来后检索一次、拼上下文、生成答案。复杂任务并不总是适合这种单次 top-k 流程。一个比较任务可能需要拆维度，一个研究任务可能需要多轮查证，一个不确定答案可能需要判断证据是否足够，一个多源问题可能需要先选知识库再检索。

Agentic RAG 把这些检索相关决策放进 Agent loop 或图工作流里：系统可以先规划子问题，选择知识源，改写 query，调用多个 retriever，评估证据质量，不足时重查，最后再生成带引用的回答。它的关键不是“用了 Agent 这个词”，而是检索决策从固定 pipeline 变成可观察、可分支、可重试的行动过程。

和 [[Agentic Retrieval]] 的边界要切开：Agentic Retrieval 更偏检索层，强调 query planning、子查询、多源检索和 grounding data；Agentic RAG 更偏完整回答系统，除了检索层，还包括是否检索、如何使用证据、是否追问、是否调用工具、是否写回记忆、如何停止和如何评估。换句话说，Agentic Retrieval 可以是 Agentic RAG 的一部分，但不等于整个 Agentic RAG。

现代性上，Agentic RAG 是 current-practice / frontier 之间的概念。作为模式，它已经在 LangGraph、LlamaIndex、Azure AI Search 等生态里被反复使用；但具体 API、产品能力、query planner 形态、成本和可靠性仍在变化。学习它时要抓住稳定边界：复杂任务里的检索决策；不要把某个 vendor 的 preview 功能写成通用定义。

证据边界：[[前沿主源清单]] 说明它属于 RAG 进化方向；[[Azure AI Search Agentic Retrieval]] 支持 query planning、多查询检索和 agent workflow 的现代检索层；[[RAG 类型对比]] 提供本 vault 对 Agentic RAG / Agentic Retrieval 的层级切分。具体实现细节是工程综合和当前产品状态，需要 freshness watch。

## 它解决什么问题

普通 RAG 往往是固定流程：问题进来，检索一次，生成答案。

复杂任务可能需要拆问题、多次检索、比较来源、判断证据是否足够、发现检索失败后重查。Agentic RAG 把这些决策交给 Agent 或图工作流。

## 它不是什么

Agentic RAG 不是“加一个 Agent”就自动变强。

如果没有评估、停止条件和证据引用，它可能只是更复杂、更不稳定的 RAG。

它也不是 [[Agentic Retrieval]] 的同义词：后者更偏检索层，前者包含完整回答/行动流程。

## 最小例子

用户问：“LangGraph 和 OpenAI Agents SDK 在 human-in-the-loop 上有什么区别？”

Agentic RAG 可能会：

1. 拆成两个子问题。
2. 分别检索 LangGraph 和 OpenAI 文档。
3. 判断证据是否足够。
4. 追加检索 guardrails 或 handoff。
5. 汇总对比并标注来源边界。

## 常见误解 / 风险

- 误解：只要把 RAG 放进 Agent 框架，就变成 Agentic RAG。
- 误解：更多检索轮次一定更准确；实际上可能引入更多噪声。
- 风险：没有停止条件时，Agent 会过度检索、成本上升、延迟变长。
- 风险：没有 trace 和 eval 时，很难判断错在 plan、retrieval、rerank 还是 generation。

## 边界细节

Agentic RAG 的核心不是检索本身，而是检索决策：何时查、查哪里、怎么查、证据够不够、失败后怎么补救。

和 [[GraphRAG]] 的边界：GraphRAG 用图结构增强检索；Agentic RAG 用 Agent/workflow 决定检索行为。两者可以组合，但不是同一层。

和 [[Self-RAG]] 的边界：Self-RAG 原始论文强调模型通过 reflection tokens 学习检索/生成/批判控制；Agentic RAG 更偏系统/工作流模式，可以用工具、规则、图节点和 evaluator 实现。

## 现代性状态

- 判定：current-practice / frontier。
- 稳定部分：复杂 RAG 任务需要规划、重查、证据判断和可观察的检索决策。
- 易变部分：产品 API、agentic retrieval preview、query planner、框架节点和成本模型。
- freshness: watch。
- last_checked: 2026-05-10。
- 复查点：当 Azure AI Search、LangGraph、LlamaIndex 或 Agents SDK 的检索能力改变时，优先更新实现卡或 source note，不轻易改概念边界。

## 现代系统怎么吸收 Agentic RAG 的价值

现代系统通常把 Agentic RAG 做成图：plan -> retrieve -> grade -> reretrieve or answer。每个节点要有 trace、超时、最大轮次、失败 fallback 和 evaluator。这样 Agentic RAG 才是可靠性增强，而不是把不可控检索循环藏进 prompt。

## 证据锚点

- Source: [[前沿主源清单]]
- Anchor: [[前沿主源清单#RAG 进化]]
- Source: [[Azure AI Search Agentic Retrieval]]
- Anchor: [[Azure AI Search Agentic Retrieval#为什么收]]
- Anchor: [[Azure AI Search Agentic Retrieval#一句话]]
- Source: [[RAG 类型对比]]
- Anchor: [[RAG 类型对比#一张表先抓住]]
- Evidence type: frontier source map + official docs source note + local comparison map + engineering synthesis.
- Confidence: medium
- Boundary: Azure note supports agentic retrieval/query planning, not every possible Agentic RAG pattern; the broader Agentic RAG workflow description is engineering synthesis from the source map and comparison card.

## 复习触发

- Agentic RAG 比普通 RAG 多了哪些决策？
- Agentic RAG 和 Agentic Retrieval 的边界是什么？
- 没有 trace / eval / stopping rule 的 Agentic RAG 为什么风险更高？

## 相关链接

- [[RAG]]
- [[Agent]]
- [[Planning]]
- [[Evaluation]]
- [[Agentic Retrieval]]
