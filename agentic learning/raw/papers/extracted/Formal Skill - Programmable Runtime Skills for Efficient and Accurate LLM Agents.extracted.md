# Formal Skill: Programmable Runtime Skills for Efficient and Accurate LLM Agents - Extracted Text

- Source note: [[Formal Skill - Programmable Runtime Skills for Efficient and Accurate LLM Agents]]
- Source PDF: `assets/Formal Skill - Programmable Runtime Skills for Efficient and Accurate LLM Agents.pdf`
- Extracted: 2026-05-20
- Extractor: pypdf
- Pages: 11
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

Formal Skill: Programmable Runtime Skills for
Efficient and Accurate LLM Agents
Xi Zhang Meijun Gao Yuntian Zhao Xinyu Tan Yilun Yao
Feiyu Wang Yanshu Wang Dingsiyi Tong Yang
Abstract
Large Language Model (LLM) agents increasingly act inside real workspaces,
where tools and skills determine whether model reasoning becomes reliable action.
Existing skills remain largely informal: Markdown skills and instruction packs
encode procedures as long natural-language documents, while function calling,
Model Context Protocol (MCP) servers, and framework tools structure individ-
ual actions but usually leave workflow state, policy enforcement, and completion
discipline outside the skill itself. We introduceFormal Skill, a runtime-native
abstraction that represents reusable capability with JSON metadata and action
schemas, reliable Python executors, hook-governed control logic, Formal Skill
routing, and skill-local runtime state. By moving reusable procedure from repeated
prompt text into executable state machines and hook policies, Formal Skill gives
agents a token-efficient and enforceable control surface. We implement the abstrac-
tion in FairyClaw, an open-source event-driven runtime for executable, observable,
and composable Formal Skills. On Harness-Bench, FairyClaw obtains highly
competitive average scores while using substantially fewer tokens, with especially
strong results on tasks that expose the role of Formal Skill.
1 Introduction
Large Language Model (LLM) agents are rapidly becoming a central interface for software engi-
neering, office automation, research assistance, and operational decision making. Systems such as
Claude Code [16], OpenClaw [25], and Hermes [30] illustrate a shift from chat-oriented assistants
toward agents that inspect repositories, run commands, edit files, call external services, and coordinate
multi-step work over time. In these agents, skills and tools are not peripheral conveniences: they are
the agent’s hands and feet. They determine whether a language model can move from describing the
world to acting on it.
Existing systems organize reusable agent capability mainly in two ways. First,text-packaged proce-
dural skillssuch as Claude-style skills and many SKILL.md libraries bundle discovery metadata,
Markdown procedures, auxiliary files, and optional scripts; tools may be invoked inside the procedure,
but the procedure itself is primarily a document read by the model. Second,schema-level tool
interfacessuch as function calling, Model Context Protocol (MCP) tools, framework tools, and
API-oriented tool-use methods describe individual actions with names, schemas, and protocol bound-
aries; they make tool invocation more structured, but usually do not define a skill-level workflow
that owns phase order, recovery, and completion. Agent runtimes, workspaces, sandboxes, and
benchmark harnesses provide the surrounding execution and evaluation environment for both styles,
but they do not by themselves make the reusable procedure formal. ByInformal Skills, we mean
skills whose operational semantics live mainly in natural-language instructions, naming conventions,
prompt discipline, or external orchestration rather than in a runtime-executable object; across existing
approaches, the core limitation is that the skill remains informal in this sense. Informal Skills are
costly because long procedural text must be loaded as tokens; ambiguous because natural language
Preprint.
arXiv:2605.19604v1  [cs.AI]  19 May 2026

## Page 2

