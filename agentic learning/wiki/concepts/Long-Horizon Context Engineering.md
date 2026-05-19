---
type: concept
topic:
  - agent
  - context
  - memory
  - workflow
status: seed
created: 2026-05-18
updated: 2026-05-18
last_checked: 2026-05-18
freshness: watch
aliases:
  - long-horizon context engineering
  - long context engineering for agents
  - 长时程任务上下文工程
  - 面向长时程任务的上下文工程
  - 长程上下文工程
  - 压缩整合
  - Compaction
  - Structured note-taking
  - 结构化笔记
  - Sub-agent architectures
  - 子代理架构
source:
  - "[[Context Engineering]]"
  - "[[LLM 上下文限制与突破条件]]"
  - "[[Agent State]]"
  - "[[Memory]]"
  - "[[Multi-agent Orchestration]]"
  - "[[LangChain DeepAgents]]"
  - "[[DeerFlow]]"
  - "[[526 05_项目表达 01_AI应用平台 Sub-agent 的收益到底是什么，除了“并行”还有什么？]]"
evidence:
  - "[[Context Engineering#概念详解]]"
  - "[[LLM 上下文限制与突破条件#限制分层]]"
  - "[[Agent State#现代系统怎么吸收 Agent State 的价值 / 局限]]"
  - "[[Memory#现代系统怎么吸收 Memory 的价值]]"
  - "[[Multi-agent Orchestration#概念详解]]"
  - "[[LangChain DeepAgents#概念详解]]"
  - "[[DeerFlow#概念详解]]"
  - "[[526 05_项目表达 01_AI应用平台 Sub-agent 的收益到底是什么，除了“并行”还有什么？#题目正文]]"
related:
  - "[[Context Engineering]]"
  - "[[Context Window]]"
  - "[[Context Rot]]"
  - "[[Agent State]]"
  - "[[Memory]]"
  - "[[Context Projection]]"
  - "[[Long-term Memory]]"
  - "[[Multi-agent Orchestration]]"
  - "[[Agent Harness]]"
  - "[[Trace]]"
  - "[[Evaluation]]"
relations:
  - type: specializes
    target: "[[Context Engineering]]"
    note: "把上下文选择、压缩、外部化和隔离用于超出单窗口的长任务。"
  - type: uses
    target: "[[Agent State]]"
    note: "当前 run 的阶段、待办、错误和下一步依据需要结构化保存。"
  - type: uses
    target: "[[Memory]]"
    note: "结构化笔记是跨上下文窗口持久化关键事实的一种 memory 形态。"
---

# Long-Horizon Context Engineering

## 一句话

Long-Horizon Context Engineering 是面向长时程 Agent 任务的上下文治理方法：当任务跨越数十到数百轮行动、超出单次 [[Context Window]] 时，用压缩整合、结构化笔记和子代理隔离来维持目标、状态、证据和决策的一致性。

## 概念详解

长时程任务的问题不只是“上下文窗口放不下”。大型代码库迁移、跨数小时研究、复杂调试、长期仿真或多阶段数据分析都会产生大量工具输出、搜索结果、临时假设、失败尝试和中间产物。即使模型支持更大的窗口，直接把所有历史塞回去也会带来上下文污染、[[Context Rot|相关性退化]]、成本上升和错误信息长期滞留。[[LLM 上下文限制与突破条件]] 已经把容量限制、有效使用限制和治理限制拆开；本卡进一步聚焦长任务里的运行策略。

它通常由三类方法组成。第一是 **Compaction / 压缩整合**：当上下文接近上限时，把深历史压缩成高保真摘要，并用摘要重启新的上下文窗口。好的 compaction 不只是“总结聊天”，而是保留架构性决策、未解决缺陷、关键约束、已尝试方案、当前计划和最近高相关工件，丢弃重复工具输出、日志噪声和过时草稿。调参时优先保证召回，避免丢掉关键事实；再逐步提高精确度，清理冗余内容。一个轻触式做法是优先压缩深历史中的工具调用和结果，而不是压缩最近正在操作的文件或证据。

