# How to Interpret Agent Behavior - Extracted Text

- Source note: [[How to Interpret Agent Behavior]]
- Source PDF: `assets/How to Interpret Agent Behavior.pdf`
- Extracted: 2026-05-14
- Extractor: pypdf
- Pages: 34
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

How to Interpret Agent Behavior
Jie Gao1, Kaiser Sun 1, Jen-tse Huang 1, Katherine Van Koevering1, Sijie Ji 2,
Heyuan Huang1, Weiyan Shi3, Zhuoran Lu4, Ziang Xiao1∗, Daniel Khashabi1∗, Mark Dredze1∗
1Johns Hopkins University 2California Institute of Technology 3Northeastern University 4Purdue University
Abstract
Autonomous agents such as Claude Code and Codex now operate for hours or
even days. Understanding their runtime behavior has become critical for down-
stream tasks such as diagnosing inefficiencies, fixing bugs, and ensuring better
oversight.2 A primary way to gain this understanding is analyzing the reasoning
trajectories and execution traces these agents generate. Yet such data remains in
unstructured natural-language form, making it difficult for humans to interpret at
scale. We introduce Act·ONOMY, 3 a taxonomy for describing and analyzing agent
behavior at runtime. Act·ONOMYhas two components: (1)the taxonomy itself,
developed through Grounded Theory and structured as a three-level hierarchy of
10 actions, 46 subactions, and 120 leaf categories; and (2)an open repositorythat
hosts the living taxonomy, provides an automated analysis pipeline that applies it
to agent trajectory analysis, and defines an extension protocol for customization
and growth.4 Our experiments show that Act·ONOMYcan compare behavioral
profilesacross agentsand characterizea single agent’s behavior across diverse
trajectories, surfacing patterns indicative of failure modes. By providing a shared
vocabulary, Act·ONOMYhelps researchers, agent designers, and end users inter-
pret agent behavior more consistently, enabling better oversight and control.
“The limits of my language mean the limits of my world. ”
— Ludwig Wittgenstein,Tractatus Logico-Philosophicus
1 Introduction
Modern agents increasingly run autonomously, sometimes for hours or even days [23]. They now
tackle complex tasks such as solving GitHub issues [59, 53], navigating web interfaces [63], and
conducting research [31]. Over such extended executions, agents rarely succeed or fail cleanly;
more often, they fail and recover repeatedly before reaching a final outcome. Did the agent follow
an effective plan or a flawed one? Did it recover from errors, or get stuck in a loop? Did it hallucinate
outputs, or ask for help? Understanding what agents actually do during execution is critical for a
range of downstream tasks, from diagnosing and repairing agent design bugs and improving runtime
efficiency, to building human-centered systems that support meaningful oversight [41].
A central means of developing this understanding is to analyze agenttrajectories[6, 59], which are
sequential records of an agent’s planning, reasoning, and tool use. Recently, trajectory analysis has
accordingly emerged as an active research area [47, 57, 14]. Traditional analyses rely on quantitative
outcome metrics such as task success rate [59], which revealwhetheran agent succeeded but little
abouthoworwhy[6, 32]. Withouthoworwhy, it is difficult to identify what to fix, which in turn
makes it hard to push success rates higher. Recent work has therefore turned to more informative
∗These authors contributed equally to guiding this work.
2Byruntime behavior, we mean the observable actions an agent takes during execution.
3A combination ofAction and Taxonomy, pronounced /æk'ta:nemi/.
4GitHub repo:https://github.com/gaojie058/Act-onomy
Preprint.
arXiv:2605.13625v1  [cs.AI]  13 May 2026

## Page 2

/gid00020/gid00024/gid00006/gid00183/gid00003/gid00032/gid00041/gid00030/gid00035/gid00001/gid00194/gid00001pylint-dev/pylint
Turn 1 Turn 5 Turn 10 Turn 13
SWE-agent localizes and patches a pylint bug where --notes silently drops note tags that are entirely punctuation (e.g. silently dropping “???”)
A 13-turn successful bug-fixing trajectory
confirm • stumble • pinpoint
Turn 4 • Phase pivot Turn 6 • Recovery Turn 9 • Pinpoint
The agent confirmed the bug and 
pivoted to code localization.
Evaluating Reasoning Planning
Reasoning Retrieval
Selected behaviors:
The agent detected that the previous 
fix had failed and switched to a differ-
ent search term, breaking the loop.
The agent read the regex source 
and identified \b as the root cause 
of the bug.
Reflection Deciding Reasoning
Reasoning
Planning
ReasoningRetrieval
Reasoning
Turn 9 • A deep dive into how Act*ONOMY can be used to label a raw trajectory 
OBSERVATION THOUGHT ACTION
Reasoning Analyse source code
Thought: The regular expression 
pattern used to match note tags is 
constructed in lines 122-128.
Reasoning Pinpoint root cause mechanism
Thought: The pattern does not ac-
count for note tags that consist 
entirely of punctuation...
Plan deeper inspection 
before edit
goto 122
Planning
(scroll to the regex construction 
before patching)
human readable 
interpretations
Figure 1:Why do we need Act·ONOMY? Act·ONOMYcan be used to label agent trajectories
with human-readable action tags; we use a 13-turn SWE-bench trajectory as a running ex-
ample.Top:A phase overview of the trajectory onpylint-dev/pylint-5859, with color-coded
regions marking distinct turns.Middle:Three pivotal turns annotated with Act·ONOMYsub-action
tags: Turn 4 (confirm) verifies the bug and pivots to code localization; Turn 6 (stumble) detects a
failed fix and recovers with a new search strategy; Turn 9 (pinpoint) identifies\bin the regex as
the root cause.Bottom:A sentence-level zoom into Turn 9, grounding each tag in a specific quoted
span from the agent’s Observation→Thought→Action loop.
qualitative analysis [6], in which humans read trajectories directly to interpret agent behavior and
ground subsequent diagnosis or characterization. However, there are two challenges. First, trajec-
tories are unstructured: they appear as long, free-form, and often messy natural-language text, not
designed for human consumption [13]. Second, agents are a new kind of artifact that produces be-
haviors, and the research community has not yet converged on a shared vocabulary for describing
what they do [19, 48]. Researchers studying agent behavior thus lack an established conceptual and
vocabulary toolkit to draw on when reporting their findings. Without this toolkit, findings are hard
to communicate in ways others can build on, and behavioral knowledge cannot accumulate.The
gap between the growing complexity of agent runtime behavior and the vocabulary available
to describe and analyze it continues to widen.This motivates a fundamental question:“How do
we interpret agent behavior?”
We introduce Act·ONOMY, a taxonomy for describing and analyzing agent behavior at runtime. It
is grounded in a corpus of 565 behavior descriptions drawn from peer-reviewed publications on
AI agents between 2024 and 2026. We applied a grounded-theory approach [7] in which terms
emerged inductively from the corpus, while drawing on existing cognitive architecture frameworks
for theoretical grounding [49]. It comprises 10 top-level actions (e.g., planning, reasoning), 46
sub-actions (e.g., retrieving from local corpus, executing code), and 120 leaf-categories. Since the
field of autonomous agents is evolving rapidly, we envision Act·ONOMYas a living taxonomy. We
therefore host it as an open GitHub repository, where new behaviors (particularly sub-actions and
leaf categories) can be proposed, reviewed, and incorporated by the community. We demonstrate
Act·ONOMYthrough two case studies: one comparing behavioral profiles across multiple agents,
and another characterizing a single agent’s behavior within diverse trajectories.
In summary, our main contributions are as follows:
•Taxonomy.We propose Act·ONOMY, the first hierarchical taxonomy for describing and
analyzing observable agent behavior. It comprises 10 actions, 46 sub-actions, and 120 leaf
categories, theoretically grounded in literature [49] and empirically grounded in 565 agent
behavior descriptions drawn from the latest peer-reviewed papers at top AI venues.
2

## Page 3

Grounding
17.7%
Interact with users
6.3%
Augment external computation
4.4%
Interact with other agents
3.2%
Interact with physical environments
1.9%
Interact with digital environments
1.9%
Retrieval
4.4%
From external knowledge base
1.9%
From local corpus
1.3%
From open web
0.6%
From relevant context
0.6%
From skill library
—
Planning
10.8%
Decompose task
4.4%
Formulate workflow/plan
3.8%
Select strategy
1.3%
Modify plan
1.3%
Reasoning
25.9%
Generating
6.3%
Contextualizing
5.7%
Analyzing
3.8%
Inferring
3.2%
Combining & Synthesizing
3.2%
Comparing & Ranking
2.5%
Filtering
0.6%
Explaining
0.6%
Summarizing & Distilling
—
Evaluating
14.6%
Without ground truth
8.9%
With goals/constraints
3.8%
With gold
1.9%
Deciding
1.3%
Accept/reject
0.6%
Under uncertainty
0.6%
Make a decision
—
Pick scores
—
Executing
3.2%
Executing debug
1.3%
Terminating
1.3%
Executing plan
0.6%
Reflecting
14.6%
On errors/failures
7.0%
On self-outcomes
5.1%
On feedback
2.5%
Learning
3.8%
New knowledge
2.5%
Updating LLM parameters
1.3%
Updating reasoning
—
Updating grounding
—
Updating Instructions
—
Memory
3.8%
Discard information
1.3%
Consolidate memory
1.3%
Store information
0.6%
Read memory
0.6%
Update information
—
Figure 2: The Act·ONOMY: 10 main actions and 46 subactions. Within each category, sub-actions
are ordered by descending frequency.Italicizedrows (freq. “—”) marking sub-actions retained by
theoretical motivation but not yet observed in the construction corpus.Freq.is the share of paper-
grounded behavior-description sentences (n=120) drawn from the paper construction set.
•Automatic analysis tool.We provide anAutomated-Trace-Analysis-Toolpipeline
that automates the application of Act·ONOMYfor agent trajectory analysis, enabling users
to build behavioral profiles of agents at scale.
•Extensibility.We host an open repository to maintain Act·ONOMYas a living taxonomy
that absorbs new sub-actions as the technology evolves. We also provide an automatic tool
that lets users adapt the taxonomy according to their preferences and domain requirements.
•Use cases.We demonstrate Act·ONOMY’s utility through two case studies, applying it to
agent trajectories to compare behavioracrossandwithinagents.
2 Act·ONOMY: Describing and Analyzing Agent Behaviors at Scale
Interact with users
Augment external computation
Interact with other agents
Interact with physical envs
Interact with digital envs
From external knowledge base
From local corpus
From open web
From relevant context
From skill library
Decompose task
Formulate workflow/plan
Select strategy
Modify plan
Generating
Contextualizing
Analyzing
Inferring
Combining & Synthesizing
Comparing & Ranking
Filtering
Explaining
Summarizing & Distilling
Without ground truth
With goals/constraints
With gold
Accept/reject
Under uncertainty
Make a decision
Pick scores
Executing debug
Terminating
Executing plan
On errors/failures
On self-outcomes
On feedback
New knowledge
Updating LLM parameters
Updating reasoning
Updating grounding
Updating Instructions
Discard information
Consolidate memory
Store information
Read memory
Update information
Grounding
Retrieval
Planning
Reasoning
Evaluating
Deciding
Executing
Reflecting
Learning
Memory
/gid00045/gid00068/gid00064/gid00081/gid00077/gid00072/gid00077/gid00070/gid00001/gid00007/gid00001
/gid00034/gid00067/gid00064/gid00079/gid00083/gid00064/gid00083/gid00072/gid00078/gid00077
/gid00019/gid00019/gid00015/gid00019/gid00006
/gid00038/gid00087/gid00083/gid00068/gid00081/gid00077/gid00064/gid00075/gid00001
/gid00042/gid00077/gid00083/gid00068/gid00081/gid00064/gid00066/gid00083/gid00072/gid00078/gid00077
/gid00019/gid00019/gid00015/gid00018/gid00006
/gid00036/gid00078/gid00070/gid00077/gid00072/gid00083/gid00072/gid00078/gid00077/gid00001/gid00007/gid00001
/gid00038/gid00087/gid00068/gid00066/gid00084/gid00083/gid00072/gid00078/gid00077
/gid00022/gid00022/gid00015/gid00025/gid00006
Figure 3: An at-a-glance map of Act·ONOMY.
To build a shared vocabulary and con-
ceptual framework for describing and an-
alyzing agent behavior, we constructed
Act·ONOMYthrough a grounded theory
approach. Because the taxonomy is our
primary contribution, we present it first
and detail our methodology in §3.
2.1 Taxonomy Overview
Act·ONOMYorganizes agent behaviors
into 10 main actions, 46 subactions, and
120 leaf instances (Figure 2).
The first cluster captures how the agent
acquires information and interacts with
the external world. GROUNDINGde-
scribes behaviors through which the agent
exchanges information with external enti-
ties (e.g., users, physical or digital environments, peer agents, and external tools or computational
resources).RETRIEVALdescribes behaviors through which the agent obtains task-relevant infor-
mation from various information sources, including external knowledge bases, local corpora, and
the open web.
3

