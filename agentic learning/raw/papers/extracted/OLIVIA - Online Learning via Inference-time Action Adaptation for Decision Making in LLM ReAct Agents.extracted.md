# OLIVIA: Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents - Extracted Text

- Source note: [[OLIVIA - Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents]]
- Source PDF: `assets/OLIVIA - Online Learning via Inference-time Action Adaptation for Decision Making in LLM ReAct Agents.pdf`
- Extracted: 2026-05-14
- Extractor: pypdf
- Pages: 18
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

Preprint. Under review.
OLIVIA: Online Learning via Inference-time Action Adapta-
tion for Decision Making in LLM ReAct Agents
Sheldon Yu1∗, Junda Wu1∗, Xintong Li1, Nikki Lijing Kuang1, Sizhe Zhou2,
Tong Yu3, Jiawei Han2, Jingbo Shang1, Julian McAuley1
1UC San Diego 2University of Illinois at Urbana-Champaign 3Adobe Research
{ziy040,juw069,xil240,jshang,jmcauley}@ucsd.edu
{sizhez,hanj}@illinois.edu tyu@adobe.com
Abstract
Large language model agents interleave reasoning, action selection, and
observation to solve sequential decision-making tasks. In deployed set-
tings where agents repeatedly handle related multi-step tasks, small action-
selection errors can accumulate into wasted tool calls, latency, and reduced
reliability. Despite this need for deployment-time improvement, however,
existing inference-time adaptation methods for LLM agents mainly rely on
prompting or retrieval, which influence behavior indirectly through context
manipulation. For ReAct-style agents, such approaches do not expose an
explicit decision layer that can score candidate actions, represent uncer-
tainty, or be updated online from action-level feedback. As a result, they
provide limited support for trackable, fine-grained, and uncertainty-aware
adaptation during deployment. We propose OLIVIA, an inference-time
action adaptation framework for ReAct-style agents. OLIVIA models
the LLM’s final action-selection layer as a contextual linear bandit over
candidate actions, with frozen hidden states as decision contexts. This
choice is particularly suitable for deployment because it adapts behavior
directly at the action-selection interface, preserves the underlying reason-
ing process, and provides explicit uncertainty estimates and lightweight
online updates from action-level feedback. With upper-confidence-bound
exploration, OLIVIA improves the policy sample-efficiently with minimal
computational overhead. We instantiate OLIVIA on four benchmarks and
show that it consistently improves task performance over static ReAct and
prompt-based inference-time baselines. Our results suggest that explicit
online decision layers provide an effective alternative to purely prompt or
retrieval-based adaptation for LLM agents during deployment.
1 Introduction
LLM agents increasingly operate as sequential decision makers in deployed settings such as
tool-using assistants, API orchestration systems, and enterprise workflow agents. In these
applications, the agent must interleave natural-language reasoning, action selection, and
environment feedback through a sequence of thoughts, actions, and observations in order
to complete multi-step tasks. ReAct-style prompting has emerged as a practical template
for such agents because it exposes intermediate decisions, supports multi-step interaction,
and can be deployed without parameter updates (Wu et al., 2025b; Nguyen et al., 2025; Xia
et al., 2025). However, despite this sequential structure, agent behavior is typicallystaticat
inference time: the model follows a fixed prompt-guided policy, while feedback gathered
during deployment is not used to systematically improve future decisions. In repeated or
streaming deployments, this limitation can be costly. Agents may revisit similar decision
states, repeat the same local mistakes, and waste interaction budget when an early error
leads to an unproductive trajectory. A growing body of work seeks to improve inference-
time behavior through prompt engineering (Yao et al., 2023b), reflection (Shinn et al., 2023),
∗These authors contributed equally to this work.
1
arXiv:2605.11169v1  [cs.AI]  11 May 2026

## Page 2

Preprint. Under review.
or memory augmentation (Majumder et al., 2023; Wang et al., 2025a;b). These approaches
can change what the model generates, but they typically do not provide an explicit online
optimization mechanism for sequential decision making (Huang et al., 2025a). In particular,
they offer limited support for adapting action-selection behavior from observed feedback
over a stream of related tasks. As a result, improvements often remain indirect, heuristic,
or tied to prompt design rather than to an explicit decision layer that can learn during
deployment.
We study this problem through the lens ofonline adaptation for inference-time decision making.
At each decision step, an agent must choose an action based on the current task state and its
evolving reasoning history, while feedback from previous interactions may be informative
for future decisions in similar contexts (Wu et al., 2022). This setting naturally calls for a
lightweight online learner that can sit on top of a frozen LLM, use the model’s internal
state as context, and update from observed interaction feedback without requiring model
fine-tuning.
To this end, we propose OLIVIA, an online adaptation framework for ReAct-style agents.
OLIVIA adds a lightweight contextual decision layer on top of a frozen language model: at
each step, it uses the model’s hidden-state representation of the current task and reasoning
history as context, selects the next action from a candidate set, and updates from step-level
feedback to improve future decisions across a stream of tasks. This design is well matched
to our setting: the agent repeatedly chooses from a discrete action set and observes feedback
only for the selected action, making contextual bandits a natural model of partial-feedback
online adaptation (Wu et al., 2021; Hu et al., 2025). Compared with policy-gradient or
purely episodic updates, this yields a more direct and lower-variance learning signal, while
unlike retrieval-augmented memory, it adapts behavior through an explicit decision layer
rather than indirect context modification. In this paper, we instantiate OLIVIA on tool-
use benchmarks, where decision context is trajectory-dependent: each action changes the
subsequent reasoning history, so later hidden states, rewards, and updates are coupled
across the interaction even though the backbone model remains fixed.
Our approach is lightweight and modular. It does not require retraining the base model,
modifying the prompting interface, or storing large retrieval memories. Instead, it augments
the frozen LLM with an online controller that adapts action preferences from experience,
enabling the agent to improve over time as it encounters related tasks. We summarize our
contributions as follows:
• We formulate online adaptation for language model agents as an inference-time
sequential decision-making problem, in which a lightweight decision layer uses
LLM hidden-state representations to adapt action selection from step-level feedback.
• We develop OLIVIA, a contextual-bandit-based online decision layer that operates
on top of a frozen LLM and supports efficient action scoring, uncertainty-aware
exploration, and incremental updates during deployment.
• We instantiate OLIVIA on four tool-use benchmarks and show that it improves task
performance and online adaptation behavior over static prompting baselines and a
prompt-based inference-time adaptation baseline, while preserving the underlying
language model.
2 Related work
2.1 Inference-time adaptation.
Recent work shows that LLM agents need not remain fixed after deployment. ReAct already
casts inference as a closed-loop process of reasoning, acting, and observing, creating a
natural interface for adaptation from interaction feedback (Yao et al., 2023b; Wu et al., 2025b;
Nguyen et al., 2025; Lu et al., 2024). Most inference-time adaptation methods, however,
operate indirectly through memory, prompting, or lightweight control variables: verbal
reflection and episodic memory (Majumder et al., 2023; Shinn et al., 2023; Zhong et al., 2023),
dynamic in-context example selection (Wang et al., 2025a), in-context preference adaptation
2

