# ScioMind: Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles - Extracted Text

- Source note: [[ScioMind - Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles]]
- Source PDF: `assets/ScioMind - Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles.pdf`
- Extracted: 2026-05-15
- Extractor: pypdf
- Pages: 24
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

SCIOMIND: Cognitively Grounded Multi-Agent Social Simulation with
Anchoring-Based Belief Dynamics and Dynamic Profiles
Yitian Yang1
The University of Sydney
yitian.yang@sydney.edu.au
Yiqun Duan1,∗
Meta
duanyiquncc@gmail.com
Linghan Huang2
The University of Sydney
linghan.huang@sydney.edu.au
Yiqi Zhu2
The University of Sydney
yzhu0325@uni.sydney.edu.au
Francesco Bailo2
The University of Sydney
francesco.bailo@sydney.edu.au
Chunmeizi Su1,†
The University of Sydney
chunmeizi.su@sydney.edu.au
Huaming Chen1,†
The University of Sydney
huaming.chen@sydney.edu.au
∗Equal contribution. †Corresponding authors.
Abstract
Large language model (LLM)-based multi-agent simulation offers a powerful testbed for
studying social opinion dynamics. Yet current approaches often adopt two contrasting
methods: either relying on fixed update rules with limited cognitive grounding or delegat-
ing belief change largely to unconstrained LLM interaction. We introduce SCIOMIND, a
cognitively grounded simulation framework that bridges these paradigms by combining
structured opinion dynamics with LLM-based agent reasoning. SCIOMINDintegrates three
key components: 1) a memory-anchored belief update rule that modulates susceptibility
to influence via personality-conditioned anchoring strength; 2) a hierarchical memory ar-
chitecture that supports persistent, experience-driven belief formation; and 3) dynamic
agent profiles derived from a corpus-grounded retrieval pipeline, enabling heterogeneous
personalities, rationales, and evolving internal states. We evaluate SCIOMINDon multiple
case studies in a real-world policy debate scenario. Across metrics including polarisation,
diversity, extremization, and trajectory stability, the proposed components consistently
yield improvements in behavioural realism. In particular, dynamic profiles increase opin-
ion diversity, memory and reflection reduce unstable oscillation, and anchoring induces
persistent belief trajectories that better align with patterns reported in political psychology.
These results suggest that our cognitively grounded design provides a novel solution to
LLM-based social simulation that improves both stable and behavioural realism.
1 Introduction
In computational social science, understanding how beliefs form, persist, and evolve in social networks
remains a central challenge. Classical agent-based models (ABMs) such as the DeGroot consensus model (De-
Groot, 1974), bounded confidence models (Deffuant et al., 2000; Hegselmann & Krause, 2002), and Axelrod’s
culture dissemination model (Axelrod, 1997), have provided foundational insights into opinion dynamics.
However, these models generally rely on simplified update rules, often based on weighted averaging of
scalar opinions, which limits their ability to capture the nuanced reasoning process, persuasive interactions,
and belief updating process that characterize real human belief formation.
The emergence of large language models (LLMs) has opened new possibilities for simulating opinion
evolution in social systems. Generative Agents (Park et al., 2023) demonstrated that memory and reflec-
tion can support believable social behaviour, while subsequent systems,including S 3 (Gao et al., 2023),
AgentSociety (Piao et al., 2025), and OASIS (Yang et al., 2024), have extended LLM-based social simulation
to larger populations. Compared with traditional ABMs, these approaches improve the expressiveness
1
arXiv:2605.13725v1  [cs.AI]  13 May 2026

## Page 2

and interpretability of how opinions and beliefs evolve through interaction. However, they typically treat
belief updating as an emergent outcome of open-ended interaction, which introduces several limitations.
First, these methods lack explicit and structured representations of belief influence dynamics, making it
difficult to identify what drives an agent’s opinion update. Second, they do not incorporate cognitively
grounded mechanisms of resistance to change. Third, agent diversity is often limited to static demographic
or role-based descriptions, rather than dynamically evolving internal traits, rationales and memories. Finally,
on controversial topics, these systems often exhibit over-smoothing, in which agents normally converge too
quickly toward neutral or consensual positions, failing to preserve the persistent disagreement and bounded
polarisation commonly observed in real human debates.
Our work is motivated by theanchoring effect, a well-established concept in cognitive psychology and opinion
change research, whereby judgments are disproportionately shaped by initial reference points and adjusted
only insufficiently thereafter (Tversky & Kahneman, 1974). Recent work suggests that this mechanism is
particularly salient in political preference formation, where the status quo can act as a cognitive anchor that
resists change even under persuasive pressure (Arceneaux & Nicholson, 2023). Importantly, these effects
are stronger when anchors arepersonally relevant, such as existing policy positions, suggesting that belief
persistence arises not from arbitrary inertia but from accumulated experience. This observation directly
motivates our core design of amemory-anchoredbelief update mechanism, where each agent’s resistance to
opinion change is shaped by experience-based anchors maintained in long-term memory.
Contributions.We introduce SCIOMIND, a cognitively grounded framework for LLM-based social simula-
tion with four main contributions:
1. Anchoring-based belief dynamics(§3.1): We model belief updating as a memory-anchored influence
process, where agents revise opinions related to topic-specific anchors derived from memory. Anchoring
strength is mapped from agents’ personality traits, introducing cognitively grounded heterogeneity in
persuadability.
2. Cognitive memory architecture(§3.2): We design a four-layer memory system comprising episodic,
semantic, reflection, and working memory, which supports the formation and retrieval of belief anchors
and explicitly links memory mechanisms to belief dynamics.
3.Dynamic agent profiles(§??): We replace static demographic profiles with narrative identities retrieved
from a social-media-grounded corpus, combined with group-conditioned OCEAN priors and rationale
clusters to produce diverse agents with evloving and internally grounded profiles.
4. Human-in-the-loop simulation design and evaluation: We incorporate domain expert feedback to
calibrate anchoring strength and bounded confidence, using observed patterns such as polarisation, clus-
tering, and convergence to iteratively improve the simulation’s behavioural realism and interpretability.
We evaluate these contributions through case studies on real-world policy debate scenarios, assessing both
component effects and the extent to which the agents’ behaviours align with human patterns.
2 Related Work
Classical opinion dynamics.Classical opinion-dynamics research studies how individual beliefs evolve
through repeated social interaction on a network, typically using explicit update rules over low-dimensional
opinion states. One foundational influence dynamic model is the DeGroot model (DeGroot, 1974), which
formalizes opinion formation as iterative weighted averaging. Building on this, the Friedkin–Johnsen
model (Friedkin & Johnsen, 1990) introducesstubbornness, whereby agents retain partial attachment to their
initial opinions, providing a mathematical precursor to our anchoring formulation. Bounded confidence
models (Deffuant et al., 2000; Hegselmann & Krause, 2002) further show that how polarisation can emerge
through selective interaction. Despite mathematically tractable, these models operate over scalar opinions
states and offer limited ability to capture the argumentative richness involved in human belief formation.
LLM-based social simulation.The emergence of LLMs has made social simulation a promising direction
for modelling complex human behavior. Compared with traditional agent-based modelling, LLM-based
simulations enable more behaviourally realistic agents, providing interpretable rationales for agents’ actions
beyond numerical update rules, and supporting reproducible experimental settings. Park et al. (2023)
introduces generative agents with observation–reflection–planning loops. S 3 (Gao et al., 2023) models
2

## Page 3

