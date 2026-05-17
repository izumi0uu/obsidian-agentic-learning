# Concept taxonomy tooling

这个目录是项目级概念关系审计工具。它让后续新增概念卡、重跑层级审计、验证 `up` / `relations` 边界时，都以本仓库路径为长期事实来源。

## 目录边界

- `scripts/concept_taxonomy/`：可复跑程序和边界策略。
- `reports/concept-card-relation-map/`：项目内机器可读审计基线和最近一次报告。
- `agentic learning/maps/09 概念层级审计基线.md`：人类 / agent 可读的 vault 镜像。

## 默认路径

脚本默认从仓库根目录读取：

- vault：`agentic learning/`
- concepts：`agentic learning/wiki/concepts/`
- reports：`reports/concept-card-relation-map/`

可用环境变量覆盖：

```bash
CONCEPT_TAXONOMY_OUT_DIR=reports/concept-card-relation-map python3 scripts/concept_taxonomy/validate.py
CONCEPT_TAXONOMY_CONCEPT_DIR='agentic learning/wiki/concepts' python3 scripts/concept_taxonomy/build.py
```

第一条命令展示如何指定报告目录；默认不需要设置。

## 推荐只读验证

```bash
python3 scripts/concept_taxonomy/validate_taxonomy_baseline_map.py
python3 scripts/concept_taxonomy/validate.py
python3 scripts/concept_taxonomy/plugin_contract_verification.py
python3 scripts/concept_taxonomy/control_surface_sync.py
```

这些命令不写概念卡。它们会更新 `reports/concept-card-relation-map/` 下的验证报告，但不新增概念卡关系。验证报告包括插件契约与控制面同步；`plugin_contract_verification.py` 必须保持 0 problems，证明 post-apply dry-run、历史写回边和 forbidden field 守卫仍然成立。

## 新增概念卡后的保守流水线

```bash
python3 scripts/concept_taxonomy/build.py
python3 scripts/concept_taxonomy/decide.py
python3 scripts/concept_taxonomy/writeback.py --dry-run
python3 scripts/concept_taxonomy/taxonomy_placement_review.py --close-audit --check
python3 scripts/concept_taxonomy/validate.py
python3 scripts/concept_taxonomy/validate_taxonomy_baseline_map.py
git diff --check
```

边界：

1. `build.py` 生成临时关系雷达，不等于 taxonomy 判定。
2. `decide.py` 生成候选边判定台账；只有 `writeback_action=add_up` 可进入 dry-run。
3. `writeback.py --dry-run` 不改概念卡。
4. 真实写回必须显式小批量执行：`writeback.py --apply --limit N` 或 `taxonomy_placement_review.py --apply-reviewed --limit N`。
5. 禁止无界 apply；禁止把 `related`、正文 wikilink、topic family、component-of、support-of 直接升格成 `up`。
6. `concepts_without_up` 可以大于 0；没有安全父类的卡要保持 terminal reason 或 deferred-with-backlog。

## 关键文件

- `paths.py`：项目根、concept 目录、report 目录解析；支持 `CONCEPT_TAXONOMY_OUT_DIR` 指定报告目录。
- `boundary_policy.py`：非 taxonomy 边界守卫，防止高混淆 pair 被写成 `up`。
- `build.py`：生成全库临时关系图。
- `decide.py`：把候选边转成 reviewed decision ledger。
- `writeback.py`：关系写回 dry-run / 小批量 apply。
- `taxonomy_placement_review.py`：逐卡 concept hierarchy placement 审计。
- `validate.py`：总体验证与插件兼容检查。
- `plugin_contract_verification.py`：验证 Abstract Folder / Breadcrumbs 的 durable contract、历史写回边和 forbidden field 守卫。
- `control_surface_sync.py`：验证脚本 README、报告 README、工作流、健康检查、基线页和日志仍同步。
- `validate_taxonomy_baseline_map.py`：验证 vault map `09 概念层级审计基线` 与机器基线一致。

## 不做什么

- 不读取或修改 live `.obsidian/` 插件配置。
- 不为 Juggl 生成字段；Juggl 已退役。
- 不手写 `down` / 常规 `children`。
- 不把临时报告目录当长期唯一事实来源。