## Page 3

Preprint. Under review.
Tool Bank
Book 6 rooms for 9 nights in Glendale starting on Feb 15th, 2023 below 580 USD per night.
Task
Transformer Layer
Hidden States ..
Linear Layer
…
Tool Selected 
The user want to stay in Glendale for 9 night...
Thought
score𝑎=𝜃!"𝑥#
𝜃!"𝜙𝑥$,#+𝛼𝜙𝑥$,#"𝐴!&'𝜙𝑥$,#
GT list𝑟#=𝕀𝑎#∈𝒢𝓉
Update Action PreferencesCompute!𝜃!=𝐴!&'𝑏!
Candidate Tools
Figure 1: Overview of OLIVIA.Left: A frozen LLM backbone processes the task and
trajectory prefix through its transformer layers, producing hidden states and a reasoning
trace (Thought).Right: At each action-selection step, OLIVIA extracts the last-layer hidden
state as the decision context and scores candidate tools using per-action UCB estimates.
(Wu et al., a), and parameter-internalized context (Wang et al., 2025b), reusable natural-
language experience or skill libraries (Zhao et al., 2024; Wang et al., 2023; Xia et al., 2025),
retrospective prompt optimization (Yao et al., 2024), CoT debiasing and offline alignment
(Wu et al., 2024b; 2025a), and information-theoretic prompt tuning (Wu et al., 2023), and
lightweight test-time adaptation under environment shift (Chen et al., 2026), latent-state
reasoning analysis (Wu et al., b; Yu et al., 2025). Surveys also document the rapid expansion
of inference-time adaptation across personalized, multimodal, and federated LLMs (Zhang
et al., 2024; Wu et al., 2024a;c; Surana et al., 2026). These works establish deployment-
time adaptation as a viable paradigm, but they generally do not expose an explicit online
decision layer for sequential action selection. Our work shares the same deployment-time
perspective, but focuses on updating a lightweight action-selection module online from
step-level feedback.
2.2 Online optimization of sequential decisions.
A complementary line of work treats inference itself as an online optimization problem
over a sequence of intermediate decisions. In reasoning, this appears as explicit search or
planning over thought states (Yao et al., 2023a; Hao et al., 2023); in agent settings, as tree-
search-based interaction and planning with environment feedback (Zhou et al., 2024; Koh
et al., 2026; Mundada et al., 2026); and in test-time compute scaling, as adaptive allocation of
inference resources such as branching depth or search breadth (Inoue et al., 2025; Liu et al.,
2024; Kveton et al., 2025). Related uncertainty-aware methods also use posterior sampling
or contextual Thompson sampling to guide sequential choice under partial feedback (Cai
et al., 2025; Zhang et al., 2025; Xia et al., 2023). Together, these works motivate viewing
inference as online optimization over reasoning, acting, and compute allocation. Our
method is closest to this perspective: we study online adaptation for sequential LLM
decision making using frozen-model contextual representations and lightweight online
updates from observed step-level feedback. Closely related online-RL formulations adapt
action policies under simulator-to-deployment dynamics shift (Wu et al., 2022), while
pluralistic off-policy evaluation extends this view to multi-stakeholder alignment (Huang
et al., 2025b; Xie et al., 2025).
3 Preliminaries
3.1 Contextual Bandits
A contextual bandit models repeated decision making under partial feedback (Li et al., 2010;
Ban et al., 2023). At round n= 1, 2,. . ., N, the learner observes a context xn ∈ X, chooses
3

## Page 4

Preprint. Under review.
an action an ∈ A(xn), and receives a scalar reward rn for that action alone; the rewards of
unchosen actions are not observed. An optimal action satisfies
a∗
n ∈arg max
a∈A(x n)
E[rn |x n,a].
The learner’s goal is to find an action-selection rule that achieves high cumulative reward
across rounds while balancingexplorationof uncertain actions againstexploitationof actions
that already appear promising. When the expected reward is modeled as a parametric
function of contextual features, the learner can generalize across related decision states and
employ principled exploration strategies such as upper confidence bounds (Ban et al., 2023).
3.2 ReAct-Style Sequential Agents
We consider an LLM agent that interacts with an environment over multiple decision steps
following the ReAct paradigm (Yao et al., 2023b; Zhou et al., 2024; Koh et al., 2026). In
episode e, the agent receives a task input qe and a candidate action set Ae. Let he,t−1 denote
the interaction history before step t, comprising prior reasoning traces, selected actions,
and environment observations. At step t the agent selects an action ae,t ∈ Ae,t, receives an
observationo e,t, and updates the history:
he,t =h e,t−1 ⊕(a e,t,o e,t),
where ⊕ denotes concatenation. The episode terminates when the agent issues a stop action
or reaches a step budget. Because the history grows with each step, every action decision is
conditioned on a distinct, trajectory-dependent contextx e,t = (qe,h e,t−1 ).
4 Problem Formulation
We studyonline inference-time action adaptationfor sequential LLM agents. Our goal is to
enable a frozen language model to improve its action choices over a stream of related
episodes by updating only a lightweight decision layer from interaction feedback, without
fine-tuning the backbone. This section develops the conceptual foundation in three steps: we
first show that ReAct-style action selection naturally maps to a contextual bandit problem,
then identify a linear decision interface inside the frozen LLM that can serve as the bandit’s
scoring mechanism, and finally argue that this structure enables principled online adaptation
with exploration.
4.1 ReAct Action Selection as a Contextual Bandit
Consider a stream of ReAct-style episodes e= 1, 2,. . ., N. Using the notation from Sec-
tion 3.2, at step t of episode e the agent faces a decision context xe,t = (qe, he,t−1 ) and
must choose the next action from Avalid
e,t ⊆ Ae, the subset of actions still available at that
step. After acting, the agent observes feedback only for the selected action—the rewards of
alternative actions remain unknown.
This per-step structure directly mirrors the contextual bandit setting of Section 3.1: a context-
dependent choice from a discrete action set under partial feedback. The key additional
observation is that, although full trajectories differ across tasks,similar local decision states
recuracross a stream of related episodes. When the same or a closely related action-selection
problem appears again, feedback collected from earlier decisions becomes informative.
This recurrence creates an opportunity for deployment-time learning that purely static
prompting cannot exploit. We therefore cast each action-selection step in the ReAct loop as
a round of an online contextual decision problem. The remainder of this section develops
the representation and adaptation mechanism that make this casting concrete.
4.2 The LLM’s Action-Selection Interface as a Linear Bandit
The bandit perspective above requires a contextual representation of each decision state and
a scoring rule over candidate actions. We now show that the frozen LLM already provides
both.
4

## Page 5

