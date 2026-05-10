---
type: map
topic:
  - maintenance
  - llm-wiki
  - team
status: active
created: 2026-05-10
updated: 2026-05-10
related:
  - "[[LLM Wiki 工作流]]"
  - "[[06 Wiki 健康检查]]"
  - "[[Agent 知识地图]]"
---

# 07 Team 概念卡全量规范化

这页是给 `$team 7` 使用的执行协议。目标不是把所有卡写成长文，而是让每张 `wiki/concepts/` 按自己的深度等级达到当前概念卡规范。

## 执行前必须读

- `AGENTS.md`
- [[LLM Wiki 工作流]]
- [[字段规范]]
- [[06 Wiki 健康检查]]
- 本页

## 总目标

把 `agentic learning/wiki/concepts/` 中不符合规范的概念卡，按 `seed-lite / qualified / anchor / volatile` 四类修到对应最低质量线。

验收重点：`## 概念详解` 是否成为主体解释，而不是只补标题。

必须覆盖：

- 概念为什么出现。
- 原始问题是什么。
- 机制 / 组件 / 工作流是什么。
- 论文、官方文档、社区实践或 source note 怎样支持它。
- 哪些是 source evidence，哪些是 engineering synthesis。
- 和邻近概念的边界。
- 现代系统如何吸收它的价值或限制它的风险。

## 硬边界

- 不修改 `agentic learning/raw/`。
- 不修改 `AGENTS.md`、[[LLM Wiki 工作流]]、[[字段规范]]、模板页，除非 leader 明确要求。
- 不修改 `agentic learning/log.md` 和 [[06 Wiki 健康检查]]；leader 收尾时统一更新。
- 不批量删除、重命名、移动概念卡。
- 不把 `reviews/` 当 raw evidence。
- 不把无来源工程直觉写成来源事实。
- 不以“section 都存在”作为通过标准。
- 不把所有卡写成同样长度；必须遵守 no-one-size-depth。

## 深度等级

| 等级 | 适用对象 | 详解最低线 | 处理原则 |
|---|---|---:|---|
| seed-lite | 暂存弱概念、Obsidian/工作流辅助概念 | 可短 | 写清缺口，不强行扩成长文 |
| qualified | 稳定概念卡 | 约 700+ 字符 | 有 `## 概念详解`、边界、最小例子、证据锚点、复习触发 |
| anchor | 地基卡、对比卡、样板卡 | 约 900+ 字符 | 详解必须充分，解释动机、机制、来源、现代吸收和邻近边界 |
| volatile | API、SDK、协议、安全、产品生态 | 约 650+ 字符 | 除 qualified 外，还要 `last_checked` / `freshness`，避免把易变 API 写成稳定概念 |

边界：字符数只是防浅卡阈值，不是鼓励灌水。真正验收看是否能帮助用户复述、举例、判断边界。

## 本地审计脚本

脚本位置：`scripts/concept_card_audit.py`

常用命令：

```bash
python3 scripts/concept_card_audit.py --format markdown
python3 scripts/concept_card_audit.py --team-plan --format markdown
python3 scripts/concept_card_audit.py --format json --output .omx/reports/concept-card-audit.json
```

脚本会输出：

- 每张卡的建议深度等级。
- 5 个 writer lane 的文件分配。
- 缺 `## 概念详解`、Evidence type / Boundary、复习触发、现代性状态等问题。

注意：脚本是 lint 辅助，不替代人工判断。Verifier 必须抽查正文质量。

## 7 进程结构

不要 7 个全写。使用：

- 5 个 writer：只改自己 lane 的概念卡。
- Worker 6：evidence auditor，默认只读。
- Worker 7：final verifier / lint，默认只读。

### Worker 1：Agent foundations

范围：Agent 基础、loop、planning、tool use、reasoning/prompting。

主要文件由脚本 lane `writer-1-agent-foundations` 输出。优先处理：

- [[Agent]]
- [[Agent Harness]]
- [[Planning]]
- [[ReAct]]
- [[Tool Calling]]
- [[Plan-and-Solve Prompting]]
- [[Observation]]
- [[Tool Use]]
- [[Zero-shot CoT]]

### Worker 2：Framework / runtime / memory

范围：框架、runtime、state/workflow 之外的执行层、durable execution、memory。

主要文件由脚本 lane `writer-2-framework-runtime` 输出。优先处理：

