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
- 写入 `agentic learning/raw/articles/xiaolinnote/`
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
python3 scripts/concept_card_audit.py --format json --output .omx/reports/concept-card-audit.json
```

脚本行为：

- 只读检查 `agentic learning/wiki/concepts/*.md`。
- 按 `seed-lite / qualified / anchor / volatile` 给出建议深度等级。
- 检查 `## 概念详解`、`## 证据锚点` 中的 Evidence type / Boundary、`## 现代性状态`、`## 复习触发` 等缺口。
- 输出 5 个 writer lane + evidence auditor + final verifier 的 `$team 7` 分工依据。

注意：脚本只做结构和浅层质量审计；最终仍要人工/leader 判断概念详解是否真的讲透。
