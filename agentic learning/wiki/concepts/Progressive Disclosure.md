---
type: concept
topic:
  - agent
  - context
  - tools
status: seed
created: 2026-05-18
updated: 2026-05-18
last_checked: 2026-05-18
freshness: watch
conflicts: []
aliases:
  - 渐进式披露
  - 渐进披露
  - 渐进式加载
  - progressive disclosure
source:
  - "[[060 ai tools 9. Skill 是什么？]]"
  - "[[045 ai tools 10. MCP 和 Agent Skill 的区别是什么？]]"
  - "[[Hermes Agent Repo]]"
  - "[[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]]"
  - "[[RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents]]"
evidence:
  - "[[060 ai tools 9. Skill 是什么？#页面正文]]"
  - "[[045 ai tools 10. MCP 和 Agent Skill 的区别是什么？#页面正文]]"
  - "[[Hermes Agent Repo#关键事实]]"
  - "[[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry#为什么收]]"
  - "[[RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents#为什么收]]"
related:
  - "[[Context Engineering]]"
  - "[[Context Window]]"
  - "[[Tool Registry]]"
  - "[[Agent Harness]]"
  - "[[MCP]]"
  - "[[Tool Calling]]"
---

# Progressive Disclosure

## 一句话

Progressive Disclosure 是把工具、skill、文档或上下文资源分层暴露给 Agent：先给轻量索引和摘要，确认需要后再加载完整说明、schema、脚本或参考资料。

## 概念详解

Progressive Disclosure 最初是通用交互设计思想：不要一次性把所有细节压给使用者，而是先暴露能做选择的少量信息，再按任务需要展开更深层内容。在 Agent 工程里，它变成了一个很实用的 [[Context Engineering]] 模式，因为模型的 [[Context Window]]、注意力和工具选择能力都有限。

在 Skill 场景里，它通常表现为三层：启动时只给 Agent 看 skill 的名字和一句话描述；当任务匹配某个 skill 时，再加载 `SKILL.md` 的完整流程指令；执行过程中真的需要模板、脚本或参考资料时，才继续读取对应资源。这样 skill library 可以很大，但单次任务上下文仍保持精简。

在工具和 registry 场景里，它回答的是同一个问题：如果系统有几十到几千个工具，是否要把所有工具 schema 和长描述都塞进 prompt？更稳的做法通常是先暴露工具类别、短描述或候选摘要，再按任务逐步展开更具体的 tool docs、参数 schema 或执行权限。[[RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents]] 这类论文把它进一步操作化为工具空间里的主动探索策略，但它不是 Progressive Disclosure 的唯一形态。

它的核心价值不是“隐藏信息”，而是控制信息出现的时机。对模型来说，太早出现的细节会变成噪声；太晚出现的细节会导致工具误选或流程缺失。Progressive Disclosure 的工程目标是让 Agent 在每一步看到足够决策的信息，但不被当前任务不需要的信息淹没。

## 它解决什么问题

- 节省上下文预算：避免所有 skill、工具 schema、长文档和模板一次性进入 prompt。
- 降低选择噪声：先让 Agent 在短描述或类别层面选择，再展开候选细节。
- 支持大规模能力库：skill registry、tool registry、repo docs 和操作手册可以很多，但每轮只加载相关部分。
- 改善可审计性：系统可以记录“何时暴露了什么信息”，而不是只有一个巨大混合 prompt。

## 它不是什么

Progressive Disclosure 不是 [[Tool Calling]]。Tool Calling 是模型发出结构化工具调用请求；Progressive Disclosure 是决定工具/skill 信息什么时候、以多细粒度进入上下文。

它也不是 [[MCP]]。MCP 是连接工具、资源和 prompt 的协议；Progressive Disclosure 可以用于 MCP host 呈现 tools/resources 的方式，但不是协议本身。

它也不是简单的“少给一点上下文”。少给但不给关键 schema、权限、输入约束或错误边界，会让 Agent 误判任务。Progressive Disclosure 要求按需展开，而不是永远压缩。

它也不等同于 Progressive Active Tool Exploration。后者是更具体的 Agent 主动探索工具空间机制；Progressive Disclosure 是更通用的信息分层暴露原则。

## 最小例子

```text
启动阶段：
  code-review: Review code changes for correctness and security.
  data-report: Generate structured data analysis reports.

任务匹配后：
  load code-review/SKILL.md

执行到报告输出步骤时：
  load code-review/assets/report_template.md
```

模型先知道“有哪些能力”，再知道“选中的能力怎么执行”，最后才读取“这一步真正要用的资源”。

## 常见误解 / 风险