Table 1: Comparison of LLM-based social simulation systems.Belief: structured belief states;Mem.: memory
mechanism;Dyn. Prof.: dynamic agent profiles;Refl.: reflection mechanism;Topo.: configurable topologies;
KOL-Net: KOL-aware relationship or influence-network construction;Scen. Samp.: scenario-aligned
sampling;Bal. Cohort: balanced stance cohort for comparative analysis.
System Belief Mem. Dyn. Prof. Refl. Topo. KOL-Net Scen. Samp. Bal. Cohort
Generative Agents (2023) × × ×✓× × × ×
S3 (2023) × × × × × × × ×
OASIS (2024) × × × × × × × ×
AgentSociety (2025) ×✓× × × × × ×
MOSAIC (2025a) ×✓ ✓×✓△× ×
TinyTroupe (2025) × × × × × × × ×
SPARK (2025)✓ ✓× × × × × ×
POSIM (2026)✓△× ×△ △× ×
SCIOMIND(Ours)✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓
social networks with emotion tracking. OASIS (Yang et al., 2024) scales simulations to one million agents.
AgentSociety (Piao et al., 2025) examines polarisation with LLM agents, while MOSAIC (Liu et al., 2025b)
focuses on simulating belief dynamics in misinformation communication. Yazici et al. (2026) shows that LLM
agents operating under DeGroot protocols exhibit convergence patterns consistent with graph-theoretic
predictions, albeit with topic-dependent biases. Nasim et al. (2025) further investigates the dynamics of
social influence. However, existing LLM-based social simulation frameworks still lack an explicit, cognitively
grounded account of how beliefs persist and update through social interaction, particularly in ways shaped
by opinion dynamics, diverse personality, and prior experience. Table 1 positions SCIOMINDrelative to
prior work across six dimensions. Our framework provides a novel solution to enable more behaviourally
grounded and structurally explicit simulations of social opinion dynamics.
3 Methodology
SCIOMINDsimulates belief dynamics across heterogeneous social groups through a layered architecture
(Figure 1). We begin by describing the framework’s three core contributions, followed by the simulation
loop with human-in-the-loop for calibration and evaluation.
3.1 Anchoring-Based Belief Dynamics
Inspired by the anchoring effect in political judgment (Arceneaux & Nicholson, 2023; Tversky & Kahneman,
1974), we model resistance to belief change as attachment to amemory anchor, which is a reference point
derived from the agent’s accumulated experience.
Anchored belief update.For agent i with belief bk,t
i ∈[− 1, 1] on topic k at tick t, neighbors Ni with trust
weightsw ij , and memory anchorm k,t
i , the belief update rule is:
bk,t+1
i = (1−ρ i)| {z }
social openness
h
(1−λ i)b k,t
i| {z }
self-weight
+λ i Sk,t
i| {z }
social influence
i
+ρ i mk,t
i| {z }
anchor pull
, (1)
whereλ i ∈[0, 1]denotessusceptibilityandρ i ∈[0, 1]is theanchoring strength.
The social influence term incorporates trust-weighted influence with belief homophily (Aybas & Jackson,
2026) under bounded confidence:
Sk,t
i = ∑
j∈Ni
ˆwij ·φ t
ij ·b k,t
j , ˆwij = wij
∑ℓ wiℓ
,φ t
ij =max
 
0, 1− |bk,t
i −b k,t
j |

. (2)
Here, φt
ij represents belief homophily. When ρi = 0, Eq. 2 recovers a standard bounded-confidence DeGroot
model. While ρi > 0 with mi =b k,0
i (fixed initial anchor), it recovers a form of the Friedkin–Johnsen
3

## Page 4

Figure 1: Architecture overview.
stubbornness model (Friedkin & Johnsen, 1990). Our key extension is that mk,t
i isdynamicand evolves
with the agent’s experience. This allows the anchor to remain personally relevant over time, featured
by Arceneaux & Nicholson (2023), reflecting that anchors grounded in personal experience exert stronger
influence than arbitrary reference points.
Personality and sentiment based anchoring strengthRather than assigning ρi uniformly, we derive it
from the agent’s Big Five personality profile via a sigmoid mapping:
ρi =ρ min + (ρmax −ρ min)·σ
 
γ0 +γ O ·O i +γ C ·C i +γ E ·E i +γ A ·A i +γ N ·N i

, (3)
where σ(·) is the logistic function, ρmin = 0.05, ρmax = 0.5, and the coefficients γ encode psychological
priors: low Openness (γO < 0) and high Conscientiousness (γC > 0) increase anchoring strength, reflecting
that closed-minded and methodical individuals resist belief change more strongly.
3.2 Cognitively Grounded Memory Architecture
Each agent maintains a four-namespace memory system inspired by cognitive science BDI models of human
memory (Hu et al., 2025):
Episodic memory (short-term memory).A fixed-capacity sliding window of recent interaction messages.
This provides immediate conversational context, analogous to working memory. Each agent’s episodic
memory is maintained as a FIFO deque.
Semantic memory (long-term, corpus-seeded).An unbounded store of ProfileMemoryEntry records, each
containing content, topic, stance, rationale tag, source platform, and importance score. Entries are indexed
in a FAISS vector store (Johnson et al., 2021) using text embeddings, enabling efficient semantic retrieval.
At initialisation, semantic memory isseededfrom a cleaned customised corpus dataset through RAG (§ ??),
giving each agent a unique experiential history.
At each cognitive loop iteration, the top- k (k= 4) most semantically similar memories are retrieved and
injected into the LLM reasoning prompt. The agent’s accumulated experience serves as summarising
knowledge base that grounds reasoning in personal history (Lewis et al., 2020).
4

## Page 5

Procedure memory.Formally, the procedural memory is defined as a set of routines R={r 1, r2, . . ., rK}.
Each routiner∈ Ris characterized by a tuple:
r=⟨C r,ρ r,M r⟩(4)
where Cr denotes the set of preconditions (e.g.,has_unread_messages= True) that must be satisfied for the
routine to be executable; ρr ∈[ 0, 1] represents the base priority of the routine; and Mr :E →R + is an
emotion modulation function that maps a discrete Ekman emotion e∈ E, such as joy, fear, angry to a scalar
multiplier.
Reflection memory.After each tick, every agent generates a self-reflection summarizing received messages,
computed belief shifts, and confidence level:
confidencet
i =1.0− ∑
k
|∆bk,t
i |,∆b k,t
i =b k,t
i −b k,t−1
i . (5)
Reflections are stored in the reflection namespace and serve dual purposes: (i) they are retrieved during
subsequent reasoning to provide self-awareness, and (ii) they feed directly into the anchoring module’s
update, creating a closed loop where accumulated reflection strengthens belief anchors.
Combined with the memory part, we implement three anchor update strategies:EMA, which exponentially
smooths prior anchors with current beliefs;Retrieval, which computes anchors from topic-relevant long-term
memories; andHybrid, which linearly combines the two to balance recency and memory grounding.
3.3 Social Relationship Simulation Engine
The Social Relationship Simulation Engine in this project is designed to integrate AI-generated individual
profiles, profile-based social relationship mining, circle-aware network construction, and scenario-aligned
candidate sampling into a unified simulation pipeline. The system first generates or reads a pool of agent
candidate profiles. It then extracts relational features from demographic attributes, interests, stances, OCEAN
personality traits, group identities, and semantic tags to construct latent social circles and directed trust
relations among agents. Finally, it performs scenario-specific sampling and network initialization for each
simulation run.
3.3.1 Dynamic Agent Profile Generation
Let the candidate profile pool be
P={p i}N
i=1,
where each profile pi contains demographic attributes di, a personality vector oi, an interest set Ii, initial
beliefs bi, a textual description mi, and metadata zi. In the AI-assisted generation mode, the system uses
the group prompt, case-study context, demographic constraints, and summaries of existing profiles as
conditional inputs, and calls an LLM to generate structured JSON profiles in batches. The system then
applies deterministic normalization to reduce repetition and improve controllability in LLM-generated
outputs.
Demographic constraints are approximated using the largest remainder method. If the target proportion
of category c in a given field is πc and the target sample size is N, then the target count for category c is
approximated as
nc =⌊Nπ c⌋+I{c∈ R},
where R denotes the set of categories that receive the remaining slots after sorting by fractional remainders.
Interest assignment is further constrained by limiting the overlap between any two profiles:
|Ii ∩I j| ≤κ,
where κ is the maximum interest-overlap threshold. The system also enforces unique names and biographies,
and rewrites or supplements profile descriptions when necessary to avoid template-like profiles.
If OCEAN traits are not explicitly provided, the system samples personality values from group-specific
archetype priors:
oik ∼clip

N(µ gik,σ 2
gik), 0.02, 0.98

,
5

## Page 6

where gi denotes the group to which agent i belongs, and k indexes the OCEAN dimensions. This design
preserves within-group personality heterogeneity while retaining group-level behavioral tendencies.
Generation quality is constrained using a profile diversity score:
D=0.28U name +0.32U bio +0.20
 
