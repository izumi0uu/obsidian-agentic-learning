# AGENTS.md

This repository is an Obsidian vault for learning Agents from zero. Treat it as a persistent LLM-maintained wiki, not as a pile of notes.

## Core Principle

The vault has three knowledge layers:

- `agentic learning/raw/`: immutable source notes. These answer "where did this come from?"
- `agentic learning/wiki/`: structured understanding. These answer "how do I understand this?"
- `agentic learning/maps/` and `agentic learning/index.md`: durable navigation, durable indexes, workflow documents, and explicitly requested learning routes. Maps are scarce control surfaces, not a place to record every ingest batch.

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
7. Update existing maps or indexes only when durable navigation changes.
8. Add unanswered questions to `maps/02 问题池.md`.
9. Append durable query answers to `maps/05 Query 写回队列.md` or write them directly into wiki pages.
10. Append an entry to `agentic learning/log.md`.

Map boundary:

- Do not create new map files just because a source batch, paper batch, repo batch, or "recent / speed-read" collection was ingested.
- Do not add "近期论文速读入口", "速读清单", or similar batch-specific links to main topic pages unless the user explicitly asks for a durable reading route.
- Prefer updating existing stable maps: `资料收集索引`, `Agent 知识地图`, `04 页面目录`, `03 前沿追踪`, `05 Query 写回队列`, or the relevant topic page.
- A new map is allowed only when it is durable navigation that will still be useful after the current ingest batch, such as a stable topic map, workflow rule, health-check page, or explicitly requested reading plan.
- Temporary paper/source triage belongs in the source index, a raw source note, the question pool, or query write-back queue, not in a new standalone map.

Paper reading priority:

- When maintaining paper sources, rank papers by learning leverage, not recency: P0 = unlocks core concepts or prevents common misunderstandings; P1 = directly strengthens current Agent engineering judgment; P2 = topic-specific expansion; P3 = background/model-training context to read on demand.
- Record durable priority rules in `资料收集索引` or `LLM Wiki 工作流`; do not create one-off paper priority maps.
- Before creating stable concept cards from frontier paper titles, check whether the paper is P0/P1 and whether it has enough evidence beyond abstract-level intake.

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

Concept cards are **双层学习 + 判断卡**:

- 学习层：帮助用户从“听过这个词”走到能解释、能举例、能发现误解。
- 判断层：帮助用户判断边界、适用条件、现代工程吸收方式、证据强弱和下一步复习问题。

The learning layer must be explicit enough for the user to explain the concept, not merely recognize the label. For `qualified` and `anchor` cards, `## 概念详解` is the main body and should normally carry the highest explanatory weight. `## 一句话` remains only a quick entry point.

When creating or materially updating concept cards, preserve this structure where possible:

- 一句话
- 概念详解：主体段落；解释概念为什么出现、内部机制/组成部分、论文/官方文档/社区实践如何描述它、以及现代系统如何吸收或限制它
- 它解决什么问题
- 它不是什么
- 最小例子
- 常见误解 or 风险
- 边界细节
- 现代性状态：主动判断 foundation / transitional / current-practice / frontier / 不适用
- 现代系统怎么吸收这个概念的价值/局限（适用于 Agent、prompting、framework、evaluation 类概念）
- 证据锚点
- 复习触发
- 相关链接

`## 一句话` is only an entry point. It must not become the whole card when the concept needs background, examples, boundary cuts, or evidence. A qualified durable concept card should not be a label plus one sentence plus bullets; it needs a real explanation section. If it is intentionally short, state why the concept is low-scope or still `seed`.

Style reference: `wiki/concepts/Plan-and-Solve Prompting.md`, with one upgrade: modern concept cards should include `## 概念详解` when the concept is important enough to learn deeply. Concept cards should start from the concept's own problem, make neighboring boundaries explicit, include common misunderstandings, and explain whether diagrams or assets are source evidence, user-provided redraws, community summary, or engineering analogy.

When creating or updating a concept card, the LLM should proactively run the modernity/frontier classification from `maps/LLM Wiki 工作流.md`: decide whether the concept is foundation, historical transition, current engineering practice, frontier/volatile, or not applicable. Do not wait for the user to ask “is this modern/frontier?”. If the concept touches Agent, prompting, framework, evaluation, RAG, memory, tooling, safety, protocols, or product ecosystems, write the classification into `## 现代性状态` or the nearest modern-system section.

Do not batch rewrite old concept cards without explicit user confirmation. First update the standard/template, repair a few style anchors, and put broader gaps into `agentic learning/maps/06 Wiki 健康检查.md` or `agentic learning/maps/05 Query 写回队列.md`.

## Editing Rules

- Keep Markdown readable in Obsidian.
- Prefer Chinese prose for user-facing notes; keep directory names and metadata stable.
- Use Obsidian links like `[[Agent]]`.
- Do not delete raw sources unless the user explicitly asks.
- Do not create many files for weak concepts. Put weak or unclear material in `maps/02 问题池.md` first.
- Append to `log.md`; do not rewrite historical log entries except to fix broken formatting.