Preprint. Under review.
At the token position immediately preceding the next action decision, the model’s last-layer
hidden state
ue,t =h LLM(qe,h e,t−1 )∈R d (1)
encodes the task semantics and the full trajectory so far. Intuitively, this vector is the model’s
internal answer to the local question:what action should come next?
To produce a next-token distribution, the frozen model scores each vocabulary token through
its output projection layer. When the output vocabulary is restricted to the candidate action
setA valid
e,t , this projection reduces to a per-action linear score
s0(ue,t,a) =w ⊤
a ue,t, (2)
where wa ∈R d is the frozen parameter row associated with action a—concretely, the
corresponding row of the language-model head or an embedding derived from the same
model.
This decomposition reveals that the frozen LLM’s action-selection mechanism is already
acontextual linear scorer: the hidden state serves as the context vector and the per-action
parameters serve as arm-specific weights, exactly the structure assumed by linear contextual
bandits. We emphasize that we are not claiming the full LLM is a bandit; rather, we isolate
itsaction-selection interfaceas a linear scoring layer that can be separated from the underlying
reasoning dynamics.
This observation is the conceptual basis of our method. Because the frozen scoring layer
{wa} is fixed, it cannot adapt to deployment feedback. But the same linear structure admits
alearnablereplacement: a per-action parameter θa that starts from the LLM’s prior and
is updated online as the agent accumulates interaction experience. The next subsection
describes the adaptation mechanism that this structure enables.
4.3 Online Adaptation and Exploration
Replacing the frozen scoring weights with learnable parameters creates an online learning
problem: the agent must estimate which actions yield high reward in each context from
a growing stream of partial-feedback interactions. A critical challenge is that feedback is
observedonly for the selected action. If the learner always picks the action that currently looks
best, it may never discover that an under-explored action is superior in a given context.
Existing inference-time adaptation methods do not address this challenge directly. Prompt-
based approaches such as reflection (Shinn et al., 2023) and memory augmentation (Ma-
jumder et al., 2023) influence behavior indirectly through context manipulation, but they
have no mechanism to systematically explore uncertain actions or to quantify how confident
the agent is about each candidate.
The linear bandit structure identified in Section 4.2 provides a principled solution. Because
the learner maintains an explicit parametric model of action quality, it can estimate not only
the expected reward of each action but also theuncertaintyof that estimate. An optimistic
selection rule can then add an exploration bonus proportional to the current uncertainty,
favoring actions whose reward is still poorly characterized. As more feedback is collected,
the uncertainty shrinks and the learner concentrates on high-reward actions—balancing
exploration and exploitation automatically.
5 Methodology
This section presents OLIVIA, the concrete instantiation of the framework outlined in
Section 4. OLIVIA operates entirely at the action-selection interface of a frozen LLM: the
model’s reasoning process generates a trajectory-dependent hidden state, and a lightweight
online decision layer selects the next action from the valid candidate set based on that
hidden state. All backbone parameters, prompts, and reasoning generation remain fixed
throughout deployment; only the decision layer is updated from online feedback.
5

## Page 6

Preprint. Under review.
5.1 Hidden-State Decision Layer
At each decision step t of episode e, the frozen LLM processes the current task qe and trajec-
tory prefix he,t−1 . We extract the last-layer hidden state at the token position immediately
preceding the next action token:
ue,t =h LLM(qe,h e,t−1 )∈R d. (3)
This vector serves as the contextual input to the online controller. It encodes both the
original task semantics and the evolving reasoning history, so two decision points that
share similar task structure and trajectory prefixes produce similar context vectors, enabling
generalization across episodes.
For each candidate actiona, OLIVIA maintains per-action sufficient statistics
Aa ∈R d×d ,b a ∈R d, ˆθa =A −1
a ba, (4)
where ˆθa is the current estimate of the action’s reward parameter. The base predicted reward
for actionain contextu e,t is
se,t(a) = ˆθ⊤
a ue,t. (5)
LLM-aligned initialization.Rather than starting from a random policy, we warm-start
the controller from the frozen model’s own prior. We initialize
A(0)
a =I,b (0)
a =embed(a), (6)
where embed(a)∈R d is the mean input embedding of the action’s name tokens under
the same LLM. Because A(0)
a =I , the initial parameter satisfies ˆθ(0)
a =embed(a) , so the
controller’s starting scores are aligned with the frozen model’s representation of each action.
This initialization is especially valuable early in the stream before substantial feedback has
been collected, as it ensures the controller inherits the semantic priors already encoded in
the language model.
5.2 UCB-Based Exploration
The partial-feedback nature of the problem (Section 4.3) demands a selection rule that
actively explores uncertain actions. We adopt the LinUCB strategy (Li et al., 2010), which
augments the predicted reward with an exploration bonus that reflects the learner’s uncer-
tainty about each action in the current context.
Given contextu e,t, each valid actiona∈ Avalid
e,t is scored by
UCBe,t(a) = ˆθ⊤
a ue,t +α
q
u⊤
e,t A−1a ue,t, (7)
where α> 0 is the exploration coefficient. The first term is the current reward estimate; the
second term is the exploration bonus, proportional to the width of the confidence interval
for actionain the direction of the current context. The selected action is
ae,t ∈arg max
a∈Avalid
e,t
UCBe,t(a). (8)
The exploration bonus has two desirable properties. First, it iscontext-dependent: the bonus
for a given action varies with the decision state, so the controller explores actions that are
uncertain in the current context rather than exploring uniformly at random. Second, it
shrinks automaticallyas data accumulates: each observation tightens the confidence ellipsoid,
reducing the bonus for well-characterized actions and concentrating selection on those that
remain uncertain. These properties distinguish UCB from simpler alternatives. ε-greedy
exploration selects randomly and ignores the structure of the context space; Thompson
sampling introduces stochastic noise that can be harder to diagnose in deployment; prompt-
based adaptation methods have no explicit exploration mechanism at all.
6

## Page 7

