---
type: concept
topic:
  - agent
  - coding-agent
  - evaluation
status: seed
created: 2026-05-05
updated: 2026-05-05
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[SWE-bench]]"
evidence:
  - "[[SWE-bench#为什么收]]"
related:
  - "[[Agent]]"
  - "[[Repo Context]]"
  - "[[Patch Validation]]"
  - "[[Agent Harness]]"
---

# Coding Agent

## 一句话

Coding Agent 是能在代码库中理解问题、修改文件、运行验证并根据反馈继续修正的 Agent。

## 它解决什么问题

普通代码生成只写片段；真实软件工程需要理解 repo 结构、issue、依赖、测试和历史约束。Coding Agent 试图把这些步骤放进一个行动循环中。

## 它不是什么

Coding Agent 不只是代码补全。

它也不只是会写函数的 LLM。没有 repo context、测试验证和执行反馈，就很难称为完整代码 Agent。

## 最小例子

给 Agent 一个 GitHub issue，它读取相关文件，修改代码，运行测试，看到失败日志后继续修。

## 边界细节

代码 Agent 的可靠性通常要靠 [[Patch Validation]]、sandbox 和 [[Agent Harness]]。

## 证据锚点

- Source: [[SWE-bench]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent]]
- [[Repo Context]]
- [[Patch Validation]]
- [[Agent Harness]]
