---
type: concept
topic:
  - evaluation
status: seed
created: 2026-05-05
updated: 2026-05-05
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[GAIA Benchmark]]"
  - "[[SWE-bench]]"
evidence:
  - "[[GAIA Benchmark#为什么收]]"
  - "[[SWE-bench#为什么收]]"
related:
  - "[[Evaluation]]"
  - "[[Task Success Rate]]"
---

# Benchmark

## 一句话

Benchmark 是用一组固定任务和评分方式来比较系统能力的评测集合。

## 它解决什么问题

没有 benchmark，Agent 很容易只靠 demo 给人“看起来很强”的感觉。Benchmark 让不同模型或系统可以在同一任务集上比较。

## 它不是什么

Benchmark 不是现实世界能力的完整证明。

一个系统在 benchmark 上高分，不等于在你的真实任务中可靠。Benchmark 也可能被污染、被刷榜、过时或覆盖面不足。

## 最小例子

GAIA 用真实助手问题评估通用 AI assistant；SWE-bench 用真实 GitHub issue 评估代码修改能力。

## 边界细节

Agent benchmark 应该尽量评估任务完成，而不仅是文本答案好不好看。

## 证据锚点

- Source: [[GAIA Benchmark]]
- Source: [[SWE-bench]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Evaluation]]
- [[Task Success Rate]]
- [[GAIA Benchmark]]
- [[SWE-bench]]