remains only semi-structured to the machine; weak because ordering constraints, safety rules, and
completion criteria are soft suggestions; and brittle because recovery state is usually implicit in the
transcript rather than represented as skill-local runtime state.
To address these limitations, we proposeFormal Skillas a runtime-native alternative. A Formal
Skill converts a reusable agent capability from a purely natural-language artifact into a structured
executable object with five components: (1) JSON metadata and action schemas that define the
model-visible interface, (2) reliable executors that implement actions with deterministic validation
and bounded side effects, (3) lifecycle hooks that mediate model calls and tool calls, (4) skill-local
runtime state that records phase, evidence, gates, and recovery context, and (5) routing metadata that
determines when the skill should be exposed to a task or subtask. It is formal because JSON metadata
and schemas describe the skill’s machine-readable surface, while transition points, state variables,
side-effect boundaries, and completion gates are represented as runtime data and executable programs
rather than as prose alone. The goal is not to remove language from agent behavior, but to assign it
the right role: the model reasons and chooses among structured actions, while the runtime owns the
procedural invariants. Token-heavy manuals become compact state-conditioned guidance; ambiguous
instructions become schemas and hook policies; soft constraints become executable checks; and
implicit recovery becomes an observable state machine.
We buildFairyClawto realize and evaluate the Formal Skill concept. FairyClaw is an event-driven
LLM-agent runtime with a single-step planner, typed history Intermediate Representation (IR),
capability registry, hook pipeline, persistent session state, sub-agent delegation, and Formal Skill
routing. It is therefore not merely a system that uses Formal Skill, but the concrete runtime substrate
developed to make Formal Skills routable, executable, observable, and enforceable. We evaluate
FairyClaw on the independent Harness-Bench suite [ 33]. Among six evaluated agent harnesses,
FairyClaw obtains an average overall score of 0.690, ranking third by mean score across two model
families and first in the gpt-5.4 group, while using 7.35M tokens in total, or 49.0K tokens per task
on average. This per-task token use is about 48% lower than the mean of the other five harnesses
and about 33% lower than the next most token-efficient harness. On tasks that demonstrate typical
Formal Skill effects, FairyClaw achieves especially strong task-level results.
Our contributions are:
• We introduceFormal Skill, a token-efficient and enforceable skill abstraction that moves
procedural knowledge from long natural-language prompts into JSON metadata and action
schemas, reliable Python executors, hook-governed control loops, Formal Skill routing, and
skill-local runtime state.
• We implementFairyClaw, an open-source event-driven agent runtime for Formal Skills,
integrating single-step planning, typed history IR, persistent session state, sub-agent del-
egation, Formal Skill routing, and hook-based execution control. The implementation is
available athttps://github.com/PKULab1806/FairyClaw.
2 Related Work
2.1 Prompt-based agent skills andSKILL.md
Prompt-based agent skills are already widely used in practical agent systems. Anthropic’s Agent
Skills package discovery metadata written in YAML, a required SKILL.md instruction file, and
optional scripts or assets under progressive disclosure [13, 14, 15]; Claude Code adopts this pattern
with invocation controls, subagents, allowed tools, plugins, hooks, and MCP integration [ 16, 17].
These systems correctly identify reusable procedural knowledge as a missing layer between tools
and monolithic prompts. Their limitation is that the procedure itself remains mostly text-level:
once selected, the Markdown body is still paid for as prompt tokens, interpreted as semi-structured
natural language, and trusted to guide ordering, recovery, and completion. Optional scripts can make
subroutines deterministic, but the skill-level workflow usually remains prose. Formal Skill preserves
the packaging and progressive-disclosure intuition while moving the reusable procedure into JSON
metadata and action schemas, reliable executors, lifecycle hooks, and skill-local runtime state.
2

## Page 3

