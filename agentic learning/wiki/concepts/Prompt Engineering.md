---
type: concept
topic:
  - llm
  - prompting
  - agent
  - evaluation
status: growing
created: 2026-05-17
updated: 2026-05-17
source:
  - "[[123 01_AI 04_上下文工程与记忆 Prompt Engineering 及 Prompt 优化策略有哪些？]]"
  - "[[124 01_AI 04_上下文工程与记忆 Prompt Engineering 和微调策略如何协同？]]"
  - "[[127 01_AI 04_上下文工程与记忆 你如何定义“上下文工程”？和 Prompt Engineering 的边界是什么？]]"
  - "[[136 ai llm 16. 如何写好 Prompt？分享下 Prompt 工程实践经验？]]"
  - "[[Prompt]]"
  - "[[Context Engineering]]"
evidence:
  - "[[123 01_AI 04_上下文工程与记忆 Prompt Engineering 及 Prompt 优化策略有哪些？#题目正文]]"
  - "[[124 01_AI 04_上下文工程与记忆 Prompt Engineering 和微调策略如何协同？#题目正文]]"
  - "[[127 01_AI 04_上下文工程与记忆 你如何定义“上下文工程”？和 Prompt Engineering 的边界是什么？#题目正文]]"
  - "[[136 ai llm 16. 如何写好 Prompt？分享下 Prompt 工程实践经验？#页面正文]]"
  - "[[Prompt#证据锚点]]"
  - "[[Context Engineering#边界细节]]"
  - "[[Context Engineering#概念详解]]"
aliases:
  - prompt engineering
  - Prompt 工程
  - 提示词工程
  - 提示工程
freshness: stable
related:
  - "[[Prompt]]"
  - "[[Context Engineering]]"
  - "[[Evaluation]]"
  - "[[LLM Training Pipeline]]"
  - "[[RAG]]"
  - "[[Prompt Injection]]"
---

# Prompt Engineering

## 一句话

Prompt Engineering 是围绕 prompt 的设计、测试、版本管理和效果优化实践；它把“怎么给模型下任务”从一次性写指令，推进到可评估、可复用、可回滚的工程流程。

## 概念详解

Prompt Engineering 解决的不是“写一句神奇提示词”，而是如何稳定地把任务、角色、上下文、约束、示例、输出格式和证据使用规则组织成模型可执行的输入。它的工程性体现在：先有任务假设和失败样本，再设计 prompt 模板；修改后用测试集、A/B、人工抽检或自动评测验证；上线时记录版本、指标、成本和回滚路径。

早期 LLM 应用里，prompt engineering 常被理解为“把话说清楚”。这确实是起点，但不足以支撑生产系统。真实项目里，一个 prompt 需要回答：谁在说话、要完成什么任务、哪些资料可信、输出给谁看、格式如何被程序解析、哪些内容必须拒答、失败时如何降级。缺少这些边界，模型输出可能看似流畅，却不稳定、不可解析、不可复现。

在 Agent 和 RAG 系统里，Prompt Engineering 通常退到更大的 [[Context Engineering]] 之内。Prompt Engineering 关注指令文本和模板质量；Context Engineering 还要决定哪些 tool result、memory、retrieved evidence、trace summary、policy 和权限信息进入本轮上下文。换句话说，Prompt Engineering 负责“怎么说清任务和约束”，Context Engineering 负责“基于哪些信息说、按什么顺序说、旧信息何时淘汰”。

