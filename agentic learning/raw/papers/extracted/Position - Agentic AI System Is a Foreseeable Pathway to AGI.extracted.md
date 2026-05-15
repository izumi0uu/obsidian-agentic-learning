# Position: Agentic AI System Is a Foreseeable Pathway to AGI - Extracted Text

- Source note: [[Position - Agentic AI System Is a Foreseeable Pathway to AGI]]
- Source PDF: `assets/Position - Agentic AI System Is a Foreseeable Pathway to AGI.pdf`
- Extracted: 2026-05-15
- Extractor: pypdf
- Pages: 16
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

Position: Agentic AI System Is a Foreseeable Pathway to AGI
Junwei Liao 1 2 Shuai Li 1 2 Muning Wen1 Jun Wang3 Weinan Zhang1 2
Abstract
Is monolithic scaling the only path to AGI? This
paper challenges the dogma that purely scaling
a single model is sufficient to achieve Artificial
General Intelligence. Instead, we identify Agen-
tic AI as a necessary paradigm for mastering
the complex, heterogeneous distribution of real-
world tasks. Through rigorous theoretical deriva-
tions, we contrast the optimization constraints
of monolithic learners against the efficiency of
Agentic systems, progressing from simple routing
mechanisms to general Directed Acyclic Graph
(DAG) topologies. We demonstrate that Agentic
AI achieves exponentially superior generalization
and sample efficiency. Finally, we discuss the
connection to Mixture-of-Experts, reinterpret the
instability of current multi-agent frameworks, and
call for greater research focus on Agentic AI.
1. Introduction
The No Free Lunch Theorem (Wolpert & Macready, 1997)
dictates that no universal intelligence can perform perfectly
on every conceivable task. Consequently, given the in-
ductive nature of real-world problems, the objective is to
achieve AGI within the context of the human world. But how
is AGI defined in this sense? Historically, Machine Intelli-
gence has been subject to numerous interpretations (Gudwin,
2000; Horst, 2002). Legg and Hutter, after surveying various
perspectives, define it as an agent’s ability to“achieve goals
in a wide range of environments, ”which aligns with most
definitions (Legg & Hutter, 2007). Furthermore, Chollet
posits that“the intelligence of a system is a measure of its
skill-acquisition efficiency over a scope of tasks, with respect
to priors, experience, and generalization difficulty”(Chol-
let, 2019).In essence, within the scope of our physical
existence, AGI necessitates optimal performance across
a near-infinite spectrum of human-relevant tasks.
1Shanghai Jiao Tong University 2Shanghai Innovation Institute
3University College London. Correspondence to: Weinan Zhang
<wnzhang@sjtu.edu.cn>.
Proceedings of the 43 rd International Conference on Machine
Learning, Seoul, South Korea. PMLR 306, 2026. Copyright 2026
by the author(s).
Reed et al. (2022) states that“...such an agent (which is
generally capable on a large number of tasks) can be ob-
tained through scaling data, compute and model parameters,
continually broadening the training distribution while main-
taining performance... ”
Despite relentless scaling of data and computation, no sin-
gle monolithic model commands ubiquitous dominance
across all benchmarks (Jimenez et al., 2024; Mialon et al.,
2024; Patil et al., 2025; Phan et al., 2025), and the elusive
quality of true AGI has notably failed to emerge despite
the saturation of high scores. While scaling pushes per-
formance boundaries, it yields diminishing returns at pro-
hibitive costs (Kaplan et al., 2020; Hoffmann et al., 2022;
Pearce & Song, 2024; Porian et al., 2024), resulting in nar-
row proficiency peaks rather than superiority across the full
spectrum of real-world tasks. This limitation stems from
strong biases introduced by specific optimization objectives
and training data (Battaglia et al., 2018), a problem that is
exacerbated when synthetic data is employed (Dohmatob
et al., 2024).
The termAgentic AI is formally proposed as a paradigm
marked by multi-agent collaboration, dynamic task de-
composition, and coordinated autonomy(Sapkota et al.,
2026). From isolated to coordinated, Agentic AI moves
beyond monolithic scaling to bring up more aspects of or-
chestrating the multi-agent systems. Actually, platforms
like Manus AI (Manus, 2024) and coding assistants such
as Codex (OpenAI, 2024), Claude Code (Anthropic, 2024),
have preliminarily exemplified the power of Agentic AI.
However, most AI research centers on monolithic models,
and there is still no concrete theoretical proof showing that
Agentic AI is overall superior to the monolithic approach.
In this work, we present a series of demonstrations and the-
oretical derivations to substantiate the claim thatAgentic
AI is the foreseeable cross-level move towards AGI. This
capability arises from its ability to adaptively decompose
tasks into correlated atomic ones and orchestrate specific
agents with distinct biases, thereby aligning with real-world
structures and pushing Pareto optimality. The remainder of
the paper is organized as follows: In Section 2, we estab-
lish the theoretical foundations necessary for our proof by
reviewing constraints from learning theory. In Section 3, we
demonstrate the inability of monolithic models to achieve
1
arXiv:2605.12966v1  [cs.AI]  13 May 2026

## Page 2

