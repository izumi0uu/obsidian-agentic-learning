---
type: concept
topic:
  - llm
  - reasoning
  - decoding
status: seed
created: 2026-05-23
updated: 2026-05-23
last_checked: 2026-05-23
freshness: stable
conflicts: []
aliases:
  - self-consistency
  - Self Consistency
  - self consistency
  - 自洽采样
  - 多路径投票
  - 多次采样投票
source:
  - "[[AI Engineering From Scratch - Few-Shot CoT]]"
  - "[[Plan-and-Solve Prompting - Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models]]"
  - "[[raw/repos/xiaolinnote/questions/121 ai llm 17. 什么是 CoT？为啥效果好？它有什么缺点或局限性？]]"
  - "[[raw/repos/xiaolinnote/questions/122 ai llm 12. 大模型生成文本时的解码策略有哪些？贪心、Beam Search、采样分别什么时候用？]]"
evidence:
  - "[[AI Engineering From Scratch - Few-Shot CoT#关键事实]]"
  - "[[raw/repos/xiaolinnote/questions/121 ai llm 17. 什么是 CoT？为啥效果好？它有什么缺点或局限性？#Self-Consistency：CoT 的升级版]]"
  - "[[raw/repos/xiaolinnote/questions/122 ai llm 12. 大模型生成文本时的解码策略有哪些？贪心、Beam Search、采样分别什么时候用？#进阶策略：推测解码与 Self-Consistency]]"
related:
  - "[[Few-shot CoT]]"
  - "[[Zero-shot CoT]]"
  - "[[Tree of Thoughts]]"
  - "[[Reasoning Trace]]"
  - "[[Top-K]]"
  - "[[Hallucination]]"
---

# Self-Consistency

## 一句话

Self-Consistency 是对同一问题采样多条推理路径，再从最终答案中做多数投票或聚合，用更多调用成本换更稳的推理答案。

## 概念详解

Self-Consistency 的出发点是：单条 CoT 路径可能在中间走错，但正确答案往往可以由多种不同路径抵达。如果对同一个问题用非零 temperature 生成多条相互独立的 reasoning trace，再只比较最终答案，随机错误路径更不容易一致收敛，正确答案更可能成为多数。

它和贪心解码的关系很关键。temperature 为 0 时，多次调用通常会得到高度相似甚至相同的路径，多数投票没有意义。Self-Consistency 需要适度采样，让路径有差异；但 temperature 太高又会让路径质量下降。工程上常用 N=3、5 或 10，而不是无限扩大，因为调用次数、延迟和 token 成本线性增长，收益会递减。

Self-Consistency 适合数学推理、逻辑题、符号推理、某些高风险决策的候选答案确认。它不适合事实未知或外部信息缺失的问题：如果模型没有证据，多次采样可能只是让多个幻觉互相投票。它也不适合答案空间开放、没有明确可聚合 final answer 的任务，例如创意写作或复杂方案设计。

现代 reasoning model 可能在内部做多步推理、验证或采样式搜索，因此显式 Self-Consistency 的边际收益会变小。但作为工程策略，它仍然有清晰价值：当单次输出不够可信、答案可抽取、成本可接受时，用多路径投票提高鲁棒性。

Self-Consistency 的关键产物不是最长的推理链，而是可规范化的最终答案集合。实践里通常要把每条样本的 final answer 提取成统一形式，例如数字、小写标签、枚举值或结构化字段；否则“20”“20 students”“twenty”会被误分成不同票。对于开放式方案题，更适合先把候选方案交给 rubric / judge / verifier 排序，而不是把自然语言段落直接多数投票。

它也不是免费的可靠性按钮。Self-Consistency 增加的是 test-time compute：每多采样一条路径，就增加一次模型调用和一段推理 token 成本。只有当错误主要来自随机路径偏差、而不是题目理解错误、事实缺失或系统性偏见时，多路径投票才更可能带来收益。

## 它解决什么问题

它解决的是单条推理路径偶发出错的问题。与其相信一次生成的 reasoning trace，不如让模型从多个路径抵达答案，然后看最终答案是否一致。

## 它不是什么

