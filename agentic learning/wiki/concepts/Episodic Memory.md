---
type: concept
topic:
  - memory
  - agent
  - frontier
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[LangGraph Memory 官方文档]]"
  - "[[Mem0 Memory 官方文档]]"
evidence:
  - "[[LangGraph Memory 官方文档#为什么收]]"
  - "[[Mem0 Memory 官方文档#为什么收]]"
related:
  - "[[Memory]]"
  - "[[Long-term Memory]]"
  - "[[Semantic Memory]]"
  - "[[Trace]]"
---

# Episodic Memory

## 一句话

Episodic Memory 保存过去发生过的事件、任务轨迹、操作结果和经验样例。

## 它解决什么问题

Agent 不只需要知道事实，还需要知道“之前发生了什么、当时做了什么、结果怎样”。这能帮助它复盘失败、复用成功路径、避免重复踩坑。

## 它不是什么

Episodic Memory 不是稳定知识库。

它更像“经历记录”。从经历中提炼出的长期规则，才可能进入 [[Semantic Memory]] 或 procedural memory。

## 最小例子

一次论文处理失败的 episodic memory：

- 处理 `Attention Is All You Need.pdf`。
- `pdftotext` 能抽正文，但公式、表格和图结构损失严重。
- 下次需要同时保留 PDF、抽取 Markdown，并人工检查关键图表。

## 常见误解 / 风险 / 边界细节

- 事件太多会淹没重要经验。
- 单次失败不能直接变成长期规则。
- trace 可以生成 episodic memory，但 trace 本身不是 memory。
- 事件记忆也可能包含隐私和敏感数据。

## 证据锚点

- Source: [[LangGraph Memory 官方文档]]
- Source: [[Mem0 Memory 官方文档]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Long-term Memory]]
- [[Semantic Memory]]
- [[Trace]]
- [[Replay]]
