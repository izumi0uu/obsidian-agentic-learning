# PIVOT: Bridging Planning and Execution in LLM Agents via Trajectory Refinement - Extracted Text

- Source note: [[PIVOT - Bridging Planning and Execution in LLM Agents via Trajectory Refinement]]
- Source PDF: `assets/PIVOT - Bridging Planning and Execution in LLM Agents via Trajectory Refinement.pdf`
- Extracted: 2026-05-14
- Extractor: pypdf
- Pages: 27
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

PIVOT: Bridging Planning and Execution in LLM
Agents via Trajectory Refinement
Tuo Zhang
tuozhang@amazon.com
Alin-Ionut Popa
popaaln@amazon.com
Yan Xu
yanxuml@amazon.com
Rui Song
ruisong@amazon.com
Dimitrios Dimitriadis
dbdim@amazon.com
Figure 1:Plan–Execution Misalignment in LLM Agents.LLM-generated plans (blue) often
appear valid but diverge during execution (red) due to infeasible steps, incorrect state assumptions,
or constraint violations. These discrepancies compound over long horizons, lead to undesirable or
suboptimal outcomes. Aligning planning with execution to reach an optimal trajectory (green) is
therefore a core challenge in reliable agentic systems.
Abstract
Large language model (LLM)-based agents frequently generate seemingly coher-
ent plans that fail upon execution due to infeasible actions, constraint violations,
and compounding errors over extended horizons. PIVOT (Plan–Inspect–eVOlve
Trajectories) addresses this plan–execution misalignment through a self-supervised
framework that treats trajectories as optimizable objects iteratively refined via
environment interaction. The framework comprises four stages: PLAN generates
candidate trajectories; INSPECT executes them and computes structured losses
with textual gradients encoding plan–execution discrepancies; EVOLVE applies
these signals to produce improved trajectories; and VERIFY performs a final global
check against task constraints. A monotonic acceptance process ensures a non-
decreasing solution quality. Empirical evaluations on DeepPlanning and GAIA
demonstrate state-of-the-art performance: with human-in-the-loop (HITL) feed-
back, PIVOT establishes a strong upper bound up to ∼94% relative improvement
in constraint satisfaction, while its fully autonomous variant retains substantial
gains, showing that the core trajectory-refinement mechanism remains effective
without external supervision. At the same time, PIVOT remains computationally
efficient, requiring up to 3–5× fewer tokens than competing refinement methods.
These findings establish that (self- or human-supervised) feedback-based trajectory
optimization is a principled methodology for mitigating plan–execution gaps in
autonomous agent systems.
Preprint.
arXiv:2605.11225v1  [cs.AI]  11 May 2026

## Page 2

1 Introduction
The deployment of agents based on large language models (LLMs) as autonomous decision-makers
marks a paradigm shift in how AI systems interact with the world. Rather than merely generating text,
these agents plan multi-step action trajectories, invoke tools and APIs, and adapt to environmental
feedback [15, 14]. Yet as the scope and autonomy of these agents grow, a fundamental reliability gap
persists that current architectures fail to adequately address. The core difficulty isplan–execution
misalignment: the systematic divergence between an agent’s intended actions and its realized behavior
in a dynamic environment. As shown in Fig. 1, an LLM agent produces seemingly coherent plans,
yet fails during execution due to infeasible actions, incorrect assumptions about the environment, or
constraint violations that only become apparent upon interaction. Critically, these failures compound
throughout the trajectory, triggering cascading errors that often render the remainder of the plan
unrecoverable [27]. This problem is not confined to text-based agentic systems; analogous challenges
arise in multi-agent robotic planning under partial observability [ 15], underscoring a converging
insight across the field:planning and execution must remain tightly coupled.
Existing agent-improvement methods only partially address this challenge because they lack a
trajectory-level optimization view. Diagnostic methods identify failures post-hoc but do not optimize
the underlying plan; iterative refinement methods revise local reasoning steps or prompts; constraint-
based methods apply localized fixes; and evolutionary methods search over candidate trajectories
without directly optimizing the loss induced by execution outcomes (see Sec. 2). What is missing is a
mechanism that treats the full trajectory as anoptimizable objectand converts execution feedback
into an update signal. To this end, we proposePIVOT(Plan–Inspect–eVOlve Trajectories), a self-
supervised framework that formulates trajectory refinement as iterative optimization in a discrete,
language-defined space. PIVOT defines a trajectory-level objective combining goal-achievement loss,
plan–execution divergence, and execution cost. Since exact gradients are unavailable for language
trajectories, PIVOT uses structured natural-language feedback as a surrogatetextual gradient[23],
guiding local updates to the unsupported parts of the plan. A preference-based monotonic acceptance
rule then keeps only refinements that improve the estimated trajectory loss, yielding a gradient-like
optimization procedure over plans without requiring model fine-tuning.
We evaluate PIVOT on two complementary benchmarks: DeepPlanning [26], which stresses long-
horizon constraint satisfaction in Travel and Shopping Planning, and GAIA [14], which tests open-
domain tool use and multi-step reasoning. PIVOT performs best on constraint-heavy planning tasks,
where execution feedback exposes recoverable violations for trajectory-level repair. HITL feedback
provides an upper-bound regime, while the autonomous variant remains competitive without external
supervision. On GAIA, gains are more limited by retrieval quality, but PIVOT still improves task
success in realistic tool-augmented settings. Across model families, PIVOT complements backbone
scaling and remains token-efficient relative to competing refinement methods.
PIVOT represents a meaningful scientific advance in closing the plan–execution gap for LLM agents.
It proposes safer autonomous systems, democratized capabilities, computational efficiency, and
interpretable failure attribution. However, these same capabilities introduce risks around reduced
human oversight, dual-use potential, misplaced trust, and labor displacement that must be proactively
addressed. The responsible path forward requires coupling PIVOT technical contributions with
deployment guardrails, and ongoing evaluation in real-world settings beyond controlled benchmarks.
2 Related Work
Trajectory analysis and failure diagnosis.A growing body of work studies the reliability gap
between planned and executed agent behavior through trajectory analysis and failure diagnosis [2,
4, 9, 12, 24, 25, 27]. AgentDebug [ 27] models agent behavior as a modular pipeline and shows
how errors propagate across components, while VeriLA [18] introduces human-centered criteria for
identifying component-level failures. In multi-agent settings, MAST [2] and attribution benchmarks
such as Who&When [25] and AgenTracer [24] highlight the difficulty of localizing failures in long
trajectories. These diagnostic efforts motivate closed-loop correction, but do not formulate trajectory
improvement as an optimization procedure.
Planning robustness and execution-grounded correction.Complementary approaches improve
planning robustness before or during execution. Constraint-based methods [9, 11] detect violations
2

## Page 3

by checking plans against task requirements and applying localized corrections. Pre-execution
refinement includes iterative self-critique [ 1], explicit problem modeling [ 16], and long-horizon
lookahead mechanisms such as FLARE [10]. Hierarchical planning and execution frameworks [3]
reduce non-executable plans by structuring decisions across abstraction levels. In multi-agent
robotics, LLaMAR [15] introduces a plan-act-correct-verify architecture that decomposes high-level
instructions into subtasks and uses a Corrector module to repair failed actions from real-time visual
observations under partial observability, without oracle feedback. While LLaMAR demonstrates
the value of execution-grounded correction, its repairs remain localized to individual action failures
within a centralized multi-agent system and do not optimize the full plan–execution discrepancy.
Iterative refinement and trajectory-level optimization.Most closely related are methods that
iteratively refine model outputs using feedback. Self-Refine [13] and Reflexion [17] improve outputs
or behaviors through self-generated feedback, while CRITIC [ 5] refines reasoning through tool-
interactive self-critique. Recent self-critique methods [ 1] further show that structured refinement
of intermediate reasoning and tool use can yield strong empirical gains, especially when domain
expertise is incorporated; however, such approaches remain largely local, operating through step-wise
corrections rather than modeling the full trajectory as an optimizable object. PromptAgent [ 21]
similarly frames optimization as search over prompts and intermediate states, but does not directly
optimize execution-grounded trajectory discrepancies. SE-Agent [8] moves closer to trajectory-level
optimization by treating trajectories as genotypes whose phenotypic expression is problem-solving
performance, using revision, recombination, and refinement to exploit cross-trajectory diversity and
escape local optima on SWE-bench Verified. This shares PIVOT’s view of trajectories as optimizable
objects, but derives its signal fromcross-trajectory diversity and recombinationrather than fromhow
intended plans diverge during execution. PIVOT instead models the plan–execution discrepancy as a
structured loss and interprets execution feedback as a textual gradient,i.e., TextGrad [23], enabling
gradient-like optimization directly in trajectory space through a task-agnostic, self-supervised loop.
Figure 2:Overview of PIVOT, a trajectory-level optimization framework for aligning planning and
execution in LLM agents. Given a task t, the PL A Nmodule generates candidate trajectories τ, which
are executed in the environment M to produce traces ˆτ. The IN S P E C Tmodule performs backward
discrepancy analysis, computing a loss bL and a textual gradient g that localizes the earliest failure
point i⋆ and attributes errors to trajectory steps. Guided by this signal, the EV O L V Emodule updates
the trajectory by preserving the validated prefix and rewriting the unsupported suffix, producing an
improved candidate τ′. This iterative Plan–Inspect–Evolve loop performs gradient-like optimization
in trajectory space. Finally, VE R I F Yenforces global constraint satisfaction, yielding a final trajectory
τ⋆ that aligns planning with execution while respecting task requirements.
3 PIVOT: Discrepancy-Driven Trajectory Refinement
The proposed algorithm PIVOT is a trajectory-level framework that improves alignment between
planning and execution by iteratively refining agent trajectories using execution feedback. The method
operates as a self-supervised learning loop, where trajectories are evaluated through interaction with
the environment and improved based on structured feedback. The overview of the PIVOT is illustrated
in Fig. 2, and the mechanism is formalized in Alg. 1 in the App. B.
Problem Setup.We consider a task t to be completed over an environment M= (S,A,O) , where
S is the state space, A is the action space, O the space of outcomes (aka observations) after each
step, and a transition function f(·) that maps state-action interactions to next states and outcomes ,
f:M → S × O, reflecting the environment dynamics induced by agent actions.
A trajectory τK of length K is defined as τK = ((s0, a0), . . . ,(sK, aK)), where k≤K , sk ∈ S
and ak ∈ A. Executing τk up to a step k produces an outcome ok evaluated as G(ˆτ≤k, ok), with
transitions following(s k+1, ok+1) =f(sk, ak, ok).
3

