# AGENTS.md

This repository is an Obsidian vault for learning Agents from zero. Treat it as a persistent LLM-maintained wiki, not as a pile of notes.

## Top Hard Rule: Systemic Change Propagation

When a change is **systemic** rather than a simple one-page/source/card edit, the agent must propagate the new constraint to the vault's durable control surfaces before claiming completion.

A systemic change includes any full-batch, incremental-batch, multi-lane, script-driven, schema/template, alias-map, backlink/navigation, raw-ingest policy, concept-card standard, or validation-rule change. Examples: adding bilingual concept-linking across interview pages, changing concept frontmatter, introducing new `up` / `relations` semantics, changing raw-source annotation rules, or adding an audit script.

Hard requirements:

1. Identify whether the work is **simple content work** or **systemic change**.
2. If systemic, update every affected durable control surface, as applicable:
   - project rule: `AGENTS.md`
   - workflow rule: `agentic learning/maps/LLM Wiki 工作流.md`
   - field/schema rule: `agentic learning/maps/字段规范.md`
   - template: `agentic learning/templates/`
   - automation: `scripts/` and alias/config files
   - navigation/backlog: relevant `maps/`, indexes, or `05 Query 写回队列`
   - operation record: `agentic learning/log.md`
3. If future concept cards, raw notes, or topic pages must follow the new behavior, write that behavior as a durable rule, not only as a one-time implementation detail.
4. If a systemic change reveals missing concepts or uncertain Chinese/English canonical names, add them to the appropriate backlog instead of silently treating the current implementation as complete.
5. Final reports for systemic changes must state which control surfaces were updated, which validations were run, and which surfaces were intentionally not changed.

Boundary: a single concept card, one raw source note, or a small typo/link fix does not require rewriting standards. It must still follow the existing standards. But once a change modifies how future cards/sources/maps/scripts should behave, the standards must move with it.

## Top Hard Rule: Bilingual Terminology Audit

When adding or updating concepts, raw-source links, interview-question links, alias maps, or terminology-heavy topic pages, run a **Chinese/English terminology gate** before writing durable links or concept cards.

Hard requirements:

1. Search both the Chinese term and likely English names across `wiki/concepts/`, `wiki/topics/`, `raw/`, `maps/`, `scripts/interview_question_concept_aliases.json`, and `maps/08 面试题概念卡待补充.md`.
2. Choose one canonical concept name before linking. For Agent / RAG / LLM / tooling / evaluation technical concepts, prefer the stable English term when it is the established paper/docs/community name; store Chinese names as aliases or link display text.
3. Classify each bilingual pair as exactly one of:
   - existing concept card / add alias only
   - new concept card with evidence
   - merge into an existing broader card
   - backlog candidate because the English canonical name or boundary is uncertain
   - forbidden mapping / false friend
4. Do not map a Chinese term to the nearest English card just because it is related. Overlap is not equivalence; a broader, narrower, or adjacent concept must stay out of `aliases`.
5. If the term is not stable enough for a card, write it to `[[08 面试题概念卡待补充]]` or `[[05 Query 写回队列]]`; do not create weak concept cards.
6. When a new canonical concept is accepted, synchronize all affected surfaces: concept card frontmatter `aliases`, `related` / `up` / `relations`, relevant raw-question `related` and `## 相关知识 wiki`, `scripts/interview_question_concept_aliases.json` when interview auto-linking should know it, maps/indexes when navigation changes, and `log.md`.
7. Validate with the relevant audit path, at minimum `git diff --check`; for interview links also run `python3 scripts/interview_question_concept_links.py --self-test` and a dry-run.

Boundary: this gate is mandatory for terminology alignment. It does not mean every bilingual term deserves a card; it means every durable mapping must have an explicit boundary decision.
Rule shape: keep this rule at the method level. Do not turn project rules into a fixed vocabulary list; concrete term pairs, edge cases, and representative false-friend examples belong in concept cards, audit reports, backlog pages, or topic pages.

## Top Hard Rule: New Concept Mention Backlink Sweep

When a new concept card is created, or when an existing card receives a new canonical name / major alias / materially broader boundary, the agent must run a project-wide mention sweep before claiming completion.

Hard requirements:

1. Search the vault for the concept's canonical title, Chinese aliases, English variants, abbreviations, and high-confidence phrase forms across `agentic learning/wiki/`, `agentic learning/wiki/topics/` when present, `agentic learning/raw/`, `agentic learning/maps/`, `agentic learning/reviews/`, and relevant automation such as `scripts/interview_question_concept_aliases.json`.
2. Classify each hit before editing:
   - same concept and educationally useful: add an Obsidian link, usually first meaningful mention or local `## 相关知识 wiki`; use display aliases like `[[Canonical Concept|中文术语]]` when preserving Chinese prose.
   - raw-source evidence: do not rewrite quoted/source text; add or update `related`, `## 相关知识 wiki`, synthesis notes, or evidence anchors around the source.
   - ambiguous, broader/narrower, or false friend: do not link; record the boundary in the concept card, backlog, or audit note when it may recur.
   - already linked or noisy repeated mention: leave as-is to avoid link spam.
