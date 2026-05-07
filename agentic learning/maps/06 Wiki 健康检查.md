---
type: map
topic:
  - maintenance
  - llm-wiki
status: active
created: 2026-05-07
updated: 2026-05-07
related:
  - "[[LLM Wiki 工作流]]"
  - "[[04 页面目录]]"
  - "[[05 Query 写回队列]]"
  - "[[字段规范]]"
---

# 06 Wiki 健康检查

这页记录周期性 lint、freshness 和 contradiction check 的结果。

## 当前状态

- Last lint: 2026-05-07
- Missing links: none
- Concept cards: 81
- Raw source notes: 47
- Query write-back pending: 0

## 每周检查清单

- [ ] 更新 [[04 页面目录]]。
- [ ] 跑 missing-link scan。
- [ ] 检查概念卡是否有“它不是什么”。
- [ ] 检查概念卡是否有“证据锚点”。
- [ ] 检查 raw source 是否有 `last_checked` 和 `freshness`。
- [ ] 处理 [[05 Query 写回队列]]。
- [ ] 把发现的问题追加到本页。

## Freshness 规则

| freshness | 复查节奏 | 适用对象 |
|---|---|---|
| stable | 低频，学习复盘时查 | 经典论文、基础概念 |
| watch | 每月 | 框架、repo、前沿方向 |
| volatile | 1-2 周 | API 文档、安全榜单、活跃产品 |
| stale | 立即 | 已发现可能过期的来源 |

## 待复查来源

```dataview
TABLE source_type, site, freshness, last_checked, status
FROM "raw"
WHERE type = "source" AND (freshness = "watch" OR freshness = "volatile" OR freshness = "stale")
SORT freshness DESC, last_checked ASC
```

## 证据锚点缺口

```dataview
TABLE source, evidence, status, updated
FROM "wiki/concepts"
WHERE type = "concept" AND !evidence
SORT file.name ASC
```

## 潜在矛盾

| 日期 | 概念 | 冲突说法 | 来源 | 处理状态 |
|---|---|---|---|---|
| 2026-05-07 | [[Agent]] | OpenAI、Anthropic、LangGraph 对 Agent/workflow 边界表述不同 | [[OpenAI - A Practical Guide to Building Agents]], [[Anthropic - Building Effective Agents]], [[LangGraph 官方文档]] | pending |
| 2026-05-07 | [[GraphRAG]] / [[RAGGraph]] | RAGGraph 可能是项目名、工作流图，也可能被误当作 GraphRAG 同义词 | [[03 前沿追踪]], [[RAGGraph]] | watching |

## 本次维护记录

- 2026-05-07：建立 page catalog、query 写回队列、健康检查页、证据锚点规范、freshness 字段。
