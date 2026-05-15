# Cognifold: Always-On Proactive Memory via Cognitive Folding - Extracted Text

- Source note: [[Cognifold - Always-On Proactive Memory via Cognitive Folding]]
- Source PDF: `assets/Cognifold - Always-On Proactive Memory via Cognitive Folding.pdf`
- Extracted: 2026-05-14
- Extractor: pypdf
- Pages: 23
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

COGNIFOLD: Always-On Proactive
Memory via Cognitive Folding
Suli Wang1,* Yiqun Duan1,*,B Yu Deng1,* Rundong Zhao1
Dai Shi1,2 Xinliang Zhou1,3
1OpenNorve 2University of Cambridge 3Stanford University
/githubGitHub
HuggingFace
Abstract
Existing agent memory remains predominantly reactive and retrieval-based, lacking
the capacity to autonomously organize experience into persistent cognitive structure.
Toward genuinely autonomous agents, we introduce Cognifold, a brain-inspired
"always-on" agent memory designed for the next generation of proactive assistants.
CogniFold continuously folds fragmented event streams into self-emerging cogni-
tive structures, bootstrapping progressively higher-level cognition from incoming
events and accumulated knowledge. We ground this by extending Complemen-
tary Learning Systems (CLS) theory from two layers (hippocampus, neocortex)
to three, adding a prefrontal intent layer. Emulating the prefrontal cortex as the
locus of intentional control and decision-making, CogniFold achieves this through
graph-topology self-organization: cognitive structures proactively assemble under
the stream, merge when semantically similar, decay when stale, relink through
associative recall, and surface intents when concept-cluster density crosses a thresh-
old. We evaluate structural formation using CogEval-Bench, demonstrating that
CogniFold uniquely produces memory structures that match cognitive expectations
and concept emergence. Furthermore, across 7 broad-coverage benchmarks span-
ning five cognitive domains, we validate that CogniFold simultaneously performs
robustly on conventional memory benchmarks.
1 Introduction
Memory-Augmented Agents [42, 54] have empowered Large Language Models (LLMs) to transcend
finite context constraints, enabling long-horizon reasoning [51], context-grounded personalization [6],
and experience-driven continual learning [33]. However, as agents evolve from on-demand systems
into always-on assistants, their input paradigm shifts from bounded, prompt-driven inputs to continu-
ously arriving, fragmented event streams [28, 65]. This creates an increasing demand forproactive
behaviour: an assistant that self-organizes structure, anticipates intent, and emits goals before the
user issues a query [13].
Yet, existing memory architectures share a common limit: their topology is fixed once formed.
Whether leveraging static knowledge graphs [19, 20], text-level rewrites [6], hybrid decoupling [23],
or temporal tracking [ 48], memory remains agraph-as-product—a finished artifact to retrieve
from, never a substrate thatmetabolisesunder the stream. Consequently, agents are forced to graft
proactivity on top as application-layer machinery, such as scheduled triggers, planning loops [61, 64],
or periodic reflection [51, 63]. This separation creates a structural ceiling: goals can only arise from
sources the application layer was explicitly designed to handle. We argue that proactivity must instead
∗Equal contribution.BCorresponding author:duanyiquncc@gmail.com
arXiv:2605.13438v1  [cs.AI]  13 May 2026

## Page 2

Lufthansa Info: Your flight LH123 to VIE on Dec 20 has been 
cancelled. We apologize for the inconvenience. Please check 
alternative options via our mobile app or our official website.
TIME: [10:01 AM]
My flight LH123 got 
cancelled. Could you 
help me find alternate 
flights around Dec 20th?
TIME: [11: 30 AM]
I've found the 
following 5 alternative 
flight options for you...
TIME: [11: 30 AM]
Notice: Your flight LH123 is 
cancelled. Would you like 
me to help you rebook? I've 
found 5 available options.
TIME: [10:30 AM]
Notice: Your flight LH123 is 
cancelled. Would you like 
me to help you rebook? 
I've found 5 available 
options.
[Relevant Events Reminder] 
Do you also need me to 
adjust your Vienna hotel 
reservation and cancel the 
Golden Hall concert?
TIME: 
[10:01 AM]
Reactive Agent
(Passive Retrieval)
Proactive Agent
(Grafted)
Proactive Agent
(CogniFold)
…
[CRON_TRIGGER]: Scheduled routine check (every 30 min) 
 1. Scan inbox/SMS/calendar since last tick (10:00).
 2. Extract entities and query user_memory (context). 
 3. If relevance_score > threshold, generate proactive 
alert.
TIME: [10: 30 AM][Sleeping]
Figure 1:From reactive to proactive agent memory.Conventional agents wait for explicit
user queries (left) or graft delayed, application-layer triggers onto a reactive memory (middle). In
contrast, COGNIFOLD(right) processes unprompted, asynchronous events instantly within its memory
substrate, simultaneously reactivating related dormant concepts (e.g., the Vienna hotel and concert).
be a property of the memory substrate—goals should emerge from the topology accumulating the
conditions for them.
Human biological memory is evolutionarily adapted to exactly this setting: it continuously receives
sensory input to autonomously encode, consolidate, forget, and surface intentions in the background.
Inspired by this, we proposeCOGNIFOLD, a proactive always-on agent memorythat folds
continuously arriving events into self-emerging cognitive structure. COGNIFOLDbootstraps in a
strict sense: the graph’s current state is the interpretive context for the next event, which in turn
modifies the state for future events—a self-referential loop in which the system organises input
entirely through its accumulated structure. COGNIFOLDrests on two complementary perspectives.
From theneuralside, we extend Complementary Learning Systems (CLS) theory [ 26, 35] from
two layers (hippocampus, neocortex) to three by adding aprefrontal Intent layer; rather than
being hardcoded [4], intents autonomously emerge once concept-cluster density crosses a threshold.
From thecognitiveside, the graph is a substrate forconceptual bootstrapping[ 5, 66]: recursively
scaffolding higher-level cognition from accumulated structure—a transparent, auditable form of
test-time learning, distinct from both surface-level text rewriting (e.g., A-Mem [ 63]) and opaque
gradient updates (e.g., Titans [2]).
We conduct a two-layer evaluation. At thestructurallayer, we introduce CogEval-Bench, a first-
principles evaluation framework that directly measures whether the topology formed under continuous
event streams matches cognitive expectations, demonstrating that COGNIFOLDuniquely produces
event-grounded concepts, coherent conceptual structure, and proactive intent emergence. At the
downstreamlayer, we evaluate across seven benchmarks spanning five cognitive domains, confirming
that COGNIFOLDsimultaneously performs competitively on conventional memory tasks.
Our contributions are summarized as follows:
• Always-On Proactive Memory Paradigm.We recast agent memory from a reactive retrieval
target into an always-on cognitive substrate (Fig. 1), natively supporting continuous understanding
and proactive anticipation.
• Tri-Layered Cognitive Architecture.We extend the two-layer CLS framework with a prefrontal
Intent layer, enabling self-emerging intents from accumulated concepts.
• Continuous Topological Self-Organization.We identify and algorithmically resolve four intrinsic
structural debts of streaming events via transparent graph-level operations, yielding a transparent
and auditable form of test-time learning.
2

## Page 3

10: 15
09: 45
09: 35
09: 25
09: 10
Hippocampal Layer
EVENT
NODE
Hippocampus
Episodic
Encoding
Neocortical Layer
Neocortex
Semantic
Consolidation
EVENT
…
… CONCEPT
NODE
EVENT
Prefrontal Layer
Prefrontal
Cortex
(vmPFC)
INTENT
NODE
Emergence
EVENT
TIMEINTENT
CONCEPT
TIME
GROUNDS
TRIGGERS
TRIGGERS
GROUNDS DEADLINE_FORTRIGGERS
NODE 
INTERACTION
2 3 
1 2 3 ACCUMULATING CONSOLIDATING CRYSTALLIZATING
COGNITIVE FOLDING LOOP
09: 01
EVENT STREAM
1 
Intent Layer
Concept Layer
Event Layer
TRI-LAYER INTERACTION
Top-
Down
Bias
GROUNDS REINFORCE
TRIGGERS RELATE_TO
Figure 2:The COGNIFOLDArchitecture: Conceptual Bootstrapping via Tri-Layered Cognitive
Folding.Extending the Complementary Learning Systems (CLS) framework, the memory substrate
continuously metabolizes streaming events through three stages: accumulating raw episodic traces
(Hippocampal layer), consolidating redundant patterns into semantic concepts (Neocortical layer),
and crystallizing intents (Prefrontal layer).
• CogEval-Bench Evaluation Framework.We release a structural diagnostic evaluation framework
that isolates proactive emergence from retrieval accuracy. Alongside seven established downstream
benchmarks, we jointly validate COGNIFOLD’s effectiveness in both high-level cognitive emergence
and conventional memory robustness.
2 CogniFold: From Neural Layers to Conceptual Bootstrapping
An always-on agent requires a fundamentally different memory substrate. Continuously arriving event
streams demand an architecture capable of incremental, online integration. A genuinely autonomous
assistant must transition from reactive retrieval toproactive assembly—continuously capturing
implicit intents and organizing relevant cognitive structures in the background. COGNIFOLDgrounds
this substrate in an extended Complementary Learning Systems (CLS) theory, formalizing memory
as a dynamically evolving, typed multigraph.
2.1 Tri-Layer Substrate
Human declarative memory is organized byComplementary Learning Systems(CLS) [ 26, 35]: the
hippocampus rapidly encodes sparse, episode traces [34, 41, 52], while the neocortex slowly distills
statistical regularities into semantic representations [45, 59]. This division is dynamic: over time,
long-term storage shifts from the hippocampus to the medial prefrontal cortex (mPFC) [3, 15].
Crucially, the mPFC is not a passive recipient. It exerts top-down control over the hippocampus
via pre-existing knowledge frameworks (schemata) to actively shape which hippocampal traces are
retained and how they are organized [9, 58]. This bidirectional dialogue, in which the mPFC imposes
schematic frameworks to guide subsequent encoding, forms the biological substrate from which
goal-directed memory emerges [12, 47, 60].
COGNIFOLDoperationalizes the three-layer dialogue above as a typed, dynamically evolving multi-
graph.Eventnodes play the hippocampal role: each input from the stream is committed verbatim
and time-stamped—an immutable episodic trace.Conceptnodes play the neocortical role: recurrent
patterns are abstracted into schemata, anchored to their constituent events through provenance edges.
Intentnodes play the prefrontal role: when concept-level evidence converges into a coherent goal, an
intent emerges and exerts top-down influence on how subsequent events are surfaced and encoded.
Yet, static layers are insufficient. Structure is merely the container of cognition; the vitality of memory
lies in itsmetabolism. This brings us to the architectural dynamic at the core of COGNIFOLD:
conceptual bootstrapping.
3

