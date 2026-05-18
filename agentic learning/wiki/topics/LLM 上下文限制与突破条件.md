---
type: map
topic:
  - llm
  - context
  - long-context
status: seed
created: 2026-05-17
updated: 2026-05-17
source:
  - "[[Context Window]]"
  - "[[Context Engineering]]"
  - "[[prompt-engineering-vs-context-engineering-for-agents.svg]]"
  - "[[LLM 输入输出基础边界对比]]"
  - "[[130 01_AI 04_上下文工程与记忆 Wide Research Beyond the Context Window]]"
  - "[[138 01_AI 04_上下文工程与记忆 补充材料：如何突破上下文窗口限制]]"
related:
  - "[[LLM 主题]]"
  - "[[Context Window]]"
  - "[[Context Engineering]]"
  - "[[Memory]]"
  - "[[RAG]]"
  - "[[LLM 基础结构对比]]"
---

# LLM 上下文限制与突破条件

![[prompt-engineering-vs-context-engineering-for-agents.svg]]

## 一句话总览

LLM 的上下文限制不是一个单独参数，而是容量、计算、结构、有效使用和治理共同形成的边界。未来突破也不会只是“把 [[Context Window]] 做大”，而是模型结构、训练数据、推理系统、外部 [[Memory]] / [[RAG]] 和 [[Context Engineering]] 一起进步。

最小边界：[[Context Window]] 解决“一次调用能看见多少”；[[Memory]]、[[RAG]] 和 [[Context Engineering]] 解决“哪些信息应该被保存、检索、选择、排序并被正确使用”。

## 学习价值

这个问题连接了三层学习：

- LLM 基础：token、context window、attention、position encoding 和生成预算。
- 工程运行：[[KV Cache]]、延迟、成本、吞吐、压缩、缓存和 prompt 组织。
- Agent / RAG 系统：外部记忆、检索、任务分解、trace、引用、权限和评估。

如果只把它理解成“模型窗口太小”，就会错过真正的工程判断：长上下文是容量改善，不自动等于长期记忆、证据可靠性或任务稳定性。

## 限制分层

| 层 | 受什么限制 | 典型表现 | 工程含义 |
|---|---|---|---|
| 容量限制 | [[Token]] budget 和 [[Context Window]] | system prompt、历史、tool schema、RAG 证据和输出预算互相挤占 | 需要摘要、裁剪、检索、分段执行和输出预算管理 |
| 计算限制 | attention 复杂度、[[KV Cache]]、显存、内存带宽、延迟和成本 | 序列变长后推理更慢、显存占用更高、并发吞吐下降 | 需要 [[KV Cache]] 优化、prompt caching、批处理、压缩和模型/硬件选型 |
| 结构限制 | [[Self-Attention]]、[[Multi-Head Attention]]、[[Positional Encoding]] 和训练长度分布 | 模型能接收长输入，不代表能稳定处理远距离依赖 | 长上下文能力需要位置鲁棒性、长序列训练和专门评测 |
| 有效使用限制 | 噪声、冲突、无关材料、位置偏置、Lost in the Middle | 正确证据在窗口里，但模型忽略、误读或被低质量片段干扰 | 需要排序、去重、重排、结构化提示、引用规则和 evidence selection |
| 治理限制 | 来源、权限、时效、prompt injection、审计和评估 | 过期资料、越权资料或恶意内容进入上下文会污染答案 | 需要 [[Context Engineering]]、access control、citation、trace 和 eval harness |

小边界：输入进了窗口，只表示“可见”；能否被模型优先、正确、可追溯地使用，是另一个问题。

上图把这个边界压得很直观：Prompt Engineering 侧重点是单轮输入怎么写清楚；Context Engineering 侧重点是从可能的文档、工具、memory、历史和指令中筛出本轮最该进入窗口的材料。

## 未来突破需要什么

### 模型侧

模型侧突破包括更长的训练上下文、更稳的位置编码 / attention 机制、更好的长距离依赖建模，以及覆盖真实长任务的训练和评测。这里的关键不是把参数表里的 context length 写大，而是让模型在长输入里仍能保持位置鲁棒性、证据定位能力和指令遵循稳定性。

### 推理系统侧

推理系统侧突破包括 [[KV Cache]] 压缩 / 量化 / 分页管理、prompt caching、Flash Attention 类实现优化、更好的批处理调度、显存/带宽效率和硬件支持。长上下文会把成本、延迟和吞吐问题放大，所以“能跑”之外还要问“能不能便宜、稳定、低延迟地跑”。