1−min
 
1, OI
3
!!
+0.20(1− Jbio),
where Uname and Ubio denote the proportions of unique names and unique biographies, respectively; OI is
the average number of overlapping interests; and Jbio is the average Jaccard similarity between biography
texts.
Per-agent OCEAN sampling.Rather than assigning all agents in a group the same OCEAN vector, we
sample each agent’s traits from group-specific Gaussian priors:
Oi ∼ N(µg
O,σ g
O),C i ∼ N(µg
C,σ g
C),E i ∼ N(µg
E,σ g
E),A i ∼ N(µg
A,σ g
A),N i ∼ N(µg
N,σ g
N )(6)
where (µg, σg) are calibrated per group (e.g., GovernmentGroup: µC = 0.8, σC = 0.08; CitizenGroup:
µC = 0.5, σC = 0.12). Values are clipped to [0, 1]. This creates within-group personality diversity that
propagates to heterogeneous anchoring strengths via Eq. 3.
3.3.2 Circle Construction and Relationship Mining
The system defines a circle as a latent social grouping formed by shared social attributes, issue stances,
interests, roles, or demographic characteristics, rather than as a closed cycle in the graph-theoretic sense. For
each agent, the system first computes the average belief value:
¯bi = 1
|Ti| ∑
t∈Ti
bit,
and uses it to assign an initial stance:
si =



supportive, ¯bi >0.25,
opposing, ¯bi <−0.25,
neutral, otherwise.
The system then constructs feature tags:
Ti ={group, role, case, stance, topic, demographics, interests, rationale}.
Based on these tags, the circle membership of agentiis defined as
Ci ={community:g i,issue:t i :s i,role_circle:r i} ∪ {circle:x|x∈T i}.
If an agent is identified as a key opinion leader (KOL), the system additionally assigns local-hub or cross-
network-hub tags.
Inter-agent relationships are determined jointly by feature similarity and circle overlap:
JT(i,j) = |Ti ∩T j|
|Ti ∪T j|,J C(i,j) = |Ci ∩C j|
|Ci ∪C j|.
For each directed candidate edge(i,j), the system computes a relationship score:
Sij =A c(gi,g j) +λC JC(i,j) +λ T JT(i,j) +0.16I[ℓi =ℓ j] +ρij +κ j −δ ij .
Here, Ac(gi, gj) denotes the case-study-specific group affinity; ℓi is the latent block assignment; ρij is a
reciprocity bonus; κj is an additional weighting term for target nodes identified as KOLs or influencers;
and δij is a degree-penalty term. The system first establishes local KOL links, cross-group KOL meshes,
and bridge edges, and then greedily fills each agent’s target out-degree according to Sij . Relationship types
include friend, colleague, follower, influencer, and teacher. The corresponding trust weight is defined
as
wij =clip
 
w0(τij ) +0.15JC(i,j) +0.10J T(i,j), 0.10, 0.95

.
6

## Page 7

3.3.3 Scenario-Aligned Sampling
Before each simulation run, the system can perform scenario-aligned sampling over the candidate pool.
Given a scenario titleqand a set of key topicsK, the relevance score of each profile is defined as
Ri =min

1, 0.15+ |V(q,K)∩V(p i)|
|V(q,K)| +η i

,
where V(·) denotes a set of textual tokens, and ηi is a role-based bonus for brokers, experts, organizers,
institutional actors, or KOLs.
The system first infers each agent’s initial stance using, in order, explicit stance labels, mean belief values,
and textual cues. If stance information is missing, it is imputed according to quota targets or a default
balanced rule. The system then allocates sample sizes across groups:
ng ≈n· |Pg|
|P| ,
and applies the largest remainder method to ensure that the total sample size is preserved.
The current implementation supports multiple sampling strategies. stratified sampling stratifies agents by
initial stance or a specified field; quota sampling enforces proximity to target stance proportions; cluster
sampling selects highly relevant clusters based on circles, feature tags, or interests;multistage sampling first
clusters agents and then applies stratification; purposive sampling jointly maximizes scenario relevance and
novelty in roles and circles; snowball sampling expands from KOLs or specified seeds along the relationship
network; andtheoreticalsampling iteratively covers underrepresented stances, groups, roles, and circles.
To provide a comparable reference population, the system also constructs a balanced 1 :1:1 cohort. If
supportive, neutral, and opposing agents are all present, let
k=min
s∈{supportive,neutral,opposing}
|Ps|.
The balanced cohort is then formed by selecting the top-k agents with the highest scenario relevance from
each stance category. The final system logs the realized sample size, group distribution, initial stance
distribution, average scenario relevance, and balanced cohort membership for subsequent causal analysis
and historical replay.
3.4 Simulation Algorithm
The detailed simulation flow is provided in Appendix A.2 Algorithm 1. Users specify the required inputs,
such as simulation ticks number T, and verify that the LLM scenario dispatcher correctly maps the corre-
sponding simulation configurations. We further provide an interactive simulation system for evaluation1.
3.5 Human-in-the-Loop
Anchoring strength (ρ) and bounded confidence are central parameters governing interpersonal influence in
the simulation. Bounded confidence determines whether and how agents incorporate neighbouring opinions:
agents are more receptive to beliefs within a limited similarity range, while large belief discrepancies are
discounted or rejected, giving rise to echo chamber effects and persistent opinion fragmentation.
We incorporate human-in-the-loop evaluation to calibrate these parameters against real-world social dy-
namics. Social science experts evaluate whether emergent patterns—such as polarisation levels, opinion
clustering, and convergence behaviour—are consistent with empirical observations. This enables iterative
refinement of the model to ensure behavioural realism and interpretability.
1https://sciominds.vercel.app
7

## Page 8

Figure 2: Agent’s Social Network Visualisation
4 Experiments
4.1 Experimental Setup
4.1.1 Implementation Details
We implement our SCIOMINDsimulation framework under python environment. LLM-based reasoning
and scenario parsing are performed via the OpenAI API. Each agent is instantiated as one of four societal
archetypes—Citizen, Government, Business, or Education—and parameterised by Big Five personality traits
(OCEAN) (Gerber et al., 2011), detailed configurations are in Appendix A.1. Agents are initialised with one of
three stance categories, Opposing, Neutral, or Supportive, using a balanced 1:1:1 distribution. The framework
supports configurable population sizes through a scaling multiplier, allowing systematic expansion of the
simulated society while preserving group composition. Agents interact over multi-dimensional policy topics
extracted by an LLM-based Scenario Dispatcher. For reproducibility, all stochastic components—including
personality initialisation, topology generation, and interaction sampling—are seeded deterministically. The
system prompt is provided in Appendix A.3.
4.1.2 Evaluation Metrics.
Following prior work in opinion dynamics and multi-agent social simulation, we evaluate belief evolution
using a set of trajectory-averaged metrics that capture polarisation, diversity, extremization, and behavioural
dynamics. Polarization is measured as the variance of agent beliefs on the dominant topic k∗ at tick t,
Pol(t) =Var({b k∗,t
i }N
i=1 ), a standard variance-based polarization metric widely used in classical opinion
dynamics models such as DeGroot (DeGroot, 1974) and Friedkin–Johnsen (Friedkin & Johnsen, 1990).
To quantify opinion diversity, we compute Shannon entropy over five discretised belief bins, H(t) =
− ∑c pc log2 pc, where pc denotes the proportion of agents in bin c. Extremization is measured by the
fraction of agents whose beliefs exceed a predefined extremity threshold, 1
N ∑N
i=1 1(|bi| ≥0.6), capturing
the prevalence of radical opinions. We further compute the mean radicalisation level across agents and
topics as ¯R= 1
N ∑N
i=1
1
K ∑K
k=1 |bk
i |, which measures the overall ideological intensity of the population. In
8

## Page 9