## Page 4

Table 1:Edge types.Each edge type maps to a specific cognitive/biological motif (CLS Analogue
column). Default weights are reported in Appendix B.
Edge Type Semantics CLS Analogue
GROUNDSEvent evidences concept/intent Episodic grounding [35]
CAUSESEvent causes event Causal encoding
TRIGGERSConcept triggers intent Goal activation [13]
REINFORCESEvent supports concept Synaptic LTP [21]
PART_OFStructural hierarchy Hierarchical binding [12]
DERIVED_FROMConcept abstraction Schema generalization [1]
DEADLINE_FORTemporal constraint Prospective memory [13]
RELATED_TOAssociative link Associative memory [35]
USER_FEEDBACKFeedback→intent Valence signal
2.2 Dynamics: Conceptual Bootstrapping
If the neuro perspective specifies the structural layers, conceptual bootstrapping [5, 66] specifies how
an agent “pulls itself up by its own bootstraps” on top of them. In COGNIFOLD, this self-referential
dynamic unfolds throughcontinuous foldingin three stages.
Stage 1: Accumulation.The hippocampal layer (Eventnodes) ingests the raw stream verbatim.
Events initially function as cognitiveplaceholders: raw experiential fragments committed before
their overarching concepts exist.
Stage 2: Consolidation.As events accumulate, the system detects statistical regularities across them
andconsolidatesthem into the neocortical layer: discrete Event nodes are folded intoConceptnodes
anchored to their grounding events.
Stage 3: Crystallization.Concepts then act as active scaffolds for future input: incoming events are
interpreted through them rather than from scratch. When concept-cluster density crosses a threshold,
the bootstrap iterates upward—anIntentnodecrystallizesin the prefrontal layer, providing top-down
bias for schema-congruent encoding. The loop closes: structure interprets experience, and experience
reshapes structure.
The synergy between neural structure and cognitive dynamic enables COGNIFOLDtometaboliselike
biological memory: continuously folding to eliminate redundancy (compression) and bootstrapping
to climb levels of abstraction, sustaining cognitive agility under an always-on event stream.
2.3 Graph Formalization
Having grounded COGNIFOLDin neurobiological mapping (§2.1) and cognitive dynamics (§2.2), we
now formalise the substrate as a typed directed multigraph G= (V,R) with four node types and nine
semantic edge types (Table 1).
Node types. Event(episodic trace),Concept(semantic pattern),Intent(crystallized goal), andTime
(temporal anchor). The first three correspond to the CLS layers;Timeis an auxiliary type connecting
temporal obligations to intents viaDEADLINE_FORedges.
Edge ontology.Nine typed edges encode distinct semantic relations (Table 1), each mapping to
a specific cognitive motif. This typed ontology constrains the LLM’s update proposals toward
meaningful topology, reducing the hallucination-driven bloat of free-form extraction.
Write/read decoupling.The architecture decouples graph expansion from query execution. The
write path (§3.1, §3.3) specifies topology-evolution operations that run on every incoming event; the
read path specifies multi-strategy retrieval over the graph snapshot (parameters in Appendix B). This
ensures formation and retrieval can be diagnosed independently.
3 Continuous Cognitive Folding
Reactive memory architectures enjoy considerable design slack: ingestion is bound to user turns,
consolidation can be deferred offline, and retrieval is the only operation under latency pressure. A
4

## Page 5

1. Dormant Substrate
Morning
Health Routine
2. Reactivation
Coach 
reminder: 
morning 
weigh-in
Agent
Good morning! 
The scale is 
calling your 
name. Don't 
forget your 
morning 
supplement 
stack.
Morning
Health Routine Weight
Monitoring
Agent
Logged. I've 
initiated your 
weekly weight 
trend monitor.
USER
65.9 this 
morning.
3. First intent
Monitor
weekly weight
trend
65.9 this
morning
4. Reactivation + merge
Supplement
Routine
Took
creatine /
zinc /
omegaMorning
Stack
Supplement
Intake
merge
USER 
Grabbing a 
Core Power 
shake on the 
way out.
5. Second Intent
Morning
Health Routine
Weight
Monitoring
Protein
Intake Focus
Macro
Tracking
Supplement
Routine
Grabbing
Core
Power
Took
creatine /
zinc /
omega
USER
Grabbed a 
McMuffin for 
breakfast. 
Skipped the 
hash brown.
Agent
Logged. 
Factoring the 
macros into 
today's 
allowance.
6. Episodic Accumulation
Morning
Health Routine
Weight
Monitoring
Protein
Intake Focus
Macro
Tracking
Supplement
Routine
McMuffin, 
no hash 
brown
4. Merge
Hit daily 
protein target 
(140g+)
7. Top-Down Bias
Morning
Health Routine
Weight
Monitoring
Protein
Intake Focus
Macro
Tracking
Hydration
Tracking
Supplement
Routine
McMuffin, 
no hash 
brown
Took
creatine /
zinc /
omega
Grabbing
Core
Power
First 
refill 
done
8. Temporal Decay 9. Contextual Reactivation
Morning
Health Routine
Weight
Monitoring
Protein
Intake Focus
Macro
Tracking
Hydration
TrackingPerformance
Nutrition
Supplement
Routine
Thinking of 
getting a 
McMuffin 
again
Took
creatine /
zinc /
omega
Grabbing
Core
Power
Monitor
weekly weight
trend
Agent
You had one on 
Monday. Since 
we are 
monitoring 
your weekly 
weight trend 
and aiming for 
140g+ protein, 
maybe grab a 
Greek yogurt 
instead?
Hit daily 
protein target 
(140g+)
First 
refill 
done
Event
Concept
Intent
Dormant
Related-to
Grounding
Triggers
Agent
Recorded. 
Your 
supplement 
routine is on 
track.
USER
Took my 
morning stack: 
creatine, zinc, 
and omega.
USER
First water 
refill done. 
Should I do 
salmon or 
chicken for 
lunch?
Agent
Go with 
chicken. You 
need the 
higher protein 
density to hit 
your 140g 
target today.
Coach 
reminder
Agent
Strong start. 
With this, I'll 
track your 
daily goal 
towards the 
140g+ protein 
target.
USER STATE
On vacation (No 
health events).
USER
Thinking of 
grabbing a 
McMuffin 
again this 
morning.
Figure 3:Continuous cognitive metabolism.Under an asynchronous event stream, the memory
substrate dynamically self-organizes. The graph autonomously consolidates episodic events (Panel 3),
merges associated schemata (Panel 4), and crystallizes goal-directed intents from converging concept
density (Panel 5). This living topology natively supports top-down cognitive bias (Panel 7), natural
temporal decay (Panel 8), and structure-driven proactive intervention (Panel 9).
proactive, always-on agent has none of these. Events arrive continuously and asynchronously, working
memory stays bounded, and the next query may concern structure that has not yet been formed—all
between user touchpoints. The graph must therefore mutate in place under a stream that never pauses;
topology must keep paying down the four structural debts—accumulation, compression, decay,
completion—that any continuously evolving graph naturally accrues; and a proactive agent must
assemble relevant context before being asked, which forces structural centrality, temporal recency,
and usage intensity to be treated as simultaneous hard constraints rather than retrieval-time heuristics.
Three mechanisms purpose-built under these pressuresoperationalise conceptual bootstrapping
(§2.2) under the stream: a proactive context-assembly harness on the write path (§3.1), automatic
topology-evolution operations that discharge the four debts (§3.2), and an intent-emergence stage
that crystallizes goals from converging concept evidence (§3.3).
3.1 Proactive Context Assembly
The working-memory constraint is Miller’s classical capacity bound [ 38] transposed to an agent:
each encoding step can only reason over a tiny subset of accumulated knowledge. This imposes a
priority allocation problemon the write path: the system must select which subset of the existing
graph the LLM sees when interpreting the next event.
Priority is allocated through three signals, each anchored in a distinct cognitive memory tradition.
Structural centrality—how embedded a node is in the cognitive graph—follows the Personalized
PageRank tradition [19]; we extend it from retrieval into the write path because what the LLM sees
during encoding directly shapes what it writes, making centrality a formation-time prior rather than
only a query-time signal.
Temporal recency—whether a trace is still fresh—follows the Ebbinghaus forgetting curve [10],
applied to LLM memory in MemoryBank [68]; the same exponential kernel governs our write-path
priority so that stale schemata do not perpetually crowd out new evidence.
5

## Page 6

Access intensity—how often a node has been re-engaged—is a Hebbian signal [ 21]: nodes that
repeatedly co-fire with the agent’s working context wire more strongly into the next context, akin to
the access-count heuristic in Mem0 [6] but lifted from a passive tally to an active scoring term.
These three signals compose linearly into a per-node priority:
Score(v) =

α·PR(v) +β·exp(−λ·∆t v) +γ·Acc(v)