3. Update both directions where appropriate: the new concept card's `source` / `evidence` / `related`, the mentioning page's `related` or local wiki-link section, and maps/indexes when the concept changes navigation.
4. If the sweep finds many uncertain or weak hits, do not create weak cards or force links; put candidates into `[[08 面试题概念卡待补充]]`, `[[05 Query 写回队列]]`, or `[[06 Wiki 健康检查]]` with the unresolved boundary.
5. Validate with the smallest reproducible check: at minimum a search summary plus `git diff --check`; for interview-question links also run `python3 scripts/interview_question_concept_links.py --self-test` and a dry-run when the script/alias map is touched.

Boundary: this rule requires a backlink/mention sweep, not indiscriminate auto-linking. Links are learning/navigation commitments; ambiguous mentions are better recorded as backlog than silently linked to the wrong concept.

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
- `agentic learning/maps/08 面试题概念卡待补充.md`
- `agentic learning/maps/08 面试题概念链接待办.md`
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

## Retrieval Tooling

When answering questions against this vault or maintaining wiki pages, prefer the Obsidian hybrid search MCP tools before broad filesystem search:

1. Use `obsidian_status` when tool availability, index freshness, or ignore rules matter.
2. Use `obsidian_search` for concept/topic discovery, related-note lookup, fuzzy title lookup, and semantic recall across the vault.
3. Use `obsidian_read` to read exact notes before synthesizing, editing, or citing them.
4. For synthesis, concept comparison, wiki edits, or evidence claims, if `obsidian_read` output is truncated, re-read the core note individually with a larger `snippet_length` or without truncation before making claims.
5. Start from wiki/maps for synthesis and use raw notes as evidence; do not let semantic retrieval flatten the raw/wiki/map layer boundary.
6. Fall back to `rg` and direct file reads when MCP is unavailable, stale, or when an exact path/symbol search is already the narrower check.

Do not store runtime details such as proxy settings, model cache paths, local MCP install commands, or local Codex config in this file. Keep `.omx/**`, `.codex/**`, `.obsidian/**`, templates, and canvas files out of the search index.

## Main Operations

### Ingest

Use when the user adds a source or asks to process a raw note.

1. Read the source note from `raw/`.
2. Preserve the source note as evidence; do not overwrite it with synthesis.
3. Extract key claims, concepts, questions, and boundaries.
4. Create or update concept cards in `wiki/concepts/`.
5. Add `source` and evidence anchors. Prefer `[[Source#Section]]`; use page/section notes when available.
6. For every new canonical concept or major alias, run the New Concept Mention Backlink Sweep: search existing pages, add correct `[[Concept]]` references, and record ambiguous/non-link hits as backlog.
7. Update relevant topic pages in `wiki/topics/`.
8. Update existing maps or indexes only when durable navigation changes.
9. Add unanswered questions to `maps/02 问题池.md`.
10. Append durable query answers to `maps/05 Query 写回队列.md` or write them directly into wiki pages.
11. Append an entry to `agentic learning/log.md`.

Request-meta boundary:

- Treat user-side intake-decision phrasing, recording requests, project names, local task names, and incidental side comments as operation context, not as knowledge content.
- Do not write intake-decision wording into durable concept cards, topic pages, or source-note synthesis. Convert it into neutral knowledge language such as "学习价值", "应沉淀为某类边界", "证据支持的概念", or omit it.
- Hard rule: any paragraph whose main job is to say who supplied it, which batch it came from, where to index it, or which frontier judgment to follow must be deleted from source-note/topic/concept正文 instead of rewritten in place; keep only neutral evidence, learning value, or write-back metadata.
- If the user's side context matters only for the current request, keep it in the reply or log at most; do not promote it into `wiki/` unless it is itself the subject being documented.
- For weekly or systemic maintenance, run `python3 scripts/request_meta_audit.py --format markdown` to catch leaked chat wrappers, hook text, or request-routing wording in durable vault pages.

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

For weekly or systemic maintenance, run the reproducible audit bundle before updating status pages:

```bash
python3 scripts/concept_card_audit.py --format markdown
python3 scripts/comparison_topic_audit.py --format markdown
python3 scripts/paper_source_audit.py
python3 scripts/interview_question_concept_links.py --self-test
python3 scripts/interview_question_concept_links.py --dry-run
python3 scripts/concept_taxonomy/validate.py
python3 scripts/concept_taxonomy/validate_taxonomy_baseline_map.py
python3 scripts/request_meta_audit.py --format markdown
git diff --check
```

Write the current counts, passes, and remaining action queues back to `agentic learning/maps/06 Wiki 健康检查.md`. Treat older counts in that page as historical snapshots once a newer audit run is recorded.

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
