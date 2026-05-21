---
type: concept
topic:
  - llm
  - context
  - evaluation
status: growing
created: 2026-05-18
updated: 2026-05-18
last_checked: 2026-05-18
freshness: watch
conflicts: []
aliases:
  - context rot
  - Context degradation
  - context degradation
  - long-context degradation
  - long context degradation
  - 上下文退化
  - 上下文腐化
  - 长上下文退化
  - 长上下文可靠性退化
source:
  - "[[Chroma - Context Rot 技术报告]]"
  - "[[Context Window]]"
  - "[[LLM 上下文限制与突破条件]]"
evidence:
  - "[[Chroma - Context Rot 技术报告#报告主张]]"
  - "[[Chroma - Context Rot 技术报告#实验 / 证据]]"
  - "[[Context Window#概念详解]]"
  - "[[LLM 上下文限制与突破条件#限制分层]]"
related:
  - "[[Context Window]]"
  - "[[Context Engineering]]"
  - "[[Long-Horizon Context Engineering]]"
  - "[[GSSC Pipeline]]"
  - "[[RAG Evaluation]]"
  - "[[LLM 上下文限制与突破条件]]"
relations:
  - type: contrasts_with
    target: "[[Context Window]]"
    note: Context Window 是容量边界；Context Rot 是长输入中有效使用质量下降的风险。
  - type: risk_for
    target: "[[Context Engineering]]"
    note: 上下文工程需要通过选择、结构化、去噪和压缩来降低 context rot。
  - type: related_to
    target: "[[Long-Horizon Context Engineering]]"
    note: 长任务直接累积历史、工具结果和中间产物时，context rot 是核心风险之一。
---

# Context Rot

## 一句话

Context Rot 是长上下文里的有效使用退化：输入 token 变多、噪声和干扰项增加后，模型虽然“看得见”信息，但对关键内容的定位、使用和稳定推理会变差。

## 概念详解

Context Rot 出现的背景是长窗口模型越来越常见，很多人会自然假设：既然 [[Context Window]] 够大，把资料都放进去就行。但 Chroma 的技术报告提醒，模型能接收长输入，不等于会均匀处理长输入。越长的上下文越容易包含重复、干扰、冲突、过期资料、低相关段落和结构混乱的材料；这些材料会让关键证据更难被模型稳定使用。

这个概念的重点不是“信息不在窗口里”，而是“信息已经在窗口里，却没有被可靠使用”。在 [[RAG]] 中，retriever 可能已经找到了正确 chunk，但如果 top-k 太大、排序差、chunk 之间冲突、引用结构不清，模型可能仍然忽略中间证据或被无关 chunk 牵走。在 Agent 长任务中，工具日志、旧假设、失败尝试和重复中间产物不断累积，也会让后续推理被噪声拖慢或误导。

从机制上看，Context Rot 不是单一故障点，而是一组长输入风险的合称：位置偏置、干扰项相似度、haystack 结构、重复内容、无关上下文、冲突证据、历史错误固化、摘要遗漏和任务指令优先级下降都可能贡献退化。它把“长上下文可见性”和“长上下文可用性”切开：可见只是容量问题，可用才是上下文治理和评测问题。

这也是 [[Context Engineering]] 仍然重要的原因。窗口越大，越需要明确 Gather / Select / Structure / Compress：哪些信息进入候选池，哪些真正进入模型上下文，如何标注来源和优先级，超预算时压缩什么，以及如何用 eval 检查模型是否真的使用了关键证据。长窗口不是 RAG、memory、state、trace 和评测的替代品；它只是给这些工程层更大的操作空间，也放大了噪声管理问题。

证据边界：当前本卡主要由 Chroma 2025 research report 支撑，报告本身覆盖 18 个 LLM 和多种长上下文实验，但它不是同行评审论文，也不等于行业统一术语。`Context Rot` 作为命名应保持 watch 状态；它的稳定学习价值是“长上下文不保证可靠使用”，而不是某个具体模型或某个固定阈值。

## 它解决什么问题

- 给“上下文变长后为什么反而更不稳”一个专门入口。
- 防止把 [[Context Window]] 大小误读成答案质量保证。
- 解释为什么 RAG / Agent 不能把所有历史、chunk、memory 和 tool result 原样堆进 prompt。
- 帮助排错时区分：是没检索到关键证据，还是证据在上下文里但被噪声、顺序或结构影响了。
- 给 long-context evaluation 一个复习触发：要测模型是否真的使用长输入，而不是只看能否接收长输入。

## 它不是什么

Context Rot 不是 [[Context Window]]。Context Window 是一次调用能放多少 token；Context Rot 是放进去之后质量是否稳定的问题。

它也不是 [[Lost in the Middle]] 的完全同义词。Lost in the Middle 更像一个位置偏置现象：中间信息更容易被忽略；Context Rot 更宽，包含输入变长、噪声、干扰项、结构和重复内容导致的整体可靠性退化。

它也不是所有“退化”。模型微调后整体能力下降、memory 反复总结后变差、向量索引过期、服务端延迟上升、量化精度损失，都可能叫 degradation，但不应直接归到 Context Rot，除非问题明确发生在长上下文有效使用层。

它也不是“长上下文没用”。长窗口可以减少截断、支持更大证据包和长文分析；Context Rot 只是提醒：窗口变大后更要治理和评测。

## 最小例子

```text
问题：合同里乙方是否可以提前 30 天解除协议？

上下文 A：
  3 个相关条款，按标题组织，含来源。
  -> 模型正确引用解除条款。

上下文 B：
  3 个相关条款 + 40 个相似但无关条款 + 旧合同版本 + 会议纪要。
  -> 关键条款仍在窗口里，但模型引用了旧版本，或漏掉 30 天条件。
```

