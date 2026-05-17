# 小林 Note 更新功能

这个目录放项目级可调用脚本。

## 更新小林 Note raw source

```bash
cd /Users/idah/Projects-combined/obsidian-agentic-learning
python scripts/update_xiaolinnote.py --dry-run
python scripts/update_xiaolinnote.py
```

可选：只检查 AI 面试题部分：

```bash
python scripts/update_xiaolinnote.py --scope ai
```

脚本行为：

- 读取 `https://xiaolinnote.com/sitemap.xml`
- 抓取匹配页面正文和链接
- 用 raw note frontmatter 里的 `sha256` 判断是否新增/变化
- 写入 `agentic learning/raw/repos/xiaolinnote/questions/`
- 按 URL 复用现有题页文件名；新页面追加新编号，避免重复导入
- 保留既有 `## 相关知识 wiki` 和 frontmatter `related`，避免刷新 raw source 时冲掉概念回链
- 刷新集合索引 `小林 Note 面试题索引.md`
- 刷新 `资料收集索引.md`、`04 页面目录.md`、`index.md`
- 如果有新增、变化或错误，追加 `log.md`

返回 JSON 字段：

- `new`: 新增页面数
- `changed`: 内容变化页面数
- `unchanged`: 未变化页面数
- `errors`: 抓取失败页面数
- `new_files`: 最多前 20 个新增文件
- `changed_files`: 最多前 20 个变化文件

注意：这个脚本只更新 raw evidence，不自动改 `wiki/concepts/`。如果页面变化重要，再单独做概念卡消化。

## 概念卡审计 / Team 分工

```bash
cd /Users/idah/Projects-combined/obsidian-agentic-learning
python3 scripts/concept_card_audit.py --format markdown
python3 scripts/concept_card_audit.py --team-plan --format markdown
python3 scripts/concept_card_audit.py --format json --output reports/concept-card-audit.json
```

脚本行为：

- 只读检查 `agentic learning/wiki/concepts/*.md`。
- 按 `seed-lite / qualified / anchor / volatile` 给出建议深度等级。
- 检查 `## 概念详解`、`## 证据锚点` 中的 Evidence type / Boundary、`## 现代性状态`、`## 复习触发` 等缺口。
- 输出 5 个 writer lane + evidence auditor + final verifier 的 `$team 7` 分工依据。

注意：脚本只做结构和浅层质量审计；最终仍要人工/leader 判断概念详解是否真的讲透。

## 对比 topic 审计

```bash
cd /Users/idah/Projects-combined/obsidian-agentic-learning
python3 scripts/comparison_topic_audit.py --format markdown
python3 scripts/comparison_topic_audit.py --team-plan --format markdown
python3 scripts/comparison_topic_audit.py --format json --output reports/comparison-topic-audit.json
```

脚本行为：

- 只读检查 `agentic learning/wiki/topics/*.md` 中的概念对比页。
- 检查 [[概念对比页]] 模板要求的关键 section、核心区别表、证据锚点、复习触发和链接密度。
- 输出 comparison lane 分工，方便后续小批量修复。

注意：Needs action 代表结构 / 证据边界需要排队修，不代表应一次性批量重写所有 topic。

## 论文 source note 审计

```bash
cd /Users/idah/Projects-combined/obsidian-agentic-learning
python3 scripts/paper_source_audit.py
```

脚本行为：

- 只读检查 `agentic learning/raw/papers/*.md`。
- 确认每张论文 source note 保留 `type: source`、`source_type: paper`。
- 检查最低核心 section：`为什么收`、`一句话`、`需要我读的内容`、`论文主张`、`可以拆成概念卡`、`我的疑问`、`边界提醒`。
- 检查 `### 必读` 下至少有一个 `#### 必读块`，且包含位置、为什么必读、原文短摘、中文概括、机制、支撑概念、证据边界。
- 检查原文短摘长度，避免把长篇原文搬进 raw note。

注意：脚本只验证结构与短摘长度，不证明论文理解正确；证据真实性仍需要回到 PDF、extracted markdown 或论文页面核对。

## 面试题概念链接审计

```bash
cd /Users/idah/Projects-combined/obsidian-agentic-learning
python3 scripts/interview_question_concept_links.py --self-test
python3 scripts/interview_question_concept_links.py --dry-run
```

脚本行为：

- 检查 `scripts/interview_question_concept_aliases.json` 的 alias / canonical mapping 是否能安全匹配。
- 扫描面试题页的 `## 相关知识 wiki` 区域，避免改写 raw/source 原文。
- dry-run 输出 would modify、missing concept candidates 和 protected region violations。

结果写回：

- 每周维护或系统性链接规则变更后，把 self-test / dry-run 结果写入 `agentic learning/maps/06 Wiki 健康检查.md`。
- 缺失但不稳定的概念候选写入 [[08 面试题概念卡待补充]]。
- 自动链接无把握的题页或 alias 待办保留在 [[08 面试题概念链接待办]]。

## 概念关系 / taxonomy 审计工具

```bash
cd /Users/idah/Projects-combined/obsidian-agentic-learning
python3 scripts/concept_taxonomy/build.py
python3 scripts/concept_taxonomy/decide.py
python3 scripts/concept_taxonomy/writeback.py --dry-run
python3 scripts/concept_taxonomy/validate.py
python3 scripts/concept_taxonomy/plugin_contract_verification.py
python3 scripts/concept_taxonomy/control_surface_sync.py
python3 scripts/concept_taxonomy/validate_taxonomy_baseline_map.py
```

脚本行为：

- 默认读写 `reports/concept-card-relation-map/`。
- 验证报告会记录插件契约、控制面同步和边界守卫；默认验证命令不新增概念卡关系。
- 只把 `up` 当 strict taxonomy；`relations` / `related` / 正文 wikilink 不能直接升格。
- 真正写回必须小批量显式执行 `--apply --limit N` 或 `taxonomy_placement_review.py --apply-reviewed --limit N`。
- 如需验证其它报告目录，可设置 `CONCEPT_TAXONOMY_OUT_DIR=<report-dir>`。

边界：默认验证命令不会新增概念卡关系；`concepts_without_up` 允许大于 0，只要审计台账证明它们是 root/terminal/deferred-with-backlog。

## Weekly maintenance audit bundle

```bash
python3 scripts/concept_card_audit.py --format markdown
python3 scripts/comparison_topic_audit.py --format markdown
python3 scripts/paper_source_audit.py
python3 scripts/interview_question_concept_links.py --self-test
python3 scripts/interview_question_concept_links.py --dry-run
python3 scripts/concept_taxonomy/validate.py
python3 scripts/concept_taxonomy/plugin_contract_verification.py
python3 scripts/concept_taxonomy/control_surface_sync.py
python3 scripts/concept_taxonomy/validate_taxonomy_baseline_map.py
git diff --check
```

边界：这个 bundle 用来更新健康状态和修复队列，不等于自动批量修复。把最新统计写回 [[06 Wiki 健康检查]]，旧统计只作为历史快照。
