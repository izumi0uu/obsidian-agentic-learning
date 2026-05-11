---
type: concept
topic:
  - memory
  - agent
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-10
last_checked: 2026-05-10
freshness: watch
conflicts: []
source:
  - "[[LangGraph Memory 官方文档]]"
  - "[[Mem0 Memory 官方文档]]"
evidence:
  - "[[LangGraph Memory 官方文档#为什么收]]"
  - "[[Mem0 Memory 官方文档#为什么收]]"
related:
  - "[[Memory]]"
  - "[[Long-term Memory]]"
  - "[[Semantic Memory]]"
  - "[[Trace]]"
---

# Episodic Memory

## 一句话

Episodic Memory 保存过去发生过的事件、任务轨迹、操作结果和经验样例，让 Agent 能回看“当时发生了什么”。

## 概念详解

Episodic Memory 关注的是经历，而不是抽象事实。它记录某次任务的输入、步骤、工具调用、结果、失败原因、用户反馈或环境状态，回答“那一次发生了什么、我是怎么做的、结果怎样”。

在 Agent 系统里，episodic memory 可能来自 conversation history、trace、trajectory、tool call log、task run artifact 或专门 memory service 里的 episode。它比单纯聊天记录更有结构：好的 episode 会保留时间、任务目标、关键 action、observation、结果和后续启发。

它和 [[Semantic Memory]] 的关系很重要：episode 是原始经历或经历摘要；semantic memory 是从多个经历中抽取出的稳定事实或偏好。例如“第 3 次运行 audit 失败，因为缺少 Evidence type”是 episodic；多次之后总结出“概念卡证据锚点必须显式写 Evidence type / Boundary”才更像 semantic memory。

官方 memory 文档和社区实践常把 episode 用作长期记忆的一类输入，但不同系统对 episode 的存储粒度、检索方式和自动反思机制不同。本卡把它作为学习分类，不声称所有 memory 产品都使用同一字段或同一算法。

在学习库中，reviews 里的费曼回答也可能像 episode 一样暴露“我哪里没懂”，但它不是 raw evidence。若要把它转成长期记忆，应该先明确：这是一次学习过程记录、一次错误经验，还是已经被 source / 概念卡支持的稳定规则。这个边界能防止把临时理解误写成事实。
## 它解决什么问题

Agent 不只需要知道事实，还需要知道“之前发生了什么、当时做了什么、结果怎样”。这能帮助它复盘失败、复用成功路径、避免重复踩坑。

没有 episodic memory，系统可能只保留最终答案，却丢失为什么失败、哪些工具调用已经发生、用户当时如何纠正，以及下次应该避免什么。

## 它不是什么

Episodic Memory 不是稳定知识库。它更像“经历记录”；从经历中提炼出的长期规则，才可能进入 [[Semantic Memory]] 或 procedural memory。

它也不是完整 [[Trace]] 的同义词。Trace 更偏执行记录和可观测性；episodic memory 是把某些执行经历保存为未来可复用的记忆对象。一个 trace 可以生成 episode，但 trace 本身未必被长期记忆系统使用。

## 最小例子

一次论文处理失败的 episodic memory：

- 处理 `Attention Is All You Need.pdf`。
- `pdftotext` 能抽正文，但公式、表格和图结构损失严重。
- 下次需要同时保留 PDF、抽取 Markdown，并人工检查关键图表。

这条记忆保留的是一次事件。若未来多次 PDF 处理都出现同样问题，系统可以再通过 [[Memory Reflection]] 总结成更稳定的处理规则。

## 常见误解和风险

- 事件太多会淹没重要经验，检索时反而干扰当前任务。
- 单次失败不能直接变成长期规则。
- episode 可能包含隐私、密钥、客户信息或未授权工具结果。
- 过度依赖相似经历，会让 Agent 在新场景里套旧方案。

## 边界细节

和 [[Trace]] 的边界：trace 是可观测执行记录，常用于调试、评估和 replay；episodic memory 是被选择性保留下来、未来可能影响决策的经历。不是所有 trace 都应该进 memory。

和 [[Replay]] 的边界：replay 关注复现一次执行；episodic memory 关注从过去经历中取回有用上下文。episode 可以帮助 replay，但 replay 需要更完整的输入、环境和工具结果。

和 [[Semantic Memory]] 的边界：semantic memory 抽取稳定事实；episodic memory 保留事件脉络。学习时可以问：这条信息是在说“发生过什么”，还是在说“长期上通常是什么”？

## 现代性状态

Episodic Memory 是基础概念 + 当前工程实践，具体实现带 `watch`。

- 基础地基：用事件经历辅助未来判断是稳定学习思想。
- 当前工程实践：Agent memory 系统、trace 平台和任务日志都可能把历史 trajectory 转成可检索 episode。
- 前沿 / 易变：自动 episode 抽取、压缩、隐私过滤、和 semantic memory 的合并策略仍在快速变化。

## 现代系统怎么吸收 Episodic Memory 的价值

现代系统通常不会把完整历史无差别塞回上下文，而是把关键 episode 做摘要、索引和权限过滤。检索时只取与当前任务相似或有明确启发的片段，并标注它来自过去经历而不是稳定事实。

这样做能让 Agent 从过去任务中学习，同时保留“这只是一次经历”的证据边界。

## 证据锚点

- Evidence type: official docs note — [[LangGraph Memory 官方文档]]，支持 memory / store / thread 等 framework 语境。
- Evidence type: official docs note — [[Mem0 Memory 官方文档]]，支持 memory service 语境中从历史交互提取可用记忆的方向。
- Boundary: 当前卡把 episodic memory 作为 memory 类型学习分类；具体 episode 字段、抽取算法和检索策略需回到具体产品文档确认。
- Engineering synthesis: “trace 可生成 episode，但 trace 不等于 episode”是观测层与记忆层的边界总结。
- Confidence: medium。

## 复习触发

- 如何判断一条信息是 episodic memory 还是 semantic memory？
- 为什么不是所有 trace 都应该进入长期记忆？
- 单次失败经历要变成长期规则，中间还需要什么确认步骤？

## 相关链接

- [[Long-term Memory]]
- [[Semantic Memory]]
- [[Trace]]
- [[Replay]]