Preprint. Under review.
The valid action set Avalid
e,t ⊆ Ae may shrink during an episode: once an action has been
selected the maximum allowed number of times, it is removed from the candidate set. This
constraint prevents degenerate repetition while still allowing the controller to select the
same tool more than once when warranted by the ground-truth trajectory.
The coefficient α controls exploration aggressiveness. Smaller values place more weight on
the current reward estimate and the LLM-aligned prior; larger values encourage broader
exploration early in the stream. We study the sensitivity toαempirically in Section 6.3.
5.3 Step-Level Feedback and Online Update
ToolBenchTaskBenchTaskBench-mm BFCL 
Qwen/Qwen3-4BMistral-7B-v0.1AccuracyAccuracy0 2002006000 2002006000 2002006000 200200600
0 2002006000 2002006000 2002006000 200200600
0.20.30.1
0.2
0.20.3
0.20.30.10.2
0.20.3
0.1
0.2
0.10.2
Step Step Step Step
Figure 2: Running-average F1 over the episode stream on the four benchmarks. Static
baselines (CoT, BM25, ReAct) remain flat; online methods improve over time. OLIVIA
converges faster and reaches higher final F1 than CLIN.
Reward signal.In our tool-use instantiation, each episode e is associated with a ground-
truth tool multiset Ge. Let Grem
e,t denote the unmatched portion of that multiset before step t.
After selecting actiona e,t, the agent receives immediate binary feedback:
re,t =1[a e,t ∈G rem
e,t ]. (9)
If re,t = 1, one occurrence of ae,t is removed from Grem
e,t so that each ground-truth tool can
be matched at most once. This provides a step-level learning signal that directly reflects
action-selection quality, in contrast to episode-level feedback that conflates all decisions
within a trajectory.
Online update.After observing reward re,t, only the statistics of the selected action are
updated via a rank-one rule:
Aae,t ←A ae,t +u e,tu⊤
e,t,b ae,t ←b ae,t +r e,t ue,t. (10)
The parameter estimate is then ˆθae,t =A −1
ae,t bae,t . In practice, we maintain the inverse A−1
a
incrementally using the Sherman–Morrison formula, so each update requires O(d2) time
and avoids re-inverting the full covariance matrix.
The episode terminates when the agent emits a stop action, no valid action remains, or
the per-episode step budget is exhausted. Across the full episode stream, the cumulative
reward is the objective we seek to maximize through online adaptation.
Design summary.The three components above—hidden-state context extraction, UCB-
based exploration, and rank-one online updates—together constitute the OLIVIA decision
layer. All backbone LLM parameters, the prompt template, and the reasoning generator re-
main frozen throughout deployment. The only learned quantities are the per-action statistics
{Aa,b a}, which are lightweight and updated incrementally from step-level feedback.
7

## Page 8

Preprint. Under review.
Dataset
Model Method ToolBench TaskBench TaskBench-MM BFCL
qwen
CoT 0.211 0.030 0.031 0.082
BM25 0.353 0.116 0.127 0.181
ReAct 0.520 0.174 0.162 0.272
Bandit 0.348 0.155 0.126 0.242
CLIN 0.553 0.2110.170 0.307
OLIVIA (Ours) 0.5850.205 0.178 0.366
mistral
CoT 0.142 0.036 0.064 0.107
BM25 0.353 0.116 0.127 0.181
ReAct 0.386 0.178 0.146 0.281
Bandit 0.348 0.155 0.126 0.242
CLIN 0.394 0.193 0.127 0.324
OLIVIA (Ours) 0.420 0.208 0.207 0.352
Table 1: Main results (F1) across four benchmarks and two backbone models. First three
baselines with fixed policies; following methods below areonline learningmethods that
adapt from deployment feedback.
6 Experiments
6.1 Experimental Setup
Benchmarks.We evaluate on four tool-use benchmarks: TOOLBENCH(Xu et al., 2023),
TASKBENCH, TASKBENCH-MM (Shen et al., 2024), and BFCL (Patil et al., 2023). These
benchmarks span complementary tool-use settings, varying in task domain, modality, and
candidate-set size. Each instance provides a natural-language task, a candidate tool set,
and one or more reference tool-call trajectories. Following our formulation, we convert
each reference completion into a ground-truth tool multiset and evaluate all methods as
sequential tool-selection policies under the same candidate tool set.
Backbone models.We use Qwen/Qwen3-4B (Yang et al., 2025) and
mistralai/Mistral-7B-v0.1 (Jiang et al., 2023) as base language models, chosen as
representative open-weight backbones that support ReAct-style tool use while remaining
practical for repeated online evaluation. We keep the backbone, system prompt, and
few-shot demonstrations fixed across all methods so that performance differences can be
attributed to the decision policy alone.
Baselines.We compare against both non-learning and inference-time adaptation baselines.
CoT(Wei et al., 2023) uses chain-of-thought prompting for free-form reasoning and tool
selection without online adaptation.BM25(Robertson & Zaragoza, 2009) ranks candidate
tools by lexical similarity to the task description.ReAct(Yao et al., 2023b) performs iterative
reasoning and tool selection but does not adapt across episodes.CLIN(Majumder et al.,
2023) is a memory-based continual-adaptation method that updates a persistent textual
memory after each episode to improve future decisions.
Online protocol.Each dataset is treated as a stream of episodes. For every seed, we
randomly shuffle the episode order and run each method sequentially over that stream,
reporting mean and standard deviation over three random seeds. All methods use the same
per-episode step budget B=|G|+s , where |G| is the ground-truth tool-multiset size and s
is a small fixed allowance for recovery from early mistakes, and each tool is capped at m
selections per episode to prevent degenerate repetition.
Evaluation Metrics.We evaluate tool-selection quality using multiset-matching precision,
recall, and F1 (Patil et al., 2023), reporting macro-averaged scores over episodes with F1 as
the primary metric. For the synthetic experiments described in Section 6.3, we additionally
report cumulative regret and parameter estimation error∥ ˆθt −θ ⋆∥2
2.
8

## Page 9

Preprint. Under review.
0 25 50 75 100
Cumulative Regret
0
10
20
30
40
0 100 200 300 400
Avg F1
0.20
0.25
0.30
0.35
0.40
0.45
0.50
0 150 300 450 600
 Error
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
0 150 300 450 600
Optimal-Action Rate
0.2
0.4
0.6
0.8
1.0
Both ( =0.1)
 Final Only ( =0.1)
 Intermediate ( =0.1)
 Random
Figure 3: Synthetic experiments. Left: cumulative regret over rounds. Right: parameter esti-
mation error ∥ˆθt −θ ⋆∥2
2. OLIVIA converges faster and recovers the true reward parameter
more accurately.
6.2 Results
Learning curves.Figure 2 plots running-average F1 over the episode stream. Static
baselines (CoT, BM25, ReAct) produce flat reference lines since their policies are fixed.
Among the online methods, CLIN improves gradually through episodic memory updates,
but OLIVIA improves faster and converges to a higher F1 across all four benchmarks.
This demonstrates the core deployment-time claim: the lightweight decision layer converts
sparse step-level feedback into steadily better action selection, without modifying the
backbone model.
6.3 Ablation Studies
Synthetic validation.To validate the online controller in a setting where the ground-
truth reward structure is known, we construct synthetic contextual decision streams with
linear rewards governed by an unknown θ⋆ and partial feedback. Figure 3 shows that
OLIVIA achieves lower cumulative regret and parameter estimation error than weaker
online baselines, confirming that the controller recovers the true decision structure rather
than improving by chance.
Effect of the exploration coefficient.We vary the LinUCB exploration coefficient α while
keeping the rest of the method fixed. Table 2 shows that OLIVIA is robust across a rea-
sonable range of α values but performs best in a moderate regime. When α is too small,
the controller under-explores and is slower to correct early mistakes; when α is too large,
excessive optimism leads to unnecessary exploration and weaker final performance.
Table 2: Reward-design ablation on synthetic
streams.
Reward Performance Convergence
Avg
F1(↑)
Opt. Rate
(%)(↑)
Regret
@100(↓)
∥θ−θ∗∥2
(↓)
Final 0.323 36.2 56.3 16.48
Step 0.536 98.0 8.20.00
Both 0.536 98.2 8.33.04
Effect of reward design.We compare
three reward configurations:step-level
only,final only, andboth. Table 2 shows
that step-level feedback is substantially
more effective than final-only reward,
confirming that local credit assignment
is important in multi-step tool selec-
tion. Combining both signals yields the
strongest overall performance, suggest-
ing that dense local feedback and episode-
level evaluation provide complementary
training signals.
7 Conclusion
We presented OLIVIA, an inference-time action adaptation framework for ReAct-style
agents. By placing an explicit online decision layer at the action-selection interface of a
frozen language model, OLIVIA adapts behavior directly from action-level feedback while
preserving the underlying reasoning process. Instantiated as a contextual linear bandit over
9