## Page 4

These definitions are task-agnostic: the initial plan τ(0) should preserve user-specified requirements,
the executed trace ˆτ(0) reveals where they are no longer supported, IN S P E C Tproduces a repair
signal, andEV O L V Erewrites the remaining trajectory.
PLAN: Trajectory Generation and Forward Rollout.PIVOT begins with thePL A N
 module,
which converts the task into an explicit candidate trajectory. Like chain-of-thought reasoning, agent
execution unfolds as an explicit reasoning-and-action trace; here, we view that trace as an unrolled
forward computation in trajectory space. A planned trajectory τ induces an execution trace ˆτwhen
interacting with the environment, that can diverge due to incorrect assumptions or infeasible actions.
We capture this mismatch through a trajectory-level objective:
L(τ) =ℓG(ˆτ, oK) +D(τ,ˆτ) +C(ˆτ),(1)
This objective combines three complementary sources of error: The term ℓG(ˆτ, oK) captures failure
to achieve the desired task outcome, i.e. a terminal goal-achievement loss derived from the reward-like
success function G(ˆτ, oK) as ℓG(ˆτ, oK) = 1−G(ˆτ, oK), D(τ,ˆτ) measures divergence between
planned and executed trajectories, and C(ˆτ)penalizes inefficient execution, defined as the number of
tool calls: C(ˆτ) =PK
i=0 1[ai invokes a tool]. This decomposition separates three different failure
modes. The term ℓG(ˆτ, oK) rises when the final outcome fails to satisfy the task, D(τ,ˆτ)increases
once execution no longer preserves the constraint structure encoded in the plan, and C(ˆτ)captures
the computation spent on trajectories that have already gone off course.
To localize failure, we identify the first step at which the planned and executed trajectories diverge :
i⋆ = min{i:D(τ ≤i,ˆτ≤i)≥T},(2)
where T is a divergence threshold. The index i⋆ marks the earliest step at which the executed trace
no longer provides sufficient support for the planned trajectory prefix, and therefore identifies the
point from which local repair should begin.
INSPECT: Backward Discrepancy Analysis via Textual Gradients.The objective in Eq. 1
provides a unified signal for trajectory refinement by aggregating goal-level, trajectory-level, and
efficiency-related errors. If Section 3.2 treats the agent trace as a forward rollout, then IN S P E C T
performs the reverse operation: once a task-level loss is observed, it analyzes the trajectory backward
to identify the earliest causally responsible break. For a specific trajectory, the gradient of L becomes,
∂L
∂τ ≈
X
i≤K

∇τiℓG(·) +∇τiD(·) +∂C(·)
∂τi

,(3)
each term contributes error signals to every trajectory step, playing the role of backward credit
assignment over the discrete trace: deviations from the final outcome are attributed to earlier reasoning
or action decisions that caused them; mismatches between planned and executed behavior are localized
to the steps where support is lost, and inefficient tool use is attributed to the actions that incurred it.
Trajectories are discrete and non-differentiable, making backpropagation not possible. Instead, we
approximate this backward analysis using a trajectory-level decomposition inspired by TextGrad [23].
The loss components are then estimated through structured natural language feedback rather than
exact mathematical derivatives under different supervision regimes. In the fully supervised setting
(“human-in-the-loop” or HITL), these terms are computed using human feedback that evaluates goal
satisfaction and trajectory consistency [19]. In a self-supervised setting, an LLM-as-a-judge model
provides structured feedback on final outcomes and intermediate execution behavior [6]. In contrast,
the cost termC(ˆτ)is supervision-independent, reflecting execution (i.e.tool calls) efficiency.
The resulting textual gradientg(τ)≈∂L/∂τis therefore not just a critique of the final answer; it is
a structured backward-attribution signal over the trajectory. Starting from the observed loss at the
outcome, IN S P E C Ttraces the causal chain backward until it reaches the first broken assumption,
then emits a repair instruction for EV O L V E. In practice, this diagnosis identifies four pieces of
information: the observed failure at the outcome, the immediate downstream manifestation of that
failure in the executed trace, the earliest causally responsible break in the trajectory, and an actionable
repair signal for rewriting the unsupported suffix.
EVOLVE: Local Trajectory Repair and Update.Given a backward attribution signal from
IN S P E C T, the role of EV O L V E
 is to produce an improved trajectory by modifying current plan
4

## Page 5