第二是 **Structured note-taking / 结构化笔记**。它把长任务的关键事实写到上下文窗口之外，例如 `NOTES.md`、TODO 列表、阶段性结论、依赖关系、阻塞项、决策日志、实验计数或外部 memory store。它和 [[Agent State]]、[[Memory]] 相邻：state 保存当前 run 的阶段和下一步依据；memory / notes 保存未来阶段仍要取回的事实。结构化笔记的价值是用很小的上下文开销维持持久状态，让 Agent 经历多次 compaction 或上下文重置后仍能知道“已完成什么、还差什么、哪些结论不能推翻”。

第三是 **Sub-agent architectures / 子代理架构**。主代理保留高层目标、计划和综合责任，把搜索、阅读、验证、实现或审查分派给专长子代理。每个子代理在干净的 scoped context 中深入探索，调用工具并保留自己的搜索噪声，最后只把凝练摘要、证据和风险回传给主代理。这个模式的收益不是只有并行，还包括关注点分离、上下文隔离、专业化工具/提示词/权限和局部失败隔离。[[LangChain DeepAgents]] 和 [[DeerFlow]] 这类 harness source note 都体现了长任务 Agent 需要 filesystem、subagents、memory、context compression 和 sandbox/workspace 这组结构。

证据边界：这张卡主要是工程综合卡。三件套来自用户提供的知识点，并由本 vault 里已有 [[Context Engineering]]、[[Agent State]]、[[Memory]]、[[Multi-agent Orchestration]]、[[LangChain DeepAgents]]、[[DeerFlow]] 的概念边界支撑。它不是某一篇论文的正式 taxonomy；具体 compaction 触发阈值、摘要格式和子代理 token 预算属于实现参数。

## 它解决什么问题

它解决的是长任务中的“连贯性和聚焦”问题：Agent 需要跨很多轮行动记住目标、约束、已知事实、未解决问题和当前阶段，但又不能把全部历史原样塞回模型。

没有这层工程，长任务常见失败包括：重复搜索同一问题、忘记已经做过的实现决定、把旧错误日志当成当前事实、被大量工具输出淹没、越到后期越偏离目标，或主上下文被子任务细节污染。

## 它不是什么

Long-Horizon Context Engineering 不是单纯扩大 [[Context Window]]。大窗口只是容量改善，不会自动选择信息、清理噪声、标注来源或隔离子任务。

它也不是完整 [[Memory]] 系统。结构化笔记是它使用的一种外部状态/记忆手段，但长时程上下文工程还包括 compaction、[[Context Projection|context projection]]、子代理隔离和汇总策略。

它也不是“多 Agent 越多越好”。子代理架构只在任务能清晰切分、主代理能综合验证、子代理输出能被压缩成证据时才有价值。

## 最小例子

一个代码库迁移任务：

```text
1. 主代理维护 migration plan、风险列表和验收标准。
2. 每 20-30 次工具调用后做 compaction，保留架构决策、已改文件、失败测试和下一步。
3. 运行中持续更新 NOTES.md：
   - 已迁移模块
   - 未解决兼容问题
   - 关键 API 差异
   - 必跑测试
4. 对数据库层、API 层、测试层分别派 sub-agent 调查。
5. 子代理只回传 1000-2000 tokens 的结论、证据路径和风险。
6. 主代理汇总后继续执行，并把新事实写回 state / notes。
```

这里的关键是：长历史被压缩，长期事实被外部化，搜索噪声被隔离，主代理只承担综合和决策。

## 常见误解 / 风险

- 误解：摘要越短越好。过度压缩会丢掉关键约束、失败原因和未完成事项；长任务中通常先保召回，再调精确。
- 误解：结构化笔记就是把聊天记录存文件。真正有用的是 TODO、决策、阻塞项、依赖、证据路径和当前状态，而不是完整流水账。
- 误解：子代理只为并行。它更重要的收益是干净上下文、权限隔离、专业化和局部失败隔离。
- 风险：compaction 把猜测写成事实，后续窗口会继承错误。
- 风险：notes 没有更新规则，旧状态和新状态冲突。
- 风险：子代理输出只给结论不给证据，主代理无法验证。

