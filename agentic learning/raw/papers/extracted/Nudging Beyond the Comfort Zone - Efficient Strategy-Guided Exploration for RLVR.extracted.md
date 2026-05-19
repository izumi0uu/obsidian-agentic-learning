# Nudging Beyond the Comfort Zone: Efficient Strategy-Guided Exploration for RLVR - Extracted Text

- Source note: [[Nudging Beyond the Comfort Zone - Efficient Strategy-Guided Exploration for RLVR]]
- Source PDF: `assets/Nudging Beyond the Comfort Zone - Efficient Strategy-Guided Exploration for RLVR.pdf`
- Extracted: 2026-05-18
- Extractor: pypdf
- Pages: 28
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

Nudging Beyond the Comfort Zone:
Efficient Strategy-Guided Exploration for RLVR
Chanuk Lee1* Sangwoo Park1* Minki Kang1 Sung Ju Hwang1,2
1KAIST 2DeepAuto.ai
{tallyforce, swgger}@kaist.ac.kr
Abstract
Reinforcement learning with verifiable rewards (RLVR) has emerged as a scalable
paradigm for improving the reasoning capabilities of large language models. How-
ever, its effectiveness is fundamentally limited by exploration: the policy can only
improve on trajectories it has already sampled. While increasing the number of
rollouts alleviates this issue, such brute-force scaling is computationally expensive,
and existing approaches that modify the optimization objective provide limited
control over what is explored. In this work, we propose NUDGERL, a framework
for structured and diversity-driven exploration in RLVR. Our approach introduces
Strategy Nudging, which conditions each rollout on lightweight, strategy-level
contexts to induce diverse reasoning trajectories without relying on expensive
oracle supervision. To effectively learn from such structured exploration, we fur-
ther propose a unified objective, which decomposes the reward signal into inter-
and intra-context components and incorporates a distillation objective to transfer
discovered behaviors back to the base policy. Empirically, NUDGERL outper-
forms standard GRPO with up to 8× larger rollout budgets, while outperforming
oracle-guided RL baseline on average across five challenging math benchmarks.
These results demonstrate that structured, context-driven exploration can serve
as an efficient and scalable alternative to both brute-force rollout scaling and
feasibility-oriented methods based on privileged information. Our code is available
athttps://github.com/tally0818/NudgeRL.
1 Introduction
Reinforcement learning with verifiable rewards (RLVR) has emerged as a powerful paradigm for
improving the reasoning capabilities of large language models (LLMs) [ 7, 20]. By leveraging
verifiable rewards, methods such asGroup-Relative Policy Optimization(GRPO) [ 18] enable scalable
post-training without requiring dense supervision. This paradigm has been successfully applied
across a wide range of domains.
Despite its success, RLVR remains fundamentally limited by its ability to explore the space of
reasoning trajectories. A natural approach is to scale the number of sampled rollouts, which increases
the probability of discovering rare trajectories [5]. However, such brute-force scaling quickly becomes
computationally prohibitive, motivating alternative approaches that improve exploration efficiency.
Recent work has sought to address this limitation by modifying the optimization objective, for
example through entropy regularization or decoupled clipping [ 24, 26]. While these methods
encourage broader exploration at the distribution level, they provide limited control overwhatis
explored, and often fail to ensure coverage of semantically meaningful reasoning strategies. Another
*Equal contribution
Preprint.
arXiv:2605.15726v1  [cs.AI]  15 May 2026

## Page 2

Question
C: Induction on natural numbersB: Linear functions and their propertiesA: Cauchy’s functional equationPotentialStrategies
𝜋!LLMRollout 1 ARollout 2 ARollout 3 B Naive Sampling collapses to the Dominant Mode(a) Naive Sampling (GRPO)Q + AQ + BQ + C Rollout 1 ARollout 2 BRollout 3 CLLM(b) Strategy Nudging (NudgeRL)
Standard Nudging allows sampling Diverse Modes
(c) Effect of Strategic Nudging
Determine all functions 𝑓:ℕ!→ℝsatisfying 𝑓𝑥+𝑦+𝑓𝑥−𝑦=𝑓(3𝑥)for all 𝑥,𝑦
𝜋!
       
*URXSFRXQW




)UDFWLRQRISUREOHPV
6WUDWHJ\1XGJLQJ
1DLYH6DPSOLQJ
Figure 1:Concept: Improving exploration diversity through Strategy Nudging.(a) Naive
sampling methods (e.g., GRPO) often collapse to a dominant reasoning mode, limiting the exploration
of the reasoning space. (b) NUDGERL introduces Strategy Nudging, which appends lightweight
strategy to the input, forcing the model to traverse diverse reasoning modes. (c) As a result, Strategy
Nudging significantly increases the number of distinct reasoning approaches discovered compared to
the baseline, effectively mitigating the exploration bottleneck. Additional details are in Sec. B
line of work leveragesprivileged information, such as oracle solutions or intermediate reasoning
steps, to improve the feasibility of discovering correct trajectories [8, 16, 19, 27]. Although effective,
these approaches are primarily feasibility-oriented and rely on strong supervision signals that are
expensive to obtain and difficult to scale. Moreover, by guiding the policy toward a narrow set of
predefined successful trajectories, they may limit exploration diversity and hinder the discovery of
alternative reasoning strategies [23, 25].
In this work, we address the exploration bottleneck by explicitly structuring the reasoning space in a
scalable manner. We propose NUDGERL, a framework that introducesStrategy Nudgingduring the
exploration phase. Instead of relying on expensive oracle data, Strategy Nudging appends lightweight,
heuristic text prompts (e.g., specific strategies for math problems or reasoning keywords) to the input.
This deliberately forces the model to traverse distinct, diverse reasoning modes that it might otherwise
ignore under purely naive sampling.
However, learning from such context-conditioned exploration introduces new challenges. Since
rollouts are generated under different context-conditioned prompts, the samples are naturally par-
titioned into multiple distinct groups, where reward variation reflects both the intrinsic trajectory
quality and context-specific biases, making standard group-wise advantage estimation unreliable.
Furthermore, context forcing creates a mismatch between how trajectories are sampled and how
the policy is finally used at inference time. Without intervention, improvements discovered under
context-forced exploration may not transfer directly to the base policy. To address these challenges,
we further introduce (i) anInter-Intra group advantageto enable meaningful credit assignment across
context-induced groups, and (ii) adistillation-augmented objectivethat explicitly transfers effective
behaviors discovered during context-forced exploration back to the base policy.
Our approach enables structured and diversity-driven exploration while remaining fully compatible
with standard RLVR pipelines. Empirically, NUDGERL achieves performance surpassing GRPO
even when GRPO is given an 8× larger rollout budget, while outperforming oracle-guided baselines.
This demonstrates that scalable, diversity-oriented exploration can serve as an effective alternative to
both brute-force rollout scaling and feasibility-driven privileged information.
2 Preliminaries
2.1 Group-Relative Policy Optimization (GRPO)
We consider an empirical distribution of prompts x0 ∈ D. For each prompt x0, a policy πθ generates
a group of N rollouts {yi}N
i=1, where each rollout is sampled as yi ∼π θ(· |x0). Each rollout is
evaluated by a verifiable reward functionR(x 0, yi)∈ {0,1}.
Unlike standard PPO [ 17], which typically estimates advantages using a learned value function,
GRPO [18] derives advantages from group-wise rewards. For rollouts sampled from the same prompt
x0, letr i =R(x 0, yi)denote the reward of rollouty i. The group-wise advantage is then defined as:
ˆAi = ri −µ
σ+δ ,(1)
2

## Page 3

where µ and σ are the reward mean and standard deviation within the group, and δ >0 is used for
numerical stability. This yields a relative advantage estimate without training a value function.
The policy is then optimized with a PPO-style clipped objective:
LGRPO(θ) =−E y∼πθ(·|x0)
h
min
 
r0 ˆA,clip(r 0,1−ϵ,1 +ϵ) ˆA
i
,wherer 0 = πθ(y|x0)
πold(y|x0).(2)
Thus, GRPO retains PPO’s clipped objective while using group-relative advantages.
2.2 Motivation: From Exploration to Performance Gain
To understand why exploration is a fundamental bottleneck in RLVR, we look beyond trajectory-level
rewards and examine how the probability mass of generated tokens shifts during training. Hu et al.
[5] characterizes the expected one-step performance improvement (∆Qpos) in RLVR as:
∆Qpos = η
N

(1−S R)QnegA2 +S RQposB2 +S R(QposUneg,2 −Q negUpos,2)

,(3)
where Qpos and Qneg = 1−Q pos denote the total probability mass of correct and incorrect tokens, η
is the learning rate, and N is the number of rollouts. A2 and B2 are the second moments ofsampled
correct and incorrect tokens, while Upos,2 and Uneg,2 are those ofunsampledcorrect and incorrect
tokens.S R ∈[0,1]represents the net reward contribution from sampled tokens.
Since SR ∈[0,1] , the first two terms in Eq. 3 are non-negative and drive learning forward. The third
term, however, acts as a potential penalty. Because incorrect tokens typically dominate the probability
mass (Qneg ≫Q pos), a large Upos,2, meaning the model has significant probability mass on correct
trajectories that it simplyfails to explore, creates a dominant negative force that hinders performance
gain. Therefore, the core bottleneck of RLVR lies in theunexploredcorrect regions.
Limitations of rollout scaling.To mitigate this penalty, a naive solution is to increase the rollout
size N. Hu et al. [5] shows that for a collection of tokens with probabilities {pi}, the expected
unsampled second moment afterNdraws is:
X
i
p2
i (1−p i)N ,(4)
which decreases monotonically with N. However, tokens with small pi decay slowly, so fully
covering long-tail correct trajectories requires prohibitively large rollout budgets.
This highlights the limitation of blindly scaling N to reduce the unexplored correct mass (Upos,2).
Long-tail correct trajectories remain unlikely to be sampled even under large N, suggesting the need
for astructured explorationmechanism that canefficientlyexpose such latent trajectories.
3 NUDGERL
We introduceNUDGERL, a framework for structured exploration and learning in RLVR. NUDGERL
consists of three components: (i)Strategy Nudging, which conditions rollout generation onstrategy-
levelcontexts to induce diverse reasoning trajectories; and (ii)Inter-intra Group Advantage, a
credit assignment method that enables controlled exploration and exploitation of strategies; and (iii)
Distillation augmented RL objectiveto learn from context-conditioned rollouts and distill effective
strategies into the policy under the original prompt for inference without external context.
3.1 Strategy Nudging: Structured Exploration via Strategy-Level Contexts
Given that prior work [5] alleviates the exploration bottleneck by reducing unsampled probability
mass through larger rollout budgets, a natural question arises:how many rollouts are required to
reliably discover a rare trajectory?To quantify this discovery cost, consider a rare trajectory y with
π(y|x0)≪1. The expected number of rollouts required to observeyat least once is:
E

