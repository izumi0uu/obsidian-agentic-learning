---
type: concept
topic:
  - agent
status: seed
created: 2026-05-05
updated: 2026-05-16
last_checked: 2026-05-10
freshness: stable
aliases:
  - AI Agent
  - 智能体
conflicts:
  - OpenAI、Anthropic、LangGraph 对 Agent/workflow 边界表述不同：OpenAI 更偏实践构建，Anthropic 强调 workflow vs agent 取舍，LangGraph 强调有状态图执行。
source:
  - "[[OpenAI - A Practical Guide to Building Agents]]"
  - "[[Anthropic - Building Effective Agents]]"
  - "[[LangGraph 官方文档]]"
  - "[[OpenAI Agents SDK 文档]]"
evidence:
  - "[[OpenAI - A Practical Guide to Building Agents#为什么收]]"
  - "[[OpenAI - A Practical Guide to Building Agents#一句话]]"
  - "[[Anthropic - Building Effective Agents#一句话]]"
  - "[[Anthropic - Building Effective Agents#边界提醒]]"
  - "[[LangGraph 官方文档#一句话]]"
  - "[[OpenAI Agents SDK 文档#一句话]]"
related:
  - "[[LLM]]"
  - "[[Agent Loop]]"
  - "[[Agent Workflow]]"
  - "[[Agent Harness]]"
  - "[[Tool Calling]]"
  - "[[Memory]]"
  - "[[Planning]]"
  - "[[Evaluation]]"
  - "[[Human-in-the-loop]]"
---

# Agent

## 一句话

Agent 是围绕目标连续行动的系统：它用模型做判断，但还需要状态、工具、反馈、边界和评估来推进任务。

## 概念详解

Agent 这个概念最容易被说空，因为它同时包含模型能力和工程外壳。更稳的理解是：Agent 不是“更会聊天的 LLM”，而是一个围绕目标运行的行动系统。模型负责判断、生成计划或选择动作；系统负责把目标、工具、状态、权限、观察结果、停止条件和评估组织起来。没有这些工程层，模型即使能写出“下一步我要做什么”，也只是一次文本生成或一次工具请求。

从来源边界看，OpenAI 的实践指南更强调构建 Agent 时要定义任务、工具、指令、边界和评估；Anthropic 的文章提醒不要把所有问题都做成高自主 Agent，很多稳定任务应先用 workflow；LangGraph 和 Agents SDK 类来源则把 state、graph、tool execution、trace、handoff 等实现细节显性化。它们对 Agent 的表述角度不同，但共同指向一个结论：现代 Agent 是模型判断和运行时控制的组合，不是模型本身。

学习 Agent 时要抓住两层：第一层是稳定地基，Agent 必须能围绕目标反复行动并利用 [[Observation]] 调整；第二层是现代工程吸收，具体行动通常被 [[Tool Calling]]、[[Agent State]]、[[Agent Workflow]]、[[Agent Harness]]、[[Trace]]、[[Evaluation]] 和 [[Human-in-the-loop]] 分担。这样就能避免两个极端：把普通 LLM 调用夸大成 Agent，或把 Agent 想象成完全自主、无需约束的机器人。

一个实用判断是看“责任是否跨过一次回答”。如果系统只负责把用户输入改写成答案，责任主要在模型输出；如果系统还负责选择工具、解释工具失败、保存中间状态、在预算内重试、把结果交给评测或人类确认，责任就已经进入 Agent 边界。这个判断能避免把“自动调用一次 API”的薄包装误判成 Agent，也能解释为什么同一个模型在不同 harness 下会表现出不同 Agent 能力。

最后，Agent 的边界要从“谁做决定”扩展到“谁承担后果”。一个真正的 Agent 系统要能解释：目标从哪里来，动作如何被限制，失败如何被发现，完成如何被证明，危险动作如何暂停。只要这些问题还没有答案，就算模型输出了连续步骤，也更像一个 agent-like demo，而不是可托付的 Agent 系统。
## 它解决什么问题

普通 [[LLM]] 更像一次性生成器：给它上下文，它给出回答。Agent 试图解决的是连续任务：任务需要多步执行、读取环境、调用工具、处理失败、保存中间状态，并根据反馈调整下一步。

更重要的是，Agent 不是为了“显得自主”，而是为了把一个目标推进到可检查的结果。OpenAI 的实践指南强调任务、工具、边界和评估；Anthropic 的工程建议提醒：很多场景用简单 workflow 更可靠，不需要一开始就追求复杂自主 Agent。这个张力是学习 Agent 的核心边界。

## 它不是什么

Agent 不等于聊天机器人。聊天机器人可以只回答问题，而 Agent 需要围绕目标产生行动和反馈闭环。

Agent 不等于“会调用工具的 LLM”。工具调用只是行动能力的一部分；没有目标分解、状态管理、错误处理、权限边界和结果评估，系统仍可能只是一次工具调用包装。

