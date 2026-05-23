---
type: concept
topic:
  - llm
  - reasoning
  - planning
  - prompting
status: seed
created: 2026-05-23
updated: 2026-05-23
last_checked: 2026-05-23
freshness: stable
conflicts: []
aliases:
  - ToT
  - Tree-of-Thought
  - Tree of Thought
  - 思维树
  - 树状思维
source:
  - "[[Tree of Thoughts - Deliberate Problem Solving with Large Language Models]]"
  - "[[raw/repos/xiaolinnote/questions/005 ai agent 14. 如何赋予 LLM 规划能力？]]"
  - "[[raw/repos/agent_java_offer/questions/014 01_AI 01_Agent基础 在 Agent 的设计中，“规划能力”至重要。请谈谈目前有哪些主流方法可以赋予 LLM 规划能力？（例如 CoT, ToT, GoT等）]]"
evidence:
  - "[[Tree of Thoughts - Deliberate Problem Solving with Large Language Models#需要我读的内容]]"
  - "[[raw/repos/xiaolinnote/questions/005 ai agent 14. 如何赋予 LLM 规划能力？#ToT：从「一条链」到「一棵树」，解决走错方向的问题]]"
  - "[[raw/repos/agent_java_offer/questions/014 01_AI 01_Agent基础 在 Agent 的设计中，“规划能力”至重要。请谈谈目前有哪些主流方法可以赋予 LLM 规划能力？（例如 CoT, ToT, GoT等）#题目正文]]"
related:
  - "[[Zero-shot CoT]]"
  - "[[Few-shot CoT]]"
  - "[[Self-Consistency]]"
  - "[[Plan-and-Solve Prompting]]"
  - "[[Reasoning Trace]]"
  - "[[Planning]]"
  - "[[ReAct]]"
  - "[[ReWOO]]"
  - "[[Agent Workflow]]"
  - "[[Task Success Rate]]"
---

# Tree of Thoughts

## 一句话

Tree of Thoughts（ToT，思维树）是把 [[Zero-shot CoT]] 的单条推理链扩展成多分支搜索：模型先生成多个候选 thought，再评估、剪枝、回溯或继续展开，用更多推理时计算换更高的复杂任务成功率。

## 概念详解

Tree of Thoughts 的出发点是 CoT 的单路径局限。普通 CoT 让模型把推理步骤写出来，但通常还是沿着一条链往下生成：早期方向如果错了，后续 token 会继续受这个错误路径影响。ToT 把“下一步怎么想”变成一个搜索问题：在某个中间状态下，模型不只生成一个后续步骤，而是生成多个候选 thought，再让模型或外部搜索控制器评估这些候选，保留更有希望的路径继续展开，必要时回溯。

这里的 thought 不是神秘的“真实脑内想法”，而是一个可被模型生成、评分和继续扩展的文本中间单位。它可以是一种解题方向、一个局部计划、一段中间推理、一个候选子目标，粒度比 token 更粗。ToT 的关键不在于“让回答变长”，而在于把中间推理状态显式化成可比较的候选集合。

论文证据支持的核心边界是：ToT 适合需要探索、战略前瞻或早期决策很关键的任务，例如 Game of 24、创意写作、mini crossword。这类任务有多个可能路径，而且路径好坏可以被阶段性评估。相反，简单事实问答、格式转换、短分类这类任务没有明显搜索空间，启用 ToT 通常只是增加调用次数、延迟和 token 成本。

工程上可以把 ToT 看成 prompt-time / inference-time search scaffold。它可以由外部代码控制 BFS / DFS / beam-like search，也可以用比较轻的方式让模型一次列出多种方案并自评。但真正严肃的 ToT 不是“最后从多个答案里选一个”，而是每层都生成候选、评估、剪枝、继续搜索。这个边界很重要：只让模型输出三个答案然后挑一个，更像 self-consistency 或候选重排；ToT 的独特性在于树状展开和中途控制。