·U(v)(1)
where U(v)≥1 is a deadline-driven urgency multiplier from connectedTimenodes; weights are
reported in Appendix B.
The resulting scores define aproactive context window: structurally central, temporally fresh, and
frequently used knowledge surfaces before the next event is interpreted—rather than waiting for
a later query to reveal what should have mattered. Selected nodes are partitioned into Immediate,
Working, and Background tiers (proportions in Appendix B), forcing the LLM to process et within a
layered subgraph rather than in isolation.
Given the assembled context, an LLM central executive emits an UpdatePlan: a sequence of atomic
operations (ADD_NODE, ADD_EDGE, UPDATE_NODE, MERGE_NODES, REMOVE_NODE), each carrying
natural-language reasoning and grounded_in provenance. The executor validates and applies the
plan atomically with snapshot-based rollback, and near-duplicate concepts (above a title-similarity
threshold; see Appendix B) are silently converted to reinforcement updates to prevent bloat from
redundant events.
3.2 Four Structural Debts
Continuous event arrival is not a neutral inflow: by the nature of the input, a memory graph ac-
cumulates four kinds of structural debt over time. These are not design choices but mandatory
state-change operations imposed by the stream; any always-on memory that fails to address any
one of them degrades along the corresponding axis. COGNIFOLDaddresses all four as automatic
graph-level operations, executed without per-step LLM supervision in a consolidation pass inspired
by sleep-dependent consolidation [53].
1. Accumulation—persistent patterns must strengthen; one-off noise must not. Without it, a one-
off event and a recurring concept reach equivalent PageRank. Our operation: when a new
event corroborates an existing concept, the system creates a REINFORCES edge rather than a
duplicate node, boosting that concept’s in-degree and PageRank—implementing Bartlett’s schema
assimilation [1] as a graph operation.
2. Compression—redundant fragments must fold. Without it, graph size grows with |events|,
PageRank diffuses across duplicates, and evidence that should aggregate stays fragmented. Our
operation: when two concept nodes exceed a semantic-similarity threshold (Appendix B), the
executor automatically merges them (MERGE_NODES); the higher-access node absorbs all edges.
This implements schema unitization [17] and physically shortens graph-theoretic distances—multi-
hop chains collapse to direct adjacency.
3. Decay—aged structure must weaken. Without it, there is no forgetting; stale connections dominate
attention, and “recent” becomes indistinguishable from “active”. Our operation: all edges undergo
exponential decay at every consolidation pass, following MemoryBank’s [68] application of the
Ebbinghaus curve.
4. Completion—connections invisible to a local LLM view must be inferred. Without it, the LLM
sees only the current event plus its context window and cannot know that a concept created now
should connect to one created three sessions ago; cross-session structure fragments into orphans.
Our operation: kNN inference over concept embeddings (parameters in Appendix B) scans for
zero-edge concept nodes and creates GROUNDS connections—automatically repairing gaps the
LLM’s local-view planning misses.
Prior systems address each debt at most partially (Appendix C, Table 12): HippoRAG covers a
narrow form of completion via synonym edges; Mem0 performs write-time dedup without post-hoc
consolidation or decay; MAGMA’s slow-path inference densifies an ingested batch but does not
reinforce, compress, or decay; A-Mem and PREMem operate at the text-rewrite layer and never
modify graph structure. COGNIFOLDis the first agent-memory system to address all four debts as
automatic, topology-level operations—the mutually-reinforcing cycleREINFORCES→MERGE_NODES
6

## Page 7

→ kNN completion, balanced by edge decay. Why graph-level and not text-level or gradient-level?
Text rewriting updates the content of a note while leaving graph-theoretic distance, PageRank, and
reasoning paths invariant; gradient-based memory updates weights that cannot be inspected, audited,
or selectively deleted [36]. Only topology change makes memory’s internal geometry both mutable
and inspectable.
3.3 Intent Emergence
Intentnodes emerge when concept-cluster density crosses a threshold [ 13, 17]: converging evidence
across multiple concepts signals an unmet goal, and the LLM crystallizes it as an intent linked to its
supporting concepts via TRIGGERS edges. Each intent follows a lifecycle (pending→resolved|
rejected|deferred) that provides goal-directed organization for always-on agents.
A per-category EMA loop calibrates the emission threshold from accept/reject/defer/modify feedback:
w(t)
c = (1−α ema)·w (t−1)
c +α ema ·s t,(2)
where st maps each feedback type to a numeric score (Appendix B). Categories the user consistently
accepts see lowered thresholds; rejected categories are suppressed—prediction-error correction [7, 16]
applied to intent generation rather than model weights.
Under the single-session QA protocols of §4, concept-cluster density never reaches the emission
threshold, so intents are not triggered there. In the controlled multi-domain streams of CogEval-Bench
(§4.5), the threshold is reached repeatedly and intent emission is measured directly (Proactivity 0.614).
4 Experiments and Results
4.1 Datasets
Proactive Evaluation.QA accuracy alone cannot validate the central claim that cognitive structures
emerge from event-stream folding—a flat RAG system with strong BM25 can score well on factual
QA without forming any concepts, and a verbatim event store can pass multi-hop retrieval without any
compression. We therefore introduceCogEval-Bench, a structural diagnostic benchmark. CogEval-
Bench usestop-down generation: for each scenario a gold concept graph G∗ = (C∗,R∗,H∗,I ∗)
is specified first (concepts, inter-concept relations, hierarchy parents, expected intents, and planted
multi-hop chains), then grounded first-person events are generated from it, followed by distractor
injection (10–15%) and temporal shuffling. The benchmark spans 6 scenarios across 4 domains
(SoftEng, Health, Team, News, Academic, Support); scale statistics are reported in Appendix F.
Ground truth is establishedby constructionrather than through post-hoc annotation. Three evaluation
tracks are computed per system:Concept Emergence(Gold F1 via Hungarian-matched [ 25] soft-
matching, LLM Quality, Harmony, Purity),Relationship Topology(Chain Discovery, Clustering,
Modularity, Edge Type Entropy), andCompression & Proactivity(Compression Ratio, PageRank
Gini, Proactivity). Full schemas, generation prompts, and per-scenario breakdowns are in Appendix F.
Memory-Quality Evaluation.Downstream memory utility is evaluated across 7 broad-coverage
benchmarks spanning 5 cognitive domains: dialogue coherence (MuTual[ 8]), theory of mind
(ToMi[ 29]), multi-hop reasoning (MuSiQue[ 57]), narrative comprehension (NarrativeQA[ 24]),
streaming temporal QA (StreamingQA[ 31]), conversational memory (LoCoMo[ 32], full 10-
conversation Mem0 protocol), and long-context factual extraction (BABILong[ 27]). Per-benchmark
sample sizes, baselines, and detailed results are in §4.5 (Table 5 and Figure 4).
4.2 Baselines
Memory-Quality baselines.On LoCoMo, we compare against MIRIX [ 62], Mem0 [6], Zep [48],
Memobase [37], Supermemory [ 55], MemU [ 39], MemOS [ 30], and ENGRAM [ 44] under the
matched single-judge gpt-4o-mini Mem0 protocol; numbers come from Li et al. [30]’s public
reproduction for all but ENGRAM (taken from 44) and Zep (corrected reproduction [ 48]). On
MuSiQue, we adopt the standard graph-retrieval suite of Gutiérrez et al.[20]—BM25, Contriever, NV-
Embed-v2, RAPTOR [50], GraphRAG [11], LightRAG [18], HippoRAG [19], HippoRAG 2 [20]—
plus PolicyRAG [49]. On the remaining benchmarks we report against the most-cited published
baselines under each benchmark’s headline metric (Figure 4).
7

## Page 8

Table 2:CogEval-Bench: structural evaluation across 7 systems.Averages over 6 scenarios
(small scale, ∼42 events each). Track A measures concept quality, Track B measures graph topology,
Track C measures compression and proactivity. Arrows indicate preferred direction. All systems share
GPT-4o-mini and text-embedding-3-small; differences are attributable to architecture. Only
COGNIFOLDachieves non-zero purity and proactivity—structural properties absent from entity-level,
batch-processed, or text-rewrite representations. Bold: best; underline: second-best.
Track Metric OpenIE KG Cognee HippoRAG 2 GraphRAG Mem0 Zep COGNIFOLDTrack A
Harmony↑0.138 0.094 0.095 0.323 0.000 0.1380.476
Gold F1↑0.081 0.053 0.058 0.232 0.000 0.0810.358
LLM Quality↑0.492 0.454 0.341 0.541 0.000 0.494 0.733
Purity↑0.000 0.000 0.000 0.000 0.000 0.0000.361
Track B
Chain Disc.↑0.7501.0000.917 0.8331.000 † 0.917 0.833
Clustering↑0.005 0.2000.7160.002 0.382 0.704 0.327
Modularity 0.848 0.714 0.7590.8730.434 0.784 0.546
Edge Entropy↑0.9680.540 0.000 0.968 0.000 0.507 0.624
Track C
Compression↑0.3×0.5×0.2×1.2× 1.0×0.5×4.6×
PR Gini 0.323 0.352 0.310 0.317 0.189 0.2420.274
Proactivity↑0.000 0.000 0.000 0.000 0.000 0.0000.614
†Mem0 has no native graph; we materialise each extracted memory as a node and induce edges via vector-similarity neighbours, which trivially
saturates Chain Disc. but produces no typed-edge structure (Edge Entropy= 0).
Proactive baselines.On CogEval-Bench, seven systems are compared under identical LLM and
events:OpenIE KG(HippoRAG-style triples),Cognee[ 56] (Extract–Cognify–Load pipeline),Hip-
poRAG 2[20] (deep passage + synonym expansion),GraphRAG[ 11] (batch community detection +
LLM summarisation),Mem0[ 6] (text-rewrite memory cells),Zep[ 48] (temporal knowledge graph),
and COGNIFOLD.
4.3 Implementation Details
We usegpt-4o-mini as the agent and reader on every benchmark, withtext-embedding-3-small
as the embedding model throughout, so cross-system performance differences are attributable to
architectural design rather than reader capability. All benchmarks run with stream ingestion: each
event is processed sequentially through the full write path (context assembly →UpdatePlan→
atomic execution → consolidation), so the topology-evolution operations of §3.2 fire per event and
consolidation operates throughout ingestion—the same online operation COGNIFOLDperforms in
deployment, not a one-shot batch pass at the end. Hyper-parameters, full prompts, and the cost /
reproducibility statement are in Appendix B and Appendix G.
4.4 Graph Evolution
Table 3 reports per-benchmark statistics of the substrate COGNIFOLDproduces under the protocol
above—events ingested, concepts crystallised, edges accreted, and the compression ratio achieved
by the consolidation operations of §3.2. The numbers serve a diagnostic role: they make explicit
the structural footprint each downstream score in §4.5 is sitting on, so the reader can read accuracy
alongside the graph that produced it.
4.5 Results
Proactive Results.
Table 2 reports CogEval-Bench averages across all six scenarios; per-scenario breakdowns and full
evaluation details are in Appendix F. COGNIFOLDachieves Harmony 0.476, substantially above
GraphRAG (0.323, the strongest baseline) and far above entity-level systems (OpenIE KG 0.138;
Cognee 0.094; HippoRAG 2 0.095). COGNIFOLDis the only system producing non-zero Purity
(0.361)—its concepts are coherently grounded in their constituent events, while all baselines lack
event-level grounding. On topology, COGNIFOLD’s clustering coefficient (0.327) reflects genuine
triadic closure among semantically related concepts, distinct from HippoRAG 2’s high raw clustering
8