2.2 Tool use and structured action interfaces
Tool-use research shows that structured action interfaces extend model capability: Modular Reasoning,
Knowledge and Language (MRKL) routes language models to external modules [2], ReAct interleaves
reasoning with actions and observations [1], Toolformer learns API-use decisions [3], and Gorilla,
API-Bank, and ToolLLM/ToolBench study API selection and tool-call generation at scale [4, 5, 6].
Production systems instantiate this idea through JSON schemas and protocol boundaries, including
OpenAI function calling and Agents Software Development Kit (SDK) tools [21, 22], MCP tools and
resources over JSON Remote Procedure Call (JSON-RPC) [19, 20], and framework tools such as
LangChain [12]. These interfaces type individual actions, but a typed action is not yet a formal skill:
phase order, recovery state, side-effect policy, and completion gates are typically left to prompts or
outer orchestration. Formal Skill is complementary because it organizes structured actions under
routing, hooks, skill-local runtime state, and gates so that a tool set becomes an enforceable procedure.
2.3 Agent runtimes and software engineering agents
Agent and coding runtimes demonstrate that performance depends on the action space and feedback
channel, not only on the base model. Reflexion, Self-Refine, and V oyager study feedback and
reusable executable skills [7, 8, 9]; SWE-agent and AutoCodeRover show that repository navigation,
editing, testing, search, and repair workflows are shaped by the agent-computer interface [10, 11].
Engineering systems such as Claude Code [16, 18], Codex CLI [23, 24], OpenClaw [25, 26], and
Hermes Agent [30, 31, 32] expose workspaces, shell and file operations, sandbox or approval policies,
MCP integration, subagents, memory, toolsets, and skills. They make agents practically useful, but
reusable capability is still usually represented as either individual tools or textual skills. Formal Skill
makes the reusable procedure itself a first-class runtime object with compact descriptions, executable
policy, lifecycle control, and observable state.
3 Formal Skill Design and Implementation
Formal Skill is a runtime contract for reusable agent capability. It is motivated by the same failure
modes identified in the introduction and related work: prompt skills encode procedures as expensive
semi-structured text, leave execution constraints as soft instructions, and lack explicit skill-local
runtime state for recovery and completion. This section defines the abstraction, describes its im-
plementation in FairyClaw, and then instantiates it with CODEREPAIROPS, a concrete code-repair
skill.
3.1 Failure modes of prompt skills
A prompt skill is easy to author because it resembles an onboarding document for a human operator.
That convenience becomes a liability when the reader is a model whose actions affect a workspace.
The problem is not that natural language instructions are useless; it is that they are a weak boundary
between reasoning and side effects.
First, prompt skills aretextual procedures. A SKILL.md file can describe ordering constraints,
forbidden actions, recovery strategies, and reporting requirements, but all of this material must be
loaded as tokens and interpreted from prose. Even with progressive disclosure, the loaded instruction
is still semi-structured from the runtime’s perspective: the system can store the text, but it cannot
directly execute the procedure encoded in it.
Second, prompt skills provideweak execution constraints. A paragraph can say that the agent must
reproduce a failure before patching, must not edit tests, or must verify before finishing. Unless these
constraints are reimplemented in code, however, the runtime cannot hide inappropriate tools, reject
unsafe arguments, or block a premature final answer. The model may follow the instruction, but the
skill itself does not enforce it.
Third, prompt skills haveimplicit state and recovery. After a failed command, an invalid patch, or
a partially written artifact, the transcript contains evidence of what happened, but the skill has no
compact execution object that says which phase it is in, what obligations remain, or why completion
is blocked. This encourages ad hoc recovery and self-defined checkpoints, especially in long-horizon
tasks.
3

## Page 4

3.2 Formal Skill as an executable contract
A Formal Skill replaces the text-only procedure with a skill-local protocol that the runtime can inspect
and enforce. The model still reasons about the task and chooses actions, but the action surface is
governed by code, schema, state, and hooks. Its structure follows directly from the three failures
above.
• Structured skill interfaces: to address text-heavy procedures, a Formal Skill moves most
procedural knowledge out of prompt prose and into JSON metadata and action schemas,
Python executors, hook code, and configuration. The model sees short tool descriptions and
phase guidance, while detailed policies remain executable runtime objects. This reduces
repeated token consumption and avoids paying for long natural-language manuals on every
relevant turn.
• Executable enforcement: to address weak execution constraints, a Formal Skill turns
suggestions into runtime checks. Executors validate arguments and side effects; hooks filter
visible tools, reject unsafe calls, and prevent completion when verification or artifact gates
remain open. Constraints therefore become part of the agent’s action semantics rather than
instructions the model may or may not follow.
• Skill-local runtime state: to address implicit state and recovery, a Formal Skill stores
progress in skill-local runtime state consumed by hooks and tools. Fields such as phase,
verification status, produced artifacts, required artifacts, and gate-failure reasons make
recovery explicit: the runtime can decide whether to continue collecting evidence, return to
patching, enter reporting, or block finalization.
The resulting abstraction is not merely a more disciplined prompt. It is a division of labor: natural
language remains useful for task-specific reasoning, but reusable procedure is represented as compact
interfaces, executable policy, and stateful control.
This division also exposes a real trade-off. Prompt skills and Skill.md files are attractive partly
because they are easy for non-programmers to author: a user can describe a procedure in natural
language without writing schemas, executors, state machines, or hook code. Formal Skill raises
the authoring bar because the skill creator must specify JSON metadata, implement reliable Python
actions, and sometimes design state transitions enforced by hooks. We view this as a practical cost
rather than a conceptual objection. Modern LLMs are already strong code-generation systems, so an
informal skill can itself become the source artifact from which an agent synthesizes the corresponding
formal components: action schemas, executor skeletons, hook programs, and state definitions. In this
sense, Formal Skill can support a bootstrapping path in which users still begin with a human-readable
Skill.md, while the runtime or an assisting model compiles it into a token-efficient and enforceable
skill representation.
3.3 Hook-governed programming model
In FairyClaw, a Formal Skill is packaged as a capability plugin. The manifest declares tools and
hooks; configuration files define deterministic policy parameters; scripts implement executors and
hook logic. The programming model is intentionally divided along runtime boundaries.
The action plane is where model-visible verbs are defined. A code-repair skill, for example, should
not expose an unstructured “please fix the code” operation. It should expose smaller actions such as
collecting evidence, applying a unified patch, running verification, and writing artifacts. The JSON
side tells the model what operation exists and what arguments are valid; the Python side decides what
actually happens, including path checks, command allowlists, patch-shape validation, and structured
output.
The control plane is implemented by hooks around the LLM and tool boundary. Figure 1 shows the
pipeline. The point is not that each hook is complex; the point is that the runtime has named interven-
tion points where a skill can turn state into visible tools, guidance, validation, and continuation.
The state plane makes the procedure an execution object rather than a transcript conven-
tion. A repair state may include phase, verification_passed, required_artifacts,
produced_artifacts, gate_fail_reasons, and last-tool status. Hooks consume this state
4

