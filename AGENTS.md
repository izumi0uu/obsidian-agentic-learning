# AGENTS.md

This repository is an Obsidian vault for learning Agents from zero. Treat it as a persistent LLM-maintained wiki, not as a pile of notes.

## Core Principle

The vault has three knowledge layers:

- `agentic learning/raw/`: immutable source notes. These answer "where did this come from?"
- `agentic learning/wiki/`: structured understanding. These answer "how do I understand this?"
- `agentic learning/maps/` and `agentic learning/index.md`: navigation, reading plans, indexes, and workflow documents.

Do not mix raw source excerpts and durable understanding in the same page. A source note may produce several concept cards, but the source note itself remains evidence.

## Important Files

Always check these before doing wiki maintenance:

- `agentic learning/index.md`
- `agentic learning/maps/LLM Wiki 工作流.md`
- `agentic learning/maps/字段规范.md`
- `agentic learning/raw/资料收集索引.md`
- `agentic learning/maps/Agent 知识地图.md`
- `agentic learning/maps/04 页面目录.md`
- `agentic learning/maps/05 Query 写回队列.md`
- `agentic learning/maps/06 Wiki 健康检查.md`
- `agentic learning/log.md`

## Main Operations

### Ingest

Use when the user adds a source or asks to process a raw note.

1. Read the source note from `raw/`.
2. Preserve the source note as evidence; do not overwrite it with synthesis.
3. Extract key claims, concepts, questions, and boundaries.
4. Create or update concept cards in `wiki/concepts/`.
5. Add `source` and evidence anchors. Prefer `[[Source#Section]]`; use page/section notes when available.
6. Update relevant topic pages in `wiki/topics/`.
7. Update maps or indexes when navigation changes.
8. Add unanswered questions to `maps/02 问题池.md`.
9. Append durable query answers to `maps/05 Query 写回队列.md` or write them directly into wiki pages.
10. Append an entry to `agentic learning/log.md`.

### Query

Use when the user asks a question against the wiki.

1. Start from `agentic learning/index.md`.
2. Read relevant maps and concept cards.
3. Use raw notes only as supporting evidence, not as the first source of synthesis.
4. Answer with links to the relevant Obsidian pages.
5. If the answer is durable, file it back into `wiki/concepts/`, `wiki/topics/`, or `maps/05 Query 写回队列.md`.

### Lint

Use when the user asks to check health, clean up, or maintain the wiki.

Look for:

- orphan concept pages
- missing backlinks
- duplicate concepts
- concepts mentioned but not yet created
- stale claims
- raw sources that have not produced concept cards
- concept cards without "it is not" boundaries
- concept cards without evidence anchors
- stale `freshness: watch/volatile/stale` sources
- unresolved items in `maps/05 Query 写回队列.md`
- pages missing required frontmatter

Prefer small, explicit fixes over broad rewrites.

## Frontmatter

Use the conventions in `agentic learning/maps/字段规范.md`.

Common shape:

```yaml
---
type:
topic:
status:
created:
updated:
source:
related:
---
```

Status values:

- `inbox`
- `seed`
- `growing`
- `mature`
- `review`
- `active`

## Human Learning Rule

The LLM may write and maintain the wiki, but a concept is not considered learned until the user can explain it in their own words.

When updating concept cards, preserve this structure where possible:

- 一句话
- 它解决什么问题
- 它不是什么
- 最小例子
- 常见误解 or 风险
- 相关链接

## Editing Rules

- Keep Markdown readable in Obsidian.
- Prefer Chinese prose for user-facing notes; keep directory names and metadata stable.
- Use Obsidian links like `[[Agent]]`.
- Do not delete raw sources unless the user explicitly asks.
- Do not create many files for weak concepts. Put weak or unclear material in `maps/02 问题池.md` first.
- Append to `log.md`; do not rewrite historical log entries except to fix broken formatting.
