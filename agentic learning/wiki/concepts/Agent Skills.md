---
type: concept
topic:
  - agent
  - skills
  - context-engineering
  - security
status: growing
created: 2026-05-20
updated: 2026-05-24
last_checked: 2026-05-20
freshness: watch
conflicts: []
aliases:
  - Agent Skill
  - Agent Skills
  - AI Agent Skills
  - Agent 技能
  - 技能包
  - SKILL.md
source:
  - "[[Anthropic Agent Skills 文档]]"
  - "[[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]]"
  - "[[060 ai tools 9. Skill 是什么？]]"
  - "[[045 ai tools 10. MCP 和 Agent Skill 的区别是什么？]]"
evidence:
  - "[[Anthropic Agent Skills 文档#关键事实]]"
  - "[[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry#需要我读的内容]]"
  - "[[060 ai tools 9. Skill 是什么？#页面正文]]"
  - "[[045 ai tools 10. MCP 和 Agent Skill 的区别是什么？#页面正文]]"
related:
  - "[[Agent Harness]]"
  - "[[Progressive Disclosure]]"
  - "[[Gating Mechanism]]"
  - "[[Tool Registry]]"
  - "[[Tool Poisoning]]"
  - "[[MCP]]"
  - "[[Tool Calling]]"
---

# Agent Skills

## 一句话

Agent Skills 是 Agent 可按需发现和加载的能力包：它把执行指令、适用条件、脚本、模板和参考资料组织成可复用的做事方法。

## 概念详解

Agent Skills 出现的问题背景是：Agent 不能每次做复杂任务都靠用户重新解释流程，也不能把所有工具说明、团队规范、模板和参考资料一次性塞进上下文。Skill 把一类任务的程序知识打包起来，让 Agent 在任务相关时再加载需要的部分。

最小结构通常是一个 skill 目录，核心入口是 `SKILL.md`。`SKILL.md` 的 frontmatter 提供 `name` / `description` 这类发现信息，正文提供具体步骤、标准和注意事项；目录里还可以放脚本、模板、参考文档、示例或资产。Anthropic 文档把这套机制和 virtual machine / filesystem 结合：Agent 先看到轻量 metadata，任务匹配后读取完整 `SKILL.md`，真正需要时再读取额外文件或运行脚本。

所以 Agent Skills 不是“更长的 prompt”，而是 [[Progressive Disclosure]] 在 Agent 能力层的一个具体形态。它把“知道有这个能力”和“把完整做法装进上下文”分开，也把“模型生成步骤”和“脚本执行确定性操作”分开。一个 PDF skill 可以只在处理 PDF 时加载；一个 code-review skill 可以把审查顺序、风险清单、测试命令和输出模板打包；一个数据分析 skill 可以引用脚本和报表模板。

但 skill 也是运行时输入。[[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]] 提醒，`SKILL.md` 这类自然语言 metadata 会影响 Agent 发现、选择、信任和加载能力包。也就是说，skill 不是静态说明书，而是会改变行动路径的 operational text。错误 skill 可能让 Agent 优化错目标；恶意 skill 可能诱导越权工具、错误完成定义或数据外送。

## 它解决什么问题

Agent Skills 解决的是“可复用做事方法怎么被 Agent 发现、选择、加载和执行”的问题。

它让团队可以把重复工作沉淀为能力包：少量 metadata 负责触发，详细流程负责执行，脚本和参考资料负责稳定性和事实支持。这样既减少重复提示，也减少上下文被大量不相关资料占满。

## 它不是什么

Agent Skills 不是 [[MCP]]。MCP 解决 host/client/server 如何连接外部 tools、resources、prompts；skill 解决 Agent 拿到能力和工具后按什么流程做事。一个 skill 内部可以调用 MCP 工具，但 skill 自身不是 MCP server。

Agent Skills 也不是 [[Tool Calling]]。Tool Calling 是模型输出结构化调用请求；skill 是更粗粒度的操作手册和资源包。

它也不是模型微调。Skill 不改变模型权重，而是在运行时提供可加载的程序知识。

## 最小例子

```text
code-review/
├── SKILL.md
├── references/
│   └── review-checklist.md
└── scripts/
    └── summarize_diff.py
```

