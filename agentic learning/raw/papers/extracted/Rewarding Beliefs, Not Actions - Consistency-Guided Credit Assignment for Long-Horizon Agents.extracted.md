# Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Horizon Agents - Extracted Text

- Source note: [[Rewarding Beliefs, Not Actions - Consistency-Guided Credit Assignment for Long-Horizon Agents]]
- Source PDF: `assets/Rewarding Beliefs, Not Actions - Consistency-Guided Credit Assignment for Long-Horizon Agents.pdf`
- Extracted: 2026-05-20
- Extractor: pypdf
- Pages: 25
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

Rewarding Beliefs, Not Actions: Consistency-Guided
Credit Assignment for Long-Horizon Agents
Wenjie Tang1 Minne Li2 Sijie Huang3 Liquan Xiao1 Yuan Zhou2∗
1College of Computer, National University of Defense Technology
2Intelligent Game and Decision Lab (IGDL)
3Institute of Artificial Intelligence, Xiamen University
Abstract
Reinforcement learning from verifiable rewards (RLVR) is a promising paradigm
for improving large language model (LLM) agents on long-horizon interactive tasks.
However, in partially observable environments, incomplete observations cause
agent beliefs to drift over time, while delayed rewards obscure the causal impact
of intermediate decisions, exacerbating temporal credit assignment challenges. To
address this, we propose ReBel (Reward Belief), a process-level reinforcement
learning algorithm that explicitly models structured belief states to summarize
interaction history and guide subsequent policy learning. ReBel introduces belief-
consistency supervision, converting discrepancies between predicted beliefs and
observed feedback into dense self-supervised signals without requiring external
step-wise annotations or verifiers. It also employs belief-aware grouping to compare
trajectories under similar belief states, yielding more robust and lower-variance
advantage estimates. We evaluate ReBel on challenging long-horizon benchmarks,
including ALFWorld and WebShop. ReBel improves task success by up to 20.4
percentage points over the episode-level baseline GRPO and increases sample
efficiency by 2.1×. These results suggest that belief-aware self-supervision is
a promising direction for reliable long-horizon decision-making under partial
observability. Code is available at: https://github.com/Fateyetian/
Rebel.git.
1 Introduction
Large language models (LLMs) are increasingly being deployed as autonomous agents for long-
horizon interactive tasks such as embodied instruction following and web navigation [ 4, 39, 44].
These settings require more than fluent generation: agents must maintain an evolving understanding
of the environment, plan over multiple steps, and adapt robustly under uncertainty [ 10, 25, 29].
Reinforcement learning from verifiable rewards (RLVR) has emerged as a promising paradigm for
improving such agents, because it optimizes policies directly against objective and environment-
grounded outcomes rather than relying on expensive human annotations or potentially unreliable
external judges [ 14, 18, 34]. Compared with LLM-as-a-judge or manually specified intermediate
labels, RLVR provides scalable supervision with clear task-level semantics [ 13, 43], making it
particularly attractive for training agents that must act reliably in open-ended environments [ 11, 30].
Despite its promise, RLVR remains difficult in partially observable environments, where agents must
continuously infer latent context from incomplete observation histories rather than direct access to
the full state [6]. Small inference errors can accumulate over time, inducing belief drift: a growing
mismatch between the agent’s internal state estimate and the environment [21, 25]. As illustrated
∗Corresponding author.
Preprint.
arXiv:2605.20061v1  [cs.CL]  19 May 2026

## Page 2

in Figure 6, an agent may confidently believe that the key is in a box, only to observe after opening
it that the box is actually empty. If the policy fails to revise this belief, it may repeatedly inspect
the wrong location and drive the trajectory progressively away from the goal [10]. Delayed terminal
rewards further obscure which intermediate belief errors caused the failure, making temporal credit
assignment especially challenging. Thus, effective policies must learn not only which actions to take,
but also when their latent state estimates should be trusted [9].
Existing RLVR methods are not well suited to this setting. Episode-level rewards are often too sparse
to correct intermediate belief errors, especially when failures are only revealed at the end of a long
trajectory [5, 12]. Step-wise supervision or external verifiers can provide denser feedback, but they are
costly, difficult to scale, and often unavailable in open-ended interactive tasks [7]. More importantly,
most existing approaches optimize trajectories primarily through return-based signals, without
explicitly modeling the agent’s evolving belief state [10, 25]. This makes it difficult to distinguish
failures caused by poor action selection from failures caused by incorrect state estimation [19]. In
partially observable long-horizon tasks, these two factors are tightly coupled, and ignoring belief
dynamics can lead to unstable optimization and poor sample efficiency [14, 17].
To address this challenge, we proposeReBel(Reward-Belief), a process-level reinforcement learning
framework for partially observable long-horizon tasks. The core insight is that effective credit
assignment in partially observable settings requires more than reward signals and demands explicit
supervision of belief dynamics that bridge observations and actions. Failures in long-horizon tasks
often stem from persistent internal misunderstandings rather than poor action selection. Concretely,
ReBel realizes this idea through two complementary design layers. First, it maintains a structured
belief representation that summarizes the agent’s inferred environment state from past interaction
history. Rather than attempting to reconstruct a complete latent world model, this representation cap-
tures task-relevant state predicates that are sufficient for decision making. Second, ReBel introduces
belief-consistency supervision, which converts mismatches between predicted beliefs and subsequent
environment observations into dense self-supervised feedback. This provides process-level correction
signals without requiring step-wise annotations or external verifiers. In addition, we design a belief-
aware grouping strategy that compares trajectories under similar belief states, enabling more robust
advantage estimation and reducing optimization variance. Together, these components form a closed
iterative learning loop in which more accurate beliefs induce more informative comparisons, which
in turn stabilize policy updates and further improve belief quality.
We evaluate ReBel on two partially observable long-horizon benchmarks: ALFWorld [ 33] for
embodied task planning under incomplete observations and WebShop [ 42] for goal-driven web
interactions under sparse delayed feedback. Using Qwen2.5-1.5B-Instruct [ 41], ReBel achieves
success rates of93.2±4.1% on ALFWorld [33] and 75.1±2.7% on WebShop [42], improving over the
strongest episode-level baseline GRPO [32] by 20.4 percentage points and over the strongest step-level
method GiGPOw/o std [11] by 7.1 and 7.7 percentage points on ALFWorld [33] and WebShop [42],
respectively. ReBel reaches GRPO’s [32] final performance in approximately 35 training iterations,
yielding a 2.1× sample-efficiency gain, all without requiring dense human annotations or external
step-wise verifiers. These results validate belief-aware RLVR as an effective framework for optimizing
LLM agents in partially observable long-horizon settings.
In summary, our main contributions are threefold:
1. We identify belief drift under partial observability as a key failure mode of RLVR in long-
horizon interactive tasks, where delayed rewards exacerbate temporal credit assignment.
2. We propose ReBel, a process-level reinforcement learning framework that combines struc-
tured belief representation, belief-consistency supervision, and belief-aware grouping to
provide dense self-supervised feedback without external step-wise verifiers.
3. We demonstrate substantial gains on ALFWorld [33] and WebShop [42], showing that ReBel
improves both task success and sample efficiency over strong episode-level and step-level
baselines.
2 Related Work
Reinforcement learning for LLM agents.As large language models (LLMs) are increasingly
deployed as autonomous agents in program synthesis, embodied control, device interaction, and
2

## Page 3

web navigation, reinforcement learning (RL) has become a central paradigm for improving their
decision-making behavior. Early RLHF methods, such as InstructGPT [ 26], demonstrated that
preference-based optimization can effectively align model outputs with human intent. More recent
work has shifted from single-turn response optimization toward trajectory-level learning in interactive
environments such as ALFWorld [33] and WebShop [42]. To improve exploration and long-horizon
reasoning, methods such as RAP [ 16] and Agent Q [ 27] incorporate Monte Carlo tree search
(MCTS [35]) into training or inference, while ArCHer [45] introduces history-aware value estimation
for agent trajectories. In parallel, critic-free optimization methods such as GRPO [32] and RLOO [1]
reduce optimization overhead and improve training efficiency. Recent systems including DigiRL [2],
WebRL [28], RAGEN [38], and LOOP [6] further demonstrate the promise of RL for end-to-end
device control and web interaction. Despite these advances, most existing methods still rely primarily
on terminal rewards or assume near-complete observability, which makes them vulnerable to severe
credit assignment challenges in partially observable long-horizon tasks.
Process supervision and belief modeling.A complementary line of work seeks to densify learning
signals by providing supervision at the process level rather than only at the final outcome. Process
supervision was advocated in early work by Uesato et al. [ 36] and Let’s Verify Step by Step [20],
which showed that intermediate verification can substantially improve reasoning and planning.
Building on this idea, recent methods such as Math-Shepherd [ 37], PRIME [8], and Watch Every
Step [40] explore automated or weakly supervised step-level reward construction, reducing reliance
on expensive human annotations. More agent-oriented methods, including GiGPO [11] and related
follow-up work [22, 46], further refine optimization at the step level by grouping trajectories and
estimating advantages over finer-grained units. However, these methods typically condition grouping
and reward estimation on the current observation alone, which can be brittle when the underlying
environment is only partially observed. In such settings, observation-conditioned grouping may
fail to reflect the agent’s latent state, leading to degraded grouping quality and unstable advantage
normalization. In parallel, work on partially observable decision making has explored belief-centric
approaches through retrieval augmentation [15], symbolic augmentation [23], and broader augmented
LM paradigms [24], as well as intrinsic motivation mechanisms such as curiosity [31] and random
network distillation [3]. While these methods can improve representation learning or exploration,
they do not directly couple belief evolution with process-level optimization. ReBel addresses this
gap by turning belief consistency into a dense self-supervised training signal, thereby aligning policy
optimization with latent state tracking in partially observable long-horizon tasks.
3 Method
Reinforcement learning with verifiable rewards (RLVR) has significantly improved the performance
of large language model (LLM) agents on long-horizon tasks. However, extending this paradigm
to partially observable environments remains challenging, primarily because the agent’s internal
reasoning process is not directly transparent. Outcome-based optimization such as vanilla GRPO [32]
provides only sparse terminal feedback, making it difficult to distinguish a logically sound trajectory
from one that merely succeeds by chance. Action-centered process reward models alleviate this
sparsity to some extent, but they often remain insensitive to the underlying belief state and may
therefore reinforce actions driven by incorrect internal assumptions. We refer to this phenomenon
ascredit drift, where spurious successes contaminate credit assignment and lead to high-variance
updates as well as poor generalization.
To address this issue, we proposeReBel(RewardingBelief), a framework that shifts process
supervision from what the agent does to why it believes an action should work. ReBel introduces
a two-level supervision structure: (i)consistency-based supervision, which penalizes mismatches
between the agent’s predicted belief state and subsequent observations; and (ii)belief-anchored
advantage estimation, which compares actions only within semantically aligned belief clusters.
Together, these components enable process-level optimization that explicitly aligns policy learning
with latent-state tracking in partially observable long-horizon tasks.
3.1 Belief-Structured Interaction in POMDPs
We consider the general setting in which large language model (LLM) agents perform multi-step
tasks in a partially observable Markov decision process (POMDP). The process is defined by the tuple
3

