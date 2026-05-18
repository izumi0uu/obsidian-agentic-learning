# Concept card relation map reports

这个目录保存项目内机器可读的概念关系审计基线，作为后续维护的长期事实来源。

## 角色分工

- `scripts/concept_taxonomy/`：生成、判定、写回 dry-run、验证这些报告的程序。
- `reports/concept-card-relation-map/`：机器可读 JSON / Markdown 报告和最近一次审计基线。
- `agentic learning/maps/09 概念层级审计基线.md`：人类可读镜像。
- 备用报告目录：可通过 `CONCEPT_TAXONOMY_OUT_DIR` 指定，只用于一次性复核；不是长期唯一事实来源。

## Baseline 文件

最重要的证明文件：

- `concept-relations-temp.json`：全库临时关系图。
- `relation-decision-ledger.json`：候选关系逐条判定台账。
- `concept-hierarchy-placement-review.json`：133 张概念卡概念层级归属审计。
- `concept-hierarchy-placement-closure.json`：审计闭环与 deferred-with-backlog 证明。
- `plugin-compat-validation.json`：Abstract Folder / Breadcrumbs / forbidden fields 兼容验证。
- `plugin-contract-verification.json`：重建与插件契约验证。
- `control-surface-sync.json`：控制面同步验证。

## 当前基线语义

- `total_concepts: 133`
- `reviewed_concepts: 133`
- `concepts_with_up: 37`
- `concepts_without_up: 96`
- `open_review: 0`
- `open_writeback: 0`
- `dry_run_planned: 0`
- `deferred_with_backlog: 21`

`concepts_without_up` 不是失败；失败条件是出现未审计、无理由、无 backlog home 的隐藏 open tail。

## 复跑命令

```bash
python3 scripts/concept_taxonomy/validate.py
python3 scripts/concept_taxonomy/validate_taxonomy_baseline_map.py
python3 scripts/concept_taxonomy/plugin_contract_verification.py
python3 scripts/concept_taxonomy/control_surface_sync.py
```

如果要临时对其它报告目录验证，可设置 `CONCEPT_TAXONOMY_OUT_DIR=<report-dir>`。

## 写回边界

本目录的报告不自动授权写回。新增或修改 `up` 仍必须走：候选生成 → LLM/规则判定 → dry-run → 小批量 limited apply → 重建验证 → 更新 `09 概念层级审计基线`。