## Page 4

The second cluster captures how agents conduct internal cognition and carry out concrete ex-
ecution. REASONINGrefers to the internal cognitive operations the agent performs to produce new
content. Notably, reasoning was predominantly used to describe operations over information al-
ready present in the agent’s context; it does not reach outside the agent. It is also the most frequently
described behavior (25.9%), encompassing operations such as generating, analyzing, inferring, com-
paring & ranking & filtering, contextualizing, and combining & synthesizing (e.g.,“combine infor-
mation from multiple sources...to produce a coherent solution”(P2)). Although often co-occurring
with reasoning,PLANNING(10.8%) plays a distinct role: it is primarily used to decide what to
do next, including decomposing tasks into subgoals, formulating workflows, selecting strategies,
and modifying plans. For example,“the planner accurately interprets user intent and formulates a
comprehensive analysis workflow”(P1).EVALUATINGcaptures actions in which the agent judges
quality or correctness, either against gold-standard results or against specific criteria such as goals,
requirements, constraints, rubrics, or domain rules. For example,“independently checks whether
objectives are truly complete, preventing the orchestrator from advancing when the main agent in-
correctly believes a task is finished”(P25). It also frequently describes situations in which the agent
must evaluate in the absence of ground truth, relying instead on internal standards and heuristics
(e.g.,LLM-as-a-judge scoring,visualorbehavioral correctness checks). We treatDECIDINGas a
distinct subaction because it marks an important “commitment” phase in the overall task. For in-
stance, selecting among options surfaced by upstream actions, or determining whether to engage at
all. Similarly, we includeEXECUTINGas a distinct subaction because it captures phases in which
the agent commits to and carries out an action, e.g., executing a plan or terminating the run by deliv-
ering a final answer. Unlike cognitive subactions such as planning or reasoning,EXECUTINGrefers
only to the act of carrying out, not to the deliberation that precedes it. For example,an insertion
agent executes this plan for HLS-C optimization(P29).
The third cluster captures how the agent learns from experience and adapts to real-world com-
plexity. REFLECTINGdescribes actions in which the agent examines its own process, including
reflecting on failures, reflecting on self-generated outcomes, and incorporating external feedback.
Notably, in our corpus, reflection is most often used to describe “thinking about” past behavior
rather than “fixing” it. For example,“Given the [Chat History] REFLECT carefully on the AI as-
sistant’s last response”(P25). In contrast,LEARNINGhas less empirical grounding in our corpus
and reflects a more theory-driven framing; following Sumers et al. [49], we define it as the process
of updating an agent’s knowledge, reasoning procedures, or parameters in ways that persist across
episodes. However, in practice,LEARNINGandREFLECTINGare often used interchangeably in
the literature; we nevertheless retain them as separate categories to mark this subtle but meaning-
ful distinction.MEMORYcaptures actions that operate on the agent’s explicit external memory
resources, such as memory banks, scratchpads, and to-do lists. These actions include storing, updat-
ing, and discarding information.
2.2 Large-Scale Analysis of Agent Behavioral Descriptions
Grounding
Reasoning
Reflecting
Memory
Planning
Evaluating
Learning
Deciding
Retrieval
Executing
Grounding
Reasoning
Reflecting
Memory
Planning
Evaluating
Learning
Deciding
Retrieval
Executing
138
101
154
55
75
87
51
67
37
75
74
87
52
45
101
66
87
55
39
57
100
43
55
39
34
35
39
72
59
65
37
33
45
43
27
79
46
42
20
32
37
26
16
19
56
22
28
15
15
18
16
7
12
12
32
Action Co-occurrence (# of Papers)
Reasoning and Grounding co-oc-
cur in 101/211 papers  
Reasoning appears with every 
other action in >= 28 papers
Executing rarely 
co-occurs with 
others (<=28)
Planning and Evaluating 
co-occur with Reasoning 
most frequently
Figure 4: Action co-occurrence.
To examine how Act·ONOMYgeneralizes be-
yond its construction set, we applied it to 3,455
behavioral descriptions automatically extracted
from 211 behavior-related agent papers curated
by theawesome-language-agentsGitHub
list,5 spanning safety, evaluation, software en-
gineering, computer use, and web automation.
Two patterns stand out.(1) Frequency is
top-heavy at the Action level and long-tailed
at the Leaf level:GROUNDING(21.0%) and
REASONING(20.2%) alone cover over 40% of
descriptions and EXECUTING(1.8%) is rarely
described, yet at the leaf level the top-10 codes
each stay below 6% (see Appendix 8a). This
shows that current research attention concen-
trates on a few high-level behaviors while the
fine-grained vocabulary remains broad and di-
5github.com/ysymyth/awesome-language-agents
4

## Page 5

Theory Seeding
Verb Noun+
Verb + Noun format LLM Discovery 
Qualitative Analyst
Peer Review 
& Discussion
 Sentence-level
Inter-Rater Reliability
1 2 3 4 5
CoALA
Codebook V1 Codebook V2
Codebook V3
Formalizing coding schema
Humans Verify
+
6 coauthors verify / revise
Codebook V4
(v4.1, v4.2)
Multi-round consensus
Phase 1 Constructing Taxonomy Phase 2 Validating Taxonomy
Figure 5: An Overview of our Grounded Theory [7] pipeline to construct Act·ONOMY.
verse.(2) REASONINGco-occurs broadly with other actions(Figure 4): it appears with every
other action in≥28 papers and pairs with GROUNDINGin 101 papers, the most frequent pair across
the corpus. EXECUTING, by contrast, co-occurs sparsely (≤28), suggesting that most papers de-
scribe what agents think and observe but treat acting itself as incidental. Per-level frequency bar
charts and sub-action / leaf-level co-occurrence heatmaps are provided in Appendix F.
3 Construct and Extend Act·ONOMY: A Grounded Theory Approach
We construct Act·ONOMYvia a grounded theory approach [8, 7], a qualitative method well-suited
for surfacing vocabulary in emerging, ill-defined domains and previously used to study agent failure
modes [6]. We further anchor it in the Cognitive Architectures for Language Agents (CoALA)
framework [49], which provides foundational action-space definitions such as planning, reasoning,
and learning. Figure 5 overviews our method.
Phase 1: Constructing Taxonomy.We build Act·ONOMYfrom 565 behavioral descriptions ex-
tracted from 35 peer-reviewed agent papers, selected after 6 co-authors reviewed 664 candidate
sentences and dropped 99 from off-topic papers (Appendix C). The construction proceeds in three
stages (Figure 5, left).(1) Seed (V1→V2).We initializedCodebook V1based on our guiding theo-
retical framework [49], populating it with high-level categories (e.g., planning, reasoning, retrieval)
along with descriptive sentences characterizing agent behavior under each. We then reformulate
each seed behavior into a “verb + noun” form (V2); this brings heterogeneous descriptions to a uni-
form level of abstraction and surfaces the two minimal components of an agent action, operation and
object.(2) Scale and review (V2→V3).ALLM-powered-Discovery-Qualitative-Analyst
(Appendix D), given the current codebook and a behavior description, either matches it to an ex-
isting code or proposes a new one with a quoted evidence span. Six co-author annotators (one as
the main annotator) split the descriptions into batches and, for every (description,suggested code)
pair, independentlyverify,accept,proposea new code,renamefor clarity, ordiscardit. 8 off-topic
papers were dropped (99 sentences); the remaining 565 yieldedV3.(3) Refine (V3→V4.2).The
six co-authors collectively reviewed V3 over multiple rounds, producingV4.1;V4.2further extends
this with 120 leaf-level instances (Table 2).
Phase 2: Validating Taxonomy.We validateCodebook V4.1along two axes (Figure 5, right).
(1) Mapping reliability.Two authors independently coded 50 behavior sentences from a held-
out validation set (multi-label allowed), followed by multiple rounds of discussion and codebook
refinement, yielding Cohen’sκ= 0.87at the action level and0.72at the sub-action level, substantial
agreement indicating the codebook is relatively clear and consistent. AnLLM-powered deductive
analystreplicates the primary coder’s decisions with Cohen’sκ= 0.74at the action level and0.71
at the subaction level.(2) Theoretical saturation.We apply the finalized V4.2 codebook to a
held-out set using the sameLLM-powered deductive analyst: no new actions emerge, and any new
sub-actions are minor variations of existing ones, indicating that Act·ONOMYhas reached initial
saturation at the Action level and is close to saturation at the Sub-action level (Table 3). Overall, the
construction and validation process required substantial human effort: all six co-authors contributed
over 6 hours of annotation, with the primary and secondary annotators investing more than 20 and
10 hours, respectively.
Toolkit for Extending Act·ONOMY.We treat Act·ONOMYas a living taxonomy: the main actions
and sub-actions are expected to remain relatively stable, while the leaf level continues to expand
5

## Page 6

as new agents emerge and new behavior descriptions are added. We support extension through
Automated-Codebook-Extension-Tool, which automatically propagates codebook changes to
dependent files (Appendix G).
4 How Can Act·ONOMYSupport Downstream Tasks?
A primary purpose of Act·ONOMYis to support downstream tasks such as trajectory analysis for
understanding agent behaviors. We first propose an automated pipeline for describing and analyzing
trajectories, and then present two case studies that illustrate its use in practice.
4.1 Toolkit for Applying Act·ONOMYin Agent Behavior Analysis at Scale.
We leverage LLM-powered qualitative coding to deductively apply a codebook for downstream
trajectory analysis. We developAutomated-Trace-Analysis-Tool, which performs:
1.Preprocessing.Given a trajectory from any agent framework (e.g., SWE-agent, AG2) as
input,Automated-Trace-Analysis-Toolparses it into a sequence of per-turn triples of
observation,thought, andaction.
2.Behavioral indicator extraction.Within each turn,Automated-Trace-Analysis-Tool
identifies behavior-indicating spans in both thethoughtand theaction.
3.Codebook assignment.Each extracted span is annotated with anaction–subaction–leaf
label. When no suitable subaction or leaf exists,Automated-Trace-Analysis-Tool
proposes new ones to extend the codebook.
4.Aggregation and summarization.Automated-Trace-Analysis-Toolcomputes statis-
tics over the annotated trajectory, segments it into coherent sessions, and generates a
natural-language summary describing what the agent did in each session.
5.Profile presentation.The statistics, summaries, and grounded annotations are compiled into
a behavioral profile that users can interactively inspect to understand the agent’s behavior.
We iteratively refinedAutomated-Trace-Analysis-Tooluntil its labels reached substantial
agreement with human coders on a held-out set of trajectories (Cohen’sκ >0.81at every level),
supporting its use as a scalable annotator. We implement this pipeline as a Claude Code Skill to
ensure easy usage (see Appendix H).
4.2 Understanding Similarities and Differences in Behavior DistributionsAcross Agents.
One use case for Act·ONOMYis to characterize each agent’s behavior profile both qualitatively and
quantitatively. We selected three agents from different domains and tasks to perform automatic
trajectory analysis usingAutomated-Trace-Analysis-Tool: AG2 [55], HyperAgent [39], and
SWE-Agent [59]. We collected 300 traces from their public trajectories in total, and our automated
analysis produced 100 action sequence representations per agent. We compare them from two per-
spectives: their individual action distributions (Figure 6a) and their deviations from the average
behavior across all agents (Figure 6b).Similarity and Differences:Overall, the three agents share
a similar high-level pattern: REASONINGand EXECUTINGdominate, while LEARNINGaccounts
for the smallest share.Beyond this, however, their profiles diverge in ways that reflect each
agent’s architecture and intended task. AG2scores significantly above average on EVALUAT-
ING, GROUNDING, and DECIDING, while scoring significantly below average on RETRIEVALand
REFLECTING. This aligns with its focus on math problems, where verifying whether results match
the gold answer is central, with low requirement on retrieval capabilities.HyperAgentis the only
agent that scores significantly above average on REFLECTING, and is also significantly above aver-
age on REASONINGand MEMORY, while scoring significantly below average on EXECUTINGand
GROUNDING. This pattern is consistent with its multi-agent architecture solving repository-level
software engineering tasks, which demand extensive context and rely on multiple agents communi-
cating through structured context design and organization.SWE-Agentscores far above average on
EXECUTING, while scoring far below average on REASONINGand GROUNDING. This is consistent
with the analysis in the original paper [59], which reports that reproduction, editing, and submis-
sion together account for∼57% of actions, matching our finding that SWE-Agent is dominated by
EXECUTING.Notably, Act·ONOMYcan surface action categories that human analysis tends
to overlook.For instance, SWE-Agent still produces non-trivial amounts of PLANNING, EVALU-
6

## Page 7

Reasoning
Executing
Grounding
Planning
Evaluating
Memory
Deciding
Retrieval
Reflecting
Learning
0
10
20
30
40
% of agent's quotes
24.0
20.3
18.3
14.7
13.6
4.1
2.8
1.5
0.8
0.0
AG2 (n=1006)
All-agents avg
Reasoning
Executing
Retrieval
Planning
Grounding
Evaluating
Reflecting
Memory
Deciding
Learning
0
10
20
30
40
24.0
17.3
13.3
13.2
12.9
8.8
4.7
4.4
1.1
0.2
HyperAgent (n=4375)
Executing
Reasoning
Retrieval
Planning
Grounding
Evaluating
Memory
Reflecting
Deciding
Learning
0
10
20
30
40
29.5
15.7
13.4
11.5
10.9
9.1
4.5
3.7
1.6
0.0
SWE-Agent (n=2863)
Retrieval
Evaluating
Reflecting
Grounding
Deciding
Planning
Reasoning
Executing
Learning
Memory
−20
−10
0
10
20
Deviation from average (z-score)
-11.3*
+6.2*
-5.5*
+3.9*
+3.4*
+2.4*
+2.3*
-1.1
-1.0
+0.5
AG2 leans on its own
evaluating, not on lookups
Executing
Reasoning
Grounding
Deciding
Reflecting
Memory
Learning
Planning
Retrieval
Evaluating
−20
−10
0
10
20
-9.2*
+6.1*
-3.3*
-3.1*
+2.9*
+2.8*
+2.4*
+2.3*
+1.6
+1.2
HyperAgent prefers thinking
over shell-side execution
Executing
Reasoning
Grounding
Memory
Learning
Planning
Evaluating
Retrieval
Reflecting
Deciding
−20
−10
0
10
20
+12.1*
-8.4*
-6.0*
+2.5*
-2.0
-1.6
+1.5
+1.2
-1.0
+0.2
SWE-Agent does executing a lot
■
above average (z > 0)
■
below average (z < 0)
*
significantly different from average (|z| ≥ 2)
(a) What each agent
does most
(b) Where each agent stands out
from the average
Figure 6: Three agents show distinct behavioral profiles. (a) Action distribution for each agent;
(b) each agent’s largest deviations from the cross-agent average, measured as az-score from aχ 2
test of independence.
ATING, DECIDING, REFLECTING, LEARNING, and MEMORYactions. These were missed in the
original human analysis [59] but surfaced automatically by Act·ONOMY.
4.3 Understanding Behavior DistributionsWithin a Single Agent.
After examining how Act·ONOMYdifferentiatesacrossagents, we now turn to how it characterizes
variationwithina single agent’s behavior. We select two trajectories generated by SWE-agent [59]
on GitHub issue-repair tasks from SWE-bench: Trace 1,psf/requests-2317, which the agent
resolved, and Trace 2,django/django-14411, which it did not. Figure 7 presents the per-turn
breakdown of both runs, theAutomated-Trace-Analysis-Tool-generated Act·ONOMYtags, and
the session-level summaries characterizing the agent’s behavior.
Trajectory-level shape.Although both trajectories are dominated by REASONINGand EXECUT-
ING, a pattern consistent with SWE-agent’s task domain, they diverge significantly in their behav-
ioral composition. Trace 1 includes 10 turns and 33 Act·ONOMYtags, organized into four phases:
locate the bug,patch the bug,verify the fix, andsubmit. Trace 2, by contrast, extends to 16 turns and
53 tags across five phases:search for the bug,hit a dead end,hit a second dead end,find the correct
file, andpatch, recover, and submit. The two runs also differ in their internal balance: Trace 1 dis-
tributes tags evenly between REASONINGand EXECUTING(N=9 each), whereas Trace 2 is heavily
skewed toward REASONING(22 of 53 tags) over EXECUTING(14 tags). This shift is attributable to
the prolonged search and dead-end phases, signaling a more convoluted problem-solving process.
These compositional differences mirror the eventual outcomes: Trace 1 successfully resolves the
task, while Trace 2, despite its longer run, ultimately fails.
Surfacing a fine-grained failure mode.Beyond high-level differences in action distributions, leaf-
level analysis reveals subtle yet critical insights into the agent’s problem-solving process. As il-
lustrated on the right of Figure 7,Automated-Trace-Analysis-Toolassigns a series of quote-
grounded labels to the agent’s thought and action: (i)Reasoning→Inferring→Conclude success
from evidence(“The changes ... have been successfully applied”); (ii)Evaluating→Evaluating with
gold→Plan verification step(“it would be prudent to test that the changes have the desired effect”);
(iii)Evaluating→Evaluating without ground truth→Recognize knowledge boundary(“since we
cannot run a Django server ... we will proceed with submitting”); and (iv)Executing→Terminating
→Terminate rollout with submission(“Let’s submit the changes ... using the submit command”).
Taken together, these four labels expose a“submit anyway, without verifying”failure pattern: the
7

## Page 8

Submit anyway, without verifying
T1
T2
T3
T4
T5
T6
T7
T8
T9
T10
0
2
4
# Act*ONOMY quotes
psf/requests-2317 (resolved)
T1
T2
T3
T4
T5
T6
T7
T8
T9
T10
T11
T12
T13
T14
T15
T16
0
2
4
# Act*ONOMY quotes
django/django-14411 (unresolved)
Planning
Reasoning
Memory
Executing
Deciding
Reflecting
Evaluating
Act*ONOMY Auto-Analysis 
Agent searches for 
the bug
Agent’s find_file lookup 
misses; search_dir returns 9 
hits; agent picks helpers.py 
and zooms to line 215
Agent hits a dead 
end in helpers.py
Agent sees the read_on-
ly branch at line 215 
doesn’t render a...
Agent hits a 
second dead 
end
Agent traces the widget 
class to its HTML tem-
plate, finds no...
Agent finds 
the right spot
Agent searches 
inside forms.py and 
opens UserChan
Agent patches, 
recovers, and 
submits
T14: agent overrides 
label_tag at the field 
level. T15...
Agent locates the 
bug
Agent opens sessions.py, 
skips the duplicate copy 
under build/lib/, searches 
for ...
Agent 
patches 
the bug
Agent spots the 
bytes → string 
conversion bug 
and inserts...
Agent verifies 
the fix
Agent writes repro-
duce_issue.py, runs 
it against the live 
requests import, 
sees 200...
Agent submits
Agent wraps up 
cleanly once the fix 
is verified.
Figure 7:Two SWE-agent trajectories produce contrasting behavioral shapes.Stacked bars
show per-turn Act·ONOMYcategories assigned byAutomated-Trace-Analysis-Tool, accompa-
nied by its automatically generated natural-language session summaries. The callout zooms in on
the leaf-level, quote-grounded labels that pinpoint specific behaviors driving the agent’s decision.
agent acknowledges the need for verification, recognizes its inability to perform one, and proceeds
to submit nonetheless. Such a pattern is invisible at the trajectory level and prohibitively tedious
to recover from raw traces, yetAutomated-Trace-Analysis-Toolsurfaces it directly through
its action sequences and behavior breakdowns. This fine-grained analysis can help practitioners
identify recurring failure patterns and design appropriate interventions.
5 Related Work
Trajectory analysis of LLM agents.Most analyses of LLM agents rely on quantitative outcome
metrics: AgentBench [30], AgentBoard [32], and SWE-bench [21] report task success, progress,
or issue-resolution rates. Such metrics tell uswhetheran agent succeeded but little abouthowor
why. Analyzing trajectories can be valuable to understand the dynamics of agent behavior, however,
agent trajectories are long, free-form, often-messy natural-language text not designed for human
consumption, which makes systematic manual analysis costly and hard to scale. Recent work that
does inspect trajectories mainly focuses on failure modes or ad-hoc analysis. First, the focus is
largely onfailure: Cemri et al. [6] taxonomize multi-agent failure modes, and Kapoor et al. [22]
catalog reliability gaps, leaving a spectrum of agent behaviors largely unexamined. Second, the few
exceptions are agent-specific, e.g., manual analyses of how SWE-agent navigates repositories [59],
with terminology that does not transfer across systems. As a result, there is no shared vocabulary
for characterizing agent runtime behavior. Act·ONOMYtargets this gap with a descriptive taxonomy
that describes and analyzes agent behavior, paired with an automated pipeline that automatically
turns unstructured trajectories into human-readable behavioral profiles at scale.
Action-space and cognitive-architecture frameworks.A complementary line of work conceptu-
alizes agents through cognitive architectures. CoALA [49] organizes language agents around exter-
nal actions (interacting with users, environments, and tools) and internal actions (retrieval, reason-
ing, learning). Earlier theoretical foundations from Newell’s unified theory of cognition [35, 1, 51]
offer operational criteria for cognition such as adaptivity, robustness, and self-awareness, which map
naturally onto behaviors observable in LLM agents. From a more concrete angle, WorldAPIs [36]
8

## Page 9

approaches the action space empirically by inducing primitive APIs from wikiHow tutorials. How-
ever, researchers, developers, and end users lack a shared framework for describing and analyzing
what agentsactuallydo at runtime. Act·ONOMYcomplements them with the descriptive vocabu-
lary needed for trajectory analysis: 10 actions, 46 sub-actions, theoretically grounded in cognitive-
architecture theory and empirically grounded in behavioral descriptions written by AI researchers.
Qualitative coding with LLMs.Qualitative methods such as grounded theory [7, 8] and the-
matic analysis [5, 10] have a long tradition of turning unstructured natural-language data into a
structured, human-interpretable vocabulary. Recent work shows that LLMs can scale parts of this
pipeline [15, 16, 37]. We build on this line in two ways. First, we use human qualitative coding
to derive Act·ONOMYinductively from agent papers while drawing on cognitive-architecture theory
as a sensitizing construct. Second, we provideAutomated-Trace-Analysis-Tool, an LLM-as-
qualitative-coder pipeline that applies Act·ONOMYto agent trajectories at scale.
6 Discussion
Behavioral interpretability as a complement to mechanistic interpretability.Most current
work on understanding language-model systems looksinsidethe model via probing [2], sparse au-
toencoders [12], and circuit analysis [52, 11]. Act·ONOMYargues for a complementary lens that
looksat the trajectory: agents are now complex enough to warrant ethological description [41],
not only mechanistic dissection. Outcome metrics such as pass@1 or turn count [22, 32] cannot
distinguish a cleanlocate–patch–verify–submitrun from asearch–dead-end–submit-anywayrun,
whereas a behavioral profile, with its quote-grounded leaf categories, makes this distinction explicit.
A natural next step is to link behavioral codes back to internal model state—for instance, probing
for REFLECTING[46] or PLANNING[60, 62]—so that Act·ONOMYcan serve as a bridge between
behavioral and mechanistic interpretability.
Implications for agent observability and oversight.Behavioral profiles open a practical surface
for agent monitoring [14, 13]. Across-agent profiles surfacearchitectural fingerprintsthat distin-
guish single-task math agents from repository-scale multi-agent systems (Case Study 4.2); within-
agent profiles surfacetrajectory-level patternsandfailure precursors, such as the elevated share
of REASONINGon complex tasks and the “submit anyway, without verifying” pattern surfaced by
quote-grounded T16 labels (Case Study 4.3). Ad-hoc behavioral analyses already appear across
recent agent papers [59, 6], but each invents its own categories. Act·ONOMYconsolidates them
into a shared codebook, enabling scalable downstream tasks: behavioral regression testing across
agent versions [43, 3, 42, 33], behavioral drift detection in production [40], and oversight [4] of
long-running agents whose raw traces would otherwise be too voluminous to read [57]. By giving
researchers, designers, and end users a shared vocabulary, Act·ONOMYaims to make agent behavior
something that can be discussed, compared, and built upon rather than re-described from scratch by
every new system.
7 Conclusion
As modern AI agents grow increasingly complex and autonomous, describing and analyzing their
behavior has become correspondingly difficult. We began with a fundamental question:how do
we interpret agent behavior?In response, we introduce Act·ONOMY, a taxonomy that provides a
shared vocabulary for agent behavior, empirically grounded in 565 behavioral descriptions drawn
from 35 agent papers (2024–2026) and theoretically anchored in cognitive-architecture research.
Act·ONOMYcomprises two components: (1)the taxonomy itself, organized as a three-level hier-
archy of 10 actions, 46 subactions, and 120 leaf categories; and (2)an open repositorythat hosts
the living taxonomy alongside two supporting artifacts:Automated-Trace-Analysis-Tool, an
automated analysis pipeline that produces quote-grounded annotations of raw trajectories, and an ex-
tension protocol that enables the community to incorporate new actions over time. Two case studies
demonstrate the utility of Act·ONOMYfor both across-agent and within-agent analysis. We position
Act·ONOMYas a starting point: a living vocabulary for the agents we study today, designed to grow
into one for the agents we have yet to build.
9

## Page 10

References
[1] J. R. Anderson and C. Lebiere. The newell test for a theory of cognition.Behavioral and brain
Sciences, 26(5):587–601, 2003.
[2] Y . Belinkov. Probing classifiers: Promises, shortcomings, and advances.Computational
Linguistics, 48(1):207–219, Mar. 2022. doi: 10.1162/coli a 00422. URLhttps:
//aclanthology.org/2022.cl-1.7/.
[3] V . P. Bhardwaj. Agentassay: Token-efficient regression testing for non-deterministic ai agent
workflows, 2026. URLhttps://zenodo.org/doi/10.5281/zenodo.18842011.
[4] S. R. Bowman, J. Hyun, E. Perez, E. Chen, C. Pettit, S. Heiner, K. Luko ˇsi¯ut˙e, A. Askell,
A. Jones, A. Chen, A. Goldie, A. Mirhoseini, C. McKinnon, C. Olah, D. Amodei, D. Amodei,
D. Drain, D. Li, E. Tran-Johnson, J. Kernion, J. Kerr, J. Mueller, J. Ladish, J. Landau,
K. Ndousse, L. Lovitt, N. Elhage, N. Schiefer, N. Joseph, N. Mercado, N. DasSarma, R. Lar-
son, S. McCandlish, S. Kundu, S. Johnston, S. Kravec, S. E. Showk, S. Fort, T. Telleen-
Lawton, T. Brown, T. Henighan, T. Hume, Y . Bai, Z. Hatfield-Dodds, B. Mann, and J. Ka-
plan. Measuring progress on scalable oversight for large language models, 2022. URL
https://arxiv.org/abs/2211.03540.
[5] V . Braun and V . Clarke. Using thematic analysis in psychology.Qualitative research in psy-
chology, 3(2):77–101, 2006.
[6] M. Cemri, M. Z. Pan, S. Yang, L. A. Agrawal, B. Chopra, R. Tiwari, K. Keutzer,
A. Parameswaran, D. Klein, K. Ramchandran, M. Zaharia, J. E. Gonzalez, and I. Stoica. Why
do multi-agent llm systems fail?, 2025. URLhttps://arxiv.org/abs/2503.13657.
[7] K. Charmaz.Constructing grounded theory: A practical guide through qualitative analysis.
sage, 2006.
[8] K. Charmaz. Grounded theory.Qualitative psychology: A practical guide to research methods,
3(2015):53–84, 2015.
[9] P. Chong, H. Abichandani, J. Shen, A. Ghosh, M. P. Moe, Y . Mai, and D. Dahlmeier. Talk,
evaluate, diagnose: User-aware agent evaluation with automated error analysis, 2026. URL
https://arxiv.org/abs/2603.15483.
[10] V . Clarke and V . Braun. Thematic analysis.The journal of positive psychology, 12(3):297–298,
2017.
[11] A. Conmy, A. N. Mavor-Parker, A. Lynch, S. Heimersheim, and A. Garriga-Alonso. Towards
automated circuit discovery for mechanistic interpretability, 2023. URLhttps://arxiv.or
g/abs/2304.14997.
[12] H. Cunningham, A. Ewart, L. Riggs, R. Huben, and L. Sharkey. Sparse autoencoders find
highly interpretable features in language models, 2023. URLhttps://arxiv.org/abs/23
09.08600.
[13] D. Deshpande, V . Gangal, H. Mehta, J. Krishnan, A. Kannappan, and R. Qian. Trail: Trace
reasoning and agentic issue localization, 2025. URLhttps://arxiv.org/abs/2505.086
38.
[14] M. Desmond, J. Y . Lee, I. Ibrahim, J. M. Johnson, A. Sil, J. MacNair, and R. Puri. Agent
trajectory explorer: Visualizing and providing feedback on agent trajectories. InProceedings
of the AAAI Conference on Artificial Intelligence, volume 39, pages 29634–29636, 2025.
[15] T. Fischer and C. Biemann. Exploring large language models for qualitative data analysis. In
M. H ¨am¨al¨ainen, E. ¨Ohman, S. Miyagawa, K. Alnajjar, and Y . Bizzoni, editors,Proceedings
of the 4th International Conference on Natural Language Processing for Digital Humanities,
pages 423–437, Miami, USA, Nov. 2024. Association for Computational Linguistics. doi:
10.18653/v1/2024.nlp4dh-1.41. URLhttps://aclanthology.org/2024.nlp4dh-1.41/.
10

## Page 11

[16] J. Gao, Y . Guo, G. Lim, T. Zhang, Z. Zhang, T. J.-J. Li, and S. T. Perrault. Collabcoder:
a lower-barrier, rigorous workflow for inductive collaborative qualitative analysis with large
language models. InProceedings of the 2024 CHI conference on human factors in computing
systems, pages 1–29, 2024.
[17] C. Hu, L. Zhang, Y . Lim, A. Wadhwani, A. Peters, and D. Kang. Repro-bench: Can agentic ai
systems assess the reproducibility of social science research?, 2025. URLhttps://arxiv.
org/abs/2507.18901.
[18] X. Hu, Z. Zhao, S. Wei, Z. Chai, Q. Ma, G. Wang, X. Wang, J. Su, J. Xu, M. Zhu, Y . Cheng,
J. Yuan, J. Li, K. Kuang, Y . Yang, H. Yang, and F. Wu. Infiagent-dabench: Evaluating agents
on data analysis tasks, 2024. URLhttps://arxiv.org/abs/2401.05507.
[19] F. Jia, Z. Ye, S. Lai, K. Shu, J. Gu, A. Bibi, Z. Hu, D. Jurgens, J. Evans, P. H. Torr, et al. Can
large language model agents simulate human trust behavior?Advances in neural information
processing systems, 37:15674–15729, 2024.
[20] Z. Jiang, H. Guo, C. Fang, C. Xiao, X. Hu, L. Sun, and M. Xu. Medvr: Annotation-free
medical visual reasoning via agentic reinforcement learning, 2026. URLhttps://arxiv.or
g/abs/2604.08203.
[21] C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and K. Narasimhan. Swe-bench:
Can language models resolve real-world github issues? InInternational Conference on Learn-
ing Representations, volume 2024, pages 54107–54157, 2024.
[22] S. Kapoor and A. Narayanan. Ai agents that matter.arXiv preprint arXiv:2407.01502, 2024.
[23] T. Kwa, B. West, J. Becker, A. Deng, K. Garcia, M. Hasin, S. Jawhar, M. Kinniment, N. Rush,
S. V . Arx, R. Bloom, T. Broadley, H. Du, B. Goodrich, N. Jurkovic, L. H. Miles, S. Nix, T. Lin,
N. Parikh, D. Rein, L. J. K. Sato, H. Wijk, D. M. Ziegler, E. Barnes, and L. Chan. Measuring ai
ability to complete long software tasks, 2026. URLhttps://arxiv.org/abs/2503.14499.
[24] K. Li, J. Shi, Y . Xiao, M. Jiang, J. Sun, Y . Wu, D. Fu, S. Xia, X. Cai, T. Xu, et al. Agencybench:
Benchmarking the frontiers of autonomous agents in 1m-token real-world contexts.arXiv
preprint arXiv:2601.11044, 2026.
[25] R. Li, J. Xiong, X. He, J. Zhao, J. Lv, H. Fang, L. Qi, and X. Wang. Chathls: Towards
systematic design automation and optimization for high-level synthesis, 2026. URLhttps:
//arxiv.org/abs/2507.00642.
[26] X. Li, J. Gao, S. Lin, X. Zhou, C. Zhang, B. Cheng, J. Han, and B. Wang. Human or machine?
a preliminary turing test for speech-to-speech interaction, 2026. URLhttps://arxiv.org/
abs/2602.24080.
[27] J. Liao, Y . Feng, Y . Zheng, J. Zhao, S. Wang, and J. Zheng. My words imply your opinion:
Reader agent-based propagation enhancement for personalized implicit emotion analysis. In
Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 16156–16172, 2025.
[28] J. Liu, C. Huang, Z. Guan, W. Lei, and Y . Deng. E2edev: Benchmarking large language models
in end-to-end software development task, 2025.
[29] W. Liu, S. An, J. Lu, M. Wu, T. Li, X. Wang, C. Lv, X. Zheng, D. Yin, X. Sun, and
X. Huang. Tell me what you don’t know: Enhancing refusal capabilities of role-playing
agents via representation space analysis and editing. In W. Che, J. Nabende, E. Shutova,
and M. T. Pilehvar, editors,Findings of the Association for Computational Linguistics: ACL
2025, pages 5983–6005, Vienna, Austria, July 2025. Association for Computational Lin-
guistics. ISBN 979-8-89176-256-5. doi: 10.18653/v1/2025.findings-acl.311. URL
https://aclanthology.org/2025.findings-acl.311/.
[30] X. Liu, H. Yu, H. Zhang, Y . Xu, X. Lei, H. Lai, Y . Gu, H. Ding, K. Men, K. Yang, et al. Agent-
bench: Evaluating llms as agents. InInternational Conference on Learning Representations,
volume 2024, pages 52989–53046, 2024.
11

## Page 12

[31] C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune, and D. Ha. The ai scientist: Towards fully
automated open-ended scientific discovery, 2024. URLhttps://arxiv.org/abs/2408.0
6292.
[32] C. Ma, J. Zhang, Z. Zhu, C. Yang, Y . Yang, Y . Jin, Z. Lan, L. Kong, and J. He. Agent-
board: An analytical evaluation board of multi-turn llm agents. In A. Globerson, L. Mackey,
D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang, editors,Advances in Neural Infor-
mation Processing Systems, volume 37, pages 74325–74362. Curran Associates, Inc., 2024.
doi: 10.52202/079017-2365.
[33] W. Ma, Y . Yang, Q. Hu, S. Ying, Z. Jin, B. Du, Z. Xing, T. Li, J. Shi, Y . Liu, and L. Jiang. Re-
thinking testing for llm applications: Characteristics, challenges, and a lightweight interaction
protocol, 2025. URLhttps://arxiv.org/abs/2508.20737.
[34] E. Meyerson and X. Qiu. Position: Scaling llm agents requires asymptotic analysis with llm
primitives, 2025. URLhttps://arxiv.org/abs/2502.04358.
[35] A. Newell.Unified theories of cognition. Harvard University Press, 1994.
[36] J. Ou, A. Uzunoglu, B. V . Durme, and D. Khashabi. Worldapis: The world is worth how many
apis? a thought experiment, 2025. URLhttps://arxiv.org/abs/2407.07778.
[37] A. Parfenova, A. Marfurt, J. Pfeffer, and A. Denzler. Text annotation via inductive coding:
Comparing human experts to LLMs in qualitative data analysis. In L. Chiruzzo, A. Ritter, and
L. Wang, editors,Findings of the Association for Computational Linguistics: NAACL 2025,
pages 6471–6484, Albuquerque, New Mexico, Apr. 2025. Association for Computational Lin-
guistics. ISBN 979-8-89176-195-7. doi: 10.18653/v1/2025.findings-naacl.361. URL
https://aclanthology.org/2025.findings-naacl.361/.
[38] D. Paul, D. Murphy, M. Gritta, R. Cardenas, V . Prokhorov, L. S. Bolliger, A. Toker, R. Miles,
A.-M. Oncescu, J. A. Sivakumar, P. Borchert, I. Elezi, M. Zhang, K. Y . Lee, G. Zhang, J. Wang,
and G. Lampouras. A benchmark for deep information synthesis, 2026. URLhttps://arxi
v.org/abs/2602.21143.
[39] H. N. Phan, T. N. Nguyen, P. X. Nguyen, and N. D. Q. Bui. Hyperagent: Generalist software
engineering agents to solve coding tasks at scale, 2025. URLhttps://arxiv.org/abs/24
09.16299.
[40] C. Qin, X. Feng, W. Ma, X. Feng, and L. Kong. Implicitmembench: Measuring unconscious
behavioral adaptation in large language models, 2026. URLhttps://arxiv.org/abs/26
04.08064.
[41] I. Rahwan, M. Cebrian, N. Obradovich, J. Bongard, J.-F. Bonnefon, C. Breazeal, J. W. Cran-
dall, N. A. Christakis, I. D. Couzin, M. O. Jackson, N. R. Jennings, E. Kamar, I. M. Kloumann,
H. Larochelle, D. Lazer, R. McElreath, A. Mislove, D. C. Parkes, A. S. Pentland, M. E.
Roberts, A. Shariff, J. B. Tenenbaum, and M. Wellman. Machine behaviour.Nature, 568
(7753):477–486, 2019. doi: 10.1038/s41586-019-1138-y.
[42] T. Rehan. Test-driven ai agent definition (tdad): Compiling tool-using agents from behavioral
specifications, 2026. URLhttps://arxiv.org/abs/2603.08806.
[43] M. T. Ribeiro, T. Wu, C. Guestrin, and S. Singh. Beyond accuracy: Behavioral testing of nlp
models with checklist, 2020. URLhttps://arxiv.org/abs/2005.04118.
[44] R. D. Santi, F. A. Joseph, N. Liniger, M. Mutti, and A. Krause. Geometric active exploration
in markov decision processes: the benefit of abstraction, 2024. URLhttps://arxiv.org/
abs/2407.13364.
[45] H. Shi, Z. Sun, X. Yuan, M.-A. C ˆot´e, and B. Liu. OPEx: A component-wise analysis
of LLM-centric agents in embodied instruction following. In L.-W. Ku, A. Martins, and
V . Srikumar, editors,Proceedings of the 62nd Annual Meeting of the Association for Com-
putational Linguistics (Volume 1: Long Papers), pages 622–636, Bangkok, Thailand, Aug.
2024. Association for Computational Linguistics. doi: 10.18653/v1/2024.acl-long.37. URL
https://aclanthology.org/2024.acl-long.37/.
12

## Page 13

[46] N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao. Reflexion: Language agents
with verbal reinforcement learning.Advances in Neural Information Processing Systems, 36,
2023.
[47] Y . Song, D. Yin, X. Yue, J. Huang, S. Li, and B. Y . Lin. Trial and error: Exploration-based
trajectory optimization of LLM agents. In L.-W. Ku, A. Martins, and V . Srikumar, editors,
Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 7584–7600, Bangkok, Thailand, Aug. 2024. Association for
Computational Linguistics. doi: 10.18653/v1/2024.acl-long.409. URLhttps://aclantho
logy.org/2024.acl-long.409/.
[48] K. Sreedhar and L. Chilton. Simulating human strategic behavior: Comparing single and
multi-agent llms. 2024. URLhttps://arxiv.org/abs/2402.08189.
[49] T. R. Sumers, S. Yao, K. Narasimhan, and T. L. Griffiths. Cognitive architectures for language
agents, 2024. URLhttps://arxiv.org/abs/2309.02427.
[50] S. Triantafyllou, A. Sukovic, D. Mandal, and G. Radanovic. Agent-specific effects: A causal
effect propagation analysis in multi-agent mdps, 2024. URLhttps://arxiv.org/abs/23
10.11334.
[51] D. Vernon, C. von Hofsten, and L. Fadiga. Desiderata for developmental cognitive architec-
tures.Biologically Inspired Cognitive Architectures, 18:116–127, 2016.
[52] K. Wang, A. Variengien, A. Conmy, B. Shlegeris, and J. Steinhardt. Interpretability in the wild:
a circuit for indirect object identification in gpt-2 small, 2022. URLhttps://arxiv.org/
abs/2211.00593.
[53] X. Wang, B. Li, Y . Song, F. F. Xu, X. Tang, M. Zhuge, J. Pan, Y . Song, B. Li, J. Singh, H. H.
Tran, F. Li, R. Ma, M. Zheng, B. Qian, Y . Shao, N. Muennighoff, Y . Zhang, B. Hui, J. Lin,
R. Brennan, H. Peng, H. Ji, and G. Neubig. Openhands: An open platform for ai software
developers as generalist agents, 2025. URLhttps://arxiv.org/abs/2407.16741.
[54] Y . Wang, R. Xu, K. Zheng, T. Zhang, J. N. Kogundi, S. Hans, and V . Ustun. Gameplayqa:
A benchmarking framework for decision-dense pov-synced multi-video understanding of 3d
virtual agents, 2026. URLhttps://arxiv.org/abs/2603.24329.
[55] Q. Wu, G. Bansal, J. Zhang, Y . Wu, B. Li, E. Zhu, L. Jiang, X. Zhang, S. Zhang, J. Liu,
A. H. Awadallah, R. W. White, D. Burger, and C. Wang. Autogen: Enabling next-gen llm
applications via multi-agent conversation, 2023. URLhttps://arxiv.org/abs/2308.081
55.
[56] Y . Xiao, J. Liu, Y . Zheng, X. Xie, J. Hao, M. Li, R. Wang, F. Ni, Y . Li, J. Luo, S. Jiao,
and J. Peng. Cellagent: An llm-driven multi-agent framework for automated single-cell data
analysis, 2024. URLhttps://arxiv.org/abs/2407.09811.
[57] Y .-A. Xiao, P. Gao, C. Peng, and Y . Xiong. Reducing cost of llm agents with trajectory reduc-
tion. 2026. doi: https://doi.org/10.1145/3797084. URLhttps://arxiv.org/abs/2509.2
3586.
[58] H. Yang, J. Liu, C. Huang, F. Wu, W. Lei, and S.-K. Ng. Metro: Towards strategy induction
from expert dialogue transcripts for non-collaborative dialogues, 2026. URLhttps://arxi
v.org/abs/2604.11427.
[59] J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, and O. Press. Swe-
agent: Agent-computer interfaces enable automated software engineering.Advances in Neural
Information Processing Systems, 37:50528–50652, 2024.
[60] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y . Cao. React: Synergizing
reasoning and acting in language models.arXiv preprint arXiv:2210.03629, 2023.
[61] S. Yi, J. Nguyen, H. Xu, T. Lim, A. Well, M. Markey, and Y . Ding. Auto-ta: Towards scalable
automated thematic analysis (ta) via multi-agent large language models with reinforcement
learning, 2025. URLhttps://arxiv.org/abs/2506.23998.
13

## Page 14

[62] A. Zhou, K. Yan, M. Shlapentokh-Rothman, H. Wang, and Y .-X. Wang. Language agent
tree search unifies reasoning acting and planning in language models. 2024. URLhttps:
//arxiv.org/abs/2310.04406.
[63] S. Zhou, F. F. Xu, H. Zhu, X. Zhou, R. Lo, A. Sridhar, X. Cheng, T. Ou, Y . Bisk, D. Fried,
et al. Webarena: A realistic web environment for building autonomous agents.arXiv preprint
arXiv:2307.13854, 2023.
14

## Page 15

Contents
A Limitations 16
B Broader Impacts 16
C Corpus and Annotation Details 16
D Discovery Qualitative Analyst 17
E Codebook Evolution 18
F Large-Scale Analysis of Agent Behavioral Descriptions 19
G Extension Protocol 21
H Automated Trace Analysis Tool 21
I Action Space Codebook 21
I.1 GROUNDINGSub-actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
I.2 PLANNINGSub-actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
I.3 REASONINGSub-actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
I.4 RETRIEVALSub-actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
I.5 MEMORYSub-actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
I.6 EVALUATINGSub-actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
I.7 DECIDINGSub-actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
I.8 EXECUTINGSub-actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
I.9 REFLECTINGSub-actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
I.10 LEARNINGSub-actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
15

## Page 16

A Limitations
Act·ONOMYhas several scope-bound limitations. First, our scope is manually constructed on 565
behavioral sentences extracted from 35 peer-reviewed agent papers (Appendix §1), and the prelim-
inary coding saturation we report (§3) is bounded by this corpus. We tested the generalizability of
Act·ONOMYon a large-scale dataset in §4 and §F: action and sub-action levels remain relatively sta-
ble, while new behavioral descriptions continue to emerge at the leaf level, which our extension pro-
tocol is designed to absorb. Second, because the codebook is built from sentences researcherswrote
abouttheir agents, it captures narratable, architectural-aspirational moves (“the agent reflects”) and
may under-represent silent low-level behaviors surfaced only by bottom-up trajectory analysis; we
leave this direction to future work. Third, we rely on Claude Opus 4.7 as the primary annotator in
LLM-powered-Discovery-Qualitative-Analyst; cross-model annotation studies (GPT-class,
Qwen, open-weight) are an important next step. Finally, our two case studies use a small number
of trajectories and demonstrate the kinds of analyses Act·ONOMYenables; larger behavioral surveys
using the releasedAutomated-Trace-Analysis-Toolare deferred to follow-up work.
B Broader Impacts
Act·ONOMYis a descriptive tool meant to make agent runtime behavior easier to describe and
compare for researchers, designers, and end users, and to give failure-mode taxonomies such as
MAST [6] a vocabulary for what the agent was doing before it failed. We flag four considerations
for responsible use. First, a Act·ONOMYprofile is an interpretation of what an agent did on the
trajectories we can observe, not a ground-truth account of what agents actually do; when deciding
whether to ship an agent, profiles should be read alongside the raw trajectories they summarize, with
the trajectories themselves remaining the primary evidence. Second, a widely adopted vocabulary
can in turn constrain how researchers describe behaviors that do not yet fit existing codes, so our ex-
tension protocol (Section G) and versioned releases keep the codebook open to revision, and down-
stream users should contribute new codes rather than force-fit observations into the nearest existing
label. Third, the construction corpus is drawn from NeurIPS, ICML, ICLR, and the ACL Anthology
(2024–2026), which skew toward English-language work from well-resourced labs, so behaviors
documented in regional venues, industry reports, or non-English literature are under-represented
and should be folded in as the codebook is reused. Finally,Automated-Trace-Analysis-Tool
relies on a commercial LLM API, adding marginal cost per annotation, and as commercial mod-
els are retired results from earlier model versions also become harder to reproduce; the taxon-
omy and extension protocol are nevertheless model-agnostic, and we release the prompt template
and codebook so any sufficiently capable LLM, including open-weight models, can implement
Automated-Trace-Analysis-Tool.
C Corpus and Annotation Details
Corpus collection. Paper selection.We assembled a corpus of35 peer-reviewed agent pa-
pers(P1–P35) from NeurIPS, ICML, ICLR, and the ACL Anthology (2024–2026), filtered by the
keywordsbehavior analysisoranalysisin the title or abstract; workshop papers were excluded.
The corpus deliberately spans diverse agent-research subdomains (LLM-agent benchmarks and
evaluation, multi-agent systems, embodied agents, reinforcement-learning theory, and a range of
domain applications such as software engineering, medical AI, and hardware design). We split
the 35 papers in advance into a 28-paper construction set and a 7-paper held-out set, with the
latter reserved for the reliability check (Section 3).Behavior-description extraction.Using
theLLM-powered-Discovery-Qualitative-Analyst(Appendix D, role i), we extracted780
behavior-description sentencesfrom the 35 papers. After author review of the extractions against
their source papers, 8 construction papers were judged off-topic for an agent-behavior taxonomy
(position pieces, theory papers without runtime behavior, or systems whose described actions do
not generalize) and their 99 sentences were removed. The remaining 565 sentences from the 20
incorporated construction papers were used to construct Act·ONOMY; the 116 sentences from the 7
held-out papers were reserved for the reliability check (Table 1). The final corpus is released in our
GitHub repository.
16

## Page 17

Table 1: How the 35 papers split into construction, off-topic, and held-out subsets. TheRolecolumn
describes how each subset is used.
Subset Papers Sentences Role
Construction (incorporated) 20 565 Six co-authors reviewed all 565 sentences; 120 appear as
quoted evidence in the released V4.2 codebook.
Construction (not incorporated) 8 99 All 99 sentences reviewed, but the papers were judged off-
topic for an agent-behavior taxonomy, so their sentences were
dropped.
Held-out (reliability check) 7 116 Reserved for Phase 2 reliability checks (Section 3): 50 sen-
tences sampled for the human–human and human–LLMκ
checks. Not used during construction.
Total 35 780
Annotation process.We assigned codes to the 565 behavioral descriptions in two steps: an
LLM proposed a candidate code for each description, and six co-authors reviewed every (sen-
tence, suggested-code) pair.Step 1:LLM-powered-Discovery-Qualitative-Analystsuggests
a code.For each behavioral description, theLLM-powered-Discovery-Qualitative-Analyst
(Appendix D, role ii) compared the description against the current codebook and either matched it to
an existing code or proposed a new candidate, in each case with a verbatim quote as evidence.Step
2: co-authors review each pair.Six co-authors split the corpus into batches of 4–5 papers each,
with one as the main reviewer. For every (sentence, suggested-code) pair, the reviewer first checked
whether the sentence was in scope, verified the quoted span against the source paper, and thenac-
cepted,renamed,proposeda new code, ordiscardedthe sentence. All six co-authors contributed
at least 6 hours; the primary and secondary annotators spent over 20 and 10 hours respectively.
Per-coauthor annotation instructions are released in our GitHub repository.
D Discovery Qualitative Analyst
We developed theLLM-powered-Discovery-Qualitative-Analystto handle parts of the
pipeline that are too tedious to do by hand. It has two main operations: identifying behavioral
descriptions in a corpus paper, and, given a description, either matching it to an existing code in the
current codebook or proposing a new one. We apply it at four points throughout this work:
1.Behavior extraction.Given a corpus paper, the
LLM-powered-Discovery-Qualitative-Analystextracts candidate behavior-
description sentences, that is, sentences in which the authors describe what their agent
does at runtime.
2.Code suggestion (V2→V3).Given the current codebook and a behavior description, the
LLM-powered-Discovery-Qualitative-Analystproposes either an existing code that
fits or a new candidate code; the six co-authors then decide whether to accept it.
3.Code assignment for inter-rater reliability.Given Codebook V4 and a behavior description
from the held-out set, theLLM-powered-Discovery-Qualitative-Analystassigns a
code to the behavior description, used to compute the human–LLM Cohen’sκ. A high IRR
means an LLM can apply the codebook as reliably as a human annotator.
4.Saturation probe.Once role (iii) confirms a sufficiently high IRR, we apply the
LLM-powered-Discovery-Qualitative-Analystto a held-out paper set and test
whether there are new codes that emerge (§3).
All four share the same model and pipeline, differing only in the instruction block, the artifacts
loaded into context (codebook version, behavior description), and the output format. We implement
theLLM-powered-Discovery-Qualitative-Analystas a Claude Code Skill and release it in
our GitHub repository.
17

## Page 18

Table 2: The 20 incorporated construction papers, ordered by paper ID.Sen-
tencesis the per-paper count of behavior-description sentences extracted by the
LLM-powered-Discovery-Qualitative-Analystand kept after author review (565 in to-
tal).
ID Cite Domain Title Sentences
P1 [56] LLM Agents CellAgent: LLM-Driven Multi-Agent Framework for
Natural Language-Based Single-Cell Analysis
30
P2 [38] LLM Agents (Benchmark) A Benchmark for Deep Information Synthesis 26
P3 [9] LLM Agents (Evaluation) Talk, Evaluate, Diagnose: User-aware Agent Evaluation
with Automated Error Analysis
28
P4 [20] Medical AI MedVR: Annotation-Free Medical Visual Reasoning via
Agentic Reinforcement Learning
28
P8 [58] LLM Agents (Dialogue) METRO: Towards Strategy Induction from Expert Dia-
logue Transcripts for Non-collaborative Dialogues
28
P9 [17] LLM Agents (Benchmark) REPRO-Bench: Can Agentic AI Systems Assess the Re-
producibility of Social Science Research?
28
P11 [26] Speech Interaction Human or Machine? A Preliminary Turing Test for
Speech-to-Speech Interaction
28
P13 [40] LLM Behavior (Benchmark) ImplicitMemBench: Measuring Unconscious Behav-
ioral Adaptation in Large Language Models
27
P14 [54] Multimodal Video Understanding GameplayQA: A Benchmarking Framework for
Decision-Dense POV-Synced Multi-Video Understand-
ing of 3D Virtual Agents
28
P16 [24] LLM Agents (Benchmark) AgencyBench: Benchmarking the Frontiers of Au-
tonomous Agents in 1M-Token Real-World Contexts
30
P17 [34] Position Paper Position: Scaling LLM Agents Requires Asymptotic
Analysis with LLM Primitives
30
P21 [27] Multi-Agent Social Simulation My Words Imply Your Opinion: Reader Agent-Based
Propagation Enhancement for Personalized Implicit
Emotion Analysis
25
P22 [29] LLM Agents (Safety) Tell Me What You Don’t Know: Enhancing Refusal
Capabilities of Role-Playing Agents via Representation
Space Analysis and Editing
28
P27 [61] Multi-Agent Systems Auto-TA: Towards Scalable Automated Thematic Anal-
ysis via Multi-Agent Large Language Models with Re-
inforcement Learning
26
P28 [28] Software Engineering E2Edev: Benchmarking Large Language Models in
End-to-End Software Development Task
35
P29 [25] Hardware Design / EDA ChatHLS: Towards Systematic Design Automation and
Optimization for High-Level Synthesis
30
P31 [44] Reinforcement Learning Theory Geometric Active Exploration in Markov Decision Pro-
cesses: the Benefit of Abstraction
27
P32 [18] LLM Agents (Benchmark) InfiAgent-DABench: Evaluating Agents on Data Anal-
ysis Tasks
28
P33 [50] Reinforcement Learning Theory Agent-Specific Effects: A Causal Effect Propagation
Analysis in Multi-Agent MDPs
26
P34 [45] Embodied Agents OPEx: A Component-Wise Analysis of LLM-Centric
Agents in Embodied Instruction Following
29
Total 565
E Codebook Evolution
We summarize how the codebook evolved alongside the annotation process described in Section C.
After V3, no new top-level actions are added and later versions only restructure; after V4.1, no new
sub-actions are added and the leaf set stabilizes.
18

## Page 19

Table 3: Overview of how Act·ONOMYcodebook evolved across iterative annotation process.
Version Actions Sub-actions Leaf Categories Key change
V1 seed6 17 53 Bullet-list seed drawn from CoALA [49]; no Verb+Noun
normalization and no quoted evidence.
V2 normalize 6 6 35 Action labels normalized to Verb+Noun form with plain-
English explanations. Only a few sub-actions are pro-
posed.
V3 expand13 13 113 First corpus-anchored version: 664 behavior-
description sentences from 28 construction pa-
pers (Appendix C) were routed through the
LLM-powered-Discovery-Qualitative-Analyst
and reviewed by six co-authors, adding the first column
of paper-anchored quoted evidence. Seven new top-level
categories appear: PLANNING, REFLECTION, TOOL
USE, SYNTHESIS, EVALUATE, BOUNDARY-AWARE,
ROLECONDITIONING.
V4.1 restructure 11 60 130 Three-level tree (Action→Sub-action→Leaf Category)
with paper-anchored examples, with anUnclassifiedbin
for items pending placement.
V4.2 final⋆ 10 46 120 Final reorganization: theUnclassifiedbin is folded into
mainline categories; redundant leaves and actions are
merged or renamed; low-frequency codes are consoli-
dated or removed; GENERATINGbecomes a sub-action
under REASONING.
F Large-Scale Analysis of Agent Behavioral Descriptions
To test how Act·ONOMYgeneralizes beyond the 35-paper construction corpus, we applied it to a
much larger and noisier set of 211 papers and 3,455 behavioral descriptions. This appendix records
how that corpus was assembled.
Paper collection.We started from theawesome-language-agentsGitHub list, 6 a community-
maintained index of language-agent research that catalogues several hundred papers across safety,
evaluation, software engineering, computer use, web automation, and embodied tasks. We pulled
the list as of April 2026, downloaded every paper reachable from it, removed duplicates and broken
links, and kept entries whose title or abstract indicated that the paper analyzes agent runtime behavior
or reports per-step traces of an agent solving a task. This left 211 papers, intentionally broader and
noisier than our 35-paper construction corpus, so that the codebook is stress-tested on work it was
not built from.
Behavioral description extraction.We ranLLM-powered-Discovery-Qualitative-Analyst
(Appendix D, role i) once per paper, keeping only its verbatim-quote hallucination guard and skip-
ping the per-sentence author review used in the construction run. This produced 3,455 behavioral
descriptions, roughly 16 per paper on average.
Codebook annotation.For each of the 3,455 sentences,
LLM-powered-Discovery-Qualitative-Analyst(Appendix D, role ii) suggested an Ac-
tion, Sub-action, and Leaf-category label, and proposed a new code whenever no existing code fit.
The resulting label distributions feed the figures below and complement the co-occurrence summary
in Figure 4.
6github.com/ysymyth/awesome-language-agents
19

## Page 20

GroundingReasoningReflectionMemoryPlanningEvaluateLearningDecidingRetrievalExecuting
0%
10%
20%
30%% of Sentences
21.0%20.2%
10.8%10.4%10.2%10.1%
6.2% 5.1% 4.1%
1.8%
(a) Action
Eval. w/o Ground Truth
ContextualizingInteract w/ AgentsReflect on ErrorsFormulate Plan
Store Info.Generating
Interact w/ Env.
Augment w/ Ext. Comp.
Retrieve
0%
2%
4%
6%
8%
10%% of Sentences
8.0% 7.8%
6.8%
6.2%
5.7%
5.1% 5.0% 4.9%
4.2% 4.1%
(b) Top-10 Subaction
Package Prior Reasoning
Self-Correct Step
Issue Oper. Commands
Gen. Struct. ArtifactsDecide by MemoryStore in LT Memory
Self-reflect
Formulate Hi-Level Plan
Plan Func./Tool Use
Invoke Spec. Comp. Tool
0%
2%
4%
6%
8%% of Sentences
5.9%
4.4%
3.7% 3.7% 3.4%
2.8% 2.8% 2.7% 2.6% 2.6%
(c) Top-10 Leaf Cat.
(a) Frequency of each code across the 3,455 sentences, shown at the Action, Sub-action, and Leaf levels (top-10 for Sub-action and
Leaf).
GroundingReasoningReflectionMemoryPlanningEvaluateLearningDecidingRetrievalExecuting
Grounding
Reasoning
Reflection
Memory
Planning
Evaluate
Learning
Deciding
Retrieval
Executing
138
101 154
55 75 87
51 67 37 75
74 87 52 45 101
66 87 55 39 57 100
43 55 39 34 35 39 72
59 65 37 33 45 43 27 79
46 42 20 32 37 26 16 19 56
22 28 15 15 18 16 7 12 12 32
(a) Action
Eval. w/o Ground Truth
ContextualizingInteract w/ AgentsReflect on ErrorsFormulate Plan
Store Info.Generating
Interact w/ Env.
Augment w/ Ext. Comp.
Retrieve
Eval. w/o Ground Truth
Contextualizing
Interact w/ Agents
Reflect on Errors
Formulate Plan
Store Info.
Generating
Interact w/ Env.
Augment w/ Ext. Comp.
Retrieve
83
50 110
31 41 70
40 45 19 67
33 54 29 28 74
23 38 24 25 25 58
39 42 29 31 30 19 66
18 37 20 15 26 19 14 55
29 41 28 21 33 20 23 23 62
19 34 23 16 30 24 21 20 23 56
(b) Top-10 Subaction
Package Prior Reasoning
Self-Correct Step
Issue Oper. Commands
Gen. Struct. ArtifactsDecide by MemoryStore in LT Memory
Self-reflect
Formulate Hi-Level Plan
Plan Func./Tool Use
Invoke Spec. Comp. Tool
Package Prior Reasoning
Self-Correct Step
Issue Oper. Commands
Gen. Struct. Artifacts
Decide by Memory
Store in LT Memory
Self-reflect
Formulate Hi-Level Plan
Plan Func./Tool Use
Invoke Spec. Comp. Tool
92
36 58
30 8 50
24 23 10 51
35 17 18 15 57
25 16 9 8 14 42
23 24 10 9 10 10 38
27 12 11 9 10 8 13 40
22 13 16 13 11 7 9 10 39
27 12 15 13 15 14 8 13 15 45
(c) Top-10 Leaf Cat.
20
40
60
80
100
120
140
# Papers
(b) Per-paper co-occurrence of codes at the Action, Sub-action, and Leaf levels; each cell counts how many of the 211 papers contain
at least one sentence labeled with both codes.
Figure 8: Large-scale distribution and co-occurrence of Act·ONOMYcodes on 3,455 behavioral
sentences extracted from 211 agent papers.
20

## Page 21

G Extension Protocol
Act·ONOMYis meant to be a single shared codebook that grows as new agent designs appear, without
losing comparability across papers that have already used it. As reported in Section 3, the action and
sub-action levels are relatively stable, with new additions occurring primarily at the leaf level. We
support extension in two stages: theAutomated-Codebook-Extension-Toollets a downstream
user grow their own copy of the codebook locally, and a public submission channel folds general-
interest codes back into the shared release.
Local extension.When a user downloads Act·ONOMY, they receive the current released codebook
as their starting point. As they analyze new trajectories,Automated-Codebook-Extension-Tool
compares each observed behavior against the codebook: if an existing code fits, it assigns the
code; if no existing code fits, it proposes a new leaf (or, more rarely, a new sub-action or
top-level category) along with the position where the code should sit. The user accepts the
suggestion to grow their local copy without blocking on the public codebook. We release
Automated-Codebook-Extension-Toolas a Claude Code Skill in our open repository; any suf-
ficiently capable LLM backend can serve as a drop-in replacement.
Public submission.If a user judges a locally added code to be of general interest, they submit it
through a GitHub issue or pull request in the same repository. We review submissions and incorpo-
rate accepted ones into the next versioned release.
H Automated Trace Analysis Tool
Automated-Trace-Analysis-Tool(introduced in Section 4) takes a raw agent trajectory and, for
each turn, assigns Action, Sub-action, and Leaf-category labels to its thought and action compo-
nents, together with the verbatim quote behind every label. Figure 9 shows the rendered HTML
report: the overall action distribution alongside a per-label quote panel.
I Action Space Codebook
We list all codes in the Act·ONOMYaction space.
21

## Page 22

Figure 9: Interface ofAutomated-Trace-Analysis-Tool.
22

## Page 23

I.1 GROUNDINGSub-actions
Interact with users.
Specialization Example & Quote
Accept instructions from hu-
mans
Receive a task or command from a human user (e.g., “book
me a flight” or “translate this paragraph”); “agent receives task
queries and deliverables, completing tasks through multi-turn
interactions” (P16); “demonstrate clear intent understanding,
partial progress” (P5).
Ask for clarification from peo-
ple
Proactively ask the human when the request is unclear (e.g.,
“Which file did you mean?”).
Communicate task outcome in
natural language
Agent informs the user of the result, e.g., “Buy a nice rich
navy bathing dress” (P3); WiFi-off notification example (P3).
Communicate via visualization “CellAgent generated differential expression and marker gene
visualizations, enabling intuitive interpretation of cluster iden-
tities” (P1).
Communicate via structured
format
“generate outputs in a JSON format (or lists of JSON objects)”
(P2).
Communicate refusal/inability “appropriately reject queries that exceed their knowledge
boundaries or conflict with their role settings” (P22); “recog-
nize and refuse queries that conflict with their role knowledge”
(P22); “providing clear refusal responses with appropriate ex-
planations” (P22).
Express tone to user “models exhibit a strong default tendency to excessively af-
firm, apologize, and express gratitude” (P11).
Disclose self-information to
user
“identity disclosure, S2S systems often proactively mention
that they are intelligent assistants” (P11).
Interact with physical environments.
Specialization Example & Quote
Perceive physical environment Convert images/sensor/audio readings to text via VLMs so a
text-based LLM can consume them; “Explore skill enhances
the LLM-based executor’s ability to guide the agent in room
exploration by sampling navigation goals from traversable ar-
eas” (P33); “semantic mapping module receives egocentric vi-
sual observations. . . processed into a depth map and instance
segmentation using a UNet and a MaskRCNN” (P34).
Affect physical environments Send language commands to a robot arm to move things in the
real world; “the action Play is utilized to interact with the en-
vironment or request re-planning of the current plan S” (P34).
Interact with digital environments.
Specialization Example & Quote
Navigate digital interfaces Browse websites, scroll pages, navigate menus, move within
apps; “navigate multiple websites, extract information from
both structured and unstructured sources” (P2).
Modify digital objects Annotate UI components by addingdata-testidat-
tributes: “annotate interactive components(file,
strategy=‘add data-testid’)” (P28).
Issue operational commands Invoke a structured API or data endpoint: “Game Control:
get game state,press buttons, andnavigate tofor di-
rect game control” (P25).
23

## Page 24

Interact with other agents.
Specialization Example & Quote
Monitor peer agent’s state or
decision
Observe another agent’s chosen action before making one’s
own decision—a prerequisite for oversight, override, or trust-
based deference in multi-agent systems: “observes bothS 0
andA 0, and decides whether to override the AI’s treatment or
not” (P33).
Receive feedback from peer
agent
Evaluator provides natural-language feedback (P1).
Send message to peer agent “agent engages in multi-turn interactions. . . to generate deliv-
erables” (P16).
Recommend action to peer
agent
Communicate a proposed action to a peer agent for their con-
sideration, knowing the peer may accept or override it—agent-
to-agent advisory communication: “the AI recommends one
of eight possible treatments, which is then reviewed and po-
tentially overridden by the clinician” (P33).
Override peer agent’s decision Replace another agent’s selected action with one’s own
decision—the active side of human-in-the-loop oversight or
hierarchical agent control: “If the clinician overrides the AI,
the patient outcomeYis determined byS 0 and the alternative
treatmentH 0 suggested by the clinician” (P33).
Dispatch task to sub-agent “A central orchestrator maintains a high-level route plan while
dynamically dispatching sub-agents based on game context”
(P25).
Argue or debate with peer agent Multi-agent argumentation toward a better answer; have mul-
tiple agents argue different sides to reach a better answer.
Augment with external computation.
Specialization Example & Quote
Execute code Test Runner detects logic inconsistencies (P28); “Test Runner
executes the script to detect logical inconsistencies or failed
assertions” (P28).
Invoke specialized computation
tool
Use calculator/heavy-compute tools to handle math beyond
the LLM;run shell commandtool (425 and 362 invoca-
tions, respectively) (P16); “necessitates over 90 precise tool
calls, significantly raising the bar” (P16); “deliverables are
synced to a Docker-based remote sandbox. . . emulates hu-
man computer operations” (P16).
Invoke visual inspection tool Zoom-in tool for region-of-interest (P4): “proactively invokes
the Zoom-in tool for a targeted examination of the specific
region of interest” (P4).
I.2 PLANNINGSub-actions
Decompose task.
24

## Page 25

Specialization Example & Quote
Decompose into subtasks “LLM-based planner to decompose the specified language in-
structionLinto a sequence of subtasksS= [S 0, S1, . . . , Sn]”
(P34); “Decomposing hard problems into subproblems often
makes them easier and more efficient to solve” (P17); “De-
composes complex user requests into manageable subtasks,
an Executor that carries out the analysis by generating and
running code, and an Evaluator that assesses the quality of
the results” (P1); “formulate plans, decompose problems into
sub-steps” (P2);todo writetool (15 invocations by GPT-
5.2) (P16).
Decompose into subgoals with
success conditions
“LLM decomposes the task into a sequence of subgoals, each
paired with an executable success-condition function” (P25).
Decompose by role specializa-
tion
“splitting the instruction-following challenge into distinct rea-
soning and grounding roles handled by a reasoner agent and
an actor agent” (P34); “Specialists each solve a distinct task
type, receiving only the relevant portion of the input” (P17).
Formulate a workflow or plan.
Specialization Example & Quote
Formulate a high-level plan “METRO starts with the identification of the strategic action
ai for every expert utteranceu i in transcriptD” (P10); “sum-
marizing it into a high-level planning directive that empha-
sizes cumulative temporal effects” (P8).
Formulate an analysis workflow “the Planner accurately interprets user intent and formulates a
comprehensive analysis workflow” (P1).
Plan navigation through envi-
ronment
“planning to navigate the web; tasks require navigation
through an average of 4.2 web pages” (P2).
Plan function or tool use “I can use the pandas methodcorr()to calculate the Pearson
correlation coefficient” (P32).
Plan code or artifact structure “Planning: HTML Structure, CSS Styling, JavaScript Func-
tionality” (P28).
Formulate plan from template “HLSTuner formulates a detailed plan that specifies: (1) the
combination of HLS directives, (2) target code segments, and
(3) the insertion actions” (P29).
Select strategy.
Specialization Example & Quote
Select among candidate strate-
gies
“selects effective HLS directive combination strategies and in-
serts directives within the specific structure (e.g., loops and
arrays)” (P29).
Switch to fallback strategy “incorporating a dummy score prediction as a fallback mech-
anism” (P11).
Modify plan.
Specialization Example & Quote
Replan dynamically based on
feedback
“RequireReplan provides the LLM-based executor with the
capability to dynamically adjust the plan” (P34).
Refine requirements “Refine requirement based on validated test cases to ensure
alignment” (P28).
25

## Page 26

I.3 REASONINGSub-actions
Generating.
Specialization Example & Quote
Generate candidate options Brainstorm one or more possible next moves; “Running mul-
tiple candidate pipelines for each analysis step” (P1); “gener-
ates solutions based on analogies to unrelated projects, which
resemble few-shot prompting” (P28); “Fork the current gen-
erative state and generate a new parallel trajectory from this
point of high uncertainty” (P4); “the LLM reinterprets the ac-
tions from breadth logic. . . summarizing them into a concise
next-step strategy” (P8).
Generate structured artifacts “Each agent then emits a set of initial codes; cluster seman-
tically similar codes and generate preliminary themes” (P27);
“automatically generates candidate user-facing requirements”
(P28); “Create JavaScript functionality handling empty dis-
play and consecutive operator clicks” (P28); “break down
the given character description into multiple atomic pieces of
knowledge” (P22).
Generate evaluations “LLM Group for multifaceted evaluation generates diverse de-
bugging instructions” (P29); “For every binary scorez(q)
i,j from
the judge, there is a corresponding explanatione (q)
i,j ” (P3).
Analysing.
Specialization Example & Quote
Analyse artifact structure and
behavior
“Analyze frontend framework and interactive components”
(P28); “analyzes the project’s core functionalities and their in-
teractions with UI elements by reading the source code” (P28).
Detect patterns or trends in
data
“Identifying patterns, directions, or changes in data over time
or across contexts” (P2); “Measuring relationships or associa-
tions between two or more variables” (P2).
Interpret meaning of artifacts “logical reasoning to interpret papers and code; mathematical
reasoning to modify and run code; causal reasoning to infer
scientific insights from results” (P11).
Classify inputs into categories “delegator can determine which of thektasks the input string
belongs to by observing only a constant number of metadata
tokens” (P17).
Explaining.
Specialization Example & Quote
Explain reasoning or outcomes “Explain the failure from a user requirement perspective”
(P16).
Summarizing/Distilling.
Specialization Example & Quote
Summarize recent observations
and trajectories
Condense recent observations and trajectories into key take-
aways.
Inferring.
26

## Page 27

Specialization Example & Quote
Infer hidden state from observ-
able evidence
“intelligently infers hidden information through game me-
chanics: damage calculations reveal stat distributions, move
priority ordering constrains speed ranges” (P25).
Infer causal relationship “determine the most plausible event or factor accounting for
this variability” (P2).
Infer structure from indirect ev-
idence
“agents must infer the directory layout by inspecting package
structures and README files” (P11).
Infer errors “Mq has the capacity to identify exactly one bug at a time”
(P17); “The analysis LLM then examines the error causes and
provides debugging instructions” (P29).
Comparing & Ranking.
Specialization Example & Quote
Compare values across sources “Quantifying occurrences and comparing values across
sources or categories” (P2).
Rank items by criteria “Ordering items or facts based on specific criteria or impor-
tance” (P2).
Contextualizing.
Specialization Example & Quote
Package prior reasoning as
context for subsequent calls
Feed the reasoning so far as context to the next LLM call.
Construct structured context
object
“global interactive multi-behavior overlapping network is
constructed based on the simulated behaviors of reposting and
reposting with a comment, as well as following” (P21); “con-
struct prompt templates for creating reader agents based on
user attributesu a and user historical posts” (P21).
Configure agent persona or
role-conditioning
“I want you to play as{role}, imitating{role}’s personal-
ity and values” (P22); “maintain its role-playing ability even
when refusing to answer” (P22); “A pool ofk= 4role-
conditioned GPT-4o agents are each given the full interview
transcript as input” (P27); “others may retain role-specific per-
spectives to support diverse theme formulation” (P27).
Assign roles in a multi-agent
team
“specifying a scope, or role, for an agent allows it to be treated
as a computational object. . . map each one to an employee
in a human organization” (P17); “assembling a team of three
LLM roles—analyst, coder, and tester—responsible for anal-
ysis, coding, and testing” (P28); “assigns diverse roles to mul-
tiple agents to efficiently decompose complex tasks” (P28).
Combining & Synthesis.
Specialization Example & Quote
Combine information from mul-
tiple sources
“combine information from multiple sources. . . to produce
a coherent solution” (P2); “the final results from all subtasks
are synthesized to meet the user’s requirements” (P1); “Deter-
mining a representative value that summarises numerical data
collected from multiple sources” (P2).
Aggregate observations into a
structured representation
“supplementary semantic mapM ′
t, which aggregates the in-
formation fromM t over successive time steps. The intuition
resembles a form of majority voting” (P34); “aggregates pre-
diction results from multiple tools to generate the final cell
type labels” (P1).
27

## Page 28

Filtering.
Specialization Example & Quote
Filter information by threshold “Selecting relevant information based on criteria, quality, or
thresholds” (P2).
I.4 RETRIEVALSub-actions
Retrieve from skill library.
Specialization Example & Quote
Retrieve from skill library Grab a pre-built skill snippet (e.g., Minecraft “chop tree”)
from a library of ready-made code; find and load a ready-made
code snippet from a pre-built library.
Retrieve from local corpus.
Specialization Example & Quote
Retrieve from local corpus “diverse filetype reading; read between 1 to 15 docu-
ments and/or tables” (P2); “read the README file—Phase
1:read file(’reproduction package/readme.txt’)”
(P11).
Retrieve from external knowledge base.
Specialization Example & Quote
Retrieve from external knowl-
edge base
“LLM which generates buggy code by integrating retrieved er-
ror slices from BugRAG as context” (P29); “queries BugRAG
to check for existing entries” (P29); “Recall three (03) relevant
and distinct problems (different from the user task)” (P28).
Retrieve from open web.
Specialization Example & Quote
Retrieve from open web “high reliance on web search to offload knowledge retrieval to
external sources” (P16).
Retrieve relevant context.
Specialization Example & Quote
Retrieve relevant context “LLM leverages retrieved HLS-related context to transform
input C algorithms or natural language descriptions” (P29).
I.5 MEMORYSub-actions
Store information.
Specialization Example & Quote
Store information in working
memory
A scratchpad / quick-access buffer that holds recent inputs and
intermediate results.
Store episodic trajectories Record full action sequences (start to finish) for later training
or review.
28

## Page 29

Specialization (cont.) Example & Quote
Store knowledge in semantic
memory
Save general world facts not tied to any specific event.
Store experiences in episodic
memory
Save past events as personal-diary-like episodes (e.g., which
game was won, which plan failed).
Store information in long-term
memory
Persist state and key information in external storage; “Gemini-
3-Pro. . .initialize memory bank(7 times); Gemini-3-
Pro. . .update memory bank(22 times). . . attempts to per-
sist state and key information externally” (P16).
Maintain curriculum library Keep a syllabus of mastered and upcoming skills, arranged by
difficulty, so the agent learns in a sensible order.
Update information.
Specialization Example & Quote
Update memory Update experiences—refinement of memories (represented in
text) as the system encounters new scenarios.
Discard information.
Specialization Example & Quote
Discard information from work-
ing memory
“the local memory is discarded upon successful completion of
the subtask” (P1).
Discard redundant game state,
keep summaries
“automatic context compaction to manage thousands of rea-
soning steps, preserving only LLM responses and action sum-
maries while discarding redundant game state” (P25).
Consolidate memory.
Specialization Example & Quote
Consolidate working memory
into long-term memory
Discard-after-use strategy that retains only the clear and suc-
cessful analysis path in global memory, preventing interfer-
ence from intermediate trial-and-error history (P1).
Compact context window “automatic context compaction to manage the thousands of
reasoning steps required, preserving only LLM responses and
action summaries while discarding redundant game state”
(P25).
Read memory.
Specialization Example & Quote
Read from working memory Check the scratchpad: grab stored intermediate results and
state; “IMPLICITMEMBENCH reframes evaluation from
‘what agents recall’ to ‘what they automatically enact’ ” (P12).
Read from long-term memory Importance-weighted retrieval of discoveries (P25): “Persis-
tent memory system storing discoveries (locations, NPCs,
items, strategies) with importance-weighted retrieval” (P25).
I.6 EVALUATINGSub-actions
Evaluating with gold.
29

## Page 30

Specialization Example & Quote
Compare against gold reference “we prompt LLM to review the correct HLS-C code, pairing
buggy code segments with corresponding error messages to
construct debugging CoT” (P29); “HLSFixer retests the cor-
rected HLS design against the golden results to ensure seman-
tic equivalence” (P29).
Score on gold criteria “The Gold Checker evaluates each annotation on three binary
criteria: equivalence, completeness, and correctness, where a
score of 1 indicates the criterion is met” (P28).
Evaluating with goals/requirements/constraints.
Specialization Example & Quote
Goal-completion check “Independently checks whether objectives are truly complete,
preventing the orchestrator from advancing when the main
agent incorrectly believes a task is finished” (P25).
Requirement-satisfaction check “the final results from all subtasks are synthesized to meet the
user’s requirements” (P1).
Constraint / budget check “HLSTuner enables QoR-aware reasoning to align optimiza-
tion goals with hardware constraints” (P29); “if hardware uti-
lization exceeds the budget” (P29).
Domain-rule / best-practice
check
“codified best-practices, such as the standard order of opera-
tions (e.g., quality control must precede normalization)” (P1);
“Agents share project context to ensure: Cross-file consis-
tency; Non-conflicting test-ids” (P28); “Detect logical errors,
missing functionalities, or violations of best practices” (P16).
Evaluating without ground truth.
Specialization Example & Quote
Score on quality dimensions “we use GPT-4o as the default evaluator, each dimension
scored on a scale of 0 to 2” (P22); “map the agent’s deliv-
erables to a score ranging from 0 to 10” (P16); “Evaluation
Scores: Obtains (t) = (C, D, T)on the trustworthiness di-
mensions” (P27); “the scoring agent (functioning as the judge)
based on clarity, logical soundness, alignment with error mes-
sages, this agent selects the optimal suggestion” (P29).
Check rubric compliance “Verify the implementation of every item listed in{Rubrics}”
(P16); “list exactly which rubrics were not met” (P16).
Evaluate visual/behavioral cor-
rectness
“Evaluates dynamic behavior and visual correctness based
on screenshots” (P16); “Analyze{Visual Assets}for UI el-
ements, layout consistency, and text rendering” (P16).
Evaluate internal consistency “task an evaluator agent with determining whether each theme
is consistent with its supporting quotes” (P27); “In Phase 2,
they inspect the provided code for potential inconsistencies;
generating a reproducibility score on a scale from 1 to 4”
(P11).
Evaluate intermediate results “agents with domain expertise verify intermediate results and
reduce errors” (P28).
Provide qualitative judgement “Upon successful generation of a result, the Evaluator agent,
ALLMe assesses the outcome and provides natural language
feedback if it deems revisions are necessary” (P1).
30

## Page 31

Specialization (cont.) Example & Quote
Simulate counterfactual out-
comes
Mentally simulate an alternative scenario—either before act-
ing (“if I do X, what happens?”) or post-hoc (“what would
have happened if action X had been different?”)—including
counterfactual trajectory generation for causal analysis: “ana-
lyzing this effect necessitates counterfactual reasoning across
three distinct scenarios” (P33).
Validate predicted issues “The agent assesses the contextual applicability of potential
bugs, reducing the probability that the LLM forcibly generates
trivial results” (P29).
I.7 DECIDINGSub-actions
Make a decision.
Specialization Example & Quote
Make a decision according to
memory
“The agent conditions its decisions onI, the current observa-
tions t, and a history buffer ofnpast state–action pairs” (P5).
Pick scores.
Specialization Example & Quote
Select action by score argmax = highest score; softmax = probabilistic sample; ma-
jority vote across evaluators.
Decide accept or not.
Specialization Example & Quote
Decline out-of-scope queries “appropriately reject queries that exceed their knowledge
boundaries or conflict with their role settings” (P22).
Decide under uncertainty.
Specialization Example & Quote
Fork trajectory at uncertainty “Fork the current generative state and generate a new parallel
trajectory from this point of high uncertainty” (P4).
I.8 EXECUTINGSub-actions
Executing plan.
Specialization Example & Quote
Execute strategy “an insertion agent executes this plan for HLS-C optimiza-
tion” (P29).
Executing debug.
Specialization Example & Quote
Adopt debugging instructions “Operating under strict instruction adherence, this agent
adopts the instructions to implement debugging” (P29).
Rewrite code after bug fix “debugging specialist rewrites the entire code every time it
fixes a bug” (P17).
31

## Page 32

Terminating.
Specialization Example & Quote
Provide final answer “Final Answer: The average number of lines per scene in the
ep 7.csvdataset is approximately 6.02” (P32); “produces
a final answer and terminates the rollout; enclose it within
<answer></answer>tags” (P4).
Generate refusal “providing clear refusal responses with appropriate explana-
tions” (P22).
I.9 REFLECTINGSub-actions
Reflect on errors and failures.
Specialization Example & Quote
Diagnose failure against
ground truth
“Analyzes stuck states by comparing current situation against
ground truth sources (porymap data, knowledge base) to diag-
nose navigation failures” (P25).
Inspect error pattern “an inspection agent examines the erroneous code and error
messages parsed from the HLS tool test results” (P29).
Analyze log to formulate fix in-
structions
Reasoning-to-instruction on HLS log (P29): “an analysis
agent adopts a reasoning-to-instruction method, analyzing the
HLS log to formulate error modification actions” (P29); “This
model formulates explicit modification instructions with de-
tailed analysis” (P29); “Provide explicit instructions on what
must be rectified in the next iteration” (P16).
Reflect on failed episodes for
prior knowledge
“RequireReplan. . . dynamically adjust the plan, improv-
ing the robustness to exceptions” (P26); “the grounded prior
knowledge prevents the agents from repetitive errors and fa-
cilitates grounded exception handling” (P34); “This allows the
agent to learn from mistakes in realtime and avoid repeating
errors before the local memory is discarded” (P1).
Self-correct step implementa-
tion
“Modify step implementation based on error message” (P28);
“In case of an execution errorE(c i), the Executor au-
tonomously performs self-correction to produce a valid code
version” (P1); “When the initial attempt fails. . . HLSTuner
activates an iterative refinement incorporating current direc-
tives and the resulting QoR” (P29).
Reflect on self-outcomes.
Specialization Example & Quote
Self-reflect “The results of the execution are fed back, enabling GPT-4
to refine its responses and propose further iterations” (P32);
“This iterative cycle continues until GPT-4 determines that
the accumulated information suffices to conclusively answer
the problem” (P32); “This self-reflective optimization loop it-
erates to enhance precision, and the final results from all sub-
tasks are synthesized” (P1); “the optimization process runs
three iterations, each invoking a different algorithm” (P1).
Reflect on proposed fix “reflects on the code after assuming the fix to ensure the mod-
ification is reasonable” (P29).
Pre-action self-check “These steps are labeled as reflective, indicating the model is
engaging in self-monitoring or explicit reasoning before issu-
ing commands” (P1).
32

## Page 33

Specialization (cont.) Example & Quote
Refine strategy iteratively Iterative refinement using current QoR (P29): “When the ini-
tial attempt fails. . . HLSTuner activates an iterative refine-
ment incorporating current directives and the resulting QoR”
(P29).
Reflect on external feedback.
Specialization Example & Quote
Receive and integrate external
feedback
“the Evaluator agent ALLMe assesses the outcome and pro-
vides natural language feedback if it deems revisions are nec-
essary” (P1); “feedback from the feedback agent is used to
iteratively refine and improve the generated themes” (P27);
“leverage feedback to markedly improve performance. . .
feedback-driven self-correction” (P16); “The Evaluator drives
a self-reflective optimization mechanism, which leverages au-
tomated evaluation methods for various analysis tasks to iter-
atively refine outcomes, replacing subjective manual assess-
ments” (P1).
I.10 LEARNINGSub-actions
Learning reasoning.
Specialization Example & Quote
Update reasoning via prompt
update
Rewrite the agent’s own prompt template; learn a better way
to reason via prompt rewrite.
Learning grounding.
Specialization Example & Quote
Update grounding via code-
based skills
Improve web-navigation code snippets; write or improve code
that interacts with the outside world.
Update retrieval procedures Improve how the agent searches for information (better key-
word strategies, smarter ranking).
Learning knowledge.
Specialization Example & Quote
Update source code as procedu-
ral memory
Self-patch the agent’s own source code to change its behavior.
Update semantic memory with
knowledge
Expand error repository with new mnemonic (P29): “the in-
spection agent identifies a new error type and integrates the
slice into the error repository with a new mnemonic identi-
fier” (P29).
Update memory from new expe-
riences
“refinement of memories (represented in text) as the system
encounters new scenarios” (P17).
Update hypothesis with new ev-
idence
“allowing the model to update its textual understanding, refine
its hypothesis, or even trigger further visual exploration” (P4).
Learning LLM parameters.
33

## Page 34

Specialization Example & Quote
Update parametric policy Change the model’s internal weights through training; real
learning by changing internal weights.
Update LLM parameters via
SL/RL/RLHF
Use supervised, reinforcement, or human-feedback learning
to adjust model weights.
Update action parameters
based on feedback
Auto-adjust parameters from exception info (P1): “automati-
cally adjusts parameters using exception information to gen-
erate executable code” (P1).
Learning instructions.
Specialization Example & Quote
Infer instructions from input–
output examples
Extract the underlying rule from input/output examples for fu-
ture use.
34