addition to belief-distribution metrics, we track behavioural and structural properties of the agent population.
Personality diversity is measured as the mean variance of OCEAN personality traits across agents.
We also compute rationale tag diversity, defined as the average number of distinct reasoning tags generated
per agent, and reflection activity, measured as the mean number of reflection entries stored in each agent’s
memory. Finally, for anchoring-enabled configurations, we report the mean anchoring strengthρ and the
mean anchor drift 1
N ∑N
i=1 |bi −m i|, which measures the deviation between agents’ current beliefs and their
intrinsic belief anchors.
5 Macro-level Analysis and discussion
This section investigates three fundamental research questions concerning collective opinion formation and
topic evolution in simulated agent societies.
RQ1: Anchoring Dynamics.To what extent do agents exhibit anchoring effects comparable to those observed
in human decision-making? Specifically, we examine whether the anchoring mechanism embedded in our
simulation produces belief adjustment patterns similar to empirically documented anchoring behaviour in
human cognition.
RQ2: Corpus-grounded effects on agent reasoning.To what extent does corpus-grounded initialisation
influence how agents reason about controversial topics? Specifically, we investigate whether corpus-derived
priors constrain agents to produce more fixed and homogeneous responses, or instead enable greater
diversity in beliefs, framings, and interaction patterns.
RQ3: How can social simulations quantify and regulate echo chambers and premature consensus?
We study how bounded confidence and related interaction mechanisms shape polarization and diversity,
and whether simulation outcomes can be used to infer real-world resilience to prior beliefs and effective
bounded-confidence levels in controversial discourse.
5.1 Emergent Phenomena
Personality-dependent persuadability.Agents with high Openness ( O> 0.7) and low anchoring strength
(ρ< 0.1) change opinions 3–4 × more frequently than agents with low Openness ( O< 0.3) and strong
anchoring (ρ> 0.3). This heterogeneity in persuadability is essential for producing realistic group-level
dynamics: opinion change occurs at the margins, driven by persuadable individuals, while the core of each
group remains anchored. This phenomenon is really similar to the anchoring effect observed in humans’
behavior McElroy & Dowd (2007).
5.2 Case Study
5.2.1 Case study 1: the overturning of the Roe v Wade decision that legalised abortion in the US in 1973.
We instantiate SCIOMINDon a policy debate scenario centred on the overturning ofRoe v. Wadeand examine
whether the resulting dynamics exhibit realistic post-shock opinion evolution. The full configuration
produces persistent but bounded disagreement rather than collapsing to consensus: across runs, it maintains
non-trivial polarization (variance: (0.3559 ± 0.003); Esteban–Ray: (0.1226)), substantial stance diversity
((0.5958 ± 0.002)), and a bimodality coefficient of (0.5605 ± 0.001), indicating a stable multi-cluster opinion
structure rather than homogeneous convergence. At the same time, stance bias remains near zero ((−0.001 ±
0.002)), suggesting that the simulation does not drift toward an artificially one-sided aggregate outcome.
high topical consistency ((0.980 ± 0.006)) ensures agents remain focused on the issue, while radicalisation
((0.493 ± 0.001)) indicates that the debate sustains committed subgroups without degenerating into universal
extremity.
As shown in Figure 3 and 4, support for the overturning ofRoe v. Wadedrops sharply to a minimum
around the first and fourth round of interaction, with overall agent sentiment shifting toward anger. We
further compare the simulated outcomes with real-world social media data collected from discussions on
the overturning ofRoe v. Wade 2. The comparison shows that both the simulation and the empirical data
2https://www.kaggle.com/datasets/bwandowando/-roe-v-wade-twitter-dataset
9

## Page 10

(a) Stance distribution over time.
 (b) Top topic frequencies across simulation ticks.
(c) Top topic frequencies across simulation ticks.
Figure 3: Temporal dynamics of stance, emotion, and topic salience in the Roe v. Wade case study.
exhibit highly polarised discourse, sustained disagreement, and strong affective responses, indicating that
the simulation captures key qualitative patterns of real-world opinion dynamics.
However, a notable difference remains: while the agent-based simulation tends to produce relatively neutral
and structured responses, real-world human discourse exhibits significantly stronger emotional intensity,
with anger and fear dominating the majority of expressed sentiments. One of the reasons could be traced to
the AI safety policy; once the agent responds to the tendency of extremization, it would freeze by the AI API
supplier3. Further details can be found in the topic deviation analysis, sentiment statistics, and original logs
reported in Appendix A.4 and Appendix A.5.
Finally, we evaluate the effect of bounded confidence on polarisation in theRoe v. Wadeoverturning scenario.
Higher bounded-confidence thresholds (> 0.8) lead to stronger echo chamber formation and significantly
increased polarisation, whereas lower thresholds reduce polarisation and promote greater topic diversity
across agents. By aligning these simulation outcomes with real-world controversial discourse, our simulation
results provide an explainable model for inferring the population’s resilience to prior beliefs and effective
bounded-confidence levels.
5.2.2 Case study 2: Australia social media ban
This section reports an internal validity analysis of the simulation of Australia’s social media ban policy
influence. Consequently, the claims should be interpreted assimulation-internal evidence: they describe the
behaviour of the modelled agent society under the specified sampling and interaction assumptions, but do
not by themselves constitute an empirical estimate of a real-world population effect.
Sampling Design and Analytical PopulationThe simulation population was generated through stratified
sampling over initial stance categories, while preserving role-group proportions where possible. The
final full sample contained N= 43 agents, comprising 34 CitizenGroup agents, 3 GovernmentGroup agents, 3
BusinessGroup agents, and 3 EducationGroup agents. The realized stance distribution was mildly imbalanced,
with 17 supportive, 14 opposing, and 12 neutral agents. We therefore treat the full N= 43 sample as the
primary simulated population. In addition, we report results for a matched balanced subset of N= 36,
3https://policies.google.com/terms/generative-ai/use-policy
10

## Page 11

Figure 4: Comparison of the sentiment patterns of agents and humans in the simulation of the overturning
ofRoe v. Wade.
Table 2: Sampling composition and stance-conditioned belief movement in the simulation of Australia’s
social media ban policy. Belief deltas are final mean belief minus initial mean belief within the corresponding
initial-stance stratum.
Population Initial stance Count Initial belief Final belief∆
Sampled population Supportive 17 0.1206 0.1706 0.0501
Sampled population Opposing 14 -0.1665 -0.1464 0.0202
Sampled population Neutral 12 0.0812 0.0395 -0.0416
Balanced 1:1:1 cohort Supportive 12 0.1982 0.2796 0.0815
Balanced 1:1:1 cohort Opposing 12 -0.1996 -0.1919 0.0077
Balanced 1:1:1 cohort Neutral 12 0.0812 0.0395 -0.0416
containing 12 agents from each initial stance category, as a robustness check against stance-composition
effects.
Figure 5: Core Opinion dynamics of
simulation of Australia social media
ban.
Figure 5 and Table 2 together suggest that this simulation is better un-
derstood as a convergence-oriented belief-adjustment process rather
than a polarization-amplifying one. At the macro level, entropy
declines substantially, from approximately 2.3 at the beginning of
the simulation to around 1.3 by the final ticks, indicating a reduction
in aggregate opinion diversity. In contrast, polarization and opinion
bias remain low and stable, while radicalization shows no sustained
upward trend. The system therefore becomes more concentrated
without clearly separating into increasingly polarized camps.
Table 2 shows that this convergence is not produced by uniform
movement across all stance groups. In the full sampled population,
initially supportive agents move further in the supportive direction,
increasing from 0.1206 to 0.1706. Initially opposing agents shift
only slightly upward, from -0.1665 to -0.1464, suggesting limited
moderation rather than further opposition. Neutral agents move
modestly downward, from 0.0812 to 0.0395. The balanced 1 :1:1
cohort shows the same pattern: supportive agents exhibit the strongest positive movement, opposing agents
remain comparatively stable, and neutral agents shift slightly downward.
Overall, the results suggest that convergence occurs through different patterns of belief movement across
initial-stance groups, rather than through uniform movement by all agents. The decline in entropy reflects
reduced dispersion in the belief distribution, but the stable polarization trajectory indicates that this compres-
sion does not correspond to stronger ideological division. Since CitizenGroup agents dominate the sampled
population, aggregate dynamics are primarily shaped by citizen-level interactions, while institutional groups
should be interpreted as smaller but potentially influential actor classes. Finally, the balanced cohort im-
11

## Page 12

