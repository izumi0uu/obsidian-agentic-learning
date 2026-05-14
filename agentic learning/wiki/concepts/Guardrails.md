---
type: concept
topic:
  - security
  - agent
  - evaluation
status: growing
created: 2026-05-06
updated: 2026-05-14
last_checked: 2026-05-14
freshness: watch
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[OpenAI Agents SDK 文档]]"
  - "[[Workflow Guardrails 主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[OpenAI Agents SDK 文档#为什么收]]"
  - "[[Workflow Guardrails 主源#值得先读的主源]]"
related:
  - "[[Workflow Guardrails]]"
  - "[[Policy Engine]]"
  - "[[Approval Gate]]"
  - "[[Prompt Injection]]"
  - "[[Tool Permissioning]]"
---

# Guardrails

## 一句话

Guardrails 是限制、检查或修正模型输入、输出和工具动作的安全/质量边界。

## 概念详解

Guardrails 的问题背景是 Agent 系统会把模型输出接到工具、数据和用户动作上，单靠“请遵守规则”的 system prompt 不足以控制风险。Guardrails 把安全、质量、格式、权限和任务边界做成可执行检查：输入进来时先判断是否可处理，模型输出后检查是否合规，工具调用前判断动作是否被允许，必要时触发人工审批或拒绝。

机制上，guardrails 可以由多种东西组成：规则、分类器、schema validation、policy engine、allow/deny list、敏感信息检测、工具参数检查、人类审批、trace 审计和回退策略。OpenAI Agents SDK source note 把 guardrails 和 agents、tools、handoffs、tracing 并列，说明现代 guardrails 是 Agent runtime 的工程抽象，而不是单句提示。Agent 工程基础设施 source note 又列出 NeMo Guardrails、OpenAI Agents SDK guardrails、Promptfoo red teaming 等主源，说明它横跨运行时控制和评测验证。

它和 [[Policy Engine]] 的边界：policy engine 更像规则决策核心；guardrails 是更宽的防护层，可能调用 policy engine，也可能调用分类器或 schema 检查。它和 [[Evaluation]] 的边界：evaluation 衡量系统表现，guardrails 在运行中拦截或修正。好的 guardrails 必须承认误判和绕过风险，所以要和 least privilege、approval gate、sandbox、trace、red team 一起使用。

在现代 Agent 系统里，guardrails 常被拆成 input guardrail、output guardrail 和 tool/action guardrail。input guardrail 判断请求是否越权或含攻击；output guardrail 检查格式、敏感信息和合规；tool/action guardrail 拦截高风险调用。这个拆分能避免一种常见浅理解：只在最终回答上做过滤，却让模型已经读取了不该读的数据或调用了不该调用的工具。

[[Workflow Guardrails]] 是这张卡的 workflow 层展开：当系统有 handoff、delegated specialist、RAG、tool calling 或持久化副作用时，guardrail 应该贴近 workflow 边界，例如 retrieval 后、tool/internal API 调用前、validated output 写库前、transaction commit 前和 state failure hook 处。这样 guardrails 才不是最后一道“内容过滤网”，而是工作流中的多个可审计控制点。


## 它解决什么问题

Agent 可能输出不合规内容、误用工具、泄露数据、忽略格式、执行高风险动作。Guardrails 把部分规则放到模型调用前后或工具调用前后。

代表生态包括 NVIDIA NeMo Guardrails、OpenAI Agents SDK guardrails、Guardrails AI、Llama Guard 类模型。

## 它不是什么

Guardrails 不是绝对安全。

它也不是只写一句 system prompt。真实 guardrails 可能包括规则、分类器、schema validation、policy engine、人类审批和审计。

## 最小例子

```text
user input -> input guardrail -> agent -> tool call guardrail -> output guardrail -> response
```

## 常见误解和风险

- guardrail 本身也会误判。
- 只拦输出不拦工具动作，仍可能造成损害。
- 过严会让系统不可用，过松会形同虚设。

## 边界细节

Guardrails 不是绝对安全，也不是只写 system prompt。它适合降低已知风险和格式错误，但会误判、漏判和被绕过。越靠近真实工具动作，越需要 policy、approval、sandbox 和 trace 一起约束。

## 现代性状态

current-practice / watch。Guardrails 已是现代 Agent runtime 常见抽象，但具体 SDK、分类器、schema、red-team 工具和策略接口会变化。不要把某一产品能力写成概念定义。

## 证据锚点

- Evidence type: source evidence — [[Agent 工程基础设施主源#为什么收]]；[[OpenAI Agents SDK 文档#为什么收]]
- Evidence type: workflow placement — [[Workflow Guardrails 主源#值得先读的主源]]
- Evidence type: source boundary — 本卡只使用现有 source note / project note 的小节级证据；未伪造段落、页码或不存在的小节。
- Evidence type: engineering synthesis — “概念详解”“边界细节”“现代性状态”把 [[Agent 工程基础设施主源]]；[[OpenAI Agents SDK 文档]] 与本 vault 的 Agent 工程学习目标综合起来。
- Boundary: source note 多数仍是 seed/growing 级摘要；除 frontmatter 的 `last_checked` 外，不把具体 API 字段、SDK 版本或 registry 状态写成长期稳定事实。
- Confidence: medium

## 复习触发

- Guardrails 和 system prompt 的边界是什么？
- 为什么 guardrails 需要和 trace/eval/approval 一起使用？

## 相关链接

- [[Policy Engine]]
- [[Approval Gate]]
- [[Prompt Injection]]
- [[Tool Permissioning]]
- [[Workflow Guardrails]]