#rollouts

= 1
π(y|x0).(5)
3

## Page 4

𝜋𝜃
Q + A
Q + B
Rollout 1
Rollout 4LLM
Rollout 2
Rollout 5
𝜋𝜃
LLM
Q + B Rollout 
Q 𝜋𝜃
ℒDistill
(b) Self-distillation
Rollout 3
Rollout 6
(a) Inter-Intra Group Advantage
Correct / Wrong Reward Positive / Negative Advantage/ /
𝑥1
𝑥0
Figure 2:Overview of the NudgeRL learning mechanism. (a) Inter-Intra Group Advantage:
Demonstrates credit assignment that emphasizes reliable contexts (i.e., λ∈(1,2] ). A successful
rollout from a consistently high-reward context (Strategy B) receives a larger positive advantage
than a rare success from a low-reward context (Strategy A).(b) Self-distillation:Illustrates bridging
the train-test gap. High-quality trajectories discovered via context-conditioned exploration (Q+B )
are distilled back into the base policy (Q) using LDistill, allowing the model to internalize effective
reasoning modes for context-free inference.
This implies that for low-probability trajectories, the required rollout budget grows prohibitively
large. In practice, naive rollout scaling repeatedly samples from high-probability modes of the current
policy, leading to diminishing returns in covering rare trajectories.
This motivates conditioning generation on a context c that can shift the sampling distribution to-
ward otherwise rare trajectories. If such a context increases the probability of a trajectory y, i.e.,
π(y|x, c)≫π(y|x), then its expected number of rollouts becomes:
E

#rollouts|c

= 1
π(y|x0, c)≪ 1
π(y|x0).(6)
Thus, contexts need not provide a solution; they can serve as lightweight controls that alter the
sampling distribution and reduce the cost of discovering rare trajectories.
Strategy Nudging.Even though context conditioning can improve exploration efficiency in princi-
ple, simply placing multiple contexts in a single prompt leaves the choice of strategy to the policy,
which may ignore some contexts and repeatedly follow dominant reasoning patterns. To enforce
coverage over contexts, we instead assign a single sampled context to each rollout before generation.
Let C(x0) ={c 1, . . . , cM } denote a pool of Strategy-level contexts for the original prompt x0. For
each rollout index i, we begin with sampling c(i) ∼Uniform(C(x 0)). To avoid relying exclusively
on the context pool and to retain compatibility with the original prompt, we further apply context
dropout. Specifically, we sample a maskb (i) ∼Bernoulli(1−p drop)and define the context as:
z(i) =
c(i), b (i) = 1,
∅, b (i) = 0. (7)
We then construct the final prompt x(i)
1 = (x0, z(i)), and generate yi ∼π θ(· |x(i)
1 ). By varying z(i)
across rollout indices, Strategy Nudging induces diversity at the input-conditioning level, rather than
relying solely on sampling from a single prompt. Details on generatingCare in Sec. B.
Context-induced rollout diversity.To verify that Strategy Nudging induces the intended diversity,
we compare it against naive sampling without context conditioning. For each prompt, both methods
generate 8 rollouts in total: Strategy Nudging samples 4 rollouts from each of 2 contexts without
context dropout, whereas the baseline samples all 8 rollouts from the base policy under the original
prompt. We then cluster the reasoning structures using an LLM-as-a-judge (gpt-4o-mini [15]) and
measure the number of distinct clusters; additional details are provided in Sec. B.
As shown in Fig. 1, Strategy Nudging more often increases the number of distinct reasoning structures
relative to naive sampling, whereas the base policy frequently collapses to similar patterns. This
suggests that Strategy Nudging diversifies exploration before any policy update is applied, allowing
the rollout set to cover a broader range of reasoning modes under the same rollout budget.
3.2 Inter-Intra Group Advantage: Learning to Balance Exploration between Strategies
GRPO estimates advantages by comparing rewards among rollouts conditioned on the same prompt
distribution. With Strategy Nudging, however, rollouts are drawn from context-conditioned prompts
4

## Page 5

(x0, z(i)). A single group baseline therefore entangles reward variation induced by different contexts,
distorting the relative advantage assigned to each rollout.
To address this, we propose theInter-Intra Group Advantage, which assigns credit through two com-
plementary signals: anintra-context signal, capturing trajectory quality under the same conditioning
context, and aninter-context signal, capturing the relative reliability of the context itself.
Given sampled rollouts {yi}N
i=1 with rewards ri =R(x 0, yi), we group them according to their
assigned contexts. The set of context groups is defined as
G(x0) = Unique({z(i)})⊆ C(x0)∪ {∅}.(8)
For each group g∈ G(x0), we define the index set Ig ={i|z (i) =g} , which partitions all rollouts.
We then compute both context-level and global reward baselines:
¯rg = 1
|Ig|
X
i∈Ig
ri,¯r= 1
N
NX
i=1
ri.(9)
Using these baselines, we define the advantage as:
ˆAi = Ai −µ A
σA +δ ,whereA i =
(ri −¯rz(i) ) +λ(¯rz(i) −¯r)ifz (i) ̸=∅,
ri −¯rifz (i) =∅. (10)
µA andσ A are the mean and standard deviation of{A i}, andδ >0ensures numerical stability.
Because advantages determine direction of the policy update, they should remain consistent with the
underlying rewards while allowing context-level preferences to affect credit assignment.
Proposition 3.1.Consider two trajectories y and y′ sampled from context groups z and z′, with
rewards r and r′, respectively. Let ¯rz and ¯rz′ denote the corresponding context means, and let A and
A′ denote their advantages. In the binary reward setting, ifλ∈[0,2], then:
r > r′ ⇒A > A′.(11)
Thus, for λ∈[0,2] , a higher reward always receives a higher advantage, ensuring consistency with
the underlying objective; context only affects the relative ordering among equal-reward trajectories.
For equal-reward trajectories, λ controls the context-level preference: λ <1 favors successes from
lower-reward contexts, encouraging exploration of less typical contexts, whereas λ >1 favors
successes from higher-reward contexts, emphasizing more reliable contexts. The neutral case λ= 1
treats equal-reward trajectories identically across contexts; theλ >1case is illustrated in Fig. 2 (a).
3.3 Training objective
Although Strategy Nudging improves exploration by sampling rollouts from context-conditioned
prompts x1 = (x0, z), the target policy at inference time should operate without external contexts.
Therefore, useful trajectories discovered underx 1 must be transferred to the base policyπ θ(· |x0).
To bridge this gap, we introduce an advantage-weighted distillation term following Song et al.[19],
which directly updates the policy using trajectories sampled under the context-conditioned input x1:
LDistill(θ) =−E y∼πθ(·|x1)
 ˆAlogπ θ(y|x0)

.(12)
Unlike standard behavior cloning, this formulation selectively emphasizes trajectories with high nor-
malized advantage, ensuring that only useful behaviors discovered under diverse contexts contribute
to the update ofπ θ(· |x0).
In parallel, we optimize the reinforcement learning objective on thecontext-conditioned policy:
LRL(θ) =−E y∼πθ(·|x1)

min(r1 ˆA,clip(r 1,1−ϵ low,1 +ϵ high) ˆA)

,wherer 1 = πθ(y|x1)
πold(y|x1).(13)
The final objective combines both terms:
LNUDGERL =L RL +λ distillLDistill.(14)
5

## Page 6

Table 1:Main resultscomparing rollout scaling, oracle hinting, and context-based exploration. We
reportpass@1 estimated using 128 rollouts. Best results are represented asboldand second best as
underline.†indicates additional implementation details; see Sec. C for details.
Model Method Rollouts (N) AIME24 AIME25 AMC23 MATH500 APEX Average
Qwen3-4B-
Instruct
Base model – 0.374 0.352 0.653 0.592 0.036 0.402
GRPO
8 0.444 0.367 0.749 0.668 0.040 0.454
16 0.454 0.355 0.840 0.655 0.045 0.470
32 0.451 0.370 0.881 0.674 0.0580.487
64 0.415 0.324 0.848 0.641 0.027 0.451
POPE† [16] 8 0.460 0.337 0.838 0.652 0.048 0.467
NUDGERL 8 0.482 0.393 0.857 0.660 0.053 0.489
Olmo3-7B-
Instruct-SFT
Base model – 0.134 0.118 0.467 0.384 0.021 0.225
GRPO
8 0.187 0.159 0.537 0.434 0.025 0.268
16 0.188 0.176 0.548 0.461 0.023 0.279
320.1950.176 0.553 0.459 0.024 0.281
64 0.081 0.053 0.349 0.2910.0270.160
POPE† [16] 8 0.186 0.169 0.558 0.460 0.023 0.279
NUDGERL 8 0.190 0.179 0.563 0.468 0.025 0.285
This objective induces a complementary learning dynamic. The RL term operates on the context-
conditioned policy, improving exploration and reinforcing successful trajectories within each context.
In contrast, the distillation term projects these improvements onto the base-prompt policy, enabling
cross-context generalization. As a result, the model learns to reproduce effective reasoning strategies
without relying on explicit context at inference time. Unlike GRPO in Eq. 2, which samples and
optimizes trajectories under the original prompt x0, NUDGERL performs RL on context-conditioned
rollouts underx 1 while distilling high-advantage trajectories back into the base policyπ θ(·|x0).
4 Experiments
4.1 Experimental Setup
Baselines.We compare our method against (i) the base model without optimization, which serves
as the reference point; (ii) GRPO with increasing rollout budgets, where N∈ {8,16,32,64}, which
evaluates naive rollout scaling as a brute-force exploration strategy; and (iii) POPE [ 16], which
augments standard GRPO by appending prefixes of the oracle solution at the end of the base prompt,
thereby alleviating the sparse reward signal bottleneck. Further details are provided in Sec. C.
Evaluation Datasets and Metrics. AIME24 and AIME25, 30-problem olympiad-style high-school
competitions [13]; AMC23, a 40-problem high-school contest benchmark [12]; the level-5 subset of
MATH500, containing 134 difficult MATH problems [4]; and the Apex Shortlist, consisting of 48
advanced competition-style problems [1]. We reportpass@1, estimated from 128 rollouts using the
unbiased estimator of Chen et al. [2]. All solutions are automatically graded using math-verify [6].
Additional details are provided in Sec. E.
Implementation Details.We apply NUDGERL to Qwen3-4B-Instruct-2507 [21] and
Olmo-3-7B-Instruct-SFT [14] using DAPO-17k-Processed as a training set [24]. To construct
the pool of contexts, we used gpt-4o-mini [15] to generate two strategy-level contexts per problem
(e.g., Pythagorean theorem), and used them without additional verification (i.e., ∀x∈ D,|C(x)|= 2).
For the POPE baseline, oracle solutions were generated using DeepSeek Reasoner v3.2 [9]. We
provide additional optimization details in Sec. D.
4.2 Main Results
NudgeRL matches larger-budget GRPO with fewer rollouts.As shown in Tab. 1, NUDGERL
achieves the best average performance on both models while using only 8 rollouts per prompt. On
Qwen3-4B-Instruct-2507, NUDGERL reaches 0.489 average pass@1, slightly outperforming the
best GRPO result at 32 rollouts (0.487) and surpassing GRPO at 64 rollouts (0.451) with an 8 ×
6