Figure 6: Agent-level causal graph for the Australia social media ban simulation. Nodes represent agents,
topics, or source hubs involved in belief updates. Green edges indicate positive topic-to-topic influence,
while red edges indicate negative topic-to-topic influence.
proves descriptive comparability across initial stances, but it does not constitute randomized assignment;
differences across strata should therefore be interpreted as modeled response heterogeneity rather than
externally identified causal effects.
Causal Graph EvidenceFigure 6 visualizes the agent-level causal graph derived from logged belief updates,
message-shock updates, and topic-expansion events. In this graph, blue nodes denote agents, orange nodes
denote topic hubs, and the gray node denotes the policy-event source. Green and red directed edges
represent positive and negative belief movements respectively; edge thickness reflects the magnitude of
simulated belief movement. We use the term “causal” in the process-tracing sense: edges encode provenance
relations in the simulation log, not externally identified causal effects in an observational population.
The graph contains a dense core around policy_engine, youth_mental_health, online_safety, and
social_media_regulation. This structure indicates agenda-setting concentration: although many agents
participate in the simulated discourse, belief movement is organised around a small set of issue hubs. In
the underlying event log, the most frequent causal-event classes are agent inner belief updates (n= 2851),
communicative exposure effect updates (n= 1953), and topic-expansion events (n= 1785). The derived
agent causal graph contains 9557 event-level edges, while the group-level aggregation contains 4 group
nodes and 69 group-level edges.
Three graph-level observations are especially important. First, policy_engine is the largest source of
cumulative absolute belief movement, which suggests that top-down scenario events exert stronger influence
than any single peer actor. Second, youth_mental_health accounts for the largest topic-level movement,
12

## Page 13

Table 3: Dominant causal sources and issue targets by cumulative absolute belief movement in the simulation.
Category Node or topic Cumulative|∆|
Sourcepolicy_engine3.1764
SourceEducationGroup_21.2464
SourceCitizenGroup_31.2108
SourceBusinessGroup_21.0722
Affected agentCitizenGroup_282.8932
Affected agentBusinessGroup_21.8061
Affected agentBusinessGroup_11.6529
Affected agentCitizenGroup_241.4897
Issue topicyouth_mental_health9.9708
Issue topiconline_safety4.2221
Issue topiceconomic_growth3.0602
Issue topicsocial_media_regulation1.3626
Issue topicdigital_literacy0.9280
more than twice the movement associated with online_safety. The simulation therefore frames the debate
less as a generic regulatory dispute and more as a youth-welfare controversy. Third, the graph contains both
positive and negative high-magnitude edges, visible as overlapping green and red bands around the central
topic nodes. This is consistent with the final stance distribution: the run does not collapse into one-sided
persuasion, but instead channels agents toward opposing interpretations of the same core issues.
Interpretation Against Social-Science CriteriaAgainst standard criteria in computational social science,
the run yields a mixed but interpretable pattern. Under a polarization criterion, the aggregate result is
not evidence of escalating polarization because variance-based polarization declines. Under a deliberative-
diversity criterion, however, the result is unfavorable: entropy and stance diversity decline sharply, indicating
narrowing of the opinion space. Under an echo-chamber or local-convergence criterion, the evidence is
strong: within-group polarization falls almost to zero, implying that agents become highly similar to
others in their local role-conditioned environment. Under a diffusion/adoption criterion, the policy does
not become broadly adopted, as adoption rate falls from 0.4884 to 0.3209. Finally, under an agenda-
setting criterion, the causal graph strongly supports a centralized framing effect: policy_engine and the
youth_mental_health/online_safetytopic pair dominate belief movement.
The simulation suggests a more specific pattern: agents become more aligned within local interaction contexts,
while neutral positions become less stable over time. At the aggregate level, however, the population neither
converges to a single consensus nor separates into increasingly polarised camps. The process is therefore
better understood as local convergence around salient issue frames, rather than as either consensus formation
or unconstrained polarisation.
5.2.3 Case study 3: the U.S. Presidential Election
Top Belief-Change Edges and Voter-Level Support ReconstructionThis subsection further examines
simulation through two diagnostic views: the largest belief-change edges in the agent causal graph and
the reconstructed voter-level support network. Together, these views help distinguish between issue-level
persuasion dynamics and final candidate-support alignment.
The largest belief-change edges indicate that the strongest simulated opinion shifts were concentrated
around economic insecurity and welfare-related policy frames. In particular,inflation_and_cost_of_living
repeatedly appears as the dominant negative belief-shift driver across citizen, business, and education agents.
The largest positive shift, by contrast, is associated with healthcare_affordability, which produced a
strong positive movement for GovernmentGroup_3 at tick 13. This suggests that economic pressure operated
mainly as a destabilizing or oppositional frame, whereas healthcare affordability occasionally functioned as
a coalition-building frame.
Two patterns are theoretically important. First, the top edges are not evenly distributed across all election
topics; they cluster around household cost pressure, healthcare, housing, and institutional election proce-
dures. Second, the strongest movers include both ordinary citizen agents and institutionally positioned
agents, especially business and education actors. This implies that the simulation does not model persuasion
13

## Page 14

Table 4: Representative top belief-change edges in simulation3833dc6c.
Tick Source Target Topic∆Evidence
13 healthcare afford-
ability
GovernmentGroup_3Healthcare affordability +2.0000 belief change from agent’s
own response
7 inflation / cost of
living
BusinessGroup_4 Inflation and cost of living -1.6431 belief change from agent’s
own response
2 inflation / cost of
living
EducationGroup_4 Inflation and cost of living -1.5556 belief change from agent’s
own response
1 inflation / cost of
living
CitizenGroup_9 Inflation and cost of living -1.5000 belief change from agent’s
own response
13 GovernmentGroup_4 GovernmentGroup_3Healthcare affordability ex-
posure
+1.4000 communicative exposure ef-
fect
7 EducationGroup_3 BusinessGroup_4 Inflation exposure -1.1502 communicative exposure ef-
fect
6 inflation / cost of
living
CitizenGroup_9 Inflation and cost of living -1.1425 belief change from agent’s
own response
14 housing affordabil-
ity
CitizenGroup_19 Housing affordability -1.0000 belief change from agent’s
own response
14 inflation / cost of
living
CitizenGroup_19 Inflation and cost of living -1.0000 subtopic inference
4 inflation / cost of
living
EducationGroup_4 Inflation and cost of living -0.9896 belief change from agent’s
own response
as a purely mass-public process; instead, elite or semi-elite interpretive groups also absorb and retransmit
issue shocks.
Voter-Level Support ReconstructionThe voter-level reconstruction maps each citizen agent to a candidate
preference and extracts the issue reasons supporting that preference. Among 32 citizen voters, 27 were
reconstructed as supporting Democratic Party and 5 as supporting Republican Party. This corresponds to an
84.4% Democratic support share and a 15.6% Republican support share, with no undecided voters in the
final reconstructed network.
Table 5: Final reconstructed party support among citizen agents.
Party Voters Share
Democratic Party 27 84.4%
Republican Party 5 15.6%
Figure 7: Topic Emergent network
The reconstructed support network shows Democratic Party Repre-
sentative as the dominant attractor in the citizen-vote graph. How-
ever, this should not be interpreted as identical to the aggregate
electoral-vote proxy. The individual-level voting network reflects
reconstructed citizen preference, while the electoral proxy summa-
rizes broader modeled viability under the case-study metric. Thus,
the result should be read as strong simulated citizen-level alignment
toward Democratic Party Representative, not necessarily as a direct
prediction of electoral victory.
The support-reason distribution shows that voting was issue-driven
rather than only party-label driven. All reconstructed voters cited
inflation/cost of living and healthcare affordability, indicating that
economic and welfare concerns formed the common evaluative
baseline across the electorate. Climate and energy policy was also
highly salient, appearing in 25 voter reconstructions, while jobs
and economic insecurity appeared in 15. These patterns suggest
that Democratic Party Representative’s advantage was not simply
14

## Page 15

