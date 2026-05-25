# Taxonomy Tooling Control-Surface Sync

Generated: `2026-05-25T02:56:13Z`

## Summary

- required_surfaces_total: `8`
- required_surfaces_synced: `8`
- taxonomy_open_review_remaining: `0`
- taxonomy_defer_boundary_review_remaining: `30`
- taxonomy_open_writeback: `0`
- plugin_contract_problems: `0`
- plugin_problems: `0`
- forbidden_up_edges: `0`
- concept_card_writebacks_this_check: `0`
- problems: `0`

## Required surfaces

- project_rules: `True` — `AGENTS.md`
- script_readme: `True` — `scripts/concept_taxonomy/README.md`
- report_readme: `True` — `reports/concept-card-relation-map/README.md`
- script_index: `True` — `scripts/README.md`
- workflow: `True` — `agentic learning/maps/LLM Wiki 工作流.md`
- health_check: `True` — `agentic learning/maps/06 Wiki 健康检查.md`
- baseline_map: `True` — `agentic learning/maps/09 概念层级审计基线.md`
- log: `True` — `agentic learning/log.md`

## Intentionally not changed

- `agentic learning/maps/字段规范.md`: Tooling and baseline evidence moved into project-owned paths; no `up` / `relations` field semantics changed.
- `agentic learning/templates/概念卡.md`: No concept-card page shape or `up` / `relations` writeback contract changed.

## Boundary

- Project tooling verification checks project-owned control surfaces after the audit baseline is closed; it does not adjudicate or write new concept-card relationships.
- Remaining defer_boundary_review rows are closed only when review_status=deferred_with_backlog and a backlog home is recorded.
- Field spec and concept-card template stay unchanged because the tooling migration moved tooling/evidence locations without changing `up` / `relations` field semantics or concept-card page shape.

## Problems

- none