## Page 4

Figure 1:Overview of ReBel.ReBel learns belief-aware policies for partially observable long-
horizon tasks by making latent belief explicit and decomposing policy generation into belief, think,
and action. It turns sparse terminal rewards into step-wise belief consistency feedback and performs
belief-anchor grouping to support stable step-level advantage estimation.
(S,A,Ω,T,O,R, γ) , where S denotes the latent state space, A the action space, Ω the observation
space, T the transition kernel, O the observation model, R the reward function, and γ the discount
factor. Given a task instruction x∈ X, the agent receives a local observation ot ∈Ω at each discrete
time step t= 1, . . . , T. Since the underlying environment state st ∈ Sis not directly accessible,
the agent must reason over a history trace ht = (o1, a1, o2, a2, . . . , at−1, ot), which records both
observations and prior decisions. At each interaction step, the policy πθ generates a structured output
field yt = (bt, zt, at), where bt denotes a structured belief, zt an intermediate thought state, and
at ∈ Aan executable action. The environment then returns a scalar reward rt ∈R . In realistic
long-horizon scenarios, reward signals are typically extremely sparse and delayed, often appearing
only at the end of an episode as a terminal indicator of success or failure. When a single trajectory
spans thousands of tokens, credit assignment is no longer merely a sparse-reward problem; rather, it
becomes an attribution problem across a long generation chain and multiple internal decisions. In
particular, it is often difficult to determine whether the final outcome should be attributed to a specific
observation interpretation, an intermediate reasoning step, or a particular action choice.
To address this challenge, ReBel does not directly map history to actions in an end-to-end manner.
Instead, it explicitly reconstructs each generation step as a Belief-Think-Action process. Specifically,
before executing an action, the agent first constructs a structured beliefbt from the history ht and task
instruction x, where bt explicitly encodes the agent’s assessment of the current environment state.
The agent then performs internal reasoning conditioned onbt to produce an intermediate thought state
zt, and finally outputs an executable actiona t based on bothb t andz t. This process is factorized as
πθ(bt, zt, at |h t, x) =πθ(bt |h t, x)πθ(zt |h t, x, bt)π θ(at |h t, x, bt, zt).(1)
Here, bt ⊆P={p 1, . . . , pK} denotes a task-relevant belief set composed of predefined predicates.
It is worth noting that bt is not the Bayesian posterior belief in the standard POMDP sense, but rather
a symbolic approximation of the current environment state, used to explicitly represent the agent’s
state assessment. Unlike methods that compress internal reasoning into a single latent variable, we
explicitly model beliefbt, thought zt, and actionat, thereby making the intermediate cognitive process
directly supervisable. Accordingly, training signals can come not only from trajectory-level outcomes,
but also from intermediate beliefs, reasoning processes, and action decisions. By organizing the
generation process asb t →z t →a t, ReBel converts the credit assignment problem in long-horizon
tasks into local constraints on the consistency between intermediate beliefs and subsequent behaviors,
thereby providing a more stable learning signal.
4

## Page 5

3.2 Belief Consistency Supervision
The effectiveness of explicit belief lies not in its static representation, but in whether it can remain
consistent with evidence generated through environmental evolution over time. Based on this insight,
ReBel introduces an observation-based dense supervision mechanism that decomposes sparse terminal
feedback into step-wise belief consistency evaluations, enabling belief quality to be optimized at
each time step. Let P={p 1, . . . , pK} denote the set of task-relevant predicates. We represent
the belief at time step t as a binary vector over the predicate space, bt ∈ {0,1}K, where bt,k = 1
indicates that the agent believes predicate pk to be true at time t, and bt,k = 0 indicates it to be
false. To characterize the consistency between belief and observations, we define a consistency
indicator function Ck(bt, at, ot+1)∈ {0,1}, which determines whether the judgment on predicate pk
encoded in bt can be supported by the next observation ot+1 after executing action at. Here, action
at influences observations indirectly by inducing state transitions in the environment; therefore, Ck
measures whether the current belief remains supported by evidence after environmental evolution.
Since not all predicates are verifiable at every time step, we further introduce an observability mask
mt ∈ {0,1}K, where mt,k = 1 indicates that predicate pk can be checked against observation ot+1,
and mt,k = 0 indicates that the predicate is temporarily unverifiable at the current step. Based on this
mask, the belief consistency reward is defined as
rcons
t =
PK
k=1 mt,kCk(bt, at, ot+1)
PK
k=1 mt,k
if
KX
k=1
mt,k >0.
When PK
k=1 mt,k = 0, the consistency reward is undefined for that step. This treatment avoids
interpreting an unverifiable state as inconsistent, ensuring that the supervision signal is derived only
from observable evidence. In other words, a time step contributes to consistency supervision only
when at least one predicate is checkable; for belief items that are temporarily unobservable, no
additional training bias is imposed.
To handle predicates that become verifiable only after a delay, we maintain a pending belief buffer
that stores historical belief items for which no validation evidence has yet been obtained. We define
Ut =
(
(pk, t′)
bt′,k = 1, t′ ≤t,
tX
τ=t′
mτ,k = 0
)
,
where Ut denotes the set of belief items that have not yet been validated by observation up to
time step t. If a predicate is not observable when it is generated, the corresponding belief is
buffered and excluded from reward computation. Once the predicate becomes observable later, its
consistency signal is assigned to the original generation step t′. This mechanism enables temporal
credit assignment for delayed evidence beyond single-step observability.
3.3 Belief-Anchor Step-wise Advantage
While group-based reinforcement learning reduces variance through relative benchmarking across
trajectories, relying solely on terminal feedback in partially observable long-horizon tasks leads to
severecredit drift, making it difficult to identify the true contribution of specific steps within a se-
quence. Although introducing step-wise advantage estimation could refine process-level supervision,
it encounters thesingleton group problemin POMDP scenarios: since the environment state s is
not directly observable and long-horizon trajectories are highly unique in physical space, different
trajectories rarely encounter identical physical states at the same time step. Consequently, state-based
grouping often collapses into isolated samples, causing local relative advantage signals to fail due to
a lack of comparable benchmarks.
To overcome this bottleneck, ReBel shifts the benchmark for credit assignment from the unobservable
physical state s to an explicitbelief anchor b. The core logic of this shift is that, in partially observable
environments, the prerequisite for evaluating action quality is no longer “external consistency” but
rather “internal cognitive equivalence.” As long as the agent’s belief predicate setsbt are logically
equivalent, action choices across different trajectories share a common semantic background for
benchmarking. Specifically, let the i-th trajectory be τi ={(o i,t, bi,t, zi,t, ai,t, renv
i,t , rcons
i,t )}Ti
t=1. We
define the step-wise total reward as rtot
i,t =r env
i,t +ηr cons
i,t , and its corresponding step-wise discounted
5

## Page 6