## Page 10

Preprint. Under review.
hidden decision states, the method provides lightweight online updates, explicit uncertainty
estimates, and sample-efficient exploration through UCB. Across four benchmarks, OLIVIA
consistently improves task performance over static ReAct and prompt-based inference-time
baselines, showing that deployment-time adaptation can be achieved without model fine-
tuning. More broadly, our results suggest that explicit online decision layers are a promising
alternative to purely prompt- or retrieval-based adaptation for sequential decision making
in LLM agents.
LLM usage:AI writing tools were used to assist with drafting and the icons in Figure1 are
generated by AI drawing tool.
References
Yikun Ban, Yunzhe Qi, and Jingrui He. Neural contextual bandits for personalized recom-
mendation, 2023. URLhttps://arxiv.org/abs/2312.14037.
Tiffany Tianhui Cai, Hongseok Namkoong, Daniel Russo, and Kelly W Zhang. Active
exploration via autoregressive generation of missing data, 2025. URL https://arxiv.
org/abs/2405.19466.
Arthur Chen, Zuxin Liu, Jianguo Zhang, Akshara Prabhakar, Zhiwei Liu, Shelby Heinecke,
Silvio Savarese, Victor Zhong, and Caiming Xiong. Test-time adaptation for llm agents
via environment interaction, 2026. URLhttps://arxiv.org/abs/2511.04847.
Shibo Hao, Yi Gu, Haodi Ma, Joshua Jiahua Hong, Zhen Wang, Daisy Zhe Wang, and
Zhiting Hu. Reasoning with language model is planning with world model, 2023. URL
https://arxiv.org/abs/2305.14992.
Songwen Hu, Ryan A. Rossi, Tong Yu, Junda Wu, Handong Zhao, Sungchul Kim, and
Shuai Li. Interactive visualization recommendation with hier-SUCB. InTHE WEB
CONFERENCE 2025, 2025. URLhttps://openreview.net/forum?id=Hkh2umURYm.
Chengkai Huang, Junda Wu, Yu Xia, Zixu Yu, Ruhan Wang, Tong Yu, Ruiyi Zhang, Ryan A.
Rossi, Branislav Kveton, Dongruo Zhou, Julian McAuley, and Lina Yao. Towards agentic
recommender systems in the era of multimodal large language models, 2025a. URL
https://arxiv.org/abs/2503.16734.
Chengkai Huang, Junda Wu, Zhouhang Xie, Yu Xia, Rui Wang, Tong Yu, Subrata Mitra,
Julian McAuley, and Lina Yao. Pluralistic off-policy evaluation and alignment.arXiv
preprint arXiv:2509.19333, 2025b.
Yuichi Inoue, Kou Misaki, Yuki Imajuku, So Kuroki, Taishi Nakamura, and Takuya Akiba.
Wider or deeper? scaling llm inference-time compute with adaptive branching tree search,
2025. URLhttps://arxiv.org/abs/2503.04412.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh
Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile
Saulnier, L´elio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut
Lavril, Thomas Wang, Timoth´ee Lacroix, and William El Sayed. Mistral 7b, 2023. URL
https://arxiv.org/abs/2310.06825.
Jing Yu Koh, Stephen McAleer, Daniel Fried, and Ruslan Salakhutdinov. Tree search for
language model agents, 2026. URLhttps://arxiv.org/abs/2407.01476.
Branislav Kveton, Xintong Li, Julian McAuley, Ryan Rossi, Jingbo Shang, Junda Wu,
and Tong Yu. Active learning for direct preference optimization.arXiv preprint
arXiv:2503.01076, 2025.
Lihong Li, Wei Chu, John Langford, and Robert E. Schapire. A contextual-bandit approach
to personalized news article recommendation. InProceedings of the 19th international
conference on World wide web, WWW ’10, pp. 661–670. ACM, April 2010. doi: 10.1145/
1772690.1772758. URLhttp://dx.doi.org/10.1145/1772690.1772758.
10

## Page 11

Preprint. Under review.
Jiahao Liu, Qifan Wang, Jingang Wang, and Xunliang Cai. Speculative decoding via early-
exiting for faster llm inference with thompson sampling control mechanism, 2024. URL
https://arxiv.org/abs/2406.03853.
Xiaofan Lu, Yixiao Zeng, Feiyang Ma, Zixu Yu, and Marco Levorato. Improving multi-
candidate speculative decoding, 2024. URLhttps://arxiv.org/abs/2409.10644.
Bodhisattwa Prasad Majumder, Bhavana Dalvi Mishra, Peter Jansen, Oyvind Tafjord, Niket
Tandon, Li Zhang, Chris Callison-Burch, and Peter Clark. Clin: A continually learning
language agent for rapid task adaptation and generalization, 2023. URL https://arxiv.
org/abs/2310.10134.
Gagan Mundada, Zihan Huang, Rohan Surana, Sheldon Yu, Jennifer Yuntong Zhang, Xin-
tong Li, Tong Yu, Lina Yao, Jingbo Shang, Julian McAuley, et al. Ws-grpo: Weakly-
supervised group-relative policy optimization for rollout-efficient reasoning.arXiv
preprint arXiv:2602.17025, 2026.
Dang Nguyen, Jian Chen, Yu Wang, Gang Wu, Namyong Park, Zhengmian Hu, Hanjia Lyu,
Junda Wu, Ryan Aponte, Yu Xia, et al. Gui agents: A survey. InFindings of the Association
for Computational Linguistics: ACL 2025, pp. 22522–22538, 2025.
Shishir G. Patil, Tianjun Zhang, Xin Wang, and Joseph E. Gonzalez. Gorilla: Large language
model connected with massive apis, 2023. URLhttps://arxiv.org/abs/2305.15334.
Stephen Robertson and Hugo Zaragoza. The probabilistic relevance framework: Bm25
and beyond.Found. Trends Inf. Retr., 3(4):333–389, April 2009. ISSN 1554-0669. doi:
10.1561/1500000019. URLhttps://doi.org/10.1561/1500000019.
Yongliang Shen, Kaitao Song, Xu Tan, Wenqi Zhang, Kan Ren, Siyu Yuan, Weiming Lu,
Dongsheng Li, and Yueting Zhuang. Taskbench: Benchmarking large language models
for task automation, 2024. URLhttps://arxiv.org/abs/2311.18760.
Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan,
and Shunyu Yao. Reflexion: Language agents with verbal reinforcement learning, 2023.
URLhttps://arxiv.org/abs/2303.11366.
Rohan Surana, Gagan Mundada, Xunyi Jiang, Chuhan Wang, Zhenwei Tang, Difan Jiao,
Zihan Huang, Yuxin Xiong, Junda Wu, Sheldon Yu, Xintong Li, Raghav Jain, Nikki
Kuang, Sizhe Zhou, Bowen Jin, Zhendong Chu, Tong Yu, Ryan Rossi, Kuan-Hao Huang,
Jingbo Shang, Jiawei Han, and Julian McAuley. Generate, filter, control, replay: A
comprehensive survey of rollout strategies for llm reinforcement learning, 2026. URL
https://arxiv.org/abs/2605.02913.
Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi
Fan, and Anima Anandkumar. Voyager: An open-ended embodied agent with large
language models, 2023. URLhttps://arxiv.org/abs/2305.16291.
Ruoyu Wang, Junda Wu, Yu Xia, Tong Yu, Ryan A Rossi, Julian McAuley, and Lina Yao.
Dice: Dynamic in-context example selection in llm agents via efficient knowledge transfer.
arXiv preprint arXiv:2507.23554, 2025a.
Yu Wang, Xinshuang Liu, Xiusi Chen, Sean OBrien, Junda Wu, and Julian McAuley. Self-
updatable large language models by integrating context into model parameters. In
International Conference on Learning Representations, volume 2025, pp. 16961–16979, 2025b.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi,
Quoc Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large lan-
guage models, 2023. URLhttps://arxiv.org/abs/2201.11903.
Junda Wu, Rohan Surana, Zhouhang Xie, Yiran Shen, Yu Xia, Tong Yu, Ryan A Rossi,
Prithviraj Ammanabrolu, and Julian McAuley. In-context ranking preference optimization.
InSecond Conference on Language Modeling, a.
11