Position: Agentic AI System Is a Foreseeable Pathway to AGI
Human IntelligenceAgentic AI
Monolithics
Universally
Perfect
Intelligence
Task Spectrum
Real-world Tasks
Specific Tasks ExpandedExpanded
Usability
Threshold
Figure 1.Agentic AI expands the range of usable tasks and im-
proves performance compared to monolithic models. While mono-
lithic models exhibit narrow performance peaks only on specific
tasks they are trained for, Agentic AI demonstrates multi-peak
performance across a broader spectrum. This expands usable capa-
bilities, approaching and even surpassing the altitude and breadth
of human intelligence.
multi-peak performance and derive the advantage of routing-
based Agentic AI. We then extend this analysis in Section 4
to general Agentic AI represented as directed acyclic graphs
(DAGs) of Agents. We also list some alternative views in
Section 5 and reinterpret them after conveying the main idea
of the paper. Finally, in Section 7, we conclude by posi-
tioning Agentic AI as the inevitable successor to monolithic
scaling on the path to AGI.
2. Theoretical Foundations
2.1. Structured Real-World Distribution
The No Free Lunch Theorem asserts that, without prior
assumptions on the data distribution, no learning algorithm
outperforms any other on average. However, real-world
tasks are not uniform noise; they obey specific physical and
semantic constraints. To rigorously analyze the advantage
of Agentic AI, we formalize the data-generating process
not merely as a statistical mixture, but as a collection of
functions supported on low-dimensional manifolds.
Definition 2.1(Structured Real-World Distribution).Let
the input space be X ⊆RD and the output space be Y ⊆R.
We define theStructured Real-World Distribution Dreal as
a measure on X × Ygenerated by a latent task variable
z∈ {1, . . . , K}with prior probabilities αk =P(z=k) .
The joint distribution is defined by the tuple (M,F,α) ,
characterized by the following structural properties:
1. Union of Manifolds: The support of the marginal distri-
bution P(x) is a union of K distinct, compact Riemannian
manifolds {Mk}K
k=1, where each Mk ⊂R D has an intrin-
sic dimensiond k ≪D:
supp(P(x))⊆
K[
k=1
Mk
2. Local Functional Consistency: For each task k, there
exists a distinct labeling function fk :M k → Ysuch that
the conditional distribution P(y|x, z=k) is concentrated
aroundf k(x)with noiseξ:
y=f k(ProjMk (x)) +ξ,wherex∈ M k
3. Task Divergence: The optimal functions are heteroge-
neous, meaning for any pair j̸=k , the functional distance
implies distinct optimization landscapes:
inf
θ∈Θ
Ex∼Mk [ℓ(hθ(x), fk(x))]̸= inf
θ∈Θ
Ex∼Mj [ℓ(hθ(x), fj(x))]
Consequently, the density of the structured distribution is
given by:
Dreal(x, y) =
KX
k=1
αk ·I Mk (x)·P(y|f k(x))
This definition elevates the premise from a simple proba-
bilistic mixture to a piecewise-smooth manifold learning
problem.
2.2. Theorems on Generalization Bounds
The Curse of Dimensionality (Bellman et al., 1957) creates
volumetric sparsity as dimension D increases. This is illus-
trated by the vanishing ratio of a hypersphere’s volume to
its enclosing hypercube:
lim
D→∞
Vsphere(r, D)
Vcube(r, D) = 0
Consequently, high-dimensional data concentrates in the
domain’s “corners”. This increases the average distance be-
tween nearest neighbors, rendering local density estimation
intractable.
Due to the volumetric sparsity discussed above, covering
the domain Ω sufficiently to ensure small ∥x−x ′∥2 re-
quires a sample size N that grows exponentially with D.
This limitation is formally quantified by the minimax lower
bound.
Proposition 2.2(Minimax Lower Bound on Compact Do-
mains (Stone, 1982)).Let FL(Ω) be the class of L-Lipschitz
functions restricted to a compact subset Ω⊂R D. Under
the standard non-parametric regression model, the minimax
risk for any estimator ˆfN based onNsamples satisfies:
inf
ˆfN
sup
f∈FL
E
Z
Ω
| ˆfN (x)−f(x)|dP(x)

≥C·N − 1
2+D
where P(x) is the marginal distribution of inputs supported
onΩ, andC >0is a constant independent ofN.
The term N− 1
2+D reflects the curse: to maintain a fixed
error level, N must scale exponentially with D, mirroring
the geometric expansion of the volume.
2

## Page 3

Position: Agentic AI System Is a Foreseeable Pathway to AGI
Recent theoretical advancements provide a rigorous founda-
tion for understanding the efficiency of Transformer-based
architectures. While Yun et al. (2020) established that
Transformers are universal approximators capable of im-
plementing precise contextual mappings, Jiang & Li (2024)
advanced this further by deriving explicit Jackson-type ap-
proximation rates. They proved that the generalization error
is intrinsically governed by the spectral decay properties of
the target function’s temporal coupling, represented by the
singular value decay rateαof the attention mechanism.
By linking these spectral properties to the model’s capac-
ity, we can express the approximation error E as a function
of the parameter count P and the task’s intrinsic dimen-
sion d. Under the standard architectural assumption that
parameters scale quadratically with the hidden dimension
(P∝m 2
h)(Hoffmann et al., 2022) and the spectral theoreti-
cal observation that the decay rate α scales inversely with
dimension (α∝1/d ), the approximation error follows a
dimensionality-dependent power law:
E(P)≈C·P −κ
d (1)
where C is a task-dependent constant and κ represents the
regularity (smoothness) of the target function.
2.3. Multi-Class Learning
Since Agentic AI may involve routing problems, specifi-
cally, choosing a proper agent for a specific input, we intro-
duce some multi-class learning theories. Let X be the in-
stance space and Y={1, . . . , K}be the label space withK
classes. We consider a hypothesis class H ⊆ {h:X → Y}.
Natarajan Dimension (Natarajan, 1989) is the generalization
of VC dimension (Vapnik & Chervonenkis, 1971) for mul-
ticlass classification problems (where the number of labels
K >2).
A set S={x 1, . . . , xm} ⊆ Xis Natarajan-shattered by H
if there exist two ”witness” functions f0, f1 :S→ Y such
that f0(xi)̸=f 1(xi) for all i, and for any binary vector
b∈ {0,1}m, there existsh∈ Hsuch that:
h(xi) =
(
f0(xi)ifb i = 0
f1(xi)ifb i = 1
The Natarajan Dimension dN (H) is the maximum size of
such a shattered set.
Jin (2023) gave the upper bounds on the Natarajan dimen-
sion, dN (H), for the tree-based and neural network function
classes as below.
Theorem 2.3(Natarajan Dimension Upper Bound for
Tree-based Classifiers (Jin, 2023)).Consider multi-class
classification problems with d classes and inputs in Rp. Let
Πdtree
L,d be the class of decision trees of depthL. Let Πforest
L,T,d
be the class of random forests consisting of T such decision
trees. The Natarajan dimensions for these classes are upper
bounded by:
dN (Πdtree
L,d ) =O(L2 L log(pd)),
dN (Πforest
L,T,d ) =O(LT2 L log(pd)).
Theorem 2.4(Natarajan Dimension Upper Bound for Neu-
ral Network Classifiers (Jin, 2023)).Let Πσ
p,S denote the
class of feed-forward neural networks with a fixed structure
S and at most p parameters for d-class classification. If the
activation functions are restricted to binary or linear sets
(denoted as Πbinary
p,S ), or if the activation functions addition-
ally include ReLU (denoted as ΠReLU
p,S ), then the Natarajan
dimension for both cases is upper bounded by:
dN (Πbinary
p,S ) =d N (ΠReLU
p,S ) =O(d·p 2).
With the Natarajan dimension of a hypothesis class estab-
lished, the relationship between model complexity and gen-
eralization performance can be characterized as follows.
Theorem 2.5(Generalization Error Bounds for Multiclass
ERM (Daniely et al., 2011)).For every hypothesis class
H with a finite label set Y, given a sample size m and
confidence parameterδ:
ϵH(m, δ)≤ϵERM (m, δ)≤O


s
dN (H) ln(|Y|) + ln(1
δ )
m


where ϵH(m, δ)denotes the minimax (PAC) error achiev-
able by the optimal learning algorithm, and ϵERM (m, δ)
denotes the uniform ERM error, representing the worst-case
guarantee for any Empirical Risk Minimizer.
3. Why and How Much Monolithic Learner
Falls Behind
In this section, we first provide a formal justification for
the negative transfer phenomenon in monolithic models
when facing heterogeneous tasks. We frame the Average
Trap explicitly as the penalty for ignoring the modular struc-
tural bias of Dreal. Effectively, the monolithic model at-
tempts to compress a modular reality into a dense parameter
space, resulting in optimization conflicts. Then, we model
a naive Routing-based Agentic AI and demonstrate that
even a merely routing-based Agentic AI can beat the mono-
lithic model exponentially in both sample and parameter
complexity.
3.1. The Monolithic Dilemma
Let the parameter space be Θ⊆R d. The goal of a mono-
lithic model is to minimize the weighted average risk:
θ∗
mono = arg min
θ∈Θ
Ltotal(θ) = arg min
θ∈Θ
KX
k=1
αkLk(θ)
3

## Page 4

Position: Agentic AI System Is a Foreseeable Pathway to AGI
In contrast, a specialist model for task k seeks the task-
specific optimumθ ∗
k = arg minθ∈Θ Lk(θ).
Assumption 3.1(Regularity under Ideal Task Sharding).
Assuming the tasks are perfectly sharded such that each
Dk represents a distinct, internally consistent function, the
loss function Lk(θ) is well-behaved. Specifically, we as-
sume Lk(θ) is twice continuously differentiable (C2). Fur-
thermore, in the local neighborhood of its optimal param-
eter θ∗
k, Lk(θ) is strictly convex, implying that its Hessian
matrix Hk(θ) =∇ 2Lk(θ) is positive definite (PD), i.e.,
v⊤Hkv >0for allv̸= 0.
Assumption 3.2(Lipschitz Continuous Hessian).For each
task k, the loss function Lk is twice differentiable and
has a ρk-Lipschitz continuous Hessian, i.e., ∥∇2Lk(θ)−
∇2Lk(θ′)∥ ≤ρk∥θ−θ ′∥.
We now state the proposition, which provides a lower bound
on the monolithic risk. Rather than simple degradation, it
demonstrates the inevitability of a suboptimal compromise:
to accommodate the conflicting gradients of heterogeneous
tasks, the monolithic model is forced to sacrifice peak profi-
ciency in specialized domains, resulting in a flattened and
averaged performance profile.
Proposition 3.3(The Average Trap).Let Ltotal(θ∗
mono) be
the converged risk of the monolithic model. Under Assump-
tion 3.1, if the tasks are heterogeneous such that their opti-
mal parameters do not coincide (i.e.,∃i, j, θ∗
i ̸=θ ∗
j ), strictly
positive lower boundϵ >0exists:
Ltotal(θ∗
mono)≈
KX
k=1
αkLk(θ∗
k) +
KX
k=1
αk
2 ∥θ∗
mono −θ ∗
k∥2
Hk
| {z }
ϵ
where ∥v∥2
Hk =v ⊤Hkv denotes the squared Mahalanobis
distance induced by the task curvature.
See Appendix A.1 for the proof. Thus, we formally prove
the inevitability of the “Generalist’s Penalty”: as the diver-
sity of tasks increases, a monolithic model must trade away
its expert-level acuity to maintain stability, resulting in a
representation that is broadly usable but universally distinct
from the optimum.
3.2. A Merely Routing-based Agentic AI Dominates
The limitations of the Monolithic learner, as proven in The-
orem 3.3, stem from its attempt to approximate a global
function over the complex union SMk. It is forced to
smooth over the discontinuities between disjoint manifolds,
expending capacity on the empty ambient space.
Now, we formalize a naive Routing-based Agentic AI (de-
noted as MR-Agentic), which in contrast, bypasses the Average
Trap by explicitly aligning its architecture with the topolog-
ical structure of Dreal. Instead of solving for a compromised
4
3
2
1
0
1
2
3
4
1
4
3
2
1
0
1
2
3
4
2
0
2
4
6
8
10
12
14
Loss
Sharp T askFlat T ask
Monolithic
Minimum
T ask A (Sharp) Contours
T ask B (Flat) Contours
T ask A Optimum
T ask B Optimum
Monolithic Loss Surface
Monolithic Optimum
Optimum Projection (Floor)
Figure 2.A demonstration of the Average Trap. The monolithic
optimum is pulled towards the sharp task, illustrating the curvature-
induced bias described in Proposition 3.3.
global optimum, the system exploits the geometric decom-
posability of the task mixture. We formalize the routed
agentic hypothesis by assuming the target function f can be
factorized through a routing mechanism π and a set of local
maps:
fR-Agentic(x) =
KX
k=1
I[π(x) =k]·f k(ϕk(x))
where π:X → {1, . . . , K}acts as a geometric router
identifying the active manifold, and ϕk :M k →R dk repre-
sents the local coordinate chart (or projection) that maps the
high-dimensional input onto the low-dimensional intrinsic
manifold of taskk.
In this analysis, we focus on the over-parameterized regime
(P→ ∞), assuming the model possesses sufficient capacity
to fully interpolate the finite training set. Under this assump-
tion, the generalization error is no longer bottlenecked by
model expressivity, but is strictly governed by the sample
complexity relative to the intrinsic geometry of the data.
Monolithic BaselineConsider a Monolithic Learner
Mmono that attempts to approximate f directly in the joint
space RD. In the absence of structural assumptions, the
model must populate the entire D-dimensional domain.
Given a fixed training budget of N samples, the generaliza-
tion error Emono follows the standard convergence rate for
Lipschitz functions in high-dimensional spaces by Proposi-
tion 2.2:
Emono(N)≈ O

N− 1
D

This relationship highlights that the error convergence is bot-
tlenecked by the total dimension D. As the task complexity
(D) increases linearly, the sample size required to maintain
a constant error rate grows exponentially (N∝ϵ −D).
4

## Page 5

Position: Agentic AI System Is a Foreseeable Pathway to AGI
Routing-based Agentic DecompositionIn the Routing-
based Agentic AI framework, the problem is explicitly de-
composed into K distinct sub-tasks. Each agent Ak is
responsible for learning a sub-function fk :R dk →R .
Assuming the aggregation (or routing) function π is fixed
or introduces negligible error, the system’s complexity is
determined by the complexity of its sub-components.
Assuming the training budget N is distributed among the
agents (e.g., N/K samples per agent), the total error bound
is dominated by the sub-task with the highest dimensionality.
Let dmax = maxk(dk) and let Lk be the Lipschitz constant
for fk. The error upper bound for Routing-based Agentic
AI is given by:
ER-Agentic(N) =
KX
k=1
Ek ≈
KX
k=1
Lk · O
 N
K
− 1
dk
!
(2)
≤
KX
k=1
Lk · O
 N
K
− 1
dk
!
+E routing
Assuming ideal routing and considering the dominance of
the most complex sub-task, we obtain:
ER-Agentic(N)≈ O

K·N − 1
dmax

Since dmax ≪D , the exponent −1/dmax is significantly
larger in magnitude (more negative) than −1/D, implying
a substantially faster decay of error.
We further quantify the advantage of the Routing-based
Agentic AI by comparing the ratio of the expected errors.
Neglecting constant factors, we derive the following rela-
tion:
ER-Agentic(N)
Emono(N) ≈ K·N − 1
dmax
N− 1
D
=K·N ( 1
D − 1
dmax )
Since dmax ≪D , the exponent

1
D − 1
dmax

is strictly
negative, indicating that the error of Routing-based Agentic
AI vanishes exponentially faster relative to the Monolithic
error asNgrows.
The implication of the negative exponent is profound when
interpreted through the lens of sample complexity. Specifi-
cally, to achieve a target error rateϵ, the Monolithic model
requires Nmono ∝ϵ −D samples, whereas the Routing-based
Agentic AI requires only NR-Agentic ∝K dmax ϵ−dmax . The
ratio of data requirements is:
NR-Agentic
Nmono
∝K dmax ϵD−dmax (3)
Since ϵ is typically small (ϵ≪1 ) and the dimensionality
gap D−d max is substantial, the term ϵD−dmax asymptoti-
cally dominates the ratio. Although the pre-factor Kdmax
introduces a polynomial overhead corresponding to the num-
ber of agents, it is negligible compared to the exponential
reduction driven by the dimensionality reduction asϵ→0.
This aligns with empirical evidence that specialized agents
are significantly more data-efficient. (Hu et al., 2022). By
decomposing the high-dimensional manifold into lower-
dimensional ones, the Routing-based Agentic AI effectively
circumvents the Curse of Dimensionality, transforming an
overwhelming learning problem into a set of solvable ones.
Based on the scaling law E(P)∝P −κ
d established
in Eq. (1), parameter efficiency follows the same
dimensionality-dependent power law as sample efficiency.
Consequently, the analysis above applies symmetrically to
model size: the Monolithic learner’s error decay is stifled by
the ambient dimension ( O(P − κ
D )), whereas the Routing-
based Agentic AI benefits from a faster rate governed by the
lower intrinsic dimension (O(P− κ
dmax )).
The Routing RegretWe now analyze the omitted Erouting
and explain why it can be ideally omitted in the inequal-
ity (2). We define theRouting Regret, denoted as Erouting,
as the expected performance deficit caused by selecting a
sub-optimal expert. Formally, let k∗(x) be the index of the
optimal expert for input x, and π(x) be the expert selected
by the router. The routing error can be decomposed into the
probability of error and the severity of the mismatch:
Erouting =E x∼Dreal

I(π(x)̸=k ∗(x))
| {z }
ϵπ:Routing Error Rate
·

L(Aπ(x)(x))−L(A k∗(x)(x))

| {z }
∆(x):Mismatch Penalty

To derive a tractable bound, we analyze the two components
of this expectation: the Routing Error Rate ( ϵπ) and the
Mismatch Penalty (∆).
The router essentially solves a K-way classification prob-
lem, mapping the input space X to the set of agent indices
Y={1, . . . , K}. The hardness of this task is governed by
the complexity of the hypothesis class Hrouter employed by
the router.
We quantify the Routing Error Rate ϵπ as the generalization
error of the router. Invoking Theorems from Section 2.3,
for the most common routers trained on Nrouter samples, we
further obtain how the bounds scale with the number of
agentsKas follows:
ϵπ ∝



˜O

logK√Nrouter

,ifπis a Tree-based Routerq
K
Nrouter
,ifπis a Neural Router
The routing error rate of both kinds of routers increases asK
increases, though for the tree-based one, the polylogarithmic
dependence allows a stronger guarantee for the scalability.
The severity of a routing error depends on the orthogonality
of the experts. We define the maximum mismatch penalty
as∆ max = supx,j̸=k∗ |L(Aj(x))−L(A k∗(x))|.
5

## Page 6

Position: Agentic AI System Is a Foreseeable Pathway to AGI
We verify the intuition that the cost of mismatch∆max scales
with the granularity of specialization K. We model this
relationship using subspace information loss.
Assumption 3.4(Manifold Alignment with Orthogonal Sub-
spaces).Following Definition 2.1, we assume each mani-
fold Mk is contained within a feature subspace Sk ⊂R D.
These subspaces form an orthogonal decomposition of the
feature space, such that RD = LK
k=1 Sk and Sj ⊥S k for
j̸=k.
Lemma 3.5.Let x∼ Dj be an input belonging to task j.
Ideally, the information required to solvex is contained in
Sj. However, if misrouted to expertAk (k̸=j ), the expert
processes the projection Pkx. The information preservation
ratio ρ is given by the cosine similarity between the required
subspace and the expert’s subspace:
ρ(j, k) =∥Pkx∥2
∥x∥2
Under Assumption 3.4, if j̸=k , then Sj ⊥S k, implying
Pkx≈0 . In a relaxed setting with partial overlap, as K
increases, the subspaces become increasingly disjoint. We
model the residual information as inversely proportional to
K:
E[∥Pkx∥2]∝ 1
K−1 ∥x∥2 (forj̸=k)
Let the loss function L be λ-Lipschitz continuous. The
mismatch penalty is bounded by the distance in the feature
space caused by the projection loss:
∆(x)≤λ∥x−P kx∥=λ∥x∥

1− ∥Pkx∥
∥x∥

Substituting the expected information preservation ratio
from Lemma 3.5, and defining the maximum potential loss
on the domain as Lmax ≜λE[∥x∥] (representing the loss
scaling with input magnitude), we obtain:
∆max(K)≈L max
 
1−
r
1
K−1
!
∼L max

1− 1√
K

asymptotically, as K→ ∞, using the Taylor expansion
(1−ϵ) −1/2 ≈1 +ϵ/2.
Finally, combining the routing error rate and the mismatch
penalty, we derive an upper bound for the Routing Regret:
Erouting ≤



CtreeLmax

1− 1√
K
q
poly(logK)
Nrouter
,if Tree-based Router
CNNLmax

1− 1√
K
q
K
Nrouter
,if Neural Router
Joint Bound and Optimal GranularityThe preceding
analysis factored out routing error for clarity. We now
present a joint bound that unifies specialization gain and
routing cost. Substituting the routing error ϵπ and mismatch
∆into the agentic bound (2):
ER-Agentic(K, N)≤ KCexp
N1/dmax
| {z }
decreases withK
+ ∆max(K)·ϵ π(K)| {z }
increases withK
This yields a U-shaped error profile in K: too few agents
(K→1 ) provides insufficient specialization, while too
many (K→ ∞) causes routing overhead to dominate, with
an optimal K∗ in between. Expanding for specific router
types:
For tree-based routers:
E ≤ KC
N1/dmax
+C treeLmax

1− 1√
K
r
poly(logK)
Nrouter
The modularity cost grows polylogarithmically, so special-
ization dominates for largeK.
For neural routers:
E ≤ KC
N1/dmax
+C NNLmax

1− 1√
K
r
K
Nrouter
The cost rises as
√
K, restricting K∗ unless Nrouter ∝
K. In both cases, the specialization gain ( N−1/dmax vs.
N−1/D) dominates the polynomial routing cost for suffi-
ciently largeN, sinced max ≪D.
Consequently, for a fixed data budget, the optimal number
of agents K∗ is the solution to ∂Etotal
∂K = 0. System design-
ers face a dichotomy: use tree-based routing to maximize
scalability (K≫1 ) or neural routing to handle complex,
non-axis-aligned task boundaries at the cost of a smaller
feasible agent pool.
In a data-scarce regime, the tree-based router is superior.
Its error scales with O(√logK) , allowing massive scaling
of K even with limited routing data. Here, the Routing
Regret is negligible. In a data-rich regime, if the sample
size N is sufficient (N≫K ), the linear penalty of neural
routers (O(
√
K)) is suppressed by the large denominator.
In this regime, neural routing becomes preferable despite
its higher sample complexity, as it avoids the inductive bias
of trees and can capture complex, non-hierarchical expert
boundaries.
Now we establish that the transition from Monolithic to
Routing-based Agentic AI is not merely an architectural
preference, but a geometric necessity for mastering hetero-
geneous, high-dimensional tasks, manifested by real-world
task distribution.
4. A Closer Look at General Agentic AI
Through the analysis in Section 3, we have theoretically
established that decomposing a monolithic problem into
6

## Page 7

Position: Agentic AI System Is a Foreseeable Pathway to AGI
specialized sub-tasks aligns with the real-world task distri-
bution and yields exponential gains in efficiency and effec-
tiveness. However, it primarily modeled the system as a
static routing between expert agents. In real-world Agen-
tic AI, agents rarely operate in isolation; they function as
interconnected nodes facilitating the dynamic propagation
of information.
To rigorously analyze the generalization bounds, we first
establish a formal mathematical definition of Agentic AI.
Unlike monolithic models, which approximate a target func-
tion F:X → Yvia a single dense parameterization, Agen-
tic AI is defined as a structured composition of specialized
operators.
Definition 4.1(Agentic AI as a System of a Topological
Compositional DAG of Agents).Let X be the global input
space and Y be the global output space. An Agentic AI
system is defined as a tupleΨ = (G,F,Λ), where:
1. G= (V,E) is a Directed Acyclic Graph (DAG) with
K=|V| nodes, representing the flow of information. The
node setVis topologically sorted.
2. F={f 1, . . . , fK} is a set of heterogeneous, learnable
mappings (agents). Each agent vi implements a local func-
tion fi :H (i)
in ×Θi → H(i)
out, where Θi represents the agent’s
specific parameters and H represents the latent manifold of
intermediate representations.
3. Λ is a composition operator that maps the outputs of
parent nodes to the input of a child node. For any agent
vi, the input state si is constructed from the set of parents
P a(i) ={vj |(v j, vi)∈ E}:
xi =f i
 
Λ
 
{xj}j∈Pa(i)

;θ i

The global system behavior is not a static function, but rather
emerges as the topological flow from the source nodes (ini-
tialized by X) to the sink nodes (projected to Y), respecting
the partial order ofG.
For each node vi, let Si ∈ {0,1}be a Bernoulli random
variable indicating the success of the specific task assigned
to agent i. The execution of vi depends on the latent states or
outputs hPa(i) from its parent set P a(i) ={vj |(v j, vi)∈
E}. Assuming the Markov property on the graph, the joint
probability of a successful execution trajectory is:
P(S1, . . . , SN ) =
NY
i=1
P(Si |h Pa(i) )
Then, we transform the multiplicative success probabil-
ity into an additive loss function using the negative log-
likelihood. The loss for Agentic AI LAgentic can be defined
as:
LAgentic(θ) =−log
 KY
i=1
P(Si = 1|h Pa(i) )
!
=
KX
i=1
−logP(S i = 1|h Pa(i) )| {z }
ℓi(θi)
whereℓ i represents the local loss contribution of agenti.
To explicitly derive the local loss li, we instantiate the ab-
stract local function fi as a stochastic generator parame-
terized by a policy. Specifically, the execution of fi cor-
responds to sampling an action ai (which constitutes the
output xi) from a policy πθi(ai |s i) conditioned on the
input state si. Consequently, the local loss ℓi relates to the
agent’s policy via the expectation over actions:
ℓi(θi, si) =−log
Z
A
ρ(si, ai)πθi(ai |s i)da i

where ρ(si, ai)∈[0,1] is the conditional success probabil-
ity of taking actiona i in states i.
To understand how the Agentic AI generalizes, we must
quantify how a local perturbation at a specific agent propa-
gates through complex topologies to affect the loss.
We define theDirect Adjacency Jacobian Matrix J∈
RK×K . The entry Jji captures the local sensitivity of agent
jto its direct parent agenti:
Jji = ∂xj
∂xi
=
(∂fj
∂xi
if(i, j)∈ E
0otherwise
Then, we can derive the topological weight of a specific
agent in the DAG.
Lemma 4.2(Topological Weight).Let L be the Agentic AI
loss function and ωu =
 dL
dxu
 be the scalar Topological
Weight representing the total sensitivity of the loss to agentu.
The weight ωu is determined by the aggregation of gradient
flow along all paths connectinguto the sink agents:
ωu =

X
v∈Sinks
∂L
∂xv
X
ρ∈Paths(u→v)

 Y
(a,b)∈ρ
Jba



See Appendix A.2 for the proof. Given specific agent
weights, we analyze the Agentic AI generalization error,
EAgentic. Consistent with Section 3, we assume local errors
decay via a power law governed by intrinsic dimension
du. Using a first-order Taylor expansion around the opti-
mal agent outputs, EAgentic is approximated as the weighted
7

## Page 8

Position: Agentic AI System Is a Foreseeable Pathway to AGI
superposition of local errors.
EAgentic ≈
KX
u=1
ωu · Eu ≈
KX
u=1
ωu · O
 N
K
− 1
du
!
(4)
≈C(G)·
N
K
− 1
deff
where deff is the effective intrinsic dimension of the task and
C(G) is the Topology Factor determined by the topology of
Agentic AI.
To disentangle the impact of the Topology Factor from the
intrinsic difficulty of specific sub-tasks, we assume that the
complex global task is divided into sub-tasks of comparable
intrinsic difficulty, formally for any sub-task u, du ≈d eff.
Then, the convergence rate term becomes uniform across
all agents. This allows us to factor the complexity term out
of the summation in Equation (4), isolating the Topology
Factor. And further, the Topology Factor C(G) can be
formally defined as the sum of Topological Weights:
C(G)≡
KX
u=1
ωu =
KX
u=1

X
v∈Sinks
∂L
∂xv

 X
ρ∈Pathu→v
Y
e∈ρ
Je



The definition allows us to analyze the stability of different
agentic orchestrations by evaluating how C(G) scales with
DAG complexity, and confirms that whiledeff governs the
rate of convergence, C(G) determines the magnitude of the
error. Agentic AI succeeds when the topology minimizes
C(G)while maximizing the dimensionality gap.
Theorem 4.3(Agentic AI Convergence Superiority).As the
scale of resources (dataset size N or parameter budget P)
increases, the generalization error of the Agentic AI decays
exponentially faster than that of the Monolithic model, pro-
vided the topology satisfies spectral stability (well designed
withC(G)<∞).
Apart from the overall analysis of the graph, we can further
decompose global instability into single-edge contributions
to better analyze the connections.
Lemma 4.4(Topological Edge Weight).Consider a specific
edge e∗ = (u, v)connecting a parent agent u to a child
agent v. The Topological Edge Weight W(e∗) represents
the total gradient flux passing through this edge, linking the
accumulated history of the parent to the future criticality of
the child. It is formally defined as:
W(e∗) =

1 +
X
k∈P(u)

X
ρ∈Path(k→u)
Y
e∈ρ
Je



| {z }
Upstream History
· ∥Je∗∥| {z }
Local Valve
·

X
z∈Sinks
∂L
∂xz
X
γ∈Path(v→z)
Y
e′∈γ
Je′

| {z }
Downstream Future
where P(u) is the set of predecessors of agent u, and Sinks
denotes the set of final output agents.
See Appendix A.3 for the proof. To minimize the global
error C(G), we must well orchestrate the necessary agents
and find the small combinations of edge weights. This
equation reveals a fundamental design principle regarding
what kind of edges we should buildat runtimeand gives a
reference to analyze each edgepost hoc. Specifically: (1)
after long chains (high Upstream History), edges must be
contractive (∥Je∗∥<1 ) to filter accumulated noise, e.g.,
critic or judge edges. (2) Before critical decisions (high
Downstream Sensitivity), edges should satisfy ∥Je∗∥ ≪1,
e.g., voting or verification edges that collapse multiple paths
into a stable signal.
Consequently, we find that optimal edges function as adap-
tive valves. An ideal edge is not a passive pipe but an active
variational filter that suppresses the noise accumulated from
the upstream before it propagates to critical downstream
tasks.
Finally, in this section, we not only extend the superiority
from a Routing-based Agentic AI to a general Agentic AI
by deriving the topological properties of the Agentic AI, but
also further analyze the impact of specific agents and edges,
giving backgrounds for Agentic AI design and Agentic AI
success and failure explanation.
5. Alternative Views
Monolithic scaling is enough for AGIDeepMind ever
stated that“...an agent capable on a large number of tasks
and able to be adapted with little extra data to succeed at an
even larger number of tasks can be obtained by scaling data,
compute and parameters... ”(Reed et al., 2022). Ag¨uera y
Arcas & Norvig (2023) even said that“...the most important
parts of it (AGI) have already been achieved by the current
generation of advanced AI large language models such
as ChatGPT, Bard, LLaMA and Claude. ”However, very
few researchers firmly admit that AGI has come and are
one hundred percent satisfied with one specific monolithic
model, at least in coding, not mention in all real-world
tasks. We don’t object to the view that scaling is effective,
but both neural scaling laws and empirical experiments
have demonstrated that the marginal improvement is more
obvious as an inevitable bottleneck (Kaplan et al., 2020;
Hoffmann et al., 2022). More attention should be drawn to
Agentic AI to break the bottleneck.
Agentic AI is conceptually similar to Mixture-of-Experts
Mixture-of-Experts (MoE) (Shazeer et al., 2017) and Agen-
tic AI share a common design principle: both route inputs
to specialized sub-networks rather than processing every-
thing through a single monolithic model. Both architectures
8

## Page 9

Position: Agentic AI System Is a Foreseeable Pathway to AGI
leverage the insight that task heterogeneity is better handled
by specialized components than by a universal compromise,
and the empirical success of sparse MoEs (Fedus et al.,
2022; Lepikhin et al., 2021) validates this core premise of
our theory, namely that routing to specialized sub-networks
improves performance even when tasks share a common
backbone. In our theoretical framework, MoE corresponds
to the routing regime of Section 3.2, where C(G)≈ PLu
and the system is inherently stable.
However, Agentic AI generalizes beyond MoE in three fun-
damental aspects. First, in scope: MoE employs fixed expert
sub-networks with learned gating within a single forward
pass (Fedus et al., 2022; Lepikhin et al., 2021), whereas
Agentic AI deploys autonomous agents with independent
parameters capable of multi-step reasoning (Sapkota et al.,
2026). Second, in topology: MoE implements single-layer
routing (router → expert), while Agentic AI extends to
arbitrary DAG compositions as formalized in Section 4.
Third, in routing mechanism: MoE relies on differentiable
gating trained end-to-end, whereas agentic routing accom-
modates iterative refinement, external tool use, and dynamic
knowledge retrieval (Sapkota et al., 2026; Anthropic, 2025).
While MoE and routing-based Agentic AI share a common
design principle, Agentic AI extends to richer topological
structures with greater expressivity.
Multi-Agent systems often failEmpirical evidence indi-
cates that increasing agent quantity often introduces organi-
zational entropy rather than performance gains. Complexity
frequently hinders reliability, with failures stemming pri-
marily from system design issues, inter-agent misalignment,
and task verification difficulties (Pan et al., 2025). Fur-
thermore, current LLMs struggle with coordination tasks
requiring Theory of Mind compared to RL methods (Agashe
et al., 2025), necessitating dedicated automated methods to
diagnose these persistent failures (Zhang et al., 2025).
Recent works exploring LaMAS flaws align with our deriva-
tion, attributing failures to Topological Weights and Edge
Weights. For instance, misaligned agents introduce toxic
topological properties, causing massive downstream vari-
ance and hallucination. This necessity for topological aware-
ness is exemplified by the performance surge with well-
designed topologies (Anthropic, 2025). Agentic AI de-
mands dedicated topological design; most current frame-
works are merely static pipeline decompositions based on
human priors, masquerading as true Agentic AI.
6. Call to Action
Prioritize Agentic AI for accessible AGI researchWe
urge researchers and institutions, especially those with lim-
ited resources, to prioritize Agentic AI, which offers a viable
alternative to the prohibitive costs of monolithic scaling and
yields exponential gains in both sample and parameter effi-
ciency. This paradigm allows for state-of-the-art generaliza-
tion without the need for brute-force computation. Since the
efficiency advantage grows exponentially with the dimen-
sionality gap between the ambient space and task-intrinsic
manifolds, a well-designed agentic system of moderately
sized specialists can match or exceed monolithic perfor-
mance at a fraction of the cost, broadening access to AGI
research beyond resource-rich laboratories.
Not only fine-tune weights, but also invent better multi-
agent evolution methods for applicable Agentic AIThe
community must expand its focus from simply fine-tuning
individual agents to a broader and more diverse optimiza-
tion of the agentic system. Research should look beyond
specific weight adjustments and explore various enhance-
ments, such as mitigating organizational entropy, designing
graph, tree or forest evolution methods, and ensuring spec-
tral stability. The goal is to move from static pipelines to the
evolution of topologically stable multi-agent ecosystems.
In particular, automated methods for discovering optimal
DAG topologies, routing mechanisms that scale gracefully
with agent count, and topology-aware evaluation protocols
that attribute failures to specific graph components are all
pressing open problems.
7. Conclusion
This paper challenges the dogma of monolithic scaling,
identifying Agentic AI as the superior pathway to AGI. By
formalizing real-world task distributions as unions of low-
dimensional manifolds, we prove that monolithic models
are trapped in an irreducible compromise, the Average Trap,
where conflicting optimization landscapes force a penalty
that accumulates with task diversity. In contrast, even a
merely routing-based Agentic AI achieves exponentially
superior sample and parameter efficiency by aligning its
architecture with the intrinsic manifold structure, where
each agent operates on a low-dimensional sub-manifold
(dk ≪D ) rather than the full ambient space. We further
extend this analysis to general Agentic AI formalized as
DAG topologies, introducing the Compositional Capacity
C(G) and Edge Weight decomposition W(e∗) as princi-
pled tools for analyzing and designing multi-agent systems.
Importantly, we show that the agentic advantage degrades
gracefully under partial task overlap and that an optimal
agent granularity K∗ exists, balancing specialization gains
against routing costs. We also clarify the relationship be-
tween Agentic AI and Mixture-of-Experts, and that cur-
rent multi-agent failures stem from poor topological design
rather than fundamental flaws. Ultimately, we conclude that
achieving AGI requires shifting from brute-force scaling to
the precise optimization of stable, well-designed Agentic
AI ecosystems.
9

## Page 10

Position: Agentic AI System Is a Foreseeable Pathway to AGI
Acknowledgements
This work was supported by National Natural Science Foun-
dation of China (62322603) and Shanghai Municipal Spe-
cial Program for Basic Research on General AI Foundation
Models (Grant No. 2025SHZDZX025D08).
References
Agashe, S., Fan, Y ., Reyna, A., and Wang, X. E. LLM-
coordination: Evaluating and analyzing multi-agent coor-
dination abilities in large language models. In Chiruzzo,
L., Ritter, A., and Wang, L. (eds.),Findings of the As-
sociation for Computational Linguistics: NAACL 2025,
pp. 8038–8057, Albuquerque, New Mexico, April 2025.
Association for Computational Linguistics. ISBN 979-
8-89176-195-7. doi: 10.18653/v1/2025.findings-naacl.
448. URL https://aclanthology.org/2025.
findings-naacl.448/.
Ag¨uera y Arcas, B. and Norvig, P. Artificial general intelli-
gence is already here. Noema Magazine, October 2023.
Accessed: 2026-01-24.
Anthropic. Claude Code. https://claude.com/
product/claude-code, 2024. Accessed: 2026-01-
17.
Anthropic. Building a multi-agent research system. https:
//www.anthropic.com/engineering/
multi-agent-research-system , 2025. Ac-
cessed: 2026-01-17.
Battaglia, P., Hamrick, J. B. C., Bapst, V ., Sanchez, A.,
Zambaldi, V ., Malinowski, M., Tacchetti, A., Raposo, D.,
Santoro, A., Faulkner, R., Gulcehre, C., Song, F., Ballard,
A., Gilmer, J., Dahl, G. E., Vaswani, A., Allen, K., Nash,
C., Langston, V . J., Dyer, C., Heess, N., Wierstra, D.,
Kohli, P., Botvinick, M., Vinyals, O., Li, Y ., and Pascanu,
R. Relational inductive biases, deep learning, and graph
networks.arXiv, 2018. URL https://arxiv.org/
pdf/1806.01261.pdf.
Bellman, R., Bellman, R., and Corporation, R.Dynamic
Programming. Rand Corporation research study. Prince-
ton University Press, 1957. URL https://books.
google.com/books?id=rZW4ugAACAAJ.
Chollet, F. On the measure of intelligence, 2019. URL
https://arxiv.org/abs/1911.01547.
Daniely, A., Sabato, S., Ben-David, S., and Shalev-Shwartz,
S. Multiclass learnability and the ERM principle. In
Kakade, S. M. and von Luxburg, U. (eds.),Proceed-
ings of the 24th Annual Conference on Learning The-
ory, volume 19 ofProceedings of Machine Learning
Research, pp. 207–232, Budapest, Hungary, 09–11 Jun
2011. PMLR. URL https://proceedings.mlr.
press/v19/daniely11a.html.
Dauphin, Y . N., Pascanu, R., Gulcehre, C., Cho, K., Gan-
guli, S., and Bengio, Y . Identifying and attacking the
saddle point problem in high-dimensional non-convex op-
timization. InAdvances in Neural Information Processing
Systems (NIPS), volume 27, pp. 2933–2941, 2014.
Dohmatob, E., Feng, Y ., Yang, P., Charton, F., and Kempe, J.
A tale of tails: model collapse as a change of scaling laws.
InProceedings of the 41st International Conference on
Machine Learning, ICML’24. JMLR.org, 2024.
Fedus, W., Zoph, B., and Shazeer, N. Switch Transformers:
Scaling to trillion parameter models with simple and ef-
ficient sparsity.Journal of Machine Learning Research,
23(120):1–39, 2022.
Gudwin, R. Evaluating intelligence: a computational semi-
otics perspective. InSmc 2000 conference proceed-
ings. 2000 ieee international conference on systems, man
and cybernetics. ’cybernetics evolving to systems, hu-
mans, organizations, and their complex interactions’
(cat. no.0, volume 3, pp. 2080–2085 vol.3, 2000. doi:
10.1109/ICSMC.2000.886422.
Hoffmann, J., Borgeaud, S., Mensch, A., Buchatskaya, E.,
Cai, T., Rutherford, E., de Las Casas, D., Hendricks,
L. A., Welbl, J., Clark, A., Hennigan, T., Noland, E.,
Millican, K., van den Driessche, G., Damoc, B., Guy, A.,
Osindero, S., Simonyan, K., Elsen, E., Vinyals, O., Rae,
J., and Sifre, L. An empirical analysis of compute-optimal
large language model training. In Koyejo, S., Mohamed,
S., Agarwal, A., Belgrave, D., Cho, K., and Oh, A. (eds.),
Advances in Neural Information Processing Systems, vol-
ume 35, pp. 30016–30030. Curran Associates, Inc., 2022.
Horst, J. A native intelligence metric for artificial systems.
InProceedings of the Performance Metrics for Intel-
ligent Systems (PerMIS) Workshop. National Institute
of Standards and Technology (NIST), 2002. URL
https://tsapps.nist.gov/publication/
get_pdf.cfm?pub_id=824478. Accessed:
2026-01-25.
Hu, E. J., Shen, Y ., Wallis, P., Allen-Zhu, Z., Li, Y ., Wang,
S., Wang, L., and Chen, W. LoRA: Low-rank adaptation
of large language models. InInternational Conference
on Learning Representations, 2022. URL https://
openreview.net/forum?id=nZeVKeeFYf9.
Jiang, H. and Li, Q. Approximation rate of the Transformer
architecture for sequence modeling. In Globerson, A.,
Mackey, L., Belgrave, D., Fan, A., Paquet, U., Tomczak,
J., and Zhang, C. (eds.),Advances in Neural Information
Processing Systems, volume 37, pp. 68926–68955. Cur-
ran Associates, Inc., 2024. doi: 10.52202/079017-2202.
10

## Page 11

Position: Agentic AI System Is a Foreseeable Pathway to AGI
Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press,
O., and Narasimhan, K. R. SWE-bench: Can language
models resolve real-world GitHub issues? InThe Twelfth
International Conference on Learning Representations,
2024. URL https://openreview.net/forum?
id=VTF8yNQM66.
Jin, Y . Upper bounds on the Natarajan dimensions of some
function classes. In2023 IEEE International Symposium
on Information Theory (ISIT), pp. 1020–1025, 2023. doi:
10.1109/ISIT54713.2023.10206618.
Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B.,
Chess, B., Child, R., Gray, S., Radford, A., Wu, J.,
and Amodei, D. Scaling laws for neural language mod-
els, 2020. URL https://arxiv.org/abs/2001.
08361.
Keskar, N. S., Mudigere, D., Nocedal, J., Smelyanskiy, M.,
and Tang, P. T. P. On large-batch training for deep learn-
ing: Generalization gap and sharp minima. InInterna-
tional Conference on Learning Representations (ICLR),
2017.
Langley, P. Crafting papers on machine learning. In Langley,
P. (ed.),Proceedings of the 17th International Conference
on Machine Learning (ICML 2000), pp. 1207–1216, Stan-
ford, CA, 2000. Morgan Kaufmann.
Legg, S. and Hutter, M. Universal intelligence: A definition
of machine intelligence, 2007. URL https://arxiv.
org/abs/0712.3329.
Lepikhin, D., Lee, H., Xu, Y ., Chen, D., Firat, O., Huang, Y .,
Krikun, M., Shazeer, N., and Chen, Z. GShard: Scaling
giant models with conditional computation and automatic
sharding. InInternational Conference on Learning Rep-
resentations (ICLR), 2021.
Liu, B., Liu, X., Jin, X., Stone, P., and Liu, Q. Conflict-
averse gradient descent for multi-task learning.Advances
in Neural Information Processing Systems, 34, 2021.
Manus. Manus: The general purpose AI agent. https:
//manus.im/, 2024. Accessed: 2026-01-17.
Mialon, G., Fourrier, C., Wolf, T., LeCun, Y ., and Scialom,
T. GAIA: a benchmark for general AI assistants. InThe
Twelfth International Conference on Learning Represen-
tations, 2024. URL https://openreview.net/
forum?id=fibxvahvs3.
Natarajan, B. K. On learning sets and functions.Mach.
Learn., 4(1):67–97, October 1989. ISSN 0885-6125.
doi: 10.1023/A:1022605311895. URL https://doi.
org/10.1023/A:1022605311895.
OpenAI. OpenAI Codex. https://chatgpt.com/
codex, 2024. Accessed: 2026-01-17.
Pan, M. Z., Cemri, M., Agrawal, L. A., Yang, S., Chopra, B.,
Tiwari, R., Keutzer, K., Parameswaran, A., Ramchandran,
K., Klein, D., Gonzalez, J. E., Zaharia, M., and Stoica, I.
Why do multiagent systems fail? InICLR 2025 Workshop
on Building Trust in Language Models and Applications,
2025. URL https://openreview.net/forum?
id=wM521FqPvI.
Patil, S. G., Mao, H., Cheng-Jie Ji, C., Yan, F., Suresh, V .,
Stoica, I., and E. Gonzalez, J. The Berkeley function
calling leaderboard (BFCL): From tool use to agentic
evaluation of large language models. InForty-second
International Conference on Machine Learning, 2025.
Pearce, T. and Song, J. Reconciling Kaplan and Chin-
chilla scaling laws.Transactions on Machine Learning
Research, 2024. ISSN 2835-8856. URL https://
openreview.net/forum?id=NLoaLyuUUF. Re-
producibility Certification.
Phan, L., Gatti, A., Han, Z., Li, N., Hu, J., Zhang, H., Zhang,
C. B. C., Shaaban, M., Ling, J., Shi, S., et al. Humanity’s
last exam, 2025. URL https://arxiv.org/abs/
2501.14249.
Porian, T., Wortsman, M., Jitsev, J., Schmidt, L., and Car-
mon, Y . Resolving discrepancies in compute-optimal
scaling of language models. In Globerson, A., Mackey,
L., Belgrave, D., Fan, A., Paquet, U., Tomczak, J., and
Zhang, C. (eds.),Advances in Neural Information Pro-
cessing Systems, volume 37, pp. 100535–100570. Curran
Associates, Inc., 2024. doi: 10.52202/079017-3189.
Reed, S., Zolna, K., Parisotto, E., Colmenarejo, S. G.,
Novikov, A., Barth-maron, G., Gim ´enez, M., Sulsky,
Y ., Kay, J., Springenberg, J. T., Eccles, T., Bruce, J.,
Razavi, A., Edwards, A., Heess, N., Chen, Y ., Had-
sell, R., Vinyals, O., Bordbar, M., and de Freitas, N.
A generalist agent.Transactions on Machine Learning
Research, 2022. ISSN 2835-8856. URL https://
openreview.net/forum?id=1ikK0kHjvj. Fea-
tured Certification, Outstanding Certification.
Sapkota, R., Roumeliotis, K. I., and Karkee, M. AI agents
vs. agentic AI: A conceptual taxonomy, applications and
challenges.Information Fusion, 126:103599, February
2026. ISSN 1566-2535. doi: 10.1016/j.inffus.2025.
103599. URL http://dx.doi.org/10.1016/j.
inffus.2025.103599.
Shazeer, N., Mirhoseini, A., Maziarz, K., Davis, A., Le,
Q., Hinton, G., and Dean, J. Outrageously large neural
networks: The sparsely-gated mixture-of-experts layer.
InInternational Conference on Learning Representations
(ICLR), 2017.
11

## Page 12

Position: Agentic AI System Is a Foreseeable Pathway to AGI
Stone, C. J. Optimal Global Rates of Convergence
for Nonparametric Regression.The Annals of Statis-
tics, 10(4):1040 – 1053, 1982. doi: 10.1214/aos/
1176345969. URL https://doi.org/10.1214/
aos/1176345969.
Vapnik, V . N. and Chervonenkis, A. Y . On the uniform
convergence of relative frequencies of events to their
probabilities.Theory of Probability & Its Applications, 16
(2):264–280, 1971. doi: 10.1137/1116025. URL https:
//doi.org/10.1137/1116025.
Wang, Z.Mitigating Negative Transfer for Better
Generalization and Efficiency in Transfer Learning.
PhD thesis, Carnegie Mellon University, Pitts-
burgh, PA, 2021. URL https://www.lti.cs.
cmu.edu/people/alumni/alumni-thesis/
wang-zirui-edward-thesis.pdf.
Wolpert, D. and Macready, W. No free lunch theorems for
optimization.IEEE Transactions on Evolutionary Com-
putation, 1(1):67–82, 1997. doi: 10.1109/4235.585893.
Yu, T., Kumar, S., Gupta, A., Levine, S., Hausman, K.,
and Finn, C. Gradient surgery for multi-task learning.
InProceedings of the 34th International Conference on
Neural Information Processing Systems, NIPS ’20, Red
Hook, NY , USA, 2020. Curran Associates Inc. ISBN
9781713829546.
Yun, C., Bhojanapalli, S., Rawat, A. S., Reddi, S., and
Kumar, S. Are Transformers universal approximators of
sequence-to-sequence functions? InInternational Confer-
ence on Learning Representations, 2020. URL https:
//openreview.net/forum?id=ByxRM0Ntvr.
Zhang, S., Yin, M., Zhang, J., Liu, J., Han, Z., Zhang,
J., Li, B., Wang, C., Wang, H., Chen, Y ., and Wu, Q.
Which agent causes task failures and when? on automated
failure attribution of LLM multi-agent systems. InForty-
second International Conference on Machine Learning,
2025. URL https://openreview.net/forum?
id=GazlTYxZss.
Zhang, Z., Shen, J., Cao, C., Dai, G., Zhou, S., Zhang, Q.,
Zhang, S., and Shutova, E. Proactive gradient conflict
mitigation in multi-task learning: A sparse training per-
spective, 2024. URL https://arxiv.org/abs/
2411.18615.
12

## Page 13

Position: Agentic AI System Is a Foreseeable Pathway to AGI
A. Proofs for Theorems
A.1. Proof of Proposition 3.3
Proof.Sinceθ ∗
mono is a minimizer of the total convex lossL total, it satisfies the first-order optimality condition:
∇Ltotal(θ∗
mono) =
KX
k=1
αk∇Lk(θ∗
mono) = 0
This implies that the weighted gradients sum to zero. Unless all θ∗
k are identical, for any specific task k, ∇Lk(θ∗
mono)̸= 0 .
Geometrically, θ∗
mono lies within the convex hull of the individual optima {θ∗
k}K
k=1 but coincides with none. Thus, the
monolithic solution is a compromise, merely a Pareto stationary point where gradients cancel out destructively.
We expand the loss Lk(θ) for each task around its specific optimum θ∗
k. By Assumption 3.1, ∇Lk(θ∗
k) = 0. Using the
Lagrangian form of the Taylor expansion, we have:
Lk(θ∗
mono) =L k(θ∗
k) + 1
2(θ∗
mono −θ ∗
k)⊤Hk(θ∗
mono −θ ∗
k) +R 3(θ∗
mono, θ∗
k)
where R3 is the third-order remainder term. Under the assumption of ρ-Lipschitz Hessian (Assumption 3.2), this remainder
is bounded by|R 3| ≤ρ
6 ∥θ∗
mono −θ ∗
k∥3.
Substituting this back into the total risk objective:
Ltotal(θ∗
mono) =
KX
k=1
αk

Lk(θ∗
k) + 1
2∥θ∗
mono −θ ∗
k∥2
Hk +R (k)
3

=
KX
k=1
αkLk(θ∗
k)
| {z }
Lideal
+
KX
k=1
αk
2 ∥θ∗
mono −θ ∗
k∥2
Hk +
KX
k=1
αk|R(k)
3 |
| {z }
Higher-order error
To guarantee that the interference cost ϵ is significant, the quadratic term must dominate the third-order error. Since ∥ · ∥2
Hk
scales with ∆2 while the error scales with ∆3, for a local neighborhood around the optima where the task divergence is
bounded, the positive curvature (guaranteed by positive definite Hk) strictly dominates the higher-order variations. Thus, we
derive the lower bound:
Ltotal(θ∗
mono)≳L ideal +
KX
k=1
αk
2 ∥θ∗
mono −θ ∗
k∥2
Hk
This confirms that ϵ >0 holds as long as the conflicting gradients force θ∗
mono away from individual optima, creating an
irreducible quadratic penalty.
A.2. Proof of Lemma 4.2
Proof.Since agents are topologically sorted,Jis strictly lower triangular and nilpotent.
By the multivariate chain rule, the total variation dxj
dxi
captures the cumulative effect of agenti on agent j throughallpossible
paths.
dxj
dxi
= ∂xj
∂xi|{z}
Direct edge
+
X
k∈Pa(j),k̸=i
∂xj
∂xk|{z}
Direct path
· dxk
dxi|{z}
Recursive path
=
X
k
∂xj
∂xk|{z}
Jjk
dxk
dxi|{z}
Mki
Then we define M∈R K×K be theInfluence Matrixwhere Mji = dxj
dxi
. The recursive relation can be written in matrix
form:
M=JM+I
Here,Iis defined as the self-influenceI ii = dxi
dxi
and anywhere else0. Then, rearranging forM:
(I−J)M=I=⇒M= (I−J) −1
13

## Page 14

Position: Agentic AI System Is a Foreseeable Pathway to AGI
SinceJis nilpotent (due to the acyclic property of DAGs), this inverse can be expanded as a Neumann Series:
M=
K−1X
k=0
Jk =I+J+J 2 +. . .
Physically, Jk represents the influence propagation along paths of length exactlyk. The matrix M mathematically aggregates
all parallel and serial paths automatically. Then, we can derive the topological weight of a specific agent in the DAG.
Let g= [∥ ∂L
∂x1
∥, . . . ,∥∂L
∂xK
∥]T be the gradient of the loss with respect to agent outputs (typically non-zero only for sink
agents). The total sensitivity ofLto a specific agentuis theu-th component of:
ω=M T g
The scalar Topological Weightωu for agentuis explicitly:
ωu =

dL
dxu
 =

X
v∈Sinks
∂L
∂xv
X
ρ∈Paths(u→v)


Y
(a,b)∈ρ
Jba
| {z }
Weight of pathρ



A.3. Proof of Lemma 4.4
Proof. The weight is derived by tracing the full back-propagation path of the loss gradient through the specific edge e∗. The
total influence is the product of the signal magnitude reaching the parent u and the distribution of that signal to all upstream
ancestors.
First, we isolate the incoming gradient signal from the child v. By the chain rule, the gradient at u contributed strictly by v
is ∂L
∂xv
Je∗. The magnitude of this local flux is:
∥Fluxv→u∥ ≤ ∥Je∗∥ ·

∂L
∂xv
 =∥J e∗∥ ·ωv
Second, we account for the propagation of this flux to the past. The signal distributes to u itself (identity gain) and to every
predecessork∈ P(u). The cumulative amplification factor is the sum of path gains:
Upstream Mass=∥I∥+
X
k∈P(u)

X
ρ∈Path(k→u)
Y
e∈ρ
Je

Third, we expand the downstream sensitivity ωv. The total gradient ∂L
∂xv
is the aggregation of error signals back-propagated
from all reachable sink nodesz. Expanding the influence matrixM zv = dxz
dxv
as a sum over all pathsγ:
ωv =

X
z∈Sinks
∂L
∂xz
dxz
dxv
 =

X
z∈Sinks
∂L
∂xz
X
γ∈Path(v→z)
Y
e′∈γ
Je′

Multiplying these three components, Upstream Mass, Local Valve (Je∗), and expanded Downstream Sensitivity, yields the
complete Topological Edge Weight definition.
B. Some Relevant Remarks
B.1. Remark for Section 3.1
RemarkB.1 (Data-Abundant Regime).It is crucial to distinguish our theoretical setup from typical few-shot transfer learning
or low-resource multi-task learning scenarios. We assume a data-abundant regime distinct from low-resource settings,
allowing models to reach convergence.
14

## Page 15

Position: Agentic AI System Is a Foreseeable Pathway to AGI
RemarkB.2 (Alignment with Negative Transfer in Multi-Task Learning).The proposition of the Average Trap is consistent
with the Negative Transfer in Multi-Task Learning, which states that when the gradient direction of task A makes an angle
greater than 90 degrees with the gradient direction of task B, updating parameters by one step will simultaneously impair the
performance of one or both tasks (Wang, 2021). Though researchers have been finding ways to mitigate the effect (Yu et al.,
2020; Zhang et al., 2024), theϵterm in the Average Trap is an unavoidable constraint.
RemarkB.3 (When Is the Average Trap Binding?).The magnitude of the Average Trap penalty ϵ= PK
k=1
αk
2 ∥θ∗
mono −
θ∗
k∥2
Hk depends on both the number of tasks K and the curvature Hk. For narrow task families (small K, closely related
tasks), the penalty is mild: the task-optimal parameters θ∗
k cluster tightly, and the monolithic compromise remains near
each individual optimum. However, the penalty becomes increasingly binding as the task distribution broadens toward
AGI-level generality. First, ϵ accumulates with K as the monolithic optimum must compromise across more divergent
directions. Second, the effective ambient dimension D of the union manifold SMk grows with K, exacerbating the curse
of dimensionality captured by Equation (3). This explains why monolithic models succeed on narrow benchmarks but
progressively degrade on diverse leaderboards: the Average Trap transitions from a negligible correction to a dominant
constraint precisely in the regime this paper targets.
B.2. Remark for Assumption 3.1
RemarkB.4 (Non-convexity of Neural Networks).As is well known, the loss surface of deep neural networks is non-convex,
filled with saddle points and flat minima (Dauphin et al., 2014; Keskar et al., 2017). Even against a non-convex background,
the conclusion still holds as long as conflicting gradient components exist (Liu et al., 2021).
B.3. Remark for Section 3.2
RemarkB.5 (LLMs as Non-parametric Estimators).While LLMs are parameterized by a finite set of weights, they operate
in the “over-parameterized” regime where they function as universal approximators. In the context of complex task solving,
we treat the LLM as a non-parametric estimator ˆfN attempting to learn the target function f:R D →R solely from data.
Thus, the minimax lower bounds regarding sample complexity and dimensionality directly apply to the generalization
capabilities of LLMs.
RemarkB.6 (Data Abundance via Interaction).It is worth noting that, in the context of Agentic AI, the assumption of
limited Nrouter is often relaxed. Unlike static datasets, agents can continuously interact with the environment (the real
world) to generate feedback. This online data generation capability implies that Nrouter can be effectively infinite (N→ ∞),
mitigating the sample complexity of neural routers and allowing the system to leverage their superior expressivity.
B.4. Remark for Assumption 3.4
RemarkB.7 (Graceful Degradation under Partial Overlap).Assumption 3.4 posits near-orthogonal task subspaces, which
serves as a best-case analysis establishing the ceiling of the agentic advantage. In practice, tasks often share partial
underlying structure. We formalize this relaxation by introducing an overlap parameterγ= dim(S shared)/dmax ∈[0,1].
Each task’s feature subspace decomposes as Sk =S shared ⊕S res
k , where Sshared is the common subspace across all tasks
withdim(S shared) =γ·d max, andS res
k captures task-specific residuals withS res
j ⊥S res
k forj̸=k.
In the shared subspace, all tasks agree on a common optimum (zero penalty). In the residual subspace, the full divergence
applies. The penalty from Proposition 3.3 therefore becomes:
ϵ(γ)≈(1−γ)·ϵ full
whereϵ full is the penalty under full divergence (γ= 0).
The sample complexity ratio (Equation (3)) generalizes to:
NR-Agentic
Nmono
∝K dmax ·ϵ (1−γ)(D−dmax)
The exponent shrinks linearly withγbut remains strictly negative for anyγ <1, preserving the exponential advantage.
The mismatch penalty (Lemma 3.5) generalizes to:
∆max(K, γ)≈Lmax ·(1−γ)·

1− 1√
K

15

## Page 16

Position: Agentic AI System Is a Foreseeable Pathway to AGI
At γ= 0 (full separation), the original results are recovered exactly. At γ >0, the advantage degrades smoothly but remains
strictly positive for all γ <1. At γ= 1 (complete overlap), the system reduces to the monolithic case, confirming that
agentic decomposition provides a strict generalization of monolithic learning.
16