return as Gstep
i,t = PTi
k=t γk−trtot
i,k . This return not only reflects the action’s contribution to the final
task goal but also captures its immediate maintenance of cognitive accuracy throughr cons
i,t .
Next, we leverage the symbolic representation of the predicate spaceP to aggregate trajectory nodes—
which are otherwise isolated in physical state space—into semantically consistent comparison groups.
For a belief anchor ˜b∈ {0,1}K, its corresponding step-wise group is defined as GS(˜b) ={(i, t)|
bi,t = ˜b}. Since belief representations are semantic abstractions of complex physical states, this
anchoring mechanism significantly increases the coverage of comparable samples, thereby resolving
the singleton group problem. On this basis, we define the belief-anchored step-wise advantage as:
AS(i, t) =
(
0,|G S(bi,t)|= 1
Gstep
i,t −µ(GS(bi,t))
σ(GS(bi,t))+ϵ ,otherwise (2)
where µ and σ denote the mean and standard deviation of returns within the group GS, respectively.
This mechanism achieves the following core advantages through cognitive benchmarking:
• Explicit Decoupling of Decision and Cognition:By comparing actions within the same belief
anchor, the model can tell whether low return comes from wrong reasoning or from a poor action
choice. This helps the agent learn the best action under its current belief.
• Learning Resilience under Sparse Feedback:When the environment reward is zero for all
samples in a group, the relative advantage still captures small differences in belief maintenance.
This lets the model strengthen actions that keep the belief correct and reduce belief drift.
In summary, Belief-Anchor Step-wise Advantage transforms credit assignment from blind competition
over outcomes into precise selection under logically equivalent conditions. It provides a more stable
process-level supervision signal that aligns with the nature of decision-making for long-horizon
agents in partially observable environments.
3.4 Belief-aware Policy Optimization
ReBel optimizes a belief-aware policy by combining trajectory-level outcome signals with belief-
anchor step-wise advantages. For the i-th trajectory τi and time step t= 1, . . . , Ti, we define the
total advantage as Atot
i,t =A E(τi) +ωA S(i, t), where AE(τi) captures the relative terminal quality
of the trajectory within its group, AS(i, t)measures the relative quality of the current step under the
same belief anchor, andω≥0balances the two terms.
J(θ) =E τi∼πθold
"
1
Ti
TiX
t=1

min
 
ρi,t(θ)Atot
i,t ,clip(ρ i,t(θ),1−ϵ,1 +ϵ)A tot
i,t

−βD KL
 
πθ(· |hi,t)∥πref(· |hi,t)
#
.
(3)
Here, ϵ controls the clipping range and β regularizes the deviation from the reference policy πref.
The importance ratio is defined over the joint generation of belief, thought, and action as
ρi,t(θ) = πθ(bi,t, zi,t, ai,t |h i,t)
πθold (bi,t, zi,t, ai,t |h i,t).(4)
Using the Belief-Think-Action factorization, πθ(bi,t, zi,t, ai,t |h i,t) =π θ(bi,t |h i,t)πθ(zi,t |
hi,t, bi,t)πθ(ai,t |h i,t, bi,t, zi,t), this objective propagates learning signals to belief formation, inter-
nal reasoning, and action selection, rather than to the final action alone. As a result, ReBel assigns
credit not only to successful outcomes, but also to belief-consistent intermediate decisions, enabling
temporally grounded credit assignment in partially observable long-horizon tasks.
4 Experiments
We structure our experiments around three questions: (i) whether REBELoutperforms strong baselines
in partially observable environments; (ii) how much each of its main components contributes to
6

## Page 7

Table 1: Performance comparison on ALFWorld [ 33] and WebShop [ 42]. All RL methods are
initialized from Qwen2.5-1.5B-Instruct [41]; results are reported as mean±std over 3 random seeds.
Bold: best result among RL-trained methods. ALFWorld [33] reports per-task and overall success
rate (%); WebShop [42] reports average score and task success rate (%). †: initialized with SFT
warm start on belief-annotated data; the isolated contribution of SFT warm start is quantified in
Appendix E.2.
Paradigm Method ALFWorld WebShop
Pick Look Clean Heat Cool Pick2 Overall Score SR
Closed-source frontier models (zero-shot reference)
Prompt GPT-4o 75.3 60.8 31.2 56.7 21.6 49.8 48.0 31.8 23.7
Prompt Gemini-2.5-Pro 92.8 63.3 62.1 69.0 26.6 58.7 60.3 42.5 35.9
Prompt-based agents (Qwen2.5-1.5B-Instruct)
Prompt Qwen2.5 5.9 5.5 3.3 9.7 4.2 0.0 4.1 23.1 5.2
Prompt ReAct 17.4 20.5 15.7 6.2 7.7 2.0 12.8 40.1 11.3
Prompt Reflexion 35.3 22.2 21.7 13.6 19.4 3.7 21.8 55.8 21.9
RL-trained agents (Qwen2.5-1.5B-Instruct, 3 seeds)
RL PPO 64.8 ±3.5 40.5±6.9 57.1±4.9 60.6±6.6 46.4±4.0 47.4±1.9 54.4±3.1 73.8±3.0 51.5±2.9
RL RLOO 88.3 ±3.0 52.8±8.6 71.0±5.9 62.8±8.7 66.4±5.5 56.9±4.7 69.7±2.5 73.9±5.6 52.1±6.7
RL GRPO 85.3 ±1.5 53.7±8.0 84.5±6.8 78.2±7.9 59.7±5.0 53.5±5.6 72.8±3.6 75.8±3.5 56.8±3.8
RL GiGPO w/std 94.4±5.9 67.5±4.6 94.8±3.8 94.4±7.8 79.8±4.7 76.4±5.4 86.7±1.7 83.1±1.6 65.0±3.2
RL GiGPO w/o std 96.0±1.4 76.5±3.9 91.8±5.5 91.3±6.3 71.7±8.4 79.5±7.7 86.1±4.7 83.5±1.8 67.4±4.5
RL ReBel (Ours)†91.8±2.1 84.2±4.3 91.3±3.1 95.8±4.3 84.8±4.2 96.5±3.2 93.2±4.1 79.8±2.8 75.1±2.7
performance; and (iii) whether REBELimproves sample efficiency and mitigates belief drift in
long-horizon decision making.
4.1 Experimental Setup
We evaluate REBELon ALFWorld [ 33] and WebShop [ 42], two representative benchmarks for
partially observable decision making. We compare against closed-source frontier models, prompt-
based open-source agents, and RL-trained baselines, covering zero-shot prompting, in-context
reasoning, and policy optimization settings. All methods use Qwen2.5-1.5B-Instruct [ 41] as the
backbone model, and REBELis initialized with an SFT warm start before RL training to stabilize
the structured ⟨belief⟩ output format. Unless otherwise specified, all results are reported as mean
± standard deviation. Additional dataset statistics, baseline descriptions, hyperparameters, and
implementation details are provided in Appendix A.
4.2 Main Results
Table 1 shows that REBELestablishes a new performance frontier, achieving an overall success
rate of 93.2±4.1% on ALFWorld [33] and 75.1±2.7% on WebShop [42]. Compared with the
strongest episode-level baseline, GRPO [32], this corresponds to improvements of +20.4 and +18.3
percentage points, respectively. Although closed-source frontier models such as Gemini-2.5-Pro
and GPT-4o exhibit strong general reasoning capabilities, their performance on these long-horizon
partially observable tasks remains substantially lower than that of RL-trained agents, suggesting
that generic zero-shot reasoning is insufficient for maintaining state coherence over long trajectories.
Prompt-based agents such as ReAct and Reflexion perform even worse, indicating that without
parameter updates, errors accumulate rapidly in these environments.
REBELalso consistently outperforms the strongest step-level baseline, GiGPOw/o std [11], by +7.1
points on ALFWorld [33] and +7.7 points on WebShop [42]. This gain suggests that belief-based
credit assignment provides a more semantically stable learning signal than observation-hash grouping,
which can conflate distinct latent states under surface-level similarity. In contrast, REBELpropagates
supervision through structured belief representations, enabling the model to distinguish temporally
separated but semantically related decisions.
The benefits of REBELare further reflected in its sample efficiency and robustness on harder tasks.
As shown in Figure 2(a), REBELmatches the final performance of GRPO [ 32] after only about
35 training iterations, corresponding to an approximate 2.1× improvement in sample efficiency.
Moreover, Figure 2(b) and (c) show that the performance gap between REBELand GRPO [ 32] grows
with task difficulty and trajectory length. In the most challenging ALFWorld [33] task,Pick2, which
7

## Page 8

0 25 50 75 100
Training Epoch
0
20
40
60
80
100Validation Success Rate (%)
×2.1 sample
eff. (epoch~45)
(a) ALFWorld Training Curve
ReBel  93.2%
GRPO  60.9%
GiGPO  83.6%
Pick &
Place
Clean
& Place
Heat
& Place
Cool
& Place
Look at
in Light
Pick×2
& Place
0
20
40
60
80
100Success Rate (%)
+6 +7
+18
+25 +30
+43
85 84
78
60
54 54
94 95 94
80
68
76
92 91 96
85 84
96
(b) Per-Task Success Rate
(sorted by trajectory length,   = ReBel  GRPO)
GRPO
GiGPO
ReBel
10 20 30 40 50
T ask Difficulty (100  GRPO SR, %)
0
10
20
30
40
50ReBel  GRPO Gain (pp)
Pick & PlaceClean & Place
Heat & Place
Cool & Place
Look at in Light
Pick×2 & Place
x-axis: 3-seed avg GRPO SR
(c) Gain Scales with
Task Difficulty
Trend  0.88 pp/pp
~10s ~13s ~13s ~14s ~17s ~21s
Est. Avg. Trajectory Length
Figure 2:Training dynamics and per-task performance.(a) ALFWorld [ 33] training curves.
REBELreaches the final GRPO [ 32] performance after roughly 35 iterations, corresponding to an
approximate 2.1× improvement in sample efficiency. (b) Per-task success rates on ALFWorld [33],
sorted by estimated trajectory length; ∆ denotes the improvement of REBELover GRPO [ 32]. (c)
The gain of REBELover GRPO [ 32] increases with task difficulty, indicating that structured belief
tracking is more beneficial in harder partially observable tasks.
requires the longest reasoning chain, REBELachieves a success rate of 96.5%, outperforming the best
GiGPO [11] variant by +17.0 points. Overall, these results indicate that structured belief tracking is
a key factor behind REBEL’s gains in partially observable long-horizon decision making.
4.3 Ablation Study
Table 2:Incremental ablation from GRPO [ 32]
to full REBEL.B0–B3 incrementally add the
main modules in a stepwise fashion. B0 is the
GRPO [32] baseline initialized from SFT, and each
later variant adds one new component to measure
its contribution to the final performance.
Method Prompt Group Step
Adv.
Belief
Reward ALFWorld
B0: GRPO× × × ×60.9
B1: + Prompt✓× × ×78.1
B2: + Group✓ ✓ ✓×93.0
B3: REBEL✓ ✓ ✓ ✓96.9
Table 2 decomposes the performance gains of
REBELinto three key factors: explicit repre-
sentation, fine-grained credit assignment, and
consistency supervision. Moving from vanilla
GRPO [32] (B0) to the belief-prompted variant
(B1) yields a 17.2% improvement, indicating
that making latent state tracking explicit through
structured reasoning alleviates the burden of en-
coding history in internal memory. However, al-
though B1 improves the representational form, it
still relies primarily on high-variance trajectory-
level rewards; as the task horizon increases, such
rewards become increasingly insufficient for pro-
viding precise optimization guidance.
The most substantial improvement occurs with B2 (93.0%). This variant mitigates credit diffusion
in long-horizon tasks through belief-aligned semantic grouping and step-wise advantage ( Astep).
Specifically, by providing dense optimization signals over belief equivalence classes, the model can
more accurately identify critical intermediate subgoals. As shown in Figure 2b, this fine-grained
feedback is particularly effective in long-horizon tasks such asPickx2 & Place, where trajectory-level
rewards are often diluted by noise from lengthy action sequences. This mechanism also explains the
2.1×gain in sample efficiency observed during the early stages of training in Figure 2a.
The full REBELmodel (B3, 96.9%) stabilizes the reasoning–action loop through the auxiliary belief
reward rbel. This reward serves as an alignment anchor, preventing reasoning drift—a phenomenon
in which the agent may produce the correct action based on hallucinated state representations. By
continuously constraining the policy to remain grounded in the state space defined by environmental
predicates, rbel improves robustness in partially observable settings, with particularly clear benefits in
tasks with greater observation sparsity and deeper reasoning requirements (see Figure 2c). Overall,
these results show that the performance gains of REBELarise from the synergy of structured
representation (B1), fine-grained credit assignment (B2), and grounded supervision (B3).
8

## Page 9

20 40 60 80 100
Training Step (Epoch)
0
10
20
30
40
50
60
70Singleton Group Ratio (%)
ReBel final:
11.1%
(a) Grouping Quality: ReBel vs GiGPO over Training
(ReBel singleton  vs GiGPO avg group size [obs-hash, no improvement])
ReBel singleton ratio (rolling mean8)
GiGPO avg group size (rolling mean8)
20 40 60 80 100
Training Step (Epoch)
0
5
10
15
20
25
30Mean Episode Length (steps)
(b) Episode Length: ReBel vs GRPO vs GiGPO
(shorter = more goal-directed; reflects SR improvement)
ReBel (30 9.2 steps, ×3.3)
GRPO (30 16.9 steps, ×1.8)
GiGPO (30 11.4 steps, ×2.6)
0 5 10 15 20 25 30 35 40
Cumulative Env Interactions (K steps)
0
20
40
60
80
100Rollout Success Rate (%)
ReBel
20K
GiGPO
32K
GRPO
<85%
(c) Sample Efficiency: SR vs Cumulative Env Interactions
(ReBel reaches 85% SR using ×1.6 fewer env steps than GiGPO)
ReBel  (29K steps, 96% SR)
GiGPO  (34K steps, 84% SR)
GRPO   (40K steps, 68% SR)
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
20.0
GiGPO Avg Group Size (steps)
GiGPO: ~11.5 (flat)
Figure 3:Grouping quality and training efficiency.(a) Singleton ratio for REBELand GiGPO [ 11]
during training. The average group size for GiGPO [ 11] is shown on the right axis. (b) Average
episode length on ALFWorld [33]. REBELreduces the average episode length from about 29.9 steps
to 9.2 steps, a 3.2× reduction. (c) Success rate versus cumulative environment interactions. REBEL
reaches 85% rollout success with roughly 1.6× fewer environment steps than GiGPO [11] and earlier
than GRPO [32].
4.4 Grouping Quality and Efficiency
Why grouping quality matters: it determines the usefulness of credit assignment.As shown
in Figure 3(a), GiGPO [11] produces a relatively high fraction of singleton groups during training,
indicating that many states cannot be stably aggregated into semantically coherent sets. An excessive
number of singleton groups weakens step-wise normalization and makes advantage estimates more
susceptible to noise. In contrast, REBELconsistently maintains a low singleton ratio, while the
average group size increases steadily throughout training, suggesting that it can continuously form
more stable and semantically coherent belief-based groups. In other words, REBELdoes not merely
create more groups. It forms groups that are more stable and semantically coherent.
Better grouping quality translates into higher task execution efficiency.Figure 3(b) shows that
REBELreduces the average episode length on ALFWorld [ 33] from about 29.9 steps to 9.2 steps,
corresponding to a 3.2× reduction. This means that the model can form effective sub-goal strategies
faster and complete tasks with fewer decision steps. By comparison, GiGPO [11] yields only modest
improvements, while GRPO [32] shows almost no reduction. This result suggests that higher-quality
grouping not only improves credit assignment, but also makes it easier for the policy to learn efficient
behavioral paths, such as more accurate object selection and more compact action sequences.
At the training level, this advantage further manifests as higher sample efficiency and faster
convergence.Figure 3(c) plots the success rate as a function of cumulative environment interac-
tions. To reach 85% rollout success, REBELrequires roughly 1.6 × fewer environment steps than
GiGPO [11] and reaches this level earlier than GRPO [32]. Meanwhile, REBEL’s convergence curve
is smoother and its confidence band is narrower, indicating a more stable training process. Overall,
Figures 3(a)–(c) form a clear chain. Better belief grouping leads to more reliable credit assignment.
This shortens task execution and ultimately improves sample efficiency and convergence.
5 Conclusion
We introduce REBEL, a process-supervised reinforcement learning framework that opens a new and
promising path toward addressing credit assignment in long-horizon agentic tasks by optimizing
explicit belief-state consistency, marking a shift from purely outcome-driven optimization to deeper
process-level alignment. Rather than relying solely on terminal rewards, REBELprovides dense
step-level supervision through the belief-consistency reward to effectively mitigate cascading failures,
while employing a belief-grouping mechanism to identify semantically coherent phases in partially
observable environments and enable more precise advantage normalization. Experimental results
show that, using only a 1.5B-parameter backbone, REBELachieves success rates of 93.2% on ALF-
World and 75.1% on WebShop, marking substantial improvements of +20.4 and +18.3 percentage
points over the strong GRPO baseline, while enhancing sample efficiency by 2.1×. Our ablation
studies further confirm that the integration of belief consistency and semantic grouping produces
additive performance gains, underscoring that the self-alignment of an agent’s internal world model
is essential for achieving efficient and robust autonomous intelligence.
9

## Page 10

References
[1] Arash Ahmadian, Chris Cremer, Matthias Gallé, Marzieh Fadaee, Julia Kreutzer, Olivier
Pietquin, Ahmet Üstün, and Sara Hooker. Back to basics: Revisiting reinforce-style optimization
for learning from human feedback in llms. InProceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), pages 12248–12267, 2024.
[2] Hao Bai, Yifei Zhou, Mert Cemri, Jiayi Pan, Alane Suhr, Sergey Levine, and Aviral Kumar.
Digirl: Training in-the-wild device-control agents with autonomous reinforcement learning.
Advances in Neural Information Processing Systems, 37:12461–12495, 2024.
[3] Yuri Burda, Harrison Edwards, Amos Storkey, and Oleg Klimov. Exploration by random
network distillation.arXiv preprint arXiv:1810.12894, 2018.
[4] Shiyi Cao, Dacheng Li, Fangzhou Zhao, Shuo Yuan, Sumanth R Hegde, Connor Chen, Charlie
Ruan, Tyler Griggs, Shu Liu, Eric Tang, et al. Skyrl-agent: Efficient rl training for multi-turn
llm agent.arXiv preprint arXiv:2511.16108, 2025.
[5] Bolin Chen, Ru-Ling Liao, Yan Ye, Jie Chen, Shanzhi Yin, Xinrui Ju, Shiqi Wang, and Yibo
Fan. Sparse2dense: A keypoint-driven generative framework for human video compression and
vertex prediction, 2025. URLhttps://arxiv.org/abs/2509.23169.
[6] Kevin Chen, Marco Cusumano-Towner, Brody Huval, Aleksei Petrenko, Jackson Hamburger,
Vladlen Koltun, and Philipp Krähenbühl. Reinforcement learning for long-horizon interactive
llm agents.arXiv preprint arXiv:2502.01600, 2025.
[7] Youngbin Choi, Min Jae Lee, Saemi Moon, Seunghyuk Cho, C. Chung, Moon Jeong Park, and
Dongwoo Kim. In-place feedback: A new paradigm for guiding llms in multi-turn reasoning.
ArXiv, abs/2510.00777, 2025.
[8] Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Yuchen Zhang, Wendi Li, Bingxiang
He, Yuchen Fan, Tianyu Yu, Qixin Xu, Weize Chen, Jiarui Yuan, Huayu Chen, Kaiyan Zhang,
Xingtai Lv, Shuo Wang, Yuan Yao, Xu Han, Hao Peng, Yu Cheng, Zhiyuan Liu, Maosong
Sun, Bowen Zhou, and Ning Ding. Process reinforcement through implicit rewards.ArXiv,
abs/2502.01456, 2025.
[9] LI DU, Zhouhao Sun, Xiao Ding, Yixuan Ma, Yang Zhao, Kaitao Qiu, Ting Liu, and Bing Qin.
Causal-guided active learning for debiasing large language models.ArXiv, abs/2408.12942,
2024.
[10] Jinhao Duan, James Diffenderfer, Sandeep Madireddy, Tianlong Chen, Bhavya Kailkhura,
and Kaidi Xu. Uprop: Investigating the uncertainty propagation of llms in multi-step agentic
decision-making.ArXiv, abs/2506.17419, 2025.
[11] Lang Feng, Zhenghai Xue, Tingcong Liu, and Bo An. Group-in-group policy optimization for
llm agent training, 2025. URLhttps://arxiv.org/abs/2505.10978.
[12] Jiayi Fu, Xuandong Zhao, Chengyuan Yao, Heng Wang, Qi Han, and Yanghua Xiao. Reward
shaping to mitigate reward hacking in rlhf, 2026. URL https://arxiv.org/abs/2502.
18770.
[13] Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan
Shen, Shengjie Ma, Honghao Liu, Sai Wang, Kun Zhang, Zhouchi Lin, Bowen Zhang, Li-Hua
Ni, Wen yuan Gao, Yuanzhuo Wang, and Jian Guo. A survey on llm-as-a-judge.The Innovation,
2026.
[14] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu,
Ruoyu Zhang, Shirong Ma, Xiao Bi, et al. Deepseek-r1 incentivizes reasoning in llms through
reinforcement learning.Nature, 645(8081):633–638, 2025.
[15] Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, and Mingwei Chang. Retrieval
augmented language model pre-training. InInternational conference on machine learning,
pages 3929–3938. PMLR, 2020.
10

