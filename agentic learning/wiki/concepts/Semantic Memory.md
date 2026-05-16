---
type: concept
topic:
  - memory
  - agent
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-16

up:
  - "[[Memory]]"

last_checked: 2026-05-07
freshness: watch
conflicts: []
source:
  - "[[LangGraph Memory 官方文档]]"
  - "[[Zep Memory 官方文档]]"
  - "[[Mem0 Memory 官方文档]]"
evidence:
  - "[[LangGraph Memory 官方文档#为什么收]]"
  - "[[Zep Memory 官方文档#为什么收]]"
  - "[[Mem0 Memory 官方文档#为什么收]]"
related:
  - "[[Memory]]"
  - "[[Long-term Memory]]"
  - "[[Episodic Memory]]"
  - "[[RAG]]"
---

# Semantic Memory

## 一句话

Semantic Memory 保存相对稳定的事实、偏好、概念和关系，让 Agent 在未来任务中复用“已知是什么”的知识。

## 概念详解

Semantic Memory 关注的是可跨场景复用的“事实性 / 概念性”信息：用户偏好、项目属性、术语定义、实体关系、长期约束。它回答“系统知道什么”，而不是“昨天发生了什么”。

在 Agent 系统里，semantic memory 常被写成 profile、facts、preferences、knowledge triples、文档片段或结构化字段。它可以存在数据库、向量库或 graph 中，但存储形式不是核心；核心是这类记忆在未来任务中应被当作相对稳定的背景知识使用。

和论文里的 non-parametric memory 相比，semantic memory 更强调内容角色：它可能来自对话、项目文档、用户确认或事件总结；一旦被写入，就会在未来影响回答方式或行动选择。因此它需要比普通检索文档更严格的来源、更新时间、适用范围和覆盖规则。

现代 memory service 往往会自动从 conversation 或 episode 中抽取 facts，但“自动抽取”并不等于“事实成立”。学习时要把三层分开：原始事件记录、从事件中提取的候选事实、被确认并可长期使用的 semantic memory。越接近长期使用，越需要用户可见、可编辑和可撤销。

Semantic Memory 需要来源和冲突边界。用户说过一次“我喜欢详细解释”不一定是永久偏好；项目事实也可能随时间改变。可靠的 semantic memory 应该能说明来源、更新时间、适用范围和覆盖关系。

在实践里，semantic memory 最容易和“总结”混淆。总结可以只是压缩文本；semantic memory 需要能被未来任务当作事实或偏好使用。因此写入前要问：这条内容是否跨任务有效？是否有主体和范围？是否需要过期？如果答案不清楚，它更适合先留在 episode 或待确认队列。
## 它解决什么问题

Agent 需要知道“用户是谁、项目是什么、术语如何定义、某个偏好是否长期成立”。这些不是一次任务里的临时步骤，而是可在多个任务中复用的知识。

如果没有 semantic memory，Agent 会反复询问已知偏好，或在同一项目里重复建立概念背景。

## 它不是什么

Semantic Memory 不是事件流水账。“昨天我打开网页失败三次”更像 [[Episodic Memory]]；“用户偏好中文解释，并希望先讲边界”更像 semantic memory。

它也不是任意文档知识库。外部资料可以通过 [[RAG]] 被检索，但只有经过选择、归属到用户 / 项目 / 概念并带来源边界的信息，才更像 Agent 的 semantic memory。

它也不是不可变真理。语义记忆会过期、冲突或被用户显式修改。

## 最小例子

在你的 vault 里：

- “[[Agent]] 是围绕目标行动的系统。”
- “用户对 Agent 和 Obsidian 从零开始。”
- “当前学习系统采用 raw/wiki/maps 三层。”

这些都适合成为 semantic memory，因为它们描述相对稳定的概念、用户背景或项目结构。

相对地，“今天第 3 次运行 audit script 失败”更像 episodic memory 或 task state，不应直接写成长期语义事实。

## 常见误解

- 稳定事实也会过期。
- 用户偏好可能依场景变化。
- 语义记忆需要冲突解决，例如“用户现在想要详细解释”可能覆盖旧偏好。
- 语义记忆的来源应该可追溯。

## 边界细节

Semantic Memory 的边界由“可复用事实”决定，而不是由“是否使用向量检索”决定。向量库里可以存 semantic memory，也可以存普通文档块；graph 里可以存项目实体关系，也可以存临时任务数据。

和 [[Episodic Memory]] 的边界：semantic memory 抽取稳定事实；episodic memory 保留发生过的事件和轨迹。一次失败经历可能先作为 episodic memory 保存，后来被总结成“某工具在这个网络环境下不稳定”的 semantic memory。

和 [[Long-term Memory]] 的边界：long-term memory 是跨会话能力总称；semantic memory 是其中保存事实 / 偏好 / 概念的一类。

## 现代性状态

Semantic Memory 是基础概念 + 当前工程实践。

- 基础地基：语义记忆作为“事实与概念知识”的分类很稳定。
- 当前工程实践：Agent memory 系统会把用户事实、偏好、profile、实体关系和项目知识显式保存，并在任务时检索使用。
- 前沿 / 易变：自动抽取事实、冲突合并、用户可编辑记忆面板、多应用共享 profile 等实现仍在变化，所以本卡标记为 `freshness: watch`。

## 现代系统怎么吸收 Semantic Memory 的价值

现代系统通常把 semantic memory 做成可编辑、可追溯的 facts/profile，而不是只靠模型从长聊天里猜。写入时要尽量区分“用户确认的事实”“模型推断的偏好”“项目文档里的定义”；检索时要考虑当前任务是否真的需要这条记忆。

这能减少重复沟通，同时避免把一次上下文里的偶然表达固化成长期规则。

## 证据锚点

- Evidence type: official docs note — [[LangGraph Memory 官方文档]]，支持 memory 类型 / store 的 framework 语境。
- Evidence type: official docs note — [[Zep Memory 官方文档]]，支持 memory service 中 facts / episodes 等语境。
- Evidence type: official docs note — [[Mem0 Memory 官方文档]]，支持 memory service 生态语境。
- Boundary: 当前卡片使用多个 memory 系统的共同抽象来解释 semantic memory；不声称它们对 semantic memory 的字段、算法或 API 定义完全一致。
- Engineering synthesis: “事实、偏好、概念和关系需要来源、更新时间、适用范围和覆盖关系”是记忆治理总结，需要具体实现验证。
- Confidence: medium。

## 复习触发

- Semantic Memory 和 Episodic Memory 怎样从同一次失败经历中分化出来？
- 为什么“存在向量库里”不等于“一定是 semantic memory”？
- 用户偏好发生冲突时，semantic memory 应该怎样保留来源和覆盖关系？

## 相关链接

- [[Long-term Memory]]
- [[Episodic Memory]]
- [[Memory]]
- [[Obsidian + LLM Wiki]]
