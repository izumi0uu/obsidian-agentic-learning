---
type: concept
topic:
  - llm
  - context
status: growing
created: 2026-05-12
updated: 2026-05-18
last_checked: 2026-05-12
freshness: watch
source:
  - "[[LLM]]"
  - "[[Context Engineering]]"
  - "[[Attention Is All You Need]]"
evidence:
  - "[[LLM#边界细节]]"
  - "[[Context Engineering#概念详解]]"
  - "[[Attention Is All You Need#我的疑问]]"
related:
  - "[[Token]]"
  - "[[Prompt]]"
  - "[[Context Engineering]]"
  - "[[Context Projection]]"
  - "[[Context Rot]]"
  - "[[RAG]]"
---

# Context Window

## 一句话

Context Window 是一次模型调用能接收和生成的 token 序列容量边界；它限制模型这一轮“看得见”多少输入和输出。

## 概念详解

LLM 不会无限读取所有资料。每次调用都有一个上下文窗口，包含系统消息、开发者/用户消息、工具 schema、历史对话、检索证据、图片/文件表示、模型输出预算等。超过窗口的内容要么进不来，要么被截断、摘要或压缩。[[Context Engineering]] 的核心问题之一，就是决定在有限窗口里放哪些信息、按什么顺序放、如何标注来源和优先级。

Context Window 容量扩大能缓解短上下文瓶颈，但不能自动解决上下文质量。长窗口里如果塞入过期资料、互相冲突的 chunk、prompt injection、无权限文档或低价值历史，模型仍可能误读。[[Context Rot]] 进一步提醒：输入越长、干扰越多时，模型对窗口内信息的使用可能变得更不稳定。RAG、memory 和 context engineering 的价值并不会因为窗口变长而消失；它们变成了“选择和治理上下文”的问题。

证据边界：[[Attention Is All You Need]] 支持 Transformer 处理序列位置和依赖的架构地基；[[LLM]] 与 [[Context Engineering]] 支持 LLM 依赖当前上下文生成、但不是长期记忆或数据库。具体模型窗口大小属于易变产品参数，不写入本卡的稳定定义。

实践中，窗口大小还会影响系统边界设计：短窗口迫使系统做摘要、检索和分段推理；长窗口则要求更强的上下文排序、引用标注和冲突处理。窗口是容量上限，不是注意力质量保证。模型可能能接收很长输入，但仍会遗漏中间信息、受噪音干扰或把低可信片段当成指令。因此现代系统会把 window budget 当作资源管理问题，而不是单纯等待模型支持更大数字。
## 它解决什么问题

它给模型一次调用的输入输出容量划边界，帮助工程系统预算 prompt、工具 schema、RAG 证据、历史消息和输出长度。

## 它不是什么

Context Window 不是长期记忆。模型看不到窗口外的信息，除非外部系统重新检索、摘要或写入上下文。

它也不是可靠性保证。窗口变大只说明能放更多 token，不说明模型会正确使用这些 token。

## 最小例子

```text
context window = system prompt + user question + retrieved chunks + tool schemas + answer budget
```

如果 retrieved chunks 太多，就可能挤掉历史、指令或输出预算。

## 常见误解 / 风险

- 误解：长上下文可以替代 RAG。大窗口仍需要选择、排序、权限和引用治理。
- 误解：模型会同等重视窗口里所有内容。位置、结构、噪音和冲突都会影响使用。
- 风险：把无关资料塞满窗口，让模型更难找到关键证据，触发 [[Context Rot|上下文退化]]。
- 风险：历史太长时，旧错误或注入内容被持续带入。

## 边界细节

和 [[Token]] 的边界：token 是计量单位，context window 是容量上限。

和 [[Prompt]] 的边界：prompt 是具体输入组织；context window 决定 prompt 和输出的容量边界。

和 [[RAG]] 的边界：RAG 负责从外部资料中挑选证据进入窗口；窗口越大不等于可以跳过检索质量。

## 现代性状态

- 判定：foundation / current-practice / watch。
- 稳定部分：模型一次调用受上下文容量限制。
- 易变部分：具体窗口大小、缓存、长上下文位置鲁棒性、压缩策略和多模态 token 计算会变化。
- 复查点：涉及具体模型时查最新官方文档；概念卡只保存容量边界，不保存某模型参数。

## 现代系统怎么吸收 Context Window 的价值 / 局限

现代系统会把 context window 当成预算：系统指令、工具 schema、RAG evidence、memory、trace summary 和输出各占多少。长任务 Agent 会用 compaction、summarization、retrieval 和 [[Context Projection|state projection]] 控制窗口内容。

局限是窗口只是容器，不是判断器。真正可靠来自上下文选择、来源标注、权限过滤、评估和必要时拒答。

## 证据锚点

- Concept anchor: [[LLM#边界细节]]
- Concept anchor: [[Context Engineering#概念详解]]
- Source anchor: [[Attention Is All You Need#我的疑问]]
- Evidence type: LLM/Context concept synthesis + Transformer source note + engineering inference.

- Boundary: Context Window 是单次调用容量边界，不是长期记忆、知识库、检索系统或事实校验机制。
## 复习触发

1. 为什么 context window 不是长期记忆？
2. 长上下文为什么不能自动替代 RAG？
3. 一次 Agent 调用中，哪些内容会共同占用 context window？

## 相关链接

- [[Token]]
- [[Prompt]]
- [[Context Engineering]]
- [[Context Projection]]
- [[Context Rot]]
- [[RAG]]
- [[LLM 输入输出基础边界对比]]
