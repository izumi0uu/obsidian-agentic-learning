---
type: map
topic:
  - llm
  - prompting
  - context
  - evaluation
  - comparison
status: active
created: 2026-05-12
updated: 2026-05-17
source:
  - "[[LLM]]"
  - "[[Token]]"
  - "[[Context Window]]"
  - "[[Prompt]]"
  - "[[Prompt Engineering]]"
  - "[[Hallucination]]"
  - "[[Attention Is All You Need]]"
evidence:
  - "[[LLM#证据锚点]]"
  - "[[Token#证据锚点]]"
  - "[[Context Window#证据锚点]]"
  - "[[Prompt#证据锚点]]"
  - "[[Prompt Engineering#证据锚点]]"
  - "[[Hallucination#证据锚点]]"
related:
  - "[[LLM 主题]]"
  - "[[LLM 基础结构对比]]"
  - "[[Context Engineering]]"
  - "[[Prompt Engineering]]"
---

# LLM 输入输出基础边界对比

## 一句话总览

LLM 输入输出的基础边界可以用五个词切开：[[Token]] 是模型读写的离散单位，[[Context Window]] 是一次调用能容纳的 token 边界，[[Prompt]] 是给模型的任务/上下文/约束组合，[[Prompt Engineering]] 是让 prompt 可设计、可测试、可版本化的工程实践，[[Hallucination]] 是输出与事实或证据不一致的失败结果。

## 为什么这组值得对比

这组概念是 Agent / RAG / prompting 的共同地基，但经常被混用：把 prompt 当成模型知识，把 context window 当成长期记忆，把 token 当成字符，把 hallucination 当成“模型坏了”。如果不先切清输入输出边界，后面学习 [[RAG]]、[[Memory]]、[[Tool Calling]]、[[Context Engineering]] 和 [[Agent Loop]] 时会把工程控制点放错位置。

## 共同问题域

共同问题域是“一次 LLM 调用如何把外部信息变成输入，并生成受概率、上下文和证据约束的输出”。

```text
text / tool results / memory / retrieved docs
        -> tokenization -> prompt/context -> model generation -> output / possible hallucination
```

## 核心区别表

