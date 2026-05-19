# Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP - Extracted Text

- Source note: [[Context, Reasoning, and Hierarchy - A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP]]
- Source PDF: `assets/Context, Reasoning, and Hierarchy - A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP.pdf`
- Extracted: 2026-05-18
- Extractor: pypdf
- Pages: 29
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

Context, Reasoning, and Hierarchy: A Cost-Performance Study of
Compound LLM Agent Design in an Adversarial POMDP
Igor Bogdanov
igorbogdanov@cmail.carleton.ca
Carleton University
Ottawa, Ontario, Canada
Chung-Horng Lung
chlung@sce.carleton.ca
Carleton University
Ottawa, Ontario, Canada
Thomas Kunz
tkunz@sce.carleton.ca
Carleton University
Ottawa, Ontario, Canada
Jie Gao
jie.gao6@carleton.ca
Carleton University
Ottawa, Ontario, Canada
Adrian Taylor
Adrian.Taylor@forces.gc.ca
Defence R&D Canada
Ottawa, Ontario, Canada
Marzia Zaman
Marzia@cistel.com
Cistel Technology
Ottawa, Ontario, Canada
Abstract
Deploying compound LLM agents in adversarial, partially observ-
able sequential environments requires navigating several interact-
ing design dimensions: (1) what the agent sees, (2) how it reasons,
and (3) how tasks are decomposed across components. Yet prac-
titioners lack guidance on which design choices improve perfor-
mance versus merely increase inference costs. We present a con-
trolled study of compound LLM agent design in CybORG CAGE-2,
a cyber defense environment modeled as a Partially Observable
Markov Decision Process (POMDP). Reward is non-positive, so
all configurations operate in a failure-mitigation mode and errors
compound over time. Our evaluation spans five model families,
six models, and twelve configurations (3,475 episodes) with token-
level cost accounting. We systematically vary context representa-
tion (raw observations vs. a deterministic, programmatic environ-
ment state-tracking layer with compressed history), deliberation
(self-questioning, self-critique, and self-improvement tools, with
optional chain-of-thought prompting), and hierarchical decompo-
sition (monolithic ReAct vs. delegation to specialized sub-agents).
We find that: (1) Programmatic state abstraction delivers the largest
returns per token spent (RPTS), improving mean return by up to
76% over raw observations. (2) Distributing deliberation tools across
a hierarchy degrades performance relative to hierarchy alone for all
five model families, reaching up to 3.4×worse mean return while
using 1.8-2.7×more tokens. We call this destructive interaction pat-
tern adeliberation cascade. (3) Hierarchical decomposition without
deliberation tools achieves the best absolute performance for most
models, and context engineering is generally more cost-effective
than deliberation. These findings suggest a design principle for
structured adversarial POMDPs: invest in programmatic infrastruc-
ture and clean task decomposition rather than deeper per-agent
reasoning, as these strategies can interfere when combined.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
ACM CAIS ’26, San Jose, CA, USA
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2415-2/26/05
https://doi.org/10.1145/3786335.3813149
CCS Concepts
•Computing methodologies →Artificial intelligence;Partially-
observable Markov decision processes;Multi-agent systems;
Intelligent agents;•Security and privacy →Network secu-
rity.
Keywords
compound AI systems, LLM agents, hierarchical agent architectures,
tool-augmented language models, context engineering, inference-
time scaling, token efficiency, cost–performance trade-offs, adver-
sarial POMDP, autonomous cyber defense, catastrophic failures
ACM Reference Format:
Igor Bogdanov, Chung-Horng Lung, Thomas Kunz, Jie Gao, Adrian Tay-
lor, and Marzia Zaman. 2026. Context, Reasoning, and Hierarchy: A Cost-
Performance Study of Compound LLM Agent Design in an Adversarial
POMDP. InACM Conference on AI and Agentic Systems (ACM CAIS ’26),
May 26–29, 2026, San Jose, CA, USA.ACM, New York, NY, USA, 29 pages.
https://doi.org/10.1145/3786335.3813149
1 Introduction
Practitioners build compound LLM agents by composing three
design dimensions:context engineering[ 6] (what the agent sees),
deliberation(reasoning depth), andhierarchical decomposition(task
distribution). While often assumed to be additive, these choices
interact destructively in adversarial, partially observable sequential
environments. We present a controlled empirical study of these
interactions within a compound LLM agent defending a network in
the CybORG CAGE-2 POMDP. By systematically ablating context,
reasoning, and hierarchy across five model families and six models,
we measure both task performance and token cost, revealing that
what the agent seesis a more reliable lever thanhow deeply it thinks:
deterministic programmatic context yields large gains at near-zero
marginal cost, whereas distributing deliberation across a hierarchy
often degrades performance while inflating token consumption. We
term this failure mode adeliberation cascade. While bounded hier-
archy often achieves the bestabsolutereturn, context engineering
delivers the bestreturns per token, making it the most cost-effective
first investment.
The Empirical Gap.Three gaps motivate this work. (1) Multi-
agent research emphasizestopology(wiring) over internal agent
design [9], leaving the interaction between internal configuration
arXiv:2605.16205v1  [cs.AI]  15 May 2026

## Page 2

ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA Bogdanov et al.
and hierarchy underexplored. (2) While context engineering is
widely endorsed [6], controlled evidence on the cost-performance
trade-offs of specific context components in sequential settings
is limited. (3) The deliberation and multi-agent literatures remain
disconnected, and we show that combining them can introduce
failure modes invisible to either in isolation.
Research Question.Our central question is:which compound-
agent design dimensions deliver performance gains per to-
ken invested, and how do they interact when composed
across a multi-agent hierarchy?We decompose this into:RQ1
(Context): value of programmatic abstraction vs. raw observations;
RQ2(Reasoning): impact of deliberation tools in monolithic vs.
hierarchical agents; andRQ3(Composition): when decomposition
helps or hurts.
Contributions.We present four contributions at the intersection
of architectural design and system optimization. (1)Cost-effective
context engineering.We show that a deterministic state-tracking
layer reduces cumulative penalty by 52-76% relative to raw obser-
vations for four of six models, dominating raw observation context
configurations at near-zero marginal cost. (2)Identification of
deliberation cascades.We demonstrate that enabling deliberation
tools across a hierarchy degrades performance in all six models
(up to3 .4×worse return) while doubling token costs, producing
cascading uncertainty. (3)Three-axis Pareto analysis.We con-
duct a controlled ablation of context, reasoning, and hierarchy
across five model families (72 pairs, 3,475 episodes), constructing
cost-performance frontiers that consistently place programmatic
context on the efficient frontier. (4)Multi-model validation.We
show that while qualitative effects (context helps, distributed rea-
soning hurts) are robust, quantitative magnitudes vary, validating
multi-model evaluation as essential for compound AI design.
Scope.This paper is a static architectural design-space study: it
asks what compound-agent architecture to build at deployment
time, before any runtime adaptation. We scope our claims to struc-
tured adversarial POMDPs.
2 Background & Problem Definition
We study compound LLM agents operating in an adversarial, par-
tially observable sequential decision problem and evaluate designs
jointly on (1) task return and (2) token cost. The agent architecture
and the multi-dimensional ablation study mirror our engineering
ladder for solving CAGE-2 with an LLM agent: we began with
raw environment observations, then introduced deterministic state
tracking and context engineering to make the observations action-
able, decomposed the task into a hierarchy as context grew, and
finally added deliberation tools to facilitate better decision-making
within each agent. This section defines the environment and objec-
tives, specifies the execution scaffold and initialization scope, and
establishes tokens as the cost primitive.
CybORG CAGE-2.We evaluate on CybORG CAGE-2 [ 19, 22], an
adversarial POMDP modelling network defense. A defender pro-
tects a 13-host network against an attacker that follows a scripted,
non-adaptive multi-stage kill chain [ 8] over 𝑇=30steps. The at-
tacker does not respond to the defender’s actions, but host attributes,
processes, and the progression of the kill chain vary stochastically
across runs. The defender chooses from five actions (Monitor,
Analyse,Remove,Restore,Decoy) with asymmetric costs. Re-
ward 𝑟𝑡 ≤0penalizes compromise and intervention; we report
episodic return 𝐺= Í𝑇
𝑡=1 𝑟𝑡 (closer to zero is better). Partial ob-
servability requires sustaining situational awareness under noisy
indicators. (See Appendix H for full details.)
Configuration-Driven ReAct Scaffold.Agents follow a ReAct [ 24]
loop, iterating between deliberation and tool use until emitting
an answer. We separate a reusable ReAct Agent engine (I/O, pars-
ing) from declarative YAML "personality" configurations (prompts,
tools). This separation ensures reproducibility and allows architec-
tural variants to be defined as configuration changes rather than
code modifications.
Knowledge-Free Initialization.To isolate architectural effects from
domain engineering, we impose a knowledge-free scope at 𝑡=0.
Agents receive only a one-sentence role instruction and a compact
action reference table. No network topology, attacker kill-chain
details, host-value assignments, or defense heuristics are provided,
and the prompt never mentions the environment by name. Perfor-
mance gains arise from model internal knowledge, runtime context,
and deliberation. Models’ internal knowledge may include infor-
mation about CAGE-2 acquired during pre-training. To minimize
the consequences of this exposure, no benchmark-specific cues are
provided at runtime. However, influence from pre-training may
still be present. All LLMs receive an identical set of prompts and
tools.
Tokens as Cost Primitive.We use total number of tokens per
episode (prompt + completion) as the primary cost metric, map-
ping directly to billed usage and correlating with latency. We use
raw token counts because they do not depend on provider pricing.
Appendix F reports prompt/completion splits by model and con-
figuration for pricing-weighted reinterpretation. We instrument
all LLM calls, aggregating prompt and completion tokens across
the Planner and sub-agents. Pairing return with token cost enables
our central evaluative question: which design choices deliver the
largestreturns per token spent(RPTS), and which inflate the
cost.
3 Compound Agent System Design
Our system couples a deterministic backbone with an LLM deci-
sion engine and spans four layers (Table 1). (1) Thehierarchy
layerallows a Planner to delegate tasks to Analyst and Action-
Chooser sub-agents via strict JSON contracts. (2) Adeterministic
infrastructure layermaintains a primitive environment model,
history of interactions, and validates actions without model calls.
(3) Thecontext engineering layercomprises injections that ex-
tend user prompts and connect environment model state and ac-
tion history by converting them into structured summaries like
{network_status}. (4) Thereasoning layerfollows the ReAct
pattern [24], optionally executing deliberation within ReAct loop.
Decision Cycle.At each of the 𝑇=30steps, an Agent Coordinator
receives the raw CybORG observation, updates the deterministic
environment model, and inserts the chosen context bundle into

## Page 3

Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA
Table 1: System Modularity and Configuration Layers. The agent architecture is built on four functional pillars, ordered from
the system’s top-level decision structure down to its internal reasoning mechanisms.
System Layer Core Aspects Responsibility Configurability
1. Hierarchy Planner, Analyst, Action-
Chooser, JSON Contracts
Distributes tasks: Planner (decides), Analyst (as-
sesses), ActionChooser (ranks).
Role definitions, tool availability, and
I/O contracts in YAML.
2. Infrastructure Env Model, State Machine, His-
tory Log, Action Validator
Maintains deterministic belief state (status, his-
tory, decoys) and validates actions via regex.
Fixed deterministic backbone (Python).
3. Context{network_status} ,
{history},{observation}
Transforms raw observations into structured
summaries and compressed logs.
YAML templates define which context
blocks are injected.
4. Reasoning ReAct Engine, Tools (Question,
Critique, Improve), CoT
Executes the reasoning loop, tool calls, and op-
tional deliberation steps.
Boolean flags toggle deliberation tools
and CoT injection.
the Planner prompt. It then startsa fresh step-level Planner
instance, validates the emitted action, retries on invalid outputs,
and submits the validated action to the environment (Figure 1).
Step-level instantiation ensures no hidden conversational state
accumulates across steps. All inter-step continuity is explicit in the
deterministic state structures and compiled context.
Reliability Mechanisms.In an adversarial sequential environ-
ment, every invalid action is a wasted step during which the attacker
advances unopposed. We therefore treat reliability as load-bearing
infrastructure implementing the following: (1)Action validation
and retry:the Planner’s output is parsed against the CybORG
action schema using regex-based validation; invalid outputs trig-
ger up to three retries with the parsing error injected as feedback.
(2)Safe fallback:if all retries fail, the system defaults toMonitor,
preserving observability without risking a misapplied intervention.
(3)Sub-agent output validation:the ActionChooser’s JSON un-
dergoes tiered parsing (direct parse →normalization →optional
repair prompt). Any repair calls are included in token accounting.
These mechanisms ensure format compliance. They are designed
to minimize harm when invoked.
3.1 Layer 1: Hierarchical Decomposition
The system can run either as amonolithic Plannerthat directly
emits an environment action, or as a fixed three-agent hierarchy
consistent with the centralized multi-agent system (MAS) topology
described by Kim et al. [9], in which an orchestrator coordinates
bounded sub-agents through structured communication. The three-
agent split separates three functions: strategic decision-making,
localized perception, and bounded action candidate ranking to
accommodate increasing context size. ThePlannerretains sole
authority over environment actions but may delegate to two sub-
agents whose outputs are advisory. TheAnalystassesses a single
host by comparing its current state against the effective baseline
and returns a structured JSON assessment (status, anomalies, sus-
pected compromise). TheActionChooserreceives the Planner’s
situational summary and, when available, theAnalyst’sreport,
returning a ranked list of up to three candidate actions with confi-
dence labels in strict JSON. Sub-agents cannot issue environment
actions. The purpose of this split is to simplify the Planner’s deci-
sion by constraining what each sub-agent produces. All three agents
share the same engine-personality separation logic, ensuring the
observed hierarchy effects reflect role decomposition.
3.2 Layer 2: Deterministic Environment Model
To provide in-context situational awareness, the system maintains
a fully deterministic environment model that transforms raw Cy-
bORG observations into structured network state description and
action history. Critically, this model is computed exclusively from
the agent’s own observations and past actions. The system stores
environmentbaseline stateupon the first observation and creates a
host-indexed data structure. This layer embeds domain-informed
observation processing. The engineering choices that form the
model shape what the agent perceives. Although the layer pre-
scribes no action-selection decisions (no threat rubrics, no host
priorities, and no response heuristics), it still carries inductive bias
that may influence the agent’s reasoning.
Dynamic Environment Model.The model data structure com-
prises a dictionary where each host obtains astatus: { baseline,
changed, unknown, analysed at step𝑛 }, and ahistory record,
an ordered, arrow-delimited record of all actions applied to each
host (e.g.,Analyse→Remove→Restore ). This concise single-host
record provides the Planner with additional intervention memory
without requiring it to parse a full transcript.
Model update mechanism.On each step, the model compares the
current observation against the savedbaseline stateusing signature-
based comparison of stable fields (process and service identity),
ignoring volatile fields (e.g., transient connections) that produce
false positives [8]. The system deterministically updates host status
based on the comparison and prior actions (Restore →baseline ;
Remove →unknown ;Analyse →analysed at step𝑛 ). Deployed
decoys are registered as baseline overrides so that expected decoy
processes are incorporated into the effective baseline and only
genuinely new processes remain visible as anomalous.
3.3 Layer 3: Context Engineering
Context Injections.Three context injections feed the Planner’s
initial prompt viaplaceholders: {observation}, {history}, and
{network_status}. {observation} is the raw CybORG dictionary:
a verbose, noisy dump of per-host process tables, network con-
nections, and service states that the LLM must parse unaided.