## Page 5

FORMAL SKILL HOOK PIPELINE
TOOLS-PREPARED
resolve base +
routed tools
BEFORE-LLM-CALL
state -> tools
+ guidance
LLM CALL
choose one
visible action
AFTER-LLM-RESPONSE
repair missing
required action
BEFORE-TOOL-CALL
validate args
and policy
TOOL EXECUTOR
deterministic
operation
AFTER-TOOL-CALL
update state
+ gates
GATE OPEN:
NEXT WAKEUP
Compact state controls visibility, prompt injection, checks, and continuation.
Figure 1: Formal Skill hook pipeline. Hooks convert compact skill-local runtime state into tool
visibility, prompt guidance, policy checks, and continuation decisions.
to determine which tools are visible, whether another LLM turn is required, and whether the task can
finish.
3.4 Implementation of Formal Skill in FairyClaw
FairyClaw is the runtime we build to make Formal Skill executable. Its role is not to add another
long system prompt, but to provide the concrete runtime services that a Formal Skill requires: plugin
loading, capability routing, hook execution, persistent session state, typed history, workspace scoping,
and parent-child task collaboration. A Formal Skill is therefore not embedded as an instruction file
inside a prompt. It is registered as a capability plugin whose tools, hooks, configuration, and state are
resolved by the runtime before each model decision.
The most important implementation mechanism is skill routing. FairyClaw separates always-available
orchestration tools from domain-specific Formal Skills. The parent planner can create a sub-session
with a narrower task, workspace, deliverable contract, and routed skill set; the sub-session then sees
only the tools and hook policies required for that work. This reduces token cost and action ambiguity
at the same time: the model receives fewer irrelevant tool descriptions, and the enabled skill can
inject only phase-local guidance rather than a full procedural manual.
Algorithm 1Sub-agent Formal Skill routing
Require:Parent sessionpand delegated taskd
1: Readd’s task type, workspace root,done_when, and task text
2: Select candidate Formal Skills from the capability registry
3:for allcandidate skillcdo
4: Scorecby task type, trigger metadata, and policy constraints
5:end for
6: Create sub-sessionswith workspace root anddone_whencopied fromd
7: Attach selected manifests, configs, hooks, and tool schemas tos
8: Expose default orchestration tools plus routed skill tools
9: Run routed hooks around LLM and tool boundaries during each wakeup ofs
10: Report the result topwhen skill gates anddone_whenare satisfied
FairyClaw’s single-step inference loop supports this implementation, but it is not the main abstraction.
Its role is to provide clean intervention boundaries: after one LLM decision and its tool effects, the
runtime persists the turn, updates skill state, and schedules a follow-up event if a gate remains open.
This lets Formal Skill hooks observe every step without being hidden inside an opaque long-running
planner loop. Dynamic routing, single-step wakeups, and parent-child collaboration are therefore
runtime services for implementing Formal Skill.
5

## Page 6

