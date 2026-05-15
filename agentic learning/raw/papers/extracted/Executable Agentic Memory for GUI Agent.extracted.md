# Executable Agentic Memory for GUI Agent - Extracted Text

- Source note: [[Executable Agentic Memory for GUI Agent]]
- Source PDF: `assets/Executable Agentic Memory for GUI Agent.pdf`
- Extracted: 2026-05-14
- Extractor: pypdf
- Pages: 26
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

Executable Agentic Memory for GUI Agent
Zerui Qin 1 Sheng Yue2 Xingyuan Hua 1 Yongjian Fu1 Ju Ren 1
Abstract
Modern GUI agents typically rely on a model-
centric and step-wise interaction paradigm, where
LLMs must re-interpret the UI and re-decide ac-
tions at every screen, which is fragile in long-
horizon tasks. In this paper, we propose Exe-
cutable Agentic Memory (EAM), a structured
Knowledge Graph (KG) that shifts GUI planning
from free-form generation to a robust retrieval-
and-execution process. Our approach includes
a sample-efficient memory construction pipeline
using state-aware DFS and action-group mining
to compress multi-step routines. To ensure effi-
cient planning, we introduce a value-guided graph
search where a lightweight Q-function model
steers Monte Carlo Tree Search (MCTS) over the
KG. We theoretically establish bias-consistency
for the Q-model and derive sample complexity
bounds for path recovery. Empirically, EAM out-
performs state-of-the-art baselines like UI-TARS-
7B by up to 19.6% on AndroidWorld, while re-
ducing token costs 6× relative to GPT-4o. With a
2.8s average latency, EAM enables reliable, quick,
and long-horizon GUI automation.
1. Introduction
Modern Graphical User Interface (GUI) agents powered by
(multimodal) LLMs can operate real-world apps by “see-
ing” screens and generating actions (Wen et al., 2024; Wang
et al., 2024a; Zhang et al., 2025). However, the dominant
interaction paradigm remainsmodel-centric and step-wise:
at every screen, an LLM must re-interpret the UI, re-decide
the next action, and implicitly maintain task progress in its
context window. This makes long-horizon automation frag-
ile: small perceptual or reasoning errors would compound,
easily producing hallucinated actions and incorrect detours,
especially in heterogeneous app environments where train-
ing coverage is limited (Qin et al., 2025; Luo et al., 2025;
Wu et al., 2025; Gou et al., 2024). For instance, UI-TARS-
7B (Qin et al., 2025), considered a SOTA GUI agent model,
1Tsinghua University, China 2Sun Yat-sen University, China.
Preprint. May 13, 2026.
achieves only 33% success rate on the long-horizon An-
droidWorld benchmark (Rawles et al., 2024), while M3A,
an agentic framework powered by GPT-4o, attains merely
40.5% (Rawles et al., 2024).
To improve robustness, a natural direction is to equip agents
with external knowledge and memory. Some efforts (Wang
et al., 2024b; 2025; Cheng et al., 2025; Sun et al., 2026)
maintain textual memory of historical interactions, such as
workflow patterns and decision heuristics, and inject them
into the LLM’s context to guide task planning. Others con-
struct external knowledge bases by extracting action-level
knowledge (e.g., element functionality or successful trajec-
tories) from exploration, storing them as vector databases
or knowledge graphs, and retrieving relevant knowledge
at inference time to augment decision-making (Xie et al.,
2025; Jiang et al., 2025; Guan et al., 2025b; Li et al., 2025).
However, such in-context knowledge injection remains un-
reliable due to model-centric generation and ignorance of
inherent structured information in historical trajectories,
making it difficult to reliably reproduce executable paths
from historical knowledge. Moreover, repeated retrieval and
step-wise generation introduce substantial cost and latency,
hindering real-time deployment.
In this paper, we investigateExecutable Agentic Memory
(EAM), which can serve as a persistent, structured repre-
sentation of the environment interaction logic, learned from
historical interactions, and can be queried at test time so
that planning can be augmented by retrieval and verifica-
tion rather than free-form generation. Specifically, EAM
enables the agent to (1) remember the GUl as a state ma-
chine (what states exist, which actions are available, and
where they lead), and (2) reason over this memory to ex-
tract an executable path that is guaranteed to stay on valid
transitions.
To this end, we first propose a sample-efficient memory
construction pipeline: a state-aware DFS exploration strat-
egy that systematically covers task-relevant transitions with
minimal redundant interactions, coupled with state dedu-
plication and action-group mining to compress frequent
multi-step routines into reusable high-level actions, yielding
a compact yet executable GUI logic knowledge graph. We
then propose a compute-efficient retrieval mechanism: a
value-guided graph search procedure in which a lightweight
1
arXiv:2605.12294v1  [cs.AI]  12 May 2026

## Page 2

Executable Agentic Memory for GUI Agent
Q-function model steers MCTS over the constrained KG ac-
tion space to rapidly select faithful high-reward paths from
noisy experience; when needed, the agent can make only
a single cloud call to summarize and validate the retrieved
path into a grounded plan. Theoretically, we establish a
bias-consistency guarantee for the learned Q-model on the
critical set and derive a finite-sample complexity bound
under which the value-guided MCTS recovers the optimal
execution path with high probability.
We evaluate our method on the AndroidWorld, MobileMini-
Wob++, and DroidTask benchmarks. Results show that our
framework consistently outperforms the existing baselines,
surpassing the state-of-the-art UI-TARS-7B by up to 19.6%
while reducing token costs 6× relative to GPT-4o. Our
Q-guided MCTS and iterative self-training pipeline bridge
the reasoning gap for small models through fine-grained
credit assignment, while the action group mechanism min-
imizes search complexity to reach a 2.8s average latency.
These findings demonstrate that grounding decision-making
in structured knowledge graphs enables reliable, high-speed,
and long-horizon planning for GUI agents.
2. Related Work
GUI Agents.Early efforts adapted foundation models (GPT-
4, GPT-4o) to GUI tasks (Wen et al., 2024; Wang et al.,
2023), with Zhenget al. (Zheng et al., 2024) demonstrating
that GPT-4V outperforms text-based models in web sce-
narios. Zhanget al. (Zhang et al., 2025) augment GPT-4V
with a memory module for historical actions. Subsequent
work explored modular frameworks: Wanget al. (Wang
et al., 2024a) integrate planning, decision, and reflection
modules; Zhanget al. (Zhang et al., 2024b) propose multi-
agent collaboration; and Zhuet al. (Zhu et al., 2024) design
a hierarchical planner-executor architecture. However, these
cloud-based frameworks incur high API costs and latency,
and suffer from hallucinations due to limited GUI domain
knowledge. More recent work pursues end-to-end GUI
agents via parameter training. Chenget al. (Cheng et al.,
2024) train a dedicated GUI grounding model with cross-
platform data, while UI-TARS (Qin et al., 2025) introduces
a comprehensive pre-training to fine-tuning pipeline. To
improve generalization, Luoet al. (Luo et al., 2025) and Lu
et al. (Lu et al., 2025) apply rule-based RL algorithms such
as GRPO (Shao et al., 2024). AutoDroid-V2 (Wen et al.,
2025) fine-tunes a lightweight model to generate executable
scripts in one shot. Despite these advances, on-device mod-
els (≤3B) remain limited in reasoning, struggling with com-
plex multi-step tasks.
Knowledge-aware GUI Agents.To mitigate hallucina-
tions and improve adaptability, some works utilize historical
memory to guide task planning. Wanget al. (Wang et al.,
2024b) propose a workflow memory extracting reusable pat-
terns from past experiences. Mobile-Agent-E (Wang et al.,
2025) introduces a self-evolving framework accumulating
general guidance over time. MAGNET (Sun et al., 2026)
constructs dual-level memory for element grounding and
workflow retrieval to handle UI drift. However, these meth-
ods rely solely on LLMs’ contextual understanding without
accounting for dynamic environment interactions. Another
line of work focuses on reliable action generation. Auto-
Droid (Wen et al., 2024) collects transition knowledge via
random exploration. GUI-explorer (Xie et al., 2025) mines
element functionality by analyzing GUI state changes. KG-
RAG (Guan et al., 2025b) transforms UI Transition Graphs
into vector databases and distills reusable actions based on
intent. While these approaches improve action accuracy,
path generation still relies on LLM reasoning over retrieved
context rather than direct extraction from an executable
state machine. Moreover, massive API calls for step-wise
decision-making incur substantial costs and latency.
LLM-based Monte Carlo Tree Search.Inspired by Al-
phaGo, recent work explores guiding LLM inference with
tree search to improve reasoning on structured tasks. Zhou
et al. (Zhou et al., 2023) propose an LLM-MCTS frame-
work leveraging environment feedback for decision-making,
while Xieet al. (Xie et al., 2024) construct a self-learning
loop using MCTS to generate preference signals for train-
ing. However, these methods require multiple LLM rollouts
during simulation, limiting efficiency. More recent work
employs LLMs as both policy and value models. Haoet
al. (Hao et al., 2023) treat the LLM as a world model for
generation and evaluation. rStar-Math (Guan et al., 2025a)
trains a reward model with trajectory-level binary rewards
for node scoring. ReST-MCTS* (Zhang et al., 2024a) in-
troduces a self-trained Process Reward Model for step-wise
evaluation, and Mendeset al. (Mendes & Ritter, 2025) equip
the value model with look-ahead capability. Despite these
advances, most methods rely on heuristic value designs with-
out theoretical guarantees and require separate policy and
value models, incurring high computational overhead.
3. Problem Statement
GUI Logic Knowledge Graph.We define the GUI Logic
Knowledge Graph as a directed graphG= (S,A,E) , where
S denotes state nodes representing unique GUI pages, A
denotes action nodes representing executable operations,
and E ⊆(S × A)∪(A × S)denotes edges connecting
states to actions and actions to resulting states. Each state
s∈ Scontains a page descriptionds, and each actiona∈ A
is annotated with a functional description fa. We denote
A(s) ={a∈ A: (s, a)∈ E}as the available actions ats.
Path Extraction as Finite-Horizon MDP.Given a user
instruction x∈ X, we formulate path extraction from the
KG as a finite-horizon episodic MDP, ⟨S,A, T, R, H⟩. The
2

## Page 3

Executable Agentic Memory for GUI Agent
state space S and action space A(s) are induced by the KG
structure. T represents a deterministic transition function
where s′ =T(s, a) follows the KG edges. R is a binary
terminal reward function, where R(sH, x) = 1if terminal
state sH satisfies instruction x, and 0 otherwise. H is the
horizon. At each step t, the agent selects at ∈ A(st) ac-
cording to policy π(·|st, x)and transits to st+1 =T(s t, at).
The objective is to find π∗ = arg maxπ Eat∼π[R(sH, x)]
that identifies a successful pathτ ∗ for instructionx.
4. Methodology
In this section, we introduce our proposed agentic mem-
ory system which comprises two main components: 1) Of-
fline Knowledge Graph Construction, which autonomously
explores the GUI environment to collect transition data
and builds a structured knowledge graph G; and 2) On-
line Knowledge-Augmented Reasoning, which leverages
the constructed KG to extract faithful execution paths via
Q-model guided MCTS. An overview of the framework is
presented in Fig. 1. We elaborate on each component in the
following subsections.
4.1. Offline Knowledge Graph Construction
The offline stage aims to construct a comprehensive GUI
Logic Knowledge Graph G= (S,A,E) that captures both
the structural logic and semantic knowledge of the target
GUI environment. This process consists of three key com-
ponents: autonomous exploration for trajectory collection,
transition-aware knowledge mining for graph construction,
and action group mining for efficient high-level guidance.
Autonomous Exploration.The core of our offline stage
lies in task-oriented autonomous exploration that systemat-
ically discovers GUI states and transitions contributing to
task completion. We propose an element-grounded hierar-
chical exploration based on depth-first search (DFS). Given
a task goal g, we extractExploration Anchorsfrom the cur-
rent GUI state—interactable elements serving as structural
primitives for sub-goal generation. The MLLM uses these
anchors to generate up to k candidate sub-goals ranked by
their likelihood of progressing toward g. At each depth,
the agent evaluates progress and determines one of three
outcomes: (1) CONTINUE—the sub-goal was achieved but
g requires further operations; (2) BACKTRACK—the current
state deviates from the path toward g; (3) COMPLETE—the
task goal g is achieved. This DFS-based design ensures
comprehensive coverage of task-relevant transitions (up to
O(kd) distinct trajectories) while the collected trajectories
naturally form a prefix tree structure that can be seamlessly
transformed into the knowledge graphG.
Transition-aware Knowledge Mining.The knowledge
construction process builds a structured KG from collected
exploration trajectories. Let ξ=⟨s 0, a0, s1, a1, . . . , sn⟩
denote an interaction trajectory. Following (Wen et al.,
2025; Xie et al., 2025), we extract transition-aware GUI
knowledge by analyzing consecutive transitions to construct
the graph structure and enrich semantic attributes.
1) Graph Structure Construction:The KG is constructed
as a Directed Acyclic Graph (DAG) where state nodes and
action nodes alternate, with each trajectory incrementally
merged into the KG. The key challenge lies in accurately
mapping new trajectories to the existing state space. To
this end, we design a state-aware deduplication mechanism
featuring dual-layer filtering:(i) Coarse Filtering—each
new state is encoded by an embedding model and matched
against existing states via similarity retrieval;(ii) Fine-
grained Filtering—candidate duplicates are verified by a
Vision-Language Model for rigorous semantic comparison.
For duplicate states, we further perform element-level dedu-
plication via IoU of bounding boxes, effectively connecting
discrete exploration trajectories into a cohesive graph.
2) Semantic Knowledge Enrichment:Once the topological
structure is established, we enrich the graph with semantic
attributes derived from state transitions. The knowledge
mining process is formalized as:
G ← G ⊕ Fextract(st, at, st+1)(1)
where Fextract : (st, at, st+1)7→(d st, dst+1 , fat) generates
page descriptions and action functional descriptions from
the state transition, and ⊕ denotes the merge operator that
continuously updates the extracted knowledge intoG.
Action Group Mining.Beyond atomic actions, real-world
GUI tasks often involve recurring multi-step action patterns.
While recent works extract high-level actions from trajecto-
ries (Jiang et al., 2025; Wang et al., 2025), they rely heavily
on LLMs to summarize these groups, suffering from poor
cross-task generalizability and high computational cost.
To address these limitations, we propose a statistical ap-
proach inspired by Byte Pair Encoding (BPE). We conceptu-
alize the KG as a “path heatmap,” where high-frequency ac-
tion subsequences represent high-value generalizable skills.
Formally, let V={a 1, a2, . . . , aM } denote the initial vo-
cabulary of atomic actions, and let P={τ 1, τ2, . . . , τK}
denote the corpus of all historical paths in the KG, where
each path τ= (a i1 , ai2 , . . . , aiL) is a sequence of atomic
actions.
The mining process proceeds iteratively. At each iteration j,
we compute the frequency of all adjacent action pairs and
identify the most frequent pair:
(a∗, a′∗) = arg max
(a,a′)∈V×V
X
τ∈P
count((a, a′), τ)(2)
3

