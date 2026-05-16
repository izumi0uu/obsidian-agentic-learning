---
type: concept
topic:
  - llm
  - evaluation
  - rag
status: growing
created: 2026-05-12
updated: 2026-05-16
last_checked: 2026-05-12
freshness: stable
source:
  - "[[LLM]]"
  - "[[RAG]]"
  - "[[RAG Evaluation]]"
evidence:
  - "[[LLM#它不是什么]]"
  - "[[RAG#常见误解 / 风险]]"
  - "[[RAG Evaluation#概念详解]]"
related:
  - "[[LLM]]"
  - "[[RAG]]"
  - "[[RAG Evaluation]]"
  - "[[RAG Citation Faithfulness]]"
---

# Hallucination

## 一句话

Hallucination 是模型生成了看似合理但缺乏事实依据、证据支持或任务约束的内容；它不是“模型故意撒谎”，而是生成机制和上下文约束不足的可靠性问题。

## 概念详解

LLM 会根据上下文生成概率上合理的 token 序列。这个能力让它擅长解释和总结，也带来风险：当上下文缺证据、问题要求超出资料、模型参数知识过期或 prompt 诱导过强时，它可能生成不存在的事实、错误引用、伪造 API、虚构论文、过度推断或把不确定内容说得很肯定。[[LLM]] 卡已明确 LLM 不是数据库；[[RAG]] 和 [[RAG Evaluation]] 则说明外部检索能降低部分事实风险，但不会自动保证答案正确。

Hallucination 的边界要分层看：有些是知识缺失，有些是检索失败，有些是证据误读，有些是引用不忠实，有些是工具结果解析错。把所有错误都叫 hallucination 会掩盖根因。对 RAG 来说，答案没有被证据支持时可能表现为 hallucination；但根因可能在 retriever、reranker、context assembly 或 source 本身。

证据边界：本卡用现有 [[LLM]]、[[RAG]]、[[RAG Evaluation]] 概念沉淀学习边界，不引入新的论文定义。不同研究和产品会对 hallucination、faithfulness、groundedness、factuality 有不同指标，本卡只保留学习用的稳定判断。

在 Agent 和 RAG 系统里，Hallucination 的边界要比“模型瞎说”更细：可能是模型没有证据却断言，也可能是证据进入上下文但被误读，或者 citation 指向了不支持结论的片段。排查时要把事实来源、上下文、prompt、工具返回、最终回答分层看。现代系统通常用 retrieval grounding、citation checking、LLM-as-judge、人工抽样和 trace 共同定位，而不是期望一个 prompt 完全消除幻觉。
## 它解决什么问题

它帮助学习者把“模型说得像真的”与“有证据支持”分开。没有这个概念，容易把流畅性、置信语气或引用格式误认为事实正确。

## 它不是什么

Hallucination 不是模型有意识欺骗。

它也不是所有错误的同义词。权限错误、工具失败、代码 bug、检索漏召回和用户问题歧义都可能导致错误，但不一定都应归因于模型幻觉。

## 最小例子

```text
用户：这篇论文提出了哪三个 benchmark？
模型：它提出了 A、B、C 三个 benchmark。
实际 source：论文没有提出 benchmark，只做了方法比较。
```

模型生成了看似学术的回答，但没有来源支持。

## 常见误解 / 风险

- 误解：更大模型就没有 hallucination。
- 误解：接入 RAG 就不会 hallucinate。RAG 可能检索错、引用错或让模型误读。
- 误解：答案有引用就不是 hallucination。引用可能不支持结论。
- 风险：在法律、医疗、金融、代码执行中，幻觉会变成真实损害。

## 边界细节

和 [[RAG Citation Faithfulness]] 的边界：citation faithfulness 专门检查答案-证据支持关系；hallucination 是更宽的生成可靠性问题。

和 [[RAG Evaluation]] 的边界：RAG Evaluation 用指标和样本定位 hallucination 可能来自哪一层。

和 [[Prompt]] 的边界：prompt 可以要求“不知道就说不知道”，但不能硬性保证模型不会生成无证据内容。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：生成模型可能产出无证据或错误内容，必须用证据、工具、评测和人工检查约束。
- 易变部分：具体 hallucination 指标、judge、groundedness 检查和模型可靠性会变化。
- 复查点：阅读评测论文或产品报告时，确认它测的是 factuality、faithfulness、citation accuracy 还是其他指标。

## 现代系统怎么吸收 Hallucination 的价值 / 局限

现代系统通过 RAG、tool calling、structured output、citation checks、eval harness、trace、refusal policy 和 human review 降低 hallucination 风险。高风险场景会要求模型给出证据、置信边界和无法回答时的拒答。

局限是没有单一手段能消灭幻觉。可靠性来自分层控制：证据进入、上下文装配、输出检查和持续评估。

## 证据锚点

- Concept anchor: [[LLM#它不是什么]]
- Concept anchor: [[RAG#常见误解 / 风险]]
- Concept anchor: [[RAG Evaluation#概念详解]]
- Evidence type: existing concept synthesis + engineering inference.

- Boundary: Hallucination 是输出与事实/证据/上下文不一致的失败形态，不等于所有错误、风格不佳或模型不确定。
## 复习触发

1. 为什么 hallucination 不是“模型故意撒谎”？
2. RAG 为什么只能降低部分 hallucination 风险？
3. 如何区分模型幻觉、检索失败和 citation 不忠实？

## 相关链接

- [[LLM]]
- [[RAG]]
- [[RAG Evaluation]]
- [[RAG Citation Faithfulness]]
- [[LLM 输入输出基础边界对比]]
