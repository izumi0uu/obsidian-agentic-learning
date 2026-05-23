---
type: concept
topic:
  - llm
  - prompting
status: seed
created: 2026-05-23
updated: 2026-05-23
last_checked: 2026-05-23
freshness: stable
conflicts: []
aliases:
  - few-shot prompting
  - Few-shot
  - few-shot
  - 少样本提示
  - 少样本提示词
source:
  - "[[AI Engineering From Scratch - Few-Shot CoT]]"
  - "[[AI Engineering From Scratch - Prompt Engineering]]"
  - "[[Prompt Engineering]]"
evidence:
  - "[[AI Engineering From Scratch - Few-Shot CoT#关键事实]]"
  - "[[AI Engineering From Scratch - Prompt Engineering#机制拆解（工程综合）]]"
  - "[[Prompt Engineering#概念详解]]"
related:
  - "[[Prompt Engineering]]"
  - "[[Prompt]]"
  - "[[Few-shot CoT]]"
  - "[[Zero-shot CoT]]"
  - "[[KV Cache]]"
  - "[[LLM Training Pipeline]]"
---

# Few-shot Prompting

## 一句话

Few-shot Prompting 是在 prompt 里放入少量输入 / 输出示例，让模型在推理时从示例中临时归纳任务格式、标签边界、风格和输出约束。

## 概念详解

Few-shot Prompting 的核心不是“给模型更多资料”，而是用示例把抽象指令变成可模仿的任务模式。相比只写“请分类这段文本”，few-shot 会先展示几条“输入是什么、应该输出什么、格式怎么写、标签怎么选”的样例，再让模型处理新输入。模型没有因此更新参数；示例只是进入当前上下文，影响后续 token 生成。

它适合格式敏感、标签边界微妙、领域术语固定、输出风格需要对齐的任务。示例比自然语言规则更容易传达“什么算正例、什么算反例、答案长什么样”。这也是它和 [[Prompt Engineering]] 的关系：few-shot 是 prompt engineering 可以使用的一种局部模式，不是全部 prompt 工程。

示例质量通常比数量更重要。课程强调语义相似、标签覆盖和难度匹配：目标输入是什么类型，就选相近案例；分类任务要覆盖主要标签；复杂任务要让示例难度接近目标问题。太少示例信号不足，太多示例会浪费 context window、增加噪声，并可能让模型过度模仿不该模仿的细节。

工程上还要考虑运行成本。固定 few-shot 前缀会消耗 token，但在批量请求、客服、代码审查或分类系统里，这类前缀也可能被 prompt caching / KV cache 复用。是否值得使用 few-shot，要看准确率提升是否覆盖 token 成本、延迟和维护样例集的成本。

还有一个容易忽略的边界：few-shot 示例本身也是 prompt 的一部分，所以它会同时传达任务模式和潜在偏差。一个示例如果把“无法判断”强行归到某个标签，模型会学到这个决策偏好；一个示例如果包含冗长解释，模型也可能在本该简短输出时模仿冗长格式。因此 few-shot 样例需要像测试用例一样维护：覆盖典型正例、边界反例和预期输出，而不是随手复制几个看起来相似的样本。

## 它解决什么问题

它解决的是“抽象指令不够具体，模型需要猜格式和边界”的问题。示例可以把任务定义、输出风格、字段形状和标签含义显式放进上下文。

## 它不是什么

Few-shot Prompting 不是 fine-tuning。它只在本次调用的上下文里给示例，不改变模型权重。

它不是 RAG。RAG 检索外部证据来回答事实问题；few-shot 示例主要定义任务模式。示例可以包含领域文本，但它们的作用不等于事实来源。

它也不是 [[Few-shot CoT]] 的同义词。Few-shot CoT 是 few-shot 的一个特殊形式：示例里包含中间推理步骤。

## 最小例子

```text
任务：把评论分成 positive / negative。

Example 1:
Input: "The battery lasts all day."
Output: positive

Example 2:
Input: "The screen cracked after two days."
Output: negative

Now classify:
Input: "The camera is sharp, but the phone gets hot."
Output:
```

这个 prompt 没有训练模型，但让模型看到标签空间和输出格式。

## 常见误解 / 风险

- 误解：few-shot 越多越好。示例过多会挤占上下文、增加噪声，也可能让模型过拟合示例表面形式。
- 误解：few-shot 可以替代清晰指令。示例和规则最好互补；复杂任务仍需要任务说明、约束和输出格式。
- 误解：示例里出现的事实都能当作证据。few-shot 示例主要是格式和模式，不应替代可引用证据。
- 风险：示例分布偏了，模型会稳定复现偏差。
- 风险：标签不均衡时，模型可能偏向出现更多的标签。

## 边界细节

和 [[Zero-shot CoT]]：zero-shot 不给示例；few-shot 给示例。是否带推理步骤是另一个维度。

和 [[Few-shot CoT]]：Few-shot Prompting 可以只给输入 / 输出；Few-shot CoT 的示例还包含 reasoning chain。

和 [[LLM Training Pipeline|微调]]：few-shot 是推理时条件化；微调是训练或适配阶段改变模型行为。常见工程路径是先用 prompt + few-shot 验证任务边界，再决定是否用训练样本固化。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：示例作为临时任务定义仍然是 LLM 应用基础技巧。
- 当前工程吸收：prompt template、example selector、semantic similarity selection、prompt caching、eval set 和 prompt registry 都会围绕 few-shot 样例集运转。
- 不应夸大：强模型和 reasoning model 降低了某些任务对 few-shot 的依赖，但格式敏感和领域边界任务仍常需要示例。

## 现代系统怎么吸收 Few-shot Prompting 的价值

现代系统通常把示例库从 prompt 字符串里拆出来管理：按任务类型、标签、难度和语言维护样例；上线前用 eval set 比较不同示例组合；高吞吐系统用 prompt caching 降低固定前缀成本；RAG / Agent 系统里则把示例、证据和工具说明分层装配，避免示例污染事实依据。

## 证据锚点

- [[AI Engineering From Scratch - Few-Shot CoT#关键事实]]：支持 few-shot 与 zero-shot、示例选择和任务适用边界。
- [[AI Engineering From Scratch - Prompt Engineering#机制拆解（工程综合）]]：支持 few-shot 作为推理时临时任务定义，不更新模型参数。
- [[Prompt Engineering#概念详解]]：支持 prompt engineering 将示例、格式、约束和评测纳入工程流程。
- Evidence type: course source note + existing concept card + engineering synthesis.
- Boundary: 本卡只记录示例作为推理时任务定义的 prompting 方法；不把 few-shot 当作事实检索、参数训练、CoT 专属技术或稳定安全边界。
- Confidence: medium-high。

## 复习触发

1. Few-shot Prompting 为什么不是 fine-tuning？
2. 示例选择的三个关键维度是什么？
3. 什么时候 few-shot 会比自然语言规则更稳？
4. few-shot 示例为什么不能当事实证据使用？

## 相关链接

- [[Prompt Engineering]]
- [[Prompt]]
- [[Few-shot CoT]]
- [[Zero-shot CoT]]
- [[KV Cache]]
- [[LLM Training Pipeline]]