- [[Memory]]
- [[Durable Execution]]
- [[Handoff]]
- [[Agent Lifecycle Hook]]
- [[Code Execution Sandbox]]
- [[LLM Gateway]]
- [[Long-term Memory]]
- [[Semantic Memory]]

### Worker 3：Evaluation / observability

范围：评估、trace、observability、trajectory、benchmark、replay。

主要文件由脚本 lane `writer-3-evaluation-observability` 输出。优先处理：

- [[Trace]]
- [[Observability]]
- [[Trajectory Evaluation]]
- [[Benchmark]]
- [[Reasoning Trace]]
- [[Patch Validation]]
- [[Task Success Rate]]
- [[Replay]]
- [[OpenTelemetry GenAI]]

### Worker 4：RAG / retrieval

范围：RAG、retrieval、ingestion、embedding、reranking、GraphRAG。

主要文件由脚本 lane `writer-4-rag-retrieval` 输出。优先处理：

- [[RAG]]
- [[Chunking]]
- [[Document Ingestion]]
- [[Embedding]]
- [[Hybrid Search]]
- [[Retriever]]
- [[Reranking]]
- [[Vector Database]]
- [[Agentic RAG]]
- [[GraphRAG]]
- [[Self-RAG]]

### Worker 5：Security / protocol / frontier / ecosystem

范围：安全、协议、tool registry、computer use、OMX、本地生态和 LLM 基础弱卡。

主要文件由脚本 lane `writer-5-security-protocol-frontier` 输出。优先处理：

- [[MCP]]
- [[MCP Registry]]
- [[A2A]]
- [[ACP]]
- [[Guardrails]]
- [[Prompt Injection]]
- [[Tool Permissioning]]
- [[Tool Poisoning]]
- [[Data Exfiltration]]
- [[Approval Gate]]
- [[Computer Use]]
- [[Browser Agent]]

### Worker 6：Evidence auditor

默认只读。检查 writer diffs：

- 新增详解是否真的有 source note 支持。
- `## 证据锚点` 是否包含 Evidence type 与 Boundary。
- 是否把 community/platform docs、paper source、official docs、engineering synthesis 混在一起。
- 是否引用了不存在的小节。
- 是否使用了 raw 以外的学习记录作为证据。

输出：问题清单 + 建议改法。除非 leader 明确要求，不直接改正文。

### Worker 7：Final verifier / lint

默认只读。职责：

- 运行 `python3 scripts/concept_card_audit.py --format markdown`。
- 抽查每个 writer 至少 3 张卡。
- 拒绝只补标题、没有连续解释的卡。
- 拒绝无证据边界的现代性判断。
- 检查 `git diff --check`。
- 检查没有修改 `raw/`。

## 给 `$team 7` 的建议指令

```text
$team 7:executor "按 agentic learning/maps/07 Team 概念卡全量规范化.md 执行概念卡全量规范化。先读 AGENTS.md、LLM Wiki 工作流、字段规范、06 Wiki 健康检查和本页。5 个 writer 只改各自 lane 的 wiki/concepts 文件；worker 6 只做 evidence audit，默认只读；worker 7 只做 final verifier/lint，默认只读。禁止修改 raw/、AGENTS.md、模板和 workflow 标准。目标不是把所有卡写成长文，而是按 seed-lite/qualified/anchor/volatile 达到对应规范。验收重点是 ## 概念详解 是否为主体解释，是否有动机、机制、证据、边界、现代系统吸收和复习触发；不要只检查 section 是否存在。"
```

## Leader 收尾清单

- [ ] 收集 5 个 writer 的改动范围。
- [ ] 读 worker 6 evidence audit。
- [ ] 读 worker 7 final verifier。
- [ ] 运行：`python3 scripts/concept_card_audit.py --format markdown`。
- [ ] 运行：`git diff --check`。
- [ ] 运行：`git diff --cached --check`。
- [ ] 运行：`git -c core.quotePath=false diff --name-only | grep '^agentic learning/raw/'`，确认没有 raw 修改。
- [ ] 更新 [[06 Wiki 健康检查]]。
- [ ] 追加 [[log]]。

## 小边界

如果 worker 发现某张卡缺少足够证据，不要硬写。应该：

1. 标为 seed-lite 或 review。
2. 在 [[06 Wiki 健康检查]] 或 [[02 问题池]] 留缺口。
3. 等 source note 补足后再深修。
