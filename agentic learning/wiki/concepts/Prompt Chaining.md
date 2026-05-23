---
type: concept
topic:
  - llm
  - prompting
  - workflow
status: seed
created: 2026-05-23
updated: 2026-05-23
last_checked: 2026-05-23
freshness: stable
conflicts: []
aliases:
  - prompt chaining
  - Prompt Chain
  - prompt chain
  - 提示链
  - 提示词链
source:
  - "[[AI Engineering From Scratch - Few-Shot CoT]]"
  - "[[ReAct]]"
  - "[[Agent Workflow]]"
evidence:
  - "[[AI Engineering From Scratch - Few-Shot CoT#关键事实]]"
  - "[[ReAct#现代系统怎么吸收 ReAct 的价值]]"
  - "[[Agent Workflow#概念详解]]"
related:
  - "[[Prompt Engineering]]"
  - "[[Agent Workflow]]"
  - "[[ReAct]]"
  - "[[Workflow Guardrails]]"
  - "[[Structured Outputs]]"
---

# Prompt Chaining

## 一句话

Prompt Chaining 是把一个复杂任务拆成多个顺序 LLM 调用，让前一步输出成为后一步输入，从而把大问题变成可检查、可替换、可组合的小步骤。

## 概念详解

单个 prompt 同时承担抽取、分析、判断、写作和格式化时，模型容易混淆目标，也很难定位错误发生在哪一步。Prompt Chaining 的做法是把任务切开：第一步抽取事实，第二步分析事实，第三步生成建议，第四步格式化输出。每一步只做一个相对清晰的子任务，并把中间产物交给下一步。

它的工程价值不只是“多问几次模型”。真正重要的是中间结果可观察、可验证、可缓存、可替换。抽取步骤可以用便宜模型，分析步骤用强模型；中间 JSON 可以做 schema validation；某一步失败时可以局部重试，而不是整条大 prompt 重新生成。这个特征让 prompt chaining 介于 prompt pattern 和轻量 workflow 之间。

它也有明确代价：更多调用、更多延迟、更多中间格式契约、更多错误传播点。如果前一步抽错事实，后一步会在错误事实上认真分析。因此 Prompt Chaining 通常要和 [[Structured Outputs]]、validation、trace、guardrails 和 eval 结合。

Prompt Chaining 的设计重点是步骤边界，而不是调用数量。一个好的链条会让每一步有清晰输入、输出和失败条件：抽取节点只抽取，不顺手给建议；判断节点只判断，不重新发明事实；写作节点只基于前面的结构化结果生成自然语言。这样错误发生时，trace 能定位是哪一步坏了，修复时也能只改对应 prompt、schema 或模型选择。

这也是它和 Agent 的分水岭。Prompt chain 可以没有长期目标、没有环境 observation、没有工具副作用，也没有自主 replan；它更像一条固定数据管线。只有当链条引入动态分支、状态持久化、工具行动、失败补偿、人类审批或跨轮目标管理时，才逐渐进入 [[Agent Workflow]] 或 runtime harness 的边界。

在现代系统中，Prompt Chaining 常被编译成显式 node graph：节点有 schema，边有条件，trace 记录每次输入输出，eval harness 逐步检查中间产物。这样它不再只是“把 prompt 拆短”，而是把 LLM 调用变成软件系统中可观测、可替换的处理节点。

## 它解决什么问题

它解决的是复杂任务在单次 prompt 里责任过多、不可观察、不可局部修复的问题。拆成链后，每个步骤都可以单独评估和调试。

## 它不是什么

Prompt Chaining 不是 [[ReAct]]。ReAct 的关键是 Thought -> Action -> Observation 的外部交互循环；Prompt Chaining 可以完全不调用外部工具，只是顺序调用模型。

它不是完整 [[Agent Workflow]]。Prompt chain 可以是 workflow 的一部分，但默认没有 durable state、分支、并行、审批、重试策略或长期运行语义。

它也不是 [[Tree of Thoughts]]。ToT 在同一问题的中间状态展开多候选搜索；Prompt Chaining 是任务阶段的顺序分解。

## 最小例子

```text
Input: 一篇客户投诉邮件

Step 1 prompt: 抽取事实，输出 JSON: issue, product, date, sentiment
Step 2 prompt: 基于 JSON 判断严重级别和是否需要升级
Step 3 prompt: 生成客服回复草稿
Step 4 prompt: 检查回复是否承认问题、避免承诺赔偿、保持礼貌
```

每一步都可以被单独记录、验证或替换。

## 常见误解 / 风险

- 误解：Prompt Chaining 只是把一个 prompt 拆短。真正收益来自中间产物可检查和责任分离。
- 误解：链越长越可靠。链越长，错误传播和延迟也越多。
- 误解：有 chain 就是 Agent。没有工具、状态、反馈和行动边界时，它仍只是顺序 LLM pipeline。
- 风险：中间输出格式漂移，导致下一步输入被污染。
- 风险：前一步幻觉被后一步当作事实使用。

## 边界细节

最小谱系：

```text
Single prompt: one call handles everything
Prompt Chaining: step output -> next prompt input
Workflow: chain + branch/parallel/retry/state/guardrails
Agent: workflow/loop + tools + observations + goal-directed control
```

Prompt Chaining 值得升级到 workflow 的信号包括：需要分支、并行、人工审批、工具副作用、暂停恢复、失败补偿或跨步骤审计。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：顺序分解、责任隔离和中间验证是 LLM 应用基础工程模式。
- 当前工程吸收：LangChain chain、LangGraph node graph、workflow engines、data pipelines、agent harness 和 eval harness 都会吸收 prompt chaining 的思想。
- 不应夸大：prompt chain 是 workflow 的组成材料，不等于有了生产 workflow。

## 现代系统怎么吸收 Prompt Chaining 的价值

现代系统通常把 prompt chain 显式化为节点：每个节点有输入 schema、输出 schema、模型选择、重试策略、trace span 和评测样例。结构化输出让节点间契约更稳，guardrails 把检查放在关键边界，workflow runtime 则负责分支、状态和恢复。

## 证据锚点

- [[AI Engineering From Scratch - Few-Shot CoT#关键事实]]：支持 prompt chaining 的顺序分解和中间输出可检查边界。
- [[ReAct#现代系统怎么吸收 ReAct 的价值]]：支持可预测任务可用 prompt chaining / routing / parallelization 等 workflow 控制路径。
- [[Agent Workflow#概念详解]]：支持 prompt chain 与更完整 workflow 的分层关系。
- Evidence type: course source note + existing concept cards + engineering synthesis.
- Boundary: 本卡只记录顺序 LLM pipeline / prompt pattern；不把它等同于 ReAct、Tree of Thoughts、完整 Agent Workflow、workflow engine 或有工具副作用的自主执行系统。
- Confidence: medium。

## 复习触发

1. Prompt Chaining 相比一个大 prompt 多了什么工程收益？
2. 它和 ReAct 的最小区别是什么？
3. 什么时候 prompt chain 应该升级成 Agent Workflow？
4. 为什么中间输出最好结构化？

## 相关链接

- [[Prompt Engineering]]
- [[Agent Workflow]]
- [[ReAct]]
- [[Workflow Guardrails]]
- [[Structured Outputs]]