### 系统工程侧

系统工程侧突破包括外部记忆、RAG、任务分解、阶段摘要、state projection、trace、citation、权限过滤和上下文预算策略。[[130 01_AI 04_上下文工程与记忆 Wide Research Beyond the Context Window]] 的核心价值就在这里：突破窗口不只是增加 token，而是把单个巨大上下文改造成分层、分阶段、可检索、可审计的外部系统。

## 判断框架

遇到“上下文不够”时，先判断瓶颈在哪一层：

| 现象 | 先看哪里 | 常见解法 |
|---|---|---|
| 输入放不下 | [[Context Window]], [[Token]] | 摘要、检索、裁剪、分批处理、输出预算调整 |
| 放得下但很慢/很贵 | [[Multi-Head Attention]], [[KV Cache]], 推理栈 | 缓存、压缩、批处理、换模型、减少固定前缀和无用上下文 |
| 正确资料在窗口里但答错 | [[Context Engineering]], [[RAG Evaluation]] | 重排、去重、证据分段、引用规则、降低噪声 |
| 长任务前后矛盾 | [[Memory]], [[Agent State]], [[Trace]] | 阶段性结论、外部状态、回溯检索、一致性检查 |
| 资料过期或越权 | [[RAG]], [[RAG Citation Faithfulness]], access control | 来源标注、权限过滤、数据 freshness、审计日志 |

## 它不是什么

- 不是“模型支持 1M token 就万事大吉”。大窗口仍可能放入错误、过期、冲突或无关材料。
- 不是 [[RAG]] 的替代品。RAG 和 memory 的价值会从“把窗口补足”变成“选择高价值信息并保持证据可追溯”。
- 不是长期记忆。窗口是一次调用的可见范围；长期记忆需要写入、检索、更新、删除和权限机制。
- 不是只靠 prompt 能解决。长上下文可靠性还依赖模型训练、推理系统、数据治理和评估闭环。

## 现代性状态

- 判定：foundation + current-practice + watch。
- 稳定部分：LLM 受 token/context window、attention 计算、外部上下文选择和输出可靠性约束。
- 当前实践：生产系统通常组合长上下文、RAG、memory、context engineering、trace 和 evaluation，而不是只依赖单次窗口扩大。
- watch 部分：具体窗口大小、[[KV Cache]] 方案、attention 变体、位置编码扩展、prompt caching 计费和长上下文 benchmark 都会快速变化。

## 证据锚点

- 概念卡：[[Context Window#概念详解]], [[Context Engineering#概念详解]], [[LLM 输入输出基础边界对比#Context Window vs Memory]], [[LLM 基础结构对比#Positional Encoding vs Context Window]]。
- raw evidence：[[130 01_AI 04_上下文工程与记忆 Wide Research Beyond the Context Window#题目正文]], [[138 01_AI 04_上下文工程与记忆 补充材料：如何突破上下文窗口限制#题目正文]]。
- 技术侧 raw evidence：[[131 ai llm 3. 多头注意力（MHA）有哪些局限？MQA、GQA、Flash Attention 怎么解决？#页面正文]], [[128 ai llm 14. KV Cache 是什么？Prompt Caching 的原理是什么？#页面正文]], [[134 ai llm 4. 大模型的位置编码是干什么用的？sin-cos、RoPE、ALiBi 有什么区别？#页面正文]]。
- Evidence type: vault concept synthesis + interview raw notes + engineering inference.
- Boundary: 本页不记录任何供应商的最新 context length 数字；具体模型参数需要回到官方文档和最新产品说明。

## 复习触发

1. 为什么 context window 大不等于 memory 强？
2. 为什么“正确证据已经进上下文”仍可能答错？
3. 长上下文的计算瓶颈和上下文治理瓶颈分别是什么？
4. 如果一个 Agent 长任务中途遗忘，你会先扩大窗口，还是先改 state / memory / trace？为什么？

## 相关链接

- [[LLM 主题]]
- [[LLM 输入输出基础边界对比]]
- [[LLM 基础结构对比]]
- [[Context Window]]
- [[KV Cache]]
- [[Context Engineering]]
- [[Context RAG Memory 对比]]
- [[Memory]]
- [[RAG]]