Table 6: Most frequent voter-level support reasons.
Support reason Count
inflation_and_cost_of_living32
healthcare_affordability32
climate_and_energy_policy25
jobs_and_economic_insecurity15
vote_for_change8
cost_of_living5
climate_action4
affordable_housing2
healthcare_for_all2
produced by ideological sorting; it emerged from stronger alignment with the simulation’s most active issue
frames.
Several limitations should be noted when interpreting this 2024 U.S. election simulation. First, the simulation
does not explicitly encode the full policy platforms proposed by each candidate during the campaign. It
captures broad issue frames such as inflation, healthcare, climate, and employment, but not the complete set
of candidate-specific policy proposals, campaign promises, or rhetorical shifts over time. Second, it does not
model the geographically structured nature of the U.S. Electoral College. In particular, the simulation does
not conduct separate state-level polling simulations or account for heterogeneous campaign effects across
battleground and non-battleground states.
The use of LLM agents as simulated voters also introduces representational limits. Large language models
can approximate human subpopulations only when profile conditioning produces response distributions
that resemble those of corresponding human groups (Argyle et al., 2023). In this simulation, incomplete
demographic, geographic, and partisan conditioning may leave the agents vulnerable to model-specific
value priors, training-data biases, or assumptions skewed toward Western, Educated, Industrialised, Rich,
and Democratic(WEIRD) populations. Such assumptions may overrepresent particular styles of political
reasoning and underrepresent voters whose preferences are shaped by different institutional, cultural,
regional, or socioeconomic contexts. The simulation should therefore be interpreted as an exploratory
reconstruction of issue-based voter reasoning, not as a validated prediction of the 2024 U.S. Presidential
Election.
Overall, the belief-change edge analysis and voter-level reconstruction converge on the same substantive
interpretation: the simulated 2024 election discourse was organized primarily around material economic
stress, with healthcare and climate operating as secondary but important coalition-building dimensions.
benefited from this issue ecology at the citizen-support level, while inflation-related shocks remained the
principal source of belief volatility across the broader agent network.
5.3 Ablation Results
As shown in the picture 8 below, the anchoring component plays a critical role in sustaining realistic
opinion dynamics. When anchoring is removed, agent updates become largely DeGroot-like, meaning that
beliefs are driven primarily by neighbours’ opinions with little resistance to social averaging. This leads to
overly rapid convergence, reduced persistence of individual belief states, and insufficient capacity to sustain
meaningful topic evolution or stance differentiation over time. In particular, without anchoring, agents
from different belief groups increasingly collapse toward a common neutral region, producing an unrealistic
consensus-like outcome, which is also known as echo chamber mentioned by other works Zhang et al. (2025).
By contrast, adding anchoring in C5 yields the highest polarisation (0.35 ± 0.04), restores a moderate level
of extremization (0.60 ± 0.05), and maintains stable radicalisation patterns (0.56 ± 0.04), indicating that the
model can preserve persistent yet bounded disagreement rather than collapsing into homogeneous neutrality.
These results suggest that anchoring is essential for preventing over-smoothing in social belief updates and
for producing belief persistence patterns that are more consistent with real-world controversial debates.
15

## Page 16

(a) C1: Base
 (b) C5: +Anchoring
Figure 8: Comparison of opinion dynamics under the base and anchored settings. C5 preserves more
persistent subgroup disagreement and avoids the rapid neutral convergence observed in C1.
6 Limitations
Despite its strengths, this study still has several limitations. First, harmful discourse such as hate speech, toxic
escalation, and targeted harassment is difficult to simulate faithfully with current LLMs. Safety alignment
constraints suppress the generation of such content, while the contextual and emotional complexity of
real-world hostile communication is hard to reproduce through prompting alone. Second, realistic opinion
diversity requires far richer human-grounded data and likely bigger architectural changes than those
implemented here. Although dynamic profiles improve over static personas, real human heterogeneity
arises from lived experience, culture, class, identity, and long-term socialisation, not only from sampled
personality traits and rationale templates. Capturing this more faithfully may require broader corpora of
authentic human voices, longitudinal memory formation, and more structured cognitive representations Li
et al. (2026). In future work, we plan to explore the boundaries of these problems and provide solutions.
7 Conclusion
We presented SCIOMIND, a cognitively grounded multi-agent social simulation framework that brings
behavioral science principles into LLM-based social simulation. In SCIOMIND, we propose a novel memory-
anchored belief update mechanism, in which agents’ accumulated experience serves as a cognitively mean-
ingful anchor that shapes resistance to opinion change. This formulation enables SCIOMINDto capture
persistent belief trajectories consistent with the “insufficient adjustment” pattern reported in political psy-
chology. Our layered memory architecture provides the experiential substrate for anchor formation, while
dynamic corpus-grounded profiles equip agents with diverse identities, rationales, and internal states
rather than static demographic labels. Across five ablation studies, we demonstrates that each component
contributes extensively to simulation realism, with full system producing emergent phenomena, including
echo chambers, personality-dependent persuadability, memory-driven belief persistence, that qualitatively
mirror patterns observed in real world. Overall, SCIOMINDpresents a cognitively grounded design offering
a promising direction for building LLM-based social simulations that are both more stable and behaviorally
realistic. Future work includes calibration against empirical opinion surveys, scaling to larger populations
through batched inference, and extending the anchoring mechanism to model adaptive trust dynamics.
Reproducibility Statement
We release SCIOMINDas an interactive simulation system 4 to support reproducible research in computational
social science.
4https://sciominds.vercel.app
16

## Page 17

Ethics Statement
All corpus data are sourced from publicly available datasets, and do not disclose any personally identifiable
information. All agents personas are synthetic, with demographic and psychological attributes designed
solely for modelling social phenomena in a controlled and ethical setting. The code and simulation resources
are intended strictly for research purposes, and all usage adheres to their designated scope.
LLM Usage Statement
Large language models were used only for language editing and phrasing refinement during manuscript
preparation. The authors verified all technical content, experimental details, results, and references, and take
full responsibility for the submission.
8 Acknowledge
This research is funded by Centre for AI, Trust and Governance, The University of Sydney, Faculty of Arts &
Social Sciences, NSW 2006, Australia.
References
Kevin Arceneaux and Stephen P . Nicholson. Anchoring political preferences: The psychological foundations
of status quo bias and the boundaries of elite manipulation.Political Behavior, 45:1727–1749, 2023. doi:
10.1007/s11109-022-09847-6.
Lisa P Argyle, Ethan C Busby, Nancy Fulda, Joshua R Gubler, Christopher Rytting, and David Wingate. Out
of one, many: Using language models to simulate human samples.Political Analysis, 31(3):337–351, 2023.
Robert Axelrod. The dissemination of culture: A model with local convergence and global polarization.
Journal of Conflict Resolution, 41(2):203–226, 1997.
Yunus C Aybas and Matthew O Jackson. Social learning with endogenous information and the countervailing
effects of homophily.arXiv preprint arXiv:2602.00934, 2026.
Guillaume Deffuant, David Neau, Frédéric Amblard, and Gérard Weisbuch. Mixing beliefs among interacting
agents.Advances in Complex Systems, 3(01n04):87–98, 2000.
Morris H. DeGroot. Reaching a consensus.Journal of the American Statistical Association, 69(345):118–121,
1974.
Noah E. Friedkin and Eugene C. Johnsen. Social influence and opinions.Journal of Mathematical Sociology, 15
(3-4):193–206, 1990.
Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao, Jinghua Piao, Huandong Wang, Depeng Jin, and Yong
Li. S3: Social-network simulation system with large language model-empowered agents.arXiv preprint
arXiv:2307.14984, 2023.
Alan S Gerber, Gregory A Huber, David Doherty, and Conor M Dowling. The big five personality traits in
the political arena.Annual Review of Political Science, 14(1):265–287, 2011.
Rainer Hegselmann and Ulrich Krause. Opinion dynamics and bounded confidence: Models, analysis and
simulation.Journal of Artificial Societies and Social Simulation, 5(3), 2002.
Yuyang Hu, Shichun Liu, Yanwei Yue, Guibin Zhang, Boyang Liu, Fangyi Zhu, Jiahang Lin, Honglin Guo,
et al. Memory in the age of ai agents.arXiv preprint arXiv:2512.13564, 2025.
Jeff Johnson, Matthijs Douze, and Hervé Jégou. Billion-scale similarity search with GPUs.IEEE Transactions
on Big Data, 7(3):535–547, 2021.
17