## Page 9

Table 3:Graph evolution statistics per benchmark.Compression = concepts/events (lower = more
folding). Edge density = edges/(concepts+intents), measuring connectivity of higher-level nodes.
Statistics are averaged over all ingested samples per benchmark. Per-benchmark accuracy results are
in Table 4 (LoCoMo) and Figure 4 (the other six).
Benchmark Events Concepts Intents Edges Compression Density
MuTual 42 18 2 35 0.43 1.75
ToMi 128 54 5 112 0.42 1.88
BABILong 480 195 8 310 0.41 1.53
StreamingQA 620 340 12 485 0.55 1.38
MuSiQue 380 260 6 320 0.68 1.20
LoCoMo 850 520 18 680 0.61 1.22
NarrativeQA [24] 1,200 480 22 1,650 0.40 3.29
Table 4:LoCoMo per-category and aggregate comparison.J-Score is the LLM-as-judge accu-
racy [67] with gpt-4o-mini as the judge; Tokens is per-question input+output token consumption.
Bold: best per column; underline: second-best.
Model Tokens Single-Hop Multi-Hop Temporal Open DomainOverallOverall F1
MIRIX (2025) – 68.22 54.26 68.54 46.88 64.33 28.10
Mem0 (2025) 1.2k 67.13 51.15 55.5172.9366.88 43.46
Zep (2025) 2.7k 79.79 74.11 67.71 66.04 75.14 41.23
Memobase (2026) 2.1k 73.12 64.65 81.20 53.12 72.0150.18
Supermemory (2026) 0.5k 67.30 51.12 31.77 42.67 55.34 34.87
MemU (2025) 0.6k 66.34 63.12 27.10 50.00 56.55 35.15
MemOS (2025) 2.6k 81.09 67.49 75.18 55.90 75.80 45.27
ENGRAM (2025) 0.9k 79.90 79.79 70.79 72.92 77.55 21.08
EverMemOS† (2026) 2.5k91.08 86.17 81.9366.6786.76–
COGNIFOLD4.2k 90.49 67.38 78.50 50.00 81.23 35.71
†Reported under a 3-LLM-judge ensemble protocol; numbers as reported in Hu et al. [22] Table 1.
(0.716) that arises from synonym-expansion cliques among name variants. On compression and
proactivity, COGNIFOLDachieves 4.6× compression (41–47 events → 7–12 concepts) while OpenIE
KG and HippoRAG 2 expand the representation; and COGNIFOLDis the only system emitting intent
nodes at all, reaching Proactivity 0.614 (61% of intents grounded by≥2supporting connections).
The seven-system comparison reveals an ordered hierarchy in representational richness:entity
graphs(OpenIE KG)—fragmented triples, high modularity from disconnection;entity graphs with
enrichment(Cognee, HippoRAG 2)—shallow structure atop entity extraction, Harmony stuck at
∼0.09;community graphs(GraphRAG)—batch community detection yields the strongest baseline
(Harmony 0.323) but with zero event-level grounding (Purity = 0) and negligible clustering (0.002);
cognitive graphs(COGNIFOLD)—online folding with merging yields event-grounded concepts,
genuine triadic closure, substantial compression, and proactive goal identification simultaneously.
The critical architectural distinction isonline, incremental processing with merging: Cognee and
HippoRAG 2 add machinery (ECL, synonym expansion, PPR) without cross-event integration and
remain at the entity-enrichment tier, confirming that the bottleneck in concept emergence is not
extraction depth but the ability to recognise that events e1, e3, e7 ground the same underlying concept
and merge them into a single abstraction. This hierarchy parallels a neuroscience progression [17,
35, 47]: episodic storage, pattern separation without consolidation, shallow categorisation, schema
extraction, and active consolidation with goal generation.
Memory-Quality Results.CogEval-Bench tells us that the substrate forms cognitive structure; the
seven downstream benchmarks of our suite (Table 5) ask whether that structure pays off as memory.
The same COGNIFOLDgraph—built once per task by the same write path, queried by the same
read path, evaluated under the same gpt-4o-mini reader—is set against eight memory systems on
the conversational-memory benchmark (Table 4, full 10-conversation Mem0 protocol with matched
judge), against the standard graph-retrieval suite of Gutiérrez et al. [20] on the multi-hop reasoning
9

## Page 10

Table 5:Downstream benchmark suite.Seven benchmarks across five cognitive domains. Per-
benchmark detailed system comparisons are reported in Table 4 (LoCoMo) and Figure 4 (the other
six).
Benchmark Domain Metricn
LoCoMo [32] Conversational memory J-Score / F1 1540
MuSiQue [57] Multi-hop reasoning EM / F1 2417
NarrativeQA [24] Narrative comprehension F1 500
StreamingQA [31] Streaming temporal QA F1 500
MuTual [8] Dialogue coherence Accuracy 500
ToMi [29] Theory of mind Exact match 500
BABILong [27] Long-context factual extr. Exact match 100
0 20 40 60
F1 Score
GraphRAG
HippoRAG
PolicyRAG
CogniFold
42.0
49.3
55.9
58.7
MuSiQue
0 20 40 60 80
F1 Score
RAPTOR
GraphRAG
HippoRAG 2
CogniFold
21.4
23.0
25.9
72.0
NarrativeQA
0 20 40 60 80 100
Accuracy (%)
RoBERTa-MC
Self-Expl.
Direct LLM
CogniFold
69.3
71.6
88.5
93.2
MuTual
0 20 40 60 80 100
F1 Score
FiD+Retr
FiD+FT
FiD (Oracle)
CogniFold
45.6
58.2
72.7
88.6
StreamingQA
0 20 40 60 80 100
Exact Match
Direct LLM
GPT-4o+MixPR
ARMT (FT)
CogniFold
65.6
66.0
94.8
96.0
BABILong
0 20 40 60 80 100
Exact Match
Direct LLM
SymbolicToM
AutoToM
CogniFold
58.0
79.9
88.3
91.6
ToMi
Figure 4:Downstream benchmarks at a glance.CogniFold (indigo, bold) against the most-cited
published baselines for each benchmark, sorted by score with the best on top. Metric varies per
benchmark; sample sizes are 500 for MuSiQue, NarrativeQA, MuTual, StreamingQA, ToMi, and 100
for BABILong.
benchmark, and against the most-cited published baselines on each of the remaining five; Figure 4
summarises the six per-benchmark comparisons at a glance. On LoCoMo the substrate leads the audit-
resilient region of the leaderboard [46], scoring above MemOS, ENGRAM, and the text-rewriting
tier; on MuSiQue it reaches F1 58.7, exceeding the strongest published RAG pipeline (HippoRAG 2,
+9.4) and the strongest symbolic-graph alternative (PolicyRAG, +2.8); on the remaining five it leads
on theory of mind (ToMi, +3.3 over AutoToM) and long-context factual extraction (BABILong,
+1.2 over fine-tuned ARMT), holds within range of streaming-FiD on StreamingQA, and tops the
published memory and structure-augmented baselines on MuTual and NarrativeQA.
MuSiQue (multi-hop reasoning).On MuSiQue COGNIFOLDis benchmarked against the stan-
dard graph-augmented retrieval suite of Gutiérrez et al. [20]—RAPTOR, GraphRAG, HippoRAG—
together with PolicyRAG [ 49], all under a unified gpt-4o-mini reader, and reaches F1 58.7 /
EM 48.0, the highest of the suite under this reader. The lift over HippoRAG (+9.4 F1) and PolicyRAG
(+2.8 F1) reflects the formation-over-retrieval principle: a dynamically folded graph carries more
answer-relevant structure than a static graph paired with a sophisticated retrieval pipeline.
Per-benchmark summary on the remaining five. MuTual(dialogue coherence) gains arise from
concept-level folding of recurring conversational themes that paragraph-level chunking destroys;
ToMi(theory of mind) gains come from the symbolic belief tracker (§ ??) bypassing LLM over-
abstraction of spatial state;NarrativeQA(long-form fiction) benefits from cross-character entity
disambiguation enabled by concept folding;StreamingQA(time-anchored facts) benefits from
explicit time nodes that allow temporal queries to resolve by traversal rather than vector ranking;
BABILong(long-context bAbI-style) is the one regime where structural memory is approximately
neutral—local key–value supports are retrievable directly without need of cross-event integration.
10

## Page 11