| 概念 | 所在位置 | 回答的问题 | 常见误解 | 证据锚点 |
|---|---|---|---|---|
| [[Token]] | 输入/输出的计量和建模单位 | 模型实际读写的离散片段是什么？ | token = 单词/字符；token 多就一定懂更多 | [[Token#证据锚点]] |
| [[Context Window]] | 单次调用的上下文容量边界 | 这轮最多能放多少输入和生成多少输出？ | 长上下文 = 长期记忆；塞进去就会被正确使用 | [[Context Window#证据锚点]] |
| [[Prompt]] | 输入组织和任务约束层 | 我怎样告诉模型任务、角色、证据和格式？ | prompt = 魔法咒语；prompt 可替代工具/状态/评估 | [[Prompt#证据锚点]] |
| [[Prompt Engineering]] | 输入组织的工程实践层 | 怎样设计、测试、版本化和回滚 prompt？ | 等于 prompt 本身；只靠技巧不用评测 | [[Prompt Engineering#证据锚点]] |
| [[Hallucination]] | 输出失败形态 | 输出是否与事实、证据或上下文不一致？ | 有 RAG/引用就不会幻觉；流畅就可信 | [[Hallucination#证据锚点]] |
| [[Context Engineering]] | 多来源上下文编排 | 哪些信息应进入 prompt，按什么顺序和边界？ | 等于 Prompt Engineering；只追求越多越好 | [[Context Engineering#证据锚点]] |

## 最容易混淆的边界

### Token vs Word / Character

[[Token]] 是模型 tokenizer 产生的片段，可能是词、子词、符号、空格组合或代码片段，不等于自然语言单词。工程上估算成本、延迟、context window 和 truncation 风险时看 token，而不是只看字符数。

### Context Window vs Memory

[[Context Window]] 是本次调用的容量限制；[[Memory]] 是跨轮保存和检索信息的系统机制。把历史全塞进长上下文不是 memory strategy，也不保证模型会优先使用正确片段。

### Prompt vs Prompt Engineering vs Context Engineering

[[Prompt]] 是输入文本/消息里的任务指令、上下文和格式约束；[[Prompt Engineering]] 是围绕 prompt 的设计、测试、版本化和优化实践；[[Context Engineering]] 是更大的工程问题，决定从 RAG、tools、memory、trace、policy 中选什么放入 prompt。prompt 是载体，prompt engineering 是输入层工程实践，context engineering 是运行时装配策略。

### Hallucination vs Citation Faithfulness

[[Hallucination]] 是输出与事实或证据不一致；[[RAG Citation Faithfulness]] 专门检查 RAG 答案的引用是否支持结论。一个没有 citation 的答案也可能幻觉；一个带 citation 的答案也可能引用不 faithful。

## 执行时序 / 机制差异

```text
1. 选择信息：系统指令、用户任务、RAG 证据、tool result、memory、policy
2. 组织 prompt：角色、目标、约束、示例、输出格式、引用规则
3. token 化：输入被 tokenizer 映射为 token 序列
4. context 裁剪：超过 context window 的部分被摘要、压缩、检索或丢弃
5. 生成输出：模型根据上下文概率生成 token
6. 校验输出：检查事实、引用、格式、权限和 task success
```

小边界：输入进了 context window 只表示模型可见，不表示模型理解、优先使用或正确引用。输出看起来有逻辑，也不表示它被证据支持。

## 学习类比（非证据）

可以把一次 LLM 调用类比成“有限桌面上的写作”：Token 是纸面单位，Context Window 是桌面大小，Prompt 是任务说明和材料摆放，Hallucination 是写出的内容没有被材料支持。

类比边界：这只是学习类比（非证据），不代表论文、官方文档或具体产品内部真的按这个类比实现。

## 现代系统如何吸收或限制

现代 Agent / RAG 系统把这些基础边界工程化：token 用于预算、延迟和截断控制；context window 用于决定摘要、检索和 memory 投影策略；prompt 被拆成 system/developer/user/tool/result 等消息边界；prompt engineering 把模板版本、测试样例、指标和回滚纳入流程；hallucination 用 RAG、tool calling、citation check、eval harness 和 human review 降低风险。现代性状态是 **foundation + current-practice**：概念本身是地基，围绕长上下文、自动上下文压缩和 faithfulness judge 的产品能力仍是 watch。

工程综合 / inference：很多“模型不听话”其实不是模型能力单点问题，而是 token 预算、上下文排序、prompt 权限、证据缺失和评估缺口共同造成的系统问题。

## 什么时候用哪个判断

- 估算成本、长度、截断：看 [[Token]]。
- 判断一次调用能否容纳资料：看 [[Context Window]]，再看 [[Context Engineering]]。
- 设计任务说明、格式和证据使用规则：看 [[Prompt]]。
- 输出事实不可靠、引用不支持、模型编造：看 [[Hallucination]]、[[RAG Evaluation]] 和 [[RAG Citation Faithfulness]]。
- 需要跨轮保留用户偏好或任务状态：看 [[Memory]] / [[Agent State]]，不要只扩大 context window。

## 它们共同不是什么

- 不是完整的 Agent 能力；Agent 还需要目标、工具、状态、观测和控制 loop。
- 不是越长越好；更多 token 和更大 context window 会增加成本、延迟和噪音。
- 不是 prompt 可以替代 retrieval、tool execution、权限、安全和评估。
- 不是 hallucination 可以被单一技巧彻底消灭；只能通过证据、工具、评估和人工校验降低风险。

## 证据锚点

- 概念卡：[[LLM#证据锚点]], [[Token#证据锚点]], [[Context Window#证据锚点]], [[Prompt#证据锚点]], [[Prompt Engineering#证据锚点]], [[Hallucination#证据锚点]], [[Context Engineering#证据锚点]], [[RAG Citation Faithfulness#证据锚点]]。
- source notes：[[Attention Is All You Need]], [[OpenAI - A Practical Guide to Building Agents]], [[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks]]。
- 主题锚点：[[LLM 基础结构对比#证据锚点]], [[RAG 可靠性与治理对比#证据锚点]]。
- 证据边界：本页是学习边界页；tokenization、context size 和消息角色的具体 API 细节会随模型/供应商变化，需要看官方文档。

- Evidence type: LLM concept cards + Transformer/RAG/agent source notes + learning synthesis.
- Confidence: high for vault-local boundaries; medium for provider-specific API details.
- Boundary: tokenizer、context size、message role 和输出限制会随模型/供应商变化，本页只沉淀基础学习边界。
## 复习触发

1. 为什么“token 多”和“上下文窗口大”都不等于模型会正确使用证据？
2. Prompt、Prompt Engineering 和 Context Engineering 的边界是什么？哪个负责“选什么资料放进去”？
3. 一个带引用的 RAG 答案仍然可能 hallucinate 吗？如何检查？

## 相关链接

- [[LLM 主题]]
- [[LLM]]
- [[Token]]
- [[Context Window]]
- [[Prompt]]
- [[Prompt Engineering]]
- [[Hallucination]]
- [[Context Engineering]]
- [[RAG Citation Faithfulness]]
- [[LLM 基础结构对比]]