3.5 Case Study: CODEREPAIROPSas a Formal Skill
CODEREPAIROPSinstantiates Formal Skill for code repair and test-driven debugging. It is inten-
tionally not a monolithic “repair” tool. The action plane exposes four structured tools for evidence
collection, unified patching, verification, and artifact writing; the control plane uses hooks to filter
those tools, inject phase-local guidance, validate calls, and keep the sub-session alive until gates pass.
The implementation recognizes five phase labels: reproduce, diagnose, patch, verify,
and report. Its injected default workflow is shorter, reproduce -> patch -> verify
-> report; diagnose is an optional compatibility phase for additional evidence or contextual
patching. The session state remains small: phase, verification status, failure signature, produced and
required artifacts, gate-failure reasons, and last-tool metadata.
REPRODUCE PATCH VERIFY REPORT
DIAGNOSE
EVIDENCE ONLY
EVIDENCE
UNIFIED PATCH
PATCH OK
STRUCTURED CHECKS
PASS
ARTIFACT GATE
EXTRA CONTEXT
OPTIONAL
DIAGNOSE
CONTEXT
VERIFICATION FAILS
Finish only after verification passes and required artifacts exist.
Figure 2: CODEREPAIROPSstate vocabulary and main transitions. In the current executor, evidence
collection from reproduce may advance directly to patch; diagnose remains a routed phase
for extra evidence or contextual patching.
Table 1 shows how the phase field is consumed before each model call. This is the main token-
efficiency mechanism: the model receives only the tools and constraints relevant to the next decision,
while the complete repair policy remains in executable code.
Table 1: CODEREPAIROPSphase policy. Tool names are abbreviated for layout; each maps to the
correspondingrepair_ * tool.
Phase Visible actions Hook policy and transition
reproducecollect evidence Only evidence collection is visible. Command or log evidence
updates the failure signature and advances topatch.
diagnosecollect, patch Routed optional phase. Evidence collection and unified patching
are visible; generic mutation tools remain hidden.
patchcollect, patch Patching must use the unified patch tool; guards reject protected
paths, missing hunks, append-only edits on existing files, and
oversized changes. Success advances toverify.
verifyverify Verification accepts structured checks. Passing checks set
verification_passed and advance to report; failures
return topatch.
reportwrite artifacts, done Artifact writing and completion are visible. Completion is
blocked until verification has passed and required artifacts in-
ferred fromdone_whenexist.
6

## Page 7

Algorithm 2CODEREPAIROPSexecution
Require:Sub-sessionsand repair stater
1:before_llm_callfilters visible tools byr.phaseand injects phase-local workflow guidance
2: The model chooses one visible repair action
3:before_tool_callchecks paths, patch shape, command policy, and verification checks
4: Execute the selected repair action with its Python executor
5: Update phase, verification status, produced artifacts, and gate reasons
6:ifverification or artifact gates remain openthen
7: Schedule a follow-up wakeup fors
8:else
9: Allow completion and return the repair report
10:end if
The injected workflow message is intentionally compact: current phase, visible tools, fixed
workflow order, no-completion-without-verification rule, required-artifact reminders inferred from
done_when, patch-only-through-repair_apply_unified_patch, and verification checks
shaped as {name,type,args}. This keeps procedural knowledge in executable state and hooks
rather than in a long natural-language repair manual.
Table 2: CODEREPAIROPShook program. Each hook is a small deterministic boundary program
around a single model or tool step.
Hook stage Checks or payload rewrite State-machine effect
before_llm_call Loads repair state, infers required arti-
facts from done_when, filters visible
tools by phase, and appends a user-role
workflow message.
Does not advance the phase. It narrows the
model’s next action space so invalid actions
are usually unreachable.
after_llm_response If the model emits no tool call, forces evi-
dence collection in reproduce, forces
verification in verify, or schedules a
report-stage follow-up when gates re-
main unresolved.
Prevents silent completion and re-enters the
loop at the same phase with an explicit re-
quired action.
before_tool_call Parses tool arguments. For patch calls,
checks target existence, protected path
patterns, and required hunk markers. For
verification, requires a non-empty check
list.
Blocks malformed calls before side effects.
Protected edits are redirected to an artifact
message; invalid patch or verification calls
force another turn.
after_tool_call Records last tool metadata, applies phase
updates after patch, verification, or arti-
fact writing, evaluates verification and
artifact gates, and publishes follow-up
events when needed.
Advances patch -> verify, verify
-> report on pass, verify -> patch
on fail, and keeps report open until com-
pletion gates pass.
The same three limitations of prompt skills appear concretely here. Instead of asking the model to
follow a repair order, CODEREPAIROPSchanges tool visibility by phase. Instead of asking the model
not to edit protected files, the patch tool and pre-tool hook reject unsafe edits. Instead of asking
for verification before completion, after-response and after-tool hooks keep the session alive until
verification and artifact gates pass. The result is not a black-box repair command but a compact
executable protocol distributed across JSON schemas, Python executors, hooks, and state.
4 Experiments and Analysis
4.1 Evaluation protocol
We evaluate the Formal Skill approach as implemented in FairyClaw on the independent Harness-
Bench suite [33]. Harness-Bench evaluates agents in real workspaces with task fixtures, executable
oracles, and usage accounting. From the benchmark repository, we use 75 tasks for this study. The
evaluation compares FairyClaw, Moltis [27], NullClaw [28], ZeroClaw [29], Hermes [30, 31], and
OpenClaw [25, 26] with two model families,gpt-5.4andgemini-3.1-pro.
For each task, the harness creates a fresh sandbox workspace, copies task fixtures into
workspace/in, renders the task prompt with workspace-local paths, and launches the target
7