What the same substrate doing well across these very different cognitive domains shows is not a tuning
result but a generality result. Conversational memory, multi-hop reasoning, theory of mind, narrative
comprehension, and streaming temporal QA pull on different cognitive operations—inter-session
consolidation, cross-document chaining, belief tracking, character disambiguation, time-anchored
recall—yet they share the same underlying ask: that the memory substrate retain the right relational
structure between events and surface it on demand. COGNIFOLD’s consistent placement in the
upper band across this spread is direct evidence thatcognitive folding—the operations of §3.2—is
a task-general write-path competence rather than a benchmark-tuned heuristic. The one regime
where the gain disappears is exactly the one the theory predicts: BABILong asks for verbatim local
key–value supports, where structural folding adds no leverage that direct retrieval did not already
have.
5 Discussion
In a strict sense, COGNIFOLDis beyond memory: it does not merely store and retrieve, it bootstraps.
Each fold collapses events into higher-level concepts that later folds reason against; the agent is
not starting cold at every event but using its own accumulated cognition as substrate. The 4.6 ×
compression and 0.614 Proactivity (§4.5) are the architectural correlates of this process, reflecting
both the aggressive folding of events and how bootstrapped concepts further crystallize into goals.
However, this bootstrapping dynamic introduces a principled limitation:path-dependence. Because
each fold conditions on previously accumulated structure, the same events in different orders produce
different graphs. While this mirrors humancurriculum effects—where pedagogical ordering yields
cleaner schemas than shuffled inputs [14, 66]—it raises an open question regarding memory stability.
Order-aware consolidation, replay-based smoothing, and bounded-divergence analyses on streaming
graphs are concrete avenues for future work.
A second limitation concerns the depth of our prefrontal mapping. COGNIFOLDoperationalizes only
schema-driven integration, whereas the biological prefrontal cortex performs reward-based valuation,
cognitive control, and counterfactual simulation [17, 47]. Without value estimation, it cannot rank
intents by long-horizon utility; without cognitive control, it cannot suppress impulsive emissions when
a stronger goal is active; without counterfactual rollout, it cannot anticipate downstream consequences.
Integrating these mechanisms forms the natural research arc beyond this paper.
6 Conclusion
We present COGNIFOLD, an always-on proactive agent memory that folds fragmented events into
persistent cognitive structure. Unlike reactive retrieval systems, COGNIFOLDbuilds a living graph that
continuously folds, merges, decays, and reconnects under the event stream. Because cognition grows
recursively from the system’s own products, goal-directed intents naturally emerge from converging
evidence. We validated this design across two critical axes: proactive structural emergence on
CogEval-Bench, and robust memory quality across seven broad-coverage downstream benchmarks.
As foundation-model capability grows, what a system computes in a single forward pass approaches
what a human can reason about in a moment; what it accumulates, organizes, and bootstraps across
time is where the value of an always-on agent will increasingly accrue. We release COGNIFOLDas a
foundation for research on real-time interaction, proactive collaboration, and agent cognition that
bootstraps beyond memory.
11

## Page 12

References
[1] Frederic Charles Bartlett.Remembering: A study in experimental and social psychology.
Cambridge university press, 1995.
[2] Ali Behrouz, Peilin Zhong, and Vahab Mirrokni. Titans: Learning to memorize at test time.
arXiv preprint arXiv:2501.00663, 2024.
[3] Bruno Bontempi, Catherine Laurent-Demir, Claude Destrade, and Robert Jaffard. Time-
dependent reorganization of brain circuitry underlying long-term memory storage.Nature, 400
(6745):671–675, 1999.
[4] Michael Bratman.Intention, plans, and practical reason. Harvard University Press, 1987.
[5] Susan Carey. The origin of concepts.Journal of Cognition and Development, 1(1):37–41, 2000.
[6] Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, and Deshraj Yadav. Mem0:
Building production-ready ai agents with scalable long-term memory.arXiv preprint
arXiv:2504.19413, 2025.
[7] Andy Clark. Whatever next? predictive brains, situated agents, and the future of cognitive
science.Behavioral and brain sciences, 36(3):181–204, 2013.
[8] Leyang Cui, Yu Wu, Shujie Liu, Yue Zhang, and Ming Zhou. Mutual: A dataset for multi-
turn dialogue reasoning. InProceedings of the 58th Annual Meeting of the Association for
Computational Linguistics, pages 1406–1416, 2020.
[9] André F de Sousa, Zachary E Zeidler, Daniel G Almeida-Filho, Yang Shen, Alessandro Luchetti,
Shana Simanian, Mouaz Mardini, Laura A DeNardo, and Alcino J Silva. The prefrontal cortex
controls memory organization in the hippocampus.Nature Neuroscience, pages 1–12, 2026.
[10] Hermann Ebbinghaus. [image] memory: A contribution to experimental psychology.Annals of
neurosciences, 20(4):155, 2013.
[11] Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven
Truitt, Dasha Metropolitansky, Robert Osazuwa Ness, and Jonathan Larson. From local to global:
A graph rag approach to query-focused summarization.arXiv preprint arXiv:2404.16130, 2024.
[12] Howard Eichenbaum. Memory: organization and control.Annual review of psychology, 68:
19–45, 2017.
[13] Gilles O Einstein and Mark A McDaniel. Prospective memory: Multiple retrieval processes.
Current Directions in Psychological Science, 14(6):286–290, 2005.
[14] Jeffrey L Elman. Learning and development in neural networks: The importance of starting
small.Cognition, 48(1):71–99, 1993.
[15] Paul W Frankland and Bruno Bontempi. The organization of recent and remote memories.
Nature reviews neuroscience, 6(2):119–130, 2005.
[16] Karl Friston. The free-energy principle: a unified brain theory?Nature reviews neuroscience,
11(2):127–138, 2010.
[17] Asaf Gilboa and Hannah Marlatte. Neurobiology of schemas and schema-mediated memory.
Trends in cognitive sciences, 21(8):618–631, 2017.
[18] Zirui Guo, Lianghao Xia, Yanhua Yu, Tian Ao, and Chao Huang. Lightrag: Simple and fast
retrieval-augmented generation.arXiv preprint arXiv:2410.05779, 2(3), 2024.
[19] Bernal J Gutiérrez, Yiheng Shu, Yu Gu, Michihiro Yasunaga, and Yu Su. Hipporag: Neurobio-
logically inspired long-term memory for large language models.Advances in neural information
processing systems, 37:59532–59569, 2024.
[20] Bernal Jiménez Gutiérrez, Yiheng Shu, Weijian Qi, Sizhe Zhou, and Yu Su. From rag to memory:
Non-parametric continual learning for large language models.arXiv preprint arXiv:2502.14802,
2025.
[21] Donald Olding Hebb.The organization of behavior: A neuropsychological theory. Psychology
press, 2005.
[22] Chuanrui Hu, Xingze Gao, Zuyi Zhou, Dannong Xu, Yi Bai, Xintong Li, Hui Zhang, Tong
Li, Chong Zhang, Lidong Bing, and Yafeng Deng. Evermemos: A self-organizing memory
operating system for structured long-horizon reasoning.arXiv preprint arXiv:2601.02163, 2026.
12

## Page 13

