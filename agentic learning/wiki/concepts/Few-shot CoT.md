---
type: concept
topic:
  - llm
  - prompting
  - reasoning
status: seed
created: 2026-05-23
updated: 2026-05-23
last_checked: 2026-05-23
freshness: stable
conflicts: []
aliases:
  - few-shot CoT
  - Few-shot Chain-of-Thought
  - few-shot chain of thought
  - 少样本 CoT
  - 少样本思维链
source:
  - "[[AI Engineering From Scratch - Few-Shot CoT]]"
  - "[[Zero-shot CoT]]"
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]"
  - "[[raw/repos/xiaolinnote/questions/121 ai llm 17. 什么是 CoT？为啥效果好？它有什么缺点或局限性？]]"
evidence:
  - "[[AI Engineering From Scratch - Few-Shot CoT#关键事实]]"
  - "[[Zero-shot CoT#常见误解]]"
  - "[[raw/repos/xiaolinnote/questions/121 ai llm 17. 什么是 CoT？为啥效果好？它有什么缺点或局限性？#题目正文]]"
related:
  - "[[Few-shot Prompting]]"
  - "[[Zero-shot CoT]]"
  - "[[Self-Consistency]]"
  - "[[Tree of Thoughts]]"
  - "[[Reasoning Trace]]"
  - "[[Plan-and-Solve Prompting]]"
---

# Few-shot CoT

## 一句话

Few-shot CoT 是在 prompt 里给出若干包含“问题、逐步推理、最终答案”的示例，让模型处理新问题时模仿同样的推理格式。

## 概念详解

Few-shot CoT 结合了 [[Few-shot Prompting]] 和 chain-of-thought 的两个信号：示例告诉模型任务长什么样，推理步骤告诉模型中间过程应该怎样展开。它比 Zero-shot CoT 更重，但也更可控，因为模型不只看到“请一步步思考”的抽象要求，还看到具体问题如何拆、最终答案如何标记、推理文本应该多细。

这对数学、逻辑、符号推理、固定格式推导和可教学复盘的任务很有用。示例中的 reasoning chain 会成为目标问题前的上下文模式，模型后续生成更容易沿着同类结构展开。尤其当最终答案需要被程序抽取时，few-shot CoT 示例还可以把“最后一行用固定格式给答案”示范出来，降低后续投票、评分或解析难度。

它的代价也明确：示例会占上下文、增加 token 成本，并可能把示例里的错误步骤或偏见复制到新题。对于简单事实问题、单步分类、低延迟高吞吐任务，Few-shot CoT 往往过重。对于现代 reasoning model，显式 few-shot CoT 的边际收益也可能变小，因为模型内部已经有更强的推理行为；但当你需要固定输出格式、教学式推导或可检查中间过程时，它仍有价值。

工程上，Few-shot CoT 的示例应当同时示范“怎么推”和“怎么收束”。如果示例只有很长的中间推理，却没有稳定的 final answer 标记，后续系统很难抽取答案、做 [[Self-Consistency]] 投票或交给 verifier。反过来，如果示例把每一步写得过度模板化，模型可能在不适合该模板的问题上机械套用。因此样例选择要看任务族、难度、答案格式和失败样本，而不是只追求更多 reasoning text。

这也解释了它和现代隐藏 reasoning 的关系：现代模型可能不需要你显式展示完整推理链，也可能不允许返回完整内部 CoT。但 Few-shot CoT 仍能作为“外部教学脚手架”使用，尤其用于小模型、格式迁移、教学复盘、离线评测和需要固定答案格式的管线。

## 它解决什么问题

它解决的是 Zero-shot CoT 格式和深度不稳定的问题。只说“请一步步思考”时，模型可能步骤太少、格式漂移或答案不易抽取；Few-shot CoT 用 worked examples 把推理粒度和答案格式固定下来。

## 它不是什么

Few-shot CoT 不是 [[Self-Consistency]]。它仍然可以是一次调用、一条推理路径；Self-Consistency 是采样多条路径再投票。