## Page 7

100 200 300 400 500
Step
0.3
0.4
0.5
0.6Reward GRPO-8
GRPO-16
GRPO-32
GRPO-64
NudgeRL
(a) Training reward
100 200 300 400 500
Step
0.36
0.38
0.40
0.42Average pass@1
GRPO-8
GRPO-16
GRPO-32
NudgeRL (b)AIME24/25pass@1
1 4 16 64 256 1024
k
0.4
0.5
0.6
0.7
0.8
0.9pass@k
Base model
GRPO-8
GRPO-16
NudgeRL (c)AIME24/25pass@k
Figure 3:Training dynamics and evaluation performanceon Qwen3-4B-Instruct. (a) EMA-
smoothed training reward with decay factor 0.99. (b, c) Averagepass@1andpass@kon AIME24/25,
estimated from 64 sampled rollouts using the unbiased estimator.
smaller rollout budget. OnOlmo3-7B-Instruct-SFT, NUDGERL likewise improves over the best
GRPO result, achieving 0.285 compared to 0.281 at 32 rollouts. These results indicate that larger
rollout budgets alone are not sufficient: GRPO improves up to N= 32 but degrades at N= 64 on
both models, suggesting instability under brute-force rollout scaling. In contrast, NUDGERL achieves
stronger performance by improving the quality of exploration through Strategy Nudging, rather than
relying on more sampled rollouts.
Comparison with oracle-prefix method.We also compare with POPE [ 16], which augments
GRPO by generating rollouts conditioned on the oracle solution prefixes. Unlike baselines relying on
expensive, unscalable oracle hints [16] or text feedback [19], our approach ensures scalable diversity.
We use a lightweight LLM (e.g.,gpt-4o-mini) to cheaply generate unverified strategy-level contexts
that induce multiple reasoning directions. Despite this weaker supervision, our method consistently
outperforms oracle-guided baselines, demonstrating that structured exploration over diverse strategies
is more effective than injecting narrow, privileged solution signals.
4.3 Efficient Coverage of Diverse Reasoning Modes
As discussed in Sec. 3.1, relying solely on scaling the rollout budget suffers from severe sample
inefficiency when discovering long-tail, low-probability reasoning modes. This is because naive
rollout scaling repeatedly allocates computation to dominant trajectories. To empirically investigate
how Strategy Nudging overcomes this exploration bottleneck and improves sample efficiency, we
compare the training dynamics of NUDGERL against GRPO under progressively larger rollout
budgets. We evaluate the model for every 50 training steps on the combined AIME24 and AIME25
benchmark by sampling 64 rollouts per problem and estimatingpass@1 andpass@8.
As shown in Fig. 3b, NUDGERL improves pass@1 faster than GRPO variants and remains the
strongest method throughout most of training. By 200 steps, NUDGERL exceeds 0.42 pass@1 on
AIME24/25, while GRPO variants remain around or below 0.41 and show slower or less stable gains
as the rollout budget increases. This suggests that Strategy Nudging improves sample efficiency
by exposing useful reasoning trajectories earlier, rather than merely increasing sampled rollouts.
Enlarging the number of samples ( k) further validates this trend under the same training rollout
budget. As shown in Fig. 3c, NUDGERL consistently outperforms GRPO-8 across the full k range,
which indicates that Strategy Nudging improves inference-time sample efficiency, requiring fewer
generated solutions to reach the same level ofpass@k.
4.4 Case Study
To examine the source of performance gains in NUDGERL, we analyze one AIME25 problem where
the NUDGERL-trained model successfully sampled correct trajectories, while the GRPO-trained
model entirely failed. We sampled 32 rollouts and categorized their dominant reasoning strategies.
As shown in Fig. 4, both models predominantly relied oncoordinate geometry. However, the GRPO-
trained model additionally explored ineffective strategies such assymmetry assumptionsandarea
decomposition, which consistently resulted in truncated solutions, causing all 32 trajectories to fail.
While GRPO sampled theshoelace formulastrategy only once, NUDGERL substantially increased
its frequency and successfully exploited it to generate correct trajectories.
7

## Page 8

13
5
4
5
4
32/32
Truncated
& wrong
GRPO
15
5
4
6
Correct
Shoelace
6/10
6/32
Correct
NudgeRL
Strategy / outcome
coordinate geometry
trigonometry
symmetry assumption
area decomposition
vector/equilateral geometry
shoelace formula
Truncated & wrong
Correct Shoelace
Figure 4:NUDGERL internalizes effective test-time strategies.Across 32 rollouts on a AIME25
problem, GRPO yields only incorrect and truncated trajectories. Conversely, NUDGERL produces 6
correct solutions using the shoelace formula.
100 200 300 400 500
Step
0.3
0.4
0.5
0.6Context Reward
Hinted Reward
Dropout Reward
Figure 5: Training dynamics. We
report time-weighted EMA re-
ward mean (0.99) with and with-
out context.
0.00 0.25 0.50 0.75
pdrop
0.54
0.56
0.58
0.60Average pass@1
NudgeRL
(a) Ablation onp drop
Random T op ranked
Hint sampling
0.56
0.58
0.60Average pass@1
NudgeRL (b) Ablation on sampling
Figure 6: Ablation results on sampling. We report Average
pass@1 estimated using 128 rollouts on AIME24/25, AMC23,
MATH500.
This behavior highlights the complementary roles of our framework:Strategy Nudgingexposes rare
but effective reasoning modes such as the shoelace-formula strategy, while theInter-Intra Group
Advantagereinforces and exploits such reliable strategies once discovered. Details are in Sec. F.
4.5 Effect of Contexts during training
We also report the dropout reward mean ( Ei[r(x0, y(i))|z (i) =∅] ) and the hinted reward mean
(Ei[r(x0, y(i))|z (i) ̸=∅] ) during training of Qwen3-4B-Instruct-2507 with NUDGERL. As
shown in Fig. 5, both rewards improve together throughout training, suggesting that trajectories
discovered under context-conditioned exploration are successfully transferred to the base policy
through the distillation objective. Interestingly, the dropout reward occasionally exceeds the hinted
reward during training. This contrasts with prior feasibility-oriented methods based on privileged
information [8, 16, 19, 27]. In ours, primary role of context is not to directly simplify the problem,
but to induce diverse reasoning trajectories that can later be internalized by the context-free policy.
4.6 Underlying Mechanism of NUDGERL
To further understand the source of performance gains in NUDGERL, we conduct a series of controlled
experiments usingQwen3-4B-Instruct-2507[21] on a subset of benchmarks.
pdrop Ablation.As shown in Fig. 6a, a moderate dropout rate ( pdrop = 0.5) consistently yields
the best performance across benchmarks. Context dropout plays a dual role: it enables exploration
beyond fixed contexts by occasionally reverting to the base prompt, while also stabilizing group-wise
statistics through a more balanced sample distribution. When pdrop = 0, exploration is restricted to
predefined contexts, whereas large values diminish the influence of context forcing. These results
suggest that maintaining a balanced mixture of context-conditioned and context-free samples is
important for achieving both diverse exploration and stable optimization.
Hint Sampling.We study how the quality of sampled contexts affects performance by comparing
two strategies:randomsampling andtop-rankedselection. In the top-ranked setting, we first generate
a pool of five candidate contexts, and then select the two that yield the largest improvement in
pass@16for each problem, as measured by oracle evaluation.
8

## Page 9