这里的问题不是窗口放不下，而是有效上下文被噪声和冲突稀释。更大的窗口让 B 可以被塞进去，但不保证模型会用对。

## 常见误解 / 风险

- 误解：只要模型支持 1M token，就可以跳过 RAG 和筛选。风险是把低质量证据也一起放大。
- 误解：context rot 只等于 Lost in the Middle。风险是只调位置，不处理噪声、冲突、重复、相似干扰项和结构问题。
- 误解：压缩越多越能避免 context rot。风险是压缩把关键证据删掉，或者把猜测固化成事实。
- 误解：只要答案最终对，就说明上下文没问题。风险是模型可能靠先验或偶然猜对，没有真正使用提供的证据。
- 风险：把 `上下文腐化` 理解成安全污染。安全污染可以造成 context rot，但本卡重点是长输入有效使用退化；安全污染另看 [[Indirect Prompt Injection]]、[[Tool Poisoning]] 和 RAG 治理。

## 边界细节

和 [[Context Window]] 的边界：window 是容量，rot 是有效使用质量。容量越大，越需要问“模型是否真的用对了”。

和 [[Context Engineering]] 的边界：Context Engineering 是治理方法；Context Rot 是它要防的风险之一。

和 [[RAG Evaluation]] 的边界：RAG Evaluation 可以把问题拆成 context precision、context recall、faithfulness 和 answer correctness；Context Rot 更像长输入条件下这些指标一起恶化的现象。

和 [[Long-Horizon Context Engineering]] 的边界：长时程任务容易累积历史噪声，因此更容易触发 Context Rot；但长时程上下文工程还包括 compaction、结构化笔记、sub-agent 隔离、state projection 等运行策略。

术语边界：`上下文退化` 比 `上下文腐化` 更适合作中文解释，因为它强调质量下降；`上下文腐化` 可以作为别名保留，但要避免和安全污染、prompt injection 混成同义词。

## 层级归属

本卡暂不直接写 `up`。[[09 概念层级审计基线]] 中 [[Context Window]] 是 root / anchor，[[Context Engineering]] 是 relation-only terminal；Context Rot 更像长上下文风险 / reliability phenomenon，当前用 `relations` 表达和容量、治理、长任务的关系。若未来建立稳定的 `Long-Context Evaluation` 或 `LLM Reliability` 父类，再走候选生成、判定、dry-run 和有限写回。

## 现代性状态

- 判定：current-practice / watch。
- 稳定部分：长窗口不保证模型均匀、可靠使用所有上下文；噪声、冲突、位置和结构会影响长输入表现。
- 当前实践：生产系统用筛选、重排、结构化、引用、去重、压缩、context budget、trace 和 evaluation 来降低风险。
- 易变部分：`Context Rot` 这个术语仍较新；不同模型家族、benchmark 和供应商可能会用 long-context reliability、context degradation、long-context robustness 等不同说法。
- 复查点：当主流 long-context benchmark、模型供应商文档或 Agent/RAG 框架把该问题标准化时，更新 aliases、边界和证据强度。

## 现代系统怎么吸收 Context Rot 的价值 / 局限

现代系统通常不会只靠扩大窗口，而会把 Context Rot 当作上下文质量风险来处理：

- 入窗前：去重、权限过滤、freshness 检查、source ranking、metadata 标注。
- 入窗时：按任务组织证据区、状态区、规则区和输出区，避免旧材料和当前事实混杂。
- 超预算时：优先压缩低价值历史和重复工具输出，保留关键约束、最新状态和证据来源。
- 评测时：检查关键证据是否进入上下文、是否被引用、答案是否 faithful，以及长输入/噪声条件下是否退化。
- 长任务中：用 compaction、structured notes、sub-agent 隔离和 trace 保留可验证状态，减少搜索噪声污染主上下文。

局限是：Context Rot 不是一个单一可修复 bug。不同任务可能由不同因素触发：有时是检索 top-k 太大，有时是证据排序，有时是旧 memory，有时是位置偏置，有时是 prompt 结构。真正的修复要回到具体 trace 和 eval，而不是只说“上下文烂掉了”。

## 证据锚点

- Source: [[Chroma - Context Rot 技术报告]]
- Report claim: [[Chroma - Context Rot 技术报告#报告主张]]
- Experiment notes: [[Chroma - Context Rot 技术报告#实验 / 证据]]
- Local concept boundary: [[Context Window#概念详解]]
- Local topic boundary: [[LLM 上下文限制与突破条件#限制分层]]
- Evidence type: Chroma research report + vault concept synthesis + engineering inference.
- Confidence: medium. 报告覆盖多模型和多实验，但术语仍应保持 watch；具体模型表现不能从本卡外推到未来版本。
- Boundary: 本卡只处理长输入条件下的上下文有效使用退化，不处理所有模型能力退化、memory 更新退化、索引质量退化或服务性能退化。

## 复习触发

1. Context Window 和 Context Rot 的最小区别是什么？
2. 为什么“正确证据已经在上下文里”仍可能答错？
3. Context Rot 和 Lost in the Middle 是什么关系？
4. 一个 RAG 系统 top-k 变大后答案变差，你会先检查哪些上下文工程环节？

## 相关链接

- [[Context Window]]
- [[Context Engineering]]
- [[Long-Horizon Context Engineering]]
- [[GSSC Pipeline]]
- [[RAG Evaluation]]
- [[LLM 上下文限制与突破条件]]
