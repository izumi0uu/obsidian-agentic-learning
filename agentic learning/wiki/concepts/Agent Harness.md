---
type: concept
topic:
  - agent
  - frontier
  - evaluation
status: seed
created: 2026-05-05
updated: 2026-05-28
last_checked: 2026-05-28
freshness: watch
conflicts: []
source:
  - "[[前沿主源清单]]"
  - "[[SWE-bench]]"
  - "[[LangSmith Evaluation and Observability]]"
  - "[[Claude Code Hooks 文档]]"
  - "[[Oh My Codex Repo]]"
  - "[[Pi Agent Harness Repo]]"
  - "[[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]]"
  - "[[Anthropic Managed Agents 文档]]"
evidence:
  - "[[前沿主源清单#代码 Agent]]"
  - "[[SWE-bench#为什么收]]"
  - "[[LangSmith Evaluation and Observability#为什么收]]"
  - "[[Claude Code Hooks 文档#关键事实]]"
  - "[[Oh My Codex Repo#本地 hook / 可观测性补充]]"
  - "[[Pi Agent Harness Repo#关键事实]]"
  - "[[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry#需要我读的内容]]"
  - "[[Anthropic Managed Agents 文档#关键事实]]"
related:
  - "[[Agent]]"
  - "[[Evaluation]]"
  - "[[Agent Loop]]"
  - "[[Agent State]]"
  - "[[Agent Workflow]]"
  - "[[Agent Lifecycle Hook]]"
  - "[[Patch Validation]]"
  - "[[Repo Context]]"
  - "[[Eval Harness]]"
  - "[[Tool Registry]]"
  - "[[Tool Poisoning]]"
  - "[[Agent Skills]]"
  - "[[Managed Agent Harness]]"
  - "[[Agent Harness 缓存分层与命中率]]"
---

# Agent Harness

## 一句话

Agent Harness 是包住模型、工具、状态、权限、运行环境、trace 和评测逻辑的执行外壳。

## 概念详解

Agent Harness 可以理解为“让 Agent 真的跑起来并留下证据的壳”。如果 [[Agent]] 是围绕目标做决策和行动的系统，那么 harness 负责把这个系统放进可控环境：准备输入、装配上下文、暴露工具、执行工具、隔离文件系统或网络、保存状态、记录 trace、处理失败、运行评测、决定是否停止。它不是智能来源，而是智能被使用时的边界和证据层。

这个概念在代码 Agent 场景里特别清楚。[[SWE-bench]] 不只是一个分数榜，它还提供 repo snapshot、issue、patch 应用和测试运行这类评测壳；没有这些，模型说“我修好了”无法被复现。[[LangSmith Evaluation and Observability]] 说明 trace、dataset、evaluation 对 agent 行为复盘很关键；[[Claude Code Hooks 文档]]、[[Oh My Codex Repo]] 和 [[Pi Agent Harness Repo]] 这类来源展示了 hook / lifecycle / tool boundary 如何把一次模型动作变成可记录、可阻断、可恢复的运行事件。

[[Pi Agent Harness Repo]] 还补了一个很有价值的边界：harness 不一定默认就是“厚重编排平台”。Pi 把自己定义为 minimal terminal coding harness，只给模型最核心的 `read` / `write` / `edit` / `bash` 工具、sessions 和扩展点，再把 sub-agents、plan mode、第三方 workflow 交给用户或扩展生态。这说明 harness 的本质是执行外壳和控制边界，不是必须内建所有高阶工作流能力。

因此 harness 的核心价值不是让模型更聪明，而是降低“聪明但不可控”的风险。它把自然语言目标翻译成有权限、有工作区、有日志、有测试、有回滚或人工接管的工程过程。现代 Agent 的很多可靠性问题——权限越界、工具失败、循环不止、上下文丢失、评估不可复现——都不是 prompt 单独能解决的，而是 harness 的责任边界。