0.9 1.0 1.1
0.56
0.58
0.60Average pass@1
NudgeRL
(a) Ablation results onλ
0.0 0.1 0.5
distill
0.54
0.56
0.58
0.60Average pass@1
NudgeRL (b) Ablation results onλ distill
0.20 0.24 0.28 0.32 0.36 0.40
high
0.54
0.56
0.58
0.60Average pass@1
NudgeRL ( high=0.20)
GRPO (c)ϵ high scaling results
Figure 7: Ablation on learning and ϵhigh scaling results. We report Averagepass@1 estimated using
128 rollouts onAIME24/25,AMC23,MATH500dataset.
As shown in Fig. 6b, random sampling consistently outperforms top-ranked selection in terms of
pass@1. While top-ranked contexts ensure more correctness, they tend to concentrate on a narrow
set of reasoning strategies. In contrast, random sampling induces a broader distribution over plausible
trajectories, resulting in more effective exploration under limited rollout budgets.
These results suggest that, within our framework, the primary role of context is not to provide the
single best hint, but to promote diversity in reasoning. Consequently, simple random sampling is not
only sufficient, but also preferable for scalable and effective context-based exploration.
Exploration-Exploitation trade-off via λ.Fig. 7a presents the effect of varying λ, where λ= 1.1
achieves the best performance. This trend aligns with our Proposition 3.1 in Sec. 3.2. Since strategy
nudging already ensures sufficient diversity at the sampling stage, increasing λ does not hinder
exploration across contexts. Instead, it strengthens exploitation within each problem by prioritizing
trajectories from more reliable contexts. This leads to more consistent learning of high-quality
solutions per instance, explaining the observed performance gains atλ= 1.1.
Distillation Coefficient.As shown in Fig. 7b, removing the distillation term ( λdistill = 0) results
in a clear performance drop, indicating that explicitly transferring context-discovered trajectories
to the base policy is essential. However, overly large values also degrade performance, likely due
to over-constraining the policy toward sampled trajectories. A moderate coefficient (λdistill = 0.1)
achieves the best results, suggesting that distillation should complement the underlying RL objective.
4.7 Comparison withϵ high scaling.
We further compare our algorithm with decoupled clipping [24]: clip(r,1−ϵ low,1 +ϵ high), where
ϵhigh controls the strength of policy updates by amplifying the contribution of successful trajectories.
Increasing ϵhigh therefore allows more aggressive policy updates toward positive-advantage trajectories.
As shown in Fig. 7c, increasing ϵhigh generally improves GRPO performance in the moderate regime
used in prior works [18, 24]. However, our method with ϵhigh = 0.2 consistently outperforms GRPO
across the entire scaling range from moderate to extreme values. This suggests that improving
exploration quality is more effective than simply increasing the magnitude of stochastic policy
updates. Additionally, under the more extreme scaling adopted in recent RLVR settings [10], GRPO
sharply deteriorates at ϵhigh = 0.4. We argue that this degradation highlights a limitation of purely
stochastic distribution-level exploration: increasing update magnitude alone provides little control
overwhatis explored.
The complete results of the evaluation are given in the Sec. G.
5 Conclusion
In this work, we introduced NUDGERL, a framework for structured exploration in RLVR. Our
approach leveragesStrategy Nudgingto induce diverse reasoning trajectories by sampling from
lightweight, strategy-level context-conditioned distributions, and learns from them via distillation
augmented RL objective. Empirically, NUDGERL achieves superior performance compared to GRPO
using up to 8× larger rollout budgets, and further outperforms oracle prefix-based baselines across
models.
9

## Page 10

Limitations & Future WorkA practical consideration of NUDGERL is the cost of generating
strategy-level contexts. However, this is anofflineprocess performed once prior to training, using
a lightweight LLM (e.g., gpt-4o-mini), and the resulting contexts can be reused across training
runs without additional overhead. A more fundamental limitation lies in how contexts are generated
independently of the model being trained. The benefit of Context Forcing stems from inducing
trajectories that are unlikely under the current policy. As training progresses, however, a fixed context
pool may become less informative as the policy adapts. A promising direction for future work is
model-adaptive context generation, which dynamically constructs contexts tailored to the current
policy’s blind spots, potentially yielding more consistent exploration gains throughout training.
References
[1] Mislav Balunovi ´c, Jasper Dekoninck, Ivo Petrov, Nikola Jovanovi ´c, and Martin Vechev.
Matharena: Evaluating llms on uncontaminated math competitions, February 2025. URL
https://matharena.ai/.
[2] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde De Oliveira Pinto, Jared
Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. Evaluating large
language models trained on code.arXiv preprint arXiv:2107.03374, 2021.
[3] Jia Deng, Jie Chen, Zhipeng Chen, Wayne Xin Zhao, and Ji-Rong Wen. Decomposing the
entropy-performance exchange: The missing keys to unlocking effective reinforcement learning.
arXiv preprint arXiv:2508.02260, 2025.
[4] Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Dawn Song, and Jacob Steinhardt.
Measuring mathematical problem solving with the math dataset.NeurIPS, 2021.
[5] Jian Hu, Mingjie Liu, Ximing Lu, Fang Wu, Zaid Harchaoui, Shizhe Diao, Yejin Choi, Pavlo
Molchanov, Jun Yang, Jan Kautz, et al. Brorl: Scaling reinforcement learning via broadened
exploration.arXiv preprint arXiv:2510.01180, 2025.
[6] HuggingFace. Math-verify: A toolkit for verifying mathematical reasoning. https://github.
com/huggingface/Math-Verify, 2024. Accessed 2026-05-06.
[7] Nathan Lambert, Jacob Morrison, Valentina Pyatkin, Shengyi Huang, Hamish Ivison, Faeze
Brahman, Lester James V Miranda, Alisa Liu, Nouha Dziri, Shane Lyu, et al. Tulu 3: Pushing
frontiers in open language model post-training.arXiv preprint arXiv:2411.15124, 2024.
[8] Baohao Liao, Hanze Dong, Xinxing Xu, Christof Monz, and Jiang Bian. Self-hinting language
models enhance reinforcement learning.arXiv preprint arXiv:2602.03143, 2026.
[9] Aixin Liu, Aoxue Mei, Bangcai Lin, Bing Xue, Bingxuan Wang, Bingzheng Xu, Bochao Wu,
Bowei Zhang, Chaofan Lin, Chen Dong, et al. Deepseek-v3. 2: Pushing the frontier of open
large language models.arXiv preprint arXiv:2512.02556, 2025.
[10] Mingjie Liu, Shizhe Diao, Ximing Lu, Jian Hu, Xin Dong, Yejin Choi, Jan Kautz, and Yi Dong.
Prorl: Prolonged reinforcement learning expands reasoning boundaries in large language models.
arXiv preprint arXiv:2505.24864, 2025.
[11] Zichen Liu, Changyu Chen, Wenjun Li, Penghui Qi, Tianyu Pang, Chao Du, Wee Sun Lee, and
Min Lin. Understanding r1-zero-like training: A critical perspective.arXiv, 2503.20783, 2025.
URLhttps://doi.org/10.48550/arXiv.2503.20783.
[12] Mathematical Association of America. American mathematics competitions. https://www.
maa.org/math-competitions, 2023.
[13] Mathematical Association of America. Aime: American invitational mathematics examination.
https://www.maa.org/math-competitions, 2025.
[14] Team Olmo, Allyson Ettinger, Amanda Bertsch, Bailey Kuehl, David Graham, David Heineman,
Dirk Groeneveld, Faeze Brahman, Finbarr Timbers, Hamish Ivison, Jacob Morrison, Jake
Poznanski, Kyle Lo, Luca Soldaini, Matt Jordan, Mayee Chen, Michael Noukhovitch, Nathan
Lambert, Pete Walsh, Pradeep Dasigi, Robert Berry, Saumya Malik, Saurabh Shah, Scott
10

## Page 11

Geng, Shane Arora, Shashank Gupta, Taira Anderson, Teng Xiao, Tyler Murray, Tyler Romero,
Victoria Graf, Akari Asai, Akshita Bhagia, Alexander Wettig, Alisa Liu, Aman Rangapur, Chloe
Anastasiades, Costa Huang, Dustin Schwenk, Harsh Trivedi, Ian Magnusson, Jaron Lochner,
Jiacheng Liu, Lester James V . Miranda, Maarten Sap, Malia Morgan, Michael Schmitz, Michal
Guerquin, Michael Wilson, Regan Huff, Ronan Le Bras, Rui Xin, Rulin Shao, Sam Skjonsberg,
Shannon Zejiang Shen, Shuyue Stella Li, Tucker Wilde, Valentina Pyatkin, Will Merrill,
Yapei Chang, Yuling Gu, Zhiyuan Zeng, Ashish Sabharwal, Luke Zettlemoyer, Pang Wei
Koh, Ali Farhadi, Noah A. Smith, and Hannaneh Hajishirzi. Olmo 3, 2025. URL https:
//arxiv.org/abs/2512.13961.
[15] OpenAI. Gpt-4o mini. https://openai.com/ko-KR/index/
gpt-4o-mini-advancing-cost-efficient-intelligence/ , 2024. Accessed: 2026-05-
04.
[16] Yuxiao Qu, Amrith Setlur, Virginia Smith, Ruslan Salakhutdinov, and Aviral Kumar. Pope:
Learning to reason on hard problems via privileged on-policy exploration.arXiv preprint
arXiv:2601.18779, 2026.
[17] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal
policy optimization algorithms.arXiv preprint arXiv:1707.06347, 2017.
[18] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Mingchuan Zhang, Y . K.
Li, Y . Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in
open language models.arXiv, 2402.03300, 2024. URL https://doi.org/10.48550/arXiv.
2402.03300.
[19] Yuda Song, Lili Chen, Fahim Tajwar, Remi Munos, Deepak Pathak, J Andrew Bagnell, Aarti
Singh, and Andrea Zanette. Expanding the capabilities of reinforcement learning via text
feedback.arXiv preprint arXiv:2602.02482, 2026.
[20] Kimi Team, Angang Du, Bofei Gao, Bowei Xing, Changjiu Jiang, Cheng Chen, Cheng Li,
Chenjun Xiao, Chenzhuang Du, Chonghua Liao, et al. Kimi k1. 5: Scaling reinforcement
learning with llms.arXiv preprint arXiv:2501.12599, 2025.
[21] Qwen Team. Qwen3 technical report, 2025. URLhttps://arxiv.org/abs/2505.09388.
[22] Leandro von Werra, Younes Belkada, Lewis Tunstall, Edward Beeching, Tristan Thrush, Nathan
Lambert, Shengyi Huang, Kashif Rasul, and Quentin Gallouédec. TRL: Transformers Rein-
forcement Learning, 2020. URLhttps://github.com/huggingface/trl.
[23] Fang Wu, Weihao Xuan, Ximing Lu, Zaïd Harchaoui, and Yejin Choi. The invisible leash:
Why RLVR may not escape its origin.arXiv, 2507.14843, 2025. URL https://doi.org/10.
48550/arXiv.2507.14843.
[24] Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Tiantian Fan,
Gaohong Liu, Lingjun Liu, Xin Liu, Haibin Lin, Zhiqi Lin, Bole Ma, Guangming Sheng, Yuxuan
Tong, Chi Zhang, Mofan Zhang, Wang Zhang, Hang Zhu, Jinhua Zhu, Jiaze Chen, Jiangjie
Chen, Chengyi Wang, Hongli Yu, Weinan Dai, Yuxuan Song, Xiangpeng Wei, Hao Zhou,
Jingjing Liu, Wei-Ying Ma, Ya-Qin Zhang, Lin Yan, Mu Qiao, Yonghui Wu, and Mingxuan
Wang. DAPO: an open-source LLM reinforcement learning system at scale.arXiv, 2503.14476,
2025. URLhttps://doi.org/10.48550/arXiv.2503.14476.
[25] Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, and Gao
Huang. Does reinforcement learning really incentivize reasoning capacity in llms beyond the
base model?arXiv, 2504.13837, 2025. URL https://doi.org/10.48550/arXiv.2504.
13837.
[26] Xiaoyun Zhang, Xiaojian Yuan, Di Huang, Wang You, Chen Hu, Jingqing Ruan, Kejiang Chen,
and Xing Hu. Rediscovering entropy regularization: Adaptive coefficient unlocks its potential
for llm reinforcement learning.arXiv preprint arXiv:2510.10959, 2025.
[27] Xuechen Zhang, Zijian Huang, Yingcong Li, Chenshun Ni, Jiasi Chen, and Samet Oymak.
Bread: Branched rollouts from expert anchors bridge sft & rl for reasoning.arXiv preprint
arXiv:2506.17211, 2025.
11

