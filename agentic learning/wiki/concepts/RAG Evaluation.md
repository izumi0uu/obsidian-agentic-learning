---
type: concept
topic:
  - rag
  - evaluation
status: growing
created: 2026-05-06
updated: 2026-05-16
last_checked: 2026-05-10
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Microsoft RAG 官方文档]]"
  - "[[LangSmith Evaluation and Observability]]"
  - "[[Langfuse Observability and Evaluation]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[Agent 工程基础设施主源#RAG / 检索基础设施]]"
  - "[[Microsoft RAG 官方文档#一句话]]"
  - "[[Microsoft RAG 官方文档#先读什么]]"
  - "[[Microsoft RAG 官方文档#边界提醒]]"
  - "[[LangSmith Evaluation and Observability#一句话]]"
  - "[[LangSmith Evaluation and Observability#边界提醒]]"
  - "[[Langfuse Observability and Evaluation#一句话]]"
  - "[[Langfuse Observability and Evaluation#边界提醒]]"
related:
  - "[[RAG]]"
  - "[[Evaluation]]"
  - "[[Reranking]]"
  - "[[Retriever]]"
  - "[[LLM-as-Judge]]"
  - "[[Context Recall]]"
  - "[[Context Precision]]"
  - "[[RAG Citation Faithfulness]]"
aliases:
  - "RAG 评估"
  - "RAG 测评"
---

# RAG Evaluation

## 一句话

RAG Evaluation 是评估检索、上下文、引用和最终回答质量的一组方法。

## 概念详解

RAG Evaluation 之所以不能只等同于“答案对不对”，是因为 RAG 的失败链路很长。一个错误答案可能来自没有检到关键文档、检到了但排序太低、切分破坏上下文、上下文里混入过期或无权限内容、模型没有读懂证据、引用不能支持结论，或者最终回答虽然流畅但没有忠实于资料。只看最终答案，会把这些根因混成一个模糊的“模型不行”。

从机制上看，RAG Evaluation 至少要拆成 retrieval、context、generation、citation 和 system dimensions。Retrieval 关注 [[Context Recall]]、[[Context Precision]]、top-k 命中、rerank 后关键证据是否出现；context 关注片段是否完整、去重、不过期、权限正确、噪音不过多；generation 关注 answer correctness、faithfulness、groundedness、拒答和不确定性表达；citation 关注引用是否真的支持对应句子；system dimensions 关注 latency、cost、权限、数据泄露和线上失败样本。这个分层让评测可以定位“错在检索还是生成”。

[[Microsoft RAG 官方文档]] 的 source note 给 RAG Evaluation 一个企业工程边界：企业级 RAG 不只是“向量检索 + LLM”，还包括数据治理、索引策略、检索质量、权限和评估；并且提醒不要把 Azure 具体产品能力误解为 RAG 通用定义。这说明 RAG eval 必须覆盖数据和权限层，而不是只在生成端打分。[[Agent 工程基础设施主源]] 收集了 Ragas、DeepEval、Phoenix、Promptfoo 等评测/观测工具，说明社区已经把 RAG 评测作为专门工程层处理。

[[LangSmith Evaluation and Observability]] 与 [[Langfuse Observability and Evaluation]] 则补上现代工作流证据：trace、dataset、evaluator、score、experiment、monitoring 可以把一次 RAG 调用拆成可观察和可评分的过程。对 RAG 来说，score 最好不要只绑定最终 answer，也要能绑定 retrieval span、reranking span、context selection、citation check 和用户反馈。否则你可能知道“这次回答低分”，但不知道是检索没命中，还是模型忽略了正确片段。

现代系统吸收 RAG Evaluation 的方式，通常是建立分层回归集：固定问题集 + 期望证据文档 + 检索命中标准 + 答案忠实性标准 + 引用支持检查 + 人审抽样。对于个人 Obsidian wiki，最小版本可以是“问题 -> 应该引用哪些 source note -> 回答是否基于这些 source -> 是否新增了无证据说法”。证据边界：Microsoft source note 支持企业 RAG 的治理/索引/检索/权限/评估边界；LangSmith/Langfuse 支持 trace/score/evaluator/monitoring 闭环；具体指标组合是本 vault 对 RAG 评测实践的工程综合。

## 它解决什么问题

RAG 系统失败可能发生在很多层：没检到、检错了、排序错了、上下文太脏、模型误读、引用不支持答案。只看最终回答很难定位问题。

代表工具包括 Ragas、DeepEval、Phoenix、Promptfoo 等。

## 它不是什么

RAG Evaluation 不是只问“答案对不对”。

它也不是只靠 LLM-as-Judge。关键任务需要人工样本、规则、引用校验和回归集。

## 现代性状态

RAG Evaluation 属于 current-practice。

现代系统通常把它拆成可独立评估的层：retrieval、context quality、answer faithfulness、citation accuracy、latency 和 cost。概念稳定，但平台、指标实现和 judge 组合会持续变化。

## 最小例子

```text
问题集 -> retrieve -> 检查 recall / context precision -> answer -> faithfulness / citation check
```

## 常见误解和风险

- judge 模型可能偏向流畅答案。
- 没有标准答案时，指标会更不稳定。
- 只评生成不评检索，会错过根因。

## 边界细节

- RAG Evaluation 评的是整条链路，不只是最终回答。
- 对检索问题，recall / precision / rerank 命中率常比 answer 分数更早暴露根因。
- 对引用问题，必须区分“答案像对了”与“证据真的支持”。
- 没有回归集的评测通常更像一次性诊断，不像稳定评测系统。

## 现代系统怎么吸收它的价值

- 把 retrieval 指标和 answer 指标分开看。
- 对失败样本做 dataset 化和回归测试。
- 用规则 + judge + 人审组合，避免只靠流畅度打分。
- 把引用校验、权限和上下文质量纳入同一评测闭环。

## 复习触发

- 为什么 RAG 评测不能只看最终答案？
- retrieval 指标和 answer faithfulness 各自暴露什么问题？
- 什么时候一个 RAG 系统需要人工样本和回归集，而不是只跑 judge？

## 证据锚点

- Source: [[Microsoft RAG 官方文档]]
- Anchors: [[Microsoft RAG 官方文档#一句话]], [[Microsoft RAG 官方文档#先读什么]], [[Microsoft RAG 官方文档#边界提醒]]
- Tooling source: [[Agent 工程基础设施主源]]
- Anchors: [[Agent 工程基础设施主源#RAG / 检索基础设施]], [[Agent 工程基础设施主源#为什么收]]
- Evaluation / observability sources: [[LangSmith Evaluation and Observability]], [[Langfuse Observability and Evaluation]]
- Anchors: [[LangSmith Evaluation and Observability#一句话]], [[LangSmith Evaluation and Observability#边界提醒]], [[Langfuse Observability and Evaluation#一句话]], [[Langfuse Observability and Evaluation#边界提醒]]
- Evidence type: official RAG docs + evaluation/observability platform notes + engineering synthesis.
- Confidence: medium
- Boundary: sources 支持 RAG 的治理/索引/检索/权限/评估边界和 trace/score/evaluator 工作流；retrieval/context/generation/citation/system dimensions 的分层是工程综合模型。

## 相关链接

- [[RAG]]
- [[Evaluation]]
- [[Retriever]]
- [[Reranking]]
- [[LLM-as-Judge]]
