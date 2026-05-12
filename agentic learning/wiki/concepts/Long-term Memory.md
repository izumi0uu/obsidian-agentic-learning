---
type: concept
topic:
  - memory
  - agent
  - frontier
status: growing
created: 2026-05-06
updated: 2026-05-12
last_checked: 2026-05-07
freshness: watch
conflicts: []
source:
  - "[[LangGraph Memory 官方文档]]"
  - "[[Letta Memory 官方文档]]"
  - "[[Zep Memory 官方文档]]"
  - "[[Mem0 Memory 官方文档]]"
  - "[[Reflexion - Language Agents with Verbal Reinforcement Learning]]"
evidence:
  - "[[LangGraph Memory 官方文档#为什么收]]"
  - "[[Letta Memory 官方文档#为什么收]]"
  - "[[Zep Memory 官方文档#为什么收]]"
  - "[[Mem0 Memory 官方文档#为什么收]]"
  - "[[Reflexion - Language Agents with Verbal Reinforcement Learning#必读块 2：Abstract / episodic memory buffer]]"
related:
  - "[[Memory]]"
  - "[[Semantic Memory]]"
  - "[[Episodic Memory]]"
  - "[[Memory Reflection]]"
  - "[[Reflexion]]"
  - "[[RAG]]"
---

# Long-term Memory

## 一句话

Long-term Memory 是 Agent 跨会话保存、检索、更新并治理信息的能力，让未来任务能复用过去确认过的偏好、事实、经验和项目状态。

## 概念详解

长期记忆的关键不是“保存聊天历史”，而是把未来仍有价值的信息变成可检索、可解释、可更新的外部状态。它通常需要写入策略、存储结构、检索策略、冲突解决、过期删除、权限控制和来源记录。

在 Agent runtime 中，long-term memory 通常位于模型上下文之外。模型在当前回合只能看到被检索出来的一小部分记忆；真正的记忆库可能在数据库、向量库、文档 store、graph 或专门的 memory service 中。runtime 决定什么时候写、写什么、下次怎样取回，以及取回后怎样注入 agent state。

官方 memory 文档常会强调 thread/user scope、store、facts、episodes、memory block 或自动抽取。它们共同说明长期记忆正在从“聊天记录很长”转向“有治理的外部状态”。但不同系统对自动写入、用户确认、隐私删除和冲突合并的做法差异很大，所以本卡只把它们综合成学习边界，不把某一家产品的 API 当成通用定义。

长期记忆和 [[Semantic Memory]]、[[Episodic Memory]] 是上下位关系：长期记忆是跨会话能力，semantic / episodic 描述长期记忆中不同内容类型。它也和 [[Durable Execution]] 相邻：durable execution 保证当前流程能恢复，long-term memory 保证跨流程信息能复用。

长期记忆还需要区分“保存”和“使用”。系统可以保存很多候选信息，但每次任务只应检索和注入少量相关内容；否则旧偏好、过期项目事实或相似但不适用的 episode 会污染当前推理。好的 long-term memory 因此同时是存储问题、检索问题和治理问题。
## 它解决什么问题

没有长期记忆，Agent 每次对话都像第一次见你。它无法稳定记住用户偏好、项目状态、历史决策、失败经验或长期目标。

长期记忆让 Agent 能把重要信息写入外部存储，在未来任务中检索并使用。它尤其适合长期学习助手、个人助理、项目代理和需要跨多次任务积累上下文的系统。

## 它不是什么

长期记忆不是上下文窗口。上下文窗口是本次调用可见输入；长期记忆是跨会话的外部状态。

它也不只是聊天记录归档。真正有用的长期记忆要解决写入、检索、更新、冲突、过期、删除、权限和来源问题。

它也不等于 [[RAG]]。RAG 常用于检索外部知识资料；长期记忆还包括用户偏好、项目状态和过去交互经验。

## 最小例子

你多次强调：“学习 Agent 时先讲边界，再讲实现。”

Agent 把这条偏好写入用户记忆。之后你问 [[MCP]]，它会先说明 MCP 不是 Agent 框架，再讲工具连接协议。