## Page 11

[16] Shibo Hao, Yi Gu, Haodi Ma, Joshua Hong, Zhen Wang, Daisy Wang, and Zhiting Hu. Reason-
ing with language model is planning with world model. InProceedings of the 2023 Conference
on Empirical Methods in Natural Language Processing, pages 8154–8173, 2023.
[17] Byunghyun Kim, Minyoung Bae, and Jae-Gil Lee. Sample-Efficient Multi-Round Generative
Data Augmentation for Long-Tail Instance Segmentation. InAdvances in Neural Informa-
tion Processing Systems, 2025. URL https://mlanthology.org/neurips/2025/
kim2025neurips-sampleefficient/.
[18] Nathan Lambert, Jacob Daniel Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison,
Faeze Brahman, Lester James Validad Miranda, Alisa Liu, Nouha Dziri, Xinxi Lyu, Yuling
Gu, Saumya Malik, Victoria Graf, Jena D. Hwang, Jiangjiang Yang, Ronan Le Bras, Oyvind
Tafjord, Christopher Wilhelm, Luca Soldaini, Noah A. Smith, Yizhong Wang, Pradeep Dasigi,
and Hanna Hajishirzi. Tülu 3: Pushing frontiers in open language model post-training.ArXiv,
abs/2411.15124, 2024.
[19] Aly Lidayan, Jakob Bjorner, Satvik Golechha, Kartik Goyal, and Alane Suhr. Abbel: Llm
agents acting through belief bottlenecks expressed in language.ArXiv, abs/2512.20111, 2025.
[20] Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee,
Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. InThe
twelfth international conference on learning representations, 2023.
[21] Bang Liu, Xinfeng Li, Jiayi Zhang, Jinlin Wang, Tanjin He, Sirui Hong, Hongzhang Liu,
Shaokun Zhang, Kaitao Song, Kunlun Zhu, Yuheng Cheng, Suyuchen Wang, Xiaoqiang Wang,
Yuyu Luo, Haibo Jin, Peiyan Zhang, Ollie Liu, Jiaqi Chen, Huan Zhang, Zhaoyang Yu, Haochen
Shi, Boyan Li, Dekun Wu, Fengwei Teng, Xiaojun Jia, Jiawei Xu, Jinyu Xiang, Yizhang Lin,
Tianming Liu, Tongliang Liu, Yu Su, Huan Sun, Glen Berseth, Jianyun Nie, Ian Foster, Logan
Ward, Qingyun Wu, Yu Gu, Mingchen Zhuge, Xinbing Liang, Xiangru Tang, Haohan Wang,
Jiaxuan You, Chi Wang, Jian Pei, Qiang Yang, Xiaoliang Qi, and Chenglin Wu. Advances and
challenges in foundation agents: From brain-inspired intelligence to evolutionary, collaborative,
and safe systems, 2025. URLhttps://arxiv.org/abs/2504.01990.
[22] Xiaoqian Liu, Ke Wang, Yuchuan Wu, Fei Huang, Yongbin Li, Junge Zhang, and Jianbin Jiao.
Agentic reinforcement learning with implicit step rewards.arXiv preprint arXiv:2509.19199,
2025.
[23] Gengchen Mai, Yingjie Hu, Song Gao, Ling Cai, Bruno Martins, Johannes Scholz, Jing Gao,
and Krzysztof Janowicz. Symbolic and subsymbolic geoai: Geospatial knowledge graphs and
spatially explicit machine learning.Trans. GIS, 26(8):3118–3124, 2022.
[24] Grégoire Mialon, Roberto Dessì, Maria Lomeli, Christoforos Nalmpantis, Ram Pasunuru,
Roberta Raileanu, Baptiste Rozière, Timo Schick, Jane Dwivedi-Yu, Asli Celikyilmaz, et al.
Augmented language models: a survey.arXiv preprint arXiv:2302.07842, 2023.
[25] Changdae Oh, Seongheon Park, To Eun Kim, Jiatong Li, Wendi Li, Samuel Yeh, Xuefeng Du,
Hamed Hassani, Paul Bogdan, Dawn Xiaodong Song, and Sharon Li. Uncertainty quantification
in llm agents: Foundations, emerging challenges, and opportunities. 2026.
[26] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin,
Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to
follow instructions with human feedback.Advances in neural information processing systems,
35:27730–27744, 2022.
[27] Pranav Putta, Edmund Mills, Naman Garg, Sumeet Motwani, Chelsea Finn, Divyansh Garg, and
Rafael Rafailov. Agent q: Advanced reasoning and learning for autonomous ai agents.arXiv
preprint arXiv:2408.07199, 2024.
[28] Zehan Qi, Xiao Liu, Daniel Hao, Kehai Peng, Maosong Sun, and Zhiyuan Yang. Webrl:
Training llm web agents via self-evolving online curriculum reinforcement learning.arXiv
preprint arXiv:2411.02337, 2024.
11