Agent 也不等于完全自主系统。很多可靠 Agent 会在付款、删除、发送、生产发布等高风险步骤前要求 [[Human-in-the-loop]] 或 approval gate。

## 最小例子

目标：整理一个文件夹里的会议记录。

Agent 可能会：

1. 查看文件列表。
2. 读取每个文件。
3. 提取日期、参与人和决议。
4. 写入汇总表。
5. 检查是否有遗漏。
6. 如果发现文件格式异常，记录问题或请求用户确认。

这里的关键不是“它会写总结”，而是它能围绕目标连续行动，并把观察结果反馈到下一步。

## 常见误解 / 风险

- 误解：模型越强，Agent 越不需要工程边界。风险是把权限、状态、评估和恢复都交给一次 prompt。
- 误解：越自主越先进。风险是简单任务被过度编排，成本、延迟和失败面都增加。
- 误解：有 trace 就说明 Agent 可靠。trace 只记录发生了什么，仍需要 [[Evaluation]] 判断是否做对。
- 风险：Agent 会把错误观察、过期检索、工具异常或用户模糊目标继续放大，直到产生看似完整但错误的结果。

## 边界细节

最小判断：如果系统只有“输入 -> 输出”，通常是 LLM 应用；如果它有“目标 -> 行动 -> 观察 -> 更新状态 -> 再行动”的循环，才更接近 Agent。

和相邻概念的区别：

- [[LLM]] 是能力底座；Agent 是围绕目标组织模型、工具和状态的系统。
- [[Agent Loop]] 是 Agent 的循环机制；Agent 是包含目标、工具、状态、权限、评估和人类介入的更大系统。
- [[Agent Workflow]] 更强调预先设计的步骤、分支和图；Agent 更强调在反馈中决定下一步。实际工程里两者常混合。
- [[Agent Harness]] 是包住 Agent 的运行时外壳，负责权限、工具执行、trace、重试、沙箱和停止条件；它不是模型本身。

反例：一个脚本调用 LLM 总结文档，不一定是 Agent；如果它会检查目录、根据失败重试、调用 OCR、向用户确认异常文件、最后生成可验证报告，就开始具备 Agent 形态。

## 现代性状态

- 判定：current-practice / foundation
- 为什么：Agent 作为“围绕目标行动的系统”是稳定基础概念；具体 SDK、框架、协议和产品实现仍在变化。
- 稳定部分：目标、行动、观察、状态、工具、反馈、评估、人类介入这些结构性要素。
- 易变部分：OpenAI Agents SDK、LangGraph、MCP、computer use、browser agent 等具体接口和最佳实践。
- 复查点：当多个主流框架同时改变 Agent/workflow 的抽象边界时，再更新本卡定义；单个 SDK API 变化优先写入对应 source note 或 [[03 前沿追踪]]。

## 现代系统怎么吸收 Agent 的价值 / 局限

现代系统通常不会把 Agent 只写成一个巨大 prompt，而是把它拆进工程层：

- runtime / framework 接管工具 schema、状态图、handoff、retry、durable execution 和 human-in-the-loop。
- harness 接管权限、沙箱、审计、trace、成本和停止条件。
- evaluation 接管最终结果、过程轨迹和回归测试，而不是只相信模型自评。
- workflow 把高确定性步骤固定下来，只在需要判断、检索、规划或异常处理时给 Agent 自主空间。

所以 Agent 的现代价值不是“让模型自由行动”，而是把模型判断放进可观测、可限制、可恢复、可评估的行动系统里。

## 证据锚点

- Source: [[OpenAI - A Practical Guide to Building Agents]]
- Anchor: [[OpenAI - A Practical Guide to Building Agents#一句话]]
- Source: [[Anthropic - Building Effective Agents]]
- Anchor: [[Anthropic - Building Effective Agents#一句话]] / [[Anthropic - Building Effective Agents#边界提醒]]
- Source: [[LangGraph 官方文档]]
- Anchor: [[LangGraph 官方文档#一句话]]
- Source: [[OpenAI Agents SDK 文档]]
- Anchor: [[OpenAI Agents SDK 文档#一句话]]
- Evidence type: source notes from official/practice docs; no long source excerpt copied here.
- Confidence: medium
- Boundary: “现代系统怎么吸收”是基于这些工程来源的综合理解，不是某一篇来源的逐字定义。

## 复习触发

- 如果一个系统能调用工具但没有状态、trace、权限或评估，你会不会叫它 Agent？为什么？
- 用自己的话解释：[[Agent]]、[[Agent Loop]]、[[Agent Workflow]]、[[Agent Harness]] 最小区别是什么？
- 举一个“不该用 Agent、简单 workflow 更好”的例子。

## 相关链接

- [[LLM]]
- [[Agent Loop]]
- [[Agent Workflow]]
- [[Agent Harness]]
- [[Tool Calling]]
- [[Memory]]
- [[Planning]]
- [[Evaluation]]
- [[Human-in-the-loop]]