## Page 4

Executable Agentic Memory for GUI Agent
Offline Exploration 
Inference
Task-oriented 
DFS Exploration
Tasks
-Turn on Bluetooth
-Turn off WIFI
-Open WIFI Config
…
Sub-goals
Execution
Trajectory
     Data
Knowledge Graph with Action Group Mining 
BPE-based 
Action Merging
Open Connection 
     Preference
Open 
Network
Click 
Bluetooth
Toggle On
Toggle Off
Open WIFI 
  Settings
Open Config
Disable WIFI
Navigate To 
Bluetooth Page
Navigate To 
WIFI Settings
CONTINUE BACKTRACK
Knowledge  Graph 𝑮
Expected State
Deviated State
Unexplored State
Page Node Atomic action Node
 Action Group Node
Exploration Tasks
MCTS on 
Graph
𝑄1,1 𝑄1,2
𝑄2,2𝑄2,1
𝑄3,1 𝑄3,2 𝑄3,3 𝑄3,4
𝑄4,1 𝑄4,2 𝑄4,3
෡𝑸𝟑,𝟏 = 𝟎 ෡𝑸𝟑,𝟒 = 𝟎
෡𝑸𝟑,𝟐 = 𝟏
෡𝑸𝟒,𝟏 = 𝟏
෡𝑸𝟑,𝟑 = 𝟎.𝟓
෡𝑸𝟒,𝟏 = 𝟏෡𝑸𝟒,𝟐 = 𝟎
෡𝑸𝟐,𝟏 = 𝟎.𝟓 ෡𝑸𝟐,𝟐 = 𝟎.𝟐𝟓
෡𝑸𝟏,𝟐 = 𝟎.𝟐𝟓෡𝑸𝟐,𝟏 = 𝟎.𝟓
在此处键入公式。
Update
Self-training Pipeline 
Q-value Guided   
        MCTS
Instruction input
“Turn on Bluetooth 
and enable WIFI”
Navigate 
          to … 
Toggle 
         on
…
𝜏∗
Filtering 
& Replace
Executable 
  Task Plan
Execute
Q-model
Soft BCE
Navigate 
      to WIFI… 
Figure 1.Overview of Executable Agentic Memory (EAM). It comprises offline automatic memory construction and inference-time
executable memory reuse guided by a trained Q-model.
where count((a, a′), τ)denotes the number of occurrences
of the adjacent pair (a, a′) in path τ. If the maximum fre-
quency exceeds a predefined threshold δf , we merge the
pair into a new action group and update the vocabulary:
a(j)
new =a ∗ ◦a ′∗,V ← V ∪ {a(j)
new}.(3)
The corpus P is then updated by replacing all occurrences of
(a∗, a′∗) with a(j)
new. This process iterates until the frequency
of the most common pair falls below δf . The mined action
groups are integrated into the KG as high-level action nodes,
extending the action space from atomic operations to multi-
step reusable skills.
4.2. Online Knowledge-Augmented Path Extraction
Given a user instruction x, extracting an executable path
from the KG can be formulated as the finite-horizon MDP
defined in Section 3. This MDP features deterministic tran-
sitions, binary terminal rewards, and a relatively small state-
action space constrained by the KG structure. Such a tabular
setting differs fundamentally from classical agentic RL sce-
narios, which typically involve complex reward structures
and vocabulary-scale action spaces. Due to this structural
mismatch, directly employing mainstream GRPO-style RL
frameworks (Shao et al., 2024; Feng et al., 2025; Jin et al.,
2025) is suboptimal, as they easily suffer from entropy col-
lapse and introduce unnecessary computational overhead.
To address this challenge, we introduce apath navigat-
ing agentthat leverages Monte Carlo Tree Search (MCTS)
guided by a lightweight Q-model to extract executable paths
from the KG. Unlike generative agents that map generated
tokens into the graph, our agent explicitly operates on the
graph topology and treats reasoning as planning over dis-
crete states and actions. This design offers three key advan-
tages. First, by constraining the action space to valid edges
in G, the agent naturally decouples graph reasoning from
semantic generation and treats the KG as a rigorous state
machine. Second, the agent automatically generates step-
level Q-value annotations through MCTS rollouts, which
obviates the need for human-labeled training data. Third,
instead of fine-tuning a generative model over a vast vocabu-
lary, the agent relies on a compact Q-model to predict scalar
values, which significantly reduces computational cost.
Our path navigating agent consists of three components: Q-
model guided MCTS framework, random policy valuation
for node evaluation, and a self-training pipeline for iterative
model refinement.
Q-model Guided MCTS.The agent performs tree search
on the KG starting from a root node h0 = (x, s0), which
encodes the instruction x and initial state s0. Each node
4

## Page 5

Executable Agentic Memory for GUI Agent
ht = (st, at) in the search tree corresponds to a state-action
pair. The search proceeds through four MCTS phases:
1) Selection:The agent traverses the tree by selecting child
nodes according to the UCT criterion until reaching a leaf
node:
UCT(s, a) =Q(s, a) +c
s
lnN(s)
N(s, a) (4)
where Q(s, a)is the estimated Q-value, N(s, a)the visit
count, andcthe exploration constant.
2) Expansion:Upon reaching a non-terminal leaf state sl,
the agent expands all available actions a∈ A(sl) as child
nodes.
3) Evaluation:Unlike standard MCTS with random roll-
outs, the agent queries its Q-model to initialize Q-values:
Q(sl, a)←Qθ(sl, a), where Qθ(s, a)∈(0,1) predicts the
task success probability.
4) Back-propagation:The agent propagates Q-values back
to the root, updating visit counts and Q-estimates along the
path via incremental averaging.
N(st, at)←N(s t, at) + 1
Q(st, at)←Q(s t, at) + Q(sl, al)−Q(s t, at)
N(st, at) .(5)
After M iterations, the top-K paths with the highest mean
Q-values are extracted and processed by a cloud-based LLM
for one-time filtering and parameter replacement into the
final executable plan.
Random Policy Valuation.To effectively guide the search,
the agent’s Q-model should not only identify superior ac-
tions but also quantify the likelihood of success after select-
ing each action. Most existing MCTS frameworks employ
Outcome Reward Models (ORM) that assign binary val-
ues (Cobbe et al., 2021). Such coarse signals overlook the
nuanced differences among intermediate steps.
Instead, we define the Q-value as the expected success prob-
ability under a uniform random policy πu(a|s) = 1/|A(s)|.
This value can be computed via the Bellman equation:
Qπu(s, a) =r(s, a) + 1
|A(s′)|
X
a′∈A(s′)
Qπu(s′, a′).(6)
s′ =T(s, a) is the successor state, and r(s, a)∈ {0,1}
is the terminal reward. The value Qπu(s, a)represents the
probability of reaching a successful terminal state when
starting from (s, a)and acting uniformly at random there-
after. When Qπu(s, a) = 0, no feasible path exists from
(s, a)to success, whereas higher values indicate greater
likelihood of task completion. Crucially, recent theoretical
results have shown that acting greedily with respect to Qπu
achieves optimality in finite-horizon deterministic MDPs
with binary rewards (He et al., 2025; Laidlaw et al., 2023),
which aligns precisely with our KG setting.
Self-Training Pipeline.We train the agent’s Q-model Qθ
through an iterative self-training procedure consisting of an
initialization stage and a refinement stage.
1) Initialization:Directly deploying an untrained Q-model
leads to random exploration and severe label imbalance,
as the search predominantly encounters dead-end nodes
with zero Q-values. To address this cold-start problem,
we initialize Qθ using preference learning on an existing
GUI dataset. For each step t along an expert trajectory,
we construct preference pairs with the expert action a+
t as
positive and a randomly sampled a−
t ∈ A(st)\ {a+
t } as
negative. The agent is trained with a pairwise ranking loss
based on the Bradley-Terry model:
Linit(θ) =−E (τ+
t ,τ−
t )∼Dinit

R(τ+
t , τ−
t )

(7)
whereR(τ +
t , τ−
t ) = logσ(Q θ(st, a+
t )−Q θ(st, a−
t )).
2) Iterative Refinement:After initialization, the agent itera-
tively refines its Q-model using self-generated data. In each
round, the agent samples instructions and executes MCTS
guided by the current Qθ to construct search trees, then
computes target Q-values via bottom-up Bellman backup:
ˆQ(s, a)←r(s, a) + 1
|A(s′)|
X
a′∈A(s′)
ˆQ(s′, a′).(8)
Since Q-values represent probabilities in[0,1] , we formulate
the optimization as binary classification with soft labels:
Lupdate(θ) =−E
(s,a)∼T
h
ˆQlogp θ + (1− ˆQ) log(1−p θ)
i
(9)
where pθ =σ(Q θ(s, a))and T denotes state-action pairs
from the search trees. Through this iterative process, the
agent progressively improves its ability to identify promis-
ing paths within the KG.
5. Theoretical Analysis
In this section, we provide theoretical guarantees for the
proposed Q-model guided MCTS framework. We first for-
malize the problem setting, then present our two main re-
sults: (1) a bias consistency guarantee ensuring the learned
Q-model is close to Qπu on critical states, and (2) a sample
complexity bound for extracting the optimal path.
5.1. Problem Setting
We analyze path extraction onG under the MDP formulation
from Section 3. Proposition 5.1 formalizes the optimality
guarantee of the greedy policy with respect toQ πu.
5

## Page 6

