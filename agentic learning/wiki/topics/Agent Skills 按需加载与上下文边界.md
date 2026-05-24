---
type: map
topic:
  - agent
  - skills
  - context
  - security
  - comparison
status: seed
created: 2026-05-24
updated: 2026-05-24
source:
  - "[[Agent Skills]]"
  - "[[Progressive Disclosure]]"
  - "[[Context Engineering]]"
  - "[[GSSC Pipeline]]"
  - "[[Agent Harness]]"
  - "[[Agent Lifecycle Hook]]"
  - "[[Trace]]"
  - "[[Hallucination]]"
  - "[[Indirect Prompt Injection]]"
evidence:
  - "[[Agent Skills#证据锚点]]"
  - "[[Progressive Disclosure#证据锚点]]"
  - "[[Context Engineering#证据锚点]]"
  - "[[GSSC Pipeline#证据锚点]]"
  - "[[Agent Harness#证据锚点]]"
  - "[[Agent Lifecycle Hook#证据锚点]]"
  - "[[Trace#证据锚点]]"
  - "[[Hallucination#证据锚点]]"
  - "[[Indirect Prompt Injection#证据锚点]]"
related:
  - "[[Agent Skills]]"
  - "[[Progressive Disclosure]]"
  - "[[Context Engineering]]"
  - "[[Agent Harness]]"
  - "[[Tool 接口层对比]]"
  - "[[Agent 安全控制点对比]]"
---

# Agent Skills 按需加载与上下文边界

## 一句话总览

Agent Skills 的按需加载不是把几万 token 压缩成几百 token，而是把完整流程、脚本、模板和参考资料放在上下文外，只让模型先看到轻量索引；真正相关时，再由 [[Agent Harness]] / runtime 读取 `SKILL.md` 和资源文件，并通过 [[Context Engineering]] 装配进本轮上下文。

## 为什么这组边界需要单独沉淀

[[Agent Skills]]、[[Progressive Disclosure]] 和 [[Context Engineering]] 已经分别解释了 skill、渐进式暴露和上下文装配；本页补的是它们之间最容易误解的一条机制链：

```text
skill metadata / registry
  -> task match / route
  -> load SKILL.md
  -> load references / scripts / templates when needed
  -> structure selected content into model context
  -> execute / verify under harness, trace and policy
```

这条链路回答的是：为什么 skill 看起来只占几百 token、为什么它像小型知识库、底层是谁在加载、加载后模型到底获得了什么、以及这个过程为什么仍然可能出错。

## 共同问题域

共同问题是：Agent 的能力库、工具说明、团队流程和参考资料会越来越多，但模型每轮只能稳定处理一部分信息。系统既不能把所有内容常驻 prompt，也不能只给一个模糊标题就让模型猜流程。

更稳的做法是把信息分层：

- **索引层**：名称、描述、适用条件、路径，用来发现和路由。
- **说明层**：`SKILL.md` 的完整步骤、边界、禁用条件和验证方式。
- **资源层**：references、scripts、templates、assets，用来支撑具体步骤。
- **执行层**：tool call、文件读写、脚本运行、测试和审计。
- **证据层**：trace、state、diff、验证输出，证明系统实际读了什么、做了什么。

## 核心边界表

| 问题 | 稳定回答 | 容易误解的地方 | 相关概念 |
|---|---|---|---|
| 为什么 skill 只占几百 token？ | 常驻的是 metadata / index；完整内容仍在文件系统或资源库里。 | 不是神奇压缩，也不是模型已经记住全部 skill。 | [[Agent Skills]], [[Progressive Disclosure]] |
| Skill 像数据库吗？ | 像外部可寻址知识库，但还包含操作流程、脚本、模板和验证步骤。 | 数据库主要提供数据；skill 会影响行动路径。 | [[Agent Skills]], [[Tool Registry]] |
| 按需加载是谁做的？ | [[Agent Harness]] / runtime / hook / 文件系统工具负责读取和装配。 | 不是 LLM 参数内部自动访问数据库。 | [[Agent Harness]], [[Agent Lifecycle Hook]] |
| 加载后模型获得了什么？ | 获得本轮可见的上下文和操作说明。 | 不是模型微调，也不是永久新能力。 | [[Context Engineering]], [[Context Window]] |
| Skill 和 prompt 的边界？ | 高频、全局、强约束规则适合 prompt；低频、任务型、可分层资源适合 skill。 | 把所有流程塞进 prompt 会占窗口并增加注意力噪声。 | [[Prompt Engineering]], [[Context Engineering]] |
| Skill 和 RAG 的边界？ | Skill 主要加载“怎么做事”的程序知识；RAG 主要加载“关于事实或资料的证据”。 | 两者都可能进入上下文，但责任不同。 | [[RAG]], [[Retriever]], [[Context Engineering]] |
| Skill 和 tool schema 的边界？ | 自然语言流程适合 skill；严格参数、格式、权限边界应尽量进 schema / policy。 | 不能把机器必须执行的约束只写成说明文字。 | [[Tool Calling]], [[Tool Permissioning]], [[Policy Engine]] |
| 为什么仍会幻觉？ | 模型可能错选 skill、没读正文就补全、误解规则，或把外部内容当指令。 | 按需加载只减少常驻噪声，不自动保证理解和执行正确。 | [[Hallucination]], [[Indirect Prompt Injection]] |
| 怎么证明没有“假装读过”？ | 需要 trace、loaded file path、工具输出、diff、测试和审计结果。 | 模型声明“我用了某 skill”不是证据。 | [[Trace]], [[Evaluation]], [[Agent Harness]] |