## Page 12

Preprint. Under review.
Junda Wu, Yuxin Xiong, Xintong Li, Sheldon Yu, Zhengmian Hu, Tong Yu, Rui Wang, Xiang
Chen, Jingbo Shang, and Julian McAuley. Ctrls: Chain-of-thought reasoning via latent
state-transition. InThe 29th International Conference on Artificial Intelligence and Statistics, b.
Junda Wu, Canzhe Zhao, Tong Yu, Jingyang Li, and Shuai Li. Clustering of conversational
bandits for user preference learning and elicitation. InProceedings of the 30th ACM
International Conference on Information & Knowledge Management, pp. 2129–2139, 2021.
Junda Wu, Zhihui Xie, Tong Yu, Handong Zhao, Ruiyi Zhang, and Shuai Li. Dynamics-aware
adaptation for reinforcement learning based cross-domain interactive recommendation.
InProceedings of the 45th international ACM SIGIR conference on research and development in
information retrieval, pp. 290–300, 2022.
Junda Wu, Tong Yu, Rui Wang, Zhao Song, Ruiyi Zhang, Handong Zhao, Chaochao Lu,
Shuai Li, and Ricardo Henao. Infoprompt: Information-theoretic soft prompt tuning
for natural language understanding. InThirty-seventh Conference on Neural Information
Processing Systems, 2023. URLhttps://openreview.net/forum?id=mSNfjOcDUv.
Junda Wu, Hanjia Lyu, Yu Xia, Zhehao Zhang, Joe Barrow, Ishita Kumar, Mehrnoosh Mirta-
heri, Hongjie Chen, Ryan A Rossi, Franck Dernoncourt, et al. Personalized multimodal
large language models: A survey.arXiv preprint arXiv:2412.02142, 2024a.
Junda Wu, Tong Yu, Xiang Chen, Haoliang Wang, Ryan Rossi, Sungchul Kim, Anup Rao,
and Julian McAuley. Decot: Debiasing chain-of-thought for knowledge-intensive tasks in
large language models via causal intervention. InProceedings of the 62nd Annual Meeting
of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 14073–14087,
2024b.
Junda Wu, Zhehao Zhang, Yu Xia, Xintong Li, Zhaoyang Xia, Aaron Chang, Tong Yu,
Sungchul Kim, Ryan A Rossi, Ruiyi Zhang, et al. Visual prompting in multimodal large
language models: A survey.arXiv preprint arXiv:2409.15310, 2024c.
Junda Wu, Xintong Li, Ruoyu Wang, Yu Xia, Yuxin Xiong, Jianing Wang, Tong Yu, Xiang
Chen, Branislav Kveton, Lina Yao, et al. Ocean: Offline chain-of-thought evaluation and
alignment in large language models. InInternational Conference on Learning Representations,
volume 2025, pp. 100570–100589, 2025a.
Junda Wu, Yu Xia, Tong Yu, Xiang Chen, Sai Sree Harsha, Akash V Maharaj, Ruiyi Zhang,
Victor Bursztyn, Sungchul Kim, Ryan A Rossi, et al. Doc-react: Multi-page heterogeneous
document question-answering. InProceedings of the 63rd Annual Meeting of the Association
for Computational Linguistics (Volume 2: Short Papers), pp. 67–78, 2025b.
Yu Xia, Junda Wu, Tong Yu, Sungchul Kim, Ryan A Rossi, and Shuai Li. User-regulation
deconfounded conversational recommender system with bandit feedback. InProceedings
of the 29th ACM SIGKDD conference on knowledge discovery and data mining, pp. 2694–2704,
2023.
Yu Xia, Yiran Jenny Shen, Junda Wu, Tong Yu, Sungchul Kim, Ryan A Rossi, Lina Yao,
and Julian McAuley. Sand: Boosting llm agents with self-taught action deliberation. In
Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pp.
3062–3077, 2025.
Zhouhang Xie, Junda Wu, Yiran Shen, Raghav Jain, Yu Xia, Xintong Li, Aaron Chang,
Ryan A. Rossi, Tong Yu, Sachin Kumar, Bodhisattwa Prasad Majumder, Jingbo Shang,
Prithviraj Ammanabrolu, and Julian McAuley. A survey on personalized and pluralistic
preference alignment in large language models. InSecond Conference on Language Modeling,
2025. URLhttps://openreview.net/forum?id=lSWOMjonL7.
Qiantong Xu, Fenglu Hong, Bo Li, Changran Hu, Zhengyu Chen, and Jian Zhang. On
the tool manipulation capability of open-source large language models, 2023. URL
https://arxiv.org/abs/2305.16504.
12

## Page 13