in response to identified discrepancies. At iteration r≤R , EV O L V Eproposes an updated trajectory:
τ′ =EV O L V E(ˆτ(r), τ(r), g(r)),(4)
where g(r) specifies both the location and nature of the failure. Rather than regenerating the full
trajectory, the update operates locally: the validated prefixτ ≤i⋆ is preserved, while the unsupported
suffix is rewritten, focusing on the part of the trajectory responsible for the current loss.
The candidate trajectory is then executed and evaluated:
( bL′, g′) =IN S P E C T(ˆτ′, τ′, t).(5)
The update is accepted only if it improves the objective:
τ(r+1) =
(
τ′ if bL′ ≺ bL(r),
τ(r) otherwise. (6)
This accept/reject mechanism ensures monotonic improvement, while preventing degradation from
noisy feedback, resembling a gradient-based update in the trajectory space, whereIN S P E C Tprovides
a structured approximation of the loss andEV O L V Eperforms a local step guided by this signal.
VERIFY: Global Constraint Validation.While IN S P E C Tprovides local feedback for trajectory
refinement, it does not guarantee that the final trajectory fully satisfies the original task specification.
To address this, PIVOT applies a final validation step usingVE R I F Y
 , which performs a global
check over the complete trajectory. Given a candidate solution τ, VE R I F Yevaluates whether
all user-specified constraints and requirements are satisfied. This step operates independently of
the trajectory-level discrepancy signals used during refinement, ensuring that improvements in
intermediate behavior do not come at the expense of violating the original task. The final output of
the system is therefore obtained by applying:
τ⋆ =VE R I F Y
 ≺
arg min
r≤R
bL(r), t

,(7)
which enforces that the selected trajectory is both optimal under the refinement objective and
consistent with the task specification.
4 Experiments
We evaluate PIVOT on three axes: (1)trajectory alignment optimization: can explicitly optimizing
the alignment between planned trajectories and executed behavior translate into state-of-the-art task
performance and improved reliability on long-horizon agent benchmarks? (2)execution efficiency:
are these gains practically attainable under favorable token usage and execution overhead? and (3)
improvement attribution: which components drive the observed gains, and what gives PIVOT an
advantage over prior agent frameworks?
4.1 Experimental Setup
Benchmarks and Evaluation Metrics.We evaluate PIVOT on two complementary benchmarks.
DeepPlanning [26] is a long-horizon planning benchmark with two tool-grounded domains:Travel
PlanningandShopping Planning, each containing 120 tasks. Travel Planning requires generating
multi-day itineraries under temporal, budget, and feasibility constraints using benchmark-specific
APIs, while Shopping Planning focuses on combinatorial product selection under budget and compat-
ibility constraints. We follow the official benchmark protocol and use composite score for Travel
Planning and case accuracy for Shopping Planning as the main evaluation metrics. GAIA [ 14]
contains 466 human-authored, open-domain questions that require multi-step reasoning and tool use
in realistic assistant settings. We report exact-match task success rate as guided in the original dataset
paper. We equip the agent with four basic tools in the evaluation: (1)web_search, which issues
Google queries and returns top snippets; (2) web_fetch, which retrieves and extracts the text of a
given URL; (3) read_file, a multi-format attachment reader that handles PDF, Office documents
5

## Page 6

(.xlsx, .docx, .pptx), images, audio, CSV/JSON/text, and ZIP archives; and (4) python_exec, a
sandboxed Python interpreter for calculation and data manipulation, details in App. E.2.
Baselines.We compare PIVOT against four representative agent baselines. ReACT [ 22] serves as a
canonical single-pass reasoning-and-acting baseline. Self-Critique [1] is a self-refinement baseline
where the model incorporates domain knowledge, critiques and revises its own plans without an
external verifier, providing a competitive benchmark for iterative plan improvement. SE-Agent [7]
is a self-evolving agent framework whose World-State-Model critic produces structured trajectory-
level judgments and corrective guidance without external supervision, offering a complementary
autonomous-critique baseline. Finally, AgentDebug [ 27] is a debugging framework that isolates
root-cause failures and generates corrective feedback for recovery, making it an especially relevant
comparison for our discrepancy-driven refinement setting.
Experimental Settings.We instantiate all methods on the same set of underlying model backbones,
including Qwen3-235B [20], Claude 4.5 model family, and Claude 4.6 Opus. We evaluate PIVOT
under two feedback regimes:w/ HITL, where the IN S P E C Tmodule receives external human
feedback, andw/o HITL, where the feedback is generated automatically. Importantly, the Self-
Critique [1] and AgentDebug [ 27] baselines also rely on human-provided or externally supplied
feedback in their evaluated setups. We therefore interpret these baselines as most directly comparable
to PIVOTw/ HITL, while PIVOTw/o HITLrepresents the fully autonomous setting. This distinction
is important when reading the results: improvements over Self-Critique and AgentDebug reflect gains
over feedback-assisted baselines, whereas PIVOTw/o HITLisolates the contribution of the automatic
trajectory-refinement loop. To ensure fair comparison, all methods use the same benchmark-specific
tools, prompt templates, and task environments; the full prompts and implementation details are
provided in the App. A.
Figure 3:Trajectory-level repair via PIVOT with HITL feedback.The initial rollout violates
constraint C4 after a failed retrieval for “Canyon Flavor Restaurant,” producing an invalid itinerary.
With HITL, IN S P E C Tuses human feedback to localize the first causal break and produce a textual
gradient; EV O L V Erepairs only the unsupported suffix while preserving the valid prefix. The refined
trajectory restores the required entity and satisfies C1–C4. Without HITL, the flow is unchanged, but
IN S P E C Tobtains the discrepancy diagnosis and textual gradient from an LLM-as-a-judge.
4.2 Main Results
Table 1 summarizes the main evaluation results; we also visualize a running example to illustrate how
PIVOT works in Fig. 3. There are four main observations:
PIVOT is consistently strong across models and benchmarks.PIVOT (w/ HITL) achieves the best
results in all of model–benchmark cells. The gains are especially pronounced on smaller backbones:
on Travel Planning, Qwen3-235B improves from 28.3 to 39.9 and Claude 4.5 Haiku from 35.2 to
57.3; on Shopping Planning, the same models improve from 10.8 to 76.7 and from 25.8 to 89.2.
6

## Page 7

Stronger backbones still benefit, indicating that PIVOT complements backbone scaling rather than
only compensating for weaker models.
PIVOT remains strong even without human feedback.PIVOT (w/o HITL) already outperforms
the strongest non-PIVOT baseline in 12 of 20 model–benchmark cells, and it improves over ReACT
in all 20 cells. The gains are most consistent on Travel Planning, where it beats the strongest baseline
across all five backbones. Human feedback brings additional gains, but it is not the sole reason
PIVOT works well. In the remaining 8 cells, Self-critique outperforms PIVOT (w/o HITL) due to the
incorporated domain knowledge.
Tool quality bounds the upside of trajectory refinement.Unlike DeepPlanning, GAIA is an
open-ended benchmark, evaluated only with a basic toolkit rather than specialized APIs. Once PIVOT
identifies a likely root cause, re-calling the same tools often returns the same evidence, rendering
refinement closer to retrying than to an actual recovery. As such, PIVOT remains competitive on
GAIA but stays closer to Self-Critique than it does on DeepPlanning.
PIVOT is token-usage efficient.To isolate the computational cost, we compute the extra tokens
each method spends on cases it solves relative to the ReACT baseline in DeepPlanning. We report
the per-case median and aggregate across backbones with the median-of-medians to be robust to
long-tail outliers where weaker backbones enter tool-call loops under ReACT. In Fig. 4, PIVOT saves
345k (4.2×) and 320k (4.1×) extra tokens per solved case compared to Self-Critique and AgentDebug,
respectively, due to: (1) Both baselines require a second full trajectory conditioned on a long failure
transcript, scaling their cost with how much the backbone needs to explore in the first place. PIVOT
instead steers a single trajectory with four in-line prompts, adding a bounded overhead that is largely
independent of backbone verbosity. (2) PIVOT bounds the worst case: when a backbone enters a long,
non-productive exchange, PIVOT inspect/evolve triggers can redirect it within the current trajectory,
whereas post-hoc methods inherit the full failed transcript and must “re-pay” for it.
Travel Planning Shopping Planning GAIA
Method
Q3
235B Haiku4.5 Sonnet4.5
Opus
4.5
Opus
4.6
Q3
235B Haiku4.5 Sonnet4.5
Opus
4.5
Opus
4.6
Q3
235B Haiku4.5 Sonnet4.5
Opus
4.5
Opus
4.6
ReACT [22] 28.3 35.2 53.1 62.9 86.0 10.8 25.8 40.8 43.3 50.8 31.5 37.0 40.6 59.4 57.0
Self-Critique [1] 30.1 45.1 52.6 75.2 87.3 16.7 35.8 55.8 53.3 70.0 37.6 44.851.5 64.2 68.5
SE-Agent [7] 29.6 41.9 52.6 63.9 82.8 15.8 31.7 45.8 43.7 53.7 37.5 37.0 40.0 57.6 56.4
AgentDebug [27] 25.1 42.7 46.2 59.3 86.1 15.0 33.3 47.5 45.8 53.3 33.4 41.8 47.9 63.6 66.7
PIVOT (w/o HITL)39.8 53.7 59.8 76.5 89.3 20.0 37.5 43.3 48.3 55.8 35.2 40.6 41.8 60.6 64.8
PIVOT (w/ HITL)39.9 57.3 67.1 82.7 96.2 76.7 89.2 89.2 94.2 98.3 41.8 44.8 52.7 68.5 71.5
Table 1:Main results across DeepPlanning and GAIA.Travel reports composite score, Shopping
reports case accuracy, and GAIA reports task success rate (all in %). Each column group corresponds
to one benchmark, and each row reports the same agent framework instantiated on the same set of
backbones. PIVOT is reported under two feedback regimes,w/o HITLandw/ HITL. We bold the best
result and underline the second-best result within each column.
Figure 4:Extra token cost per solved case, relative to ReACT baseline.Bars report median extra
billed tokens (input + output) on solved cases (composite score ≥0.7 ); lower is better. PIVOT (w/o
HITL) adds 3–5 × fewer tokens than Self-Critique, SE-Agent or AgentDebug; the HITL variant
remains cheaper than either baseline. End-to-end latency cannot be directly measured for API-based
LLMs, but token usage serves as a proxy - inference cost and response time scale with token usage.
7

## Page 8

4.3 Why PIVOT Works
Thinking is in the right place.A natural alternative to structured reflection is to simply allocate
more test-time compute by raising the extended-thinking budget but this does not work, as in Fig. 5;
increasing the budget yields no consistent gain on either benchmark. Inspection of the trajectories
reveals that under the default extended-thinking regime, 100% of thinking blocks fire on the first
assistant turn, spending tokens on task decomposition and tool selection, while 99.2% of final-plan
generation steps producezerothinking tokens. The model actually uses only ∼230 thinking tokens
on average, well below the 1024 ceiling, and raising the ceiling does not redirect where that thinking
happens. The hardest part of the task, synthesizing 20+ tool outputs into a coherent multi-day itinerary
under interacting constraints, is executed with no reasoning at all, regardless of budget. PIVOT
addresses this distributional problem rather than the quantity problem: its plan–inspect–evolve–verify
schedule triggers reasoning at multiple points along the trajectory. After tool returns, before plan
assembly, and before the final answer, thinking is allocated precisely where synthesis and verification
happen, not only at the upfront planning step.
Figure 5:Thinking-budget abla-
tion.Scaling the extended-thinking
budget from 1024 to 3072 tokens
does not improve performance on
either backbone or benchmark.
Error Analysis: Why trajectory-grounded feedback mat-
ters.We further analyze why prior correction mechanisms
underperform on long-horizon planning. Both SE-Agent [ 7]
and AgentDebug [27] attempt to improve failed trajectories,
but their feedback signals are misaligned with the structure of
the errors. SE-Agent relies on a World-State-Model (WSM)
critic whose usefulness decreases as the baseline agent becomes
stronger. On weaker backbones such as Claude-4.5-Haiku and
Sonnet, WSM precision on Travel Planning reaches 0.99, since
most trajectories contain genuine errors and critique is often
well-founded. However, as baseline quality improves, precision
drops to 0.97 on Claude-4.5-Opus and collapses to 0.49 on
Claude-4.6-Opus, where nearly half of WSM-flagged trajecto-
ries are already correct. These false positives often arise from
hallucinated constraint checks, such as claiming that a hotel
lacks a required amenity when the selected hotel satisfies it, or
flagging a coupon as incorrectly applied when the task explic-
itly requested it. The subsequent correction pass compounds
this noise: among 95 false-positive cases on Claude-4.6-Opus
Travel Planning, 40 produce strictly worse composite scores
after correction and none improve. A common failure mode is
over-editing, where a local issue, such as a suboptimal flight, triggers a broad re-plan that fixes one
element while breaking attraction coverage, meal timing, or transfer feasibility elsewhere.
AgentDebug fails for the opposite reason: its feedback is too rigid. It scores each step against a
fixed ontology of four modules and eight error types, then selects an error ID from this grid. This
taxonomy is poorly matched to long-horizon planning, where failures are compositional, constraint-
dependent, and often task-specific. Across 874 evaluated cases, 57.3% of diagnoses collapse into the
broadest category (planning, subtype constraint_ignorance), and 60.4% blame step 1.
Because Phase 1 flags 54% of all step–error pairs as erroneous, Phase 2 is forced to select from a
noisy candidate set. Moreover, the classifier cannot express repairs outside its vocabulary: 53% of
correction strings merely restate the predicted label, while most prescriptive corrections reduce to
coarse parameter changes for early tool calls. As a result, the retry agent receives a verdict rather
than an actionable repair plan, often reproducing the original failure or restarting from a coarse edit
that discards correct work, breaking 8% of already-passing cases and yielding only a +0.02 average
gain with18.1%regressions.
These two failure modes clarify the advantage of PIVOT. SE-Agent can be overly permissive
and induce unnecessary edits, while AgentDebug can be overly discretized and unable to express
trajectory-specific repairs. PIVOT instead grounds feedback in the observed discrepancy between
the planned trajectory and the execution trace. IN S P E C Tidentifies where support for the current
plan breaks, EV O L V Erewrites only the unsupported suffix, and VE R I F Ychecks the final trajectory
against the original constraints. This avoids both unconstrained over-correction and fixed-taxonomy
diagnosis, enabling localized repair without discarding validated parts of the trajectory.
8

## Page 9

Ablation study on importance of PIVOT components.Table 2 reports the effect of disabling
each PIVOT stage while keeping the remaining stages active. The largest degradation occurs when
removing VE R I F Y(−13.3 avg.), followed by PL A N(−11.4 avg.), EV O L V E(−10.8 avg.), and
IN S P E C T(−4.2 avg.). This suggests that PIVOT’s gains do not come solely from better upfront
planning; instead, reasoning at the end of the trajectory, where the draft plan is checked against the
original constraints, contributes the most. The effect persists even for stronger backbones: disabling
VE R I F Yreduces Opus 4.6 by12.9 points, indicating that even highly capable models can silently emit
constraint violations unless explicitly prompted to validate them. This finding is consistent with the
thinking-allocation analysis above. Vanilla extended thinking spends most of its reasoning budget on
the opening turn and produces little or no thinking during plan synthesis or final answering. VE R I F Y
places reasoning precisely at this under-covered stage, where constraint violations are most likely
to surface in the final output. Its benefit therefore comes from improved reasoning coverage rather
than simply adding more reasoning tokens. PL A Nand EV O L V Ealso remain important, especially for
weaker backbones, showing that both strong trajectory initialization and discrepancy-guided repair
are necessary for robust performance.
Q3-235B Haiku 4.5 Sonnet 4.5 Opus 4.5 Opus 4.6 Avg. Drop
ReAct [22]− − − −28.33 35.23 53.07 62.86 86.02 —PIVOT
! ! ! !39.81 53.69 59.82 76.45 89.27 —
✗! ! !15.34 51.51 54.69 62.79 77.89↓11.36
!✗! !29.40 50.18 58.93 71.51 87.92↓4.22
! !✗!20.57 50.62 54.74 61.28 77.92↓10.78
! ! !✗18.78 44.74 52.03 60.62 76.43 ↓13.29
Table 2:Ablation of PIVOT stages on Travel Benchmark.Each row removes one component (✗)
while keeping others (!); Avg. Drop reports the mean degradation relative to the full pipeline. All
stages contribute to performance, confirming that PIVOT operates as a tightly coupled refinement
loop rather than a set of independent modules. VERIFYhas the largest impact, highlighting the
importance of final constraint validation, followed by PLANand EVOLVE, which govern trajectory
initialization and repair. INSPECTshows a smaller but consistent contribution, indicating that even
imperfect discrepancy signals remain useful for guiding updates.
Limitations.Long-horizon agentic planning remains constrained by challenges that PIVOT mitigates
but not fully resolving. First, context degradation can cause early instructions to lose salience as
intermediate reasoning and tool outputs accumulate; while PIVOT re-evaluates trajectories and applies
final verification, it still operates within the model’s finite context window. Second, despite PIVOT
directly addressing error cascades through discrepancy-driven repairs, its monotonic acceptance
criterion cannot guarantee recovery from severely flawed initial trajectories. Third, backward
discrepancy analysis reduces myopic decision-making via surrogate credit assignment, but repair
quality remains bounded by the underlying model reasoning capacity. Fourth, the framework depends
on evaluable feedback: while textual gradients densify sparse signals, they cannot recover missing
information in retrieval-bottlenecked settings such as GAIA. Finally, iterative refinement introduces
additional latency and token cost; although this overhead is generally moderate in practice, PIVOT is
not cost-free. Extending the framework to dynamic environments remains an important direction, as
its mutable trajectory loop is suited to adaptation but not yet been systematically validated.
5 Conclusions
We present PIVOT, a self-supervised trajectory optimization framework for addressing plan–execution
misalignment in LLM-based agents. By treating trajectories as optimizable objects, PIVOT leverages
execution feedback and natural-language surrogate gradients to align planned intent with realized
behavior, while its monotonic acceptance criterion prevents degradation across refinement iterations.
Empirical results across DeepPlanning and GAIA show that PIVOT is especially effective in long-
horizon, constraint-driven settings where failures stem from recoverable plan–execution discrepancies.
On DeepPlanning, human-in-the-loop (HITL) feedback provides an upper-bound regime, yielding
up to 94.3% normalized improvement over the strongest baseline, while the autonomous variant
remains a strong no-supervision alternative and closely matches HITL in several settings ( 13.9%
vs. 14.0% on Travel Planning with Qwen3-235B). On GAIA, gains are more bounded by retrieval
9

## Page 10

quality, but PIVOT still improves task success in open-domain, tool-augmented scenarios. Across
model families, trajectory-level refinement complements backbone scaling while remaining efficient,
requiring up to 3–5× fewer tokens than competing refinement methods. Overall, our findings position
discrepancy-driven trajectory optimization as a principled mechanism for improving reliability in
autonomous agents, particularly when constraint satisfaction, execution feedback, and iterative repair
are central to task success.
10

## Page 11

References
[1] B. Bohnet, P.-A. Kamienny, H. Sedghi, D. Gorur, P. Awasthi, A. Parisi, K. Swersky, R. Liu, A. Nova,
and N. Fiedel. Enhancing llm planning capabilities through intrinsic self-critique.arXiv preprint
arXiv:2512.24103, 2025.
[2] M. Cemri, M. Z. Pan, S. Yang, L. A. Agrawal, B. Chopra, R. Tiwari, K. Keutzer, A. Parameswaran,
D. Klein, K. Ramchandran, et al. Why do multi-agent llm systems fail?arXiv preprint arXiv:2503.13657,
2025.
[3] J. Chen, H. Li, J. Yang, Y . Liu, and Q. Ai. Enhancing llm-based agents via global planning and hierarchical
execution.arXiv preprint arXiv:2504.16563, 2025.
[4] D. Deshpande, V . Gangal, H. Mehta, J. Krishnan, A. Kannappan, and R. Qian. Trail: Trace reasoning and
agentic issue localization.arXiv preprint arXiv:2505.08638, 2025.
[5] Z. Gou, Z. Shao, Y . Gong, Y . Shen, Y . Yang, N. Duan, and C. W. Critic: Large language models can
self-correct with tool-interactive critiquing. InInternational Conference on Learning Representations
(ICLR), 2024.
[6] J. Gu, X. Jiang, Z. Shi, H. Tan, X. Zhai, C. Xu, W. Li, Y . Shen, S. Ma, H. Liu, S. Wang, K. Zhang, Y . Wang,
W. G. Gao, L. Ni, and J. Guo. A survey on llm-as-a-judge.arXiv preprint arXiv:2411.15594, 2024.
[7] Y . Guo, J. Lin, H. Wang, Y . Han, S. Hu, Z. Ni, L. Wang, and M. Chen. Se-agent: Self-evolution trajectory
optimization in multi-step reasoning with llm-based agents. InThe Thirty-ninth Annual Conference on
Neural Information Processing Systems, 2025.
[8] Y . Guo, J. Lin, H. Wang, Y . Han, S. Hu, Z. Ni, L. Wang, M. Chen, H. Liu, R. Chen, Y . He, D. Jiang, B. Jiao,
and C. Hu. Se-agent: Self-evolution trajectory optimization in multi-step reasoning with llm-based agents.
arXiv preprint arXiv:2508.02085, 2025.
[9] Z. Ji, D. Wu, P. Ma, Z. Li, and S. Wang. Testing and understanding erroneous planning in llm agents
through synthesized user inputs.arXiv preprint arXiv:2404.17833, 2024.
[10] Z. Jiang, F. F. Xu, L. Gao, Z. Sun, Q. Liu, J. Dwivedi-Yu, Y . Yang, J. Callan, and G. Neubig. Active
retrieval augmented generation. InProceedings of the 2023 Conference on Empirical Methods in Natural
Language Processing (EMNLP), 2023.
[11] A. Kumar and W. W. Cohen. Localizing and correcting errors for llm-based planners.arXiv preprint
arXiv:2602.00276, 2026.
[12] T. Ma, Y . Chen, V . Anand, A. Cornacchia, A. R. Faustino, G. Liu, S. Zhang, H. Luo, S. A. Fahmy, Z. A.
Qazi, et al. Maestro: Multi-agent evaluation suite for testing, reliability, and observability.arXiv preprint
arXiv:2601.00481, 2026.
[13] A. Madaan, N. Tandon, P. Gupta, S. Hallinan, L. Gao, S. Wiegreffe, U. Alon, N. Dziri, S. Prabhumoye,
Y . Yang, S. Gupta, B. P. Majumder, K. Hermann, S. Welleck, A. Yazdanbakhsh, and P. Clark. Self-refine:
Iterative refinement with self-feedback.arXiv preprint arXiv:2303.17651, 2023.
[14] G. Mialon, C. Fourrier, T. Wolf, Y . LeCun, and T. Scialom. Gaia: a benchmark for general ai assistants. In
The Twelfth International Conference on Learning Representations, 2023.
[15] S. Nayak, A. M. Orozco, M. Ten Have, V . Thirumalai, J. Zhang, D. Chen, A. Kapoor, E. Robinson,
K. Gopalakrishnan, J. Harrison, B. Ichter, A. Mahajan, and H. Balakrishnan. Llamar: Long-horizon
planning for multi-agent robots in partially observable environments.arXiv preprint arXiv:2407.10031,
2024.
[16] A. Rana and G. Kumar. Model-first reasoning llm agents: Reducing hallucinations through explicit problem
modeling.arXiv preprint arXiv:2512.14474, 2025.
[17] N. Shinn, F. Cassano, E. Berman, A. Gopinath, K. Narasimhan, and S. Yao. Reflexion: Language agents
with verbal reinforcement learning.arXiv preprint arXiv:2303.11366, 2023.
[18] Y . Y . Sung, H. Kim, and D. Zhang. Verila: A human-centered evaluation framework for interpretable
verification of llm agent failures.arXiv preprint arXiv:2503.12651, 2025.
[19] B. Tarun, H. Du, D. Kannan, and E. F. Gehringer. Human-in-the-loop systems for adaptive learning using
generative ai.arXiv preprint arXiv:2508.11062, 2025.
11

## Page 12

[20] Q. Team. Qwen3 technical report, 2025.
[21] X. Wang, C. Li, Z. Wang, F. Bai, H. Luo, J. Zhang, N. Jojic, E. P. Xing, and Z. Hu. Promptagent: Strategic
planning with language models enables expert-level prompt optimization.arXiv preprint arXiv:2310.16427,
2023.
[22] S. Yao, J. Zhao, D. Yu, T. Nguyen, I. Shafran, D. Bhatia, and Y . Cao. React: Synergizing reasoning and
acting in language models. InInternational Conference on Learning Representations (ICLR), 2023.
[23] M. Yuksekgonul, F. Bianchi, J. Boen, S. Liu, Z. Huang, C. Guestrin, and J. Zou. Textgrad: Automatic
"differentiation" via text.URL https://arxiv.org/abs/2406.07496, 2024.
[24] G. Zhang, J. Wang, J. Chen, W. Zhou, K. Wang, and S. Yan. Agentracer: Who is inducing failure in the
llm agentic systems?arXiv preprint arXiv:2509.03312, 2025.
[25] S. Zhang, M. Yin, J. Zhang, J. Liu, Z. Han, J. Zhang, B. Li, C. Wang, H. Wang, Y . Chen, et al. Which
agent causes task failures and when? on automated failure attribution of llm multi-agent systems.arXiv
preprint arXiv:2505.00212, 2025.
[26] Y . Zhang, S. Jiang, R. Li, J. Tu, Y . Su, L. Deng, X. Guo, C. Lv, and J. Lin. Deepplanning: Benchmarking
long-horizon agentic planning with verifiable constraints.arXiv preprint arXiv:2601.18137, 2026.
[27] K. Zhu, Z. Liu, B. Li, M. Tian, Y . Yang, J. Zhang, P. Han, Q. Xie, F. Cui, W. Zhang, et al. Where llm
agents fail and how they can learn from failures.arXiv preprint arXiv:2509.25370, 2025.
12

## Page 13

A Prompts and Flow Discussion
A.1 Stage 1: PLAN - Structured Planning Before Action
Intuitive Analogy: Imagine a chef who just received an order for a multi-course dinner. Before
touching any ingredients, they sit down with pen and paper: What dishes are we making? What
ingredients do we need? Which stations handle what? What’s the cooking sequence? What if the
oven breaks or we’re out of a key ingredient? This is what PLAN forces the AI agent to do before it
touches any tool.
Core Mechanism:
• Forces the agent to produce an explicit, structured plan before any tool is called
• The plan must include: goal restatement, information needs, tool selection per step, step
dependencies, and failure contingencies
• Serves as the "blueprint" that all subsequent stages reference
PLAN BEFORE ACT:
Before using any tools, you MUST first output a plan inside
<plan>...</plan> tags:
1. Restate the user’s goal in one sentence.
2. List each piece of information you need to gather, as
numbered steps.
3. For each step, note which tool you intend to use and what
a successful result looks like.
4. Identify dependencies between steps (e.g., "step 3
requires the URL from step 2").
5. Note any potential failure modes (e.g., "if the search
returns no results, try alternative query X").
After the plan, begin executing it step by step. Refer back to
your plan as you go.
Trigger Condition: Appended to the system prompt. Runs once, at the very start of the task.
Design Rationale: Research consistently shows that LLMs perform better when they "think before
acting." Without an explicit planning step, agents tend to call tools reactively, grabbing whatever
seems relevant in the moment rather than following a coherent strategy. By requiring the agent to
articulate its plan upfront (including failure contingencies), we front-load the strategic thinking that
prevents downstream waste.
A.2 Stage 2: INSPECT — Periodic Reflection Checkpoints
Intuitive Analogy: Now the chef is actively cooking. After finishing each course, they pause to taste
and assess: "Did this sauce reach the right consistency? Am I still on schedule for the next course?
Does this plating match my original vision, or do I need to adjust my approach for the remaining
dishes?" They don’t wait until all courses are plated—they catch issues while there’s still time to
correct course.
Core Mechanism:
• Executes plans step-by-step in the actual environment
• Tracks discrepancies between what was planned and what actually happened
• Identifies constraint violations, infeasible actions, and early warning signs
• Generates structured diagnostic reports documenting exactly where and why things went
wrong
13

## Page 14

• Proactively detects problems rather than waiting for catastrophic failures
REFLECT AFTER TOOL:
Before your next action, briefly answer these three questions
in 1-2 sentences each:
1. RESULT CHECK: Did the tool return what you expected? If
not, what went wrong?
2. PLAN STATUS: Which steps of your plan are complete, and
which remain?
3. REVISION: Do you need to change your approach for the
remaining steps? If a search failed, what alternative
query or source could you try?
Then continue executing your plan.
Trigger Condition: Injected automatically every 3 tool-call rounds during execution.
Design Rationale: Without periodic reflection, agents exhibit "tunnel vision", they keep executing
the original plan even when early results clearly indicate it won’t work. The 3-round interval is a
deliberate balance: frequent enough to catch problems early, but not so frequent that it slows down
execution with excessive self-reflection. The three-question structure (Result →Status →Revision)
mirrors the observe-orient-decide loop used in real-world decision-making frameworks.
A.3 Stage 3: EVOLVE — Adaptive Plan Revision on Failure
Intuitive Analogy: The chef discovers mid-service that a key ingredient is spoiled. Rather than just
trying to salvage that same ingredient or make the dish anyway, they step back to diagnose: Why
won’t this work? Is there a completely different ingredient that provides the same flavor profile?
Could I pivot to an entirely different dish that uses what’s available? And if no substitution works,
what’s the best menu I can serve with the ingredients I do have? EVOLVE forces the agent through
this same discipline: diagnose root cause, pivot to a fundamentally different strategy, or gracefully
degrade—but never blindly retry the same failed approach.
Core Mechanism:
• Triggered specifically when a tool call fails or returns useless results
• Forces the agent to diagnose the root cause, propose a completely different approach (not
just a retry), and identify a fallback if no alternative exists
• Capped at 3 invocations per task to prevent infinite retry loops
PLAN REVISION:
Your last tool call did not return useful results. Before
retrying, you MUST:
1. DIAGNOSE: Why did it fail? (wrong query terms? page not
accessible? data not in this source?)
2. ALTERNATIVE: Name a completely different approach to get
this information. Do not repeat the same query.
3. FALLBACK: If no alternative source exists, what partial
answer can you construct from what you already have?
Then execute your revised approach.
Trigger Condition: injected when a tool call fails, max 3 times
Design Rationale: The most common failure pattern in AI agents is the "retry loop": when a
search fails, the agent tries the same query (or a trivially different one) repeatedly. EVOLVE breaks
14

## Page 15

this pattern by explicitly prohibiting repeated queries and requiring the agent to name a completely
different approach. The 3-invocation cap is a cost-control mechanism: if three fundamentally different
approaches all fail, the information likely isn’t accessible, and the agent should construct the best
partial answer it can.
A.4 Stage 4: VERIFY — Final Quality Gate
Intuitive Analogy: All courses are plated and ready. Before sending them to the dining room, the
chef does a final inspection against the original order: ✓Are all requested courses present? ✓Are
dietary restrictions honored? ✓Is the presentation what was promised? ✓Is the temperature correct
for each dish? If anything’s missing or wrong, they fix it now. If something’s impossible with
available ingredients, they communicate it clearly to the customer. VERIFY is the agent’s version of
this final quality check before serving.
Core Mechanism:
• Runs once, just before the agent produces its final answer
• Forces the agent to re-read the original question and check its answer against every stated
requirement
• Each requirement is explicitly marked as✓satisfied or✗not satisfied
• Any gaps are either fixed on the spot or transparently acknowledged
• Addresses root causes identified through backward analysis, and then fundamentally recon-
structs plans rather than just patching individual steps
• Produces plans that are more executable and constraint-aware
FINAL VERIFICATION:
Before giving your final answer, verify it:
1. Re-read the original question. List every requirement it
contains.
2. Check your answer against each requirement. Mark each as
✓satisfied or✗not satisfied.
3. For any✗items: do you have enough information to fix
it? If yes, fix it now. If no, note what’s missing and
give your best answer with what you have.
4. Check formatting: does your answer match the requested
format exactly? (number, string, list, etc.)
Do NOT discard your work. Only correct specific errors you
identified above.
Trigger Condition: injected once before the final answer
Design Rationale: Even after good planning, diligent execution, and adaptive recovery, agents
frequently produce answers that miss one or more requirements from the original question, especially
when the question is multi-part or has specific formatting requirements. VERIFY acts as a safety net
that catches these last-mile errors. The instruction "Do NOT discard your work" is critical: without it,
agents sometimes over-correct by throwing away good work and starting over, which is wasteful and
often produces worse results.
B Motivation: Backward Error Analysis for Agent Debugging
A central challenge in improving LLM-based agents is the opacity of their failure modes. When
an agent produces an incorrect answer after a multi-step reasoning trajectory involving tool calls,
web searches, and intermediate computations, it is rarely obvious where the reasoning went wrong.
The final output is a single point of failure, but the causal chain leading to it may span dozens of
steps. Without a principled method for localizing errors within this chain, practitioners are left with
15

## Page 16

two unsatisfying options: (1) manually inspecting lengthy execution traces, which does not scale,
or (2) blindly re-running the agent, which tends to reproduce the same errors. We draw inspiration
from back-propagation in neural network training, where the gradient of the loss is propagated
backward through the computation graph to identify which parameters contributed most to the error.
Analogously, we treat the agent’s reasoning trace as a directed computation graph: a sequence of
decisions, tool invocations, and intermediate conclusions. We propagate the error signal (an incorrect
final answer) backward through this graph to identify the root cause: the earliest decision point where
a different choice would have plausibly led to a correct outcome.
The backward analysis (PIVOT with HITL) revealed a consistent pattern: the most common failure
mode is not missing information but ignored information. This diagnosis points to a structural
problem: the agent’s thinking budget is allocated in the wrong place. The agent loop is a simple
cycle:
call LLM→execute tool calls→when no more tool calls, extract plan→return
There are no intermediate steps between “done gathering data” and “generate plan” where
the agent cross-references its collected evidence against constraints. More importantly, the same four
failure archetypes recur systematically across tasks and models:
• Absence of planning: agents dive into tool calls without structuring their approach, producing
disorganized trajectories with redundant searches and missed dependencies.
• Ignored evidence: agents retrieve all necessary data but fail to cross-reference it during
output assembly — the dominant failure mode at 44–47% of cases.
• Retry loops: when a tool call fails, agents retry the same query rather than pivoting to a
fundamentally different strategy.
• Silent constraint dropping: agents satisfy most requirements but silently drop one or two
constraints, producing partially correct answers indistinguishable from fully correct ones.
This observation directly motivates the PIVOT framework: rather than diagnosing and repairing
failures post-hoc, we embed the lessons from backward analysis as proactive guardrails that prevent
the failures from arising in the first place. Each PIVOT stage maps to one of the archetypes above:
PLAN addresses absence of planning, INSPECT catches ignored evidence mid-execution, EVOLVE
breaks retry loops, and VERIFY eliminates silent constraint dropping at the final gate.
C Sampled PIVOT Trajectories (without HITL feedback)
C.1 Example 1 — id_16: Hangzhou→Shaoxing day trip (0.375→1.000)
Query: Solo traveler, earliest train, cheapest Home Inn, must eat near Bazhi Bridge at a restaurant
with waiting area service.
What the baseline got wrong: Scheduled an attraction visit before opening hours (Lu Xun’s
Hometown at 08:23, opens 08:30), missed the “waiting area service” restaurant tag requirement near
Bazhi Bridge, and had an incomplete Day 2 itinerary.
What PIVOT audit caught: The <thinking> block systematically listed all constraints as a checklist,
flagged the opening-hours violation (“Lu Xun’s Hometown opens at 08:30, not 08:23!”), identified
the missing restaurant tag constraint, and noted the incomplete Day 2. It then rebuilt the plan from
scratch, fixing all three issues to achieve a perfect 1.000 composite score.
C.2 Example 2 — id_62: Harbin→Beijing 5-day trip (0.125→0.875)
Query: 3 travelers, direct Airbus flight (cheapest), highest-rated 3-star hotel, 2 rooms, must eat at
“Pebbles Courtyard Mexican Restaurant,” restaurant with private room near Beihai Park.
What the baseline got wrong: Selected a Boeing flight instead of Airbus (violating the aircraft
manufacturer constraint), missed the must-eat restaurant entirely, scheduled a meal outside restaurant
operating hours, and had cost calculation errors across the budget summary.
What PIVOT audit caught: The <thinking> block enumerated all available flights and marked each
Boeing option with ✗, identifying CZ6217 (Airbus 320, ¥520) as the correct cheapest Airbus direct
flight. It flagged the restaurant operating hours violation and the missing must-eat restaurant. The
16

## Page 17

Algorithm 1PIVOT: PLAN–INSPECT–EVOLVE–VERIFY Trajectory Refinement
Require:taskt, pool sizeM, refinement stepsR
1:T 0 ← {PL A N(t)}M
m=1
2:foreachτ∈ T 0 do
3:Executeτ→ˆτ
4: bL(τ)←IN S P E C T(ˆτ, τ, t)
5:end for
6:τ (0) ←arg min≺
τ∈T0
bL(τ)
7:τ ⋆ ←τ (0)
8: bL⋆ ← bL(τ(0))
9:forr= 0toR−1do
10:Executeτ (r) →ˆτ(r)
11:( bL(r), g(r))←IN S P E C T(ˆτ(r), τ(r), t)
12:ifSuccess(ˆτ (r), t)then
13:returnVE R I F Y(τ (r), t)
14:end if
15:τ ′ ←EV O L V E(ˆτ(r), τ(r), g(r))
16:Executeτ ′ →ˆτ′
17:( bL′,_)←IN S P E C T(ˆτ′, τ′, t)
18:if bL′ ≺ bL(r) then
19:τ (r+1) ←τ ′
20: bL(r+1) ← bL′
21:else
22:τ (r+1) ←τ (r)
23: bL(r+1) ← bL(r)
24:end if
25:end for
26:τ ⋆ ←τ (R)
27:returnVE R I F Y(τ⋆, t)
rebuilt plan corrected the flight, included Pebbles Courtyard, and fixed the budget — recovering 6 of
8 commonsense dimensions.
C.3 Example 3 — id_58: Shenzhen→Beijing 4-day trip (0.250→0.938)
Query: 4 travelers, return flight arriving 11:00–15:00, 3-star hotel with gym, birthday dinner near
Sanlitun Taikoo Li, budget meal near Tiananmen.
What the baseline got wrong: Selected return flight ZH1393 arriving at 10:10 AM (before the 11:00
AM requirement), reused bluefrog restaurant on two different days, and routed through Shichahai
without allocating actual visit time.
What PIVOT audit caught: Flagged 4 critical failures — return flight time violation (“✗ FAILED —
arrives at 10:10 AM, BEFORE 11:00”), restaurant diversity violation (“✗ — I used bluefrog twice”),
incomplete attraction coverage ("✗ — Shichahai never actually visited"). The rebuilt plan switched
to flight DZ6210 (arrives 11:55 AM), replaced the duplicate restaurant, and properly scheduled
Shichahai.
C.4 Example 4 — id_19: Ningbo→Suzhou 2-day trip (0.312→0.938)
Query: 4 travelers, most affordable direct train, hotel ¥330–360/night, 2 rooms, highest-rated
restaurant near Suzhou Museum, restaurant with outdoor seating near Suzhou Museum.
What the baseline got wrong: Selected a hotel (Four Points by Sheraton Kunshan) outside the
¥330–360 price range, had no activity diversity (insufficient attractions), and violated itinerary
structure rules.
What PIVOT audit caught: Identified the hotel price constraint violation and the missing outdoor-
seating restaurant tag. The rebuilt plan selected a correctly-priced hotel, added diverse attractions,
and matched both restaurant requirements near Suzhou Museum.
17

## Page 18

C.5 Example 5 — id_32: Harbin→Beijing 3-day trip (0.188→0.812)
Query: Solo traveler, first-class train both ways, 3-star hotel with SPA, restaurant with waiting area
near Shichahai, cheapest restaurant near Tsinghua University.
What the baseline got wrong: Failed to find the cheapest restaurant near Tsinghua University (used
wrong entity), had route consistency errors (teleportation between locations), violated business hours,
and miscalculated costs.
What PIVOT audit caught: Flagged “✗ CRITICAL FAILURE — Meal 2: Near Tsinghua University,
MUST pick LOWEST average cost per person” and identified the wrong restaurant selection. The
rebuilt plan queried the correct cheapest option (Tsinghua University Nanyuan Restaurant) and fixed
route continuity.
C.6 Example 6 — id_36: Wuhan→Nanjing 3-day trip (0.188→0.812)
Query: 3 travelers, earliest direct train, 4-star hotel with TV screen mirroring, 2 rooms, budget ≥
¥5,500, restaurant with online queue near Nanjing Eye, must eat at “New Bailu.”
What the baseline got wrong: Selected a hotel without TV screen mirroring capability (Atour Hotel
instead of one with the required service), had unreasonable visit durations, and violated business
hours.
What PIVOT audit caught: Flagged " ✗ CRITICAL FAILURE — Accommodation: TV screen
mirroring" and "I chose the WRONG hotel." The rebuilt plan selected a hotel with the correct amenity
and restructured the daily schedule with proper durations.
D Sampled PIVOT Trajectories (with HITL feedback)
D.1 Example 1— id_49: Shanghai→Enshi 4-day trip (0.312→0.875)
What the baseline got wrong: Completely omitted “Canyon Flavor Restaurant” — a must-eat
restaurant explicitly requested by the user — resulting in 0% personalized score.
What backward analysis diagnosed: The agent queried query_restaurant_details(“Canyon Flavor
Restaurant”) and got “not found,” then gave up entirely instead of trying alternative name variations
(“Grand Canyon Flavor Restaurant”) or coordinate-based searches. The backward analysis identified
this as an INFORMATION error at the tool-retry level. The correction pass used alternative search
strategies to locate and include the restaurant.
D.2 Example 2 — id_18: Hangzhou→Shaoxing 2-day trip (0.188→0.875)
Query: Train departing 6:00–7:00 AM, cheapest hotel with swimming pool, must visit Keyan Scenic
Area and free attractions, must eat at a specific local restaurant.
What the baseline got wrong: 5 cascading violations — train price mismatch (¥16 vs actual ¥520),
Keyan visited at 17:35 (closes 17:00), only 50 minutes at Keyan (requires 2.5–4 hours), unreasonable
transfer gaps, and missing Shaoxing Museum.
What backward analysis diagnosed: Root cause type INFORMATION. The agent’s train query
returned truncated results with only one option (G7711 at 16:30). The agent fabricated train G7713 at
06:40 which didn’t exist in the results, causing a late arrival that compressed the entire Day 1 schedule
into an impossible timeline. The correction pass (8 new tool calls) re-queried trains, restructured both
days, and added the missing museum.
D.3 Example 3 — id_42: Urumqi→Shanghai 4-day trip (0.125→0.750)
Query: Return flight arriving 14:00–18:00, 4-star hotel, must visit The Bund and Yu Garden,
restaurant with birthday set menu.
What the baseline got wrong: Only generated 3 days instead of 4, selected return flight arriving at
21:40 (outside the 14:00–18:00 window), and missed the birthday restaurant requirement.
What backward analysis diagnosed: Root cause type INFORMATION. The agent retrieved the
return flight but failed to validate the arrival time against the user’s explicit 14:00–18:00 constraint. It
accepted the first result without checking alternatives. The correction pass (3 new tool calls) found a
compliant flight and rebuilt the 4-day itinerary.
18

## Page 19

D.4 Example 4 — id_82: Wuhan→Nanjing 6-day trip (0.125→0.750)
Query: 6-day trip (Nov 12–17), train both ways, 3-star hotel, must visit historical sites, restaurant
near Confucius Temple.
What the baseline got wrong: Malformed last-day structure, insufficient attractions on final day,
business hours violations, and timing gaps throughout.
What PIVOT with HITL analysis diagnosed: Root cause type PLANNING. The agent correctly
counted 5 nights but failed to convert this into 6 calendar days of itinerary. The Nov 12–17 span
requires 6 daily schedules, but the agent generated fewer, leaving the final day incomplete. The
correction pass (10 new tool calls) rebuilt the full 6-day structure with proper daily closure.
D.5 Example 5 — id_77: Ningbo→Zhengzhou 5-day trip (0.062→0.688)
Query: Hotel ¥250–280/night, must visit Yellow River scenic area, earliest train, restaurant near Erqi
Square.
What the baseline got wrong: Selected a hotel outside the ¥250–280 price range, had invalid
transportation segments, missing meals, attractions visited outside operating hours, and incorrect visit
durations.
What PIVOT with HITL analysis diagnosed: Root cause type REASONING. The agent did not
enforce the user’s explicit numerical hotel price constraint — treating “between 250 and 280 yuan per
night” as a guideline rather than a hard boundary. The correction pass (23 new tool calls) re-queried
hotels with strict price filtering and rebuilt the entire itinerary from scratch.
D.6 Example 6 — id_117: Chongqing→Zhengzhou 7-day trip (0.312→0.875)
Query: Highest-rated Home Inn, must visit Shaolin Temple and Yellow River, restaurant with private
room near Erqi Square, budget-friendly meal near Zhengzhou East Station.
What the baseline got wrong: Did not book the highest-rated Home Inn (4.9⋆) despite retrieving it,
missed required attractions, and failed personalized restaurant constraints.
What PIVOT with HITL analysis diagnosed: Root cause type REASONING → INFORMATION.
The agent was “data-sufficient but logic-deficient” - it gathered all necessary information through
tool calls but did not apply systematic filtering when assembling the plan. It retrieved the 4.9⋆ hotel
but selected a lower-rated one; it found the required attractions but didn’t include them all. The
correction pass (17 new tool calls) applied proper selection logic to the already-gathered data.
E Experiment Implementation Details
E.1 Experiments Compute Resource
All the experiments related to the LLM inference are conducted by Amazon Bedrock platform. For
the data analysis part, we used the Amazon EC2 g5.48xlarge instance, with 8 NVIDIA A10G GPUs
(24 GB memory each). All experiments are run through the AWS Bedrock Converse API with
temperature 0.0 for deterministic decoding. When extended thinking is enabled (Claude 4.5 Haiku
/ Sonnet / Opus and Claude 4.6 Opus), temperature is set to 1.0 as required by the Claude API.
Qwen3-235B-A22B does not support extended thinking and is always run at temperature0.0.
E.2 Definition of Tools in GAIA Evaluation
GAIA tasks are solved by an agent that interacts with four tools through the Bedrock Converse
toolConfig interface. The same tool set is used for every method compared in Section 4, so
differences in task accuracy reflect reflection strategy rather than tool affordance. Each tool is exposed
to the model with a JSON schema specifying its name, a one-sentence description, and a typed input
object; the agent selects tools via the native tool-use protocol.
Tool Catalog.
•web_search(query: str) . Executes a Google query and returns the top result snippets.
Falls back to a DuckDuckGo lite scrape if Google returns no parseable snippets. Output is limited
to the first five results.
19

## Page 20

•web_fetch(url: str) . Retrieves a URL with a 20s timeout, strips navigation, scripts,
and style tags from HTML, and returns the visible text. Content is truncated to 15,000 characters.
•read_file(filename: str) . Reads an attachment associated with the task. PDFs, Word
(.docx), Excel (.xlsx), PowerPoint (.pptx), CSV , JSON, Python, and plain-text files are
returned as text. Images (.png, .jpg) are returned as a vision-model caption. Audio (.mp3) is
returned as an ASR transcription.
•python_exec(code: str) . Executes Python code in an isolated subprocess with a 30-
second wall-clock limit; standard output (and any stderr) is returned, truncated to 10,000 char-
acters. Pre-installed libraries include pandas, numpy, json, math, re, collections, and
itertools.
Scope.This tool set is deliberately minimal. It does not include a browser, a multi-hop retriever, or
any specialist tool (e.g., PubMed search, symbolic solver). Every method, ours and the baselines,
operates under the same ceiling on what information can be recovered from the environment. Accuracy
differences attributed to PIVOT therefore reflect better use of the available tools, not additional
affordances.
20

## Page 21

NeurIPS Paper Checklist
1.Claims
Question: Do the main claims made in the abstract and introduction accurately reflect the
paper’s contributions and scope?
Answer: [Yes]
Justification: The main claims made in the abstract and introduction are supported by the
algorithm contribution we made in Section 3 and the evaluation results in Section 4.
Guidelines:
• The answer [N/A] means that the abstract and introduction do not include the claims
made in the paper.
• The abstract and/or introduction should clearly state the claims made, including the
contributions made in the paper and important assumptions and limitations. A [No] or
[N/A] answer to this question will not be perceived well by the reviewers.
• The claims made should match theoretical and experimental results, and reflect how
much the results can be expected to generalize to other settings.
• It is fine to include aspirational goals as motivation as long as it is clear that these goals
are not attained by the paper.
2.Limitations
Question: Does the paper discuss the limitations of the work performed by the authors?
Answer: [Yes]
Justification: The limitation is thoroughly discussed in final part of Section 4.3.
Guidelines:
• The answer [N/A] means that the paper has no limitation while the answer [No] means
that the paper has limitations, but those are not discussed in the paper.
• The authors are encouraged to create a separate “Limitations” section in their paper.
• The paper should point out any strong assumptions and how robust the results are to
violations of these assumptions (e.g., independence assumptions, noiseless settings,
model well-specification, asymptotic approximations only holding locally). The authors
should reflect on how these assumptions might be violated in practice and what the
implications would be.
• The authors should reflect on the scope of the claims made, e.g., if the approach was
only tested on a few datasets or with a few runs. In general, empirical results often
depend on implicit assumptions, which should be articulated.
• The authors should reflect on the factors that influence the performance of the approach.
For example, a facial recognition algorithm may perform poorly when image resolution
is low or images are taken in low lighting. Or a speech-to-text system might not be
used reliably to provide closed captions for online lectures because it fails to handle
technical jargon.
• The authors should discuss the computational efficiency of the proposed algorithms
and how they scale with dataset size.
• If applicable, the authors should discuss possible limitations of their approach to
address problems of privacy and fairness.
• While the authors might fear that complete honesty about limitations might be used by
reviewers as grounds for rejection, a worse outcome might be that reviewers discover
limitations that aren’t acknowledged in the paper. The authors should use their best
judgment and recognize that individual actions in favor of transparency play an impor-
tant role in developing norms that preserve the integrity of the community. Reviewers
will be specifically instructed to not penalize honesty concerning limitations.
3.Theory assumptions and proofs
Question: For each theoretical result, does the paper provide the full set of assumptions and
a complete (and correct) proof?
Answer: [N/A]
21

## Page 22

Justification: [N/A]
Guidelines:
• The answer [N/A] means that the paper does not include theoretical results.
• All the theorems, formulas, and proofs in the paper should be numbered and cross-
referenced.
• All assumptions should be clearly stated or referenced in the statement of any theorems.
• The proofs can either appear in the main paper or the supplemental material, but if
they appear in the supplemental material, the authors are encouraged to provide a short
proof sketch to provide intuition.
• Inversely, any informal proof provided in the core of the paper should be complemented
by formal proofs provided in appendix or supplemental material.
• Theorems and Lemmas that the proof relies upon should be properly referenced.
4.Experimental result reproducibility
Question: Does the paper fully disclose all the information needed to reproduce the main ex-
perimental results of the paper to the extent that it affects the main claims and/or conclusions
of the paper (regardless of whether the code and data are provided or not)?
Answer: [Yes]
Justification: All the experiment implementation details, including the exact system prompt,
are provided in Section 4, Appendix A, and Appendix E.
Guidelines:
• The answer [N/A] means that the paper does not include experiments.
• If the paper includes experiments, a [No] answer to this question will not be perceived
well by the reviewers: Making the paper reproducible is important, regardless of
whether the code and data are provided or not.
• If the contribution is a dataset and/or model, the authors should describe the steps taken
to make their results reproducible or verifiable.
• Depending on the contribution, reproducibility can be accomplished in various ways.
For example, if the contribution is a novel architecture, describing the architecture fully
might suffice, or if the contribution is a specific model and empirical evaluation, it may
be necessary to either make it possible for others to replicate the model with the same
dataset, or provide access to the model. In general. releasing code and data is often
one good way to accomplish this, but reproducibility can also be provided via detailed
instructions for how to replicate the results, access to a hosted model (e.g., in the case
of a large language model), releasing of a model checkpoint, or other means that are
appropriate to the research performed.
• While NeurIPS does not require releasing code, the conference does require all submis-
sions to provide some reasonable avenue for reproducibility, which may depend on the
nature of the contribution. For example
(a) If the contribution is primarily a new algorithm, the paper should make it clear how
to reproduce that algorithm.
(b) If the contribution is primarily a new model architecture, the paper should describe
the architecture clearly and fully.
(c) If the contribution is a new model (e.g., a large language model), then there should
either be a way to access this model for reproducing the results or a way to reproduce
the model (e.g., with an open-source dataset or instructions for how to construct
the dataset).
(d) We recognize that reproducibility may be tricky in some cases, in which case
authors are welcome to describe the particular way they provide for reproducibility.
In the case of closed-source models, it may be that access to the model is limited in
some way (e.g., to registered users), but it should be possible for other researchers
to have some path to reproducing or verifying the results.
5.Open access to data and code
Question: Does the paper provide open access to the data and code, with sufficient instruc-
tions to faithfully reproduce the main experimental results, as described in supplemental
material?
22

## Page 23

Answer: [No]
Justification: We cannot release the code framework utilized for our experiments due to
legal approval constraints, however we can provide full details on reproducibility, including
data setup, model configuration and prompt setup utilized in the supplementary material /
appendix.
Guidelines:
• The answer [N/A] means that paper does not include experiments requiring code.
• Please see the NeurIPS code and data submission guidelines (https://neurips.
cc/public/guides/CodeSubmissionPolicy) for more details.
• While we encourage the release of code and data, we understand that this might not
be possible, so [No] is an acceptable answer. Papers cannot be rejected simply for not
including code, unless this is central to the contribution (e.g., for a new open-source
benchmark).
• The instructions should contain the exact command and environment needed to run to
reproduce the results. See the NeurIPS code and data submission guidelines (https:
//neurips.cc/public/guides/CodeSubmissionPolicy) for more de-
tails.
• The authors should provide instructions on data access and preparation, including how
to access the raw data, preprocessed data, intermediate data, and generated data, etc.
• The authors should provide scripts to reproduce all experimental results for the new
proposed method and baselines. If only a subset of experiments are reproducible, they
should state which ones are omitted from the script and why.
• At submission time, to preserve anonymity, the authors should release anonymized
versions (if applicable).
• Providing as much information as possible in supplemental material (appended to the
paper) is recommended, but including URLs to data and code is permitted.
6.Experimental setting/details
Question: Does the paper specify all the training and test details (e.g., data splits, hyperpa-
rameters, how they were chosen, type of optimizer) necessary to understand the results?
Answer: [Yes]
Justification: All the experiment implementation details, including the exact system prompt,
are provided in Section 4, Appendix A, and Appendix E.
Guidelines:
• The answer [N/A] means that the paper does not include experiments.
• The experimental setting should be presented in the core of the paper to a level of detail
that is necessary to appreciate the results and make sense of them.
• The full details can be provided either with the code, in appendix, or as supplemental
material.
7.Experiment statistical significance
Question: Does the paper report error bars suitably and correctly defined or other appropriate
information about the statistical significance of the experiments?
Answer: [No]
Justification: All experiments are run through the AWS Bedrock Converse API with tem-
perature 0.0 (and 1.0 only when extended thinking is mandated by the API), which makes
decoding close to deterministic and yields stable results across repeated invocations. The
benchmarks also carry non-trivial API cost: each full sweep over five backbones, two bench-
marks, and multiple reflection methods consumes a large number of long-context tool-use
calls, and our compute budget does not permit repeated full runs. Finally, the baselines we
compare against (Self-Critique [1], AgentDebug [27], SE-Agent [8]) do not report error bars
either, and we follow their evaluation protocol for fair comparison.
We report the temperature setup for API inference in Appendix E.
Guidelines:
23

## Page 24

• The answer [N/A] means that the paper does not include experiments.
• The authors should answer [Yes] if the results are accompanied by error bars, confidence
intervals, or statistical significance tests, at least for the experiments that support the
main claims of the paper.
• The factors of variability that the error bars are capturing should be clearly stated (for
example, train/test split, initialization, random drawing of some parameter, or overall
run with given experimental conditions).
• The method for calculating the error bars should be explained (closed form formula,
call to a library function, bootstrap, etc.)
• The assumptions made should be given (e.g., Normally distributed errors).
• It should be clear whether the error bar is the standard deviation or the standard error
of the mean.
• It is OK to report 1-sigma error bars, but one should state it. The authors should
preferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesis
of Normality of errors is not verified.
• For asymmetric distributions, the authors should be careful not to show in tables or
figures symmetric error bars that would yield results that are out of range (e.g., negative
error rates).
• If error bars are reported in tables or plots, the authors should explain in the text how
they were calculated and reference the corresponding figures or tables in the text.
8.Experiments compute resources
Question: For each experiment, does the paper provide sufficient information on the com-
puter resources (type of compute workers, memory, time of execution) needed to reproduce
the experiments?
Answer: [Yes]
Justification: We report it in Appendix E.
Guidelines:
• The answer [N/A] means that the paper does not include experiments.
• The paper should indicate the type of compute workers CPU or GPU, internal cluster,
or cloud provider, including relevant memory and storage.
• The paper should provide the amount of compute required for each of the individual
experimental runs as well as estimate the total compute.
• The paper should disclose whether the full research project required more compute
than the experiments reported in the paper (e.g., preliminary or failed experiments that
didn’t make it into the paper).
9.Code of ethics
Question: Does the research conducted in the paper conform, in every respect, with the
NeurIPS Code of Ethicshttps://neurips.cc/public/EthicsGuidelines?
Answer: [Yes]
Justification: [N/A]
Guidelines:
• The answer [N/A] means that the authors have not reviewed the NeurIPS Code of
Ethics.
• If the authors answer [No], they should explain the special circumstances that require a
deviation from the Code of Ethics.
• The authors should make sure to preserve anonymity (e.g., if there is a special consid-
eration due to laws or regulations in their jurisdiction).
10.Broader impacts
Question: Does the paper discuss both potential positive societal impacts and negative
societal impacts of the work performed?
Answer: [Yes]
24

## Page 25

Justification: We report it in the final paragraph in Section 1.
Guidelines:
• The answer [N/A] means that there is no societal impact of the work performed.
• If the authors answer [N/A] or [No], they should explain why their work has no societal
impact or why the paper does not address societal impact.
• Examples of negative societal impacts include potential malicious or unintended uses
(e.g., disinformation, generating fake profiles, surveillance), fairness considerations
(e.g., deployment of technologies that could make decisions that unfairly impact specific
groups), privacy considerations, and security considerations.
• The conference expects that many papers will be foundational research and not tied
to particular applications, let alone deployments. However, if there is a direct path to
any negative applications, the authors should point it out. For example, it is legitimate
to point out that an improvement in the quality of generative models could be used to
generate Deepfakes for disinformation. On the other hand, it is not needed to point out
that a generic algorithm for optimizing neural networks could enable people to train
models that generate Deepfakes faster.
• The authors should consider possible harms that could arise when the technology is
being used as intended and functioning correctly, harms that could arise when the
technology is being used as intended but gives incorrect results, and harms following
from (intentional or unintentional) misuse of the technology.
• If there are negative societal impacts, the authors could also discuss possible mitigation
strategies (e.g., gated release of models, providing defenses in addition to attacks,
mechanisms for monitoring misuse, mechanisms to monitor how a system learns from
feedback over time, improving the efficiency and accessibility of ML).
11.Safeguards
Question: Does the paper describe safeguards that have been put in place for responsible
release of data or models that have a high risk for misuse (e.g., pre-trained language models,
image generators, or scraped datasets)?
Answer: [N/A]
Justification: [N/A]
Guidelines:
• The answer [N/A] means that the paper poses no such risks.
• Released models that have a high risk for misuse or dual-use should be released with
necessary safeguards to allow for controlled use of the model, for example by requiring
that users adhere to usage guidelines or restrictions to access the model or implementing
safety filters.
• Datasets that have been scraped from the Internet could pose safety risks. The authors
should describe how they avoided releasing unsafe images.
• We recognize that providing effective safeguards is challenging, and many papers do
not require this, but we encourage authors to take this into account and make a best
faith effort.
12.Licenses for existing assets
Question: Are the creators or original owners of assets (e.g., code, data, models), used in
the paper, properly credited and are the license and terms of use explicitly mentioned and
properly respected?
Answer: [Yes]
Justification: We have properly cited the datasets and models that we used in the paper.
Guidelines:
• The answer [N/A] means that the paper does not use existing assets.
• The authors should cite the original paper that produced the code package or dataset.
• The authors should state which version of the asset is used and, if possible, include a
URL.
25

## Page 26

• The name of the license (e.g., CC-BY 4.0) should be included for each asset.
• For scraped data from a particular source (e.g., website), the copyright and terms of
service of that source should be provided.
• If assets are released, the license, copyright information, and terms of use in the package
should be provided. For popular datasets, paperswithcode.com/datasets has
curated licenses for some datasets. Their licensing guide can help determine the license
of a dataset.
• For existing datasets that are re-packaged, both the original license and the license of
the derived asset (if it has changed) should be provided.
• If this information is not available online, the authors are encouraged to reach out to
the asset’s creators.
13.New assets
Question: Are new assets introduced in the paper well documented and is the documentation
provided alongside the assets?
Answer: [N/A]
Justification: [N/A]
Guidelines:
• The answer [N/A] means that the paper does not release new assets.
• Researchers should communicate the details of the dataset/code/model as part of their
submissions via structured templates. This includes details about training, license,
limitations, etc.
• The paper should discuss whether and how consent was obtained from people whose
asset is used.
• At submission time, remember to anonymize your assets (if applicable). You can either
create an anonymized URL or include an anonymized zip file.
14.Crowdsourcing and research with human subjects
Question: For crowdsourcing experiments and research with human subjects, does the paper
include the full text of instructions given to participants and screenshots, if applicable, as
well as details about compensation (if any)?
Answer: [N/A]
Justification: [N/A]
Guidelines:
• The answer [N/A] means that the paper does not involve crowdsourcing nor research
with human subjects.
• Including this information in the supplemental material is fine, but if the main contribu-
tion of the paper involves human subjects, then as much detail as possible should be
included in the main paper.
• According to the NeurIPS Code of Ethics, workers involved in data collection, curation,
or other labor should be paid at least the minimum wage in the country of the data
collector.
15. Institutional review board (IRB) approvals or equivalent for research with human
subjects
Question: Does the paper describe potential risks incurred by study participants, whether
such risks were disclosed to the subjects, and whether Institutional Review Board (IRB)
approvals (or an equivalent approval/review based on the requirements of your country or
institution) were obtained?
Answer: [N/A]
Justification: [N/A]
Guidelines:
• The answer [N/A] means that the paper does not involve crowdsourcing nor research
with human subjects.
26

## Page 27

• Depending on the country in which research is conducted, IRB approval (or equivalent)
may be required for any human subjects research. If you obtained IRB approval, you
should clearly state this in the paper.
• We recognize that the procedures for this may vary significantly between institutions
and locations, and we expect authors to adhere to the NeurIPS Code of Ethics and the
guidelines for their institution.
• For initial submissions, do not include any information that would break anonymity (if
applicable), such as the institution conducting the review.
16.Declaration of LLM usage
Question: Does the paper describe the usage of LLMs if it is an important, original, or
non-standard component of the core methods in this research? Note that if the LLM is used
only for writing, editing, or formatting purposes and doesnotimpact the core methodology,
scientific rigor, or originality of the research, declaration is not required.
Answer: [Yes]
Justification: We leverage the LLMs to understand the execution and do the text-gradient
within the proposed algorithm framework, as we detailed elaborated in Section 3.
Guidelines:
• The answer [N/A] means that the core method development in this research does not
involve LLMs as any important, original, or non-standard components.
• Please refer to our LLM policy in the NeurIPS handbook for what should or should not
be described.
27