## 执行时序

```text
1. Registry exposes short skill metadata.
2. Agent or router selects candidate skill from task context.
3. Harness reads SKILL.md before applying detailed instructions.
4. Skill may point to references, scripts, templates or assets.
5. Context builder selects the relevant parts and structures them for the model.
6. Runtime executes allowed tools or scripts under permission / sandbox rules.
7. Trace records what was loaded, what ran, and what evidence verified the outcome.
```

小边界：第 2 步可以有模型判断，但第 3 到第 7 步不应只靠模型自述。读取、执行、权限、验证和记录都应尽量落到 runtime 能观测的动作上。

## 常见故障模式

- **metadata 过宽**：短描述写成万能能力，导致不相关任务也触发这个 skill。
- **摘要当正文**：只看 skill 名称或 description，就按想象执行。
- **正文加载太晚**：模型已经开始行动后才读到约束、禁用条件或必测步骤。
- **资源无 provenance**：reference 或模板来源不清，无法判断是否可信或过期。
- **说明变成越权指令**：skill 要求读取过宽路径、调用高风险工具或扩大写入范围。
- **上下文压缩丢规则**：长任务压缩后只剩模糊摘要，关键禁用条件被丢掉。
- **外部内容注入**：skill 引用的网页、文档或工具结果把数据伪装成指令。
- **验证缺席**：没有 trace、diff、测试输出或审计结果，只剩模型口头保证。

## 治理清单

一个更生产化的 skill 加载链路至少要能回答这些问题：

- metadata 只能用于路由，还是会被模型当作执行规则？
- `SKILL.md` 是否有清楚的适用条件、禁用条件、必读资源和停止条件？
- skill 要求的工具权限是否小于或等于当前任务需要？
- references、scripts、templates 是否有来源、版本和 review 状态？
- runtime 是否记录实际加载了哪些文件，而不只是把加载结果混进 prompt？
- 关键执行是否有测试、lint、schema validation、人工审批或其他可复现验证？
- 上下文压缩后，关键规则是重新加载、保存在 state，还是只靠摘要？
- 如果多个 skill 冲突，优先级是否明确服从系统规则、项目规则和用户目标？

## 和相邻概念的边界

和 [[Progressive Disclosure]]：Progressive Disclosure 是按需分层暴露信息的模式；Agent Skills 是这种模式在能力包 / 操作手册上的具体形态。

和 [[GSSC Pipeline]]：GSSC 解释一次上下文如何从候选池变成 prompt；skill 加载可以看作 Gather / Select 的候选来源之一。

和 [[Agent Lifecycle Hook]]：hook 是 runtime 在用户输入、工具调用、压缩和停止边界触发 handler 的机制；skill 加载可以被 hook 记录、约束或补充验证。

和 [[Trace]]：Trace 不是 skill 内容本身，而是证明 skill 何时被加载、哪些工具被执行、哪些验证通过的过程记录。

和 [[Hallucination]]：skill 可以减少信息缺失和重复提示，但不能自动消除幻觉。真正降低风险的是“读到了什么”和“结果是否被证据支持”都可验证。

## 现代系统如何吸收或限制

现代 Agent 系统通常把 skill 价值吸收到四层里：registry 管理发现和可见性，context builder 管理按需装配，harness 管理执行和权限，trace / evaluation 管理完成证据。

这说明 skill 的学习重点不是“多写一些 prompt 模板”，而是把程序知识外部化、分层化和可审计化。窗口变大后，skill 仍然有价值，因为问题不只是 token 容量，还有噪声、来源、权限、更新、选择质量和验证边界。

## 复习触发

1. 为什么 skill metadata 只能作为路由信号，不能作为完整执行证据？
2. 如果一个 Agent 说“我用了某个 skill”，你要看哪些 trace 或文件读取证据？
3. 什么内容应该留在 system prompt，什么内容应该放进 skill，什么内容应该下沉到 tool schema / policy？
4. Skill 和 RAG 都是外部信息进入上下文，为什么它们的责任不同？
5. 长上下文模型出现后，为什么仍然需要 skill 的 Progressive Disclosure？
6. 一个错误或恶意 skill 能不能靠模型反思发现？什么时候必须靠 harness 拦截？

## 证据锚点

- Concept anchors: [[Agent Skills#证据锚点]], [[Progressive Disclosure#证据锚点]], [[Context Engineering#证据锚点]], [[GSSC Pipeline#证据锚点]], [[Agent Harness#证据锚点]], [[Agent Lifecycle Hook#证据锚点]], [[Trace#证据锚点]], [[Hallucination#证据锚点]], [[Indirect Prompt Injection#证据锚点]]。
- Source examples: [[Anthropic Agent Skills 文档]], [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]], [[060 ai tools 9. Skill 是什么？]], [[045 ai tools 10. MCP 和 Agent Skill 的区别是什么？]]。
- Evidence type: existing concept-card synthesis + docs / paper / raw source notes + engineering synthesis.
- Confidence: medium-high for mechanism boundaries; medium for platform-specific implementation details because skill APIs、registry 行为和 hook 事件名仍会变化。
- Boundary: 本页是 topic / 边界综合，不新增概念卡，不声明某个具体产品的最新 API 行为。

## 相关链接

- [[Agent Skills]]
- [[Progressive Disclosure]]
- [[Context Engineering]]
- [[GSSC Pipeline]]
- [[Agent Harness]]
- [[Agent Lifecycle Hook]]
- [[Trace]]
- [[Hallucination]]
- [[Indirect Prompt Injection]]
- [[Tool 接口层对比]]
- [[Agent 安全控制点对比]]