Executable Agentic Memory for GUI Agent
Algorithm 1Self-Training for Path-Navigating Agents
Input:Instruction dataset D, initialization dataset Dinit,
knowledge graphG
Output:Trained Q-modelQ θ
▷Model Initialization
Construct preference pairs(τ +
t , τ−
t )fromD init
InitializeQ θ by minimizing ranking lossL init (Eq. 7)
▷Iterative Refinement via MCTS
foreach roundr= 1,2, . . . , Rdo
Sample instruction batchBfromD
T ← ∅
foreach instructionx∈ Bdo
Execute MCTS guided by Qθ on G to construct
search tree
Compute ˆQ(s, a)for all nodes (Eq. 8)
T ← T ∪ {(s, a,ˆQ(s, a))}
end for
UpdateQ θ by minimizingL update (Eq. 9)
end for
Return:Q θ
Proposition 5.1(Optimality of Greedy Policy (He et al.,
2025)).Consider the KG-induced MDP with deterministic
transitions, tree-structured state space, and binary termi-
nal rewards r∈ {0,1}. Let πu be the uniform policy and
Qπu its corresponding Q-function. Define the greedy pol-
icy πgreedy(s) = arg maxa∈A(s) Qπu(s, a). Then πgreedy is
optimal.
Let τ∗ = (s∗
0, a∗
0, . . . , s∗
H−1, a∗
H−1) denote an optimal path
induced by πgreedy. Define thecritical set C as the collection
of state-actions that must be ranked correctly to recover τ∗:
C=
H−1[
t=0
{(s∗
t , a) :a∈ A(s∗
t )}.(10)
Let |C|=H·max s |A(s)|. Define the minimum action gap
along the optimal path:
∆∗
min := min
t∈{0,...,H−1}

Qπu(s∗
t , a∗
t )−max
a̸=a∗
t
Qπu(s∗
t , a)

.
(11)
We train Qθ using target values computed via uniform Bell-
man backup (Eq. 8) and perform MCTS at inference to
extract the optimal path.
5.2. Main Results
Next, we give the bias consistency guarantee on the critical
set.
Theorem 5.2(Bias Consistency on C).With probability at
least1−δ, the learned predictorQ θ satisfies
∥Qθ −Q πu∥2,ρC ≤ϵ bias(m, δ)(12)
where
ϵbias(m, δ) :=
r
1
2 (ϵapprox + 2εgen(m, δ/2) +ϵopt).
(13)
ϵapprox is the in-class approximation error, εgen(m, δ)is
the generalization error depending on m and Rademacher
complexity, andϵ opt is the optimization error.
Theorem 5.2 shows that the proxy error decreases as training
samples increase. This bias bound directly controls the
accuracy of MCTS node evaluation: when ϵbias <∆ ∗
min/2,
the learned Q-model preserves correct action rankings on
the critical set (see Appendix A.1 for details).
Our second main result establishes the sample complexity
for optimal path extraction.
Theorem 5.3(Sample Complexity for Optimal Path Ex-
traction).Suppose ϵbias(m, δ/2)<∆ ∗
min/2. Let ∆eff :=
∆∗
min −2ϵ bias >0 and K= max s |A(s)|. Then for the
greedy path ˆat = arg maxa ¯Qn(s∗
t , a)to coincide with τ∗
with probability at least 1−δ , the number of MCTS simula-
tions per node must satisfy
n≥ 32(K−1)c 2 ln(Hn/δ)
∆2
eff
+ 2(K−1)

2N0 + π2
3

(14)
yielding total complexity Ntotal =O

HKc2 ln(Hn/δ)
(∆∗
min−2ϵbias)2

+
O(HKN 0), where c is the UCT exploration constant and
N0 is a burn-in threshold.
Theorem 5.3 shows that the simulation complexity scales
polynomially with horizon H, branching factor K, and in-
versely with the squared effective action gap. This provides
a theoretical foundation for the efficiency of our approach:
as the Q-model improves (reducingϵbias), fewer MCTS sim-
ulations are needed to recover the optimal path. Complete
proofs are provided in Appendix A.2.
6. Experiment
In this section, we will present the results of our empirical
study to answer the following question:
• How does our proposed method perform on standard GUI
benchmarks compared to both on-device and cloud-based
baselines in terms of success rate and efficiency?
• Does our self-training pipeline enable stable iterative
performance improvements and exhibit theoretically ex-
pected properties?
• How do the various components in our method affect
performance, and does the trained Q-model demonstrate
cross-environment generalization?
6

## Page 7

Executable Agentic Memory for GUI Agent
Method Type Input AndroidWorld (%) MobileMiniWob++ (%) DroidTask (%)
GPT-4o GPT-4o SoM 34.5 56.5 57.0
Qwen 2.5-VL-3B Qwen 2.5-VL-3B SoM 2.6 32.6 13.3
UI-TARS-2B UI-TARS-2B screen 6.9 31.5 34.8
UI-TARS-7B UI-TARS-7B screen 33.0 53.3 55.0
M3A GPT-4o SoM 40.5 68.5 72.2
AutoDroid-V2 Llama-3-8B-ft SoM 26.0 53.3 54.4
AppAgentX GPT-4o SoM 62.5 72.8 88.6
GUI-Explorer GPT-4o SoM 47.4 80.4 88.0
EAM (Ours) GPT-4o, Qwen2.5-3B-instruct-ft SoM52.6 76.1 86.1
Table 1.Success rate (%) comparison between our method and baselines on AndroidWorld, MobileMiniWob++, and DroidTask
benchmarks. “SoM” refers to Set-of-Mark prompting, which utilizes the bounding boxes recorded in the accessibility tree to annotate UI
elements with numerical labels in screenshots. All results are averaged over three independent runs.
Method Latency (s) API Tokens Cost (K)
GPT-4o 9.3 50.8
Qwen2.5-VL-3B 7.7 -
UI-TARS-2B 6.0 -
UI-TARS-7B 8.8 32.7
M3A 16.9 62.6
AutoDroid-V2 2.1 -
AppAgentX 16 6.2
GUI-Explorer 66.4 73.1
EAM (Ours)2.8 8.3
Table 2.Efficiency comparison between EAM and baselines in
terms of latency and token cost. “Latency (s)” denotes the average
execution time per step. “API Tokens Cost (K)” indicates the total
token consumption (in thousands) per step for LLM API calls. “-”
indicates that the method uses locally deployed models without
API calls.
6.1. Experimental Setup
Benchmarks.We evaluate the effectiveness and efficiency
our method on three benchmarks: AndroidWorld (Rawles
et al., 2024) (116 tasks across 20 real-world apps), Mo-
bileMiniWob++ (Rawles et al., 2024) (92 web tasks), and
DroidTask (Wen et al., 2024) (158 tasks across 13 apps).
Baselines.For on-device agents, we consider four baselines:
1) Qwen2.5-VL-3B, the vanilla VLM for on-device deploy-
ment; 2) UI-TARS-2B (Qin et al., 2025), the lightweight
SFT version of UI-TARS-7B; 3) UI-TARS-7B (Qin et al.,
2025), a SOTA GUI agent model; 4) AutoDroid-V2 (Wen
et al., 2025), a code-generation agent fine-tuned on Llama-
3-8B that produces executable scripts for one-shot task ex-
ecution. For cloud-based and knowledge-enhanced agents,
we consider: 1) GPT-4o, the base VLM for cloud-based
agents; 2) M3A (Rawles et al., 2024), a SOTA ReAct-
based agent framework; 3) AppAgentX (Jiang et al., 2025),
which extracts and reuses high-level actions from GUI tran-
sitions for task guidance; 4) GUI-Explorer (Xie et al., 2025),
an exploration-augmented framework that collects trajecto-
ries, extracts element-wise knowledge, and uses RAG for
decision-making.
Implementation.Our framework is implemented as a plug-
and-play module built on UI-TARS-2B, which serves as
a local action executor following memory-grounded plan-
ning. We use GPT-4o for task-oriented exploration and
knowledge mining. The knowledge base is constructed with
Neo4j for app-wise knowledge graphs and Pinecone for
screenshot embeddings. We fine-tune Qwen2.5-Instruct for
path extraction with three model sizes: 0.5B, 1.5B, and 3B.
For Q-value estimation, we append a value head to output
scalar predictions. The self-training pipeline runs for four
rounds. All training is conducted on 4×A800-80GB GPUs,
and inference experiments are performed on a single RTX
4090-16GB to simulate on-device deployment.
6.2. Experimental Results
Comparative results.Table 1 reports success rates on
the three benchmarks. Our method achieves52.6%on
AndroidWorld,76.1%on MobileMiniWob++, and86.1%
on DroidTask, surpassing all on-device baselines by sig-
nificant margins (+19.6, +22.8, and +31.1, respectively).
Notably, despite utilizing a 3B model for path extraction,
our method substantially outperforms GPT-4o based M3A
(+7.6, +13.9, and +29.1) and achieves performance compa-
rable to knowledge-enhanced agents like AppAgentX and
GUI-Explorer. These gains indicate that grounding decision-
making in a structured knowledge graph effectively bridges
the reasoning gap between small language models and fron-
tier LLMs. Table 2 demonstrates that our approach achieves
an average latency of2.8 sand token cost of8.3Kper step.
This efficiency stems from our plan-then-execute frame-
work: unlike cloud-based agents requiring massive iterative
API calls, our method necessitates only a single API call to
filter the extracted paths, reducing token cost by approxi-
mately 6× compared to GPT-4o (50.8K). While AutoDroid-
V2 also adopts plan-then-execute to achieve low latency
7

## Page 8

Executable Agentic Memory for GUI Agent
(2.1 s), its performance suffers due to a lack of rigorous
knowledge guidance during inference.
Substantial improvement through self-training.To an-
swer Q.2, we analyze performance gains through iterative
self-training. As shown in Fig. 2a–2b, all three model sizes
(0.5B, 1.5B, and 3B) exhibit consistent improvement on
both AndroidWorld and DroidTask as self-training rounds
increase. Notably, the 3B model achieves the most sub-
stantial gains. Fig. 2c–2d further shows the value gap be-
tween optimal and suboptimal actions on critical paths: as
self-training progresses, the model develops more accurate
value estimates, enabling better separation of optimal ac-
tions. The initially negative or near-zero margins in early
rounds indicate that the untrained model struggles to distin-
guish optimal actions, while later rounds show increasingly
positive margins, demonstrating improved discriminative
ability. This aligns with our theoretical analysis bounding
path extraction ability by sample size and value estimation
quality: as ϵbias decreases through training, the effective
action gap ∆eff = ∆∗
min −2ϵ bias increases, requiring fewer
MCTS simulations to recover optimal paths (Theorem 5.3).
/uni00000013/uni00000014/uni00000015/uni00000016/uni00000017
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047
/uni00000015/uni00000018
/uni00000016/uni00000013
/uni00000016/uni00000018
/uni00000017/uni00000013
/uni00000017/uni00000018
/uni00000018/uni00000013
/uni00000018/uni00000018/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c
/uni00000013/uni00000011/uni00000018/uni00000025
/uni00000014/uni00000011/uni00000018/uni00000025
/uni00000016/uni00000025
(a)AndroidWorld-SR
/uni00000013/uni00000014/uni00000015/uni00000016/uni00000017
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047
/uni00000016/uni00000013
/uni00000017/uni00000013
/uni00000018/uni00000013
/uni00000019/uni00000013
/uni0000001a/uni00000013
/uni0000001b/uni00000013
/uni0000001c/uni00000013/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c
/uni00000013/uni00000011/uni00000018/uni00000025
/uni00000014/uni00000011/uni00000018/uni00000025
/uni00000016/uni00000025
 (b)DroidTask-SR
/uni00000013/uni00000014/uni00000015/uni00000016/uni00000017
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047
/uni00000015
/uni00000013
/uni00000015
/uni00000017
/uni00000019
/uni0000001b
/uni00000032/uni00000053/uni00000057/uni0000004c/uni00000050/uni00000044/uni0000004f/uni00000003/uni00000024/uni00000046/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni00000030/uni00000044/uni00000055/uni0000004a/uni0000004c/uni00000051/uni00000003/uni0000000b×10 2/uni0000000c
/uni00000013/uni00000011/uni00000018/uni00000025
/uni00000014/uni00000011/uni00000018/uni00000025
/uni00000016/uni00000025
(c)AndroidWorld-Gap
/uni00000013/uni00000014/uni00000015/uni00000016/uni00000017
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047
/uni00000013
/uni00000014
/uni00000015
/uni00000016
/uni00000017
/uni00000018
/uni00000032/uni00000053/uni00000057/uni0000004c/uni00000050/uni00000044/uni0000004f/uni00000003/uni00000024/uni00000046/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni00000030/uni00000044/uni00000055/uni0000004a/uni0000004c/uni00000051/uni00000003/uni0000000b×10 2/uni0000000c
/uni00000013/uni00000011/uni00000018/uni00000025
/uni00000014/uni00000011/uni00000018/uni00000025
/uni00000016/uni00000025
 (d)DroidTask-Gap
Figure 2.Self-training dynamics: (a-b) Success rate and (c-d)
optimal action margin across rounds.
Ablation Study and Cross-Environment Generalization.
Fig. 3 quantifies the contribution of each component. Start-
ing from the Baseline (UI-TARS-2B without KG guidance),
introducing the knowledge graph with an initialization-
trained model (+KB w/ init model) yields substantial gains,
demonstrating the value of structured knowledge. Training
the Q-model in-environment (+In-env Model) achieves the
best performance, confirming that domain-specific train-
ing further refines value estimates. Notably, replacing
with a cross-environment trained model (+Cross-env Model,
trained on AndroidWorld) also improves performance on
DroidTask and MobileMiniWob++, despite never seeing
these environments during training. This addresses Q.3: the
learned value estimation captures transferable knowledge
about GUI navigation patterns, enabling reliable path ex-
traction in unseen scenarios. While in-environment training
remains optimal, cross-environment results suggest a well-
trained Q-model can serve as strong initialization for new
environments.
/uni00000025/uni00000044/uni00000056/uni00000048/uni0000004f/uni0000004c/uni00000051/uni00000048/uni0000000e/uni00000003/uni0000002e/uni00000025/uni00000003/uni0000005a/uni00000012
/uni0000004c/uni00000051/uni0000004c/uni00000057/uni00000003/uni00000050/uni00000052/uni00000047/uni00000048/uni0000004f
/uni0000000e/uni00000003/uni00000026/uni00000055/uni00000052/uni00000056/uni00000056/uni00000010/uni00000048/uni00000051/uni00000059
/uni00000003/uni00000030/uni00000052/uni00000047/uni00000048/uni0000004f
/uni0000000e/uni00000003/uni0000002c/uni00000051/uni00000010/uni00000048/uni00000051/uni00000059
/uni00000030/uni00000052/uni00000047/uni00000048/uni0000004f
/uni00000013
/uni00000015/uni00000013
/uni00000017/uni00000013
/uni00000019/uni00000013
/uni0000001b/uni00000013
/uni00000014/uni00000013/uni00000013/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c
(a)DroidTask
/uni00000025/uni00000044/uni00000056/uni00000048/uni0000004f/uni0000004c/uni00000051/uni00000048/uni0000000e/uni00000003/uni0000002e/uni00000025/uni00000003/uni0000005a/uni00000012
/uni0000004c/uni00000051/uni0000004c/uni00000057/uni00000003/uni00000050/uni00000052/uni00000047/uni00000048/uni0000004f
/uni0000000e/uni00000003/uni00000026/uni00000055/uni00000052/uni00000056/uni00000056/uni00000010/uni00000048/uni00000051/uni00000059
/uni00000003/uni00000030/uni00000052/uni00000047/uni00000048/uni0000004f
/uni0000000e/uni00000003/uni0000002c/uni00000051/uni00000010/uni00000048/uni00000051/uni00000059
/uni00000030/uni00000052/uni00000047/uni00000048/uni0000004f
/uni00000013
/uni00000015/uni00000013
/uni00000017/uni00000013
/uni00000019/uni00000013
/uni0000001b/uni00000013
/uni00000014/uni00000013/uni00000013/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c (b)MobileMiniWob++
Figure 3.Ablation study on agentic memory with different model:
cross-environment vs. in-environment trained models.
More experimental details, including analyses of training
loss curves, action groups, model size, and MCTS hyperpa-
rameters, can be found in the Appendix B.
7. Conclusion
This paper presents Executable Agentic Memory (EAM), a
structured knowledge graph that shifts GUI planning from
free-form generation to a robust retrieval-and-execution pro-
cess. Unlike prior knowledge-augmented approaches that
rely on LLM reasoning over retrieved context, EAM enables
agents to directly extract executable paths guaranteed to stay
on valid transitions. We propose a sample-efficient memory
construction pipeline and a value-guided MCTS framework
with theoretical guarantees for reliable path extraction. Ex-
perimental results across three benchmarks demonstrate
significant improvements in both success rate and efficiency.
These findings show that treating the KG as an executable
state machine, rather than a retrieval source for in-context
injection, enables reliable, efficient, and long-horizon GUI
automation.
Limitations.Our current framework assumes a relatively
static UI environment. When applications undergo signifi-
cant updates, the knowledge graph may become outdated.
Developing efficient incremental evolution mechanisms for
the knowledge graph to adapt to the frequently updating en-
vironments remains an important direction for future work.
Impact Statement
This paper presents Executable Agentic Memory (EAM),
a framework for improving the reliability and efficiency of
8