Self-Consistency 不是 [[Tree of Thoughts]]。它通常是多条完整路径生成完后再投票；ToT 会在中间状态评估、剪枝和继续搜索。

它不是事实核查。多数模型输出一致不等于事实真实；对于需要外部证据的问题，应使用 RAG、工具、引用核查或 verifier。

它也不是“自洽偏见”的普通中文含义。只有指 CoT / reasoning 的多路径采样与答案投票时，才链接本卡。

## 最小例子

```text
Problem: A class has 30 students. 1/3 are absent. How many are present?

Sample 1 final answer: 20
Sample 2 final answer: 20
Sample 3 final answer: 10
Sample 4 final answer: 20
Sample 5 final answer: 20

Vote:
20 -> 4 votes
10 -> 1 vote

Final answer: 20
Confidence proxy: 4/5
```

投票只在最终答案可抽取、可规范化时才有效。

## 常见误解 / 风险

- 误解：Self-Consistency 可以修复所有幻觉。没有证据的问题，多路径也可能共同编错。
- 误解：N 越大越好。N 增大带来成本和延迟，且收益递减。
- 误解：temperature 越高路径越好。高温只是更发散，不代表更正确。
- 风险：答案抽取规则不稳，会把等价答案拆成多个票。
- 风险：系统性错误不会被投票抵消，例如题目理解错或常识前提错。

## 边界细节

和附近概念的最小边界：

```text
Few-shot CoT: worked examples -> one reasoning path
Self-Consistency: sample N reasoning paths -> majority final answer
Tree of Thoughts: evaluate/search partial thoughts before final answer
ReAct: reasoning path can call tools and receive observations
```

Self-Consistency 的关键是“多样路径 + 可聚合答案”。如果任务没有清晰 final answer，应该改成 rubric scoring、candidate comparison 或 workflow evaluation，而不是机械投票。

## 现代性状态

- 判定：foundation / current-practice。
- 稳定部分：test-time compute 可以用多次采样提升部分任务鲁棒性。
- 当前工程吸收：多数投票、best-of-N、verifier reranking、consistency checks 和 reasoning-model internal verification 都吸收了类似思想。
- 不应夸大：显式 Self-Consistency 是昂贵策略，常作为 fallback 或高风险路径使用。

## 现代系统怎么吸收 Self-Consistency 的价值

现代系统会把它放进 escalation strategy：先跑单次低成本 CoT；若答案置信度低、任务重要或校验失败，再采样多条路径投票。对结构化输出任务，还会要求每条路径输出标准字段，方便投票、比较和审计。对事实任务，则更倾向用 retrieval / tool / citation verifier，而不是只靠模型内部一致性。

## 证据锚点

- [[AI Engineering From Scratch - Few-Shot CoT#关键事实]]：支持 Self-Consistency 的多路径采样、投票和成本边界。
- [[raw/repos/xiaolinnote/questions/121 ai llm 17. 什么是 CoT？为啥效果好？它有什么缺点或局限性？#Self-Consistency：CoT 的升级版]]：支持 CoT 基础上的多次采样投票解释。
- [[raw/repos/xiaolinnote/questions/122 ai llm 12. 大模型生成文本时的解码策略有哪些？贪心、Beam Search、采样分别什么时候用？#进阶策略：推测解码与 Self-Consistency]]：支持它和采样 / temperature 的关系。
- Evidence type: course source note + raw tutorial/interview source + engineering synthesis.
- Boundary: 本卡把 Self-Consistency 限定为 CoT / reasoning 任务中的多路径采样与答案聚合；不把普通“自洽性”、事实核查、beam search、verifier reranking 或 Tree of Thoughts 搜索混为同义词。
- Confidence: medium-high。

## 复习触发

1. 为什么 Self-Consistency 不能用 temperature=0？
2. 它和 Tree of Thoughts 的最小区别是什么？
3. 为什么多数投票不能证明事实正确？
4. 什么样的任务适合用 N=3 或 N=5 做 fallback？

## 相关链接

- [[Few-shot CoT]]
- [[Zero-shot CoT]]
- [[Tree of Thoughts]]
- [[Reasoning Trace]]
- [[Top-K]]
- [[Hallucination]]
