# Plugin Contract Verification

Generated: `2026-05-20T12:34:45Z`

## Summary

- concept_cards_checked: `145`
- top_level_up_edges: `37`
- temp_map_taxonomy_edges: `37`
- relation_writeback_dry_run_planned: `0`
- taxonomy_post_apply_dry_run_planned: `0`
- taxonomy_post_apply_dry_run_ready: `0`
- taxonomy_limited_apply_rows: `1`
- taxonomy_placement_open_review: `0`
- taxonomy_placement_defer_boundary_review: `22`
- taxonomy_placement_deferred_with_backlog: `22`
- taxonomy_placement_open_writeback: `0`
- relation_apply_rows_checked: `13`
- taxonomy_apply_rows_checked: `1`
- plugin_problems: `0`
- forbidden_up_edges: `0`
- forbidden_top_level_fields: `0`
- nested_relation_records_with_mirror-like_types: `23`
- obsidian_plugin_config_present: `False`
- problems: `0`

## Plugin contract

- abstract_folder: Contract-only verification: parent property remains `up`; no physical folder conversion or `children` writeback is required.
- breadcrumbs: Contract-only verification: top-level `up` is the only hierarchy edge field; `down` is implied; nested `relations` is not promoted to edge fields.
- juggl: Retired; no Juggl plugin state, field, or mirror edge is required or validated.
- live_obsidian_config: absent

## Doc checks

- abstract_folder_up_contract: `True`
- breadcrumbs_top_level_up_contract: `True`
- relations_not_breadcrumbs_edge_field: `True`
- juggl_retired_documented: `True`
- plugin_contract_gate_documented: `True`

## Problems

- none

## Boundary

- Plugin contract verification is verification-only; it does not write concept-card fields.
- `concepts_without_up` may remain > 0; this check proves plugin and writeback contracts after bounded apply.
- Taxonomy-placement `open_review` may remain > 0; this check is not the whole-audit closure gate.
- `.obsidian/` is absent in this repo, so live plugin settings are not mutated or asserted beyond durable contract checks.