## Page 12

[29] Zehan Qi, Xiao Liu, Iat Long Iong, Hanyu Lai, Xueqiao Sun, Wenyi Zhao, Yu Yang, Xinyue
Yang, Jiadai Sun, Shuntian Yao, et al. Webrl: Training llm web agents via self-evolving online
curriculum reinforcement learning.arXiv preprint arXiv:2411.02337, 2024.
[30] Cheng Qian, Emre Can Acikgoz, Qi He, Hongru Wang, Xiusi Chen, Dilek Hakkani-Tür, Gokhan
Tur, and Heng Ji. Toolrl: Reward is all tool learning needs.arXiv preprint arXiv:2504.13958,
2025.
[31] Jürgen Schmidhuber. A possibility for implementing curiosity and boredom in model-building
neural controllers. InProc. of the international conference on simulation of adaptive behavior:
From animals to animats, pages 222–227, 1991.
[32] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang,
Mingchuan Zhang, YK Li, Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical
reasoning in open language models.arXiv preprint arXiv:2402.03300, 2024.
[33] Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté, Yonatan Bisk, Adam Trischler, and
Matthew Hausknecht. Alfworld: Aligning text and embodied environments for interactive
learning.arXiv preprint arXiv:2010.03768, 2020.
[34] Yi Su et al. Crossing the reward bridge: Expanding RL with verifiable rewards across diverse
domains.arXiv preprint arXiv:2503.23829, 2025.
[35] Maciej ´Swiechowski, Konrad Godlewski, Bartosz Sawicki, and Jacek Ma´ndziuk. Monte carlo
tree search: A review of recent modifications and applications.Artificial Intelligence Review,
56(3):2497–2562, 2023.
[36] Jonathan Uesato, Nate Kushman, Ramana Kumar, Francis Song, Noah Siegel, Lisa Wang,
Antonia Creswell, Geoffrey Irving, and Irina Higgins. Solving math word problems with
process-and outcome-based feedback.arXiv preprint arXiv:2211.14275, 2022.
[37] Peiyi Wang, Lei Li, Zhihong Shao, Runxin Xu, Damai Dai, Yifei Li, Deli Chen, Y .Wu, and
Zhifang Sui. Math-shepherd: Verify and reinforce llms step-by-step without human annotations.
ArXiv, abs/2312.08935, 2023.
[38] Zihan Wang, Kangrui Wang, Qineng Wang, Pingyue Zhang, Linjie Li, Zhengyuan Yang, Xing
Jin, Kefan Yu, Minh Nhat Nguyen, Licheng Liu, et al. Ragen: Understanding self-evolution in
llm agents via multi-turn reinforcement learning.arXiv preprint arXiv:2504.20073, 2025.
[39] Zhiheng Xi, Jixuan Huang, Chenyang Liao, Baodai Huang, Honglin Guo, Jiaqi Liu, Rui
Zheng, Junjie Ye, Jiazheng Zhang, Wenxiang Chen, et al. Agentgym-rl: Training llm agents
for long-horizon decision making through multi-turn reinforcement learning.arXiv preprint
arXiv:2509.08755, 2025.
[40] Weimin Xiong, Yifan Song, Xiutian Chen, Hao Peng, Bryan Hooi, and Lexing Xie. Watch
every step! llm agent learning via iterative step-level process refinement.arXiv preprint
arXiv:2406.11176, 2024.
[41] Qwen An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan
Li, Dayiheng Liu, Fei Huang, Guanting Dong, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu,
Jianwei Zhang, Jianxin Yang, Jiaxin Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu,
Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji
Lin, Tianhao Li, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yi-Chao
Zhang, Yunyang Wan, Yuqi Liu, Zeyu Cui, Zhenru Zhang, Zihan Qiu, Shanghaoran Quan, and
Zekun Wang. Qwen2.5 technical report.ArXiv, abs/2412.15115, 2024.
[42] Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. Webshop: Towards scalable
real-world web interaction with grounded language agents.Advances in Neural Information
Processing Systems, 35:20744–20757, 2022.
[43] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang,
Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and
chatbot arena.Advances in neural information processing systems, 36:46595–46623, 2023.
12

## Page 13

[44] Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng,
Tianyue Ou, Yonatan Bisk, Daniel Fried, et al. Webarena: A realistic web environment for
building autonomous agents.arXiv preprint arXiv:2307.13854, 2023.
[45] Yifei Zhou, Andrea Zanette, Jiayi Pan, Sergey Levine, and Aviral Kumar. Archer: Training
language model agents via hierarchical multi-turn rl.arXiv preprint arXiv:2402.19446, 2024.
[46] Zhuoran Zhuang, Ye Chen, Jianghao Su, Chao Luo, Luhui Liu, and Xia Zeng. Enhancing
agentic rl with progressive reward shaping and value-based sampling policy optimization, 2025.
URLhttps://arxiv.org/abs/2512.07478.
13

## Page 14

