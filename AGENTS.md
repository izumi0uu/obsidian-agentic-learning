# AGENTS.md

This repository is an Obsidian vault for learning Agents from zero. Treat it as a persistent LLM-maintained wiki, not as a pile of notes.

## Core Principle

The vault has three knowledge layers:

- `agentic learning/raw/`: immutable source notes. These answer "where did this come from?"
- `agentic learning/wiki/`: structured understanding. These answer "how do I understand this?"
- `agentic learning/maps/` and `agentic learning/index.md`: navigation, reading plans, indexes, and workflow documents.

Learning-process records live separately:

- `agentic learning/reviews/`: concept-triggered review, Feynman answers, and write-back candidates. These answer "can I explain this in my own words?"

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
- `agentic learning/reviews/复习记录索引.md`
- `agentic learning/log.md`

## Tooling Boundary: OMX / Codex

This `AGENTS.md` is the repository's durable human guidance. It should describe the learning vault, workflow, and collaboration rules. It is not an OMX runtime artifact and should not be blindly overwritten by `omx setup`.

Project-scope OMX/Codex artifacts are local tooling state:

- `.codex/`: project-local agents, skills, prompts, config, and hooks.
- `.omx/`: OMX state, metrics, logs, HUD state, plans, interviews, and caches.
- `.git/info/exclude`: the preferred place for local-only ignore rules for `.codex/`, `.omx/`, and any untracked project-local `AGENTS.md`.

Keep `.codex/` and `.omx/` out of Git unless the user explicitly asks to version them. Prefer `.git/info/exclude` over committed `.gitignore` changes for these local artifacts.

Do not modify `~/.codex/AGENTS.md` unless the user explicitly asks. For project isolation while reusing the existing local Codex login, launch OMX with:

```bash
CODEX_HOME="$HOME/.codex" omx --madmax --high
```

After running `omx setup --scope project`, check `git status --short` and `git diff -- AGENTS.md .gitignore`. If `.gitignore` only gained local OMX/Codex ignore rules, restore it and keep those rules in `.git/info/exclude`. If `AGENTS.md` changed, preserve durable project guidance but remove installer/runtime noise.

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

Use `agentic learning/reviews/` for that learning check. A review note is not raw evidence and is not a durable concept card; it is a place to capture the user's explanation, Codex follow-up questions, Feynman answers, and write-back candidates.

When updating concept cards, preserve this structure where possible:

- 一句话
- 它解决什么问题
- 它不是什么
- 最小例子
- 常见误解 or 风险
- 边界细节
- 现代系统怎么吸收这个概念的价值/局限（适用于 Agent、prompting、framework、evaluation 类概念）
- 证据锚点
- 相关链接

Style reference: `wiki/concepts/Plan-and-Solve Prompting.md`. Concept cards should start from the concept's own problem, make neighboring boundaries explicit, include common misunderstandings, and explain whether diagrams or assets are source evidence, user-provided redraws, or engineering analogies.

## Editing Rules

- Keep Markdown readable in Obsidian.
- Prefer Chinese prose for user-facing notes; keep directory names and metadata stable.
- Use Obsidian links like `[[Agent]]`.
- Do not delete raw sources unless the user explicitly asks.
- Do not create many files for weak concepts. Put weak or unclear material in `maps/02 问题池.md` first.
- Append to `log.md`; do not rewrite historical log entries except to fix broken formatting.