可以把 harness 看成三条线的交叉：执行线负责把模型意图变成真实 action，安全线负责决定 action 是否允许、是否需要人类确认，证据线负责保存每一步为什么发生以及结果是什么。缺执行线，Agent 只能说不能做；缺安全线，Agent 可能把错误计划变成真实副作用；缺证据线，失败无法复盘，成功也无法作为可复用经验。这个三线结构解释了为什么 harness 常和 sandbox、tool permissioning、trace、eval harness、patch validation 同时出现。

当 Agent 支持按需加载 [[Agent Skills]] 时，harness 还要管住“选择了什么做事方法”。`SKILL.md`、skill 描述和完成定义会影响模型选择能力包，但这些文本不应自动变成可信规则。harness 至少要检查：这个 skill 是否适用于当前任务，是否要求越权工具，是否扩大写入范围，是否和上级规则冲突，执行结果是否有外部证据。模型的 reflection 可以提出怀疑，但真正的 stop / replan / reject 应由 harness、registry、policy、trace 和 evaluation 共同承载。

[[Managed Agent Harness]] 是这个概念的产品化/托管形态：平台替开发者托管 agent loop、session、工具执行、环境和事件流。它减少自建 harness 成本，但不取消业务侧的权限、验收、审计和成本控制责任。
## 它解决什么问题

单个 Agent 定义通常只描述“谁在决策”。但真实系统还需要回答：在哪里运行、能调用哪些工具、如何保存状态、如何复现失败、如何评分、如何限制权限。

Harness 负责把这些东西组织成一个可运行、可调试、可评估的系统。

## 它不是什么

Agent Harness 不是模型。

Agent Harness 也不是 Agent 本身。它更像 Agent 的实验台或运行壳。

## 最小例子

代码 Agent 的 harness 可能包括：

- checkout 一个 GitHub repo。
- 给 Agent issue 描述。
- 允许它读写文件和运行测试。
- 收集 patch、日志和测试结果。
- 判断任务是否完成。

[[SWE-bench]] 是一个很好的例子：它提供 issue、repo snapshot、patch 应用和测试运行机制，因此不只是 benchmark，也是代码 Agent 评测 harness 的典型形态。

## 常见误解 / 风险

- 误解：Harness 越厚，Agent 就越聪明。实际上 harness 提供控制和证据，不直接提供推理能力。
- 误解：有一个测试集就等于有 harness。测试集只是数据；harness 还要定义环境准备、执行协议、日志、失败处理和评分方式。
- 风险：如果 harness 只记录最终答案，不记录工具调用、输入、输出和权限判断，就很难复现失败。
- 风险：如果 harness 没有 sandbox / approval gate，高能力 Agent 会把错误计划快速变成真实副作用。
- 风险：如果 harness 不检测重复 action，同一个工具、同一组参数和相似 observation 可能让 ReAct-style loop 原地打转，消耗预算但不产生新信息。
- 风险：如果 harness 把 skill 文档当成绝对可信流程，错误或恶意 skill 会把错误完成定义、越权步骤或供应链诱导带进执行循环。

## 边界细节

Agent Harness 偏运行系统；Eval Harness 偏评测系统。两者经常重叠。

更细一点：如果它回答“Agent 怎么跑起来”，偏 [[Agent Harness]]；如果它回答“怎么重复测试并判断好坏”，偏 [[Eval Harness]]。

和缓存命中率的边界见 [[Agent Harness 缓存分层与命中率]]：harness 负责应用层的 tool result、retrieval、embedding、summary / context cache 的 key、TTL、权限 scope、版本和观测；模型内部 [[KV Cache]] 和 provider 端 Prompt Caching 的真正命中发生在 serving 层，harness 只能通过稳定前缀、上下文顺序和指标采集间接影响。

在 [[ReAct]] 或类似 action-observation loop 中，harness 还要判断 observation 是否真的改变了下一步决策。若连续出现 `同一 action + 同一参数 + 相似 observation`，这不应只被看成“模型又想了一轮”，而应被视为可能无新信息的重复路径。常见处理链路是：