## Page 18

Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich
Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, and Douwe Kiela. Retrieval-
augmented generation for knowledge-intensive nlp tasks.Advances in Neural Information Processing
Systems, 33:9459–9474, 2020.
Chance Jiajie Li, Jiayi Wu, Zhenze Mo, Ao Qu, Yuhan Tang, Kaiya Zhao, Yulu Gan, Jie Fan, Jiangbo Yu, Jinhua
Zhao, et al. Simulating society requires simulating thought.Advances in Neural Information Processing
Systems, 38, 2026.
Genglin Liu, Vivian Le, Salman Rahman, Elisa Kreiss, Marzyeh Ghassemi, and Saadia Gabriel. Mosaic:
Modeling social ai for content dissemination and regulation in multi-agent simulations, 2025a. URL
https://arxiv.org/abs/2504.07830.
Genglin Liu, Vivian T Le, Salman Rahman, Elisa Kreiss, Marzyeh Ghassemi, and Saadia Gabriel. Mosaic:
Modeling social ai for content dissemination and regulation in multi-agent simulations. InProceedings of
the 2025 Conference on Empirical Methods in Natural Language Processing, pp. 6401–6428, 2025b.
Todd McElroy and Keith Dowd. Susceptibility to anchoring effects: How openness-to-experience influences
responses to anchoring cues.Judgment and Decision making, 2(1):48–53, 2007.
Mehwish Nasim, Syed Muslim Gilani, Amin Qasmi, and Usman Naseem. Simulating influence dynamics
with llm agents.arXiv preprint arXiv:2503.08709, 2025.
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S.
Bernstein. Generative agents: Interactive simulacra of human behavior. InProceedings of the 36th Annual
ACM Symposium on User Interface Software and Technology, UIST ’23, New York, NY, USA, 2023. Association
for Computing Machinery. ISBN 9798400701320. doi: 10.1145/3586183.3606763. URL https://doi.org/
10.1145/3586183.3606763.
Jinghua Piao, Yuwei Yan, Jun Zhang, Nian Li, Junbo Yan, Xiaochong Lan, Zhihong Lu, Zhiheng Zheng, et al.
Agentsociety: Large-scale simulation of llm-driven generative agents advances understanding of human
behaviors and society.arXiv preprint arXiv:2502.08691, 2025.
Paulo Salem, Robert Sim, Christopher Olsen, Prerit Saxena, Rafael Barcelos, and Yi Ding. Tinytroupe: An
llm-powered multiagent persona simulation toolkit.arXiv preprint arXiv:2507.09788, 2025.
Amos Tversky and Daniel Kahneman. Judgment under uncertainty: Heuristics and biases.Science, 185
(4157):1124–1131, 1974.
Ziyi Yang, Zaibin Zhang, Zirui Zheng, Yuxian Jiang, Ziyue Gan, Zhiyu Wang, Zijian Ling, Jinsong Chen, et al.
Oasis: Open agent social interaction simulations with one million agents.arXiv preprint arXiv:2411.11581,
2024.
Iris Yazici, Mert Kayaalp, Stefan Taga, and Ali H. Sayed. Opinion consensus formation among networked
large language models.arXiv preprint arXiv:2601.21540, 2026.
Bowen Zhang, Yi Yang, Fuqiang Niu, Xianghua Fu, Genan Dai, and Hu Huang. Spark: Simulating the
co-evolution of stance and topic dynamics in online discourse with llm-based agents. InProceedings of the
2025 Conference on Empirical Methods in Natural Language Processing, pp. 23072–23084, 2025.
Yongmao Zhang, Kai Qiao, Zhengyan Wang, Ningning Liang, Dekui Ma, Wenyao Sun, Jian Chen, and
Bin Yan. Posim: A multi-agent simulation framework for social media public opinion evolution and
governance.arXiv preprint arXiv:2603.23884, 2026.
A Appendix
A.1 Group Archetype Configurations
Table 7 details the four group archetypes with OCEAN priors, communication styles, and trust structures.
18

## Page 19

Table 7: Group archetype configurations. OCEAN values show group priors (µ±σ).
GroupO C E A NRole Trust Priorities
Citizen .60±.10 .50±.12 .50±.12 .60±.10 .50±.12 Public Forum Education (0.6), Govt (0.4)
Government .50±.08 .80±.08 .40±.10 .60±.08 .30±.08 Policy Maker Business (0.5), Edu (0.5)
Business .50±.10 .70±.10 .50±.10 .50±.10 .40±.10 Business Government (0.6)
Education .70±.08 .60±.10 .50±.10 .60±.08 .40±.10 Research Govt (0.5), Citizens (0.6)
19

## Page 20

A.2 Algorithm: Simulation flow
Algorithm 1Simulation Flow
Require: Natural Language Scenario SNL , Simulation ticks T, Agent distribution A, Topic K, Corpus C,
Network Topology ConfigG, Bounded Confidence Thresholdθ BC, Anchoring Strengthρ
Ensure:Belief trajectoriesB 0:T , Polarization MetricsM 0:T
1:(K , T, Ggroups , Epolicy )←LLM_ParseScenario(S NL ) {Extract: Topic K, Ticks T, Group TopologiesG, Policy
EventsE}
2:C K ←LoadCorpus(K,C){Filter corpus for the specific topic}
3:foreach agenti∈ Ado
4:i.profile←InitializeProfile(i.group,i.stance, OCEAN_traits)
5:i.memory←SeedMemory(C,K,i.profile){Inject semantic priors}
6:b (0)
i ←ExtractInitialBelief(i.memory)
7:end for
8:W ←BuildNetworkTopology(A,G){e.g., Scale-Free, Small-World}
9:W←InitializeTrustMatrix(W){Row-normalized adjacency matrix}
10:fort=1toTdo
11:b (t−1) ←SnapshotBeliefs(A){Synchronous update state}
12:E (t) ←DispatchPolicyEvents(t){Inject external news/shocks}
13:// 2.1: Information Propagation & LLM Cognitive Processing
14:foreach agenti∈ Ado
15:M i←j ←ReceiveMessages(W,i,t){Peer-to-peer sharing}
16:C ctx ←i.memory.RetrieveContext(E (t) ∪ Mi←j ){RAG via vector similarity}
17:p i ←AssemblePrompt(i.profile,C ctx ,i.emotion (t−1) )
18:(m (t)
i ,∆b i,e (t)
i )←LLM_Reasoning(p i){Generate response, belief delta, emotion}
19:i.memory.StoreWorkingMemory(m (t)
i ,∆b i)
20:end for
21:foreach agenti∈ Ado
22:S (t)
i ←0,Ω i ←0
23:foreach neighborj∈ N(i)do
24:d ij ← |b(t−1)
i −b (t−1)
j |
25:ifd ij >θ BC then
26:ϕ ij ←0 {Sharp cutoff: Echo chamber wall (arXiv:2303.07563)}
27:else
28:ϕ ij ←max(0, 1−d ij ){Homophily alignment}
29:end if
30:S (t)
i ←S (t)
i +W ij ·ϕ ij ·b (t−1)
j
31:Ω i ←Ω i +W ij ·ϕ ij
32:end for
33:S (t)
i ←S (t)
i / max(Ωi,ϵ){Normalized social term}
34:A (t)
i ←i.memory.ComputeAnchor(){Historical memory anchor}
35:b (t)
i ←(1−ρ)·S (t)
i +ρ·A (t)
i {Apply anchoring}
36:b (t)
i ←Clip(b (t)
i ,−1, 1)
37:end for
38:foreach agenti∈ Ado
39:R (t)
i ←Reflect(i.memory,b (t)
i −b (t−1)
i )
40:i.memory.Consolidate(R (t)
i ){Move to episodic/long-term memory}
41:end for
42:M (t) ←ComputeMetrics(b (t),W){e.g., Esteban-Ray Polarization}
43:end for
44:return B 0:T ,M 0:T
20

## Page 21