如果未来你说“这周先用极简回答”，系统应该能更新或临时覆盖旧偏好，而不是永远机械套用旧记忆。

## 常见误解

- 记住越多不一定越好，旧信息会污染新任务。
- 错误记忆比没记忆更危险。
- 用户记忆、项目记忆、任务记忆需要分开。
- 记忆必须能被删除、审计和解释来源。
- [[Reflexion]] 里的 Experience 不会自动变成长期记忆；它先是下一轮 Actor 可读的任务经验，只有通过筛选和治理后才适合跨会话保存。

## 边界细节

长期记忆至少有三个边界：时间边界、权限边界、证据边界。时间边界决定信息什么时候过期；权限边界决定谁能看见或使用；证据边界决定这条记忆从哪里来、是否被用户确认。

和 [[Durable Execution]] 的边界：durable execution 让当前流程可恢复；long-term memory 让跨流程信息可复用。一个 agent 可以在没有长期记忆的情况下恢复同一任务，也可以在没有 durable workflow 的情况下记住用户偏好。

和 [[Semantic Memory]] / [[Episodic Memory]] 的边界：长期记忆是能力层，semantic / episodic 是内容分类。

从 [[Reflexion]] 的 Experience 写入长期记忆，需要额外门槛：经验要可靠、可验证、可泛化，不包含敏感泄露，不会把一次性失败、临时工具参数或当前 repo 状态污染到未来任务。局部经验更适合留在当前 context、trace、episode 或短期任务记忆里；稳定偏好、反复出现的失败模式、用户确认过的规则，才更适合进入长期记忆。

## 现代性状态

Long-term Memory 是当前工程实践 + 前沿 / 易变实现层。

- 基础地基：长期保存和复用信息是稳定需求。
- 当前工程实践：Agent framework 和 memory service 会提供 store、thread/user scope、retrieval、profile、facts、episodes 等机制。
- 前沿 / 易变：自动记忆写入、隐私控制、冲突解决、遗忘机制和多应用共享记忆仍在快速演进，所以本卡标记为 `freshness: watch`。

## 现代系统怎么吸收 Long-term Memory 的价值

现代系统倾向于把长期记忆做成显式 store，而不是让模型在隐式聊天历史里“感觉自己记得”。写入通常由工具、规则或用户确认触发；检索由当前任务和用户 scope 限制；使用时要把记忆来源和置信度带回上下文。

这样做能让长期记忆被审计、删除、迁移和评估，也能避免“模型把一次偶然偏好当成永久事实”。

## 证据锚点

- Evidence type: official docs note — [[LangGraph Memory 官方文档]]，支持 framework memory / store / thread 语境。
- Evidence type: official docs note — [[Letta Memory 官方文档]]，支持专门 memory agent / memory block 语境。
- Evidence type: official docs note — [[Zep Memory 官方文档]]，支持会话记忆和记忆服务语境。
- Evidence type: official docs note — [[Mem0 Memory 官方文档]]，支持 memory service 生态语境。
- Evidence type: paper source — [[Reflexion - Language Agents with Verbal Reinforcement Learning]]，支持 Experience / episodic memory buffer 的任务反思语境。
- Boundary: 当前卡片综合多个 memory 系统的共同问题，不声称它们采用同一存储模型、同一 API 或同一隐私策略。
- Engineering synthesis: “写入、检索、更新、冲突、过期、删除、权限和来源”是长期记忆治理框架，需要回到具体产品文档核对实现。
- Engineering synthesis: Experience 写入长期记忆的筛选门槛来自 memory governance 边界综合；Reflexion 论文支持 experience 机制，但不等于自动长期记忆治理。
- Confidence: medium。

## 复习触发

- 为什么长期记忆不是聊天记录归档？
- Long-term Memory 和 Durable Execution 的边界是什么？
- 一条用户偏好进入长期记忆前，应该检查哪些来源和权限问题？
- Reflexion 里的 Experience 什么时候只留在当前任务里，什么时候才适合写入长期记忆？

## 相关链接

- [[Memory]]
- [[Semantic Memory]]
- [[Episodic Memory]]
- [[Memory Reflection]]
- [[RAG]]