ToT 也帮助校准 [[Planning]] 的层次。它有 planning/search 的味道，但仍不是生产 [[Agent Workflow]]。Agent workflow 关心工具执行、外部 observation、状态持久化、权限、重试、checkpoint 和人类审批；ToT 关心的是一次问题求解中多条 reasoning path 的选择。两者可以组合，但不能画等号。

## 它解决什么问题

它解决的是“单条推理链走错方向后缺少纠偏”的问题。

最小差别可以这样记：

```text
CoT: Prompt -> one reasoning chain -> answer
Tree of Thoughts: Problem -> generate candidate thoughts -> evaluate -> select/prune/search -> answer
```

ToT 的收益来自两个动作：

- 横向展开：同一个中间状态下生成多个候选思路。
- 纵向控制：只把更有希望的候选继续展开，必要时回溯。

所以它适合复杂推理、搜索型 puzzle、创意方案探索、规划候选比较这类任务；不适合没有搜索空间、答案已知或评估信号很弱的任务。

## 它不是什么

Tree of Thoughts 不是 [[Zero-shot CoT]] 的同义词。CoT 通常是单链；ToT 是多分支搜索。

它也不是 [[ReAct]]。ReAct 的核心结构是 Thought -> Action -> Observation 的外部交互循环；ToT 可以不调用任何外部工具，只在 reasoning path 里搜索。

它更不是完整 [[Agent Workflow]]。ToT 没有天然的工具权限、状态机、checkpoint、trace、human gate 或失败恢复。把 ToT 包进 Agent runtime 可以产生强系统，但 ToT 本身只是推理时搜索框架。

Graph of Thoughts 也不是 ToT 的 alias。GoT 允许不同路径的中间结果合并、复用或形成图结构；ToT 的基本结构是树，不同分支通常彼此独立。GoT 是相邻升级方向，不在本卡 aliases 中。

## 最小例子

```text
任务：用 4 个数字得到 24。

CoT:
模型直接沿一条链尝试：
8 - 4 = 4, 7 - 4 = 3, 4 * 3 = 12 ... 走不通也可能继续硬编。

Tree of Thoughts:
第 1 层生成候选 thought：
A. 先尝试构造 6 * 4
B. 先尝试构造 12 * 2
C. 先尝试构造 8 * 3

评估候选：
B 分数高，继续展开；A / C 暂时剪枝或回溯。

下一层继续生成、评估、剪枝，直到找到可行表达式或搜索结束。
```

真实 ToT 实现通常会把“生成候选”“评估候选”“搜索控制”拆成多次模型调用或外部程序步骤。

## 常见误解 / 风险

- 误解：ToT 就是让模型多想几步。实际重点是多候选搜索，不是更长的一条链。
- 误解：ToT 永远比 CoT 好。实际它更贵；简单题和低风险任务通常不值得。
- 误解：ToT 是现代 reasoning model 自动内置的机制。更稳的说法是：现代模型可能吸收了多路径评估和反思的价值，但标准 ToT 是显式 inference-time framework。
- 误解：ToT 等于 Agent 规划能力。它只处理 reasoning path search，不负责真实工具执行和工作流治理。
- 风险：候选评估本身可能错。错误 evaluator 会保留坏路径、剪掉好路径，所以 ToT 仍需要任务设计、评估标准和预算控制。

## 边界细节

和附近概念的最小边界：

```text
Direct prompting: Prompt -> Answer
Zero-shot CoT: Prompt -> Reasoning steps -> Answer
Plan-and-Solve Prompting: Prompt -> Plan -> Solve -> Answer
Tree of Thoughts: State -> Candidate thoughts -> Evaluate -> Search/Backtrack -> Answer
ReAct: Thought -> Action -> Observation -> Thought -> ... -> Answer
Agent Workflow: Goal -> Plan/State -> Execute -> Evaluate/Replan -> Done
```

和 [[Plan-and-Solve Prompting]] 的区别：Plan-and-Solve 先生成计划再求解，仍主要是一条结构化路径；ToT 在每个中间状态可以保留多个候选路径，并用搜索策略选择下一步。

和 [[ReWOO]] 的区别：ReWOO 先规划 evidence slots，再调用工具填证据，最后合成答案；ToT 不要求 evidence slot 或外部工具，核心是搜索 reasoning path。

