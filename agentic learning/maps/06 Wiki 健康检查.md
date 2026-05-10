---
type: map
topic:
  - maintenance
  - llm-wiki
status: active
created: 2026-05-07
updated: 2026-05-10
related:
  - "[[LLM Wiki 工作流]]"
  - "[[04 页面目录]]"
  - "[[05 Query 写回队列]]"
  - "[[字段规范]]"
---

# 06 Wiki 健康检查

这页记录周期性 lint、freshness 和 contradiction check 的结果。

## 当前状态

- Last lint: 2026-05-10
- Missing links: none
- Concept cards: 90
- Raw source notes: 810（包含按题拆分的 imported question source pages；主源清单仍看 [[资料收集索引]]）
- Query write-back pending: 0
- Concept cards missing `## 边界细节`: 57（已用 4 张样例卡修复前为 60）
- Concept cards missing `## 现代性状态`: 79（已用 4 张样例卡修复前为 83）
- Concept cards missing `## 复习触发`: 86（已用 4 张样例卡修复前为 90）

边界：这些数字用于排队和抽样修复，不代表要一次性批量重写旧卡。批量修复旧卡前需要用户确认。

## 每周检查清单

- [ ] 更新 [[04 页面目录]]。
- [ ] 跑 missing-link scan。
- [ ] 检查概念卡是否有“它不是什么”。
- [ ] 检查概念卡是否有 `## 边界细节`。
- [ ] 检查 Agent / prompting / framework / evaluation / RAG / memory / tooling / safety / protocol / product-ecosystem 概念卡是否有 `## 现代性状态`。
- [ ] 检查概念卡是否有 `## 复习触发`。
- [ ] 抽查概念卡是否只是“一句话 + 链接”，没有问题背景、最小例子、误解、边界或证据。
- [ ] 检查概念卡是否有“证据锚点”。
- [ ] 检查 raw source 是否有 `last_checked` 和 `freshness`。
- [ ] 处理 [[05 Query 写回队列]]。
- [ ] 把发现的问题追加到本页。

## 2026-05-10 概念卡标准化 lint

本次 lint 的目标不是全量改写，而是把概念卡标准升级为“双层学习 + 判断卡”，并建立后续修复队列。

### 抽样结果

| 检查项 | 数量 | 解释 | 处理策略 |
|---|---:|---|---|
| 概念卡总数 | 90 | `wiki/concepts/*.md` | 只抽样修复 4 张风格锚点 |
| 缺 `## 边界细节` | 57 | 很多旧卡有定义但缺少邻近概念切分；本次修复前为 60 | 排入队列，按主题逐批修 |
| 缺 `## 现代性状态` | 79 | 旧卡多未主动判断 foundation / transitional / current-practice / frontier；本次修复前为 83 | 只对本次修改和高价值卡先补 |
| 缺 `## 复习触发` | 86 | 旧模板没有把概念卡连接到 review 流程；本次修复前为 90 | 后续每次修卡都补 1-3 个问题 |

### 第一批修复队列

| 优先级 | 候选卡 | 主要缺口 | 处理方式 |
|---|---|---|---|
| P0 | [[Agent]] | 基础概念，但缺 `边界细节`、`现代性状态`、`复习触发` | 本次作为 anchor 样例修复 |
| P0 | [[Trace]] | 已较完整，但缺现代性和复习触发；需切开 [[Trajectory]] / [[Reasoning Trace]] / eval | 本次作为 observability 样例修复 |
| P0 | [[Trajectory Evaluation]] | evaluation 判断卡代表；需拆开 trace、trajectory、score、judge 的边界 | 本次作为 eval 样例修复 |
| P0 | [[RAG]] | 非 Agent 但核心知识概念；需补现代系统吸收和复习触发 | 本次作为 RAG 样例修复 |
| P1 | [[Agent Loop]], [[Agent Framework]], [[Agent State]], [[Agent Workflow]] | Agent 工程骨架，现代性状态和复习触发不齐 | 下次按 Agent 工程主题成组修 |
| P1 | [[Evaluation]], [[Eval Harness]], [[LLM-as-Judge]], [[RAG Evaluation]] | 评估概念相互依赖，需统一 “记录 vs 判断 vs harness” 边界 | 下次按 evaluation 主题成组修 |
| P2 | [[A2A]], [[ACP]], [[MCP]], [[MCP Registry]] | 协议/生态变化较快，需要 freshness 与前沿追踪联动 | 需要查新后再修 |

### 不做的事

- 不批量重写 90 张旧概念卡。
- 不把每张卡扩成百科长文。
- 不把没有证据的工程直觉写成来源结论。
- 不把 `reviews/` 当作 raw evidence；复习记录只用于学习校准和写回候选。

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
