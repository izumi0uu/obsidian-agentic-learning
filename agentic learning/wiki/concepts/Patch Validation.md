---
type: concept
topic:
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
  - "[[Coding Agent]]"
  - "[[Evaluation]]"
  - "[[Agent Harness]]"
---

# Patch Validation

## 一句话

Patch Validation 是验证代码修改是否真正解决问题且没有破坏旧功能的过程。

## 它解决什么问题

LLM 生成的代码可能能读，但不一定能运行。Patch Validation 用测试、lint、typecheck 或人工审查来检查 patch 是否有效。

## 它不是什么

Patch Validation 不只是“代码看起来对”。

它也不保证没有隐藏 bug。测试覆盖不足时，patch 通过测试仍可能有问题。

## 最小例子

SWE-bench 把模型生成的 patch 应用到 repo，然后运行相关测试。测试通过才算 resolved。

## 边界细节

Patch Validation 是代码 Agent harness 的核心部分。

## 证据锚点

- Source: [[SWE-bench]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Coding Agent]]
- [[Evaluation]]
- [[Agent Harness]]