## 边界细节

三类方法的取舍可以这样判断：

| 方法 | 适合场景 | 核心收益 | 主要风险 |
|---|---|---|---|
| Compaction | 需要长对话连续性、但历史开始挤占窗口 | 上下文接力，保留关键历史 | 摘要遗漏或把错误固化 |
| Structured note-taking | 有里程碑、阶段性成果、待办和依赖关系 | 外部化持久状态，低上下文成本 | 笔记过期、无来源、无更新规则 |
| Sub-agent architectures | 复杂研究、分析、代码调查，可并行探索 | 上下文隔离、专业化、局部失败隔离 | 汇总失真、任务重叠、验证不足 |

和 [[Agent State]] 的边界：state 更偏当前 run 的控制事实；结构化笔记更偏可被未来阶段取回的工作记忆。两者常常互相同步，但不应混成一坨自然语言历史。

和 [[Trace]] 的边界：trace 是发生过什么的完整记录；compaction / notes 是给后续决策使用的投影。trace 可以很长，投影必须短而有用。

和 [[Multi-agent Orchestration]] 的边界：子代理架构是多 Agent 编排的一种上下文管理用途。可靠性仍取决于 ownership、通信协议、证据格式、集成权威和最终验证。

## 现代性状态

- 判定：current-practice / frontier-adjacent。
- 稳定部分：长任务 Agent 需要压缩历史、外部化状态、隔离子任务和保留可验证证据。
- 易变部分：具体 compaction 触发阈值、摘要 schema、memory tool、sub-agent API、上下文预算和 harness 默认行为会快速变化。
- 复查点：当主流 Agent harness 对 compaction、memory、filesystem、subagents 或 [[Context Projection|context projection]] 给出稳定 API 时，更新本卡实现边界。

## 现代系统怎么吸收 Long-Horizon Context Engineering 的价值 / 局限

现代 Agent harness 通常把这些方法拆到 runtime 里：checkpoint / state 保存当前阶段，filesystem 或 memory store 保存结构化笔记，compaction 管理上下文接力，subagents 用 scoped context 做局部探索，trace 记录完整过程，evaluation / human review 判断最终结果。

局限是它们都不是正确性保证。Compaction 需要检查召回，notes 需要来源和更新规则，sub-agent 汇总需要证据和主代理验证。长任务可靠性来自上下文工程、状态设计、工具权限、trace、评测和人工验收的组合。

## 证据锚点

- Concept anchors: [[Context Engineering#概念详解]], [[LLM 上下文限制与突破条件#限制分层]], [[Agent State#现代系统怎么吸收 Agent State 的价值 / 局限]], [[Memory#现代系统怎么吸收 Memory 的价值]], [[Multi-agent Orchestration#概念详解]]。
- Harness examples: [[LangChain DeepAgents#概念详解]], [[DeerFlow#概念详解]]。
- Raw interview anchor: [[526 05_项目表达 01_AI应用平台 Sub-agent 的收益到底是什么，除了“并行”还有什么？#题目正文]]。
- Evidence type: user-provided knowledge point + concept-card synthesis + harness source-note synthesis + engineering inference.
- Confidence: medium.
- Boundary: 三件套是本卡采用的工程框架，不声称为通用学术标准；具体参数需要按项目和 harness 实现验证。

## 复习触发

1. 为什么长上下文窗口不能自动解决长时程任务？
2. Compaction、structured note-taking、sub-agent architectures 分别解决什么问题？
3. 什么时候应该优先保留召回而不是追求极短摘要？
4. 子代理除了并行，还有哪些上下文工程收益？

## 相关链接

- [[Context Engineering]]
- [[Context Window]]
- [[Context Rot]]
- [[Agent State]]
- [[Memory]]
- [[Context Projection]]
- [[Long-term Memory]]
- [[Multi-agent Orchestration]]
- [[Agent Harness]]
- [[Trace]]
- [[Evaluation]]