## Page 12

A Related Work
A.1 Reinforcement Learning with Verifiable Rewards
Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a scalable paradigm for
improving the reasoning abilities of large language models[9, 18, 20, 24]. By leveraging automatically
verifiable signals, such as exact answers in mathematics or test-case correctness in code generation,
RLVR enables effective policy optimization without dense human supervision.
A representative approach isGroup-Relative Policy Optimization(GRPO) [ 18], which replaces value
function estimation with group-wise comparisons among sampled rollouts, deriving advantages from
relative reward differences within each group. Building on this formulation, subsequent work has
introduced improvements such as decoupled clipping [24] and alternative normalization strategies [11]
to enhance training stability.
These methods have been successfully applied across a range of reasoning tasks and model scales [9,
10], establishing RLVR as a standard post-training approach for LLMs. However, their effectiveness
fundamentally depends on exploration: the policy can only improve on trajectories it has already
sampled. As a result, insufficient exploration directly limits learning, making it a key bottleneck in
RLVR. We next examine how prior work addresses this challenge.
A.2 Exploration in RLVR
A straightforward approach to improving exploration is to scale the number of sampled rollouts. Prior
work has shown that such rollout scaling can significantly improve performance by reducing the
probability mass of un-sampled region[5]. However, this approach is computationally expensive and
often impractical at scale.
More commonly, recent methods attempt to encourage exploration through objective design, such
as entropy regularization [3, 26] or decoupled clipping [24]. While these approaches can steer the
update toward exploration, they do not guarantee that useful or rare modes are actually sampled
during training. In other words, shaping the distribution does not necessarily ensure coverage of
meaningful trajectories, leaving exploration fundamentally limited.
Moreover, such distribution-level exploration is inherently stochastic and unconstrained, which
can perturb the policy in semantically undesirable directions. Increasing entropy or aggressively
reweighting probabilities may encourage the model to explore low-probability regions, but without any
structural guidance, this often leads to incoherent or unproductive trajectories rather than meaningful
reasoning strategies. As a result, these approaches lack control overhowthe policy explores, and fail
to provide structured, strategy-level exploration that targets diverse and semantically valid modes of
reasoning.
A.3 Usage of Privileged Information
Another key limitation of widely used group-based advantage methods, such as GRPO [18], is that
they rely on relative comparisons within a group of rollouts. When all samples in a group are either
correct or incorrect, these methods fail to provide informative learning signals.
To address this issue, recent works have introduced privileged information to assist the policy [8, 16,
19, 27], often in the form of oracle prefixes or intermediate solutions. These approaches improve the
feasibility of solving hard problems by enabling the model to generate successful trajectories that
would otherwise be unreachable.
However, such methods come with several limitations. First, privileged information is often difficult
to scale, especially when it relies on oracle solutions or expensive annotations [16, 27]. Second, the
mechanism by which the model internalizes this information and performs well without it at test time
remains unclear [8]. Third, many approaches assume multi-turn or interactive settings [19], which
may not align with standard single-turn RLVR setups.
More importantly, existing work primarily focuses on improving the feasibility of generating correct
trajectories on difficult problems. In contrast, our work targets a complementary challenge: improving
the diversity of exploration, even when successful trajectories are already attainable.
12

## Page 13

B Details on Strategy Nudging
Strategy Generating Prompt.We use gpt-4o-mini to generate keyword-level hints for each
problem. For the main experiments, we generate two hints per problem, while in the top-ranked
setting, we first generate five candidate hints and select a subset based on oracle evaluation.
The exact prompt used for hint generation is as follows:
f"""Given the following math problem, generate {num_hints} different keyword hints
that would help solve it.
Each hint should be a specific mathematical concept, theorem, or technique (e.g.,
"Ceva’s theorem", "Lifting the exponents", "Triangle inequality").
Problem:
{problem}
Please provide exactly {num_hints} hints in the following format (one hint per
line, numbered):
1. [Hint 1]
2. [Hint 2]
...
{num_hints}. [Hint {num_hints}]
Make sure each hint is a distinct mathematical concept or theorem."""
Strategy Nudging prompt.Given a problem and an optional hint, we construct prompts that
encourage the model to follow a specific reasoning strategy. The model is instructed to explicitly
separate its reasoning process and final answer using predefined delimiters.
reasoning_start = "<start_working_out>"
reasoning_end = "<end_working_out>"
solution_start = "<SOLUTION>"
solution_end = "</SOLUTION>"
system_prompt = f"""You are given a problem.
Think about the problem and provide your working out.
Place it between {reasoning_start} and {reasoning_end}.
Then, provide your solution between {solution_start}{solution_end}"""
def build_messages(problem: str, system_prompt: str, hint: str | None = None)
-> list[dict[str, str]]:
context_block = ""
if hint:
context_block = (
"Context (exploration condition):\n"
f"- Use this hint/approach: {hint}\n\n"
"Important:\n"
"- Follow this approach as your primary strategy.\n\n"
)
user_content = (
"Problem:\n"
f"{problem}\n\n"
f"{context_block}"
"Solve this step by step and provide your final numerical answer at the
end."
)
return [
{"role": "system", "content": system_prompt},
{"role": "user", "content": user_content},
]
13

## Page 14