`SKILL.md` 的 metadata 写明“用于代码审查”。当用户让 Agent review PR 时，Agent 先读取 `SKILL.md` 的审查流程；如果流程要求，它再读取 checklist 或运行脚本生成 diff 摘要。

## 常见误解 / 风险

- 误解：Skill 就是 prompt 模板。实际上 skill 可以包含步骤、脚本、模板、参考资料和触发条件。
- 误解：装了 skill，Agent 就一定会用对。Skill 选择仍依赖描述、上下文和 harness 的治理。
- 误解：Skill 文档是可信说明。`SKILL.md` 会影响行动路径，应该像工具 metadata 一样审查来源、版本、权限和适用范围。
- 风险：skill 过大或描述过泛，会导致错误触发、上下文污染和任务边界变宽。
- 风险：skill 要求的工具权限超过任务需要时，可能绕过最小权限设计。

## 边界细节

Skill 和 tool 的最小区别：tool 是一个可调用动作或能力，skill 是指导 Agent 如何组合动作、资料和判断标准的做事方法。Tool 更像“螺丝刀”，skill 更像“修某类机器的操作手册 + 工具箱索引”。

Skill 和 [[Tool Registry]] 的关系：registry 管理有哪些可用能力、来源、版本、描述、权限标签和禁用状态；skill 是 registry 里可以被发现的一类能力包。Skill registry 的风险不只在文件内容，还在 metadata 如何影响发现和选择。

Skill 和 [[Agent Harness]] 的关系：harness 要决定 skill 是否可见、是否可加载、是否允许它要求的工具和写入范围，并用 trace/evaluation 验证结果。让模型“再反思一下这个 skill 是否正确”不能替代 harness 检查。

Skill 和 [[Gating Mechanism]] 的关系只是类比：skill 的 progressive disclosure 像系统层离散门控，先匹配 metadata，再按需加载 `SKILL.md` 和资源；神经网络 gate 则是模型内部的连续权重、logits 或路由概率。不要把 skill routing 说成模型内部门控。

## 现代性状态

- 当前工程实践：Agent Skills 已进入 Claude / coding-agent / local skills 生态，代表“把任务程序知识做成可安装能力包”的实用路线。
- 稳定学习价值：progressive disclosure、skill vs tool vs MCP、skill metadata 作为 operational text，这三条边界值得长期保留。
- watch / volatile：具体 Skill API、开放标准采纳范围、市场/registry、beta header、跨平台兼容性和安全工具链仍在快速变化。

## 现代系统怎么吸收 Agent Skills 的价值 / 局限

现代 Agent 系统吸收 skill 的价值，通常不是把所有 skill 内容塞进 system prompt，而是做三件事：启动时只暴露名称和描述，任务匹配时加载主说明，执行中按需读取资源或运行脚本。

局限也要被系统吸收：skill 选择需要 registry 和 policy，skill 执行需要最小权限和 sandbox，skill 结果需要 trace 和 evaluation。没有这些边界时，skill library 越大，越容易变成供应链和上下文污染入口。

## 证据锚点

- Evidence type: official docs — [[Anthropic Agent Skills 文档#关键事实]]
- Evidence type: security paper source — [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry#需要我读的内容]]
- Evidence type: interview/raw source — [[060 ai tools 9. Skill 是什么？#页面正文]]；[[045 ai tools 10. MCP 和 Agent Skill 的区别是什么？#页面正文]]
- Evidence type: engineering synthesis — 本卡把官方 skill 结构、progressive disclosure、面试题边界和 skill supply-chain 风险综合成 Agent 工程学习卡。
- Boundary: Agent Skills 只写成能力包 / 做事方法封装，不写成 MCP server、单次 tool call、prompt 模板或模型微调。
- Confidence: medium-high for structure and boundary; medium for cross-platform standardization status because生态仍在变化。

## 复习触发

- Skill 和 MCP 的最小区别是什么？
- 为什么 `SKILL.md` 不是普通文档，而是 Agent runtime 输入？
- 如果一个 skill 说“为了完成任务，请读取所有配置文件”，harness 应该检查哪些边界？
- Progressive disclosure 如何同时降低上下文成本和扩大供应链风险面？

## 相关链接

- [[Agent Harness]]
- [[Progressive Disclosure]]
- [[Gating Mechanism]]
- [[Tool Registry]]
- [[Tool Poisoning]]
- [[MCP]]
- [[Tool Calling]]