Preprint. Under review.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu,
Chang Gao, Chengen Huang, Chenxu Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei
Huang, Feng Hu, Hao Ge, Haoran Wei, Huan Lin, Jialong Tang, Jian Yang, Jianhong Tu,
Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jing Zhou, Jingren Zhou, Junyang Lin, Kai Dang,
Keqin Bao, Kexin Yang, Le Yu, Lianghao Deng, Mei Li, Mingfeng Xue, Mingze Li, Pei
Zhang, Peng Wang, Qin Zhu, Rui Men, Ruize Gao, Shixuan Liu, Shuang Luo, Tianhao Li,
Tianyi Tang, Wenbiao Yin, Xingzhang Ren, Xinyu Wang, Xinyu Zhang, Xuancheng Ren,
Yang Fan, Yang Su, Yichang Zhang, Yinger Zhang, Yu Wan, Yuqiong Liu, Zekun Wang,
Zeyu Cui, Zhenru Zhang, Zhipeng Zhou, and Zihan Qiu. Qwen3 technical report, 2025.
URLhttps://arxiv.org/abs/2505.09388.
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, and
Karthik Narasimhan. Tree of thoughts: Deliberate problem solving with large language
models, 2023a. URLhttps://arxiv.org/abs/2305.10601.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and
Yuan Cao. React: Synergizing reasoning and acting in language models, 2023b. URL
https://arxiv.org/abs/2210.03629.
Weiran Yao, Shelby Heinecke, Juan Carlos Niebles, Zhiwei Liu, Yihao Feng, Le Xue, Rithesh
Murthy, Zeyuan Chen, Jianguo Zhang, Devansh Arpit, Ran Xu, Phil Mui, Huan Wang,
Caiming Xiong, and Silvio Savarese. Retroformer: Retrospective large language agents
with policy gradient optimization, 2024. URLhttps://arxiv.org/abs/2308.02151.
Sheldon Yu, Yuxin Xiong, Junda Wu, Xintong Li, Tong Yu, Xiang Chen, Ritwik Sinha,
Jingbo Shang, and Julian McAuley. Explainable chain-of-thought reasoning: An empirical
analysis on state-aware reasoning dynamics. In Christos Christodoulopoulos, Tanmoy
Chakraborty, Carolyn Rose, and Violet Peng (eds.),Findings of the Association for Com-
putational Linguistics: EMNLP 2025, pp. 16660–16667, Suzhou, China, November 2025.
Association for Computational Linguistics. ISBN 979-8-89176-335-7. doi: 10.18653/v1/
2025.findings-emnlp.904. URLhttps://aclanthology.org/2025.findings-emnlp.904/.
Kelly W. Zhang, Tiffany Tianhui Cai, Hongseok Namkoong, and Daniel Russo. Contextual
thompson sampling via generation of missing data, 2025. URL https://arxiv.org/abs/
2502.07064.
Zhehao Zhang, Ryan A Rossi, Branislav Kveton, Yijia Shao, Diyi Yang, Hamed Zamani,
Franck Dernoncourt, Joe Barrow, Tong Yu, Sungchul Kim, et al. Personalization of large
language models: A survey.arXiv preprint arXiv:2411.00027, 2024.
Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, and Gao Huang.
Expel: Llm agents are experiential learners, 2024. URL https://arxiv.org/abs/2308.
10144.
Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, and Yanlin Wang. Memorybank: Enhanc-
ing large language models with long-term memory, 2023. URL https://arxiv.org/abs/
2305.10250.
Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, and Yu-Xiong Wang.
Language agent tree search unifies reasoning acting and planning in language models,
2024. URLhttps://arxiv.org/abs/2310.04406.
13

## Page 14

Preprint. Under review.
A Appendix
A.1 Implementation Algorithm
Algorithm 1 summarizes the complete OLIVIA procedure. Each episode begins by receiving
a task and initializing the valid action set. At every decision step, the frozen LLM generates
a reasoning trace and produces the hidden-state context (line 6), the controller scores all
valid actions via LinUCB (line 8) and selects the maximizer (line 10). After observing the
step-level binary reward, the selected action’s sufficient statistics are updated in place using
the Sherman–Morrison rank-one formula (lines 16–17), requiring no gradient computation
or backward pass. The per-action inverse covariance and reward accumulator persist across
episodes, enabling the controller to improve over the full deployment stream.
Algorithm 1OLIVIA: Online Contextual Bandit for ReAct Tool Selection
1:Inputs: exploration parameterα>0, extra stepss, max selections per armm
2:Initialize: For each arma∈A:A −1
a ←I d,b a ←emb LLM(a),n a ←0
3:forepisodee=1 toTdo
4:Receive taskq e with ground-truth tool multisetG e; setV ← A,Le ← |Ge|+s
5:fort=1 toL e do
6:Generate thoughtz e,t via LLM conditioned on(q e,z e,<t ,a e,<t )
7:Extract contextx e,t ←h LLM
 
qe,z e,1:t ,a e,<t

{last hidden state at action position}
8:for alla∈ Vdo
9:θ a ←A −1
a ba, ucb e,t(a)←θ ⊤
a xe,t +α
q
x⊤
e,t A−1a xe,t
10:end for
11:Selecta e,t ←arg max a∈V ucbe,t(a)
12:Executea e,t; observe per-step rewardr e,t =1

ae,t ∈G rem
e

13:ifr e,t =1then
14:Decrement remaining countG rem
e (ae,t)
15:end if
16:Update selection countn ae,t +=1; ifn ae,t ≥mremovea e,t fromV
17:Policy update(Sherman–Morrison):
18:k←A −1
ae,t xe,t
19:A −1
ae,t ←A −1
ae,t − k k⊤
1+x ⊤
e,tk ,b ae,t ←b ae,t +r e,t xe,t
20:ifV=∅then
21:break{all arms exhausted}
22:end if
23:end for
24:Compute episode metrics: recall e, precisione, F1e
25:end for
A.2 Case Study
We present qualitative examples from the ToolBench2 benchmark ( Qwen3-4B, α=0.1) to
illustrate how OLIVIA’s online controller improves tool selection over the episode stream.
Learning progression.The following two boxes show thesame taskencountered early
(episode 3) and late (episode 935) in the stream. Early on, the controller has not yet accu-
mulated feedback and selects entirely unrelated tools (F1 = 0.00). By episode 935, online
updates have shifted the per-action estimates so that all three ground-truth tools are recov-
ered (recall = 1.00), despite the first three actions still being misses—demonstrating that the
UCB exploration bonus eventually directs selection toward the correct tools.
14

## Page 15