## Page 4

ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA Bogdanov et al.
Figure 1: End-to-end system architecture. The deterministic
layer (left) compiles structured context from CybORG obser-
vations and assembles the agent prompt. The Planner (right)
executes a ReAct loop, optionally delegating to Analyst and
ActionChooser sub-agents, before emitting a validated action
back to the environment.
{network_status} is a compact JSON list of only non-baseline
hosts, each annotated with status (changed, unknown, analysed),
recency (Current vs. Past), and the action history applied to that
host. It collapses to a single sentence when all hosts are healthy.
{history} is a compressed action log that folds consecutive quiet
steps (Monitor, no state change) into ranges while preserving
full detail for intervention steps, controlling prompt growth over
the 30-step episode. {history} thus serves a dual function: it pro-
vides temporal context for intervention sequencing and supplies
the Planner’s own prior reasoning through programmatically ex-
tracted justifications, creating a compressed log of past decisions
with explanations.
The Initial User Prompt.The initial user prompt template itself
contributes nothing beyond a step counter and a closing ques-
tion. All environment understanding comes from the content in-
jected into theseplaceholders. Each sub-agent also receives a
role-specific initial prompt and context components provided by
the Planner. The Analyst receives the target hostname and is asked
to assess the host’s situation and the ActionChooser receives a sit-
uational JSON from the Planner containing the target host, threat
description, severity level, and relevant context from prior steps.
Sub-agents see neither the full network status nor the episode
history. The Planner decides what to provide, enforcing limited
context per role. All structured injections are fully deterministic
and their cost is limited to the marginal tokens they add to the
prompt (examples in Appendix B).
3.4 Deliberation Tools
To further increase decision-making capabilities each ReAct agent
in the hierarchy supports four cumulative levels of deliberation.
The deliberation tools implement a self-questioning, self-critique,
Table 2: Experimental overview, models evaluated, and eval-
uation hyperparameters.
Component Description
Models: 5 familiesGrok, Llama, Devstral, Qwen, Gemini
Axis 1: Context6 configs varying{obs},{hist},{net}
Axis 2: Deliberation 4 levels: question, critique, improve, COT
Axis 3: HierarchyDelegation vs. delegation + deliberation
Default Contexthist+net: network + history
Scale72 exp.; 3,475 episodes; 283.9M tokens
Models Grok, Llama, Devstral, Qwen, G2.5FL,
G3FP (6 models from 5 families; episode
counts in Appendix I)
Eval Config
Instances per config 10 (standard)
Runs per instance 5
Episode length 30 steps
Decoding Deterministic (greedy, temp=0)
Metrics
Mean episode return𝐺= Í𝑇
𝑡=1 𝑟𝑡 ≤0; closer to zero is better
Total tokens/episode Prompt + completion; main cost primitive
RPTS Returns per token spent;
Standard deviation Episode return variability
Validity guard Replication across 5 families, 6 Models
Reference RewardsOfficial CAGE-2 Leaderboard [22]
Top DRL agent−3.47
Simple heuristic−58.83
Random Agent−154.06
Sleeping (no-op)−218.65
and self-refinement cycle inspired by Self-Refine [ 13] and self-
interrogation techniques [ 15]; the CoT injection follows Wei et
al. [23] and Kojima et al. [10]. Unlike cross-episode reflection (e.g.,
Reflexion [18]), all deliberation occurs within a single step and
carries no memory to future steps.
The following threedeliberation toolsand an explicit chain-of-
thought (CoT) prompt injection are executed as additional ReAct
turns inside one loopwithin a single environment step: (1)question:
the agent questions its initial reasoning before committing to an
action [15]. (2)critique(includes #1): the agent generates an explicit
critique of its response [13]. (3)improve(includes #1-2): the agent
revises its action in light of the critique [13]. (4)COT(includes #1-
3): an explicit chain-of-thought instruction [10, 23] is added to the
system prompt, providing reasoning scaffolding on top of the tools.
4 Experimental Methodology
This section describes the models, evaluation protocol, metrics, and
controlled ablation design that produce the evidence base for our
findings. Table 2 provides an at-a-glance summary.
Models.We evaluate six models from five contemporary model
families (Table 2) accessed via OpenRouter (Grok, Llama, Devstral,
Qwen) and Google Cloud Gemini API. We adopt a full-coverage
design: all six models are evaluated on all 12 configurations across
three experimental axes (72 unique model-configuration pairs). This
safeguards against reliance on single-model results. All models use

## Page 5

Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA
deterministic decoding (temperature 0). All models receive identical
prompt templates and tool definitions. No per-model tuning is
performed.
Evaluation Protocol.Each configuration is evaluated over mul-
tiplecontainerized agent instancesand multiplerunsper instance.
Each run is launched with a unique seed and fresh agent state. The
standard allocation is10instances ×5runs = 50episodes per pair.
G3FP uses a reduced 25-episode budget. Several G2.5FL/Qwen con-
figs use extended batches (75-100) to resolve uncertainty on key
comparisons. These allocation differences do not affect qualitative
conclusions, which are validated across all six models (Appendix I).
Step-level fresh instantiation ensures token accounting is precise
and isolated.
Three-Axis Design with Shared Anchor configuration.The experi-
mental design varies three axes. (1)Axis 1 (Context):6 monolithic
Planner configurations varying {obs}, {hist}, and {net} place-
holders (Table 1). (2)Axis 2 (Deliberation):4 cumulative levels
adding +question, +critique, +improve, and +COT tools to the
monolithic Planner. (3)Axis 3 (Hierarchy):2 configs: hier-base
(delegation to Analyst/ActionChooser, deliberation tools OFF) and
hier-delib (delegation + deliberation tools ON on all agents, CoT
inactive). Axes 2 and 3 share a common default, the hist+net con-
figuration (structured state + compressed history, no raw obs, no
deliberation, no delegation), which emerged from our engineering
ladder as the default compound-agent context setting. Axis 1 treats
this same configuration as one of six context variants.
Metrics and Statistical Reporting.We reportmean episode re-
turn(sum of rewards 𝑟𝑡 ≤0, closer to zero is better) as the primary
performance metric, alongsidetotal tokens per episode(prompt
+ completion) as the cost primitive. To jointly evaluate cost and
performance, we definereturns per token spent(RPTS) as the
mean return improvement over the observation-only baseline per
kilotoken consumed:
RPTS= 𝐺config −𝐺obs
KTokconfig
where 𝐺obs is the per-model mean return under the obs config-
uration and KTok is total tokens (thousands) per episode. RPTS
identifies which design choices deliver the largest gains per unit
of inference budget; negative values indicate configurations that
perform worse than unstructured observation alone. To capture tail
risk in this failure-mitigation setting, we reportstandard devia-
tionandcatastrophic failure rate(fraction of episodes <−150).
We adoptmulti-model replicationas the primary validity guard:
findings must replicate across the majority of the tested models.
Reward-Scale Reference Points.To ground the reward scale, we
reference the public CAGE-2 leaderboard [22] (30-step, B_line set-
ting). Reference reward values are listed in Table 2.
5 Results
All configurations follow the protocol and metrics defined in Sec-
tion 4. Table 3 presents the complete results matrix. Appendix E
reports additional statistical support, including 95% confidence in-
tervals for mean returns and paired difference confidence intervals
for key comparisons. These analyses preserve the qualitative di-
rection of the main findings while highlighting model-dependent
uncertainty. We organize the analysis into four subsections corre-
sponding to context (RQ1), the interaction between deliberation
and hierarchy (RQ2,RQ3), cost-performance frontiers, and robust-
ness.
5.1 Finding 1: Programmatic State Abstraction
Delivers the Largest Gains Per Token
Context engineering ablations reveal that a deterministic layer com-
piling observations into structured summaries delivers the largest
return on token investment.
Figure 2: Context engineering heatmap. Each cell shows
mean episode return for one model-context pair. Darker
shading indicates worse (more negative) returns. The obs+net
and hist+net(Planner-Only) columns are consistently strong
across models, whileobsalone is typically poor.
5.1.1 Raw observation alone is ineffective.Feeding unprocessed
CybORG dictionaries (obs) yields the worst or near-worst perfor-
mance for five of six models (leftmost column in Figure 2, Table 3).
Llama, Qwen, and G2.5FL fall below−214mean return, approaching
the Sleeping (no-op) agent (−219), with catastrophic failure rates
(<−150) reaching 96-98% (Figure 5). The raw format’s verbosity
and noise overwhelm the planner.
5.1.2 Programmatic backbone enables raw data utility.Augmenting
raw observations with the deterministic {network_status} layer
(obs→obs+net ) transforms performance without additional LLM
calls. Llama improves by 76% (−214.7 →−51.4), Qwen by 71%, and
Devstral by 53% (Table 3). The contrast is visible in Figure 2, where
theobs+netcolumn is consistently lighter thanobs.
5.1.3 Less-but-structured often beats more-but-unstructured.The
hist+net anchor configuration (structured state + history, no raw
obs) matches or beats the maximum-information obs+hist+net
for four models (Llama, G3FP, Qwen, Devstral). Adding raw obser-
vations to a clean state summary often dilutes the signal; removing
them improves Llama’s return by 44% (compare the hist+net and
obs+hist+netcolumns in Figure 2).
5.1.4 History provides complementary temporal context.Adding
compressed action history to raw observations (obs→obs+hist)
improves all six models, with Llama gaining 36% and Qwen 57%

## Page 6

ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA Bogdanov et al.
Table 3: Full results matrix. Mean episode return ±standard deviation (Ret ±SD) and kilotokens per episode (KTok = tokens
×103) across all 72 pairs, grouped by experimental axis. Underline ↑= best within axis; box ✓ = best overall per model; ↓= worst
within axis; box ↓= worst overall per model. The shared anchor configuration hist+net †serves as baseline for Axes 2 and 3.
Grok Llama Devstral Qwen G2.5FL G3FP
Config Ret±SD KTok Ret±SD KTok Ret±SD KTok Ret±SD KTok Ret±SD KTok Ret±SD KTok
Axis 1: Context
obs−98.4±70 17.7 −214.7±22↓ 8.8 −155.1±65↓ 22.2 −218.2±20↓ 10.3−214.7±23 68.1−96.8±71 8.0
obs+hist−89.9±75 34.6−137.4±63 19.2−133.9±86 26.4−93.4±72 19.0−172.9±69 125.2−76.3±67 15.4
obs+hist+net−81.9±78 33.5−102.6±73 30.6−85.3±77 25.1−69.0±53 18.7−147.8±70 ↑94.0−82.6±64 19.4
obs+net−47.0±40 ↑20.9 −51.4±20✓ 12.3−72.6±48 ↑15.4−63.1±26 11.4−200.0±41 79.4−113.7±68 9.0
network−86.3±31 20.2−68.7±37 13.0−93.3±44 14.9−109.4±59 10.6 −215.4±19↓ 94.4 −136.4±49↓ 7.9
hist+net† −112.9±79↓ 29.1−57.1±54 28.6−79.3±77 21.3−61.5±52 ↑16.4−208.7±39 81.7−52.0±58 ↑18.0
Axis 2: Deliberation (cumulative, on anchor †)
+question−66.5±62↓55.6−104.1±84↓84.1−53.9±42 60.4−92.3±69 45.7−206.2±37↓104.8−100.6±57↓30.7
+critique−44.9±45 74.7−93.4±77 97.8−62.8±58 106.9−93.6±67↓68.9 −128.6±95✓ 118.2−66.4±63 41.0
+improve−53.4±47 154.0−75.0±57 ↑115.3−80.6±70↓153.1−92.4±55 115.9−168.9±60 182.9−64.0±45 58.1
+COT−42.9±33 ↑144.5−100.8±70 131.3−40.9±31 ↑157.4−55.6±43 ↑162.4−157.0±70 225.7−29.9±20 ↑75.1
Axis 3: Hierarchy (on anchor †, structured context)
hier-base −24.0±27✓ 141.9−69.5±60 ↑87.7 −37.8±37✓ 97.0 −28.6±37✓ 79.6−183.1±62 ↑120.6 −16.1±3✓ 56.4
hier-delib−40.4±26↓364.1−108.0±74↓158.1−127.4±72↓257.7−30.1±33↓209.9−186.4±58↓270.5−23.6±12↓104.8
(Table 3). However, history’s marginal value depends on what other
context is present. When network status is already available, adding
history (obs+net vs. obs+hist+net) hurts four of six models (Ta-
ble 3), suggesting that {network_status} already encodes much
of the decision-relevant temporal signal.
5.2 Finding 2: Deliberation Destructively
Interferes with Hierarchy
The intersection of Axes 2 and 3 reveals the study’s central fail-
ure mode: deliberation that helps monolithic agents can degrade
hierarchical systems.
Figure 3: Deliberation cascade effect. Paired bars show mean
episode return for hier-base (dark) vs. hier-delib (light)
across six models. Degradation ratio annotated above each
pair. Mean return decreases for all six models.
5.2.1 Monolithic deliberation is model-dependent.Adding reason-
ing tools to the monolithic Planner produces model-dependent
effects (Table 3, Axis 2). Explicit chain-of-thought (+COT) is the best
deliberation level for four models (Grok, Devstral, Qwen, G3FP),
often improving on the anchor configuration. However, patterns
are non-monotonic, and stronger baselines (e.g., Llama on anchor
configuration) can be destabilized by additional turns. Token costs
scale steeply:+COTconsumes3-10×more tokens than the anchor.
5.2.2 Hierarchy without deliberation wins.The hier-base config-
uration (delegation only, no deliberation tools) achieves the best
or near-best absolute performance for four of six models (G3FP at
−16.1, Grok at −24.0, approaching the top published DRL result
of −3.47[ 2]; dark bars in Figure 3). The benefit comes fromtask
decomposition, bounded Analyst assessments and ActionChooser
rankings, rather than deeper deliberation. Llama is the exception, de-
grading by 22% compared to monolithichist+net (−57.1 →−69.5).
5.2.3 Deliberation cascade: the destructive interaction.Enabling de-
liberation tools on all hierarchical agents (hier-delib) decreases
mean return relative to hier-base for all six models (Table 3, Fig-
ure 3). Devstral worsens by3.37×(−37.8 →−127.4), Grok by1 .68×,
and Llama by1.55×, while token costs typically double (1.8-2.7×).
This compositional failure arises fromdeliberation cascade: inde-
pendent deliberation loops in the Analyst, ActionChooser, and Plan-
ner amplify uncertainty without an arbitration protocol. Moreover,
for four of six models (Grok, Devstral, Qwen, G3FP), hier-base
matches or outperforms the best monolithic deliberation at compa-
rable or lower token cost, achieving through task decomposition
what deliberation attempts through deeper reasoning. The degrada-
tion under hier-delib is not attributable to token overhead per se:
hier-base consumes comparable tokens to monolithic +COT (e.g.,
Grok: 141.9K vs. 144.5K) yet achieves substantially better returns
(−24.0vs.−42.9), confirming the loss is structural.
Mechanistic evidence: passivity amplification under distributed
deliberation.Auditing a matched episode trace from Devstral run
reveals a recurring pattern ofpassivity amplification: under
low-severity contexts with multiple active decoys, the delibera-
tive ActionChooser converges on "avoid redundant interventions"
and defers remediation until evidence becomes unambiguous. For

## Page 7

Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA
Figure 4: Cost-performance Pareto frontiers. Points shaped by axis (circles: context, triangles: deliberation, squares: hierarchy).
Context configurations occupy the low-cost efficient region;hier-delibis high-cost and dominated.
example: at step 24 User4 has been recently analyzed and instru-
mented with multiple decoys. The ActionChooser’s deliberation pri-
oritizes passive observing: Monitor (0.9) >Analyse User4 (0.8) >
Restore User4 (0.7). The Planner adopts the top recommendation.
On the next step, the Analyst flags severity=high with concrete
anomalies (unusual outbound traffic, unknown processes), and the
Planner overrides and restores User4, with a critical delay as in a
failure-mitigation regime, even single-step deferral prolongs high-
penalty states. Distributed deliberation overestimates immediate
"stability" cues under partial observability, yielding high-confidence
deferral until evidence becomes overwhelming (See Appendix G).
5.3 Finding 3: Context Engineering Dominates
the Cost-Performance Frontier
We construct per-model Pareto frontiers over all twelve configura-
tions (tokens per episode vs. mean return, Figure 4). Three patterns
emerge. (1) Across per-model Pareto frontiers, at least one con-
text configuration is efficient for every model, typically obs+net
or hist+net. (2) Deliberation configurations reach the frontier for
only a minority of models and are often dominated by context or
hierarchy. (3) hier-base sets the high-performance frontier where
hierarchy helps, while hier-delib is consistently dominated by
hier-base, combining higher token cost with worse mean return.
Table 4: RPTS across all configurations (Section 4). Higher is
better; negatives = worse thanobs. Bold = best per model.
Config Grok Llama Devstral Qwen G2.5FL G3FP
Axis 1: Context
obs+hist 0.25 4.03 0.80 6.57 0.33 1.33
obs+hist+net 0.49 3.66 2.78 7.98 0.71 0.73
obs+net2.46 13.28 5.36 13.600.19−1.88
network 0.60 11.23 4.15 10.26−0.01−5.01
hist+net† −0.505.51 3.56 9.55 0.072.49
Axis 2: Deliberation
+question 0.57 1.32 1.68 2.75 0.08−0.12
+critique 0.72 1.24 0.86 1.810.730.74
+improve 0.29 1.21 0.49 1.09 0.25 0.56
+COT 0.38 0.87 0.73 1.00 0.26 0.89
Axis 3: Hierarchy
hier-base 0.52 1.66 1.21 2.38 0.26 1.43
hier-delib 0.16 0.67 0.11 0.90 0.10 0.70
Return per Token Spent.Table 4 reports RPTS for all non-baseline
configurations. Context configurations dominate:obs+net achieves
the highest RPTS for Grok, Llama, Devstral, and Qwen, while
hist+net leads for G3FP. G2.5FL is the exception, with +critique

## Page 8

ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA Bogdanov et al.
Figure 5: Catastrophic failure rate (return <−150) by model and configuration. G2.5FL fails across all configurations; context
engineering reduces catastrophic rates for most other models.
performing best, consistent with its difficulty exploiting struc-
tured context. Hierarchy often improves absolute return but is
less token-efficient: hier-base consumes substantially more to-
kens than obs+net, yielding lower RPTS despite stronger mean
return. hier-delib remains high-cost and low-efficiency relative
to hier-base. As a pricing sensitivity check, we re-weighted token
costs using provider-specific input/output pricing ratios (Appen-
dix F); this did not reverse any qualitative conclusion, although it
narrowed the relative cost advantage of context over hierarchy.
5.4 Robustness, Variance, and Tail Risk
Qualitative effects (context helps, distributed deliberation hurts)
are consistent across models, and magnitudes vary by2-10 ×. Stan-
dard deviations (SD) of episode return, reported alongside means
in Table 3, reveal how each design axis affects outcome variability.
Context engineering compresses both mean and variance. Program-
matic state abstraction reduces SD alongside mean return (e.g.,
Grok: 70 to 40, Devstral: 65 to 48) and reduces catastrophic failure
(<−150) from > 90%under obs to < 10%in the strongest cases
(Figure 5). Bounded hierarchy further tightens outcomes: G3FP
under hier-base achieves SD =3, and Grok’s SD falls from 79 to
27. Conversely, hier-delib increases variance: Devstral’s SD rises
from 37 to 72 and its catastrophic rate jumps from 2% to 44%, con-
sistent with the deliberation cascade. G2.5FL fails catastrophically
(> 48%) across all configurations, suggesting a capability floor for
the structured I/O compliance the architecture requires; positive
claims do not depend on G2.5FL. Hierarchy provides limited or
negative value for two models. Llama worsens under hierarchy
(−57.1 →−69.5, 22%) with SD remaining high at 60. G2.5FL im-
proves only marginally (12%; −208.7 →−183.1). The remaining
four models improve substantially (52-79%). Multi-model evalua-
tion is thus essential: a Llama-only study would conclude hierarchy
hurts, whereas a Grok-only study would assert it is important.
6 Discussion
Our findings share a unifying theme: in adversarial sequential
POMDPs, the value of a design choice is determined byinforma-
tion flowthrough the system rather than per-component merit. We
distill three design principles (RQ1-RQ3).
Principle 1: Invest in deterministic infrastructure before LLM rea-
soning (RQ1).The programmatic state-tracking layer delivers the
largest consistent gains per token by shifting the LLM from perception-
plus-reasoning to reasoning-over-state. Knowledge-free agents rely
solely on this scaffolding, so gains come frompresentationand
uncertainty compression, not domain expertise. Context engineer-
ing also compresses tail risk: catastrophic failure (return <−150,
roughly the Random Agent level) drops from > 90%under obs to
< 10%under obs+net or hist+net in the strongest cases (Figure 5),
making it the most reliable lever for average and worst case.
Principle 2: Decompose into bounded specialists, not reflective gen-
eralists (RQ2,RQ3).Hierarchy without deliberation ( hier-base)
achieves best or near-best absolute performance for four of six
models. The benefit isinterface constraints: the Analyst gives a
bounded assessment and the ActionChooser a ranked list, turning
an open-ended generation problem into a verifiable decision.
Principle 3: Do not distribute deliberation without an uncertainty-
resolution protocol (RQ2,RQ3).Enabling deliberation across all
hierarchical agents degrades performance and inflates cost. Indepen-
dent critique loops createcascading uncertainty. When a sub-agent
critiques its own answer, it introduces excessive qualifications. The
consuming agent cannot distinguish these from genuine warnings
about the environment, so caution accumulates through the hierar-
chy. If deliberation is needed across a hierarchy, centralize it or use
explicit mediation (e.g., confidence gating, aggregation rules).
Model dependence and practical ordering.Effect directions (con-
text helps, distributed deliberation hurts) hold across models, but
magnitudes vary by2-10 ×and some effects flip (e.g., Llama harmed
by hierarchy). Single-model studies would thus contradict each
other. The best first step differs by model (context for weak raw-
observation handling, hierarchy for strong baselines). The observed
Pareto ordering follows our engineering trajectory: (1) context is the
most reliable lever; (2) bounded hierarchy sets the ceiling; (3) mono-
lithic deliberation is capability-conditional; (4) distributed delibera-
tion is dominated. Our results complement topology-focused scal-
ing [9] by showing that internal configuration determines whether
decomposition helps or hurts, revealing failure modes invisible to
topology-only analyses. Each layer builds on the previous, and the

## Page 9

Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA
value of hierarchy and deliberation is conditional on the quality of
infrastructure and context.
Transferability.The effect directions (Principles 1–3) replicate
across six models from five families, making them directional start-
ing points rather than hard prescriptions; specific magnitudes are
tied to CAGE-2 and the models tested. A practitioner should: (1) add
structured programmatic context (environment model, history track-
ing, observation decomposition, baseline state); (2) compare mono-
lithic configurations against raw observations; (3) test bounded
hierarchy if feasible; and (4) avoid distributing deliberation tools
across sub-agents by default. The state-tracking layer is likely to
transfer where observations are structured enough that a program
can track what has changed and why, and most steps are routine
so history compresses without losing important information.
7 Related Work
Our study sits at the intersection of four research streams that prior
work typically addresses in isolation.
Multi-Agent Architecture and Scaling.Recent work categorizes
coordination protocols [16, 21], derives topology scaling laws [9],
and proposes structured communication formats [ 7, 20]. These
studies vary wiring while treating nodes as fixed; we hold wiring
fixed and ablateinternalconfiguration, revealing failure modes like
deliberation cascades that are invisible to topology-only analyses.
Autonomous Cyber Defense.CybORG CAGE-2 [ 8, 22] has been
addressed with RL [1], model-based planning [4], and particle filter-
ing [12]. LLM-based defenders [3, 14] are newer but lack controlled
architectural ablations. We provide the first cost-performance anal-
ysis of compound LLM design decisions in CAGE-2.
Context Engineering.Context design is a critical lever [ 6], sup-
ported by tooling ecosystems [ 11] and algorithmic context evo-
lution [25]. We contribute an orthogonal, controlled ablation of
contextcomposition(raw vs. structured) in a POMDP, showing that
deterministic state abstraction outperforms raw observations at
near-zero marginal cost.
Deliberation and Self-Critique.Intra-step deliberation techniques,
such as chain-of-thought [10, 23], self-interrogation [15], and self-
refinement [13], operate within a single inference call, unlike cross-
episode methods such as Reflexion [18]. Recent work shows that
self-correction without external feedback can be harmful in mono-
lithic agents [5], and Renze and Guven [17] decompose reflection
components but evaluate only monolithic settings. No prior work
studies deliberationdistributedacross a hierarchy. Our deliberation
cascade finding extends the single-agent self-correction limitation
to compound systems, identifying a compositional failure mode
invisible to either literature in isolation.
8 Limitations and Future Work
Our claims are scoped tostructured adversarial POMDPswhere de-
terministic state abstraction is feasible. We use a single environment
(fixed topology, scripted adversary, 30-step horizon) and a single
three-agent hierarchy; alternative topologies may exhibit different
deliberation cascade dynamics. Token counts proxy cost but do
not capture latency or pricing, and knowledge-free prompts isolate
architectural effects without fully disentangling pretrained priors.
Deliberation tools are tested only in cumulative activation order;
independent activation may yield different interaction patterns.
Our model selection spans mid-tier and efficiency-focused families;
frontier-scale models may respond differently. Our design space
is static. Priorities for future work include independent ablation
of individual deliberation tools to isolate which components drive
the cascade, selective deliberation placement within the hierarchy
(e.g., enabling deliberation on only one sub-agent), and evalua-
tion on frontier-scale models to test whether the observed effects
persist at higher capability levels. Extending ablations to diverse
environments and designing inter-agent uncertainty arbitration
protocols, such as confidence gating or calibrated aggregation, are
also important next steps.
9 Conclusion
We presented a controlled cost-performance study of compound
LLM agent design in an adversarial, partially observable sequential
environment (CybORG CAGE-2). Across a three-axis ablation of
context representation (6 configurations), deliberation depth (4 cu-
mulative levels), and hierarchical decomposition (2 configurations),
we evaluated 72 model-configuration pairs spanning five model
families, totaling 3,475 episodes and 283.9M tokens.
Three conclusions emerge. First (RQ1),context engineering dom-
inates: deterministic programmatic state abstraction yields the
largest and most consistent gains per token, while raw observa-
tions alone are destabilizing. Second (RQ2),hierarchy can substi-
tute for deliberation: bounded specialist decomposition (hier-base)
achieves the best absolute performance for most models through
strict I/O contracts rather than deeper per-agent reasoning. Third
(RQ3),deliberation is not modular: distributing deliberation tools
across a hierarchy (hier-delib) produces adeliberation cascade
that degrades returns while increasing token expenditure.
A cross-cutting finding reinforces these conclusions: qualitative
effects hold across all six models, but magnitudes vary by2-10 ×
and some reverse sign (e.g., Llama is harmed by hierarchy), validat-
ing multi-model evaluation as essential for compound AI research.
These results suggest a practical starting point for structured ad-
versarial POMDPs, mirroring the trajectory we followed: build
deterministic infrastructure to deliver clean structured context, add
bounded hierarchy when models can exploit delegation, and treat
deliberation as a costly capability-conditional option rather than a
universal upgrade. This is not a universal prescription, as magni-
tudes are environment-dependent, and practitioners should validate
this ordering in their own settings. More broadly, our findings sug-
gest that the science of compound AI systems requires studying
topology, node internals, and the interaction effects that arise when
individually sensible components are composed. The deliberation
cascade identified in this study is one such interaction effect, and
designing inter-agent uncertainty arbitration protocols to prevent
it is a promising direction for future work. Reproducibility details
and ethics considerations are in Appendix A. The archived artifact
is available at https://doi.org/10.5281/zenodo.19908100; the devel-
opment repository is available at https://github.com/isbogdanov/
agent-design-study.

## Page 10

ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA Bogdanov et al.
References
[1] Elizabeth Bates, Vasilios Mavroudis, and Chris Hicks. 2023. Reward Shaping for
Happier Autonomous Cyber Security Agents. InProceedings of the 16th ACM
Workshop on Artificial Intelligence and Security (AISec ’23)(Copenhagen, Den-
mark). Association for Computing Machinery, New York, NY, USA, 221–232.
doi:10.1145/3605764.3623916
[2] CardiffUni Team. 2022. CybORG CAGE-2 Winning Agent: PPO + Greedy Decoys.
https://github.com/john-cardiff/-cyborg-cage-2. Accessed: 2026-04-28.
[3] Sebastián R. Castro, Roberto Campbell, Nancy Lau, Octavio Villalobos, Jiaqi Duan,
and Alvaro A. Cardenas. 2025. Large Language Models are Autonomous Cyber
Defenders. InProceedings of the 2025 IEEE Conference on Artificial Intelligence
(CAI). 1125–1132. doi:10.1109/CAI64502.2025.00195
[4] Kim Hammar, Neil Dhir, and Rolf Stadler. 2024. Optimal Defender Strate-
gies for CAGE-2 using Causal Modeling and Tree Search.arXiv(2024).
arXiv:2407.11070 [cs.CR] doi:10.48550/arXiv.2407.11070
[5] Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei
Yu, Xinying Song, and Denny Zhou. 2024. Large Language Models Cannot Self-
Correct Reasoning Yet. InInternational Conference on Learning Representations
(ICLR). doi:10.48550/arXiv.2310.01798
[6] Andrej Karpathy. 2025. +1 for “context engineering” over “prompt engineering”.
X (formerly Twitter) post. https://x.com/karpathy/status/1937902205765607626
Accessed 2026-02-22.
[7] Karim Ben Khaled and Davy Monticolo. 2026. G2CP: A Graph-Grounded Com-
munication Protocol for Verifiable and Efficient Multi-Agent Reasoning.arXiv
(2026). arXiv:2602.13370 [cs.AI] doi:10.48550/arXiv.2602.13370
[8] Mitchell Kiely, David Bowman, Maxwell Standen, and Christopher Moir. 2023.
On Autonomous Agents in a Cyber Defence Environment.arXiv(2023).
arXiv:2309.07388 [cs.CR] doi:10.48550/arXiv.2309.07388
[9] Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park, Samuel Schmidgall, A. Ali
Heydari, Yao Yan, Zhihan Zhang, Yuchen Zhuang, Mark Malhotra, Paul Pu Liang,
Hae Won Park, Yuzhe Yang, Xuhai Xu, Yilun Du, Shwetak Patel, Tim Althoff,
Daniel McDuff, and Xin Liu. 2025. Towards a Science of Scaling Agent Systems.
arXiv(2025). arXiv:2512.08296 [cs.AI] doi:10.48550/arXiv.2512.08296
[10] Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke
Iwasawa. 2022. Large Language Models are Zero-Shot Reasoners. InAdvances in
Neural Information Processing Systems, Vol. 35. doi:10.48550/arXiv.2205.11916
[11] LangChain. 2025. LangChain. Open-source software framework. https://github.
com/langchain-ai/langchain Accessed 2026-02-22.
[12] Duc Huy Le and Rolf Stadler. 2025. Learning Optimal Defender Strategies for
CAGE-2 using a POMDP Model.arXiv(2025). arXiv:2509.06539 [cs.AI] doi:10.
48550/arXiv.2509.06539
[13] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah
Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank
Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir
Yazdanbakhsh, and Peter Clark. 2023. Self-Refine: Iterative Refinement with
Self-Feedback. InAdvances in Neural Information Processing Systems, Vol. 36.
doi:10.48550/arXiv.2303.17651
[14] Hamoun Mohammadi, Jonathan J. Davis, and Mitchell Kiely. 2025. Leveraging
Large Language Models for Autonomous Cyber Defense: Insights from CAGE-2
Simulations.IEEE Intelligent Systems40 (2025), 29–36. doi:10.1109/MIS.2025.
3568209
[15] Ofir Press, Muru Zhang, Sewon Min, Ludwig Schmidt, Noah A. Smith, and Mike
Lewis. 2023. Measuring and Narrowing the Compositionality Gap in Language
Models. InFindings of the Association for Computational Linguistics: EMNLP 2023.
Association for Computational Linguistics, 5687–5711. doi:10.18653/v1/2023.
findings-emnlp.378
[16] Chen Qian, Zihao Xie, YiFei Wang, Wei Liu, Kunlun Zhu, Hanchen Xia, Yufan
Dang, Zhuoyun Du, Weize Chen, Cheng Yang, Zhiyuan Liu, and Maosong Sun.
2025. Scaling Large Language Model-based Multi-Agent Collaboration. InInter-
national Conference on Learning Representations (ICLR). doi:10.48550/arXiv.2406.
07155
[17] Matthew Renze and Erhan Guven. 2024. Self-Reflection in LLM Agents: Effects
on Problem-Solving Performance.arXiv(2024). arXiv:2405.06682 [cs.AI] doi:10.
48550/arXiv.2405.06682
[18] Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik
Narasimhan, and Shunyu Yao. 2023. Reflexion: Language Agents with Verbal
Reinforcement Learning. InAdvances in Neural Information Processing Systems,
Vol. 36. doi:10.48550/arXiv.2303.11366
[19] Maxwell Standen, Martin Lucas, David Bowman, Toby J. Richer, Junae Kim, and
Damian Marriott. 2021. CybORG: A Gym for the Development of Autonomous
Cyber Agents.arXiv(2021). arXiv:2108.09118 [cs.CR] doi:10.48550/arXiv.2108.
09118
[20] Yichen Tang, Weihang Su, Yujia Zhou, Yiqun Liu, Min Zhang, Shaoping Ma,
and Qingyao Ai. 2025. Augmenting Multi-Agent Communication with State
Delta Trajectory. InProceedings of the 2025 Conference on Empirical Methods in
Natural Language Processing (EMNLP). Association for Computational Linguistics,
10219–10240. doi:10.18653/v1/2025.emnlp-main.518
[21] Khanh-Tung Tran, Dung Dao, Minh-Duong Nguyen, Quoc-Viet Pham, Barry
O’Sullivan, and Hoang D. Nguyen. 2025. Multi-Agent Collaboration Mechanisms:
A Survey of LLMs.arXiv(2025). arXiv:2501.06322 [cs.AI] doi:10.48550/arXiv.
2501.06322
[22] TTCP CAGE Challenge Working Group. 2022. TTCP CAGE Challenge 2. https:
//github.com/cage-challenge/cage-challenge-2 Accessed 2026-02-22.
[23] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei
Xia, Ed Chi, Quoc V. Le, and Denny Zhou. 2022. Chain-of-Thought Prompting
Elicits Reasoning in Large Language Models. InAdvances in Neural Information
Processing Systems, Vol. 35. doi:10.48550/arXiv.2201.11903
[24] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan,
and Yuan Cao. 2023. ReAct: Synergizing Reasoning and Acting in Language
Models. InInternational Conference on Learning Representations (ICLR). doi:10.
48550/arXiv.2210.03629
[25] Qizheng Zhang, Changran Hu, Shubhangi Upasani, Boyuan Ma, Fenglu Hong,
Vamsidhar Kamanuru, Jay Rainton, Chen Wu, Mengmeng Ji, Hanchen Li, Ur-
mish Thakker, James Zou, and Kunle Olukotun. 2025. Agentic Context Engi-
neering: Evolving Contexts for Self-Improving Language Models.arXiv(2025).
arXiv:2510.04618 [cs.LG] doi:10.48550/arXiv.2510.04618
Appendix organization.Appendix A provides reproducibility de-
tails and ethics considerations. Appendix B lists the complete YAML
definitions for the Planner, Analyst, and ActionChooser. Appen-
dix C documents the deliberation tool schemas and activation flags.
Appendix D reports complete results, cross-axis comparisons, distri-
butional analysis, and token cost data for all 72 model–configuration
pairs. Appendix E provides 95% confidence intervals and paired
mean-return difference confidence intervals. Appendix F breaks
down token consumption and prompt/completion shifts. Appen-
dix G provides illustrative trajectory excerpts for the deliberation
cascade failure mode. Appendix H summarizes CAGE-2 environ-
ment details, network topology, and instance difficulty. Appendix I
lists the evaluated episode counts per model and configuration.
A Reproducibility & Ethics
Ethics.All authors have read and adhere to the ACM Code of
Ethics1. All experiments run within the simulated CybORG CAGE-2
environment [22]; no real networks, live attack infrastructure, or
human-subject data are involved. The work is strictly defensive
in scope. LLM tools were used for language polishing and data
processing scripts; all design decisions, analyses, and claims are
authored by the research team.
Reproducibility.All models use deterministic decoding (temper-
ature 0 or provider minimum). We release the source code, ex-
act YAML configuration snapshots, episode-allocation metadata,
container specification, API-key template, and experiment runner
needed to rerun the evaluated variants. The paper reports the ag-
gregate results, token accounting, and episode counts used for the
main claims, while the artifact provides the implementation and
configuration snapshots needed for inspection and selected reruns.
We rely on cross-model replication of qualitative effects rather than
single-model statistical significance.
A.1 Artifact Availability and Scope
The artifact supporting this paper is archived on Zenodo at https:
//doi.org/10.5281/zenodo.19908100. The development repository is
available at https://github.com/isbogdanov/agent-design-study. De-
tailed build, configuration, and execution instructions are provided
in the artifact README.
1https://www.acm.org/code-of-ethics

## Page 11

Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA
The artifact contains the agent implementation, experiment
runner, container specification, API-key template, and configu-
ration snapshots needed to rerun evaluated variants. The main
implementation is in agent_base/, including the CybORG and
LLM-agent coordinators, provider-connector configuration, log-
ging utilities, and the YAML-defined Planner, Analyst, and Action-
Chooser agents. exp_configs/ contains the twelve paper configu-
rations (six context, four deliberation, two hierarchy), each a self-
contained YAML snapshot; switching conditions requires changing
definitions_sourceinexperiment_agent_eval.yaml.
Experiments are launched viarun_experiment.py (10 instances
×5 runs = 50 episodes per pair by default). The Dockerfile builds
a Python environment with CybORG CAGE-2 and dependencies;
LLM access is supplied through the provided.env.template.
A run creates an experiments/ directory with the copied con-
figuration, per-instance reports, aggregate summaries, and token-
usage logs. Full raw LLM-provider transcripts are not bundled due
to storage size; original run seeds are also not included, so the
artifact supports executable reruns rather than bit-for-bit log regen-
eration. Original logs may be available upon request. The primary
reproducibility target is to enable inspection of the implementation
and configuration snapshots, and rerunning of selected configura-
tions.
B Agent Definitions
This appendix provides the complete YAML definitions for all
three agents (Planner, Analyst, ActionChooser), demonstrating
the near-zero-knowledge starting point described in Section 2.
Each agent is defined by three files: core.yaml (identity, model
binding, tool flags), initial_prompt.yaml (per-step prompt tem-
plate), and persistent_knowledge.yaml (domain knowledge). A
shared common_knowledge.yaml applies to all agents. All remain-
ing knowledge files,reflection_knowledge.yaml,
reflection_examples.yaml, and examples.yaml, are confirmed
empty for every agent in every experiment reported in this pa-
per; the learning subsystem that would populate them is disabled
throughout. The boolean flags include_tool_raise_a_question,
include_tool_critique_the_answer, and
include_tool_improve_based_on_critiquein each agent’s
core.yaml are set to false in the baseline configuration and tog-
gled to true cumulatively for the deliberation axis (Section 3.4).
The YAML shown below reflects the baseline (anchor) configura-
tion; deliberation variants differ only in these three flags and in the
optionalinclude_COT_instructioninjection.
B.1 Shared Configuration
common_knowledge.yaml.
,
reflection_knowledge:
This file is empty, confirming that no shared domain heuristics are
injected across agents.
B.2 Planner
planner/core.yaml.
agent_type: "ReAct"
include_tool_raise_a_question: false
include_tool_critique_the_answer: false
include_tool_improve_based_on_critique: false
include_COT_instruction: false
add_examples: false
add_reflection_examples: true
system_message: |
You are the strategic decision-maker for the
Blue team's cybersecurity defense. Your role is
to select ONE action per step that best defends
the network.
You must balance immediate threats with strategic
positioning, considering that you can only act
once per step.
You MUST follow your <reflection_rules> during
each thought phase.
Provide a final answer to the question asked
by the USER.
COT_instruction: |
You MUST follow your Chain-of-Thought instructions
during each thought phase.
1. REVIEW SITUATION: Check network status and step
history. Which hosts need attention? What actions
have been tried?
2. IDENTIFY TARGET: Select the most critical host or
threat to address this step
3. GATHER INFO: If needed, use
get_analysis_of_host_update for detailed analysis
of a changed host
4. GET SUGGESTIONS: Call
get_suggestion_for_next_action with JSON:
{"target_host": "hostname", "situation":
"description", "severity": "level", "context":
"relevant history"}
5. DECIDE: Choose ONE action from suggestions. You
may override based on strategic reasoning
rules:
- You must select ONLY ONE action for your final
Answer from the list of suggestions provided by
the'get_suggestion_for_next_action'tool
- Your final Answer MUST be a verbatim copy of the
action-string from ONE of the suggestions
- TOOLS CANNOT HANDLE MULTIPLE HOSTS, YOU MUST
SELECT ONLY ONE SPECIFIC HOST AT A TIME
tools:
- name: "get_analysis_of_host_update"
description: "Provides a detailed analysis and
comparison of the state change of the specific
host to its baseline"

## Page 12

ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA Bogdanov et al.
example_calling:
"get_analysis_of_host_update: User4"
- name: "get_suggestion_for_next_action"
description: |
Suggests a ranked list of final actions, each
with a justification and confidence score based
on recent analysis and action history.
CRITICAL INPUT REQUIREMENT: Your input MUST be
a valid JSON object with these required keys:
- "target_host": The specific single hostname
- "situation": Brief description of the threat
- "severity": Threat level
(low|medium|high|critical)
- "context": Relevant information from
previous steps
example_calling: >
get_suggestion_for_next_action:
{"target_host": "Enterprise1", "situation":
"critically compromised with active C2",
"severity": "critical", "context": "Remove
action failed previously"}
is_critical: true
The Planner’s two domain-specific tools,
get_analysis_of_host_update
and get_suggestion_for_next_action, are the interfaces through
which theCoordinatorspawns the Analyst and ActionChooser
sub-agents in hierarchical configurations (hier-base and hier-delib).
When delegation is disabled, the Planner does not invoke these tools
and instead emits an environment action directly.
planner/initial_prompt.yaml.
prompt:
opening: |
You are at step {step_number} now.
{network_status}
{history}
closing: |
What action should be taken next?
The placeholders {network_status}, {history}, and (in con-
text variants that include it) {observation} are populated deter-
ministically at each step by the environment-state layer described in
Section 3.2. The anchor configuration includes {network_status}
and{history}but omits{observation}.
Context output examples.The {network_status} placeholder
is rendered as a JSON list of all non-baseline hosts, annotated with
current status, recency, and action history:
Network Status: The following hosts have
updates or are in a non-baseline state:
[
{"host_name": "Enterprise1",
"current_status": "changed",
"time_of_update": "Current",
"applied_actions_so_far": "Analyse->Remove"},
{"host_name": "User4",
"current_status": "unknown",
"time_of_update": "Past",
"applied_actions_so_far": "Remove"}
]
When all hosts are healthy, a single sentence reports baseline sta-
tus, keeping the prompt compact. The {history} placeholder is
rendered as a compressed action log with smart collapsing: consec-
utive quiet steps are folded into ranges when no state changes are
detected, while steps involving interventions retain full detail:
Steps 1-3: Action: Monitor/No action needed.
(No state changes observed)
Step 4: {"action": "Analyse Enterprise1",
"analysis": "Host shows suspicious processes"}
Step 5: {"action": "Remove Enterprise1"}
Step 6: Action: Monitor
planner/persistent_knowledge.yaml.
reflection_knowledge:
- content:
- Description: monitoring network for malicious
activity.
Example use: Monitor
Name: Monitor
Type: Passive observing action
- Description: it does not remove the host but
attempts to remove malicious infection from
a host.
Example use: Remove hostname=someName
Name: Remove
Type: Reactive intervention
- Description: analyzing a host for malicious
activity at deeper system level
Example use: Analyse hostname=someName
Name: Analyse
Type: Passive observing action
- Description: restoring a host to a clean state
with very high penalty, this action removes
all previously deployed decoys from the host
Example use: Restore hostname=someName
Name: Restore
Type: Reactive intervention
- Description: deploying a service to act as a
decoy to a host to distract the attacker
in future steps
Example use: DecoySERVICE hostname=someName
Name: DecoySERVICE
Type: Proactive Protective action
header: >
INTERPRETATION OF ACTIONS FROM
<AVAILABLE_ACTIONS_LIST>
root: actions
type: json

## Page 13

Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA
This is the only domain knowledge provided to the Planner (and,
identically, to the ActionChooser): a five-entry action-type glossary
with names, types, and usage syntax. No tactical heuristics, no
threat-assessment rubrics, and no worked examples are included.
Empty knowledge files.The following files are empty for all Plan-
ner experiments: examples.yaml, reflection_examples.yaml,
andreflection_knowledge.yaml.
B.3 Analyst
analyst/core.yaml.
agent_type: "ReAct"
include_tool_raise_a_question: false
include_tool_critique_the_answer: false
include_tool_improve_based_on_critique: false
include_COT_instruction: false
add_examples: false
add_reflection_examples: true
system_message: |
You are a cybersecurity analyst.
You MUST follow your <reflection_rules> during
each thought phase.
Provide a final answer to the question asked
by the USER.
COT_instruction: |
You MUST follow your Chain-of-Thought instructions
during each thought phase.
1. GET CURRENT STATE: Use get_host_current_state
for the target host
2. GET BASELINE: Use get_host_baseline_state to
compare against initial state
3. IDENTIFY ANOMALIES: What changed? New processes,
connections, missing services?
4. ASSESS SEVERITY: How critical is this compromise?
Is there C2 activity?
5. RECOMMEND ACTION: Should we contain, investigate
further, or just monitor?
tools:
- name: "get_host_current_state"
description: "Get the current state details for a
specific host. The input must be a single
hostname."
example_calling: "get_host_current_state:
Enterprise1"
- name: "get_host_baseline_state"
description: "Get the baseline state details for
a specific host. The input must be a single
hostname."
example_calling: "get_host_baseline_state:
Enterprise1"
answer_format: |
Your response MUST STRICTLY be a JSON array of
objects that follows the following schema:
{
"host": "<n>",
"status": "baseline|changed|unknown",
"severity": "low|medium|high|critical",
"anomalies": ["<short bullet>", "..."],
"suspected_c2": ["<ip/host>"],
"recommended_focus":
"containment|investigation|monitor",
"rationale": "<2-3 sentences>"
}
The Analyst receives a one-sentence role identity and two read-
only tools (get_host_current_state, get_host_baseline_state)
that return deterministic JSON from the environment-state layer. Its
output is a structured JSON assessment with a constrained schema.
No domain heuristics are provided: itspersistent_knowledge.yaml
and all example files are empty.
analyst/initial_prompt.yaml.
prompt:
opening: |
You must provide an analysis for the host:
{hostname}.
closing: |
What is your understanding of the situation
with the host?
B.4 ActionChooser
action_chooser/core.yaml.
agent_type: "ReAct"
include_tool_raise_a_question: false
include_tool_critique_the_answer: false
include_tool_improve_based_on_critique: false
include_COT_instruction: false
add_examples: false
add_reflection_examples: true
system_message: |
You are a tactical cybersecurity advisor for the
Blue team.
You MUST follow your <reflection_rules> during
each thought phase.
Provide a final answer to the question asked
by the USER.
COT_instruction: |
You MUST follow your Chain-of-Thought instructions
during each thought phase.
1. READ SITUATION: Check SITUATION_JSON for
target_host, threat description, severity,
and context
2. EVALUATE ACTIONS: Consider available action

## Page 14

ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA Bogdanov et al.
types and their costs vs benefits
3. RANK THREE: Provide three suggestions with
confidence scores (0.0-1.0), highest confidence
first
answer_format: |
Your response MUST STRICTLY be a JSON array of
objects, where each object represents a suggested
action. Each object must have ONLY the following
keys: "action", "confidence".
The ActionChooser hasno tools, it is a pure generation agent
that receives a situation JSON and returns a ranked action list. Its
persistent_knowledge.yaml contains the same five-entry action
glossary as the Planner (reproduced above). All example files are
empty.
action_chooser/initial_prompt.yaml.
prompt: |
<SITUATION_JSON>
{situational_understanding}
</SITUATION_JSON>
The JSON above contains:
- "target_host": The specific hostname requiring
action (CRITICAL: All your suggested actions
MUST target this host)
- "situation": Description of the current threat
- "severity": The threat level
(low|medium|high|critical)
- "context": Additional relevant information
from previous steps
Provide THREE action suggestions for the
target_host specified in the JSON, ordered from
highest confidence to lowest.
C Deliberation Tool Schemas
The deliberation tools are three generic self-critique operations
implemented in the shared BaseToolExecutor class and inherited
by all agent types. They are toggled via boolean flags in each agent’s
core.yaml; the cumulative activation sequence defines the four
deliberation levels in Axis 2 (Section 3.4).
Tool activation sequence.Table 5 shows the cumulative activation
of each flag.
Table 5: Deliberation tool activation by experimental level.
Each level cumulatively adds capabilities; +COT adds all three
tools plus an explicit chain-of-thought system prompt injec-
tion.
Flag +ques. +crit. +impr. +COT
include_tool_raise_a_question✓ ✓ ✓ ✓
include_tool_critique_the_answer✓ ✓ ✓
include_tool_improve_based_on_critique✓ ✓
include_COT_instruction✓
raise_a_question.When invoked, the agent formulates a question
directed at itself. The tool returns the question text as an "observa-
tion" prompting the agent to answer it in the next reasoning turn.
This creates a self-interrogation loop: the agent pauses its action-
selection process to surface uncertainties or alternative framings.
The tool accepts free-text input (the question) and returns a format-
ted prompt:"You have chosen ask yourself: {question}. What can you
answer to yourself?"
critique_the_answer.The agent submits its current reasoning as
input. The tool returns this text as a critique prompt, asking the
agent to evaluate its own logic:"You have chosen to critique your
reasoning: ‘{reasoning}’. Now, provide your critical assessment. "This
forces a second pass over the agent’s tentative conclusion before
action commitment.
improve_based_on_critique.After critiquing, the agent submits
an improved version of its reasoning. The tool returns:"You have
decided to improve your answer based on the critique:
‘{improved_reasoning}’. Now, provide your final answer. "This creates
a three-phase deliberation cycle: question→critique→improve.
COT instruction injection.The +COT level does not add a fourth
tool. Instead, it sets include_COT_instruction=true, which in-
jects theCOT_instruction block from the agent’score.yaml (shown
in Appendix B) into the system prompt. This provides explicit step-
by-step reasoning guidance tailored to each agent’s role. Combined
with the three tools, +COT represents the maximum deliberation
configuration.
Scope of distribution.In hier-base, only the Planner’s delibera-
tion flags are toggled (the Analyst and ActionChooser retainfalse
for all flags). In hier-delib, the same flags are toggled forall three
agents, creating the distributed deliberation condition studied in
Section 5.2.3.
D Complete Results
This appendix presents supplementary results for all 72 model–
configuration pairs, organized by experimental axis. Figure 6 com-
pares each axis’s best configuration against the shared anchor.
Figure 6: Best configuration per axis compared to the shared
anchor configuration. For most models, the largest absolute
improvement comes from hierarchy (Axis 3), but context
engineering (Axis 1) achieves competitive gains at a fraction
of the token cost.

## Page 15

Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA
D.1 Context Engineering
Table 6 provides standard deviations complementing the main-text
hero table (Table 3). Table 7 reports the marginal value of adding or
removing individual context components. Figures 7 and 8 visualize
context component marginal gains and the raw-observation penalty.
Figures 9 and 10 show context component interactions.
Figure 7: Marginal value of adding individual context com-
ponents. Positive values indicate improvement. Adding
{network_status} to raw observation delivers the largest con-
sistent gains.
Figure 8: Raw observation penalty. Gap between obs-only
and the structured hist+net anchor configuration per model.
Longer bars indicate larger benefit from replacing raw obser-
vations with programmatic context.
D.2 Hierarchy and Architecture Summary
Table 8 details the hierarchy degradation ratios. Table 9 compares
deliberation across monolithic and hierarchical settings. Table 10
quantifies the architectural impact range per model. Figure 11 shows
model fingerprints across axes. Figure 12 visualizes the deliberation
cascade penalty and Figure 13 shows the hierarchy degradation
pattern.
D.3 Deliberation
Tables 11 and 12 break down the deliberation axis with per-level
token consumption. Table 13 shows the return-on-investment for
each deliberation level. Figures 14, 15, and 16 visualize ROI, capa-
bility correlation, and the reasoning ceiling effect. Figure 17 shows
the performance trajectory across cumulative deliberation levels.
D.4 Cross-Axis Comparisons
Table 14 compares the observation-only baseline against each model’s
best and worst configuration. Tables 17, 18, and 19 identify best
and worst configurations within each axis. Table 15 and Figure 18
present pairwise win rates; Figure 19 provides a head-to-head win-
rate matrix using each model’s peak configuration. Table 16 summa-
rizes performance by configuration group. Figure 20 and Table 20
demonstrate ranking stability across axes. Table 21 reports anchor-
configuration performance.
D.5 Distributional Analysis
Table 22 reports standard deviation and worst-case (minimum)
episode return for every model–configuration pair, supporting the
robustness analysis in Section 5.4. Table 23 reports catastrophic
failure rates (return <−150) for each configuration. Figures 21, 22,
23, 24, and 25 provide distributional views of episode returns across
design axes.
D.6 Token Cost Progression
Figure 26 shows the token cost progression from cheapest (obs) to
most expensive (hier-delib) configuration.
E Statistical Support
This appendix provides 95% confidence intervals for mean episode
returns (Table 24) and paired mean-return differences for key com-
parisons (Table 25).

## Page 16

ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA Bogdanov et al.
Table 6: Full results with standard deviation. Mean episode return ( ±standard deviation) across all 72 model–configuration
pairs, complementing the token-cost data in Table 3. Configurations are grouped by experimental axis.
Group Config Grok Llama Devstral Qwen G2.5FL G3FP
Context obs−98.4±69.8−214.7±22.5−155.1±64.7−218.2±19.8−214.7±22.8−96.8±70.7
obs+hist−89.9±75.3−137.4±63.3−133.9±85.5−93.4±71.7−172.9±69.4−76.3±67.2
obs+hist+net−81.9±78.0−102.6±73.2−85.3±77.5−69.0±53.2−147.8±69.5−82.6±63.8
obs+net-47.0±40.3-51.4±19.9-72.6±47.7−63.1±25.9−200.0±40.8−113.7±68.5
network−86.3±30.9−68.7±37.5−93.3±44.2−109.4±58.8−215.4±18.5−136.4±49.1
hist+net−112.9±78.7−57.1±54.1−79.3±76.5-61.5±51.8−208.7±39.3-52.0±57.6
Delib. +question−66.5±62.2−104.1±83.8−53.9±41.8−92.3±69.2−206.2±37.0−100.6±57.3
+critique−44.9±44.6−93.4±77.3−62.8±58.0−93.6±67.1-128.6±94.8−66.4±63.4
+improve−53.4±46.6−75.0±57.3−80.6±70.5−92.4±55.0−168.9±59.8−64.0±44.9
+COT−42.9±32.8−100.8±70.1−40.9±31.1−55.6±43.2−157.0±69.7−29.9±19.7
Hierarchy hier-base−24.0±27.0−69.5±60.0−37.8±37.2−28.6±36.6−183.1±62.4−16.1±2.7
hier-delib−40.4±26.1−108.0±74.3−127.4±71.8−30.1±32.7−186.4±58.1−23.6±12.4
Table 7: Context component marginal value. Each row shows the percentage improvement from adding or removing one
context component. Positive values indicate improvement (return moves toward zero). Transitions with ≥30% improvement are
bolded.
Transition Change Grok Llama Devstral Qwen G2.5FL G3FP
obs→obs+hist Adding history 8.6%36.0%13.7%57.2%19.5% 21.2%
obs→obs+net Adding network status52.2% 76.0% 53.2% 71.1%6.9%−17.4%
obs+hist→obs+hist+net Adding net to obs+hist 8.9% 25.3%36.3%26.2% 14.5%−8.2%
network→hist+net Adding history to net−30.8% 16.8% 15.1%43.8%3.1%61.9%
obs+net→obs+hist+net Adding hist to obs+net−74.3%−99.6%−17.6%−9.3% 26.1% 27.4%
obs+hist+net→hist+net Dropping raw obs−37.8%44.4%7.1% 10.8%−41.2%37.0%
Table 8: Hierarchy results. Mean return, standard deviation,
and tokens per episode for both hierarchy configurations,
plus the degradation ratio ( hier-delib/hier-base; values >1
indicate degradation from adding distributed deliberation).
hier-base hier-delib
Model Mean Std Tok Mean Std Tok Ratio
G3FP−16.12.7 56.4K−23.612.4 104.8K 1.46×
Grok−24.027.0 141.9K−40.426.1 364.1K 1.68×
Qwen−28.636.6 79.6K−30.132.7 209.9K 1.06×
Devstral−37.837.2 97.0K−127.471.8 257.7K 3.37×
Llama−69.560.0 87.7K−108.074.3 158.1K 1.55×
G2.5FL−183.162.4 120.6K−186.458.1 270.5K 1.02×

## Page 17

Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA
Figure 9: Context component waterfall. Additive effect of history and network status on top of raw observation. Green =
improvement, red = degradation.
Table 9: Deliberation in monolithic vs. hierarchical settings. Compares the shared anchor configuration, best monolithic
deliberation level, and both hierarchy configurations. For most models, hier-base matches or exceeds the best monolithic
deliberation at comparable cost, whilehier-delibdegrades it.
Anchor (hist+net) Best Mono Delib. hier-base hier-delib
Model Return Tok Return Tok Return Tok Return Tok
Grok−112.929.1K−42.9144.5K−24.0141.9K−40.4364.1K
Llama−57.128.6K−75.0115.3K−69.587.7K−108.0158.1K
Devstral−79.321.3K−40.9157.4K−37.897.0K−127.4257.7K
Qwen−61.516.4K−55.6162.4K−28.679.6K−30.1209.9K
G2.5FL−208.781.7K−128.6118.2K−183.1120.6K−186.4270.5K
G3FP−52.018.0K−29.975.1K−16.156.4K−23.6104.8K

## Page 18

ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA Bogdanov et al.
Figure 10: Context component interaction. obs+net compared
to obs-only and network-only. Synergy ( Δ) shows whether
combining exceeds the better individual.
Table 10: Architectural impact range per model. Best and
worst configurations across all twelve, with the return gap
quantifying the maximum leverage of architectural choices
within each model family.
Model Best Config Best Worst Config Worst Gap
Grok hier-base−24.0hist+net−112.988.8
Llama obs+net−51.4obs−214.7163.3
Devstral hier-base−37.8obs−155.1117.3
Qwen hier-base−28.6obs−218.2189.6
G2.5FL +critique−128.6network−215.486.8
G3FP hier-base−16.1network−136.4120.3

## Page 19

Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA
Figure 11: Model fingerprints. Each radar shows normalized best performance on three axes (context, deliberation, hierarchy).
Larger area indicates better overall performance. Models exhibit distinct capability profiles: Grok and G3FP excel across axes,
while G2.5FL is uniformly weak.
Table 11: Deliberation results (Grok, Llama, Devstral). Mean episode return, standard deviation, and tokens per episode across
five deliberation levels. Best return per model is bolded.
Grok Llama Devstral
Config Mean Std Tok Mean Std Tok Mean Std Tok
hist+net−112.978.7 29.1K-57.154.1 28.6K−79.376.5 21.3K
+question−66.562.2 55.6K−104.183.8 84.1K−53.941.8 60.4K
+critique−44.944.6 74.7K−93.477.3 97.8K−62.858.0 106.9K
+improve−53.446.6 154.0K−75.057.3 115.3K−80.670.5 153.1K
+COT-42.932.8 144.5K−100.870.1 131.3K-40.931.1 157.4K

## Page 20

ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA Bogdanov et al.
Table 12: Deliberation results (Qwen, G2.5FL, G3FP). Mean episode return, standard deviation, and tokens per episode across
five deliberation levels. Best return per model is bolded.
Qwen G2.5FL G3FP
Config Mean Std Tok Mean Std Tok Mean Std Tok
hist+net−61.551.8 16.4K−208.739.3 81.7K−52.057.6 18.0K
+question−92.369.2 45.7K−206.237.0 104.8K−100.657.3 30.7K
+critique−93.667.1 68.9K-128.694.8 118.2K−66.463.4 41.0K
+improve−92.455.0 115.9K−168.959.8 182.9K−64.044.9 58.1K
+COT-55.643.2 162.4K−157.069.7 225.7K-29.919.7 75.1K
Table 13: Deliberation return on investment. Shows the reward change ( Δ) and token increase ( Δ Tok) relative to the planner-only
anchor for each reasoning level. PositiveΔ= improvement.
Grok Llama Devstral Qwen G2.5FL G3FP
LevelΔRetΔTokΔRetΔTokΔRetΔTokΔRetΔTokΔRetΔTokΔRetΔTok
+question+46.4+26.5K -47.0 +55.5K+25.3+39.0K -30.8 +29.2K+2.5+23.2K -48.6 +12.7K
+critique+68.0+45.6K -36.3 +69.3K+16.4+85.6K -32.1 +52.5K+80.1+36.5K -14.4 +23.0K
+improve+59.4+124.9K -17.9 +86.7K -1.3 +131.7K -30.9 +99.4K+39.8+101.2K -12.0 +40.2K
+COT+70.0+115.4K -43.7 +102.7K+38.4+136.1K+5.9+146.0K+51.7+144.0K+22.1+57.1K
Table 14: Baseline Performance (Planner + Observation Only). The simplest configuration compared against each model’s best
and worst overall configuration across all 12 options.
Baseline (obs only) Worst Config Best Config
Model Runs Return Std Min Config Return Config Return Improv.
G3FP 25−96.8±70.7−200.8network−136.4hier-base−16.188%
Grok 50−98.4±69.8−225.8hist+net−112.9hier-base−24.079%
Devstral 50−155.1±64.7−225.8obs−155.1hier-base−37.876%
Llama 50−214.7±22.5−225.2obs−214.7obs+net−51.476%
G2.5FL 50−214.7±22.8−225.8network−215.4+critique−128.640%
Qwen 50−218.2±19.8−225.9obs−218.2hier-base−28.687%

## Page 21

Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA
Figure 12: The Deliberation Cascade Penalty. Slope chart
showing the shift in mean return when moving from mono-
lithic deliberation to hierarchical deliberation. Red = degra-
dation.
Figure 13: Hierarchy degradation. Performance change when
distributing deliberation tools across the hierarchy, showing
model-specific sensitivity to the deliberation cascade.
Table 15: Pairwise Win Rates: Anchor vs. Full Deliberation
(+COT).
Model +COT Wins Ties +COT Losses Total
Grok 37 (74%) 1 12 (24%) 50
Llama 15 (30%) 0 35 (70%) 50
Devstral 33 (66%) 0 17 (34%) 50
Qwen 27 (54%) 0 23 (46%) 50
G2.5FL 34 (68%) 5 11 (22%) 50
G3FP 14 (56%) 0 11 (44%) 25
Figure 14: Deliberation ROI. Each point shows one model–
level pair’s change in return and tokens relative to anchor.
Upper-left = efficient improvement.
Figure 15: Capability correlation. Models with stronger base-
lines (right) benefit less from deliberation on average. Spear-
man correlation shown.
Table 16: Performance by config group. Mean and range of
mean episode return across all models for each configuration
group.
Group Mean Best Worst Avg Tok/ep
Anchor (net+hist)−95.2−52.0−208.732.5K
Context−113.9−47.0−218.230.6K
Deliberation−86.4−29.9−206.2106.8K
Hierarchy−72.9−16.1−186.4162.4K

## Page 22

ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA Bogdanov et al.
Table 17: Context Engineering: Best and Worst Configurations per model.
Worst Context Config Best Context Config
Model Config Return Config Return Improv.
Grok hist+net−112.9 obs+net−47.0 58%
Llama obs−214.7 obs+net−51.4 76%
Devstral obs−155.1 obs+net−72.6 53%
Qwen obs−218.2 hist+net−61.5 72%
G2.5FL network−215.4 obs+hist+net−147.8 31%
G3FP network−136.4 hist+net−52.0 62%
Table 18: Deliberation: Best and Worst Configurations per model.
Worst Reasoning Config Best Reasoning Config
Model Config Return Config Return Improv.
Grok hist+net−112.9 +COT−42.9 62%
Llama +question−104.1 hist+net−57.1 45%
Devstral +improve−80.6 +COT−40.9 49%
Qwen +critique−93.6 +COT−55.6 41%
G2.5FL hist+net−208.7 +critique−128.6 38%
G3FP +question−100.6 +COT−29.9 70%
Table 19: Hierarchy: Best and Worst Configurations per model.
Worst Hierarchy Config Best Hierarchy Config
Model Config Return Config Return Improv.
Grok hier-delib−40.4 hier-base−24.0 41%
Llama hier-delib−108.0 hier-base−69.5 36%
Devstral hier-delib−127.4 hier-base−37.8 70%
Qwen hier-delib−30.1 hier-base−28.6 5%
G2.5FL hier-delib−186.4 hier-base−183.1 2%
G3FP hier-delib−23.6 hier-base−16.1 32%
Figure 16: The reasoning ceiling. Models with higher baseline
capabilities tend to peak at lower levels of deliberation before
degrading.
Figure 17: Deliberation progression. Performance trajectory
across cumulative deliberation levels for each model, show-
ing non-monotonic patterns and model-dependent ceilings.

## Page 23

Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA
Figure 18: Pairwise win rates. Anchor vs +COT compared
instance-by-instance. Blue = anchor wins, orange = +COT
wins, gray = ties.
Figure 19: Global head-to-head win-rate matrix. Compares
the peak configuration of every model against every other
model on a per-instance basis.
Table 20: Model rankings by config group (1 = best).
Model Context Delib. Hierarchy Overall
Grok1 131
Llama 5 5 5 5
Devstral 4 2 4 4
Qwen 3 4 2 3
G2.5FL 6 6 6 6
G3FP 2 312
Figure 20: Model ranking stability. Lines connect each
model’s best-config rank across the three axes. Flat lines
= consistent relative performance.
Table 21: Anchor performance across all models.
Model Mean Std Min Tok/ep
G3FP-52.057.6−224.818.0K
Llama−57.154.1−222.528.6K
Qwen−61.551.8−199.816.4K
Devstral−79.376.5−224.821.3K
Grok−112.978.7−224.729.1K
G2.5FL−208.739.3−224.881.7K
Figure 21: Cumulative distributions by axis. Threshold lines
mark failure severity. Right-shifted curves indicate better
tail behavior.

## Page 24

ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA Bogdanov et al.
Table 22: Variance and tail risk. Standard deviation and minimum (worst-case) episode return for each model–configuration
pair.
Grok Llama Devstral Qwen G2.5FL G3FP
Group ConfigStd Min Std Min Std Min Std Min Std Min Std Min
Ctx obs 69.8−225.822.5−225.264.7−225.819.8−225.922.8−225.870.7−200.8
obs+hist 75.3−224.863.3−224.785.5−225.371.7−224.869.4−229.567.2−223.8
obs+hist+net 78.0−224.873.2−222.477.5−224.853.2−224.869.5−225.763.8−224.8
obs+net 40.3−145.819.9−117.547.7−212.825.9−176.840.8−225.168.5−224.8
network 30.9−169.737.5−167.244.2−208.658.8−223.618.5−225.849.1−220.8
hist+net 78.7−224.754.1−222.576.5−224.851.8−199.839.3−224.857.6−224.8
Delib. +question 62.2−223.883.8−223.841.8−224.869.2−224.837.0−224.857.3−200.8
+critique 44.6−226.177.3−227.458.0−223.767.1−223.894.8−224.863.4−199.8
+improve 46.6−222.457.3−223.870.5−223.855.0−223.959.8−224.844.9−147.6
+COT 32.8−174.370.1−226.431.1−152.743.2−166.769.7−224.819.7−112.2
Hier hier-base 27.0−150.860.0−222.337.2−218.836.6−184.762.4−224.82.7−20.5
hier-delib 26.1−115.974.3−223.871.8−224.732.7−173.658.1−224.612.4−52.7
Table 23: Catastrophic failure rates. Percentage of episodes with return below −150(indicating near-total network compromise).
Lower is better.
Config Grok Llama Devstral Qwen G2.5FL G3FP
obs 28.0%96.0% 64.0% 98.0% 96.0%32.0%
obs+hist 26.0% 50.0%54.0%24.0%72.0%16.0%
obs+hist+net 24.0% 38.0% 26.0% 14.0%58.0%12.0%
obs+net 0.0% 0.0% 10.0% 2.0%88.0%36.0%
network 6.0% 4.0% 10.0% 32.0%98.0%24.0%
hist+net 44.0% 10.0% 24.0% 10.0%92.0%12.0%
+question 16.0% 38.0% 4.0% 24.0%96.0%22.0%
+critique 6.0% 32.0% 12.0% 20.0% 48.0% 12.0%
+improve 6.0% 12.0% 22.0% 18.0%60.0%0.0%
+COT 4.0% 30.0% 2.0% 8.0%52.0%0.0%
hier-base 2.0% 14.0% 2.0% 5.0%78.7%0.0%
hier-delib 0.0% 36.0% 44.0% 4.0%80.0%0.0%
Table 24: Full results matrix with 95% confidence intervals. Mean episode return ( ±CI half-width) across all 72 model–
configuration pairs. Best point-estimate return per model is bolded. Configurations are grouped by experimental axis.
Group Config Grok Llama Devstral Qwen G2.5FL G3FP
Context obs−98.4±19.8−214.7±6.4−155.1±18.4−218.2±5.6−214.7±6.5−96.8±29.2
obs+hist−89.9±21.4−137.4±18.0−133.9±24.3−93.4±20.4−172.9±19.7−76.3±27.8
obs+hist+net−81.9±22.2−102.6±20.8−85.3±22.0−69.0±15.1−147.8±19.8−82.6±26.3
obs+net−47.0±11.4-51.4±5.7−72.6±13.6−63.1±7.4−200.0±8.1−113.7±28.3
network−86.3±8.8−68.7±10.7−93.3±12.6−109.4±16.7−215.4±5.3−136.4±20.3
hist+net−112.9±22.4−57.1±15.4−79.3±21.7−61.5±14.7−208.7±11.2−52.0±23.8
Self-Reas. +question−66.5±17.7−104.1±23.8−53.9±11.9−92.3±19.7−206.2±10.5−100.6±16.3
+critique−44.9±12.7−93.4±22.0−62.8±16.5−93.6±19.1-128.6±27.0−66.4±26.2
+improve−53.4±13.2−75.0±16.3−80.6±20.0−92.4±15.6−168.9±17.0−64.0±18.5
+COT−42.9±9.3−100.8±19.9−40.9±8.8−55.6±12.3−157.0±19.8−29.9±8.1
Hierarchy hier-base-24.0±7.7−69.5±17.1-37.8±10.6-28.6±7.3−183.1±14.4-16.1±1.1
hier-delib−40.4±7.4−108.0±21.1−127.4±20.4−30.1±9.3−186.4±16.5−23.6±3.5
Table 25: Paired mean-return differences with 95% confidence intervals. Each cell shows Δ = mean paired difference ±CI half-
width (matched by instance ×run; duplicate episodes averaged before pairing). Bold indicates the 95% CI excludes zero; positive
Δ means the first-named configuration yields higher return. †Post-hoc selected:best-ctxis the highest-return structured context
per model (excluding raw obs);best-SRis the highest-return monolithic self-reasoning level ( +question... +COT, excluding the
hist+netanchor).
Comparison Grok Llama Devstral Qwen G2.5FL G3FP
hier-delib−hier-base-16.4±11.5-38.5±28.7-89.6±23.1−1.6±11.9−0.1±22.7-7.5±3.6
obs+net−obs+51.4±23.3+163.3±7.9+82.5±24.5+155.1±9.1+14.8±8.5−16.8±41.1
best-ctx†−obs+51.4±23.3+163.3±7.9+82.5±24.5+156.7±15.8+66.9±19.0+44.8±32.1
hier-base−hist+net+88.8±25.1−12.4±23.2+41.4±22.8+32.9±17.7+22.5±13.5+35.9±24.0
hier-delib−best-SR † +2.4±10.3-33.0±30.1-86.5±22.3+25.4±15.0-57.8±28.6+6.3±9.0

## Page 25

Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA
Figure 22: Score distributions by design axis. Violins show
full distribution with mean and median. Context configs
have the widest spread.
Figure 23: Score distribution shift. Density ridges comparing
the continuous probability distribution of episode returns
for the Anchor baseline (blue) versus +COT (orange).
Figure 24: Risk vs. Reward stability frontier. Shifts show how
adding +COT changes both the mean return and variance.
Ideally, arrows move up and to the left.
Figure 25: Outcome breakdown for the +COT configura-
tion. Shows the percentage of episodes resulting in success,
mediocre failure, or catastrophic failure.
Figure 26: Token cost progression from cheapest ( obs) to most
expensive (hier-delib). Deliberation and hierarchy dramati-
cally increase token consumption; the deliberation cascade
represents the cost ceiling.

## Page 26

ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA Bogdanov et al.
F Token Consumption
This appendix details per-model token profiles and token efficiency
across configurations. Tables 26 through 31 report a scalarshifted
return-per-kilotokenefficiency, ˜𝐺/KTok, where ˜𝐺= 225+𝐺converts
the non-positive episodic return 𝐺 into a non-negative "defense
score" (higher is better), and KTok is tokens per episode in thou-
sands. This scalar is provided as a compact summary; our primary
cost–performance comparisons use Pareto frontiers in the main
text. We also performed a pricing sensitivity check by re-weighting
token costs using provider-specific input/output pricing ratios. This
re-weighting did not reverse any qualitative conclusion; it narrowed
the relative cost advantage of context over hierarchy because sim-
pler context configurations contain a higher share of output tokens,
but the qualitative ordering was preserved.
Table 32 breaks down the prompt vs. completion token split
for the anchor baseline and the +COT configuration. Deliberation
dramatically increases prompt tokens (due to multi-turn tool-call ex-
changes) and moderately increases completion tokens. The prompt-
to-completion ratio shifts from roughly2–24 ×at baseline to4–31 ×
under +COT, indicating that deliberation overhead is dominated by
the expansion of the conversational context rather than by longer
model outputs.
Figure 27 visualizes the prompt/completion breakdown. Figure 28
shows the exponential increase in token consumption as delibera-
tion levels are added. Figure 29 plots the token-cost multiplier of
+COT against its per-instance win rate over the anchor: models
where +COT achieves high win rates (Grok, G2.5FL) pay 4–5×more
tokens, while models where +COT is harmful (Llama) pay a similar
multiplier for worse outcomes.
Table 26: Token efficiency: Grok. Shifted return-per-KToken
( ˜𝐺/KTok, higher is better), where ˜𝐺= 225 +𝐺 converts the
non-positive return 𝐺into a non-negative defense score. The
most efficient configuration by this scalar is bolded (Pareto
efficiency is analyzed in the main text).
Config Return Tok/ep ˜𝐺/KTok
obs−98.417.7K 7.1525
obs+hist−89.934.6K 3.9046
obs+hist+net−81.933.5K 4.2716
obs+net−47.020.9K8.5167
network−86.320.2K 6.8663
hist+net−112.929.1K 3.8522
+question−66.555.6K 2.8507
+critique−44.974.7K 2.411
+improve−53.4154.0K 1.1143
+COT−42.9144.5K 1.2602
hier-base−24.0141.9K 1.4165
hier-delib−40.4364.1K 0.507
G Trajectory Examples
We present a paired trajectory comparison from Devstral on in-
stance 7, illustrating the deliberation cascade failure mode described
Table 27: Token efficiency: Llama. Shifted return-per-KToken
( ˜𝐺/KTok, higher is better), where ˜𝐺= 225 +𝐺 converts the
non-positive return 𝐺into a non-negative defense score. The
most efficient configuration by this scalar is bolded (Pareto
efficiency is analyzed in the main text).
Config Return Tok/ep ˜𝐺/KTok
obs−214.78.8K 1.1705
obs+hist−137.419.2K 4.5625
obs+hist+net−102.630.6K 4
obs+net−51.412.3K14.1138
network−68.713.0K 12.0231
hist+net−57.128.6K 5.8706
+question−104.184.1K 1.4376
+critique−93.497.8K 1.3456
+improve−75.0115.3K 1.301
+COT−100.8131.3K 0.9459
hier-base−69.587.7K 1.7731
hier-delib−108.0158.1K 0.74
Table 28: Token efficiency: Devstral. Shifted return-per-
KToken ( ˜𝐺/KTok, higher is better), where ˜𝐺= 225 +𝐺 con-
verts the non-positive return 𝐺 into a non-negative defense
score. The most efficient configuration by this scalar is bolded
(Pareto efficiency is analyzed in the main text).
Config Return Tok/ep ˜𝐺/KTok
obs−155.122.2K 3.1486
obs+hist−133.926.4K 3.4508
obs+hist+net−85.325.1K 5.5657
obs+net−72.615.4K9.8961
network−93.314.9K 8.8389
hist+net−79.321.3K 6.8404
+question−53.960.4K 2.8328
+critique−62.8106.9K 1.5173
+improve−80.6153.1K 0.9432
+COT−40.9157.4K 1.1696
hier-base−37.897.0K 1.9299
hier-delib−127.4257.7K 0.3787
Figure 27: Token profile shift. Stacked bars show prompt
(solid) vs completion (hatched) for anchor and +COT. Delib-
eration increases both components.

## Page 27

Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA
Table 29: Token efficiency: Qwen. Shifted return-per-KToken
( ˜𝐺/KTok, higher is better), where ˜𝐺= 225 +𝐺 converts the
non-positive return 𝐺into a non-negative defense score. The
most efficient configuration by this scalar is bolded (Pareto
efficiency is analyzed in the main text).
Config Return Tok/ep ˜𝐺/KTok
obs−218.210.3K 0.6602
obs+hist−93.419.0K 6.9263
obs+hist+net−69.018.7K 8.3422
obs+net−63.111.4K14.2018
network−109.410.6K 10.9057
hist+net−61.516.4K 9.9695
+question−92.345.7K 2.9037
+critique−93.668.9K 1.9071
+improve−92.4115.9K 1.1441
+COT−55.6162.4K 1.0431
hier-base−28.679.6K 2.4673
hier-delib−30.1209.9K 0.9285
Table 30: Token efficiency: G2.5FL. Shifted return-per-
KToken ( ˜𝐺/KTok, higher is better), where ˜𝐺= 225 +𝐺 con-
verts the non-positive return 𝐺 into a non-negative defense
score. The most efficient configuration by this scalar is bolded
(Pareto efficiency is analyzed in the main text).
Config Return Tok/ep ˜𝐺/KTok
obs−214.768.1K 0.1512
obs+hist−172.9125.2K 0.4161
obs+hist+net−147.894.0K0.8213
obs+net−200.079.4K 0.3149
network−215.494.4K 0.1017
hist+net−208.781.7K 0.1995
+question−206.2104.8K 0.1794
+critique−128.6118.2K 0.8156
+improve−168.9182.9K 0.3067
+COT−157.0225.7K 0.3013
hier-base−183.1120.6K 0.3474
hier-delib−186.4270.5K 0.1427
in Section 5.2.3. Both episodes use identical model weights, environ-
ment seed, and hist+net context. The only difference is whether
deliberation tools are distributed across the hierarchy.
Episode identification.The hier-base episode achieves a return
of −13.3(near-optimal defense); the hier-delib episode achieves
−211.2(near-total network loss), a15 .9×degradation on the same
environment instance. Table 33 summarizes the behavioral contrast.
Mechanism: distributed caution bias.The trajectories reveal a
failure mode we termdistributed caution bias, a concrete instan-
tiation of the cascading-uncertainty mechanism discussed in Sec-
tion 5.2.3. When each agent independently runs a deliberation cycle
(raise_a_question →critique →improve), each cycle independently
converges on the conservative option: investigate further, deploy
Table 31: Token efficiency: G3FP. Shifted return-per-KToken
( ˜𝐺/KTok, higher is better), where ˜𝐺= 225 +𝐺 converts the
non-positive return 𝐺into a non-negative defense score. The
most efficient configuration by this scalar is bolded (Pareto
efficiency is analyzed in the main text).
Config Return Tok/ep ˜𝐺/KTok
obs−96.88.0K16.025
obs+hist−76.315.4K 9.6558
obs+hist+net−82.619.4K 7.3402
obs+net−113.79.0K 12.3667
network−136.47.9K 11.2152
hist+net−52.018.0K 9.6111
+question−100.630.7K 4.0521
+critique−66.441.0K 3.8683
+improve−64.058.1K 2.7711
+COT−29.975.1K 2.5979
hier-base−16.156.4K 3.7039
hier-delib−23.6104.8K 1.9218
Figure 28: Token generation velocity. Shows the exponential
increase in token usage as cumulative deliberation capabili-
ties are added.
passive defenses, defer reactive intervention. No individual agent’s
reasoning is incorrect, the Analyst’s hedge is reasonable, the Ac-
tionChooser’s caution is defensible, the Planner’s self-questioning
is thoughtful. But thecompositionof three independently cautious
agents produces a system that never intervenes until catastrophic
damage has accumulated. The failure is structural: the absence of an
urgency-propagation mechanism that would override local caution
when system-level evidence demands immediate action.
Showcase: Step 18 (hier-delib).At step 18, the network has been
losing −13.1reward per step since step 15 (Op_Server0 is compro-
mised). The Planner’s reasoning trace proceeds as follows. (Excerpts
are lightly trimmed for space)
[Step 18, hier-delib, reward: -13.1]
Planner (thought): User4 has been analyzed twice
and has decoys deployed. The other hosts have

## Page 28

ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA Bogdanov et al.
Table 32: Token Profile Shift. Average prompt and completion tokens per episode for the Anchor baseline vs. +COT.
Anchor Baseline +COT
Model Prompt Compl Total P/C Prompt Compl Total P/C
Grok 20.7K 8.4K 29.1K 2.5× 117.7K 26.8K 144.5K 4.4×
Llama 27.0K 1.6K 28.6K 16.9× 126.7K 4.5K 131.3K 28.0×
Devstral 20.4K 1.0K 21.3K 21.3× 152.5K 4.9K 157.4K 31.2×
Qwen 15.8K 0.7K 16.4K 23.8× 156.8K 5.6K 162.4K 28.1×
G2.5FL 75.8K 5.8K 81.7K 13.1× 206.8K 18.9K 225.7K 11.0×
G3FP 17.2K 0.7K 18.0K 23.5× 71.0K 4.0K 75.1K 17.6×
Figure 29: Cost vs. Win Rate. Plots the token cost multiplier
of using +COT against the resulting win rate against the
Anchor baseline.
Table 33: Behavioral comparison: Devstral instance 7,
hier-base vs. hier-delib. The only architectural difference
is the distribution of deliberation tools across the hierarchy.
Metric hier-base hier-delib
Episode return−13.3−211.2
Restore actions 12 1
Remove actions 5 0
Decoy deployments 0 13
Monitor actions 3 7
Delib. tool calls (Planner) 0 11
AC msgs / invocation 2.0 6.6
Analyst invocations 14 5
Steps at≤−13/step 0 16
First Restore action step 4 step 25
similar setups. The next strategic step is to
ensure all hosts are consistently protected...
Planner -> raise_a_question: "Should I focus on
monitoring the network or re-analyzing User4?"
Planner (thought): I need to critique my own
reasoning to ensure I'm making the best decision.
Planner -> critique_the_answer: "My initial thought
is to either monitor or re-analyze User4.
However, I should consider whether there are
other hosts that might need attention..."
Planner -> improve_based_on_critique: "Monitoring
the network is the more strategic action. It
will provide a broader view of potential threats
and ensure all hosts are observed for anomalies."
Planner -> get_suggestion_for_next_action:
{"target_host": "User4", "severity": "low", ...}
ActionChooser (8 msgs, own deliberation cycle):
-> raise_a_question: "What would be the
appropriate strategy for User4?"
-> critique: "Have I considered the potential
need for reactive interventions?"
-> improve: "Balance passive and proactive..."
Returns: [Monitor (high), Analyse (medium),
Restore (low)]
Planner (final): Answer: Monitor
The Planner uses three deliberation tools before consulting the
ActionChooser. The ActionChooser runs its own three-phase delib-
eration cycle. Ten messages are exchanged to arrive at "Monitor",
a passive action, while the network loses 13.1 reward points. The
Analyst is not consulted at all at this step.
Contrast: Step 18 (hier-base).In the same episode phase, the
hier-base agent operates with a clean network (all hosts at base-
line, reward = 0.0) because it contained threats via timely Restore
actions at steps 4, 6, 8, 11, and 14. Its step-18 trace is four messages:
[Step 18, hier-base, reward: 0.0]
Planner (thought): Network is stable, all hosts in
baseline state. Enterprise2 was recently restored;
analyzing it again could confirm its integrity.
Planner -> get_suggestion_for_next_action:
{"target_host": "Enterprise2",
"situation": "restored, confirm integrity",
"severity": "low", ...}
ActionChooser (2 msgs): Returns:
[Analyse (high), DecoySSHD (medium),
Restore (low)]
Planner (final):

## Page 29

Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP ACM CAIS ’26, May 26–29, 2026, San Jose, CA, USA
Answer: Analyse hostname=Enterprise2
No deliberation tools are invoked. The Planner identifies the most
useful proactive action and executes it in a single delegation round.
The ActionChooser returns its recommendation in one exchange
without a critique cycle.
The critical divergence.The behavioral divergence begins at step 7.
Both systems detect changes on Enterprise0 and User4. Thehier-base
Planner, at steps 3–8, follows a tight detect–analyse–restore cy-
cle: upon finding C2 indicators (connection to port 4444, backdoor
process), it immediately requests suggestions and acts on the high-
confidence "Restore" recommendation. The hier-delib Planner,
facing the same situation, invokesinclude_tool_raise_a_question
("What is the most strategic action?"),
then include_tool_critique_the_answer ("Should I deploy a
DecoySSHD or prioritize Enterprise0?"), and resolves toward pro-
phylactic decoy deployment rather than reactive containment. By
step 14, thehier-base system has executed 5 Restore and 3 Remove
actions; the hier-delib system has executed 0 Restore, 0 Remove,
and 8 Decoy deployments. The reward gap at step 14 is −6.3vs.
−14.2.
The gap becomes irreversible at step 15, when the red agent
escalates to high-value targets. The hier-delib system, having de-
ployed passive defenses rather than containing active compromise,
faces a−13.1/step penalty that persists for the remaining 16 steps.
It does not execute its first (and only) Restore until step 25.
H CybORG CAGE-2 Environment Details
CybORG CAGE-2 [19, 22] models an autonomous network-defense
scenario used as Challenge 2 of the TTCP CAGE (Cyber Auton-
omy Gym for Experimentation) series. We summarize the key en-
vironment characteristics; full specifications and source code are
available at https://github.com/cage-challenge/cage-challenge-2.
Network topology.The simulated network comprises 13 hosts
organized into three subnets:User(User0–User4, 5 hosts),Enterprise
(Enterprise0–Enterprise2 plus a single Enterprise Server, 4 hosts),
andOperational(Op_Host0–Op_Host2, Op_Server0, 4 hosts). Traf-
fic flows from an Internet-facing subnet through User to Enterprise
to Operational. Op_Server0 is the attacker’s ultimate high-value
target.
Attacker (Red agent).The red agent follows a scripted kill chain
that progresses through five stages:Discovery(scanning for reach-
able hosts),Access(exploiting vulnerabilities to gain initial foothold),
Lateral Movement(pivoting across subnets),Privilege Escalation
(gaining root/admin access), andImpact(compromising high-value
targets for maximum penalty). The attacker advances one stage
per step and selects new targets based on reachability. The scripted
policy is fixed across all experiments; no adaptive adversary is used.
Defender actions.The blue agent (defender) selects one action
per step from a five-type repertoire:
Monitor (free, observational): Observe the network. Returns
the current observation with no side effects.
Analysehostname=X (free, diagnostic): Deeper inspection of
a host. Returns process- and connection-level details that
may reveal compromise indicators not visible in the standard
observation.
Removehostname=X (attempted cleanup): Attempt to remove
malicious artifacts from a host. May fail against persistent
threats, leaving the host in an "unknown" state.
Restorehostname=X (guaranteed cleanup, high penalty): Re-
set the host to its known-good baseline. Guaranteed to suc-
ceed, but incurs a large one-step penalty and removes all
deployed decoys from that host.
DecoySERVICEhostname=X (proactive): Deploy a decoy ser-
vice (e.g.,DecoySSHD, DecoyApache, DecoyTomcat) on a host
to attract and detect attacker activity in future steps. Multiple
decoy types can be stacked on a single host.
Reward structure.The per-step reward 𝑟𝑡 ≤0penalizes each com-
promised host according to its value tier; Operational hosts carry
the highest penalties. Restore incurs an additional fixed penalty
at the step it is applied. The maximum cumulative return (per-
fect defense) is0; all configurations operate in the negative-return
regime.
Episode structure.Each episode runs for 𝑇= 30steps. The at-
tacker begins with access to the Internet-facing subnet and pro-
gresses inward. The defender observes partial, noisy information
and must infer compromise from limited signals. Early intervention
is rewarded because attacker progress compounds: a compromised
User host enables lateral movement to Enterprise, then to Opera-
tional targets where penalties are highest.
I Episode Counts
Table 34 reports the number of evaluated episodes for each of the 72
model–configuration pairs. The standard allocation is10instances
×5runs = 50episodes per pair. G3FP uses a reduced default of5×5 =
25episodes per configuration due to staged data collection. Several
configurations include extended batches (marked with †) to reduce
uncertainty on key comparisons: G2.5FL obs+net (100 episodes),
Qwen hier-base (100 episodes), and G2.5FLhier-base (75 episodes).
The total across all models and configurations is 3,475 episodes
(104,250 agent–environment interaction steps, consuming 283.9M
tokens).
Table 34: Episode counts per model–configuration pair. Stan-
dard allocation is 10 instances ×5 runs = 50 episodes per
configuration.
Group Config Grok Ll Devs Qwen G2.5FL G3FP
Context obs 50 50 50 50 50 25
obs+hist 50 50 50 50 50 25
obs+hist+net 50 50 50 50 50 25
obs+net 50 50 50 50 100 † 25
network 50 50 50 50 50 25
hist+net 50 50 50 50 50 25
Delib. +question 50 50 50 50 50 50
+critique 50 50 50 50 50 25
+improve 50 50 50 50 50 25
+COT 50 50 50 50 50 25
Hier hier-base 50 50 50 100 † 75† 25
hier-delib 50 50 50 50 50 50
Total 600 600 600 650 675 350
†Configuration includes additional evaluation batches beyond the standard allocation.