## Page 9

Executable Agentic Memory for GUI Agent
long-horizon GUI automation agents. If deployed respon-
sibly, such systems could reduce repetitive digital work,
improve productivity, and support accessibility by helping
users complete multi-step tasks in mobile and web applica-
tions. At the same time, GUI automation can be misused
for harmful purposes, including unauthorized actions, auto-
mated abuse of online services, and privacy-invasive data
collection. Our approach also raises privacy and security
considerations because building and using agent memory
may involve storing interaction traces or screenshots that
could contain sensitive information. To mitigate these risks,
we recommend deployments incorporate explicit user con-
sent, least-privilege access, careful handling and redaction
of stored artifacts, and monitoring/auditing of automated
actions. We encourage future work on safety constraints for
high-risk operations and privacy-preserving mechanisms for
agent memory.
References
Cheng, K., Sun, Q., Chu, Y ., Xu, F., Li, Y ., Zhang, J., and
Wu, Z. Seeclick: Harnessing gui grounding for advanced
visual gui agents.arXiv preprint arXiv:2401.10935, 2024.
Cheng, W., Ni, E., Wang, W., Sun, Y ., Liu, J., Shen, W.,
Chen, Y ., Shi, B., and Wang, D. Mga: Memory-driven gui
agent for observation-centric interaction.arXiv preprint
arXiv:2510.24168, 2025.
Cobbe, K., Kosaraju, V ., Bavarian, M., Chen, M., Jun, H.,
Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano,
R., et al. Training verifiers to solve math word problems.
arXiv preprint arXiv:2110.14168, 2021.
Feng, L., Xue, Z., Liu, T., and An, B. Group-in-group
policy optimization for llm agent training.arXiv preprint
arXiv:2505.10978, 2025.
Gou, B., Wang, R., Zheng, B., Xie, Y ., Chang, C., Shu,
Y ., Sun, H., and Su, Y . Navigating the digital world as
humans do: Universal visual grounding for gui agents.
arXiv preprint arXiv:2410.05243, 2024.
Guan, X., Zhang, L. L., Liu, Y ., Shang, N., Sun, Y ., Zhu, Y .,
Yang, F., and Yang, M. rstar-math: Small llms can master
math reasoning with self-evolved deep thinking.arXiv
preprint arXiv:2501.04519, 2025a.
Guan, Z., Li, J. C. L., Hou, Z., Zhang, P., Xu, D., Zhao,
Y ., Wu, M., Chen, J., Nguyen, T.-T., Xian, P., et al. Kg-
rag: Enhancing gui agent decision-making via knowledge
graph-driven retrieval-augmented generation. InProceed-
ings of the 2025 Conference on Empirical Methods in
Natural Language Processing, pp. 5396–5405, 2025b.
Hao, S., Gu, Y ., Ma, H., Hong, J., Wang, Z., Wang, D., and
Hu, Z. Reasoning with language model is planning with
world model. InProceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing, pp.
8154–8173, 2023.
He, H., Ye, Y ., Cai, Q., Hu, C., Jiao, B., Jiang, D., and Pan,
L. Random policy valuation is enough for llm reasoning
with verifiable rewards.arXiv preprint arXiv:2509.24981,
2025.
Jiang, W., Zhuang, Y ., Song, C., Yang, X., Zhou, J. T.,
and Zhang, C. Appagentx: Evolving gui agents as profi-
cient smartphone users.arXiv preprint arXiv:2503.02268,
2025.
Jin, B., Zeng, H., Yue, Z., Yoon, J., Arik, S., Wang, D.,
Zamani, H., and Han, J. Search-r1: Training llms to
reason and leverage search engines with reinforcement
learning.arXiv preprint arXiv:2503.09516, 2025.
Kocsis, L. and Szepesv ´ari, C. Bandit based monte-carlo
planning. InEuropean conference on machine learning,
pp. 282–293. Springer, 2006.
Laidlaw, C., Russell, S. J., and Dragan, A. Bridging rl
theory and practice with the effective horizon.Advances
in Neural Information Processing Systems, 36:58953–
59007, 2023.
Li, R., Zhai, Y ., Xu, B., Xu, L., Shi, N., Zhang, W., Lin, R.,
and Wang, L. Echotrail-gui: Building actionable memory
for gui agents via critic-guided self-exploration.arXiv
preprint arXiv:2512.19396, 2025.
Lu, Z., Chai, Y ., Guo, Y ., Yin, X., Liu, L., Wang, H., Xiao,
H., Ren, S., Xiong, G., and Li, H. Ui-r1: Enhancing
efficient action prediction of gui agents by reinforcement
learning.arXiv preprint arXiv:2503.21620, 2025.
Luo, R., Wang, L., He, W., and Xia, X. Gui-r1: A general-
ist r1-style vision-language action model for gui agents.
arXiv preprint arXiv:2504.10458, 2025.
Mendes, E. and Ritter, A. Language models can self-
improve at state-value estimation for better search.arXiv
preprint arXiv:2503.02878, 2025.
Qin, Y ., Ye, Y ., Fang, J., Wang, H., Liang, S., Tian, S.,
Zhang, J., Li, J., Li, Y ., Huang, S., et al. Ui-tars: Pioneer-
ing automated gui interaction with native agents.arXiv
preprint arXiv:2501.12326, 2025.
Rawles, C., Clinckemaillie, S., Chang, Y ., Waltz, J., Lau,
G., Fair, M., Li, A., Bishop, W., Li, W., Campbell-
Ajala, F., et al. Androidworld: A dynamic benchmark-
ing environment for autonomous agents.arXiv preprint
arXiv:2405.14573, 2024.
9

## Page 10

Executable Agentic Memory for GUI Agent
Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang,
H., Zhang, M., Li, Y ., Wu, Y ., et al. Deepseekmath: Push-
ing the limits of mathematical reasoning in open language
models.arXiv preprint arXiv:2402.03300, 2024.
Sun, L., Zhang, J., Wang, S., and Wei, Z. Magnet: Towards
adaptive gui agents with memory-driven knowledge evo-
lution.arXiv preprint arXiv:2601.19199, 2026.
Wang, B., Li, G., and Li, Y . Enabling conversational in-
teraction with mobile ui using large language models.
InProceedings of the 2023 CHI Conference on Human
Factors in Computing Systems, pp. 1–17, 2023.
Wang, J., Xu, H., Jia, H., Zhang, X., Yan, M., Shen, W.,
Zhang, J., Huang, F., and Sang, J. Mobile-agent-v2: Mo-
bile device operation assistant with effective navigation
via multi-agent collaboration.Advances in Neural Infor-
mation Processing Systems, 37:2686–2710, 2024a.
Wang, Z., Xu, H., Wang, J., Zhang, X., Yan, M., Zhang, J.,
Huang, F., and Ji, H. Mobile-agent-e: Self-evolving
mobile assistant for complex tasks.arXiv preprint
arXiv:2501.11733, 2025.
Wang, Z. Z., Mao, J., Fried, D., and Neubig, G. Agent
workflow memory.arXiv preprint arXiv:2409.07429,
2024b.
Wen, H., Li, Y ., Liu, G., Zhao, S., Yu, T., Li, T. J.-J., Jiang,
S., Liu, Y ., Zhang, Y ., and Liu, Y . Autodroid: Llm-
powered task automation in android. InProceedings
of the 30th Annual International Conference on Mobile
Computing and Networking, pp. 543–557, 2024.
Wen, H., Tian, S., Pavlov, B., Du, W., Li, Y ., Chang, G.,
Zhao, S., Liu, J., Liu, Y ., Zhang, Y .-Q., et al. Autodroid-
v2: Boosting slm-based gui agents via code generation. In
Proceedings of the 23rd Annual International Conference
on Mobile Systems, Applications and Services, pp. 223–
235, 2025.
Wu, Q., Cheng, K., Yang, R., Zhang, C., Yang, J., Jiang,
H., Mu, J., Peng, B., Qiao, B., Tan, R., et al. Gui-actor:
Coordinate-free visual grounding for gui agents.arXiv
preprint arXiv:2506.03143, 2025.
Xie, B., Shao, R., Chen, G., Zhou, K., Li, Y ., Liu, J., Zhang,
M., and Nie, L. Gui-explorer: Autonomous exploration
and mining of transition-aware knowledge for gui agent.
arXiv preprint arXiv:2505.16827, 2025.
Xie, Y ., Goyal, A., Zheng, W., Kan, M.-Y ., Lillicrap, T. P.,
Kawaguchi, K., and Shieh, M. Monte carlo tree search
boosts reasoning via iterative preference learning.arXiv
preprint arXiv:2405.00451, 2024.
Zhang, C., Yang, Z., Liu, J., Li, Y ., Han, Y ., Chen, X.,
Huang, Z., Fu, B., and Yu, G. Appagent: Multimodal
agents as smartphone users. InProceedings of the 2025
CHI Conference on Human Factors in Computing Sys-
tems, pp. 1–20, 2025.
Zhang, D., Zhoubian, S., Hu, Z., Yue, Y ., Dong, Y ., and
Tang, J. Rest-mcts*: Llm self-training via process re-
ward guided tree search.Advances in Neural Information
Processing Systems, 37:64735–64772, 2024a.
Zhang, J., Zhao, C., Zhao, Y ., Yu, Z., He, M., and Fan, J.
Mobileexperts: A dynamic tool-enabled agent team in
mobile devices.arXiv preprint arXiv:2407.03913, 2024b.
Zheng, B., Gou, B., Kil, J., Sun, H., and Su, Y . Gpt-4v
(ision) is a generalist web agent, if grounded.arXiv
preprint arXiv:2401.01614, 2024.
Zhou, A., Yan, K., Shlapentokh-Rothman, M., Wang, H.,
and Wang, Y .-X. Language agent tree search unifies
reasoning acting and planning in language models.arXiv
preprint arXiv:2310.04406, 2023.
Zhu, Z., Tang, H., Li, Y ., Lan, K., Jiang, Y ., Zhou, H., Wang,
Y ., Zhang, S., Sun, L., Chen, L., et al. Moba: A two-level
agent system for efficient mobile task automation.arXiv
e-prints, pp. arXiv–2410, 2024.
10

## Page 11

Executable Agentic Memory for GUI Agent
A. Theoretical Proof
This appendix provides complete proofs of all theoretical results stated in Section 5. We organize the proofs following the
structure of the main text.
A.1. Proof of theorem 5.2
Classical MCTS with terminal rollouts produces node estimates that concentrate around their own expectations. In contrast,
we use a learned value model Qθ to guide tree search, which introduces additional bias that must be controlled. A necessary
condition for reliable navigation is that the proxy Qθ is consistent with the reference value Qπu on thecritical set C, so that
action rankings on the critical path are preserved. Thus, we first aim to control thebiasinduced by using a learned value
model. Specifically, for any critical pair(s, a)∈ C, we aim to bound
E
 ¯QN (s, a)

−Q πu(s, a)
,(15)
¯QN (s, a)denotes the MCTS estimate produced at inference time after N visits. The expectation is taken over the internal
randomness of MCTS. This bias control provides the interface to standard UCT/MCTS finite-sample analysis, where
¯QN (s, a)concentrates around its mean. Formally, for any(s, a)∈ C,
 ¯QN (s, a)−Qπu(s, a)
 ≤
 ¯QN (s, a)−E
 ¯QN (s, a)

+
E
 ¯QN (s, a)

−Q πu(s, a)
.(16)
The first term is the standard finite-sample deviation of MCTS and will be bounded by standard UCT/MCTS concentration
results. In this section, we focus on controlling the second term, which captures the bias induced by using a learned value
model. Such proxy bias can be further decomposed into two components:
•Target error (estimation noise).The target ˆQdeviates fromQ πu due to finite terminal rollouts.
• Learning/generalization error.The learned predictor Qθ deviates from the target mapping due to finite training
samples and optimization error.
Target Estimation:Let Z(s, a)∈[0,1] be the discounted terminal return obtained by rolling out from (s, a)to termination
underπ u. Then
E[Z(s, a)|s, a] =Qπu(s, a).(17)
Lemma A.1(Unbiasedness of Bellman Backup).Let the uniform-policy Bellman operator T for deterministic transitions
be
(T ˆQ)(s, a) =r(s, a) + 1
|A(s′)|
X
a′∈A(s′)
ˆQ(s′, a′)(18)
wheres ′ =T(s, a). If each child estimate is unbiased forQ πu, then the backed-up value is also unbiased.
Proof. Let s′ =T(s, a) denote the successor state under deterministic transition. Suppose for all a′ ∈ A(s′), the child
estimates satisfy
E[ ˆQ(s′, a′)] =Q πu(s′, a′).(19)
The backed-up value is
ˆQ(s, a) =r(s, a) +1
|A|
X
a′∈A(s′)
ˆQ(s′, a′).(20)
11

## Page 12

Executable Agentic Memory for GUI Agent
Taking expectations and using linearity:
E[ ˆQ(s, a)] =r(s, a) +γ1
|A|
X
a′∈A(s′)
E[ ˆQ(s′, a′)](21)
=r(s, a) +γ 1
|A|
X
a′∈A(s′)
Qπu(s′, a′)(22)
=r(s, a) +γEa′∼πu[Qπu(s′, a′)](23)
= (TQ πu)(s, a)(24)
=Q πu(s, a),(25)
where the last equality follows from the Bellman fixed-point equation forQ πu under policyπ u.
Given the target values of leaf nodes obtained by rolling out underπu, Lemma A.1 propagate Unbiasedness to the whole
tree. We can further bound the error between target values and the true values on the critical set.
Lemma A.2.Assume that every leaf-edge value contributing to ˆQ(s, a)for any (s, a)∈ Cis estimated by at least ntr
min
i.i.d. terminal rollouts underπ u, each bounded in[0,1]. Then with probability at least1−δ,
sup
(s,a)∈C
 ˆQ(s, a)−Qπu(s, a)
 ≤ϵ tr(δ) :=