- 停止：最大步数、预算、超时、重复 action 检测。
- 纠错：参数修正、换工具、query rewrite、replan，或让模型显式说明上一轮 observation 为什么不足。
- 升级：evaluator 检查、ask user、human approval、handoff。

边界：多加工具不是止损机制。止损的核心是判断这一步有没有带来新信息；没有新信息时，harness 要停、改路或升级。

对错误 skill 的处理也遵守同一条边界：多让模型反思一轮不是止损机制。harness 要把 skill 当成可验证假设，小步执行、记录 trace、检查产物和权限；一旦发现任务不匹配、证据不足、工具越权或验证失败，就应降级、换 skill、停下或升级给人类。

## 生命周期 hook 如何增强 Harness

[[Agent Lifecycle Hook]] 是 harness 的一个典型控制点。它把“模型想调用工具”和“工具真的执行”之间插入可观察、可阻断、可记录的边界：

- 工具执行前：做权限判断、参数校验、预算检查、人工确认或拒绝。
- 工具执行后：记录结果、补充上下文、触发 trace/span、更新状态或进入恢复流程。
- 会话边界：在 session start、user prompt submit、compact、stop 时保存状态、计划和日志。

这就是为什么 `PreToolUse` / `PostToolUse` 更应该理解为产品/runtime/harness 能力，而不是 LLM 自身能力。

## 现代性状态

- 基础地基：harness 来自软件工程里的运行壳、测试壳和评测壳思想。
- 当前工程实践：Agent 产品和框架普遍需要 harness 管住 tools、state、permissions、trace、retry、approval 和 evaluation。
- 稳定控制点：重复 action 检测、预算/超时、工具参数校验、replan 和升级路径属于 harness 的可靠性职责，不应只靠 prompt 自律。
- 前沿 / 易变：Codex、Claude Code、OpenAI Agents SDK、LangGraph 等具体 hook、trace、session API 会快速变化，应该靠 source note 的 `freshness: watch/volatile` 跟踪。

## 证据锚点

- Source: [[前沿主源清单]]
- Source: [[SWE-bench]]
- Source: [[LangSmith Evaluation and Observability]]
- Source: [[Claude Code Hooks 文档]]
- Source: [[Oh My Codex Repo]]
- Source: [[Pi Agent Harness Repo]]
- Source: [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]]
- Source: [[Anthropic Managed Agents 文档]]
- Anchor: [[SWE-bench#为什么收]], [[LangSmith Evaluation and Observability#为什么收]], [[Claude Code Hooks 文档#关键事实]], [[Oh My Codex Repo#本地 hook / 可观测性补充]], [[Pi Agent Harness Repo#关键事实]]
- Evidence type: benchmark/source notes + observability docs + hook/runtime repo evidence + engineering synthesis.
- Confidence: medium
- Boundary: “harness 负责状态、权限、trace、sandbox、评测、重复 action 止损”的拆分是工程综合理解；具体 hook 名称、API 和产品能力会随平台变化。

## 复习触发

- 如果一个模型能改代码但不能运行测试、记录 patch 或隔离工作区，它缺的是 Agent 还是 Harness？
- 为什么 [[SWE-bench]] 既是 benchmark，也能帮助理解 coding agent harness？
- 试着把一次工具调用拆成：模型决策、harness 执行、observation 回填、trace 记录、evaluation 判断。
- 一个 ReAct Agent 连续两次调用同一个工具和参数，得到相似 observation，harness 应该怎么停、改路或升级？
- 如果 Agent 选中了一个看似匹配但实际错误的 skill，harness 应该用哪些证据判断继续、换路或停止？

## 相关链接

- [[Agent]]
- [[Evaluation]]
- [[Agent Loop]]
- [[Agent Lifecycle Hook]]
- [[SWE-bench]]
- [[Patch Validation]]
- [[Repo Context]]
- [[Eval Harness]]
- [[Agent Skills]]
- [[Managed Agent Harness]]
- [[Agent Harness 缓存分层与命中率]]