A Experimental Details
A.1 Computational Details
For both ALFWorld and WebShop, we conduct experiments on 4 ×A800 GPUs using
Qwen2.5-1.5B-Instruct as the base model. Each setting is trained for 100 iterations. During
inference, we use vLLM as the rollout backend with tensor parallelism set to 1 and GPU memory
utilization fixed at 0.65. Unless otherwise specified, all methods are evaluated under the same training
budget and environment configuration to ensure a fair comparison.
A.2 Dataset Details
A.2.1 ALFWorld
We evaluate our method on ALFWorld, a text-based embodied interaction benchmark designed to
assess language models in multi-step decision-making scenarios. Unlike static question answering
tasks, ALFWorld features a dynamic environment in which the state evolves in response to the agent’s
actions. At each step, the model must condition on the current observation, historical trajectory,
and task goal to decide the next action. As a result, the benchmark not only tests natural language
instruction following, but also challenges the model’s state tracking, planning, and error correction
capabilities in a changing environment.
ALFWorld contains 3,827 task instances spanning six representative household sub-tasks: Pick
& Place, Examine in Light, Clean & Place, Heat & Place, Cool & Place, and Pick Two & Place.
These sub-tasks differ substantially in action dependency structure, completion conditions, and
state-transition patterns. Following the standard protocol, we evaluate on a fixed set of 128 held-
out tasks, with episode lengths ranging from 8 to 30 steps. Owing to the diversity in decision
horizon and operational complexity across sub-tasks, ALFWorld provides a comprehensive testbed
for evaluating generalization in complex embodied environments. From the perspective of ReBel, the
key challenge lies in maintaining a persistent understanding of the environment state across multiple
interactions and progressively approaching the goal through a sequence of intermediate actions. This
makes ALFWorld particularly suitable for assessing whether the model can establish a stable “belief
update–reasoning–action” decision loop.
A.2.2 WebShop
We further evaluate our method on WebShop, a web-based shopping environment designed to test
multi-step retrieval, filtering, and decision-making under partial information. In this task, an agent
must complete operations such as product search, page navigation, attribute filtering, item comparison,
and final purchase within a simulated e-commerce website according to a user instruction.
WebShop contains more than 1.1 million products and over 12,000 user instructions. The maximum
episode length is 15 steps, and the reward lies in the interval [0,1] , with high rewards available only
when the agent successfully completes the target. Since product information is often incomplete
and the set of available actions changes across pages, WebShop imposes strong requirements on the
model’s retrieval ability, constraint satisfaction, and multi-step decision-making. From the perspective
of ReBel, WebShop exhibits a typical “reasoning-driven decision-making” setting: at each step, the
model must act based on the current page state and the interaction history, while each intermediate
decision directly affects future reachable states and the final return. This makes the benchmark well
suited for evaluating whether our method can maintain stable trajectory-level reasoning and policy
consistency in complex web environments.
A.3 Implementation Details
Model and cold-start setup.We perform all experiments with Qwen2.5-1.5B-Instruct. To
ensure that the model acquires basic task-format understanding and structured generation capability
before entering the reinforcement learning stage, we adopt an SFT cold-start procedure prior to RL
training. Specifically, we first fine-tune the base model on expert trajectories, using 390 trajectories
for ALFWorld and 500 trajectories for WebShop. The SFT stage is trained for 3 epochs with a
learning rate of 1×10 −5, and the micro-batch size per GPU is 8. The goal of this stage is to teach
the model to reliably generate a structured three-part response format consisting of <belief>,
14

## Page 15

<think>, and <action>, thereby providing a format-stable initialization for the subsequent RL
stage and reducing invalid exploration caused by formatting errors at the beginning of training.
RL optimization setup.We implement ReBel on top of the veRL-agent framework and introduce
the necessary modifications to accommodate partially observable long-horizon tasks. In the RL
stage, the learning rate is set to 1×10 −6, and AdamW is used as the optimizer. For each task input,
we sample N= 16 trajectories to form a rollout group, which is used for group-wise normalized
advantage estimation. ReBel is trained for 100 iterations, whereas the other RL baselines, including
PPO, RLOO, GRPO, and GiGPO, are trained for 150 iterations and averaged over 3 random seeds.
For the ablation settings B0–B3, each configuration is trained for 100 iterations. The PPO mini-batch
size is set to 256, and the micro-batch size per GPU is 4. The maximum episode length is 30 steps
for ALFWorld and15steps for WebShop.
Advantage formulation.ReBel uses a linear combination of two-level advantages, namely the
trajectory-level episode advantage Aep(τi) and the belief-anchor step-level advantage AS(i, t). The
former is obtained by normalizing the task success signal within the rollout group, while the latter is
computed by normalizing the step-level discounted return within the same belief equivalence class.
We set the weight of the step-level component to0.5, yielding ˆAtot
i,t =A ep(τi) + 0.5·A S(i, t).
Format regularization.To encourage the model to produce well-formed three-part responses, we
apply a reward penalty of −0.1 to outputs that violate the required format. An output is considered
valid only if it contains at least one belief-state tag, namely <belief>...</belief>, and one
action tag, namely<action>...</action>.
Regularization and discounting.We set the KL divergence loss coefficient to 0.01 using the
low-variance estimator, and the KL penalty coefficient to 0.001. The RL discount factor is set to
γRL = 0.95.
A.4 Evaluation Protocol
We evaluate model performance on the validation set and use task success rate as the primary metric.
For ALFWorld, we report both per-subtask success rates and the overall success rate on the fixed
set of 128 held-out tasks. For WebShop, we report average score, which reflects partial matching
quality, as well as success rate SR. We follow the standard evaluation protocols of each benchmark.
During evaluation, sampling is disabled by setting the temperature to 0, or equivalently using greedy
decoding, in order to more stably reflect the model’s generalization performance and to distinguish
evaluation from the stochastic rollout policy used during training.
B Prompt Templates
Figure 4 and Figure 5 present the prompt templates used by REBELin the ALFWorld and WebShop
environments, respectively. The templates are implemented with Python-style string formatting,
where placeholders enclosed in curly braces are filled at runtime via .format(). Each prompt
includes the task instruction, a short interaction history, the previous belief state, and the current
observation. To keep the prompt concise, we retain only the two most recent actions in the history.
All prompts follow the same three-stage decision protocol: (i) belief update, which integrates the
previous belief with the current observation; (ii) belief-grounded reasoning, which identifies the
current task phase and the most relevant next step; and (iii) action selection, which outputs one
executable action from the admissible action set. The model response is structured into three tagged
blocks: <belief>, <think>, and <action>. The <belief> block serves as the structured
latent state used by REBEL’s grouping-based credit assignment, the <think> block encourages
brief intermediate reasoning, and the<action>block contains the final executable action string.
ALFWorld Prompt Template
You are an expert agent operating in the ALFRED embodied environment.
Task: {task_description}
Step count: {step_count} Recent history ({history_length} steps): {action_history}
Current step: {current_step}
Current observation: {current_observation}
15

## Page 16

Use the previous belief state together with the current observation to update your belief, reason
about the current task phase, and select the best next action. Historical observations are omitted
because their relevant information is already summarized in the previous belief.
Previous belief:
<belief_prev>{previous_belief}</belief_prev>
Respond in the following format:
<belief>
state:
• "target": "[attr]": "[value]"
• "confirmed": "[attr]": "[verified value]"
• "unconfirmed": ["[attr]"]
• "product_id": "[ASIN or null]"
task:
• "phase": "[searching | browsing | viewing | selecting | buying | done]"
• "target": "[product_id or null]"
• "subgoal": "[updated immediate subgoal]"
"prediction": "If I execute [planned_action], I expect [next-observation conse-
quence]."
</belief>
<think>
[Brief reasoning in 2–3 sentences: what is confirmed, what remains uncertain, which
phase the task is in, and why the chosen action is currently optimal.]
</think>
<action>
[Exact action string selected from the admissible action set]
</action>
Figure 4: ALFWorld prompt template.
WebShop Prompt Template
You are an expert autonomous agent operating in the WebShop e-commerce environment.
Task: {task_description}
Step count: {step_count}
Recent history ({history_length} steps): {action_history}
Current step: {current_step}
Current observation: {current_observation}
Use the previous belief state together with the current observation to update the belief, infer the
current task phase, identify the main information bottleneck, and select the best next action.
Previous belief:
<belief_prev>{previous_belief}</belief_prev>
Respond in the following format:
<belief>
"state":
• "target": {"[attr]": "[value]"}
• "confirmed": {"[attr]": "[verified value]"}
• "unconfirmed": ["[attr]"]
• "product_id": "[ASIN or null]"
"task":
16

## Page 17

• "phase": "[searching | browsing | viewing | selecting | buying | done]"
• "target": "[product_id or null]"
• "subgoal": "[updated immediate subgoal]"
"prediction":
"If I execute [planned_action], I expect [next-observation consequence]."
</belief>
<think>
[Brief reasoning in 2–3 sentences: what is confirmed, what remains uncertain, which
phase the task is in, and why the chosen action is currently optimal.]
</think>
<action>
[Exact action string selected from the admissible action set]
</action>
Figure 5: WebShop prompt template.
C Limitations
Our study has two main limitations. First, our experiments are conducted on two representative
benchmarks and one backbone scale, 1.5B. This setting allows us to evaluate the core hypothesis of
REBELin a controlled and comparable manner, especially in environments where partial observability
and intermediate reasoning play an important role. However, it does not fully cover the diversity of
possible task distributions, interaction patterns, and model capacity regimes. For example, tasks with
longer horizons, more diverse feedback signals, or substantially larger policy models may exhibit
different optimization dynamics. Evaluating REBELunder a wider range of environments and model
scales would therefore provide a more complete picture of its empirical generality.
Second, the belief representation used in ALFWorld is designed to align with symbolic object-state
tracking, which is a natural fit for the structure of that benchmark. This design choice makes it possible
to define and evaluate belief consistency in a transparent and interpretable way. Nevertheless, other
domains may expose different forms of observations and hidden states. For instance, vision-based
environments may require beliefs over visual entities or spatial layouts, while continuous-control
tasks may call for more compact or learned state abstractions. Extending REBELto such settings
would likely require adapting the belief format to the corresponding observation and state spaces.
We view this as a promising direction for future work, rather than a fundamental restriction of the
framework.
D Pseudo Code
E Additional Analysis
E.1 Belief Drift under Partial Observability
In partially observable environments, agents must reason over latent beliefs inferred from incomplete
observations. As illustrated in Figure 6, a think-only agent may become overconfident in an incorrect
belief and continue selecting actions that are locally consistent with this mistaken assumption, even
after receiving contradictory observations. Since sparse terminal rewards provide limited supervision
over intermediate reasoning errors, standard outcome-level reinforcement learning often fails to
correct such latent belief drift. In contrast, belief-aware policies explicitly revise their internal
beliefs according to new observations, progressively reducing uncertainty and enabling recovery from
incorrect hypotheses before the trajectory diverges from the task objective.
E.2 Independent Contribution of SFT Cold Start
To isolate the contribution of the SFT warm start, we evaluate the agent immediately after SFT
initialization, before any RL optimization, and compare it with the full REBELpipeline after SFT +
RL training.
The results indicate that SFT alone provides only limited task performance. On ALFWorld [ 33],
the SFT-only model achieves a mean success rate of 3.6% across three random seeds, with scores
ranging from 2.3% to 5.5%, which is far below the 93.2% achieved by full REBEL. This large gap
17