- 误解：只要把工具列表做成检索，就是 Progressive Disclosure。检索是实现方式之一，关键仍是分层、按需和可验证展开。
- 误解：Progressive Disclosure 会自动提升准确率。它主要减少噪声和上下文浪费，是否更准还取决于路由、描述质量、权限和验证。
- 风险：短描述写得过度营销，会让 Agent 错选 skill 或工具。
- 风险：完整说明加载太晚，会让模型在缺 schema、限制或安全条件时过早行动。
- 风险：registry 里的 metadata 会影响发现和选择，因此也可能成为 skill/tool supply-chain 攻击面。

## 边界细节

和 [[Context Engineering]] 的边界：Context Engineering 是更大的运行时信息装配问题；Progressive Disclosure 是其中一种按需分层暴露策略。

和 [[Tool Registry]] 的边界：Tool Registry 是能力目录；Progressive Disclosure 是目录内容如何被呈现和展开。一个 registry 可以支持 progressive disclosure，也可以只是把所有 schema 平铺给模型。

和 Skill 的边界：Skill 是可复用能力包；Progressive Disclosure 是 Skill 被发现、加载和读取辅助资源时常用的加载方式。没有单独的 Skill 卡时，本卡只记录这个加载/披露模式，不把 Skill 本身的定义吞进来。

和 [[Agent Harness]] 的边界：Harness 负责真正执行、权限、trace 和验证。Progressive Disclosure 只能控制信息暴露，不能替代 sandbox、approval、policy 或 evaluation。

## 层级归属

本卡暂不写 `up`。它不是 [[Tool Use]]、[[Tool Registry]] 或 [[Context Engineering]] 的严格下位概念，而是横跨 skill、tool docs、repo context 和 UI/文档结构的信息暴露模式。当前按 relation-only / parentless terminal 处理，后续如果 vault 建立更稳定的“Context Management Pattern”父类，再重新审计。

## 现代性状态

- 判定：current-practice / watch。
- 稳定部分：大规模 skill、tool、repo context 和文档体系都需要按需加载，不能无限平铺进上下文。
- 易变部分：不同 Agent 产品如何实现 skill discovery、tool summary、resource loading、MCP resources 和 registry ranking 会快速变化。
- 复查点：当模型长上下文变大时，仍要检查噪声、权限、攻击面和选择质量，而不是假设上下文预算问题已经消失。

## 现代系统怎么吸收 Progressive Disclosure 的价值

现代 Agent harness 通常会把可用能力拆成“短描述 / 详细说明 / 执行资源 / 外部工具”几层。短描述用于路由，详细说明用于生成计划和约束执行，资源文件在具体步骤中读取，工具 schema 在真正候选集合缩小后展示。这样可以让系统在能力库扩张时仍保持任务上下文清晰。

在安全上，Progressive Disclosure 还应该和 provenance、review 状态、权限和 trace 绑定。因为越晚加载的信息越容易在关键执行时改变 Agent 行为，系统需要知道这些信息来自哪里、是否可信、何时被加载、是否触发了高风险工具。

## 证据锚点

- Source: [[060 ai tools 9. Skill 是什么？]]；小林 Note 用 Skill 的三层加载解释“渐进式加载 / Progressive Disclosure”如何节省 context window。
- Source: [[045 ai tools 10. MCP 和 Agent Skill 的区别是什么？]]；小林 Note 把 Skill 的按需加载和 MCP 原子工具粒度分开。
- Source: [[Hermes Agent Repo]]；Hermes source note 记录 Skills docs 使用 progressive disclosure 并兼容 agentskills.io。
- Source: [[Under the Hood of SKILL.md - Semantic Supply-chain Attacks on AI Agent Skill Registry]]；论文 source note 支持 skill metadata 会影响发现、选择和治理，extracted 文本把 progressive disclosure 作为 skill 加载设计背景。
- Source: [[RS-Claw - Progressive Active Tool Exploration via Hierarchical Skill Trees for Remote Sensing Agents]]；论文 source note 支持工具太多导致 flat 注册爆上下文的问题；本卡只把它作为相邻机制证据，不把论文方法等同于通用概念。
- Evidence type: raw source notes + paper extracted evidence + engineering synthesis.
- Confidence: medium
- Boundary: 本卡沉淀的是按需分层暴露信息的通用 Agent 工程模式；不把 Skill 本身、MCP 协议、Tool Calling 接口或 RS-Claw 的 Progressive Active Tool Exploration 算成同义词。

## 复习触发

- Progressive Disclosure 和“直接把所有工具 schema 塞进 prompt”的差别是什么？
- 为什么它能节省 context window，但不能替代权限、验证和工具选择评估？
- Skill、MCP tools、repo context 三个场景里，分别可以如何做分层暴露？

## 相关链接

- [[Context Engineering]]
- [[Context Window]]
- [[Tool Registry]]
- [[Agent Harness]]
- [[MCP]]
- [[Tool Calling]]