Effect of Strategy Nudging.To evaluate the effect of Strategy Nudging, we sample 8 rollouts from
Qwen3-4B-Instruct-2507 [21] on 200 problems from DAPO-17k-Processed [24], both with and
without Strategy Nudging, and analyze the resulting rollout diversity via LLM-as-a-judge.
LLM-as-a-judge prompt.To analyze the diversity of generated rollouts, we employ an LLM-
as-a-judge using gpt-4o-mini to cluster solutions based on their underlying reasoning strategies
and count the number of distinct solution modes. Given a problem and a set of rollouts, the model
is instructed to identify the number ofconceptually distinctsolution approaches, while ignoring
superficial differences such as phrasing or minor computational variations.
prompt = (f"Problem:\n{problem_text}\n\n"
f"Here are {len(rollouts)} student solutions to this problem:\n"
f"{formatted_rollouts}\n"
f"Analyze these solutions and determine how many *conceptually
distinct* solution strategies are used across them.\n"
f"Ignore minor calculation differences or phrasing variations. Focus
on the core mathematical approach.\n"
f"Provide the answer in the following format: ’Distinct Strategies: X’
where X is the integer count.\n"
f"Then briefly list the distinct strategies identified.")
messages = [
{"role": "system", "content": "You are an expert math teacher evaluating
the diversity of student solution methods."},
{"role": "user", "content": prompt}
]
C Details on Baselines
Rollout Scaling in GRPO.For controlled experiments, we scale the number of rollouts per prompt
while adjusting the gradient accumulation steps and generation batch size accordingly, as summarized
in Tab. 2. This ensures that the total optimization dynamics remain comparable across different
rollout settings.
Implementing POPE [ 16].To compare our method with oracle prefix-based approaches, we
implement our own version of POPE [ 16]. We follow the original paper in using the same prompt
format and dataset mixture (i.e., with and without privileged information). Since the length of oracle
solutions varies across prior works [16, 27], we standardize this by truncating the oracle solution to
15%of its full length when used as a prefix.
Example of Generated Contexts.We provide an illustrative example of the strategy-level contexts
used in our method. These contexts are lightweight, keyword-level hints that do not directly solve
the problem, but instead steer the model toward distinct reasoning modes. Importantly, they are not
intended to provide intermediate steps or solutions, but rather to act as high-level inductive biases
that diversify exploration.
Problem
LetSbe the set of triples(a, b, c)of non-negative integers such thata+b+cis even. The value of the sum
X
(a,b,c)∈S
1
2a3b5c
can be expressed as m
n , wheremandnare relatively prime positive integers. Computem+n.
Oracle solution:
14

## Page 15

We compute the sum X
(a,b,c)∈S
1
2a3b5c ,
whereSconsists of non-negative integer triples(a, b, c)witha+b+ceven. Using the indicator
1a+b+ceven = 1
2

1 + (−1)a+b+c

,
we write
X
(a,b,c)∈S
1
2a3b5c = 1
2

 X
a,b,c≥0
1
2a3b5c +
X
a,b,c≥0
(−1)a+b+c
2a3b5c

.
The first sum factors as
X
a≥0
1
2a ·
X
b≥0
1
3b ·
X
c≥0
1
5c = 1
1− 1
2
· 1
1− 1
3
· 1
1− 1
5
= 2· 3
2 · 5
4 = 15
4 .
The second sum factors as
X
a≥0
(−1)a
2a ·
X
b≥0
(−1)b
3b ·
X
c≥0
(−1)c
5c = 1
1 +1
2
· 1
1 +1
3
· 1
1 +1
5
= 2
3 · 3
4 · 5
6 = 5
12.
Thus, the total sum is
1
2
15
4 + 5
12

= 1
2 · 50
12 = 25
12.
Since 25
12 is in lowest terms, we havem= 25,n= 12, andm+n= 37.
Strategy-level contexts(ours):
"Generating functions", "Parity of sums"
D Training Detail
Framework.We used TRL [22] for implementing baselines and our algorithm.
Hyperparameters.The hyperparameters we used in training are given in Tab. 2.
Compute resources.For all experiments, we used NVIDIA H200 140GB GPUs.
E Details on Evaluation
During evaluation, all hyperparameters are kept identical to Tab. 2, except for the temperature, which
is set to0.7.
F Details on Case study
In this section, we provide qualitative examples from the case study presented in Fig. 4.
The GRPO-trained model predominantly relied on coordinate geometry combined with heuristic
symmetry assumptions and case-by-case area decomposition. Although these approaches occasionally
progressed toward partial solutions, they frequently resulted in excessively long derivations and
truncated outputs before reaching the final answer.
In contrast, NUDGERL exploited theshoelace-formulastrategy, which directly computes polygon
areas from vertex coordinates. This strategy produced substantially shorter and more reliable
reasoning trajectories, enabling successful completion within the generation budget.
15

## Page 16

Table 2: Hyperparameters for training.
Parameter Value
LoRA rank 32
Max prompt length 2,048
Max completion length 6,144
RL steps 500
Batch size 4
Rollouts per promptN
Gradient accumulation steps N
8
Generation batch sizeN
Temperature 1
Min-p0.0
Top-p0.95
Top-k−1
Learning rate2×10 −5
LR scheduler cosine
Weight decay 0.001
Warmup ratio 0.05
Optimizer AdamW (8-bit)
KL coefficientβ0
Epsilon low 0.2
Epsilon high 0.2 (unless specified)
λ1.1
λdistill 0.1
pdrop 0.5
Random seed 42
Problem
Let △ABC be a right triangle with ∠A= 90◦ and BC= 38. There exist points K and L inside the triangle such
that
AK=AL=BK=CL=KL= 14.
The area of the quadrilateralBKLCcan be expressed asn
√
3for some positive integern. Findn.
16

## Page 17

GRPO solution
<start_working_out>
We are given a right triangle△ABC with ∠A= 90◦, and hypotenuse BC= 38. There are two points K and L
inside the triangle such that:
AK=AL=BK=CL=KL= 14
We are to find the area of quadrilateralBKLC, which is expressed asn
√
3, and determinen.
—
Step 1: Understand the configuration.
Given that AK=AL= 14 , and BK=CL= 14 , and KL= 14, all these segments are equal to 14. So, we
have:
- AK=AL= 14 : So point K and L are both at distance 14 from A - BK= 14, CL= 14: So both K and L
are at distance 14 fromBandC, respectively -KL= 14
So,Klies at intersection of: - Circle centered atAwith radius 14 - Circle centered atBwith radius 14
Similarly,Llies at intersection of: - Circle centered atAwith radius 14 - Circle centered atCwith radius 14
And additionally,KL= 14
So bothKandLlie on the intersection of circle centered atAand circles centered atBandC, respectively.
Moreover,KL= 14, so the distance betweenKandLis 14.
—
Step 2: Use symmetry.
Since the triangle is right-angled at A, and the construction is symmetric (both K and L are symmetric with respect
toA, and distances toBandCare equal), it is likely that the triangle is isosceles right triangle.
Suppose AB=AC . Then △ABC is an isosceles right triangle with legs AB=AC=x , and hypotenuse
BC=x
√
2 = 38
Then:
x
√
2 = 38⇒x= 38√
2
= 19
√
2
SoAB=AC= 19
√
2
Now, consider the pointKsuch thatAK=BK= 14
Similarly,Lsuch thatAL=CL= 14
Because of symmetry, if the triangle is symmetric about the angle bisector (the liney=xif we placeAat origin),
thenKandLare symmetric points with respect to this line.
SoKlies in one region,Lin the mirror region.
ThenKL= 14, and we can compute the distance between such symmetric points.
Let’s try to place coordinates.
—
Step 3: Coordinate setup.
Place pointAat origin(0,0)
LetB= (b,0),C= (0, c)
Since∠A= 90 ◦, this is valid.
We are toldBC= 38
By distance formula:
BC2 = (b−0)2 + (0−c)2 =b 2 +c 2 = 382 = 1444
We also have pointsKandLsuch that:
- AK= 14→K lies on circle x2 +y 2 = 196 - BK= 14→(x−b) 2 +y 2 = 196 - CL= 14→
x2 + (y−c)2 = 196-AL= 14→x 2 +y 2 = 196-KL= 14
So bothKandLlie on the circle centered atAwith radius 14.
Let’s find coordinates ofK: intersection of circles: -x 2 +y 2 = 196(1) -(x−b) 2 +y 2 = 196(2)
Subtract (1) from (2):
(x−b) 2 −x 2 = 0⇒x 2 −2bx+b 2 −x 2 =−2bx+b 2 = 0⇒ −2bx+b2 = 0⇒x= b
2
Plug into (1):
b
2
2
+y 2 = 196⇒ b2
4 +y 2 = 196⇒y 2 = 196− b2
4
Similarly, for pointL, sinceCL= 14, andAL= 14, by symmetry, we get:
x2 + (y−c)2 = 196, andx2 +y 2 = 196
Subtract:(y−c) 2 −y 2 = 0⇒ −2cy+c2 = 0⇒y= c
2
Then fromx 2 +y 2 = 196:x2 +
 c
2
2 = 196⇒x 2 = 196− c2
4
So coordinates:
-K=

b
2 , yK

, wherey 2
K = 196− b2
4 -L=
 
xL, c
2

, wherex 2
L = 196− c2
4
Now,KL= 14
So compute distance betweenKandL:
KL2 =
b
2 −x L
2
+

yK − c
2
2
= 196
17

## Page 18

GRPO Solution (Cont.)
This seems messy unlessb=c, i.e., isosceles right triangle.
Try assumingb=c
Thenb 2 +c 2 = 2b2 = 1444⇒b 2 = 722⇒b=
√
722 =
√
722
Now, forK:x K = b
2 ,y 2
K = 196− b2
4 = 196− 722
4 = 196−180.5 = 15.5
Similarly,x 2
L = 196− 722
4 = 15.5, soxL =
√
15.5
SoK=

b
2 ,
√
15.5

,L=
√
15.5, b
2

Now computeKL 2:
KL2 =
b
2 −
√
15.5
2
+
√
15.5− b
2
2
= 2
b
2 −
√
15.5
2
Setd= b
2 , thenb 2 = 722⇒d 2 = 722
4 = 180.5
ThenKL 2 = 2(d−
√
15.5)2
Computed=
√
180.5≈13.43√
15.5≈3.937
Thend−
√
15.5≈13.43−3.937 = 9.493
ThenKL 2 ≈2×(9.493) 2 ≈2×90.1≈180.2, which is not 196.
But we needKL= 14, soKL 2 = 196
So this value is too small — contradiction.
Therefore, in the isosceles case,KL 2 ≈180<196, so not satisfying the condition.
So the triangle is not isosceles?
But the symmetry suggests it might be.
Alternatively, maybe the configuration implies symmetry, and the triangle is isosceles, but our calculation is wrong.
Wait — perhaps we assumed the wrong point.
Wait: we assumed thatKis equidistant fromAandB, so lies atx=b/2
But is that correct?
Yes — from the two equations:
x2 +y 2 = 196
(x−b) 2 +y 2 = 196
Subtract:−2bx+b 2 = 0⇒x=b/2
Yes.
Similarly, forL,y=c/2
So coordinates are correct.
ThenKL 2 = (b/2−xL)2 + (yK −c/2) 2
Withx 2
L = 196−c2/4,y 2
K = 196−b2/4
So define:
Letu=b/2,v=c/2
Thenb= 2u,c= 2v
Thenb 2 +c 2 = 4u2 + 4v2 = 1444⇒u 2 +v 2 = 361
Now,y 2
K = 196−u2, soy K =
√
196−u 2
Similarly,x 2
L = 196−v 2, sox L =
√
196−v 2
Then:
KL2 = (u−
p
196−v 2)2 + (
p
196−u 2 −v) 2 = 196
This is symmetric inuandv, so likelyu=v
Tryu=v
Thenu 2 +v 2 = 2u2 = 361⇒u 2 = 180.5
Thenu=
√
180.5≈13.43
Then
√
196−u 2 = √196−180.5 =
√
15.5≈3.937
ThenKL 2 = 2(u−
√
15.5)2 ≈2(13.43−3.937) 2 = 2(9.493)2 ≈2×90.1 = 180.2̸= 196
Still too small.
So even with symmetry,KL 2 <196
But we needKL 2 = 196
So contradiction.
Therefore, the triangle is not symmetric?
But then why areAK=AL=BK=CL= 14?
There is symmetry:Kis symmetric toLin some way?
Wait — maybeKandLare symmetric with respect to the angle bisector.
But unless the triangle is isosceles, such symmetry is not possible.
Alternatively, perhaps the pointsKandLare such that triangleAKLis equilateral?
GivenAK=AL=KL= 14, so triangleAKLis equilateral!
Yes! This is key.
We are toldAK=AL=KL= 14, so△AKLis equilateral.
So∠KAL= 60 ◦
But∠A= 90 ◦, so that’s possible.
So pointKandLare at distance 14 fromA, and from each other, forming an equilateral triangle.
18

## Page 19

GRPO Solution (Cont.)
Also,BK= 14,CL= 14
SoKlies on intersection of circles: centerA, radius 14 and centerB, radius 14
Similarly,Llies on intersection of circles: centerA, radius 14 and centerC, radius 14
So we can find coordinates.
Let’s proceed with coordinate geometry.
LetA= (0,0),B= (c,0),C= (0, b), soAB=c,AC=b,BC=
√
b2 +c 2 = 38
Sob 2 +c 2 = 1444
Now, point K lies at intersection of: - x2 +y 2 = 196(distance from A) - (x−c) 2 +y 2 = 196(distance from B)
Subtract:(x−c) 2 −x 2 = 0⇒ −2cx+c2 = 0⇒x= c
2
Then
 c
2
2 +y 2 = 196⇒y 2 = 196− c2
4
Similarly, pointLlies on: -x 2 +y 2 = 196-x 2 + (y−b)2 = 196
Subtract:(y−b) 2 −y 2 =−2by+b 2 = 0⇒y= b
2
Thenx 2 +

b
2
2
= 196⇒x 2 = 196− b2
4
So: -K=
 c
2 , yK

,y K =
q
196− c2
4 -L=

xL, b
2

,x L =
q
196− b2
4
Now,KL= 14, so:
KL2 =
c
2 −x L
2
+

yK − b
2
2
= 196
Let’s define: -u= c
2 ,v= b
2
Thenc= 2u,b= 2v, andb 2 +c 2 = 4u2 + 4v2 = 1444⇒u 2 +v 2 = 361
Now: -y K =
√
196−u 2 -x L =
√
196−v 2
Then:
KL2 = (u−
p
196−v 2)2 + (
p
196−u 2 −v) 2 = 196
Let’s expand this expression:
First term:(u−
√
196−v 2)2 =u 2 −2u
√
196−v 2 + (196−v2)
Second term:(
√
196−u 2 −v) 2 = (196−u2)−2v
√
196−u 2 +v 2
Add both:
Total:
u2 + 196−v2 + 196−u2 +v 2 −2u
p
196−v 2 −2v
p
196−u 2
= 392−2u
p
196−v 2 −2v
p
196−u 2.
Set equal to 196:
392−2u
p
196−v 2 −2v
p
196−u 2 = 196
2u
p
196−v 2 + 2v
p
196−u 2 = 296
u
p
196−v 2 +v
p
196−u 2 = 148.
Now, recall thatu 2 +v 2 = 361
LetS=u
√
196−v 2 +v
√
196−u 2 = 148
We can try to assume symmetry:u=v
Then2u 2 = 361⇒u 2 = 180.5
Thenu=
√
180.5≈13.43
Then
√
196−u 2 = √196−180.5 =
√
15.5≈3.937
ThenS=u·
√
15.5 +v·
√
15.5 = 2u·
√
15.5≈2×13.43×3.937≈2×52.9≈105.8̸= 148
Too small.
So not symmetric.
We need to solve:
u2 +v 2 = 361
u
√
196−v 2 +v
√
196−u 2 = 148
Try to make a substitution.
Leta=u 2,b=v 2, soa+b= 361
Thenu= √a,v=
√
b
So the equation becomes:√a
√
196−b+
√
b√196−a= 148
Note:196−b= 196−(361−a) = 196−361 +a=a−165
Similarly,196−a=b−165
So:p
a(a−165) +
p
b(b−165) = 148
Butb= 361−a, so:p
a(a−165) +
p
(361−a)(361−a−165) = 148
Simplify:p
a(a−165) +
p
(361−a)(196−a) = 148
19

## Page 20

GRPO Solution (Cont.)
Now, define function:
f(a) =
p
a(a−165) +
p
(361−a)(196−a)
We wantf(a) = 148
Domain:a >165, and361−a >0⇒a <361, and196−a >0⇒a <196
So165< a <196
Trya= 180
Then:
- a(a−165) = 180×15 = 2700 ,
√
2700≈51.96 - (361−180)(196−180) = (181)(16) = 2896 ,√
2896≈53.82- Sum≈51.96 + 53.82 = 105.78→too small
Trya= 190
- a(a−165) = 190×25 = 4750 ,
√
4750≈68.92 - (361−190)(196−190) = (171)(6) = 1026 ,√
1026≈32.03- Sum≈68.92 + 32.03 = 100.95→even smaller
Wait — it’s decreasing?
Wait, whenaincreases, first term increases, second decreases.
But ata= 165, first term is 0, second term:(361−165)(196−165) = (196)(31) = 6076,
√
6076≈77.95
Ata= 196, first term:196(31) = 6104,
√
6104≈78.13
Second term:(361−196)(0) = 0
So maximum value off(a)is about78.13 + 0 = 78.13?
Wait — this is less than 148!
But we need sum= 148
But the maximum value of each square root is about 78, so sum can’t exceed about 156?
Wait:
p
a(a−165), fora= 196:196×(196−165) = 196×31 = 6104,
√
6104≈78.13
Similarly, maximum of other term ata= 165is √196×31 =
√
6076≈77.95
So sum max is about78 + 78 = 156
So 148 is possible!
But ata= 190, we got only∼101— why?
Wait:a= 190,a(a−165) = 190×25 = 4750,
√
4750≈68.9
(361−190) = 171,(196−190) = 6,171×6 = 1026,
√
1026≈32.0
Sum≈100.9
Ata= 180:51.96 + 53.82 = 105.78
Ata= 170:a(a−165) = 170×5 = 850,
√
850≈29.15
(361−170) = 191,(196−170) = 26,191×26 = 4966,
√
4966≈70.47
Sum≈29.15 + 70.47 = 99.62
All are below 100!
Wait — this can’t be. The maximum of the sum is about 156, but values are all below 100.
I must have made a calculation error.
Wait: whena= 196, first term:a(a−165) = 196×(196−165) = 196×31 = 6104,
√
6104 =?
6104:78 2 = 6084,792 = 6241→
√
6104≈78.13
Second term:(361−196)(196−196) = 165×0 = 0→sum= 78.13
Ata= 165: first term= 0, second term:(196)(31) = 6076, sqrt≈77.95→sum= 77.95
So the maximum is about78.13
But we need sum= 148
Impossible!
Contradiction.
So there is no solution?
But the problem states that such points exist.
Therefore, our assumption must be wrong.
Wait — is it possible that the pointKis not the intersection of circle A and circle B, but another point?
The given is:AK=AL=BK=CL=KL= 14
We have:
-AK= 14-BK= 14-AL= 14-CL= 14-KL= 14
So yes,Kis at distance 14 from bothAandB, so lies on intersection
20

## Page 21

NudgeRL Solution
<start_working_out>
We are given a right triangle△ABC with ∠A= 90◦ and hypotenuse BC= 38. There are two points K and L
inside the triangle such that:
AK=AL=BK=CL=KL= 14
We are to find the area of quadrilateralBKLC, which is expressed asn
√
3, and findn.
—
### Step 1: Understand the configuration
We have: - ∠A= 90◦, so AB and AC are legs, BC= 38 is the hypotenuse. - Points K and L are inside the
triangle. - All of the following distances are equal to 14: -AK=AL=BK=CL=KL= 14
This suggests symmetry. Since AK=AL , and BK=CL , and KL= 14, it’s likely that K and L are symmetric
with respect to the angle bisector or the median fromA.
Moreover,AK=ALsuggests thatKandLlie on the perpendicular bisector ofBLor something symmetric.
But let’s try to exploit symmetry.
—
### Step 2: Consider symmetry
Since AK=AL and BK=CL , and the triangle is right-angled at A, a natural symmetry is about the angle
bisector of∠A, which in a right triangle is the liney=xif we placeAat the origin andAB,ACalong the axes.
Let’s place the triangle in coordinate plane:
Let: -A= (0,0)-B= (b,0)-C= (0, c)
ThenBC= 38, so by Pythagoras:
b2 +c 2 = 382 = 1444
We are to find pointsKandLsuch that: -AK=AL= 14-BK= 14-CL= 14-KL= 14
Let’s suppose that due to symmetry,KandLare symmetric with respect to the liney=x. Then:
LetK= (x, y), thenL= (y, x)
Then: - AK=
p
x2 +y 2 = 14⇒x 2 +y2 = 196— (1) - BK=
p
(x−b) 2 +y 2 = 14⇒(x−b) 2 +y2 =
196 — (2) - CL=
p
(y−c) 2 +x 2 = 14⇒(y−c) 2 +x 2 = 196— (3) - KL=
p
(x−y) 2 + (y−x)2 =p
2(x−y) 2 =
√
2|x−y|= 14
So: √
2|x−y|= 14⇒ |x−y|= 14√
2
= 7
√
2
Sox−y=±7
√
2. Without loss of generality, assumex > y, sox−y= 7
√
2— (4)
—
### Step 3: Use equations (1), (2), (3), (4)
From (1):x 2 +y 2 = 196
From (4):x=y+ 7
√
2
Plug into (1):
(y+ 7
√
2)2 +y 2 = 196
y2 + 14
√
2y+ 98 +y2 = 196
2y2 + 14
√
2y+ 98 = 196
2y2 + 14
√
2y= 98
y2 + 7
√
2y= 49
This is a quadratic iny. Let’s solve it.
Complete the square:
y2 + 7
√
2y= 49
y2 + 7
√
2y+
 
7
√
2
2
!2
= 49 +
 
7
√
2
2
!2
y2 + 7
√
2y+ 49·2
4 = 49 +98
4 = 49 + 24.5 = 73.5
So:  
y+ 7
√
2
2
!2
= 73.5 =147
2
So:
y=− 7
√
2
2 ±
r
147
2
This is messy, and we haven’t yet used the other conditions involving b and c. So perhaps we should go back to
equations (2) and (3).
21

## Page 22

NudgeRL Solution (Cont.)
—
From equation (2):(x−b) 2 +y 2 = 196
From (1):x 2 +y 2 = 196
Subtract (1) - (2):
(x2 +y 2)−[(x−b) 2 +y 2] = 0
x2 −(x 2 −2bx+b 2) = 0
x2 −x 2 + 2bx−b2 = 0
2bx=b 2
Sob= 2x
Similarly, go to equation (3):(y−c) 2 +x 2 = 196
From (1):x 2 +y 2 = 196
Subtract (3) - (1):
[(y−c) 2 +x 2]−[x 2 +y 2] = 0
(y−c) 2 −y 2 = 0
y2 −2cy+c 2 −y 2 = 0
−2cy+c 2 = 0
Soc= 2y
Now we have: -b= 2x-c= 2y-x 2 +y 2 = 196-x−y= 7
√
2
And also from the hypotenuse:
b2 +c 2 = 1444
(2x)2 + (2y)2 = 1444
4x2 + 4y2 = 1444
x2 +y 2 = 361
Wait! This contradicts equation (1), which saidx 2 +y 2 = 196.
So contradiction!
That means our assumption thatK= (x, y),L= (y, x)is invalid?
But why? Because AK=AL= 14 , and symmetry about y=x makes sense, but the distance from K to B and
LtoCmay not match unless the legs are in a certain ratio.
But we get a contradiction: x2 +y 2 = 196from AK= 14, but from b2 +c 2 = 1444, we get x2 +y 2 = 361,
which is not equal.
So our assumption must be wrong.
Where did we go wrong?
Ah — in the step where we said from (2) and (1), we gotb= 2x. Let’s double-check:
From (1):x 2 +y 2 = 196
From (2):(x−b) 2 +y 2 = 196
Subtract (1) from (2):
(x−b) 2 −x 2 = 0
x2 −2bx+b 2 −x 2 = 0
−2bx+b 2 = 0
b(b−2x) = 0
So eitherb= 0(impossible) orb= 2x
Same forc= 2y
So the algebra seems correct.
But thenb 2 +c 2 = 4x2 + 4y2 = 4(x2 +y 2) = 4×196 = 784
But we are toldBC= 38, sob 2 +c 2 = 382 = 1444
But784̸= 1444
Contradiction.
So our assumption thatKandLare symmetric acrossy=xmust be invalid.
Alternative idea: MaybeKandLare symmetric with respect to the altitude fromA, or the angle bisector?
Alternatively, perhaps the configuration is such that K and L are located so that they are equidistant from A, B, C,
and each other.
Wait — we are given:
-AK=AL= 14-BK= 14-CL= 14-KL= 14
So: - K is at distance 14 from A and B - L is at distance 14 from A and C - K and L are at distance 14 from each
other
22

## Page 23

NudgeRL Solution (Cont.)
SoKlies at intersection of circles: - Circle centered atAwith radius 14 - Circle centered atBwith radius 14
Similarly,Llies at intersection of: - Circle centered atAwith radius 14 - Circle centered atCwith radius 14
So bothKandLare at intersection of circleAand circleB, andAandCrespectively.
So we can find coordinates.
—
### Step 4: Coordinate geometry setup
Let’s place: -A= (0,0)-B= (b,0)-C= (0, c)
Thenb 2 +c 2 = 382 = 1444
Now, find intersection of circle centered atA(0,0)with radius 14 and circle centered atB(b,0)with radius 14.
Equation of circle atA:x 2 +y 2 = 196
Equation of circle atB:(x−b) 2 +y 2 = 196
Subtract:
(x−b) 2 −x 2 = 0
x2 −2bx+b 2 −x 2 = 0
−2bx+b 2 = 0
x= b
2
Plug intox 2 +y 2 = 196:
b
2
2
+y 2 = 196
b2
4 +y 2 = 196
y2 = 196− b2
4
Soy=±
q
196− b2
4
SinceKis inside the triangle, we takey >0, so
yK =
s
196− b2
4
Similarly, findL: intersection of circle atAand circle atC(0, c)
Circle atC:x 2 + (y−c)2 = 196
Subtract fromx 2 +y 2 = 196:
x2 +y 2 −[x 2 + (y−c)2] = 0
y2 −(y 2 −2cy+c 2) = 0
2cy−c 2 = 0
y= c
2
Then:
x2 +
c
2
2
= 196⇒x 2 = 196− c2
4
So:
xL =
s
196− c2
4
(positive, since inside triangle)
So: -K=

b
2 ,
q
196− b2
4

-L=
q
196− c2
4 , c
2

We are given thatKL= 14
So compute distance betweenKandL:
KL2 =

b
2 −
s
196− c2
4


2
+


s
196− b2
4 − c
2


2
= 142 = 196
23

## Page 24

NudgeRL Solution (Cont.)
Let’s define: -p= b
2 -q= c
2
Thenb= 2p,c= 2q
Then:
b2 +c 2 = 4p2 + 4q2 = 4(p2 +q 2) = 1444⇒p2 +q 2 = 361
Now express the coordinates: -K= (p,
p
196−p 2)-L= (
p
196−q 2, q)
Then:
KL2 = (p−
p
196−q 2)2 + (
p
196−p 2 −q) 2 = 196
Expand:
First term:
(p−
p
196−q 2)2 =p 2 −2p
p
196−q 2 + (196−q2)
Second term:
(
p
196−p 2 −q) 2 = (196−p2)−2q
p
196−p 2 +q 2
Add both:
p2 + 196−q2 + 196−p2 +q 2
−2p
p
196−q 2 −2q
p
196−p 2 = 196
Simplify:
-p 2 −p 2 = 0-−q 2 +q 2 = 0-196 + 196 = 392
So:
392−2p
p
196−q 2 −2q
p
196−p 2 = 196
Bring to left:
392−196 = 2p
p
196−q 2 + 2q
p
196−p 2
196 = 2p
p
196−q 2 + 2q
p
196−p 2
98 =p
p
196−q 2 +q
p
196−p 2
Now recall thatp 2 +q 2 = 361
Let’s definex=p,y=q, so: -x 2 +y 2 = 361-x
p
196−y 2 +y
√
196−x 2 = 98
Let’s try to simplify or guess values.
Note thatx 2 +y 2 = 361, sox2, y2 ≤361
Also:
196−x 2 ≥0⇒x 2 ≤196
similarlyy 2 ≤196
Let’s supposex=y. Then:
2x2 = 361⇒x 2 = 180.5⇒x≈13.43
Check if the equation holds:
Left side:
x
p
196−x 2 +x
p
196−x 2 = 2x
p
196−x 2
Since:
x2 = 180.5⇒196−x 2 = 15.5
We have: √
15.5≈3.937
and
x≈
√
180.5≈13.43
So:
2×13.43×3.937≈2×52.9≈105.8̸= 98
Too big.
Sox=yis too big.
We need smaller value.
Try to assumex 2 =a,y 2 = 361−a
We want: √a
p
196−(361−a) +
√
361−a
√
196−a= 98
Simplify:
196−(361−a) =a−165
So: p
a(a−165) +
p
(361−a)(196−a) = 98
24

## Page 25

NudgeRL Solution (Cont.)
Now define function:
f(a) =
p
a(a−165) +
p
(361−a)(196−a)
Domain:
a >165
since:
a(a−165)≥0
Also:
a≤196,361−a≥0⇒a≤361
so:
a∈(165,196]
Trya= 169:
- a(a−165) = 169(4) = 676,
√
676 = 26- 361−169 = 192 - 196−169 = 27 - 192×27 = 5184 -√
5184 = 72
Sum:
26 + 72 = 98
Perfect!
So:
a= 169
Hence:
x2 = 169⇒x= 13
and:
y2 = 361−169 = 192⇒y=
√
192 = 8
√
3
Now check:
x2 +y 2 = 169 + 192 = 361
Also: p
a(a−165) =
√
169·4 =
√
676 = 26
and: p
(361−169)(196−169) =
√
192·27 =
√
5184 = 72
Sum:
26 + 72 = 98
Perfect.
So: -p=x= 13-q=y=
√
192 = 8
√
3
Then: -b= 2p= 26-c= 2q= 16
√
3
Check:
b2 +c 2 = 262 + (16
√
3)2 = 676 + 256·3 = 676 + 768 = 1444 = 382
Good.
Now we have coordinates:
K=

b
2,
s
196−
b
2
2

 = (13,
√
196−169) = (13,
√
27) = (13,3
√
3)
and:
L=
 r
196−
c
2
2
, c
2
!
Since: c
2 = 8
√
3
and: c
2
2
= (8
√
3)2 = 192
So: √
196−192 =
√
4 = 2
Thus:
L= (2,8
√
3)
25

## Page 26

NudgeRL Solution (Cont.)
Therefore: -K= (13,3
√
3)-L= (2,8
√
3)
Now we want the area of quadrilateralBKLC
Points: -B= (26,0)-K= (13,3
√
3)-L= (2,8
√
3)-C= (0,16
√
3)
QuadrilateralBKLC— in order:
B→K→L→C→B
We can compute its area using shoelace formula.
List the points in order:
1.B= (26,0)2.K= (13,3
√
3)3.L= (2,8
√
3)4.C= (0,16
√
3)
Back toB= (26,0)
Shoelace formula:
Area= 1
2

X
xiyi+1 −
X
yixi+1

Compute: X
xiyi+1
-26·3
√
3 = 78
√
3-13·8
√
3 = 104
√
3-2·16
√
3 = 32
√
3-0·0 = 0
Sum:
(78 + 104 + 32)
√
3 = 214
√
3
Compute: X
yixi+1
-0·13 = 0-3
√
3·2 = 6
√
3-8
√
3·0 = 0-16
√
3·26 = 416
√
3
Sum:
(0 + 6 + 0 + 416)
√
3 = 422
√
3
Now:
Area= 1
2|214
√
3−422
√
3|= 1
2 ·208
√
3 = 104
√
3
So:
n= 104
—
Final Answer:
<SOLUTION>104</SOLUTION>
G Full Evaluation Results
Table 3: pdrop ablation results. We reportpass@1 estimated using 128 rollouts. Best results are
represented asbold.
pdrop AIME24 AIME25 AMC23 MATH500 Average
0.00 0.418 0.344 0.759 0.628 0.537
0.25 0.461 0.354 0.773 0.658 0.561
0.500.482 0.393 0.857 0.660 0.598
0.75 0.458 0.361 0.796 0.649 0.566
Table 4: Hint sampling ablation results. We reportpass@1 estimated using 128 rollouts. Best results
are represented asbold.
SamplingAIME24 AIME25 AMC23 MATH500 Average
Random0.482 0.393 0.857 0.660 0.598
Top ranked 0.448 0.355 0.774 0.632 0.552
H Broader Impacts
This paper proposes an efficient framework for structured exploration in reinforcement learning with
verifiable rewards (RLVR). On the positive side, our method improves exploration efficiency without
26

## Page 27

Table 5: λ ablation results. We reportpass@1 estimated using 128 rollouts. Best results are
represented asbold.
λAIME24 AIME25 AMC23 MATH500 Average
0.9 0.403 0.366 0.806 0.648 0.556
1.0 0.436 0.359 0.831 0.643 0.567
1.10.482 0.393 0.857 0.660 0.598
Table 6: λdistill ablation results. We reportpass@1 estimated using 128 rollouts. Best results are
represented asbold.
λdistill AIME24 AIME25 AMC23 MATH500 Average
0.0 0.423 0.362 0.826 0.628 0.560
0.10.482 0.393 0.857 0.660 0.598
0.5 0.425 0.361 0.730 0.629 0.536
relying on extremely large rollout budgets or expensive oracle supervision, which may help reduce
the computational cost of training reasoning models and improve accessibility for smaller research
groups.
However, improving exploration efficiency may also contribute to the development of increasingly
capable reasoning systems, which could be misused in harmful or unintended ways. We therefore
emphasize the importance of continued research on safety, oversight, and responsible deployment.
27

## Page 28

Table 7: ϵhigh scaling results. We reportpass@1 estimated using 128 rollouts. Best results are
represented asbold.
Algorithmϵ high AIME24 AIME25 AMC23 MATH500 Average
NudgeRL 0.20.482 0.393 0.857 0.660 0.598
GRPO
0.2 0.444 0.367 0.7490.6680.557
0.24 0.4510.3730.795 0.6450.566
0.28 0.443 0.372 0.793 0.648 0.564
0.320.4520.358 0.813 0.6400.566
0.36 0.432 0.3380.8450.647 0.565
0.40 0.406 0.341 0.781 0.638 0.541
28