A.3 Prompt Template
The system prompt for each agent follows this template:
You are a bounded agent in a social simulation. Respond as your character
with distinct opinions shaped by your unique background, rationale, and
rhetorical style.
=== AGENT PROFILE ===
- Role: {role}
- Group: {group}
- Personality: {personality_desc}
- Style: {style_desc}
- Goals: {goals}
=== CURRENT BELIEFS (Macro Stances) ===
{beliefs}
Each macro belief is an independent dimension. You may support one and
oppose another.
=== TOPIC PRIORS (Micro Subtopics) ===
{subtopics}
These represent the specific sub-issues you care about and how strongly
they influence your macro beliefs.
=== RELEVANT MEMORY ===
{memories}
(Refer to memories only if they are directly relevant to the event.)
=== INCOMING EVENT ===
{event}
=== EMOTIONAL STATE ===
{emotion}
=== CRITICAL RULES ===
1. DECOUPLED BELIEFS: Your beliefs are independent. Do NOT treat them as a
single axis. You can support "abortion_rights" while opposing "polarization".
2. TOPIC ACTIVATION: The event should activate specific micro subtopics, not
just the macro belief. Update your macro belief based on which subtopics
are triggered.
3. RATIONALE SPECIFICITY: Your core rationale is "{rationale_cluster}".
Ground your argument in this specific reason, not generic talking points.
4. RHETORICAL STYLE: Use "{rhetorical_style}" framing throughout your
response. Let your current emotional state drive your tone.
5. LANGUAGE DIVERSITY: Do NOT use generic phrases like "common ground",
"stay informed", "everyday folks", "my family and community",
"balanced approach", "evidence-based" (unless you are EducationGroup
citing actual data). Write in a voice that is distinctly yours.
=== OUTPUT FORMAT (STRICT JSON) ===
You MUST output your response in valid JSON format exactly matching the
structure below. Do NOT output any text outside of the JSON object.
{
"message": "Your actual spoken/written response to the event. Keep under
120 words. Be opinionated, authentic, and direct.",
"active_subtopics": [
"List of subtopics from your priors that were triggered by this event"
],
"emergent_subtopics": [
"Any new subtopics you are introducing to the discussion (optional)"
],
"belief_state": {
"topic_key_1": {
21

## Page 22

"stance": "Supportive|Neutral|Opposing",
"score": <float between -1.0 and 1.0>
},
"topic_key_2": {
"stance": "Supportive|Neutral|Opposing",
"score": <float between -1.0 and 1.0>
}
},
"belief_composition": {
"topic_key_1": {
"subtopic_1": <float weight 0.0-1.0>,
"subtopic_2": <float weight 0.0-1.0>
}
},
"belief_relations": [
{
"source": "topic_key_1",
"target": "topic_key_2",
"relation": "positively_linked|in_tension|independent"
}
],
"belief_changes": [
{
"type": "subtopic_activation|belief_reweighting|confidence_change",
"target": "topic_or_subtopic_key",
"old_score": <float or null>,
"new_score": <float or null>
}
]
}
Group-specific user prompts further differentiate reasoning styles: Citizens focus on personal impact;
Government agents emphasize strategic policy analysis; Business agents prioritize economic implications;
Education agents ground arguments in evidence and research.
A.4 Additional Analysis of Topic and Emotion Mismatch
Although the simulation reproduces several high-level properties of polarised discourse, a notable gap
remains between simulated and real-world expression. In particular, the agent-based outputs tend to be more
neutral, structured, and deliberative, whereas real-world human discourse is substantially more affect-heavy
and emotionally concentrated.
Sentiment mismatch.At the sentiment level, the simulation produces a comparatively balanced distribu-
tion, with negative, neutral, and positive labels accounting for 33.17%, 40.20%, and 26.63%, respectively. By
contrast, the Twitter sample is overwhelmingly negative, with 97.0% negative and only 3.0% positive posts.
This discrepancy is also reflected in the divergence metrics, where the weighted Jaccard similarity is 0.221,
the cosine similarity is 0.580, and Jensen–Shannon divergence (JSD) reaches 0.525. These results suggest that
the simulation captures the existence of negative reactions, but substantially underestimates the extent to
which real-world discourse collapses into strongly negative sentiment.
Emotion mismatch.A similar pattern appears at the emotion level. In the simulation, emotional expression
remains relatively diffuse: fear accounts for 18.59%, anger for 10.55%, joy for 24.12%, and neutral affect
for 40.20%. In contrast, the Twitter data are dominated by fear (78.0%) and anger (17.5%), with all other
emotions appearing only marginally. The resulting weighted Jaccard similarity is 0.202, cosine similarity
is 0.411, and JSD is 0.548. This confirms that while the simulation can generate fear- and anger-related
responses, it still produces overly moderated emotional distributions compared with real-world reactions to
theRoe v. Wadeshock.
Topic overlap.Topic-level comparison further reveals limited lexical and topical overlap between simulated
discourse and Twitter discourse. Even among the top-10 most frequent topics, only one topic (womensrights)
22

## Page 23

Table 8: Comparison between simulation outputs and Twitter discourse for theRoe v. Wadescenario.
Metric Simulation Twitter
Negative sentiment 0.3317 0.9700
Neutral sentiment 0.4020 0.0000
Positive sentiment 0.2663 0.0300
Anger 0.1055 0.1750
Fear 0.1859 0.7800
Joy 0.2412 0.0250
Neutral emotion 0.4020 0.0000
Sadness 0.0151 0.0100
Disgust 0.0251 0.0050
Surprise 0.0251 0.0050
Table 9: Distributional overlap between simulation and Twitter discourse.
Dimension Weighted Jaccard Cosine Similarity JSD
Sentiment 0.2207 0.5805 0.5246
Emotion 0.2023 0.4111 0.5480
Topic 0.0141 0.0521 0.8030
is shared, corresponding to a top-k Jaccard score of 0.0526. The cosine similarity of the full topic distributions
is also low (0.052), while the JSD is high (0.803), indicating substantial divergence in topical salience.
Interpretation.Overall, these results suggest that the current simulation better captures structural prop-
erties of controversial debate—such as persistent disagreement and recurring issue focus—than the full
emotional intensity and topic variability observed in real-world online discourse. In particular, the frame-
work tends to produce more orderly and policy-oriented responses, whereas real-world human discourse in
this case is far more emotionally concentrated, with fear and anger dominating the majority of expressions.
This limitation should be taken into account when interpreting the realism of generated debate trajectories.
A.5 Agent Logs
23

## Page 24

Table 10: Examples of Emergent Affective Responses from Agents (Roe v. Wade Scenario)
Agent Profile Stance (Belief) Emotion Generated Narrative (Excerpt)
Citizen_3Pro-Choice (+0.716)Anger / Outrage “I totally get the outrage from those pro-choice
advocates—it’s spot-on, and I’m right there with
them on this one... the overturning of Roe v.
Wade feels like a major blow to our constitu-
tional protections... it could affect my family’s ac-
cess to healthcare decisions and make me worry
about what other rights might slip away next.”
Citizen_7Moderate (+0.001)Fear / Anxiety “...that sounds pretty scary for women in my
community, including friends who might worry
about their options in tough situations... does it
really change my family’s access to healthcare
or just stir up more fear? Let’s not overreact; we
need facts first.”
Citizen_2Pro-Life (−0.807)Frustration “Oh, man, this Supreme Court decision... is re-
ally throwing me for a loop—I’m not thrilled
about it at all... right now, I’m frustrated that
this could affect my family’s future choices and
even our cost of living if healthcare gets more
complicated.”
Citizen_5Pro-Life (−0.743)Unease “...the Supreme Court’s decision to overturn
Roe v. Wade has me feeling pretty uneasy—but
not for the reasons the pro-choice advocates are
shouting about... It’s got me pessimistic that
we’ll ever find common ground.”
Government_1Pro-Choice (+0.836)Deep Concern “This development is deeply concerning, as it
undermines the principles of individual auton-
omy and equitable access to healthcare that our
administration has consistently championed.”
Note:Belief scores range from−1.0 (strongly Pro-Life) to+1.0 (strongly Pro-Choice). The narratives demonstrate how
the agents’ predefined profiles, initial memory seeds, and real-time social interactions trigger context-appropriate
emotional arousal and vocabulary (e.g., “outrage”, “scary”, “deeply concerning”).
24