[23] Dongming Jiang, Yi Li, Guanpeng Li, and Bingzhe Li. Magma: A multi-graph based agentic
memory architecture for ai agents.arXiv preprint arXiv:2601.03236, 2026.
[24] Tomáš Koˇcisk`y, Jonathan Schwarz, Phil Blunsom, Chris Dyer, Karl Moritz Hermann, Gábor
Melis, and Edward Grefenstette. The narrativeqa reading comprehension challenge.Transac-
tions of the Association for Computational Linguistics, 6:317–328, 2018.
[25] Harold W Kuhn. The hungarian method for the assignment problem.Naval research logistics
quarterly, 2(1-2):83–97, 1955.
[26] Dharshan Kumaran, Demis Hassabis, and James L McClelland. What learning systems do
intelligent agents need? complementary learning systems theory updated.Trends in cognitive
sciences, 20(7):512–534, 2016.
[27] Yuri Kuratov, Aydar Bulatov, Petr Anokhin, Ivan Rodkin, Dmitry Sorokin, Artyom Sorokin, and
Mikhail Burtsev. Babilong: Testing the limits of llms with long context reasoning-in-a-haystack.
Advances in Neural Information Processing Systems, 37:106519–106554, 2024.
[28] Christopher A Kurby and Jeffrey M Zacks. Segmentation in the perception and memory of
events.Trends in cognitive sciences, 12(2):72–79, 2008.
[29] Matthew Le, Y-Lan Boureau, and Maximilian Nickel. Revisiting the evaluation of theory
of mind through question answering. InProceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the 9th International Joint Conference on Natural
Language Processing (EMNLP-IJCNLP), pages 5872–5877, Hong Kong, China, November
2019. Association for Computational Linguistics. doi: 10.18653/v1/D19-1598. URL https:
//www.aclweb.org/anthology/D19-1598.
[30] Zhiyu Li, Chenyang Xi, Chunyu Li, Ding Chen, Boyu Chen, Shichao Song, Simin Niu, Hanyu
Wang, Jiawei Yang, Chen Tang, et al. Memos: A memory os for ai system.arXiv preprint
arXiv:2507.03724, 2025.
[31] Adam Liska, Tomas Kocisky, Elena Gribovskaya, Tayfun Terzi, Eren Sezener, Devang Agrawal,
Cyprien De Masson D’Autume, Tim Scholtes, Manzil Zaheer, Susannah Young, et al. Stream-
ingqa: A benchmark for adaptation to new knowledge over time in question answering models.
InInternational Conference on Machine Learning, pages 13604–13622. PMLR, 2022.
[32] Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov, Mohit Bansal, Francesco Barbieri, and
Yuwei Fang. Evaluating very long-term conversational memory of llm agents. InProceedings
of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), pages 13851–13870, 2024.
[33] Bodhisattwa Prasad Majumder, Bhavana Dalvi Mishra, Peter Jansen, Oyvind Tafjord, Niket
Tandon, Li Zhang, Chris Callison-Burch, and Peter Clark. Clin: A continually learning language
agent for rapid task adaptation and generalization.arXiv preprint arXiv:2310.10134, 2023.
[34] David Marr. Simple memory: a theory for archicortex.Philosophical Transactions of the Royal
Society of London. B, Biological Sciences, 262(841):23–81, 1971.
[35] James L McClelland, Bruce L McNaughton, and Randall C O’Reilly. Why there are comple-
mentary learning systems in the hippocampus and neocortex: insights from the successes and
failures of connectionist models of learning and memory.Psychological review, 102(3):419,
1995.
[36] Michael McCloskey and Neal J Cohen. Catastrophic interference in connectionist networks:
The sequential learning problem. InPsychology of learning and motivation, volume 24, pages
109–165. Elsevier, 1989.
[37] MemoDB Team. Memobase: User profile-based long-term memory for AI chatbot applications.
https://github.com/memodb-io/memobase, 2026. Version 0.0.18.
[38] George A Miller. The magical number seven, plus or minus two: Some limits on our capacity
for processing information.Psychological review, 63(2):81, 1956.
[39] NevaMind AI. MemU: A memory operating system for agents. https://github.com/Nev
aMind-AI/memU, 2025.
[40] Mark EJ Newman. Modularity and community structure in networks.Proceedings of the
national academy of sciences, 103(23):8577–8582, 2006.
13

## Page 14

[41] Randall C O’Reilly and James L McClelland. Hippocampal conjunctive encoding, storage, and
recall: Avoiding a trade-off.Hippocampus, 4(6):661–682, 1994.
[42] Charles Packer, Vivian Fang, Shishir_G Patil, Kevin Lin, Sarah Wooders, and Joseph_E Gonza-
lez. Memgpt: towards llms as operating systems.arXiv preprint arXiv:2310.08560, 2023.
[43] Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and
Michael S Bernstein. Generative agents: Interactive simulacra of human behavior. InProceed-
ings of the 36th annual acm symposium on user interface software and technology, pages 1–22,
2023.
[44] Daivik Patel and Shrenik Patel. Engram: Effective, lightweight memory orchestration for
conversational agents.arXiv preprint arXiv:2511.12960, 2025.
[45] Karalyn Patterson, Peter J Nestor, and Timothy T Rogers. Where do you know what you know?
the representation of semantic knowledge in the human brain.Nature reviews neuroscience, 8
(12):976–987, 2007.
[46] Penfield Labs. Auditing LoCoMo: 6.4% answer-key error rate, judge leniency, and reproducibil-
ity failures in long-term conversational memory benchmarks. https://github.com/dial4
81/locomo-audit, 2026.
[47] Alison R Preston and Howard Eichenbaum. Interplay of hippocampus and prefrontal cortex in
memory.Current biology, 23(17):R764–R773, 2013.
[48] Preston Rasmussen, Pavlo Paliychuk, Travis Beauvais, Jack Ryan, and Daniel Chalef. Zep: a
temporal knowledge graph architecture for agent memory.arXiv preprint arXiv:2501.13956,
2025.
[49] Tejas Sarnaik, Manan Shah, and Ravi Hegde. Policyrag: Prompt-guided symbolic graph memory
for interpretable multi-hop retrieval. https://openreview.net/forum?id=0xlI09pvBs ,
2025.
[50] Parth Sarthi, Salman Abdullah, Aditi Tuli, Shubh Khanna, Anna Goldie, and Christopher D
Manning. Raptor: Recursive abstractive processing for tree-organized retrieval. InThe Twelfth
International Conference on Learning Representations, 2024.
[51] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao.
Reflexion: Language agents with verbal reinforcement learning.Advances in neural information
processing systems, 36:8634–8652, 2023.
[52] Larry R Squire. Memory and the hippocampus: a synthesis from findings with rats, monkeys,
and humans.Psychological review, 99(2):195, 1992.
[53] Robert Stickgold and Matthew P Walker. Sleep-dependent memory consolidation and reconsoli-
dation.Sleep medicine, 8(4):331–343, 2007.
[54] Theodore Sumers, Shunyu Yao, Karthik R Narasimhan, and Thomas L Griffiths. Cognitive
architectures for language agents.Transactions on Machine Learning Research, 2023.
[55] Supermemory Team. Supermemory: State-of-the-art memory and context engine for ai. https:
//github.com/supermemoryai/supermemory, 2026.
[56] Topoteretes. cognee: Memory control plane for ai agents. https://github.com/topoter
etes/cognee, 2026.
[57] Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, and Ashish Sabharwal. ♭♭ musique:
Multihop questions via single-hop question composition.Transactions of the Association for
Computational Linguistics, 10:539–554, 2022.
[58] Dorothy Tse, Rosamund F Langston, Masaki Kakeyama, Ingrid Bethus, Patrick A Spooner,
Emma R Wood, Menno P Witter, and Richard GM Morris. Schemas and memory consolidation.
Science, 316(5821):76–82, 2007.
[59] Endel Tulving et al. Episodic and semantic memory.Organization of memory, 1(381-403):1,
1972.
[60] Marlieke TR Van Kesteren, Dirk J Ruiter, Guillén Fernández, and Richard N Henson. How
schema and novelty augment memory formation.Trends in neurosciences, 35(4):211–219,
2012.
14

## Page 15

[61] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan,
and Anima Anandkumar. V oyager: An open-ended embodied agent with large language models.
arXiv preprint arXiv:2305.16291, 2023.
[62] Yu Wang and Xi Chen. Mirix: Multi-agent memory system for llm-based agents.arXiv preprint
arXiv:2507.07957, 2025.
[63] Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, and Yongfeng Zhang. A-mem:
Agentic memory for llm agents.arXiv preprint arXiv:2502.12110, 2025.
[64] John Yang, Carlos E Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik
Narasimhan, and Ofir Press. Swe-agent: Agent-computer interfaces enable automated software
engineering.Advances in Neural Information Processing Systems, 37:50528–50652, 2024.
[65] Jeffrey M Zacks. Event perception and memory.Annual review of psychology, 71(1):165–191,
2020.
[66] Bonan Zhao, Christopher G Lucas, and Neil R Bramley. A model of conceptual bootstrapping
in human cognition.Nature Human Behaviour, 8(1):125–136, 2024.
[67] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang,
Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and
chatbot arena.Advances in neural information processing systems, 36:46595–46623, 2023.
[68] Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, and Yanlin Wang. Memorybank: Enhancing
large language models with long-term memory. InProceedings of the AAAI conference on
artificial intelligence, volume 38, pages 19724–19731, 2024.
15

## Page 16

Table 6:Design-space for agent memory under continuous streams.Four orthogonal axes
distinguish always-on proactive memory from reactive, batch-oriented architectures; COGNIFOLDis
the only system satisfying all four simultaneously. Table 12 provides the complementary engineering-
coverage view (which of the four structural debts of §3.2 each system addresses). ✓= satisfies;
— = does not;partial= subset of the axis.
System Stream input Proactive update Evolving topology Symbolic
HippoRAG [19, 20] — — —✓
Mem0 [6] partial partial —✓
MAGMA [23] — — partial✓
Zep [48]✓ ✓partial✓
A-Mem [63]✓ ✓—✓
Titans [2]✓ ✓n/a —
COGNIFOLD✓ ✓ ✓ ✓
A Related Work
A.1 Graph-based Agent Memory
Current graph-augmented memory systems generally evolve along three axes, all of which treat the
graph as a query-time artifact rather than a living substrate. HippoRAG [19, 20] maps memory to
a static knowledge graph retrieved via Personalized PageRank. However, this structurally frozen
approach struggles to handle the evolving lifecycle of agent interactions. For dynamic updates,
Mem0 [6] performs per-turn memory management through LLM-driven text rewrites. MAGMA [23]
decomposes memory into multiple orthogonal graphs and supplements them with an LLM-driven
slow-path inference pass. Zep [48] introduces bi-temporal validity to track fact invalidation. Across
these paradigms, although several systems do process events incrementally, the graph’stopology
grows by accumulation, rewriting, or invalidation, but does notmetabolisebetween events—it does
not fold redundant fragments, decay stale connections by mere passage of time, or reconnect orphans
through associative similarity. Real-time topological metabolism under an event stream therefore
remains largely unaddressed. Table 6 situates representative systems—together with the non-graph
alternatives discussed below—on four orthogonal axes (stream input, proactive update, evolving
topology, symbolic and inspectable), making the absent corner explicit.
A.2 Non-Topological Test-Time Learning
A parallel line of work pursues persistent test-time learning through non-graph mechanisms, revealing
a trade-off between inspectability and structural depth. Generative Agents [43] and MemGPT [42]
treat memory as natural language to be paged or searched, while systems like A-Mem [63] rewrite
Zettelkasten-style notes upon receiving new information. These text-rewriting methods remain highly
inspectable but are structurally blind, as the underlying architecture does not evolve. Conversely,
Titans [2] introduces a neural long-term memory module updated via surprise-driven gradient descent
during inference. While computationally efficient, this implicit approach deposits knowledge into
an opaque weight space that cannot be audited or selectively deleted [36]. Consequently, the field
remains divided between methods that are transparent but topologically static, and those that learn
continuously but sacrifice discrete, mutable geometry.
A.3 Proactive Agent Memory
Most agent-memory systems are fundamentally designed for the reactive setting: the user issues a
query, and the system retrieves context to generate a response. Explicit treatment of the always-on
setting—where input is a continuously arriving event stream—remains sparse. Traditional BDI-
style architectures [ 4] address agency by deriving intentions from hardcoded rules and explicit
goals, rather than letting them emerge bottom-up from accumulated evidence. Recent prospective-
memory work [13] and cognitive-agent frameworks [51, 54] acknowledge the need for goal-directed
organization but rarely anchor intent emergence to the evolving topology of the memory itself. Even
with advanced read-path innovations, mainstream systems assume a stable graph at query time without
16

## Page 17

defining how the structure should reorganize between queries, leaving a critical gap in anticipatory,
autonomous memory assembly.
B Hyperparameters
All numeric defaults referenced in §3.1 are listed here for reproducibility. Values were tuned
empirically on a held-out subset of the personal-timeline simulator and held fixed across all reported
experiments.
B.1 Default Edge Weights (Table 1)
Edge Type Default Weight
GROUNDS, CAUSES0.9
TRIGGERS, USER_FEEDBACK0.8
REINFORCES, PART_OF0.7
DERIVED_FROM, DEADLINE_FOR0.6
RELATED_TO0.5
Table 7: Prior weights at edge creation. Per-instance weights are then updated dynamically through
REINFORCESstrengthening and exponential edge decay (§3.2).
B.2 Write-Path Scoring (Eq. 1)
Parameter Default Description
α(PageRank) 0.4 Structural importance
β(Recency) 0.4 Temporal relevance
γ(Access) 0.2 Usage frequency
λ(Node decay) 0.01 / hr Half-life≈69 hours
U(Urgency boost)[1.0,2.0]Linear ramp 24 hr before deadline
k(Context window) 50 Top-knodes selected for context
Tier proportions 10 / 30 / 50% Immediate / Working / Background
Title-similarity dedup 0.85 Near-duplicate concept-merge threshold
Table 8: Write-path scoring weights and context-window allocation. Tier sub-weights:Immediate—
70% recency + 30% urgency;Working—50% PageRank + 30% recency + 20% type;Background—
80% PageRank + 20% diversity.
B.3 Consolidation Operations (§3.2)
Parameter Default Description
Merge cosine threshold 0.85 Minimum semantic similarity for two concepts to be merged
λe (Edge decay) 0.005 / hr Half-life≈139 hours
kNNk(completion) 5 Neighbours considered when inferring missingGROUNDSedges
kNN cosine threshold 0.3 Minimum similarity for an inferred kNN edge
Table 9: Consolidation operations that discharge the four structural debts. Default weights for each
typed edge are listed in Table 1.
B.4 Intent Emergence (Eq. 2)
C Four-Debt Attack Surface
Table 12 compares how each prior agent-memory system addresses (or fails to address) the four
structural debts of §3.2—accumulation, compression, decay, and completion. COGNIFOLDis the
first system to address all four as automatic, topology-level operations.
17

## Page 18

Parameter Default Description
αema 0.3 EMA blend weight for per-category threshold updates
st (accept) 1.5 Score onacceptfeedback
st (modify) 1.1 Score onmodifyfeedback
st (defer) 0.8 Score ondeferfeedback
st (reject) 0.3 Score onrejectfeedback
Table 10: Per-category EMA loop for adaptive intent-emission threshold.
Parameter Default Description
RRFk60 Reciprocal Rank Fusion smoothing constant
BFS hop decay 0.85 Per-hop weight decay during graph traversal
BFS / PPR blend 60 / 40% Mix of BFS traversal and Personalized PageRank
Table 11: Read-path retrieval and traversal parameters.
D Implementation
Python 3.11: NetworkX (graph), Pydantic v2 (schemas), LangGraph (agent), FastAPI (HTTP), FAISS
(ANN index). 21 packages, 1,167 tests, strict typing. Deployed on GCP Cloud Run with per-session
isolation. Multi-domain support (learning, finance, programming) via prompt profiles.
E Core System Prompt (Excerpt)
The LLM agent receives a system prompt composed from modular sections. The key section
governing concept extraction:
You are a cognitive graph agent. Given an event
and context, produce an UpdatePlan with operations:
NODE TYPES: event (raw input), concept (patterns),
intent (goals), time (deadlines)
EDGE TYPES with weights:
GROUNDS (0.9): event -> concept/intent
REINFORCES (0.7): event -> existing concept
TRIGGERS (0.8): concept -> intent
PART_OF (0.7): concept -> concept (hierarchy)
RULES:
1. Create concepts for recurring patterns (3+ events)
2. Link every concept to grounding events
3. Merge near-duplicate concepts via MERGE_NODES
4. Create intents only when patterns suggest
unmet goals with supporting evidence
5. Self-review: check for missing edges between
concepts that share grounding events
The full prompt includes 20 composable sections (edge types, connectivity rules, validation checklist,
deduplication, self-review). Domain-specific Y AML profiles override the role section while retaining
structural sections.
F CogEval-Bench Details
F.1 Gold Graph Schemas
For each scenario we manually define a gold concept graph G∗ = (C∗,R∗,H∗,I ∗) with four com-
ponents.Concepts C∗: 8–9 non-hierarchical concepts, each specified with label, natural-language
description, representative keywords, and expected event count. Concepts are grounded in estab-
lished domain knowledge (e.g., SoftEng includes Code Review, Sprint Planning, Deployment) and
deliberately avoid COGNIFOLD-specific abstractions to keep the gold standard system-agnostic.
Relationships R∗: 9–14 labelled inter-concept edges using four relationship types drawn from
18

## Page 19

Table 12:Four-debt attack-surface comparison.An event-stream memory graph accumulates
four structural debts by the nature of its input (Section 3.2):accumulation,compression,decay,
completion. “—” = not addressed; “LLM rewrite” = text-layer rewrite only; “partial” = subset of
the debt; ✓= automatic graph-level operation.Scope of comparison: all systems with a published
description of their ingestion and update mechanisms in the 2024–2026 graph-memory literature;
closed industrial systems without published mechanisms are excluded. COGNIFOLDis the only
system to address all four debts as automatic graph-level operations.
System Accumulate Compress Decay Complete
HippoRAG [19, 20] — — — partial (synonyms)
Cognee [56] — — — —
Mem0 [6] LLM rewrite partial (write-time) — —
MAGMA [23] — — —✓(slow-path)
Zep / Graphiti [48] — partial (summary) — † —
A-Mem [63] LLM rewrite LLM rewrite — partial (kNN+LLM)
PREMem — LLM rewrite + dedup — — (no graph)
COGNIFOLD✓(REINFORCES)✓(MERGE_NODES)✓(edge decay)✓(kNN inference)
† Zep/Graphiti provides bi-temporal fact invalidation (t_invalid) oncontradiction, which addressesconsistencyrather than
decay: no edge weakens with passage of time alone. Consistency is orthogonal to the four debts in our taxonomy.
cognitive schema theory [1, 17]: PART_OF (compositional hierarchy), TRIGGERS (temporal causa-
tion), REINFORCES (feedback strengthening), CAUSES (interventional causation).Hierarchy parents
H∗: 1–3 superordinate concepts (e.g., Work Projects subsumes Coding Sessions and Code Review)
that test hierarchical abstraction.Expected intents I∗: 2 goal nodes per scenario, each grounded
in 2–3 supporting concepts with a specified trigger pattern (e.g., “3+ exercise events within the
week” → Maintain Regular Exercise). Each gold graph additionally contains 2planted multi-
hop reasoning chains(3–4 hops) following the compositional methodology of MuSiQue [ 57]:
chains are sequences of events connected through causal or temporal links across different concepts
(e.g., deployment → staging bug → client demo failure), requiring cross-concept traversal to recon-
struct. Complete gold concept graphs for all 6 scenarios are provided in the supplementary material
(benchmarks/cogeval/data/gold_graphs/).
F.2 Event Generation Pipeline
From each gold graph, a grounded event stream is generated in four stages. (1)Concept-grounded
events: for each concept c∈ C∗, GPT-4o-mini generates nc realistic first-person events conditioned
on the concept’s label, description, and keywords; each event receives the by-construction label
gold_concept=c . (2)Chain events: for each planted chain, the pipeline generates sequential events
following the chain’s step descriptions, ensuring entity consistency across hops (e.g., the same “auth
service v2.3” appears in the deployment, bug discovery, and client demo events). (3)Distractor
injection: 10–15% of events come from unrelated topics (weather, unrelated news, etc.), labelled
gold_concept=null . (4)Temporal shuffling: all events receive timestamps spanning the scenario’s
temporal window (5–60 days), then are sorted chronologically with chain events interleaved among
non-chain events to prevent trivial sequential pattern matching.
F.3 Scenarios
Six scenarios span four domains (Table 13): professional work (SoftEng), medical recovery (Health),
team coordination (Team), breaking news (News), academic research (Academic), and customer
support (Support). These domains test distinct cognitive patterns: daily routines with gradual concept
consolidation, crisis cascades requiring causal chain tracking, topic drift across independent threads,
deep abstraction hierarchies, and repetitive pattern detection. The benchmark totals 251 events, 49
gold concepts, 12 planted multi-hop chains, and 12 expected intents across the six scenarios.
19

## Page 20

Table 13:CogEval-Bench scenarios.Six domains with controlled gold concept graphs. Each
scenario defines gold concepts, planted multi-hop chains (3–4 hops), expected intents, and distractor
events (∼15%). Events generated by GPT-4o-mini from gold graphs, temporally shuffled.
Scenario Domain Events Gold Concepts Chains Intents
SOFTENGProfessional/tech work 41 8 2 (3-hop) 2
HEALTHMedical recovery 39 8 2 (3–4-hop) 2
TEAMProduct launch 38 8 2 (3–4-hop) 2
NEWSBreaking news stream 42 8 2 (3–4-hop) 2
ACADEMICGraduate research lab 47 9 2 (3–4-hop) 2
SUPPORTCustomer support center 44 8 2 (3–4-hop) 2
Total4 domains 251 49 12 12
F.4 Evaluation Metrics
Three tracks are computed per system and averaged across scenarios.Track A: Concept Emergence—
(i)Gold F1: precision and recall of system concepts against gold concepts via embedding-based
soft matching (text-embedding-3-small, cosine ≥0.75 ) with optimal one-to-one assignment
via the Hungarian algorithm [ 25]; (ii)LLM Quality: GPT-4o-mini judge rates meaningfulness,
groundedness, and abstraction level, each 0–1, then averaged; (iii)Harmony: harmonic mean
of Gold F1 and LLM Quality; (iv)Purity: average pairwise embedding similarity among events
grounding each concept.Track B: Relationship Topology—Chain Discovery Rate (fraction of
planted chains recoverable via BFS between endpoints), Clustering Coefficient [ 40], Modularity
(Newman Q), Edge Type Entropy.Track C: Compression & Proactivity—Compression Ratio
(input events / output concepts), PageRank Gini, Proactivity (fraction of intents with ≥2 grounding
connections).
F.5 Comparison Systems
Seven systems under identical LLM and events.OpenIE KG: HippoRAG-style triples, flat entity
graph, no concept folding.Cognee[ 56]: Extract–Cognify–Load pipeline building property graphs
via LLM entity extraction and classification; no cross-event merging or temporal tracking.Hip-
poRAG 2[20]: deeper passage integration, synonym expansion edges, PPR retrieval; still entity-level
with no concept abstraction.GraphRAG[ 11]: LLM entity/relation extraction, Leiden community
detection, LLM summarization per community; batch, no temporal folding or intent emergence.
Mem0[ 6]: text-rewrite memory cells with vector retrieval; no native graph (we materialise each cell
as a node and induce vector-similarity edges).Zep[ 48]: temporal knowledge-graph memory with
entity-centric edges and time stamps.COGNIFOLD: full merge-fold pipeline (events → concepts →
intents), 9 typed edges, online event-by-event processing, temporal decay, lifecycle management.
F.6 Per-Scenario Results
Table 14 provides per-scenario breakdowns on three key metrics. COGNIFOLD’s Harmony ranges
from 0.383 (Team) to 0.572 (SoftEng), consistently above GraphRAG’s best (0.390, Support).
Compression is robust (3.4–5.5 ×), highest on Support and Team where repetitive event patterns
benefit most from folding. Clustering ranges from 0.132 (Health) to 0.392 (Support), lowest on
Health where longer temporal spans create sparser event overlap.
F.7 Why Enrichment̸=Abstraction
Cognee and HippoRAG 2 occupy the same Harmony tier as vanilla OpenIE KG despite adding
substantial computational machinery (ECL pipeline, synonym expansion, Personalized PageRank).
This confirms that the bottleneck in concept emergence is not extraction depth butcross-event
integration—the ability to recognize that events e1, e3, e7 ground the same underlying concept
and merge them into a single abstraction. Systems that process each event in isolation, however
thoroughly, cannot produce this integration.
20

## Page 21

Table 14:CogEval-Bench per-scenario Harmony scores.Harmony = harmonic mean of gold
F1 and LLM quality (Track A). COGNIFOLDconsistently leads across all 6 scenarios despite their
diversity. Mem0’s flat memory store (no concept abstraction) yields zero across the board; entity-level
systems (OpenIE KG, Cognee, HippoRAG 2, Zep/Graphiti) cluster around 0.07–0.19; community-
level GraphRAG reaches 0.23–0.39; COGNIFOLD’s folding achieves 0.38–0.57.
Scenario OpenIE KG Cognee HippoRAG 2 GraphRAG Mem0 ZepCOGNIFOLD
SOFTENG.107 .095 .076 .312 .000 .103.572
HEALTH.138 .090 .101 .309 .000 .081.529
TEAM.157 .086 .107 .226 .000 .181.383
NEWS.127 .089 .069 .376 .000 .116.433
ACADEMIC.144 .106 .111 .325 .000 .190.423
SUPPORT.158 .100 .105 .390 .000 .158.515
Average.138 .094 .095 .323 .000 .138.476
Compression Ratio↑Clustering Coefficient↑
Scenario KG Cog HR2 GR M0 ZpCFKG Cog HR2 GR M0 ZpCF
SOFTENG0.3 0.4 0.2 1.1 1.0 0.43.4.013 .202 .721 .000 .400 .679.367
HEALTH0.2 0.4 0.2 1.3 1.0 0.54.9.000 .202 .684 .000 .452 .742.132
TEAM0.3 0.5 0.2 1.2 1.0 0.85.4.018 .230 .730 .011 .351 .666.316
NEWS0.2 0.4 0.1 1.1 1.0 0.44.2.000 .176 .736 .000 .372 .773.372
ACADEMIC0.2 0.5 0.2 1.1 1.0 0.44.3.000 .193 .706 .000 .371 .638.380
SUPPORT0.3 0.5 0.2 1.3 1.0 0.65.5.000 .200 .720 .000 .347 .726.392
Average0.3 0.5 0.2 1.2 1.0 0.54.6.005 .200 .716 .002 .382 .704.327
KG = OpenIE KG; Cog = Cognee; HR2 = HippoRAG 2; GR = GraphRAG; M0 = Mem0; Zp = Zep/Graphiti; CF = COGNIFOLD. Compression
= events/concepts (×). Clustering markedboldfor COGNIFOLDdue to semantic meaningfulness; HippoRAG 2’s high clustering arises from
synonym edges, Zep’s from dense entity co-mention edges, and Mem0’s from undifferentiated similarity-induced edges (see text).
F.8 Proactivity as Emergence Evidence
Proactivity captures a property no baseline can produce: identifying goals from converging evidence
before being asked. An average of 22 intent nodes per scenario, with 61.4% well-grounded by
multiple events, constitutes evidence of intent emergence beyond memory organization. While these
intents are LLM-generated rather than autonomously emergent from prediction error, they represent a
measurable step toward proactive intelligence that flat memory systems cannot take.
F.9 Construct Validity
Two metrics that most sharply separate COGNIFOLDfrom baselines—Purity (event-level grounding)
and Proactivity (intents with ≥2 groundings)—measure representational features that only COG-
NIFOLDemits: GROUNDS edges for Purity, intent nodes for Proactivity. A reader may reasonably
worry the metric is biased toward our representation. We address this risk with three choices: (i)
the representational hierarchy holds not only on these two metrics but also on task-agnostic ones
(Harmony, Gold F1, LLM Quality, Compression, Clustering), on which baselines are free to score
well; (ii) CogEval is deliberately supplemented by the broad 7-benchmark memory results (§4.5),
which use external benchmarks and metrics; (iii) we report raw intent counts and grounding densities,
not normalized scores. Even so, a fully adversarial benchmark—one where our representation could
lose—is future work.
F.10 Scale and Scope Limitations
CogEval-Bench uses synthetic events generated from predefined gold graphs, which may not capture
the full complexity of natural event streams. The scale is deliberately small (∼42 events per scenario)
to enable controlled structural evaluation; whether the structural hierarchy holds at larger scales
remains to be validated. The LLM judge introduces potential evaluation bias; we mitigate this by
per-concept independent scoring (not pairwise comparison) and report the full judge prompt above.
21

## Page 22

F.11 Event Generation Prompt
For each concept c with label ℓ and description d, events are generated using the following prompt
template:
Generate {n} realistic first-person events for a
{scenario} scenario, grounded in the concept
"{label}": {description}.
Each event should:
- Be a specific, timestamped experience (not generic)
- Use first-person perspective
- Be self-contained (understandable without context)
- Relate clearly to the concept keywords: {keywords}
Output as JSON array with fields: title, description,
timestamp, event_type.
Chain events use a sequential prompt that references entities from prior chain steps to maintain
cross-hop consistency. Distractor events are generated from unrelated topics (e.g., weather, unrelated
hobbies) without concept grounding.
F.12 LLM Judge Prompt
The concept quality judge evaluates each system concept independently:
Evaluate this concept extracted from an event stream.
Concept: "{concept_label}"
Grounding events (if any): {event_summaries}
Scenario context: {scenario_description}
Rate on three dimensions (0.0 to 1.0):
1. MEANINGFULNESS: Is this a semantically coherent
concept? (1.0 = clearly defined theme/pattern,
0.0 = incoherent or trivial)
2. GROUNDEDNESS: Is the concept well-supported by
its grounding events? (1.0 = strong evidence,
0.0 = no supporting evidence)
3. ABSTRACTION LEVEL: Is this the right level of
abstraction? (1.0 = useful generalization,
0.0 = too specific or too vague)
Output JSON: {"meaningfulness": X, "groundedness": X,
"abstraction": X}
F.13 Embedding Similarity Threshold Sensitivity
The Gold F1 computation uses cosine similarity ≥0.75 for concept matching. Table 15 reports
COGNIFOLD’s Harmony score averaged across 6 scenarios at varying thresholds, confirming that the
ranking is robust to threshold choice.
Table 15: Sensitivity of Harmony to embedding similarity threshold (CogniFold, averaged over 6
scenarios).
Threshold 0.65 0.700.750.80 0.85
Harmony 0.501 0.4890.4760.452 0.418
Higher thresholds are more conservative (fewer matches, lower recall); lower thresholds are more
permissive (more matches, risk of false positives). The relative ranking of systems is preserved across
all tested thresholds.
22

## Page 23

G Reproducibility
Code and data.Source code, benchmark runner scripts, and evaluation harnesses will be re-
leased upon publication. All benchmarks use publicly available datasets: MuTual [ 8], ToMi [29],
MuSiQue [57], NarrativeQA [24], StreamingQA [31], LoCoMo [32], and BABILong [27].
Compute.All experiments use the OpenAI API (GPT-4o-mini for generation, text-embedding-3-
small for embeddings). Graph construction and retrieval run on a single CPU; no GPU is required.
Total API cost for all experiments (including development iterations): approximately $150.
Randomness.The primary source of non-determinism is LLM sampling (temperature 0.0 for all
evaluation calls). Graph construction is deterministic given the same LLM outputs. Benchmark
sampling uses fixed random seeds (seed=42 for all dataset splits). Wilson confidence intervals are
reported for full-scale results (n≥100).
Broader impact.COGNIFOLDis a general-purpose cognitive memory architecture. Like any persis-
tent memory system, it raises privacy considerations: the graph accumulates personal information
that persists across sessions. Production deployments should implement access controls and data
retention policies. The system does not autonomously take actions; intent nodes represent identified
goals, not executed plans.
23