s
ln(2|C|/δ)
2ntr
min
Proof. Fix (s, a)∈ C. Let Z1, Z2, . . . , Zn be the i.i.d. terminal rollout returns contributing to ˆQ, where n≥n tr
min. Each
Zi ∈[0,1]and by (17),E[Z i] =Q πu(s, a).
The target estimate is ˆQ= 1
n
Pn
i=1 Zi.
By Hoeffding’s inequality for bounded random variables:
Pr
 ˆQ−Q πu(s, a)
 ≥ϵ

≤2 exp
 
−2nϵ2
≤2 exp
 
−2ntr
minϵ2
.(26)
Settingϵ=
q
ln(2|C|/δ)
2ntr
min
, we obtain
Pr
 ˆQ−Q πu(s, a)
 ≥ϵ

≤ δ
|C| .(27)
Taking a union bound over all|C|pairs inC:
Pr
 
sup
(s,a)∈C
 ˆQ(s, a)−Qπu(s, a)
 ≥ϵ
!
≤ |C| ·δ
|C| =δ.(28)
Thus with probability at least1−δ, the stated bound holds.
Lemma A.2 shows that the target error bound is tightened as the number of samples increases.
Learning Error.We now relate the learning error of the Q-modelQ θ to the training sample size. LetS={(x i, yi)}m
i=1
be the training data, where xi = (si, ai) denotes a state-action pair and yi = ˆQ(si, ai)∈[0,1] is the corresponding target
value. We analyze the binary cross-entropy loss:
ℓ(p, y) =−ylogp−(1−y) log(1−p)(29)
For analysis, we restrict predictors to [τ,1−τ] for some τ∈(0,1/2) , solely to ensure ℓ(·, y)is Lipschitz with a finite
constantL:= 1/τ.
12

## Page 13

Executable Agentic Memory for GUI Agent
Define the expected and empirical risks underD:
R(Q) :=E (X,Y)∼D [ℓ(Q(X), Y)],(30)
ˆRS(Q) := 1
m
mX
i=1
ℓ(Q(xi), yi).
LetQbe the function class and ˆℜm(Q)the empirical Rademacher complexity on{x i}m
i=1.
Lemma A.3(Rademacher generalization bound).With probability at least1−δover the draw ofS,
sup
Q∈Q
R(Q)− ˆRS(Q)
 ≤2L ˆℜm(Q) + 3
r
ln(2/δ)
2m .(31)
Proof.The proof proceeds in four steps.
Step 1: Symmetrization.Let S={(x i, yi)}m
i=1 and S′ ={(x ′
i, y′
i)}m
i=1 be two independent samples from D. By
standard symmetrization arguments (see, e.g., Theorem 26.5 in Shalev-Shwartz & Ben-David, 2014):
ES

sup
Q∈Q

R(Q)− ˆRS(Q)

≤2E S,σ
"
sup
Q∈Q
1
m
mX
i=1
σiℓ(Q(xi), yi)
#
,(32)
whereσ 1, . . . , σm are i.i.d. Rademacher random variables (Pr(σi =±1) = 1/2).
Step 2: Lipschitz contraction.Since ℓ(·, y)is L-Lipschitz on [τ,1−τ] (with L= 1/τ ), and the Rademacher complexity
satisfies the contraction principle:
ES,σ
"
sup
Q∈Q
1
m
mX
i=1
σiℓ(Q(xi), yi)
#
≤L·E S,σ
"
sup
Q∈Q
1
m
mX
i=1
σiQ(xi)
#
=L ˆℜm(Q).(33)
Step 3: McDiarmid’s inequality.Define Φ(S) := sup Q∈Q

R(Q)− ˆRS(Q)

. Changing a single sample (xi, yi)
changesΦ(S)by at most 2∥ℓ∥∞
m ≤ 2
m (since losses are bounded when outputs are in[τ,1−τ]and labels in[0,1]).
By McDiarmid’s inequality:
Pr (Φ(S)−E[Φ(S)]≥t)≤exp

− 2t2
m·(2/m) 2

= exp

−mt2
2

.(34)
Settingt=
q
ln(2/δ)
2m and combining:
Pr
 
sup
Q∈Q

R(Q)− ˆRS(Q)

≥2L ˆℜm(Q) +
r
ln(2/δ)
2m
!
≤ δ
2.(35)
Step 4: Two-sided bound.Applying the same argument to ˆRS(Q)−R(Q) and taking a union bound yields the two-sided
result with probability 1−δ . The constant 3 (instead of 2) in the final bound accounts for technical refinements in the
symmetrization step.
We now convert the uniform bound into an excess-risk bound between the learned predictor and the best achievable predictor.
we assume approximate ERM:
13

## Page 14

Executable Agentic Memory for GUI Agent
ˆRS(Qθ)≤inf
Q∈Q
ˆRS(Q) +ϵ opt,(36)
whereϵ opt ≥0is the optimization error. Define the in-class optimal predictor
Q⋆
Q := arg min
Q∈Q
R(Q).(37)
Then we can have the excess risk bound.
Lemma A.4(Excess risk bound).On the event of Lemma A.3, we have
R(Qθ)− R(Q⋆
Q)≤2ε gen(m, δ) +ϵopt,(38)
where
εgen(m, δ) := 2Lˆℜm(Q) + 3
r
ln(2/δ)
2m .(39)
Proof.On the event of Lemma A.3, for allQ∈ Q:
R(Q)≤ ˆRS(Q) +ε gen,(40)
ˆRS(Q)≤ R(Q) +εgen.(41)
Now we bound the excess risk:
R(Qθ)− R(Q⋆
Q)≤ ˆRS(Qθ) +ε gen − R(Q⋆
Q)(by (40) applied toQ θ) (42)
≤inf
Q∈Q
ˆRS(Q) +ϵ opt +ε gen − R(Q⋆
Q)(by approximate ERM (36)) (43)
≤ ˆRS(Q⋆
Q) +ϵ opt +ε gen − R(Q⋆
Q)(sinceQ ⋆
Q ∈ Q) (44)
≤ R(Q⋆
Q) +ε gen +ϵ opt +ε gen − R(Q⋆
Q)(by (41) applied toQ ⋆
Q) (45)
= 2εgen +ϵ opt.(46)
In our context, the loss functionℓ(p, y)is a strictly proper scoring rule for Bernoulli distributions. Thus, we can use Pinsker’s
inequality to obtain the following direct link from risk to L2 error. Let Q†(x) :=E[Y|X=x] denote the true conditional
expectation under D. In our setting, because training targets are generated from terminal rollouts under πu and unbiased
Bellman backups (Lemma A.1), we haveQ †(x) =Q πu(x).
Lemma A.5.LetQ †(x) :=E[Y|X=x]denote the true conditional expectation underD. Then for any predictorQ,
EX∼D
h 
Q(X)−Q †(X)
2i
≤ 1
2
 
R(Q)− R
 
Q†
.
Proof. The proof proceeds in three steps: (i) express excess log-loss as KL divergence, (ii) apply Pinsker’s inequality, (iii)
specialize to Bernoulli distributions.
Step 1: Log-loss decomposition.For the log-loss ℓ(p, y) =−ylogp−(1−y) log(1−p) with p, y∈(0,1) , we have the
identity:
ℓ(p, y) =ℓ(y, y) + KL(Bern(y)∥Bern(p)),(47)
whereKL(Bern(y)∥Bern(p)) =ylog y
p + (1−y) log 1−y
1−p .
14

## Page 15

Executable Agentic Memory for GUI Agent
Verification:
ℓ(y, y) + KL(Bern(y)∥Bern(p))(48)
= [−ylogy−(1−y) log(1−y)] +

ylog y
p + (1−y) log 1−y
1−p

(49)
=−ylogy−(1−y) log(1−y) +ylogy−ylogp+ (1−y) log(1−y)−(1−y) log(1−p)(50)
=−ylogp−(1−y) log(1−p)(51)
=ℓ(p, y). (52)
Step 2: Pinsker’s inequality.The classical Pinsker’s inequality states that for any two probability distributions P and Q:
TV(P, Q)2 ≤ 1
2KL(P∥Q),(53)
whereTV(P, Q) = supA |P(A)−Q(A)|is the total variation distance.
Step 3: Specialization to Bernoulli.For Bernoulli distributionsBern(y)andBern(p):
TV(Bern(y),Bern(p)) =|y−p|.(54)
(This follows by takingA={1}in the TV definition.)
Applying Pinsker’s inequality:
(y−p) 2 ≤ 1
2KL(Bern(y)∥Bern(p)) = 1
2 (ℓ(p, y)−ℓ(y, y)).(55)
Step 4: Conditional expectation and integration.Fix x and let y=Q †(x) =E[Y|X=x] . Taking the prediction
p=Q(x):
(Q(x)−Q †(x))2 ≤ 1
2
 
ℓ(Q(x), Q†(x))−ℓ(Q †(x), Q†(x))

.(56)
Taking expectation overX∼ D:
EX

(Q(X)−Q †(X))2
≤ 1
2EX

ℓ(Q(X), Q†(X))−ℓ(Q †(X), Q†(X))

(57)
= 1
2
 
EX[ℓ(Q(X), Q†(X))]−E X[ℓ(Q†(X), Q†(X))]

.(58)
SinceQ †(x) =E[Y|X=x]minimizes the conditional expected log-loss, we have
EY|X [ℓ(Q(X), Y)]≥E Y|X [ℓ(Q†(X), Y)] =ℓ(Q†(X), Q†(X)) +H(Y|X),(59)
whereH(Y|X)is the conditional entropy (which cancels in the difference).
Thus:
EX

(Q(X)−Q †(X))2
≤ 1
2
 
R(Q)− R(Q†)

.(60)
We now prove theorem 5.2.
15

## Page 16

Executable Agentic Memory for GUI Agent
Theorem A.6(Restatement of Theorem 5.2).With probability at least1−δ, the learned predictorQ θ satisfies
∥Qθ −Q πu∥2,ρC ≤ϵ bias(m, δ),(61)
where
ϵbias(m, δ) :=
r
1
2 (ϵapprox + 2εgen(m, δ/2) +ϵopt),(62)
withϵ approx :=R(Q ⋆
Q)− R(Q†)≥0.
Proof.The proof proceeds in five steps.
Step 1: Decompose total excess risk.We decompose the excess risk ofQ θ relative toQ †:
R(Qθ)− R(Q†) =
 
R(Qθ)− R(Q⋆
Q)

| {z }
estimation + optimization
+
 
R(Q⋆
Q)− R(Q†)

| {z }
approximation
.(63)
Step 2: Bound estimation + optimization error.By Lemma A.4 with confidenceδ/2:
R(Qθ)− R(Q⋆
Q)≤2ε gen(m, δ/2) +ϵopt.(64)
Step 3: Identify approximation error.The approximation error is:
ϵapprox :=R(Q ⋆
Q)− R(Q†)≥0,(65)
which is non-negative since Q† is the Bayes-optimal predictor (minimizer of population risk over all measurable functions).
Step 4: Combine and apply Lemma A.5.With probability at least1−δ/2:
R(Qθ)− R(Q†)≤ϵ approx + 2εgen(m, δ/2) +ϵopt.(66)
By Lemma A.5:
EX∼D

(Qθ(X)−Q †(X))2
≤ 1
2
 
R(Qθ)− R(Q†)

.(67)
Step 5: Identify Q† =Q πu and conclude.In our setting, training targets are generated from unbiased terminal rollouts
underπ u with Bellman backups (Lemma A.1). ThusQ †(s, a) =E[Y|X= (s, a)] =Q πu(s, a).
Taking square roots:
∥Qθ −Q πu∥2,ρC =
q
E(S,A)∼ρC [(Qθ(S, A)−Qπu(S, A))2](68)
≤
r
1
2 (ϵapprox + 2εgen(m, δ/2) +ϵopt)(69)
=ϵ bias(m, δ).(70)
A.2. Proof of Theorem 5.3
Theorem A.7(Restatement of Theorem 5.3).Suppose the bias consistency condition holds: ϵbias(m, δ)<∆∗
min/2. Let
∆eff := ∆∗
min −2ϵ bias(m, δ)>0. Then for the greedy path ˆat = arg maxa∈A(s∗
t ) ¯Qn(s∗
t , a)to coincide with the optimal
path with probability at least1−δ, it suffices that
n≥ 32(K−1)c 2 ln(Hn/δ)
∆2
eff
+ 2(K−1)

2N0 + π2
3

.(71)
Proof.The proof adapts the UCT analysis of Kocsis & Szepesv ´ari (2006) to our guided-MCTS setting.
16

## Page 17

Executable Agentic Memory for GUI Agent
Step 1: Setup and notation.At each decision node s∗
t , UCT treats action selection as a multi-armed bandit with
K=|A(s ∗
t )| arms. Let Ta(n) denote the number of times action a is selected after n total simulations. The payoff
distributions are non-stationary because subtree estimates evolve with exploration.
Step 2: Apply Kocsis-Szepesv´ari Theorem 1.By Theorem 1 of (Kocsis & Szepesv ´ari, 2006), for UCB1 applied to a
non-stationary bandit with bias (drift) bounded byϵ, each suboptimal armawith gap∆ a >2ϵsatisfies:
E[Ta(n)]≤ 16c2 lnn
(∆a −2ϵ) 2 + 2N0 + π2
3 .(72)
In our setting, the bias isϵ=ϵ bias(m, δ)(from Theorem 5.2), and for each suboptimal actiona̸=a ∗
t :
∆a :=Q πu(s∗
t , a∗
t )−Q πu(s∗
t , a)≥∆∗
min.(73)
Thus:
E[Ta(n)]≤ 16c2 lnn
(∆a −2ϵ bias)2 + 2N0 + π2
3 ≤ 16c2 lnn
∆2
eff
+ 2N0 + π2
3 .(74)
Step 3: Sum over suboptimal actions.Summing over allK−1suboptimal actions:
X
a̸=a∗
t
E[Ta(n)]≤ 16(K−1)c 2 lnn
∆2
eff
+ (K−1)