Preprint. Under review.
Episode 3 — Early Stream (F1
Task:I’m organizing a team building activity for my company. Can you help me create a
short URL for the event details? Also, suggest some domain options for the team building
link. Furthermore, provide me with a list of available domains for branding the short link.
Ground truth (3):bitly.shorten, URL Link Shortener.Create a new link, URL Link Shortener.Get
a list of domains
1.Thought:The user needs a short URL for the event details.
Action:OTT details.New Arrivals✗
2.Thought:The user also wants domain options for the short link.
Action:Streaming Availability.Get Basic✗
3.Thought:Additionally, the user needs a list of available domains for branding.
Action:Similar Movies.find similar✗
4.Thought:Now, I need to check if all the actions have been completed.
Action:Watchmode.Streaming Release Dates✗
5.Thought:All required actions have been completed.
Action:Vimeo.GetRelatedChannels✗
6.Thought:The user’s task is complete.
Action:Movie, TV , music search and download.Get Monthly Top 100 Music Torrents✗
Result:P=0.00, R=0.00, F1=0.00
Episode 935 — Late Stream (F1
Task:I’m organizing a team building activity for my company. Can you help me create a
short URL for the event details? Also, suggest some domain options for the team building
link. Furthermore, provide me with a list of available domains for branding the short link.
Ground truth (3):bitly.shorten, URL Link Shortener.Create a new link, URL Link Shortener.Get
a list of domains
1.Thought:The user needs a short URL for the event details.
Action:Watchmode.Title Seasons✗
2.Thought:The user also wants domain options for the short link.
Action:Watchmode.New Titles✗
3.Thought:Additionally, the user is looking for a list of available domains for branding.
Action:Streaming Availability.Search Pro✗
4.Thought:Now, I need to check if all the actions have been completed.
Action:URL Link Shortener.Create a new link✓
5.Thought:All tasks are completed.
Action:bitly.shorten✓
6.Thought:The final answer is ready.
Action:URL Link Shortener.Get a list of domains✓
Result:P=0.50, R=1.00, F1=0.67
Learned controller.By episode 1130, the controller has accumulated enough feedback to
select all three ground-truth tools within the first four steps, even on a previously unseen
task phrasing.
15

## Page 16

Preprint. Under review.
Episode 1130 — Complex Task, 7/9 GT Tools (F1
Task:I’m organizing a movie marathon for my company’s team-building event. Could you
suggest some action movies from the 90s that are available for streaming on Netflix, Prime
Video, and Hulu? Please include the IMDb ratings and streaming links for each movie.
Ground truth (9):Watchmode.List Titles, Watchmode.New People, Watchmode.Title Seasons,
OTT details.Basic Info, OTT details.Advanced Search, OTT details.Title Details, Streaming
Availability.Search By Title, Streaming Availability.Search Ultra, Streaming Availability.Search
Pro
1.Thought:The user is looking for action movies from the 90s.
Action:Vimeo.SearchVideos✗
2.Thought:The user wants to know where these movies are available for streaming.
Action:Watchmode.List Titles✓
3.Thought:The user is interested in IMDb ratings for these movies.
Action:Streaming Availability.Search Ultra✓
4.Thought:The user wants the actual streaming links for each movie.
Action:OTT details.Basic Info✓
5.Thought:The information should be accurate and up-to-date for a company event.
Action:Streaming Availability.Search Pro✓
6.Thought:The information needs to be concise and easy to share with the team.
Action:Watchmode.Title Seasons✓
7.Thought:The user is likely looking for a variety of options to cater to different tastes.
Action:OTT details.Title Details✓
8. Thought:The user might also want to know the release years to ensure they are from the
90s.
Action:OTT details.Search✗
9. Thought:The information should be organized in a way that is easy to use during the
marathon.
Action:OTT details.Additional Title Details✗
10.Thought:The user is looking for movies that can be watched in a short time frame.
Action:Streaming Availability.Search By Title✓
11.Thought:The movies should be engaging and suitable for a group setting.
Action:Similar Movies.find similar✗
12.Thought:The user is looking for movies that are well-received with good action elements.
Action:Vimeo.GetChannelVideos✗
Result:P=0.58, R=0.78, F1=0.67
A.3 Per-Benchmark Learning Curves
We report per-benchmark learning curves for both backbone models. Each plot shows
running-average F1 over the episode stream. Non-learning baselines (CoT, BM25, ReAct)
appear as flat reference lines; online methods (Bandit, CLIN, OLIVIA) evolve as they
accumulate feedback.
Qwen3-4B.
Mistral-7B.
A.4 Reward Studies
Each panel shows the three reward metrics (Avg Recall, Avg F1, Avg Precision) with the
same smoothing, bands, and styling as before. The shared legend sits at the top center, and
only the bottom row has x-axis labels / left column has y-axis labels to keep it clean.
16

## Page 17

Preprint. Under review.
0 100 200 300 400 500
Step
0.2
0.3
0.4
0.5
0.6Value
Qwen / Toolbench
BM25
C2S
CoT
ReAct
CLIn
Figure 4: Qwen3-4B on ToolBench.
0 100 200 300 400 500
Step
0.025
0.050
0.075
0.100
0.125
0.150
0.175
0.200
0.225Value
Qwen / Taskbench
BM25
C2S
CoT
ReAct
CLIn Figure 5: Qwen3-4B on TaskBench.
0 100 200 300 400 500
Step
0.02
0.04
0.06
0.08
0.10
0.12
0.14
0.16
0.18Value
Qwen / Taskmm
BM25
C2S
CoT
ReAct
CLIn
Figure 6: Qwen3-4B on TaskBench-MM.
0 100 200 300 400 500
Step
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40Value
Qwen / Bfcl
BM25
C2S
CoT
ReAct
CLIn Figure 7: Qwen3-4B on BFCL.
0 100 200 300 400 500
Step
0.10
0.15
0.20
0.25
0.30
0.35
0.40
0.45Value
Mistral / Toolbench
BM25
C2S
CoT
ReAct
CLIn
Figure 8: Mistral-7B on ToolBench.
0 100 200 300 400 500
Step
0.025
0.050
0.075
0.100
0.125
0.150
0.175
0.200
0.225Value
Mistral / Taskbench
BM25
C2S
CoT
ReAct
CLIn Figure 9: Mistral-7B on TaskBench.
0 100 200 300 400 500
Step
0.050
0.075
0.100
0.125
0.150
0.175
0.200
0.225Value
Mistral / Taskmm
BM25
C2S
CoT
ReAct
CLIn
Figure 10: Mistral-7B on TaskBench-MM.
0 100 200 300 400 500
Step
0.10
0.15
0.20
0.25
0.30
0.35Value
Mistral / Bfcl
BM25
C2S
CoT
ReAct
CLIn Figure 11: Mistral-7B on BFCL.
17

## Page 18

Preprint. Under review.
0 100 200 300 400 500 600
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0Value
Both (α=0.1)
0 100 200 300 400 500 600
0.2
0.4
0.6
0.8
1.0
Final Only (α=0.1)
0 100 200 300 400 500 600
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Intermediate (α=0.1)
0 100 200 300 400 500 600
Episode
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0Value
Intermediate (α=0.5)
0 100 200 300 400 500 600
Episode
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
Intermediate (α=1.0)
0 100 200 300 400 500 600
Episode
0.10
0.15
0.20
0.25
0.30
0.35
0.40
0.45
0.50
Random
Avg Recall Avg F1 Avg Precision
Figure 12: Reward Studies.
18
