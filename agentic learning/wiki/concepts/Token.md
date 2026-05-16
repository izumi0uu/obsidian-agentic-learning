---
type: concept
topic:
  - llm
status: growing
created: 2026-05-12
updated: 2026-05-16
last_checked: 2026-05-12
freshness: stable
source:
  - "[[LLM]]"
  - "[[Attention Is All You Need]]"
evidence:
  - "[[LLM#概念详解]]"
  - "[[Attention Is All You Need#Ingest 摘要]]"
  - "[[Attention Is All You Need#可以拆成概念卡]]"
related:
  - "[[LLM]]"
  - "[[Context Window]]"
  - "[[Prompt]]"
  - "[[Transformer]]"
---

# Token

## 一句话

Token 是 LLM 处理文本的基本序列单位，可能是词、词片段、字符或符号片段；模型读写的不是“整段文字”，而是 token 序列。

## 概念详解

LLM 生成文本时，本质上是在当前上下文中预测下一个 token。人看到的是句子、段落和代码，模型内部先通过 tokenizer 把输入切成 token ID，再把这些 ID 变成向量表示并进入 Transformer。[[LLM]] 卡已经强调 LLM 根据上下文生成 token 序列；[[Attention Is All You Need]] 作为 Transformer 地基，讨论的是序列位置、embedding、attention 等机制，这些都建立在离散序列单位之上。

Token 的边界很重要，因为它影响成本、延迟、上下文窗口、截断、chunking 和输出长度。中文、英文、代码、emoji、空格、标点和罕见词在不同 tokenizer 下切法不同；“一个词”不一定等于一个 token。学习 Agent / RAG 时，token 还决定了哪些检索片段能放进 prompt、工具 schema 有多长、trace 摘要需要压缩到什么程度。

证据边界：本卡不绑定某个供应商 tokenizer 的具体切分规则；这些规则和模型产品会变化。稳定概念是：LLM 使用离散 token 序列作为输入输出单位，context window 和成本通常围绕 token 数计算。

Token 也是成本、延迟和上下文预算的基本单位。prompt 里的每段说明、工具 schema、检索 chunk、历史消息和输出都要消耗 token；不同 tokenizer 对中文、英文、代码和符号的切分也不同。学习 Agent/RAG 时，token 不是抽象小字节，而是直接影响“能放多少证据、要不要摘要、是否需要检索、输出预算够不够”的工程约束。
## 它解决什么问题

Token 让文本可以变成模型可计算的离散序列。没有 tokenization，模型无法把自然语言、代码和符号稳定映射到向量空间。

## 它不是什么

Token 不是自然语言里的“单词”。一个英文单词可能被拆成多个 token，一个中文字符可能是一个或多个 token，代码符号和空格也可能占 token。

Token 也不是 [[Context Window]]。token 是单位，context window 是一次调用能容纳的 token 数边界。

## 最小例子

```text
文本：unbelievable
可能切成：un + believable

文本：function_call
可能切成：function + _ + call
```

具体切法取决于 tokenizer，不要把示例当成固定事实。

## 常见误解 / 风险

- 误解：token 等于 word。
- 误解：上下文窗口写 128k，就能放 128k 个汉字或单词。
- 风险：RAG chunk 只按字符切，实际 token 超预算。
- 风险：工具 schema、系统提示和历史消息占掉大量 token，压缩了证据空间。

## 边界细节

和 [[Prompt]] 的边界：prompt 是给模型的输入内容组织；token 是 prompt 被模型处理时的计量单位。

和 [[Context Window]] 的边界：context window 是容量上限；token 是容量单位。

和 [[Chunking]] 的边界：chunking 常需要按 token 预算设计，否则检索片段可能放不进上下文。

## 现代性状态

- 判定：foundation。
- 稳定部分：LLM 以 token 序列为输入输出单位。
- 易变部分：具体 tokenizer、压缩技术、计费方式和多模态 token 计算会变化。
- 复查点：学习具体模型 API 时，需要查官方 tokenizer / pricing，而不是靠通用估算。

## 现代系统怎么吸收 Token 的价值 / 局限

现代系统会在 prompt builder、RAG chunker、memory summarizer 和 cost monitor 中显式计算 token。Agent runtime 也会在上下文接近上限时压缩历史、截断低优先级材料或触发 context compaction。

局限是 token 只是长度单位，不代表信息质量。更多 token 不等于更可靠；错的资料放得越多，模型可能越混乱。

## 证据锚点

- Concept anchor: [[LLM#概念详解]]
- Source anchor: [[Attention Is All You Need#Ingest 摘要]]
- Source anchor: [[Attention Is All You Need#可以拆成概念卡]]
- Evidence type: LLM concept synthesis + Transformer source note + engineering synthesis.

- Boundary: Token 是模型处理序列的单位，不等于汉字/英文单词/字符，也不是 context window 或 prompt 本身。
## 复习触发

1. 为什么 token 不等于 word？
2. token、prompt 和 context window 三者是什么关系？
3. RAG chunking 为什么要考虑 token 而不是只看字符数？

## 相关链接

- [[LLM]]
- [[Context Window]]
- [[Prompt]]
- [[Chunking]]
- [[LLM 输入输出基础边界对比]]