2N0 + π2
3

.(75)
Step 4: Lower bound optimal action visits.Since P
a Ta(n) =n:
E[Ta∗
t (n)] =n−
X
a̸=a∗
t
E[Ta(n)]≥n− 16(K−1)c 2 lnn
∆2
eff
−(K−1)

2N0 + π2
3

.(76)
Step 5: Condition for optimal action dominance.For the optimal action to be selected (i.e., have the highest empirical
mean), it suffices thatE[T a∗
t (n)]> n/2, which requires:
n >32(K−1)c 2 lnn
∆2
eff
+ 2(K−1)

2N0 + π2
3

.(77)
Step 6: Union bound over path.The optimal path hasHdecision points. Taking a union bound:
Pr(allˆat =a ∗
t )≥1−H· δ
2H = 1− δ
2.(78)
Combined with the 1−δ/2 probability from the bias consistency guarantee (Theorem 5.2), the total success probability is at
least1−δ.
B. Additional Experimental Results
This appendix provides detailed analyses of the additional experimental results presented in the supplementary figures. We
systematically examine training dynamics, path extraction strategies, training methodologies, hyperparameter sensitivity,
and their implications for the proposed Executable Agentic Memory (EAM) framework.
B.1. Effect of Action Groups
We construct ablation experiments on action groups. Fig. 4 presents the length distribution of actions in the KGs. Beyond
atomic actions, our BPE-based merging mechanism constructs action groups encapsulating multi-step sequences, with
lengths following a long-tail distribution. AndroidWorld exhibits more long-sequence groups due to higher task complexity.
Fig. 5 shows that action groups yield significant improvements in both success rate and latency, with benefits more
pronounced on AndroidWorld. By consolidating frequent sequences into reusable groups, the MCTS search space is
significantly reduced, enabling more efficient planning.
17

## Page 18

Executable Agentic Memory for GUI Agent
/uni00000018/uni00000013
/uni00000014/uni00000013/uni00000013
/uni0000001a/uni0000001b/uni00000011/uni00000018
/uni00000014/uni00000016/uni00000018/uni0000001a/uni0000001c/uni00000014/uni00000014/uni00000014/uni00000016/uni00000014/uni00000018
/uni00000024/uni00000046/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni0000002f/uni00000048/uni00000051/uni0000004a/uni00000057/uni0000004b
/uni00000013
/uni00000016
/uni00000019
/uni00000017/uni00000011/uni00000018
/uni00000015/uni00000011/uni00000019
/uni00000015/uni00000011/uni00000014/uni00000014/uni00000011/uni0000001c
/uni00000015/uni00000011/uni0000001a
/uni00000014/uni00000011/uni0000001c/uni00000015/uni00000011/uni00000013/uni00000014/uni00000011/uni0000001b
/uni00000013/uni00000011/uni0000001b
/uni00000013/uni00000011/uni00000016/uni00000013/uni00000011/uni00000016/uni00000013/uni00000011/uni00000015/uni00000013/uni00000011/uni00000016/uni00000013/uni00000011/uni00000015/uni00000013/uni00000011/uni00000015
/uni00000033/uni00000048/uni00000055/uni00000046/uni00000048/uni00000051/uni00000057/uni00000044/uni0000004a/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c
(a)AndroidWorld
/uni00000018/uni00000013
/uni00000014/uni00000013/uni00000013
/uni0000001b/uni00000013/uni00000011/uni00000019
/uni00000014/uni00000015/uni00000011/uni0000001c
/uni00000014/uni00000016/uni00000018/uni0000001a/uni0000001c
/uni00000024/uni00000046/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni0000002f/uni00000048/uni00000051/uni0000004a/uni00000057/uni0000004b
/uni00000013
/uni00000018
/uni00000014/uni00000011/uni00000016
/uni00000015/uni00000011/uni00000019
/uni00000014/uni00000011/uni00000016
/uni00000013/uni00000011/uni00000019/uni00000013/uni00000011/uni00000017/uni00000013/uni00000011/uni00000015/uni00000013/uni00000011/uni00000014
/uni00000033/uni00000048/uni00000055/uni00000046/uni00000048/uni00000051/uni00000057/uni00000044/uni0000004a/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c (b)DroidTask
Figure 4.Distribution action sequence lengths in KGs
/uni00000024/uni00000051/uni00000047/uni00000055/uni00000052/uni0000004c/uni00000047/uni0000003a/uni00000052/uni00000055/uni0000004f/uni00000047/uni00000030/uni00000052/uni00000045/uni0000004c/uni0000004f/uni00000048/uni00000030/uni0000004c/uni00000051/uni0000004c/uni0000003a/uni00000052/uni00000045/uni00000027/uni00000055/uni00000052/uni0000004c/uni00000047/uni00000037/uni00000044/uni00000056/uni0000004e
/uni00000025/uni00000048/uni00000051/uni00000046/uni0000004b/uni00000050/uni00000044/uni00000055/uni0000004e
/uni00000013
/uni00000015/uni00000013
/uni00000017/uni00000013
/uni00000019/uni00000013
/uni0000001b/uni00000013
/uni00000014/uni00000013/uni00000013/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c
/uni0000005a/uni00000012/uni00000052/uni00000003/uni00000044/uni00000046/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni0000004a/uni00000055/uni00000052/uni00000058/uni00000053/uni0000005a/uni00000012/uni00000003/uni00000044/uni00000046/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni0000004a/uni00000055/uni00000052/uni00000058/uni00000053
(a)Success Rate
/uni00000024/uni00000051/uni00000047/uni00000055/uni00000052/uni0000004c/uni00000047/uni0000003a/uni00000052/uni00000055/uni0000004f/uni00000047/uni00000030/uni00000052/uni00000045/uni0000004c/uni0000004f/uni00000048/uni00000030/uni0000004c/uni00000051/uni0000004c/uni0000003a/uni00000052/uni00000045/uni00000027/uni00000055/uni00000052/uni0000004c/uni00000047/uni00000037/uni00000044/uni00000056/uni0000004e
/uni00000025/uni00000048/uni00000051/uni00000046/uni0000004b/uni00000050/uni00000044/uni00000055/uni0000004e
/uni00000016
/uni00000019
/uni0000001c
/uni00000014/uni00000015
/uni00000014/uni00000018
/uni00000014/uni0000001b/uni0000002f/uni00000044/uni00000057/uni00000048/uni00000051/uni00000046/uni0000005c/uni00000003/uni00000049/uni00000052/uni00000055/uni00000003/uni00000033/uni00000044/uni00000057/uni0000004b/uni00000003/uni00000028/uni0000005b/uni00000057/uni00000055/uni00000044/uni00000046/uni00000057/uni0000004c/uni00000052/uni00000051
/uni0000005a/uni00000012/uni00000052/uni00000003/uni00000044/uni00000046/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni0000004a/uni00000055/uni00000052/uni00000058/uni00000053/uni0000005a/uni00000012/uni00000003/uni00000044/uni00000046/uni00000057/uni0000004c/uni00000052/uni00000051/uni00000003/uni0000004a/uni00000055/uni00000052/uni00000058/uni00000053 (b)Latency
Figure 5.Effect of action group on performance and efficiency.
B.2. Training Loss Dynamics Across Self-Learning Rounds
Fig. 6 presents the training loss curves across four self-learning rounds for three model sizes (Qwen2.5-0.5B-Instruct,
Qwen2.5-1.5B-Instruct, and Qwen2.5-3B-Instruct) evaluated on three benchmarks (AndroidWorld, DroidTask, and Mo-
bileMiniWob).
Progressive Loss Reduction.A salient pattern emerges across all configurations: the initial loss at the beginning of each
subsequent round starts consistently lower than the previous round. This progressive reduction in starting loss demonstrates
that the Q-model successfully retains and builds upon knowledge acquired in previous iterations, validating the effectiveness
of our iterative self-training pipeline. Formally, this observation suggests that the empirical risk ˆRS(Qθ) decreases across
rounds, which according to Lemma A.4, implies corresponding reductions in the true riskR(Q θ).
Convergence Characteristics.All training curves exhibit rapid initial descent followed by stabilization, typically converging
within the first 100–150 training steps. The converged loss values decrease monotonically across rounds, indicating that
the quality of self-generated training data improves as the Q-model becomes more accurate at value estimation. This
phenomenon creates a virtuous cycle: better value estimates lead to more informative MCTS rollouts, which in turn produce
higher-quality Bellman backup targets, further improving subsequent training rounds.
Model Capacity Effects.Larger models consistently achieve lower final loss values across all benchmarks. This performance
gap reflects the increased representational capacity of larger models to capture complex relationships between GUI states,
actions, and their associated Q-values. The relationship can be understood through the lens of approximation error ϵapprox in
Theorem 5.2: larger model classesQreduce the gapR(Q ⋆
Q)− R(Q†), yielding tighter bias bounds.
18

## Page 19