## Page 18

Algorithm 1ReBel Training
Require: Policy πθ, reference policy πref, task distribution p(x), rollout size N, horizon T, weights
ω, β, clip rangeϵ
1:Initializeθ←θ SFT
2:foreach training iterationdo
3:Sample taskx∼p(x)and collectNrollouts
4:foreach rollouti∈ {1, . . . , N}and stept∈ {1, . . . , T}do
5:Generateb (i)
t , z(i)
t , a(i)
t fromπ θ(· |h(i)
t , x)
6:Executea (i)
t and observeo (i)
t+1
7:Compute belief-consistency rewardr (i)
t,cons using observability mask and pending buffer
8:Update historyh (i)
t+1
9:end for
10:Compute episode-level advantageA (i)
E
11: Group step samples by canonicalized belief anchors and compute step-level advantage A(i,t)
S
12:Combine advantages:A (i,t)
tot =A (i)
E +ωA (i,t)
S
13:Updateθby maximizing clipped PPO objective with KL regularization:
14:
J(θ) =E
h
min

rt(θ)A(i,t)
tot ,clip(r t(θ),1−ϵ,1 +ϵ)A (i,t)
tot
i
−βKL(π θ ∥π ref)
15:end for
Figure 6:Belief drift as a failure mode in partially observable environments.The top row shows
a Think-only agent that remains overconfident in an incorrect belief and repeatedly executes invalid
actions. The bottom row shows a Belief-Augmented agent that updates its belief from observations,
progressively reduces uncertainty, and succeeds in the task. REBELaims to induce this belief-aware
reasoning behavior during RL training.
shows that SFT is not the main source of the final performance gain. Instead, its primary role is to
stabilize the structured <belief> output format and provide a reliable initialization for subsequent
process-level RL optimization.
In other words, SFT mainly serves as a warm start that improves training stability and makes the
belief representation usable for downstream reinforcement learning. The substantial performance im-
provements in REBELcome primarily from RL optimization over belief consistency and semantically
coherent grouping, rather than from supervised pretraining itself.
18

## Page 19

Table 3: Independent contribution of the SFT warm start on ALFWorld [33]. Results are reported as
mean±std over 3 random seeds.
Method Initialization ALFWorld Overall (%)
SFT only (3 epochs, no RL) SFT checkpoint 3.6±1.6
GRPO + SFT init (ablation baseline) SFT checkpoint 60.9
ReBel(full, SFT + RL) SFT checkpoint93.2±4.1
E.3 Representative Trajectories
F Theoretical Analysis
F.1 Problem Diagnosis and REBEL Design
We consider a partially observable sequential decision process with latent state st ∈ S, observation
ot ∈ O, action at ∈ A, and history ht = (o1, a1, . . . , ot). The task input is denoted by x. Since st is
not directly observable, a policy must maintain an internal belief over the task-relevant aspects of
the environment. In what follows, we use ¯bt to denote the implicit belief induced by a conventional
end-to-end policy, andb t to denote the explicit belief used by REBEL.
A conventional end-to-end policy directly maps the history to the next output,
πθ(yt |h t, x),
where yt may contain reasoning tokens, tool calls, or the final action. Although this policy implicitly
encodes a belief ¯bt, such belief is neither explicitly exposed nor directly supervised. As a result, if ¯bt
deviates from the true task-relevant state abstraction, the agent receives no timely correction signal.
Under sparse terminal rewards, this deviation may persist across many steps and propagate through
subsequent reasoning and action choices.
We formalize this failure mode as belief drift.
Definition 1(Belief drift).Let D:B × B →R≥0 be a discrepancy function. The belief drift at step
tis defined as
dt =D(b t, ϕ(st)),
where bt is the belief used by the agent for decision making and ϕ:S → B is a task-relevant
projection from latent states to belief space.
From an optimization perspective, the main difficulty is credit assignment. With only an episode-level
returnR i for trajectoryi, all intermediate decisions share the same delayed learning signal:
gtrad
i =
TiX
t=1
∇θ logπ θ(yi,t |h i,t, xi)A E
i .
Therefore, the policy gradient cannot distinguish whether a failure is caused by an incorrect belief
update, an unhelpful reasoning step, or a poor final action. In long-horizon partially observable tasks,
this ambiguity makes training unstable. Under the usual weak-correlation assumption across steps,
the variance of such a trajectory-level estimator grows at least approximately linearly with horizon
length, which explains why sparse terminal supervision is often insufficient.
REBEL addresses this issue by making the latent decision structure explicit. Instead of treating each
step as a monolithic generation process, REBEL decomposes it into Belief, Think, and Action layers:
πθ(bt, zt, at |h t, x) =πθ(bt |h t, x)πθ(zt |h t, x, bt)π θ(at |h t, x, bt, zt).
Here bt is the explicit belief, zt is the intermediate reasoning trace, and at is the action. This
factorization turns the hidden belief into an observable and trainable object, and it separates three
sources of error: belief construction, reasoning conditioned on belief, and action selection conditioned
on both.
To supervise the belief layer, REBEL introduces belief consistency supervision. Suppose the belief is
represented by K task predicates p1, . . . , pK. Let ˆpt,k(bt) be the value of predicate pk implied by
belief bt, and let vt+1,k be the corresponding value verified from the next observation whenever it is
observable. Because not every predicate is immediately observable, we define an observability mask
mt,k ∈ {0,1}. The consistency indicator is
Ct,k =1{ˆpt,k(bt) =v t+1,k}.
19

## Page 20

The step-wise consistency reward is
rcons
t =
PK
k=1 mt,kCt,k
max{1, PK
k=1 mt,k}
.
This reward provides immediate supervision for the observable part of the belief. For predicates
that are not yet observable, REBEL maintains a pending buffer Ut and evaluates them once a later
observation makes them verifiable. In this way, consistency supervision supports both immediate
correction and delayed verification.
Finally, REBEL introduces a belief-anchor step-wise advantage to avoid the singleton problem in
partially observable environments. State-based grouping is ineffective because the same physical state
st may rarely reappear across sampled trajectories. REBEL instead groups samples by a symbolic
belief anchor ˜bt, defined as the observable and pending predicate signature extracted from bt. The
belief-anchor group is
GB(˜b) ={(i, t) :˜bi,t = ˜b}.
Let GS
i,t be a local step-level return, for example the discounted sum of consistency rewards over a
short horizon:
GS
i,t =
t+HX
ℓ=t
γℓ−trcons
i,ℓ .
The belief-anchor advantage is then
AS
i,t = GS
i,t −µ B(˜bi,t)
σB(˜bi,t) +ε
,
where
µB(˜b) = 1
|GB(˜b)|
X
(j,u)∈GB(˜b)
GS
j,u,
and σB(˜b) is the corresponding within-anchor standard deviation. The total learning signal combines
trajectory-level success with belief-anchor step-level feedback:
Atot
i,t =A E
i +ωA S
i,t.
This design gives REBEL two complementary supervision channels: AE
i preserves global task
optimization, whileA S
i,t provides dense belief-level correction under a shared semantic context.
F.2 Variance Reduction Analysis
We now explain why the above design reduces the variance of step-wise advantage estimation. The
key idea is that belief consistency supplies a dense intermediate signal, while belief-anchor grouping
provides a meaningful comparison set in partially observable settings.
We assume that the belief discrepancy decomposes over task predicates:
D(bt, ϕ(st)) =
KX
k=1
wk ℓk
 
ˆpt,k(bt), pk(ϕ(st))

,
wherew k ≥0and eachℓ k is a bounded predicate-level loss. Let
κt = 1
K
KX
k=1
mt,k
be the observable predicate fraction at stept.
Proposition 1(Consistency supervision contracts observable belief drift).Assume that observable
predicate verification is sound up to error δobs, meaning that whenever mt,k = 1 and Ct,k = 1,
the corresponding predicate-level belief error is at most δobs. Suppose further that every pending
predicate is verified within at most ∆ steps with probability at least 1−ρ . Then there exist constants
α >0,c 1 >0, andc 2 >0such that
E[dt+1]≤(1−ακ t)E[dt] +c 1 E[1−r cons
t ] +c 2(ρ+ ∆ err),
where∆ err denotes the maximum additional drift accumulated during delayed verification.
20

## Page 21

