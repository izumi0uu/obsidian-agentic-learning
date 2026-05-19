# Concept Hierarchy Placement Limited apply — Limited Apply Report

Generated: `2026-05-17T05:31:24Z`

> Limited apply applies only reviewed Writeback dry-run ready rows. It writes child-card `up` only and then requires a rebuilt post-apply review.

## Summary

- input_dry_run_planned: 1
- input_dry_run_ready: 1
- selected: 1
- unselected_due_to_limit: 0
- applied: 1
- already_present: 0
- skipped: 0
- concept_card_writes: 1
- limit: 1
- post_apply_dry_run_planned: 0
- post_apply_dry_run_ready: 0

## Policy

- limited_apply_only: True
- limit: 1
- allowed_input: Only writeback dry-run rows with status=ready and candidate-adjudication accept_taxonomy/add_up may be applied.
- field_policy: Write only child-card top-level `up`; do not write `down`, `children`, Juggl fields, or Breadcrumbs mirror fields.
- post_apply_policy: Rebuild the relation map and regenerate the concept hierarchy review after apply; post-apply dry-run may be 0 planned when all accepted rows landed.

## Applied rows

| Source | Target parent | Result | Current up after apply |
|---|---|---|---|
| [[Memory Reflection]] | [[Memory]] | applied | [[Memory]] |

## Selected rows

| Source | Target parent | Strict taxonomy test |
|---|---|---|
| [[Memory Reflection]] | [[Memory]] | passes: Memory Reflection is a memory-maintenance mechanism that saves, filters, updates, and governs long-term memory. |

## Excluded from input dry-run

| Source | Candidate parent | Decision |
|---|---|---|
| [[Approval Gate]] | [[Agent Workflow]] | reject_taxonomy |
| [[ReAct]] | [[Agent Workflow]] | reject_taxonomy |

## Post-apply review

- review_artifact_json: reports/concept-card-relation-map/concept-hierarchy-placement-review.json
- review_artifact_md: reports/concept-card-relation-map/concept-hierarchy-placement-review.md
- classification_stage: limited_apply
- concepts_with_up: 37
- concepts_without_up: 108
- post_apply_dry_run_planned: 0
- post_apply_dry_run_ready: 0