Executable Agentic Memory for GUI Agent
/uni00000013/uni00000018/uni00000013/uni00000014/uni00000013/uni00000013/uni00000014/uni00000018/uni00000013/uni00000015/uni00000013/uni00000013/uni00000015/uni00000018/uni00000013/uni00000016/uni00000013/uni00000013/uni00000016/uni00000018/uni00000013
/uni00000037/uni00000055/uni00000044/uni0000004c/uni00000051/uni0000004c/uni00000051/uni0000004a/uni00000003/uni00000036/uni00000057/uni00000048/uni00000053/uni00000056
/uni00000013/uni00000011/uni00000015
/uni00000013/uni00000011/uni00000016
/uni00000013/uni00000011/uni00000017
/uni00000013/uni00000011/uni00000018
/uni00000013/uni00000011/uni00000019/uni0000002f/uni00000052/uni00000056/uni00000056
/uni00000024/uni00000051/uni00000047/uni00000055/uni00000052/uni0000004c/uni00000047/uni0000003a/uni00000052/uni00000055/uni0000004f/uni00000047/uni00000003/uni0000000b/uni00000034/uni0000005a/uni00000048/uni00000051/uni00000015/uni00000011/uni00000018/uni00000010/uni00000013/uni00000011/uni00000018/uni00000025/uni00000010/uni0000004c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057/uni0000000c
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000014
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000015
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000016
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000017
/uni00000013/uni00000018/uni00000013/uni00000014/uni00000013/uni00000013/uni00000014/uni00000018/uni00000013/uni00000015/uni00000013/uni00000013/uni00000015/uni00000018/uni00000013/uni00000016/uni00000013/uni00000013/uni00000016/uni00000018/uni00000013
/uni00000037/uni00000055/uni00000044/uni0000004c/uni00000051/uni0000004c/uni00000051/uni0000004a/uni00000003/uni00000036/uni00000057/uni00000048/uni00000053/uni00000056
/uni00000013/uni00000011/uni00000015
/uni00000013/uni00000011/uni00000016
/uni00000013/uni00000011/uni00000017
/uni00000013/uni00000011/uni00000018
/uni00000013/uni00000011/uni00000019/uni0000002f/uni00000052/uni00000056/uni00000056
/uni00000024/uni00000051/uni00000047/uni00000055/uni00000052/uni0000004c/uni00000047/uni0000003a/uni00000052/uni00000055/uni0000004f/uni00000047/uni00000003/uni0000000b/uni00000034/uni0000005a/uni00000048/uni00000051/uni00000015/uni00000011/uni00000018/uni00000010/uni00000014/uni00000011/uni00000018/uni00000025/uni00000010/uni0000004c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057/uni0000000c
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000014
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000015
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000016
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000017
/uni00000013/uni00000018/uni00000013/uni00000014/uni00000013/uni00000013/uni00000014/uni00000018/uni00000013/uni00000015/uni00000013/uni00000013/uni00000015/uni00000018/uni00000013/uni00000016/uni00000013/uni00000013/uni00000016/uni00000018/uni00000013
/uni00000037/uni00000055/uni00000044/uni0000004c/uni00000051/uni0000004c/uni00000051/uni0000004a/uni00000003/uni00000036/uni00000057/uni00000048/uni00000053/uni00000056
/uni00000013/uni00000011/uni00000015
/uni00000013/uni00000011/uni00000016
/uni00000013/uni00000011/uni00000017
/uni00000013/uni00000011/uni00000018
/uni00000013/uni00000011/uni00000019/uni0000002f/uni00000052/uni00000056/uni00000056
/uni00000024/uni00000051/uni00000047/uni00000055/uni00000052/uni0000004c/uni00000047/uni0000003a/uni00000052/uni00000055/uni0000004f/uni00000047/uni00000003/uni0000000b/uni00000034/uni0000005a/uni00000048/uni00000051/uni00000015/uni00000011/uni00000018/uni00000010/uni00000016/uni00000025/uni00000010/uni0000004c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057/uni0000000c
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000014
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000015
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000016
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000017
/uni00000013/uni00000018/uni00000013/uni00000014/uni00000013/uni00000013/uni00000014/uni00000018/uni00000013/uni00000015/uni00000013/uni00000013/uni00000015/uni00000018/uni00000013/uni00000016/uni00000013/uni00000013/uni00000016/uni00000018/uni00000013
/uni00000037/uni00000055/uni00000044/uni0000004c/uni00000051/uni0000004c/uni00000051/uni0000004a/uni00000003/uni00000036/uni00000057/uni00000048/uni00000053/uni00000056
/uni00000013/uni00000011/uni00000015
/uni00000013/uni00000011/uni00000016
/uni00000013/uni00000011/uni00000017
/uni00000013/uni00000011/uni00000018
/uni00000013/uni00000011/uni00000019
/uni00000013/uni00000011/uni0000001a/uni0000002f/uni00000052/uni00000056/uni00000056
/uni00000027/uni00000055/uni00000052/uni0000004c/uni00000047/uni00000037/uni00000044/uni00000056/uni0000004e/uni00000003/uni0000000b/uni00000034/uni0000005a/uni00000048/uni00000051/uni00000015/uni00000011/uni00000018/uni00000010/uni00000013/uni00000011/uni00000018/uni00000025/uni00000010/uni0000004c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057/uni0000000c
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000014
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000015
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000016
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000017
/uni00000013/uni00000018/uni00000013/uni00000014/uni00000013/uni00000013/uni00000014/uni00000018/uni00000013/uni00000015/uni00000013/uni00000013/uni00000015/uni00000018/uni00000013/uni00000016/uni00000013/uni00000013/uni00000016/uni00000018/uni00000013
/uni00000037/uni00000055/uni00000044/uni0000004c/uni00000051/uni0000004c/uni00000051/uni0000004a/uni00000003/uni00000036/uni00000057/uni00000048/uni00000053/uni00000056
/uni00000013/uni00000011/uni00000015
/uni00000013/uni00000011/uni00000016
/uni00000013/uni00000011/uni00000017
/uni00000013/uni00000011/uni00000018
/uni00000013/uni00000011/uni00000019
/uni00000013/uni00000011/uni0000001a/uni0000002f/uni00000052/uni00000056/uni00000056
/uni00000027/uni00000055/uni00000052/uni0000004c/uni00000047/uni00000037/uni00000044/uni00000056/uni0000004e/uni00000003/uni0000000b/uni00000034/uni0000005a/uni00000048/uni00000051/uni00000015/uni00000011/uni00000018/uni00000010/uni00000014/uni00000011/uni00000018/uni00000025/uni00000010/uni0000004c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057/uni0000000c
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000014
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000015
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000016
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000017
/uni00000013/uni00000018/uni00000013/uni00000014/uni00000013/uni00000013/uni00000014/uni00000018/uni00000013/uni00000015/uni00000013/uni00000013/uni00000015/uni00000018/uni00000013/uni00000016/uni00000013/uni00000013/uni00000016/uni00000018/uni00000013
/uni00000037/uni00000055/uni00000044/uni0000004c/uni00000051/uni0000004c/uni00000051/uni0000004a/uni00000003/uni00000036/uni00000057/uni00000048/uni00000053/uni00000056
/uni00000013/uni00000011/uni00000015
/uni00000013/uni00000011/uni00000016
/uni00000013/uni00000011/uni00000017
/uni00000013/uni00000011/uni00000018
/uni00000013/uni00000011/uni00000019
/uni00000013/uni00000011/uni0000001a/uni0000002f/uni00000052/uni00000056/uni00000056
/uni00000027/uni00000055/uni00000052/uni0000004c/uni00000047/uni00000037/uni00000044/uni00000056/uni0000004e/uni00000003/uni0000000b/uni00000034/uni0000005a/uni00000048/uni00000051/uni00000015/uni00000011/uni00000018/uni00000010/uni00000016/uni00000025/uni00000010/uni0000004c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057/uni0000000c
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000014
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000015
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000016
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000017
/uni00000013/uni00000018/uni00000013/uni00000014/uni00000013/uni00000013/uni00000014/uni00000018/uni00000013/uni00000015/uni00000013/uni00000013/uni00000015/uni00000018/uni00000013/uni00000016/uni00000013/uni00000013/uni00000016/uni00000018/uni00000013
/uni00000037/uni00000055/uni00000044/uni0000004c/uni00000051/uni0000004c/uni00000051/uni0000004a/uni00000003/uni00000036/uni00000057/uni00000048/uni00000053/uni00000056
/uni00000013/uni00000011/uni00000015
/uni00000013/uni00000011/uni00000016
/uni00000013/uni00000011/uni00000017
/uni00000013/uni00000011/uni00000018
/uni00000013/uni00000011/uni00000019/uni0000002f/uni00000052/uni00000056/uni00000056
/uni00000030/uni00000052/uni00000045/uni0000004c/uni0000004f/uni00000048/uni00000030/uni0000004c/uni00000051/uni0000004c/uni0000003a/uni00000052/uni00000045/uni00000003/uni0000000b/uni00000034/uni0000005a/uni00000048/uni00000051/uni00000015/uni00000011/uni00000018/uni00000010/uni00000013/uni00000011/uni00000018/uni00000025/uni00000010/uni0000004c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057/uni0000000c
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000014
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000015
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000016
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000017
/uni00000013/uni00000018/uni00000013/uni00000014/uni00000013/uni00000013/uni00000014/uni00000018/uni00000013/uni00000015/uni00000013/uni00000013/uni00000015/uni00000018/uni00000013/uni00000016/uni00000013/uni00000013/uni00000016/uni00000018/uni00000013
/uni00000037/uni00000055/uni00000044/uni0000004c/uni00000051/uni0000004c/uni00000051/uni0000004a/uni00000003/uni00000036/uni00000057/uni00000048/uni00000053/uni00000056
/uni00000013/uni00000011/uni00000015
/uni00000013/uni00000011/uni00000016
/uni00000013/uni00000011/uni00000017
/uni00000013/uni00000011/uni00000018
/uni00000013/uni00000011/uni00000019/uni0000002f/uni00000052/uni00000056/uni00000056
/uni00000030/uni00000052/uni00000045/uni0000004c/uni0000004f/uni00000048/uni00000030/uni0000004c/uni00000051/uni0000004c/uni0000003a/uni00000052/uni00000045/uni00000003/uni0000000b/uni00000034/uni0000005a/uni00000048/uni00000051/uni00000015/uni00000011/uni00000018/uni00000010/uni00000014/uni00000011/uni00000018/uni00000025/uni00000010/uni0000004c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057/uni0000000c
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000014
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000015
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000016
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000017
/uni00000013/uni00000018/uni00000013/uni00000014/uni00000013/uni00000013/uni00000014/uni00000018/uni00000013/uni00000015/uni00000013/uni00000013/uni00000015/uni00000018/uni00000013/uni00000016/uni00000013/uni00000013/uni00000016/uni00000018/uni00000013
/uni00000037/uni00000055/uni00000044/uni0000004c/uni00000051/uni0000004c/uni00000051/uni0000004a/uni00000003/uni00000036/uni00000057/uni00000048/uni00000053/uni00000056
/uni00000013/uni00000011/uni00000015
/uni00000013/uni00000011/uni00000016
/uni00000013/uni00000011/uni00000017
/uni00000013/uni00000011/uni00000018
/uni00000013/uni00000011/uni00000019
/uni00000013/uni00000011/uni0000001a/uni0000002f/uni00000052/uni00000056/uni00000056
/uni00000030/uni00000052/uni00000045/uni0000004c/uni0000004f/uni00000048/uni00000030/uni0000004c/uni00000051/uni0000004c/uni0000003a/uni00000052/uni00000045/uni00000003/uni0000000b/uni00000034/uni0000005a/uni00000048/uni00000051/uni00000015/uni00000011/uni00000018/uni00000010/uni00000016/uni00000025/uni00000010/uni0000004c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057/uni0000000c
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000014
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000015
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000016
/uni00000035/uni00000052/uni00000058/uni00000051/uni00000047/uni00000003/uni00000017
Figure 6.Training loss curves across self-learning rounds. We show the training loss for each round across different model sizes and
benchmarks.
19

## Page 20

Executable Agentic Memory for GUI Agent
/uni00000013/uni00000011/uni00000018/uni00000025/uni00000014/uni00000011/uni00000018/uni00000025/uni00000016/uni00000025
/uni00000030/uni00000052/uni00000047/uni00000048/uni0000004f/uni00000003/uni00000036/uni0000004c/uni0000005d/uni00000048
/uni00000013
/uni00000014/uni00000013
/uni00000015/uni00000013
/uni00000016/uni00000013
/uni00000017/uni00000013
/uni00000018/uni00000013/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c
/uni0000002a/uni00000055/uni00000048/uni00000048/uni00000047/uni0000005c
/uni00000025/uni00000052/uni00000031
/uni00000030/uni00000026/uni00000037/uni00000036
(a)AndroidWorld
/uni00000013/uni00000011/uni00000018/uni00000025/uni00000014/uni00000011/uni00000018/uni00000025/uni00000016/uni00000025
/uni00000030/uni00000052/uni00000047/uni00000048/uni0000004f/uni00000003/uni00000036/uni0000004c/uni0000005d/uni00000048
/uni00000013
/uni00000015/uni00000013
/uni00000017/uni00000013
/uni00000019/uni00000013
/uni0000001b/uni00000013
/uni00000014/uni00000013/uni00000013/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c
/uni0000002a/uni00000055/uni00000048/uni00000048/uni00000047/uni0000005c
/uni00000025/uni00000052/uni00000031
/uni00000030/uni00000026/uni00000037/uni00000036 (b)DroidTask
Figure 7.The impact of different path extraction methods on performance.
B.3. Comparison of Path Extraction Methods
Figure 7 compares three path extraction strategies across different model sizes (0.5B, 1.5B, and 3B parameters) on
AndroidWorld and DroidTask:
•Greedy: Selects actions with highest Q-values without exploration, i.e.,a t = arg maxa∈A(st) Qθ(st, a).
• Best-of-N (BoN): Samples 10 candidate paths independently and selects the 5 with the highest cumulative Q-value (for
fair comparison with MCTS).
•MCTS: Employs the full tree search procedure with UCT-based exploration-exploitation balancing.
Consistent MCTS Superiority.MCTS consistently outperforms both Greedy and BoN strategies across all model sizes
and benchmarks. The consistent advantage of MCTS demonstrates the substantial value of structured exploration during
path extraction.
Theoretical Interpretation.These empirical findings align precisely with our theoretical analysis. Theorem 5.3 establishes
that MCTS recovers the optimal path with high probability when sufficient simulations are performed, with complexity
scaling as O

HKc2 ln(Hn/δ)
(∆∗
min−2ϵbias)2

. The Greedy strategy, by contrast, commits irrevocably to the highest-valued action without
accounting for estimation uncertainty, making it vulnerable to errors inQ θ.
B.4. Impact of Training Strategies on Q-Model Performance
/uni00000038/uni00000051/uni00000057/uni00000055/uni00000044/uni0000004c/uni00000051/uni00000048/uni00000047/uni0000002c/uni00000051/uni0000004c/uni00000057/uni00000025/uni0000004c/uni00000051/uni00000044/uni00000055/uni0000005c/uni00000034/uni00000010/uni00000059/uni00000044/uni0000004f/uni00000058/uni00000048
/uni00000037/uni00000055/uni00000044/uni0000004c/uni00000051/uni0000004c/uni00000051/uni0000004a/uni00000003/uni00000036/uni00000057/uni00000055/uni00000044/uni00000057/uni00000048/uni0000004a/uni0000005c
/uni00000013
/uni00000014/uni00000013
/uni00000015/uni00000013
/uni00000016/uni00000013
/uni00000017/uni00000013
/uni00000018/uni00000013
/uni00000019/uni00000013/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c
(a)AndroidWorld
/uni00000038/uni00000051/uni00000057/uni00000055/uni00000044/uni0000004c/uni00000051/uni00000048/uni00000047/uni0000002c/uni00000051/uni0000004c/uni00000057/uni00000025/uni0000004c/uni00000051/uni00000044/uni00000055/uni0000005c/uni00000034/uni00000010/uni00000059/uni00000044/uni0000004f/uni00000058/uni00000048
/uni00000037/uni00000055/uni00000044/uni0000004c/uni00000051/uni0000004c/uni00000051/uni0000004a/uni00000003/uni00000036/uni00000057/uni00000055/uni00000044/uni00000057/uni00000048/uni0000004a/uni0000005c
/uni00000013
/uni00000014/uni00000018
/uni00000016/uni00000013
/uni00000017/uni00000018
/uni00000019/uni00000013
/uni0000001a/uni00000018
/uni0000001c/uni00000013/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c (b)DroidTask
Figure 8.Performance with Different Training Strategies.
1.Untrained: The base language model without any task-specific fine-tuning.
20

## Page 21