Proof. For observable predicates, the consistency reward directly penalizes disagreement between
the belief-implied predicate value and the value verified from the subsequent observation. Hence, a
higherr cons
t implies a smaller observable component ofD(b t, ϕ(st)), up to verification errorδ obs.
For unobservable predicates, REBEL does not force an immediate penalty. Instead, the pending
buffer Ut stores such predicates until they become verifiable. By assumption, verification occurs
within ∆ steps with probability at least 1−ρ . During this delay, the uncorrected component can
accumulate at most∆ err additional error. Combining these two effects yields the stated bound.
Proposition 1 shows that consistency supervision acts as an intermediate corrective signal. If the
average observability is bounded below by ¯κ >0and the average inconsistency is bounded by ϵcons,
then repeated application gives
lim sup
t→∞
E[dt]≤ c1ϵcons +c 2(ρ+ ∆ err)
α¯κ .
Thus REBEL prevents belief drift from growing unchecked and confines the expected drift to a
bounded region determined by observability, verification quality, and delay.
We next analyze the variance of step-wise advantage estimation. LetN be the number of sampled
step instances in a training batch. For any grouping variable H, define the group containing sample
j= (i, t)as
GH(Hj) ={j ′ :H j′ =H j},
with group size nH(j) =|G H(Hj)|. A state-based method uses Hj =s i,t, while REBEL uses
Hj = ˜bi,t.
The failure of state-based grouping in POMDPs follows from support size. Let MS be the effective
number of reachable latent states and MB be the number of possible belief anchors. If the anchor
containsKternary predicate values, namely true, false, and unknown, then
MB ≤3 K.
In long-horizon partially observable tasks, MS is typically much larger than MB. Under a roughly
uniform occupancy approximation, the expected group sizes satisfy
E[nS]≈1 + N−1
MS
,E[n B]≥1 + N−1
MB
.
Therefore, when MB ≪M S, belief-anchor groups are much larger than state-based groups, and
state-based groups are often close to singletons.
This difference directly affects advantage variance. Let Gj denote the step-level target return for
samplej. For a grouping variableH, define the centered advantage
˜AH
j =G j −E[G j |H j].
By the law of total variance,
Var( ˜AH
j ) =E

Var(Gj |H j)

.
Hence any grouping variable that captures meaningful semantic similarity reduces the residual
variance of the advantage by removing the predictable group-level component.
In practice, the conditional mean is estimated from samples. Using a leave-one-out group mean
ˆµH,−j, define
ˆAH
j =G j −ˆµH,−j.
If the within-group variance isσ 2
H(Hj) = Var(Gj |H j)andn H(j)>1, then
Var( ˆAH
j |H j, nH(j)) =σ 2
H(Hj)

1 + 1
nH(j)−1

.
This expression shows why state-based grouping is unstable in POMDPs: whennS(j)≈1 , the group
baseline is either unavailable or highly noisy. In contrast, belief-anchor grouping has larger nB(j),
so the finite-sample estimation term is much smaller.
Belief anchors also reduce the intrinsic within-group variance. Samples sharing the same anchor
˜b have the same predicate-level cognitive context, even if their underlying physical states differ.
Suppose the local return is Lipschitz with respect to belief drift up to bounded noise:
Gj =F( ˜bj, aj) +ξ j,Var(ξ j | ˜bj)≤σ 2
ξ ,
21

## Page 22

and
|F(˜bj, aj)−F( ˜bj, a′
j)| ≤LRdj.
Then
Var(Gj | ˜bj)≤σ 2
ξ +L 2
RE[d2
j | ˜bj].
By Proposition 1, consistency supervision bounds the drift term and therefore tightens the within-
anchor return distribution.
Combining these observations gives the main conclusion: belief-anchor grouping yields a lower-
variance step-wise advantage estimator than state-based grouping in partially observable tasks,
because it avoids the singleton-group problem, increases the effective comparison set size, and aligns
samples by semantic belief rather than exact latent state. The total learning signalAtot
i,t =A E
i +ωA S
i,t
further preserves trajectory-level optimization while injecting low-variance step-level correction.
G Trajectory Case Study
IDb3_rebel_00082
Task Typepick_clean_then_place_in_recep
Status Success
Steps8
Format Valid Rate:1.00
Episode ID:82
Task
/flagTask Description
put a clean mug in coffeemachine.
Interaction
ὄ1Observation (Step 1)
-= Welcome to TextWorld, ALFRED! =-
You are in the middle of a room. Looking quickly around you, you
see a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet
2, a cabinet 1, a coffeemachine 1, a countertop 3, a countertop
2, a countertop 1, a drawer 3, a drawer 2, a drawer 1, a fridge 1,
a garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a
sinkbasin 1, a stoveburner 4, a stoveburner 3, a stoveburner 2, a
stoveburner 1, and a toaster 1.
Your task is to: put a clean mug in coffeemachine.
♂robotAgent (Step 1) (admissible)
/da◎abaseBelief State:
Phase:find
Target:mug
Subgoal:Find the mug so it can later be cleaned and placed in the coffeemachine.
Prediction:If I execute go to countertop 1, I expect On the countertop 1, you see a apple 2, a apple 1, a
bread 1, a bread 2, a egg 1, a fork 1, a mug 1, a pan 1, and a tomato 1.
/bol◎Action:
go to countertop 1
ὄ1Observation (Step 2)
You arrive at countertop 1. On the countertop 1, you see a apple 3, a
cellphone 1, a creditcard 1, a peppershaker 3, a peppershaker 1, and a
tomato 1.
22

## Page 23

♂robotAgent (Step 2) (admissible)
/da◎abaseBelief State:
Phase:find
Target:mug
Subgoal:Find the mug so it can later be cleaned and placed in the coffeemachine.
Visited:countertop 1
Prediction:If I execute go to countertop 2, I expect On the countertop 2, you see a apple 2, a bread 1, a
bread 2, a egg 2, a fork 2, a mug 2, a pan 2, and a tomato 2.
/bol◎Action:
go to countertop 2
ὄ1Observation (Step 3)
You arrive at countertop 2. On the countertop 2, you see a apple 2, a
bowl 1, a butterknife 1, a fork 1, a mug 1, a spoon 1, and a statue 1.
♂robotAgent (Step 3) (admissible)
/da◎abaseBelief State:
Phase:pickup
Target:mug 1
Subgoal:Pick up mug 1 from countertop 2 so it can be cleaned next.
Objects:mug 1: countertop 2
Visited:countertop 1, countertop 2
Prediction:If I execute take mug 1 from countertop 2, I expect You pick up the mug 1 from the countertop
2.
/bol◎Action:
take mug 1 from countertop 2
ὄ1Observation (Step 4)
You pick up the mug 1 from the countertop 2.
♂robotAgent (Step 4) (admissible)
/da◎abaseBelief State:
Phase:transform
Target:mug 1
Subgoal:Bring the mug 1 to a sinkbasin so it can be cleaned.
Objects:mug 1: in_hand
Visited:countertop 1, countertop 2
Prediction:If I execute go to sinkbasin 1, I expect On the sinkbasin 1, you see a apple 2, a apple 1, a bread
1, a fork 2, a fork 1, a knife 1, a mug 2, a potato 1, and a tomato 2.
/bol◎Action:
go to sinkbasin 1
ὄ1Observation (Step 5)
You arrive at sinkbasin 1. On the sinkbasin 1, you see a glassbottle
2, and a spatula 1.
23

## Page 24

♂robotAgent (Step 5) (admissible)
/da◎abaseBelief State:
Phase:transform
Target:mug 1
Subgoal:Clean the mug 1 using sinkbasin 1 so it can later be placed in the coffeemachine.
Objects:mug 1: in_hand
Visited:countertop 1, countertop 2, sinkbasin 1
Prediction:If I execute clean mug 1 with sinkbasin 1, I expect On the sinkbasin 1, you see a apple 2, a
apple 1, a bread 1, a fork 2, a fork 1, a knife 1, a mug 2, a potato 1, and a tomato 2.
/bol◎Action:
clean mug 1 with sinkbasin 1
ὄ1Observation (Step 6)
You clean the mug 1 using the sinkbasin 1.
♂robotAgent (Step 6) (admissible)
/da◎abaseBelief State:
Phase:place
Target:mug 1
Subgoal:Carry the cleaned mug 1 to coffeemachine 1 and place it inside.
Objects:mug 1: in_hand
Visited:countertop 1, countertop 2, sinkbasin 1
Prediction:If I execute go to coffeemachine 1, I expect On the coffeemachine 1, you see a apple 1, a
bread 2, a bread 1, a butterknife 2, a butterknife 1, a egg 1, a fork 3, a fork 2, a fork 1, a mug 2, a mug
1,...[truncated]
/bol◎Action:
go to coffeemachine 1
ὄ1Observation (Step 7)
You arrive at coffeemachine 1. On the coffeemachine 1, you see
nothing.
♂robotAgent (Step 7) (inadmissible)
/da◎abaseBelief State:
Phase:place
Target:mug 1
Subgoal:Place the cleaned mug 1 into coffeemachine 1.
Objects:mug 1: in_hand
Visited:countertop 1, countertop 2, sinkbasin 1, coffeemachine 1
Prediction:If I execute put mug 1 in/on coffeemachine 1, I expect On the coffeemachine 1, you see a
apple 1, a bread 2, a bread 1, a butterknife 2, a butterknife 1, a egg 1, a fork 3, a fork 2, a fork 1, a mug
2...[truncated]
/bol◎Action:
put mug 1 in/on coffeemachine 1
ὄ1Observation (Step 8)
On the coffeemachine 1, you see nothing.
24

## Page 25

♂robotAgent (Step 8) (admissible)
/da◎abaseBelief State:
Phase:place
Target:mug 1
Subgoal:Place the cleaned mug 1 into coffeemachine 1.
Objects:mug 1: in_hand
Visited:countertop 1, countertop 2, sinkbasin 1, coffeemachine 1
Prediction:If I execute move mug 1 to coffeemachine 1, I expect On the coffeemachine 1, you see a
apple 1, a bread 2, a bread 1, a butterknife 2, a butterknife 1, a egg 1, a fork 3, a fork 2, a fork 1, a mug 2,
...[truncated]
/bol◎Action:
move mug 1 to coffeemachine 1
25