和 self-consistency 的区别：self-consistency 常见做法是采样多条完整推理链，最后投票或聚合答案；ToT 更强调中途评估、剪枝和回溯。

## 现代性状态

- 判定：foundation / transitional / current-practice
- 基础地基：ToT 稳定地揭示了一个重要思想：复杂问题不一定靠一条 reasoning trace 走到底，可以把中间推理状态变成可搜索对象。
- 历史过渡：经典 ToT 是 prompt / inference-time scaffold，适合理解从 CoT 到搜索式推理的演进。
- 当前工程吸收：现代系统会把 ToT 的价值转成候选方案生成、planner 自评、beam-like search、tool path search、test-time compute、eval-guided retry 或 tree search agent。
- 不应夸大：很多产品不会显式跑 ToT；reasoning tokens、hidden scratchpad 或 thinking mode 也不等于标准 ToT。

## 现代系统怎么吸收 Tree of Thoughts 的价值

现代系统通常不会在所有请求上启用完整 ToT，而是按任务风险和搜索空间选择性吸收：

- 对方案比较：先生成多个候选方案，再用 rubric 评分，保留最优或合并优点。
- 对复杂规划：让 planner 产生多个 plan draft，由 evaluator 检查约束、成本、风险和依赖。
- 对工具路径：在可能的 tool action 序列里搜索，而不是只让模型一步一步贪心选择。
- 对代码和数学：用测试、约束求解器、执行结果或 verifier 替代纯 LLM 自评，提高剪枝质量。
- 对预算治理：限制 branching factor、depth、评估轮次和停止条件，避免“想太多、做太少”。

小边界：ToT 的价值不是“展示更多思维链”，而是“在可评估的候选空间里做受控搜索”。如果没有可靠评估信号，树展开会很快变成昂贵的幻觉扩增。

## 证据锚点

- Source: [[Tree of Thoughts - Deliberate Problem Solving with Large Language Models]]
- Source: [[raw/repos/xiaolinnote/questions/005 ai agent 14. 如何赋予 LLM 规划能力？]]
- Source: [[raw/repos/agent_java_offer/questions/014 01_AI 01_Agent基础 在 Agent 的设计中，“规划能力”至重要。请谈谈目前有哪些主流方法可以赋予 LLM 规划能力？（例如 CoT, ToT, GoT等）]]
- Anchor: [[Tree of Thoughts - Deliberate Problem Solving with Large Language Models#需要我读的内容]]
- Anchor: [[raw/repos/xiaolinnote/questions/005 ai agent 14. 如何赋予 LLM 规划能力？#ToT：从「一条链」到「一棵树」，解决走错方向的问题]]
- Anchor: [[raw/repos/agent_java_offer/questions/014 01_AI 01_Agent基础 在 Agent 的设计中，“规划能力”至重要。请谈谈目前有哪些主流方法可以赋予 LLM 规划能力？（例如 CoT, ToT, GoT等）#题目正文]]
- Evidence type: paper source note + raw interview/tutorial source notes + engineering synthesis.
- Confidence: medium-high
- Boundary: 论文和教程证据支持 ToT 的多路径搜索、评估、回溯和成本权衡；现代系统是否真的运行 ToT 取决于任务、模型、预算、评估器和外部控制逻辑，不能从“模型有 reasoning tokens”直接推出。

## 复习触发

1. ToT 相比 Zero-shot CoT 多了哪两个控制动作？
2. 为什么 ToT 适合 Game of 24 / crossword 这类任务，却不适合“法国首都是什么”？
3. ToT、ReAct、Agent Workflow 分别在哪一层做控制？
4. GoT 为什么不是 ToT 的 alias？

## 相关链接

- [[Zero-shot CoT]]
- [[Few-shot CoT]]
- [[Self-Consistency]]
- [[Plan-and-Solve Prompting]]
- [[Reasoning Trace]]
- [[Planning]]
- [[ReAct]]
- [[ReWOO]]
- [[Agent Workflow]]
- [[Task Success Rate]]