## Page 8

agent through a harness adapter. During execution, a local usage proxy is injected through environ-
ment variables and placed between the agent runtime and its upstream model endpoint. The proxy
records every model request and response into requests.jsonl and responses/*.json,
including provider, response model, normalized input/output/cache/total token fields, assistant mes-
sages, and tool calls. For process grading, Harness-Bench reconstructs a compact call chain from
these proxy records: it removes system messages, keeps user/assistant/tool-call content, tracks main-
agent and sub-agent histories separately, skips context-compression calls, and emits only incremental
conversation deltas plus the corresponding assistant response. Token totals are aggregated from the
complete proxy log rather than from the shortened trace.
Scoring then combines executable task outcomes with process evidence. Each task provides an
oracle module that inspects the final workspace and returns an outcome_score; tasks that re-
quire semantic judgment may additionally attach an LLM-based quality score. The reconstructed
call chain is passed to a rubric grader that scores tool-use appropriateness, consistency or flow
coherence, robustness or error handling, and a binary security gate. The final benchmark score is com-
puted as combined = outcome_effective×process_effective×security .
The reported metrics are this combined score, total token usage, and average tokens per completed
task. Our analysis asks three questions aligned with the paper’s mechanism: whether FairyClaw is
competitive on overall score, whether it improves token efficiency, and whether routed Formal Skills
help on tasks that require controlled evidence, action, verification, and recovery.
4.2 Overall score and token efficiency
Table 3 summarizes the evaluated runs. On gpt-5.4, FairyClaw achieves the strongest combined
score among the compared agents, 0.746 over 75 tasks, while also using the fewest total tokens:
3.51M total and 46.8K per task. This is a favorable score–cost point: Moltis and Hermes are close
in score, but use 6.29M and 7.28M tokens respectively; OpenClaw, NullClaw, and ZeroClaw score
lower in this snapshot.
Table 3: Harness-Bench comparison across evaluated agent harnesses.
Agent Model Tasks Combined↑Total tok.↓Avg. tok.↓
FairyClawgpt-5.475 0.7463.51M46.8K
Moltisgpt-5.475 0.7446.29M83.8K
Hermesgpt-5.475 0.7407.28M97.0K
OpenClawgpt-5.475 0.6936.03M80.4K
NullClawgpt-5.475 0.6858.16M108.9K
ZeroClawgpt-5.475 0.5876.09M81.2K
OpenClawgemini-3.1-pro75 0.6896.58M87.7K
NullClawgemini-3.1-pro75 0.64512.70M169.3K
Moltisgemini-3.1-pro75 0.6436.27M83.6K
FairyClawgemini-3.1-pro75 0.6353.84M51.2K
Hermesgemini-3.1-pro75 0.6226.21M82.8K
ZeroClawgemini-3.1-pro75 0.5064.86M64.8K
Across both model families, FairyClaw’s automatic context-compression mechanism before reaching
the maximum context window was disabled. The observed token reduction therefore comes from
routed Formal Skills, compact phase guidance, and narrower tool exposure rather than from aggressive
transcript compression. On gemini-3.1-pro, FairyClaw is not the highest aggregate-scoring
agent, but it remains competitive while preserving the strongest token-efficiency profile. It uses 3.84M
total tokens, compared with 4.86M for ZeroClaw, 6.21M for Hermes, 6.27M for Moltis, 6.58M for
OpenClaw, and 12.70M for NullClaw.
4.3 Skill-relevant task behavior
The aggregate comparison is only one view of Formal Skill. Its mechanism should matter most on
procedural tasks where the agent must avoid unsafe shortcuts and premature completion. Table 4 re-
ports one such code-debugging task from the benchmark: the workspace containsbuggy_code.py
with five layered bugs, only the current layer is exposed in each round, and the agent must edit the
file, validate it, and stop after the current layer passes. FairyClaw obtains the strongest combined
8

## Page 9

score in both model families: 0.865 with gpt-5.4 and 0.843 with gemini-3.1-pro. This is
consistent with CODEREPAIROPS’ purpose: make the repair loop executable through phase-specific
tool visibility, patch guards, verification checks, and completion gates.
Table 4: Representative code-debugging task results. This task stresses evidence collection, workspace
modification, verification, and recovery.
Agent Model Combined↑Total tok.↓Rounds↓
FairyClawgpt-5.40.865 193.0K 48
NullClawgpt-5.40.858 193.0K 21
Hermesgpt-5.40.807 750.5K 99
Moltisgpt-5.40.793 306.8K 24
OpenClawgpt-5.40.730 349.1K 24
ZeroClawgpt-5.40.700 207.8K 24
FairyClawgemini-3.1-pro0.843 209.3K 54
Hermesgemini-3.1-pro0.836 330.2K 89
OpenClawgemini-3.1-pro0.706 290.5K 23
NullClawgemini-3.1-pro0.692 293.0K 29
Moltisgemini-3.1-pro0.657 154.8K 19
ZeroClawgemini-3.1-pro0.537 138.4K 21
These task-level results should not be interpreted as a claim that every task is solved by CODERE-
PAIROPS. Rather, they identify the regime in which Formal Skill is most visible: the task has a
meaningful procedure and the procedure has unsafe shortcuts. FairyClaw may spend more rounds
than some baselines, but those rounds are governed by Formal Skill routing and hook-controlled state
transitions rather than by an unstructured transcript. Its lower token consumption is evidence that this
longer trajectory is not driven by verbose prompt accumulation, but by compact state-conditioned
control.
4.4 Analysis
The experiments show three main results. First, FairyClaw is competitive on overall Harness-Bench
score: across the six evaluated harnesses, it ranks third by mean score over the two model families
and is the top-scoring harness in the gpt-5.4 group. Second, FairyClaw uses substantially fewer
tokens than the compared systems. Because context compression was disabled during these runs, the
token reduction is attributable to Formal Skill routing, compact phase guidance, and narrower tool
exposure rather than transcript summarization. Third, FairyClaw performs especially well on the
representative code-debugging task, where CODEREPAIROPSmakes evidence collection, patching,
verification, and completion gates explicit. Together, these results suggest that Formal Skill improves
agent efficiency while preserving, and in some procedural tasks improving, task performance.
5 Conclusion
We presentedFormal Skill, a runtime-native way to turn reusable agent skills from long prompt
instructions into programmable protocols with JSON schemas, reliable executors, hooks, routing
metadata, and skill-local state. FairyClaw implements this concept as an event-driven agent runtime,
and CODEREPAIROPSshows how it becomes a concrete workflow for code repair. On Harness-
Bench, FairyClaw achieves competitive overall scores, ranks first in thegpt-5.4 group and third
by mean score across the six evaluated harnesses, and uses substantially fewer tokens. These results
support the view that agent skills should be token-efficient, runtime-governed protocols rather than
natural-language documents alone.
References
[1] Yao, S., Zhao, J., Yu, D., et al. ReAct: Synergizing reasoning and acting in language models.
ICLR, 2023.https://arxiv.org/abs/2210.03629.
[2] Karpas, E., Abend, O., Belinkov, Y ., et al. MRKL systems: A modular, neuro-symbolic
architecture that combines large language models, external knowledge sources and discrete
reasoning. arXiv:2205.00445, 2022.https://arxiv.org/abs/2205.00445.
9

## Page 10

[3] Schick, T., Dwivedi-Yu, J., Dessi, R., et al. Toolformer: Language
models can teach themselves to use tools. NeurIPS, 2023. https:
//proceedings.neurips.cc/paper_files/paper/2023/hash/
d842425e4bf79ba039352da0f658a906-Abstract-Conference.html.
[4] Patil, S. G., Zhang, T., Wang, X., and Gonzalez, J. E. Gorilla: Large language model connected
with massive APIs. NeurIPS, 2024.https://arxiv.org/abs/2305.15334.
[5] Li, M., Zhao, Y ., Yu, B., Song, F., Li, H., Yu, H., Li, Z., Huang, F., and Li, Y . API-
Bank: A comprehensive benchmark for tool-augmented LLMs. EMNLP, 2023. https:
//aclanthology.org/2023.emnlp-main.187/.
[6] Qin, Y ., Liang, S., Ye, Y ., et al. ToolLLM: Facilitating large language models to master 16000+
real-world APIs. ICLR, 2024.https://arxiv.org/abs/2307.16789.
[7] Shinn, N., Cassano, F., Berman, E., et al. Reflexion: Language agents with verbal reinforcement
learning. NeurIPS, 2023.https://arxiv.org/abs/2303.11366.
[8] Madaan, A., Tandon, N., Gupta, P., et al. Self-Refine: Iterative refinement with self-feedback.
NeurIPS, 2023.https://arxiv.org/abs/2303.17651.
[9] Wang, G., Xie, Y ., Jiang, Y ., et al. V oyager: An open-ended embodied agent with large language
models. arXiv:2305.16291, 2023.https://arxiv.org/abs/2305.16291.
[10] Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K. R., and Press, O.
SWE-agent: Agent-computer interfaces enable automated software engineering. NeurIPS, 2024.
https://openreview.net/forum?id=mXpq6ut8J3.
[11] Zhang, Y ., Ruan, H., Fan, Z., and Roychoudhury, A. AutoCodeRover: Autonomous program
improvement. ISSTA, 2024.https://arxiv.org/abs/2404.05427.
[12] Chase, H. LangChain: Building applications with LLMs through composability. GitHub reposi-
tory, 2022.https://github.com/langchain-ai/langchain.
[13] Anthropic. Agent Skills. Claude documentation. https://docs.anthropic.com/en/
docs/agents-and-tools/agent-skills/overview.
[14] Anthropic. Agent Skills specification.https://agentskills.io/specification.
[15] Anthropic. Equipping agents for the real world with Agent Skills. Anthropic
Engineering Blog, 2025. https://www.anthropic.com/engineering/
equipping-agents-for-the-real-world-with-agent-skills.
[16] Anthropic. Extend Claude with skills. Claude Code documentation. https://docs.
anthropic.com/en/docs/claude-code/skills.
[17] Anthropic. Create plugins. Claude Code documentation. https://code.claude.com/
docs/en/plugins.
[18] Anthropic. Give Claude custom tools. Claude Code Agent SDK documentation. https:
//code.claude.com/docs/en/agent-sdk/custom-tools.
[19] Model Context Protocol. Overview. https://modelcontextprotocol.io/
specification/latest/basic.
[20] Model Context Protocol. Tools. https://modelcontextprotocol.io/
specification/draft/server/tools.
[21] OpenAI. Function calling. OpenAI API documentation. https://platform.openai.
com/docs/guides/function-calling.
[22] OpenAI. Tools. OpenAI Agents SDK documentation. https://openai.github.io/
openai-agents-python/tools/.
[23] OpenAI. Codex CLI. OpenAI Developers documentation. https://developers.
openai.com/codex/cli/.
[24] OpenAI. Sandbox. Codex documentation. https://developers.openai.com/
codex/concepts/sandboxing.
[25] OpenClaw. Agent runtime. OpenClaw documentation. https://docs.openclaw.ai/
concepts/agent.md.
10

## Page 11

[26] OpenClaw. Tools. OpenClaw documentation. https://github.com/openclaw/
openclaw/blob/bf6ec64f/docs/tools/index.md.
[27] Moltis. A secure persistent personal agent server in Rust. GitHub repository. https://
github.com/moltis-org/moltis.
[28] NullClaw. Autonomous AI assistant infrastructure. GitHub repository. https://github.
com/nullclaw/nullclaw.
[29] ZeroClaw. Autonomous AI agent runtime. GitHub repository. https://github.com/
zeroclaw-labs/zeroclaw.
[30] Nous Research. Hermes Agent documentation. https://hermes-agent.
nousresearch.com/docs/.
[31] Nous Research. Hermes Agent architecture. https://hermes-agent.nousresearch.
com/docs/developer-guide/architecture/.
[32] Nous Research. Environments, benchmarks and data generation. Hermes Agent documenta-
tion. https://hermes-agent.nousresearch.com/docs/developer-guide/
environments.
[33] Qihoo360. Harness-Bench: A real-workspace benchmark for evaluating agent and claw-style
frameworks under executable task conditions. GitHub repository.https://github.com/
Qihoo360/harness-bench.
11