Executable Agentic Memory for GUI Agent
2.Init: Initialization via preference learning on expert trajectories using the pairwise ranking loss (Equation 7).
3.Binary: Training with binary outcome labels indicating path success (y= 1) or failure (y= 0).
4.Q-value: Our proposed approach using soft Q-value targets computed via Bellman backup.
All experiments employ the 3B model with identical MCTS inference configurations (N= 50iterations,c= 10).
Necessity of Task-Specific Training.The untrained model achieves the lowest success rate, establishing that raw language
model capabilities are insufficient for effective Q-value estimation in GUI navigation.
Preference-Based Initialization.The Init strategy achieves substantial improvements over the untrained baseline. This
confirms that relative preference information from expert trajectories provides valuable supervision for warming up the
Q-model. The Bradley-Terry formulation (Equation 7) effectively translates these preferences into initial value estimates
that, while not perfectly calibrated, establish meaningful action rankings.
Limitations of Binary Supervision.Training with binary outcome labels yields moderate performance. While binary labels
capture the ultimate success or failure of paths, they provide identical supervision signals to all actions along successful
trajectories and all actions along failed trajectories. This coarse granularity fails to distinguish among the quality of
intermediate decisions.
Superiority of Q-Value Training.Our proposed Q-value training achieves the highest performance: approximately 52.6%
on AndroidWorld and 86.1% on DroidTask. The substantial gains over binary training demonstrate the value of continuous
Q-value targets. By computing targets via Bellman backup:
ˆQ(s, a)←r(s, a) + 1
|A(s′)|
X
a′∈A(s′)
ˆQ(s′, a′),(79)
we obtain supervision signals that capture the nuanced probability of success from each state-action pair, enabling fine-
grained credit assignment across the trajectory.
B.5. Effect of MCTS Iteration Count
/uni00000014/uni00000013/uni00000016/uni00000013/uni00000018/uni00000013/uni00000014/uni00000013/uni00000013
N
/uni00000017/uni00000013
/uni00000019/uni00000013
/uni0000001b/uni00000013/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c
/uni00000024/uni00000051/uni00000047/uni00000055/uni00000052/uni0000004c/uni00000047/uni0000003a/uni00000052/uni00000055/uni0000004f/uni00000047
/uni00000030/uni00000052/uni00000045/uni0000004c/uni0000004f/uni00000048/uni00000030/uni0000004c/uni00000051/uni0000004c/uni0000003a/uni00000052/uni00000045/uni0000000e/uni0000000e
/uni00000027/uni00000055/uni00000052/uni0000004c/uni00000047/uni00000037/uni00000044/uni00000056/uni0000004e
(a)Success Rate
/uni00000014/uni00000013/uni00000016/uni00000013/uni00000018/uni00000013/uni00000014/uni00000013/uni00000013
N
/uni00000018
/uni00000014/uni00000013
/uni00000014/uni00000018/uni0000002f/uni00000044/uni00000057/uni00000048/uni00000051/uni00000046/uni0000005c/uni00000003/uni00000049/uni00000052/uni00000055/uni00000003/uni00000033/uni00000044/uni00000057/uni0000004b/uni00000003/uni00000028/uni0000005b/uni00000057/uni00000055/uni00000044/uni00000046/uni00000057/uni0000004c/uni00000052/uni00000051
/uni00000024/uni00000051/uni00000047/uni00000055/uni00000052/uni0000004c/uni00000047/uni0000003a/uni00000052/uni00000055/uni0000004f/uni00000047
/uni00000030/uni00000052/uni00000045/uni0000004c/uni0000004f/uni00000048/uni00000030/uni0000004c/uni00000051/uni0000004c/uni0000003a/uni00000052/uni00000045/uni0000000e/uni0000000e
/uni00000027/uni00000055/uni00000052/uni0000004c/uni00000047/uni00000037/uni00000044/uni00000056/uni0000004e
 (b)Latency
Figure 9.The impact of different number of MCTS iterations on performance.
Figure 9 investigates the trade-off between MCTS simulation budget and performance by varying the number of iterations
N∈ {10,30,50,100}. We measure both success rate and path extraction latency across all three benchmarks using the 3B
model.
Monotonic Performance Scaling.Success rate increases monotonically with MCTS iterations across all benchmarks
that additional simulation budget enables more thorough exploration of the search space, increasing the probability of
discovering optimal paths.
Diminishing Returns.The performance gains exhibit pronounced diminishing returns. Quantitatively, the marginal
improvement per additional 10 iterations decreases substantially:
21

## Page 22

Executable Agentic Memory for GUI Agent
•N: 10→30:+10points on AndroidWorld
•N: 30→50:+6points on AndroidWorld
•N: 50→100:0.7points on AndroidWorld
This sublinear scaling suggests that moderate iteration counts capture most of the benefit from tree search, with additional
simulations primarily refining already-promising paths rather than discovering qualitatively better alternatives.
Latency Characteristics.Path extraction latency scales approximately linearly with iteration count. This linear scaling,
combined with the sublinear performance gains, implies a favorable efficiency trade-off at moderate iteration counts.
Practical Operating Points.The results suggest N= 30 or N= 50 as practical operating points. At N= 50 , the system
achieves over95%of theN= 100performance on all benchmarks while requiring only50%of the computation time.
Connection to Theoretical Bounds.These findings align with Theorem 5.3, which establishes simulation complexity
scaling as:
n≥ 32(K−1)c 2 ln(Hn/δ)
∆2
eff
+ 2(K−1)

2N0 + π2
3

.(80)
The logarithmic dependence onn in the bound is consistent with the observed diminishing returns. The empirical observation
that moderate N suffices suggests that practical task instances have relatively large effective action gaps∆eff = ∆∗
min −2ϵbias,
enabling efficient path recovery without exhaustive search.
B.6. Influence of Model Size and Exploration Constant
/uni00000013/uni00000011/uni00000018/uni00000025/uni00000014/uni00000011/uni00000018/uni00000025/uni00000016/uni00000025
/uni00000025/uni00000044/uni00000056/uni00000048/uni00000003/uni00000030/uni00000052/uni00000047/uni00000048/uni0000004f/uni00000003/uni00000036/uni0000004c/uni0000005d/uni00000048
/uni00000017/uni00000013
/uni00000019/uni00000013
/uni0000001b/uni00000013/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c
/uni00000024/uni00000051/uni00000047/uni00000055/uni00000052/uni0000004c/uni00000047/uni0000003a/uni00000052/uni00000055/uni0000004f/uni00000047
/uni00000030/uni00000052/uni00000045/uni0000004c/uni0000004f/uni00000048/uni00000030/uni0000004c/uni00000051/uni0000004c/uni0000003a/uni00000052/uni00000045
/uni00000027/uni00000055/uni00000052/uni0000004c/uni00000047/uni00000037/uni00000044/uni00000056/uni0000004e
(a)Model size
/uni00000013 /uni00000018/uni00000014/uni00000013/uni00000015/uni00000013
c
/uni00000014/uni00000018
/uni00000016/uni00000013
/uni00000017/uni00000018
/uni00000019/uni00000013
/uni0000001a/uni00000018
/uni0000001c/uni00000013/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c
/uni00000024/uni00000051/uni00000047/uni00000055/uni00000052/uni0000004c/uni00000047/uni0000003a/uni00000052/uni00000055/uni0000004f/uni00000047
/uni00000030/uni00000052/uni00000045/uni0000004c/uni0000004f/uni00000048/uni00000030/uni0000004c/uni00000051/uni0000004c/uni0000003a/uni00000052/uni00000045
/uni00000027/uni00000055/uni00000052/uni0000004c/uni00000047/uni00000037/uni00000044/uni00000056/uni0000004e
 (b)Exploration constantc
Figure 10.The impact of model size and exploration constant on performance.
Figure 10 presents two hyperparameter studies: (a) the effect of base model size on success rate across 0.5B, 1.5B, and 3B
parameters; and (b) the impact of the UCT exploration constant c∈ {0,5,10,20} on performance, where c= 0 corresponds
to pure exploitation.
Model Size Analysis.Larger models achieve higher success rates across all benchmarks.
Exploration Constant Analysis.Performance peaks at c= 10 across all benchmarks Both pure exploitation (c= 0 ) and
excessive exploration (c= 20 ) yield degraded performance. At c= 0 , the search degenerates to greedy selection, forfeiting
the benefits of exploration demonstrated in Section B.3. At c= 20 , the exploration bonus dominates the Q-value term in
UCT, causing the search to behave nearly randomly and waste simulation budget on unpromising branches.
Benchmark-Specific Sensitivity.AndroidWorld shows the highest sensitivity to c. DroidTask and MobileMiniWob++
exhibit more stable performance. This differential sensitivity correlates with task complexity: AndroidWorld’s deeper search
spaces and longer optimal paths create more opportunities for both beneficial exploration and wasteful over-exploration.
22

## Page 23

Executable Agentic Memory for GUI Agent
Theoretical Perspective.The exploration constantcappears directly in the UCT criterion:
UCT(s, a) =Q(s, a) +c
s
lnN(s)
N(s, a),(81)
and in the sample complexity bound of Theorem 5.3, where it contributes to the c2 term in the numerator. The empirical
finding that moderate c optimizes performance validates the theoretical exploration-exploitation trade-off: insufficient
exploration risks committing to suboptimal paths before adequately evaluating alternatives, while excessive exploration
incurs unnecessary simulation cost.
C. Training Data
We train our Q-model in two phases, including initialization training and self-training iterations.
C.1. Step-level Preference Dataset for Initialization Training
Our training data pairs are derived from AMEX, which contains a large collection of expert trajectories with semantic
descriptions for each action step, as well as semantic annotations for task-irrelevant elements on each page. For each page
in the expert trajectories, we construct preference optimization pairs consisting of (expert action description, multiple
task-irrelevant element descriptions)as follows:
{
"instruction": "Open Google Tasks. Delete all completed tasks in the\"Work
List\".",
"history actions": [],
"page caption": "The page displays a list of tasks organized by categories such as
work, health, and family, with options to mark tasks as complete, add stars, and view
details.",
"correct actions": [
"View the list of completed tasks"
],
"false actions": [
"View details of the task ’submit progress report’ due on Monday, April 15",
"View details of the task ’project x’ with 1 subtask",
"View tasks under ’work’ category",
"View details of the task ’send a draft to the team’ due on Friday, April 12"
]
}
C.2. Dataset Generated by MCTS Rollouts
Following initialization, the value model is iteratively trained to predict the Q-value of state-action pairs. An example of
dataset from AndroidWorld is illustrated below.
Input:
<|user|>:
Task: Add the expenses from expenses.jpg in Simple Gallery Pro to pro expense.
You are at: This is an expense tracking dashboard that allows users to monitor their
spending patterns through a weekly calendar view and detailed transaction history,
while providing quick access to add new expenses via the floating action button.
Executed path: Start of Task
Proposed action:
Output:
<|assistant|>: Navigate from expense tracking application to gallery app to locate and
review expense-related images or receipts for reference during expense entry
workflow<end of step>
Label: 0.7679166666666666
23

## Page 24

Executable Agentic Memory for GUI Agent
D. Prompts
D.1. Prompt for Sub-goals Generation at Offline Exploration Phase
Given a user task, the current screenshot of{app name}, and available UI elements,
generate multiple potential sub-goals to progress toward completing the user task.
Each sub-goal must:
1. Start with interacting with a specific UI element from the provided element list
2. Be expressed as a single, clear directive following the pattern: [Starting action]
+ [Specific steps] + [End goal]
3. Be achievable within approximately 3 actions (AT MOST 5) from the anchor element
4. Provide a concrete target state that advances toward the user task completion
Context Information:
- User Task:{user task}
- App name:{app name}
- Package name:{package name}
- Current screen elements (Only interact with *visible=true elements):
{element list}
- Activity context:{activity list}
- Recent History Action (up to 5):{action history}
- Sub-goals History:{subgoal history}
- State Summary:{state summary}
Task Execution Analysis:
Before generating new sub-goals, analyze the current execution state:
1.Completed Progress: Review the sub-goals history to understand what has already
been accomplished toward the main task
2.Current Position: Based on the state summary and recent actions, identify where
you are in the task workflow
3.Remaining Work: Determine what specific components of the user task still need to
be completed
4.Next Logical Steps: Identify the most logical next actions that build upon
completed sub-goals
Sub-goal Generation Strategy:
-Continuation Focus: Generate sub-goals that logically continue from where previous
sub-goals left off
-Avoid Redundancy: Do not repeat actions or objectives that have already been
successfully completed
-Progressive Advancement: Each sub-goal should represent a clear step forward in the
overall task completion
For each sub-goal, provide:
1.Anchor Element: The specific UI element ID/description from the list to start with
2.Sub-goal: Single directive sentence following [Starting action] + [Specific steps]
+ [End goal] pattern
3.Confidence Score: How likely this sub-goal is to advance toward task completion
(0.0-1.0)
Format each sub-goal as:
Sub-goal [N]:
Anchor: [Element ID/description from element list]
Directive: [Single clear instruction with starting action + steps + end goal]
Confidence: [0.0-1.0]
24

## Page 25

Executable Agentic Memory for GUI Agent
D.2. Prompt for Progress Evaluation during Exploration
Given the user task, action history, and current screenshot of{app name}, evaluate
the current exploration state and determine the next action strategy.
Context Information:
- User Task:{user task}
- App name:{app name}
- Package name:{package name}
- Recent Action History:{action history}
(if the last action is ’{"action type": "status", "goal status": "complete"}’, it
means the last sub-goal was complete successfully)
- Sub-goals History:{subgoal history}
- Current screen elements:
{element list}
Analysis Requirements:
1. Compare the current state with the expected end goal of the user task
2. Evaluate whether the recent actions are leading toward task completion
3. Assess if the current exploration path is meaningful and relevant
4. Consider whether all required steps have been executed successfully
5. Verify if the current screen/state indicates task completion
6. Account for any error states, dead-ends, or repetitive actions in the history
7. Make sure to use answer action for information retrieval task
({"action type": "answer", "text": "<answer text>"}is the last action in the
action history)
8. Be strict about completion - partial progress is not completion
Evaluation Criteria:
- Has the user task’s primary objective been achieved? (COMPLETED)
* Have we completed all the sub-goals required by the task and at the expected
final state/screen for this task?
- Are we making meaningful progress toward the goal? (CONTINUE)
- Are we stuck, going in wrong direction, or exploring irrelevant paths? (BACKTRACK)
- Is there clear evidence of task completion, progress, or deviation in the current
state?
Format your response as:
Reasoning: [Detailed analysis of current progress, referencing specific elements
from action history, current state, and task relevance. Explain why we should
continue, backtrack, or if task is complete]
Result: [CONTINUE/BACKTRACK/COMPLETED]
25

## Page 26

Executable Agentic Memory for GUI Agent
D.3. Prompt for Action Group Mining
You are an AI assistant specialized in generating high-level common UI operation nodes
which can be part of a variety of operations. You need to generate a complete
description of a high-level action node based on the given chain information.
Please generate a high-level action node based on the following UI operation chain
information:
Task description:
{task description}
Chain operations:
{chain operations}
Chain element details:
{element details}
Chain reasoning results:
{reasoning results}
Please generate a concise description of the high-level action node, including the
following fields:
-action id: Generate a unique ID for the high-level action (format like:
"high level action xxx")
-name: Concise name of the high-level action
-function description: Brief description of the action’s functionality and purpose
-preconditions: Required conditions before executing this action, including:
* task state: What task context or state is needed
* page state: What page/interface state must be present
-post conditions: Resulting state after completing this action, including:
* task state: How the task context changes
* page state: What page/interface state is reached
-element sequence: Simplified sequence of key elements in this action:
* element id: Element ID
* atomic action: Action performed
* order: Execution order
26