这个边界可以参考 [[Context Engineering#概念详解]] 中的图：左侧单轮 prompt 更像 system prompt + user message；右侧 Agent 上下文则多了文档、工具、memory、历史和 curation。

和微调的关系也不是二选一。Prompt Engineering 适合快速约束行为、探索任务边界、沉淀失败样本；[[LLM Training Pipeline|微调 / 后训练]] 更适合把稳定任务能力、风格或格式偏好固化到模型或 adapter 中。常见工程路径是 prompt 先行、评测闭环收集样本，再判断是否需要微调收口。

## 它解决什么问题

Prompt Engineering 解决的是“同一个模型在不同输入组织下表现差异很大”这个问题。它通过角色、任务、上下文、格式、示例、约束和评测闭环，降低模型理解偏差，让输出更可控、更容易被下游系统消费。

它也解决团队协作问题：如果 prompt 只是散落在代码里的长字符串，谁改了什么、为什么效果变差、哪个版本上线、哪些样例失败，都很难复盘。把 prompt 当工程资产管理，才能让优化从个人经验变成团队可维护流程。

## 它不是什么

Prompt Engineering 不是 [[Prompt]] 本身。Prompt 是输入内容；Prompt Engineering 是围绕输入内容的设计、实验和治理过程。

Prompt Engineering 不是 [[Context Engineering]] 的同义词。前者主要关注指令文本、模板、示例和输出约束；后者还管理多来源上下文的选择、排序、压缩、更新、权限和证据边界。

Prompt Engineering 不是微调。它在推理时改变输入，不直接改变模型参数；微调 / 后训练改变模型或 adapter 的长期行为。

Prompt Engineering 也不是安全边界。它可以要求模型遵守规则，但高风险动作仍需要工具权限、sandbox、approval gate、policy engine、audit log 和测试验证。

## 最小例子

```text
任务：把客服对话归类为 refund / complaint / technical / other。
约束：只输出 JSON，不要解释。
上下文：给出业务分类定义和 3 个 few-shot 示例。
评测：用 50 条历史工单跑回归测试，记录准确率和不可解析率。
回滚：如果不可解析率上升，回到 prompt-v3。
```

这个例子里，prompt 文本只是其中一部分；真正的 Prompt Engineering 包括样例选择、格式约束、评测集、指标和版本回滚。

## 常见误解 / 风险

- 误解：Prompt Engineering 就是把提示词写长。长 prompt 可能增加冲突、噪音、成本和截断风险。
- 误解：有了好的 prompt 就不用 RAG、工具、评测或权限控制。prompt 是软约束，不能替代系统边界。
- 误解：few-shot 越多越好。示例太多会挤占上下文预算，也可能让模型过拟合示例格式。
- 风险：prompt 模板只在 demo 样本上有效，一换真实输入就失效。
- 风险：把外部文档直接塞进 prompt，可能把 [[Prompt Injection]] 带进指令区域。
- 风险：prompt 优化只看主观感觉，不看 task success、格式错误率、延迟和 token 成本。

## 边界细节

和 [[Prompt]] 的边界：Prompt 是一次调用里的输入组织；Prompt Engineering 是围绕这类输入组织的工程实践。

和 [[Context Engineering]] 的边界：Prompt Engineering 更偏“指令和模板怎么写”；Context Engineering 更偏“本轮模型到底看到哪些信息，以及这些信息的来源、顺序、预算和生命周期”。

和 prompting pattern 的边界：[[Plan-and-Solve Prompting]]、[[Step-back Prompting]]、[[Zero-shot CoT]] 这类 pattern 是可被 Prompt Engineering 使用的局部方法，不等于 Prompt Engineering 全部。

和 fine-tuning 的边界：Prompt Engineering 是推理时控制；微调 / 后训练是训练或适配阶段控制。前者快、可回滚、成本低；后者更适合稳定固化能力，但数据和上线风险更高。

概念层级边界：本卡不直接写 `up`。Prompt Engineering 靠近 [[Prompt]]，但不是 Prompt 的一种；也靠近尚未形成稳定父类的 `Prompting`。本轮按 relation-only / parentless 概念处理，后续若要放入层级，应先补稳定 `Prompting` 或 `LLM Application Engineering` 类父概念，并走 taxonomy 候选生成、判定和 dry-run。

## 现代性状态

Prompt Engineering 是 foundation + transitional + current-practice。

- foundation：LLM 仍然通过输入上下文接收任务、规则、示例和输出约束。
- transitional：早期“提示词技巧”正在被更系统的 context engineering、eval harness、prompt registry、policy 和 tool runtime 吸收。
- current-practice：生产系统仍需要 prompt 模板版本化、回归评测、trace 记录、成本监控和回滚。

最值得保留的现代判断是：Prompt Engineering 没有消失，但它不再是唯一控制点。它从“写提示词”升级为“输入层工程资产管理”，并被纳入 Agent / RAG 的运行时治理。

## 现代系统怎么吸收 Prompt Engineering 的价值

现代系统通常把 prompt 拆成 system / developer / user / tool / evidence 等层，把模板放入版本管理，把样例和失败案例放入 eval set，并用 trace 记录每次调用的 prompt 版本、输入来源、token 成本、延迟、格式错误和任务成功率。

成熟系统还会把 prompt 和 context assembly 分开：Prompt Engineering 管模板与约束，Context Engineering 管动态材料装配，Evaluation 管效果判断，权限系统管能不能执行动作。这样 prompt 不需要承担所有责任，也更容易定位失败根因。

## 证据锚点

- [[123 01_AI 04_上下文工程与记忆 Prompt Engineering 及 Prompt 优化策略有哪些？#题目正文]]：把 prompt 优化放在预算管理、分层提示、最小必要上下文、按需注入、结构化约束和指标监测中。
- [[124 01_AI 04_上下文工程与记忆 Prompt Engineering 和微调策略如何协同？#题目正文]]：支持 prompt 先行、微调收口，以及 prompt 与训练调优不是替代关系。
- [[127 01_AI 04_上下文工程与记忆 你如何定义“上下文工程”？和 Prompt Engineering 的边界是什么？#题目正文]]：提供 Prompt Engineering 与 Context Engineering 边界问题。
- [[136 ai llm 16. 如何写好 Prompt？分享下 Prompt 工程实践经验？#页面正文]]：支持 prompt 工程需要角色、任务、上下文、格式、示例和测试迭代。
- [[Prompt#证据锚点]] / [[Context Engineering#边界细节]]：支持 Prompt、Prompt Engineering 与 Context Engineering 的层级和责任边界。
- Evidence type: raw interview source notes + existing concept cards + engineering synthesis.
- Boundary: 本卡把 Prompt Engineering 定义为 prompt 的工程实践层，不把它当作 Prompt 本身、Context Engineering 同义词、fine-tuning 或安全控制系统。
- Confidence: medium-high。

## 复习触发

- Prompt 和 Prompt Engineering 的最小区别是什么？
- 为什么 Prompt Engineering 不能替代 Context Engineering？
- Prompt Engineering 和 fine-tuning 如何协同，而不是互相替代？
- 一个 prompt 改动上线后效果变差，应该看哪些指标和回滚证据？

## 相关链接

- [[Prompt]]
- [[Context Engineering]]
- [[Evaluation]]
- [[LLM Training Pipeline]]
- [[RAG]]
- [[Prompt Injection]]