它不是 [[Tree of Thoughts]]。Few-shot CoT 主要示范线性 reasoning chain；ToT 会在中间状态展开多个候选并评估、剪枝。

它也不是模型真实思维的证明。它生成的是可读推理文本，可能有用，也可能是事后合理化或包含错误步骤。

## 最小例子

```text
Q: Tom has 3 books and buys 2 more. How many books?
A: Tom starts with 3 books. He buys 2 more, so 3 + 2 = 5. The answer is 5.

Q: Mia has 10 candies and gives away 4. How many remain?
A: Mia starts with 10 candies. She gives away 4, so 10 - 4 = 6. The answer is 6.

Q: Leo has 7 pens and buys 5 more. How many pens?
A:
```

模型会更倾向按同样的推理格式补完第三题。

## 常见误解 / 风险

- 误解：Few-shot CoT 总是比 Zero-shot CoT 好。它通常更稳，但不一定值得额外 token 成本。
- 误解：示例推理越长越好。冗长示例可能引入噪声，并让模型学到不必要的表达形式。
- 误解：Few-shot CoT 能自动纠错。它只是示范推理格式，没有外部 verifier。
- 风险：示例答案错或步骤跳跃，会把错误 pattern 带到新问题。
- 风险：示例和目标任务难度不匹配时，模型可能套错解法。

## 边界细节

最小谱系：

```text
Zero-shot: task -> answer
Few-shot Prompting: examples -> task -> answer
Zero-shot CoT: task -> reasoning -> answer
Few-shot CoT: worked examples -> task -> reasoning -> answer
Self-Consistency: sample N reasoning paths -> vote
Tree of Thoughts: branch/evaluate/search partial thoughts
```

Few-shot CoT 仍然是 prompt 层方法。它可以被 [[Self-Consistency]]、[[Prompt Chaining]] 或 [[Tree of Thoughts]] 包起来，但自身不包含投票、搜索、工具调用或状态机。

## 现代性状态

- 判定：foundation / transitional / current-practice。
- 稳定部分：worked examples 仍是教模型稳定输出推理格式的有效方法。
- 历史过渡：早期 CoT 研究依赖显式示例来提升复杂任务表现；现代 reasoning model 和内部 reasoning tokens 吸收了部分价值。
- 当前工程吸收：生产系统常把完整推理链改造成结构化步骤、rubric、答案格式、verification artifact 或隐藏 scratchpad，而不是无条件展示给用户。

## 现代系统怎么吸收 Few-shot CoT 的价值

现代系统会把 few-shot CoT 样例纳入 eval harness：比较不同示例组合对准确率、可解析率、延迟和成本的影响。高风险任务通常还会加 verifier、unit test、tool execution 或 human review，避免把“看起来有推理步骤”误当成可靠性。

## 证据锚点

- [[AI Engineering From Scratch - Few-Shot CoT#关键事实]]：支持 Few-shot CoT 相比 Zero-shot CoT 的示例和格式边界。
- [[Zero-shot CoT#常见误解]]：支持两者稳定性与成本差异。
- [[raw/repos/xiaolinnote/questions/121 ai llm 17. 什么是 CoT？为啥效果好？它有什么缺点或局限性？#题目正文]]：支持 Few-shot CoT 和 Zero-shot CoT 的面试解释边界。
- Evidence type: course source note + existing concept card + raw tutorial/interview source.
- Boundary: 本卡只讨论带 worked reasoning examples 的线性 prompt 方法；不把它等同于多路径投票、树搜索、工具调用、真实内部思维或 reasoning model 训练机制。
- Confidence: medium-high。

## 复习触发

1. Few-shot Prompting 和 Few-shot CoT 的差别是什么？
2. Few-shot CoT 为什么更容易支持答案抽取？
3. 它和 Self-Consistency 的最小区别是什么？
4. 什么时候 Few-shot CoT 的 token 成本不值得？

## 相关链接

- [[Few-shot Prompting]]
- [[Zero-shot CoT]]
- [[Self-Consistency]]
- [[Tree of Thoughts]]
- [[Reasoning Trace]]
- [[Plan-and-Solve Prompting]]
