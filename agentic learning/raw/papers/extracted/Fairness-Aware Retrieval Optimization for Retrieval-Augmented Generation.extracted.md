# Fairness-Aware Retrieval Optimization for Retrieval-Augmented Generation - Extracted Text

- Source note: [[Fairness-Aware Retrieval Optimization for Retrieval-Augmented Generation]]
- Source PDF: `assets/Fairness-Aware Retrieval Optimization for Retrieval-Augmented Generation.pdf`
- Extracted: 2026-05-18
- Extractor: pypdf
- Pages: 40
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

Fairness-Aware Retrieval Optimization for
Retrieval-Augmented Generation
Yingqi Zhaoa, Vasilis Efthymioub, Jyrki Nummenmaaa, Kostas Stefanidisa
aData Science Research Centre, Tampere University, Tampere, Finland
bHarokopio University of Athens, Athens, Greece
Abstract
Retrieval-Augmented Generation (RAG) improves reliability of large lan-
guage models by incorporating external knowledge, but the retrieval pro-
cess can introduce bias that propagates to generated outputs. This issue is
particularly challenging in top-ksettings, where multiple documents jointly
influence generation. We propose a fairness-aware retrieval framework that
models and controls this bias. Our approach combines controlled bias in-
jection via reranking, a position-aware model of bias propagation, and an
optimization formulation that balances relevance and fairness. We further in-
troduce a scalable solution based on Quadratic Fairness via Dual Hyperplane
Approximation (FARO), which enables efficient optimization through prob-
lem decomposition. Experimental results show that our method effectively
mitigates generation bias while preserving relevance. This work provides a
principled approach for fairness-aware retrieval in RAG systems.
Keywords:Retrieval-Augmented Generation (RAG), Fairness-Aware
Retrieval, Bias Propagation, Fair Ranking.
1. Introduction
Recent advances in Large Language Models (LLMs) have significantly im-
proved the ability of artificial intelligence systems to generate coherent and
contextually relevant text [1, 2]. Despite their success, LLMs often suffer
Email addresses:yingqi.zhao@tuni.fi(Yingqi Zhao),vefthym@hua.gr(Vasilis
Efthymiou),jyrki.nummenmaa@tuni.fi(Jyrki Nummenmaa),
konstantinos.stefanidis@tuni.fi(Kostas Stefanidis)
arXiv:2605.15790v1  [cs.DB]  15 May 2026

## Page 2

from hallucinations and factual inconsistencies, limiting their reliability in
real-world applications [3]. Retrieval-Augmented Generation (RAG) [4] has
emerged as an effective paradigm to address these limitations by incorporat-
ing external knowledge into the generation process. By retrieving relevant
documents and feeding them to the language model as a part of the input,
RAG enhances factual grounding and improves answer quality.
However, while RAG mitigates hallucinations, it also introduces new chal-
lenges related to fairness and bias. In particular, the selection and ordering
of retrieved documents can significantly influence the generated output, po-
tentially amplifying biases present in the underlying knowledge sources or
retrieval mechanisms. As a result, even when the language model itself does
not exhibit significant bias, biased retrieval can lead to systematically skewed
responses [5, 6]. This issue is especially pronounced in top-kRAG settings,
where multiple documents jointly contribute to the final output, creating
complex interactions that are difficult to analyze and control.
Existing research has explored bias in LLMs [7] and fairness in ranking
systems [8], but these lines of work remain largely disconnected. Studies on
LLM bias primarily focus on measuring or mitigating bias through prompt
engineering, fine-tuning, or dataset curation, without explicitly considering
the potential of RAG [9]. Conversely, fairness-aware ranking methods aim
to ensure equitable exposure of items or providers, but do not account for
how ranking decisions affect downstream text generation [10]. Consequently,
thereisalackofprincipledapproachesforcontrollinggenerationbiasthrough
retrieval decisions in RAG systems.
A key challenge lies in understanding how bias propagates from retrieved
documents to generated outputs. While prior work has identified a linear re-
lationship between embedding bias and output bias in top-1 settings [11, 12],
this assumption does not directly extend to top-kretrieval, where multiple
documents with different positions jointly influence the generation process.
Modeling this position-dependent interaction is essential for designing effec-
tive fairness-aware retrieval strategies.
In this work, we address this challenge by introducing a unified frame-
work for fairness-aware retrieval in top-kRAG systems. Our approach is
based on the insight that generation bias can be controlled by manipulating
the bias of retrieved documents and understanding how this bias propagates
through the model. To this end, we propose a three-stage framework. First,
we introduce a reranker-based mechanism that enables controlled bias injec-
tion by adjusting the group distribution of retrieved documents. Second, we
2

## Page 3

develop a position-aware bias propagation model that captures how bias at
different retrieval positions influences the final output. Third, we formulate
fairness-aware retrieval as an optimization problem and propose an efficient
solution that balances relevance and fairness.
Building on this formulation, we further introduce a scalable optimization
framework based on Quadratic Fairness via Dual Hyperplane Approximation
(FARO). This approach transforms a globally coupled fairness optimization
problem into a set of independent subproblems, enabling efficient computa-
tion while preserving the ability to explore trade-offs between relevance and
fairness. By leveraging the learned bias propagation model, our method di-
rectly links retrieval decisions to generation outcomes, providing a principled
mechanism for bias control in RAG systems.
We evaluate our approach on multiple datasets and models, considering
both political and gender bias settings. The experimental results demon-
strate that our method effectively reduces generation bias while maintaining
competitive relevance performance. Furthermore, the proposed optimization
framework offers flexibility in navigating the relevance–fairness trade-off.
Overall, we propose an end-to-end three-stage framework for fairness-
aware retrieval optimization in RAG systems. Our approach integrates con-
trolledbiasinjection, position-awaremodelingofbiaspropagation, andfairness-
aware optimization of retrieval decisions. The framework provides a princi-
pled and scalable solution for balancing relevance and fairness in top-kRAG
settings. The main contributions of this work are:
•We propose a reranker-based pipeline for controlled bias injection, en-
abling precise manipulation of embedding bias without modifying the
underlying retriever.
•We introduce a position-aware bias propagation model that captures
how retrieved documents influence generation bias in top-kRAG sys-
tems.
•We formulate fairness-aware retrieval as an optimization problem and
develop a scalable solution (FARO) that balances relevance and fair-
ness.
•We conduct extensive experiments demonstrating the effectiveness of
our approach across different models and bias settings.
3

## Page 4

The remainder of the paper is structured around the proposed fairness-
aware retrieval pipeline. Section 2 reviews related work on bias in RAG sys-
tems and fairness-aware ranking. Section 3 introduces the overall three-stage
framework and formalizes the problem setting. Section 4 develops a position-
aware model of bias propagation, capturing how retrieved documents jointly
influence generated outputs. Section 5 formulates fairness-aware retrieval
as an optimization problem and presents the FARO framework for scalable
solution. Section 6 presents the experimental setup, and Section 7 reports
experimental results, including validation of the bias propagation model and
evaluation of the proposed optimization approach. Finally, Section 8 con-
cludes the paper with a summary of our contributions.
2. Related Work
2.1. Bias Introduction and Mitigation in RAG
AlthoughRetrieval-AugmentedGeneration(RAG)hasbeenwidelyadopted
to improve the performance of Large Language Models (LLMs) and reduce
hallucinations, recent studies have shown that it may also introduce or am-
plify bias in generated outputs. Hu et al. [5] propose a three-stage fairness-
awareframeworkbycontrollingtheproportionofbiasedcontentintheknowl-
edge base. Their findings show that even a small amount of biased informa-
tion can significantly influence model outputs, and that RAG may amplify
such biases. Moreover, even when retrieved knowledge appears unbiased, it
can still degrade the alignment behavior of LLMs.
Wu et al. [6] conduct extensive ablation studies to analyze how different
RAG components, such as the retriever, generator, refiner, and judger, affect
bias in generated outputs. Their results indicate that both the retriever and
the generator are primary contributors to bias, highlighting the importance
of interactions across components. Similarly, Zhang et al. [13] demonstrate
that retrieval strategies have a significant impact on bias, and show that this
effect persists across multiple languages, including Chinese and Japanese.
A key step toward understanding bias in RAG is the identification of bias
propagation mechanisms. Kim et al. [11] are the first to reveal a linear re-
lationship between embedding bias and output bias in a top-1 RAG setting.
By fine-tuning the retriever, they control the bias distribution of retrieved
documents and, through this relationship, influence the downstream gener-
ation behavior. However, this approach presents important limitations. On
the one hand, reliance on black-box embedding models introduces additional
4

## Page 5

uncertainty and makes it difficult to achieve precise control over retrieval
outcomes, even in the top-1 setting, while also limiting extension to top-kre-
trieval scenarios. On the other hand, fine-tuning the embedding model intro-
duces substantial cost, requiring dataset construction and retriever training,
as well as repeated experiments to estimate the bias relationship.
To address these limitations, our previous work [12] proposes a reranker-
based approach that directly controls embedding bias through probabilistic
selection. This method reduces deployment cost, simplifies implementation,
and enables more precise manipulation of bias in retrieved documents. Build-
ing upon this line of work, we extend the analysis from top-1 to top-kRAG
settings. This extension is crucial for real-world applications, where mul-
tiple documents jointly influence the generated output. While prior work
(e.g., [14]) has studied attention patterns in long-context LLMs, relatively
little research has examined how bias propagates across multiple retrieved
documents. In contrast, our work explicitly models position-dependent bias
propagation and leverages it for bias mitigation.
It is worth noting that there are other works on fairness-aware ranking
in RAG, such as [15], focusing on the fair presentation of retrieved rele-
vant items, thereby enabling the generator to reference its sources in a bal-
anced manner; [16] instead examines whether question associated with cer-
tain groups within a specific fairness category systematically achieve higher
accuracy, and studies the roles of exposure, utility, and attribution bias.
These approaches define and evaluate fairness in RAG along a different di-
mension from ours, and we therefore do not discuss them here.
2.2. Fairness-Aware Ranking and Optimization
The optimization framework proposed in this work is related to prior
studies on fairness-aware ranking, particularly in recommender systems and
information retrieval. FA*IR [17] introduces one of the earliest approaches
to fair top-kranking, enforcing statistical fairness constraints over binary
groups. Singh et al. [10] further highlight that ranking positions induce un-
equal exposure due to position bias, and propose aligning exposure with rel-
evance through probabilistic ranking formulations. DELTR [18] incorporates
fairness as a regularization term within learning-to-rank objectives, enabling
fairness-aware training. Additional works, such as [19] and [20], extend this
idea by integrating fairness constraints into ranking objectives using pairwise
comparisons or reinforcement learning.
5

## Page 6

Despite their relevance, these approaches are not directly applicable to
RAGsystems due tofundamental differencesin objectives. Inrecommenders,
fairnessistypicallydefinedintermsofexposureallocationtoitemsorproviders,
whereas in RAG the primary concern is the fairness of the generated out-
puts. Retrieved documents do not directly correspond to entities requiring
fair treatment; instead, they influence the generation process of the LLM.
Nevertheless, these works provide important conceptual foundations. In
particular, the notion of position-dependent exposure aligns with our obser-
vation that documents at different retrieval positions have varying influence
on the final output. This perspective allows us to reinterpret retrieval in
RAG as a ranking problem under fairness constraints, where the objective
is to balance relevance with the bias induced in the generated responses.
Building on this insight, we leverage the empirically identified linear bias
propagation model to connect retrieval decisions with generation bias. This
enables the formulation of a fairness-aware retrieval optimization problem
tailored to RAG systems, which we address in Section 5.
3. Overview of the Three-Stage Framework for Fairness-Aware Re-
trieval Optimization in RAG
3.1. Fairness in RAG Systems: Problem Setting
The notion of fairness adopted in this work is grounded in a statistical
perspective on model outputs. Specifically, we consider a set of questions,
each associated with two candidate answers. One of the candidate answers is
from one set, sayA, representing a right-oriented political view, in the case
of politics, or females in the case of sexual selection, and the other candidate
answer is from setB, representing the other political viewpoint, ie. left-
oriented in politics, or males in the case of sexual preference . Please note
that we acknowledge the view that sexual partition is not binary, however at
the same time balance in sexual preference is seen important, so in our data
is chosen in a way that there is a clear male / female division.
The set of questions are designed to be neutral and unbiased with respect
to from which candidate answer set the answer should be selected. While one
question is designed to match exactly one answer pair, there are also other
answer pairs are also related to the question, so that when looking for top-k
answers, there is a number of matching pairs.
A RAG system is considered fair if it selects answers fromAandBwith
approximately equal frequency across the question set. Systematic deviations
6

## Page 7

from this balance indicate a preference toward one group and, consequently,
bias against the other. Please note that our definition generalizes for the case
where there are more alternative answer sets, like nationalities in the case of
persons.
This definition corresponds to a form of statistical parity over generated
outputs. While simple and interpretable, it does not capture more nuanced
notions, such as individual fairness or causal fairness. Nevertheless, it pro-
vides a practical and measurable criterion for evaluating and controlling bias
in RAG systems, which is the primary objective of this work.
We focus on two representative bias types: political bias and gender bias.
For political bias, the two groups correspond to liberal and conservative view-
points. For gender bias, the groups correspond to male and female represen-
tations. In both cases, we construct neutral questions that do not admit a
unique correct answer but instead allow multiple plausible perspectives. The
RAG system is then required to select one of the provided options, enabling
us to analyze the distribution of its preferences.
For example, in the political bias setting, a question may present two
plausible viewpoints on a societal issue, each aligned with a different political
stance. In the gender bias setting, a question may ask about a notable
individual in a given domain, with answer options corresponding to different
genders. Because both options are equally valid, the aggregate selection
distribution over many such questions serves as an indicator of implicit bias
in the system. Section 6.1 provides a detailed description of the dataset
construction process and corresponding examples.
This setup allows us to systematically evaluate how bias emerges and
propagates in RAG pipelines, and provides a foundation for designing bias
mitigation strategies.
3.2. Framework Overview
We propose a three-stage framework for fairness-aware retrieval optimiza-
tion in RAG systems. The framework integrates controlled bias injection,
bias propagation modeling, and optimization-based retrieval, enabling both
the analysis and mitigation of bias in top-kRAG settings.
The key novelty of our approach lies in extending bias control from top-
1 retrieval to position-aware top-kretrieval, modeling how bias propagates
across multiple retrieved documents, and leveraging this model to guide
fairness-aware retrieval optimization. An overview of the framework is il-
lustrated in Figure 1. Given a set of bias evaluation questions and group-
7

## Page 8

partitioned knowledge bases, the frameworkproduces retrieval strategies that
balance relevance and fairness in the final generated outputs.
3.2.1. Stage 1: Controlled Bias Injection via Reranking
The first stage introduces a reranking mechanism to explicitly control
the bias of retrieved documents. RAG systems typically construct a knowl-
edge base containing rich and relevant documents, use the input question as
a query to retrieve related documents from the knowledge base, and then
aggregate their content as contextual information injected into the LLM to
improve generation quality. The central idea is to treat the bias of the re-
trieved context, referred to as embedding biasEb, as a controllable variable
that influences the final generation biasRb of the system.
To enable this control, we partition the knowledge base into group-specific
subsets (e.g., liberal vs. conservative, or female vs. male). For each question,
we independently retrieve candidate documents from each group-specific sub-
set. A probabilistic reranker is then applied to select and order documents
from these subsets when constructing the top-kretrieval list.
Unlike approaches that rely on fine-tuning the embedding model, this
design enables direct and precise manipulation of the bias distribution of
retrieved documents (for example, the proportion of liberal and conservative
viewpoints appearing at specific positions in the retrieval list for political
bias) without modifying the underlying retriever. As a result, bias control is
decoupled from the retrieval model and can be implemented as a lightweight
post-processing step when sufficient group-related documents are available.
Importantly, this mechanism allows us to control not only the overall bias
of the retrieved set, but also the bias at each position in the ranked list. We
denote the position-wise embedding bias at rankpasEp
b , which serves as the
key variable for analyzing bias propagation in subsequent stages.
3.2.2. Stage 2: Bias Propagation Modeling
The second stage aims to detect how bias in retrieved documents prop-
agates to the final generated outputs. In particular, we seek to quantify
the contribution of each position in the retrieval list to the overall system
bias. To achieve this, we treat the RAG system as a black box and per-
form controlled perturbations of position-wise embedding bias. Specifically,
we generate multiple retrieval configurations by systematically varying the
bias valuesEp
b across positions in top-kretrieval. For each configuration, we
8

## Page 9

Figure 1: Overview of the proposed three-stage framework for fairness-aware retrieval in
RAG systems. Stage 1 (top-left black box) introduces controlled bias injection through a
reranking mechanism that adjusts the group distribution of retrieved documents. Stage 2
(top-right blue box) models how position-wise embedding bias propagates to the final gen-
erated output via a linear, position-aware formulation. Stage 3 (bottom red box) leverages
this model to optimize top-k retrieval under fairness constraints, balancing relevance and
bias in the generated responses. The framework enables fine-grained, position-aware con-
trol of bias in multi-document RAG pipelines.
run the RAG system on a set of questions and measure the resulting output
biasR b.
Using the collected data, we fit a linear regression model that relates
position-wise embedding bias to the final system bias. This model captures
how bias at different positions contributes to the generated output and pro-
vides an interpretable representation of bias propagation. The resulting for-
mulation reveals that system-level bias can be approximated as a weighted
combination of position-wise embedding biases. The learned coefficients re-
flectthesensitivityofthelanguagemodeltobiassignalsatdifferentpositions,
and can be interpreted as position-dependent attention weights.
This modeling step is critical: it provides a tractable and interpretable
approximation of how multiple retrieved documents jointly influence the final
output, and serves as the foundation for the optimization stage.
3.2.3. Stage 3: Fairness-Aware Retrieval Optimization
In the final stage, we leverage the learned bias propagation model to
optimize retrieval under fairness constraints. The key idea is to treat retrieval
9

## Page 10

Table 1: Summary of the main notation.
Symbol Description
iA document in the knowledge base
qA question in a RAG experiment, representing a question in the QA dataset
Rb Bias score of final RAG outputs
Nq The set of relevant candidate documents retrieved from the knowledge
base for a question q
Eb Embedding bias score of retrieved documents in top-1 RAG
Lb The intrinsic bias score of the LLM as the generator
Ep
b Embedding bias score at rankpin the top-klist
wp Position-wise bias weight (LLM sensitivity at positionp)
ϵThe residual term in the linear model
τThe threshold for the fairness constraint
xq,i,p Denote whether documentiis assigned to positionpfor questionq
Relq,i The relevance score of documentiwith respect to questionq
as a ranking problem that balances two objectives: maximizing relevance
and controlling the bias of the final generated output. Using the linear bias
propagation model, we can express the overall system bias as a function of
the selected documents and their positions in the ranking.
Based on this formulation, we define a fairness constraint that requires
the system-level bias to remain within a predefined tolerance. At the same
time, we aim to maximize the relevance of the retrieved documents with
respect to the question. This leads to a constrained optimization problem,
where retrieval decisions directly influence both relevance and fairness.
To solve this problem efficiently, we design an optimization framework
that enables flexible trade-offs between these objectives. The framework
supports different levels of fairness constraints and can adapt to varying
application requirements, producing retrieval strategies that maintain high
relevance while mitigating bias.
Summary:We introduce an end-to-end framework for fairness-aware
retrieval optimization in top-kRAG systems. By combining controllable
bias injection, position-aware bias propagation modeling, and optimization-
based retrieval, the framework enables fine-grained control over generation
bias while preserving retrieval quality. This integrated approach provides
both analytical insights into bias behavior and practical tools for mitigating
bias in real-world RAG applications. For clarity, we summarize the main
notation used throughout the paper in Table 1.
10

## Page 11

4. Fairness in Top-kRetrieval-Augmented Generation
This section formalizes the notion of bias in RAG systems and introduces
a position-aware model for bias propagation under top-kretrieval. We begin
by revisiting the top-1 setting in Section 4.1, which provides a detailed intro-
duction to the bias evaluation metrics and reranking method, corresponding
to Stage 1 of our framework. We then extend the formulation to capture
position-dependent effects in multi-document retrieval in Section 4.2, which
presents the detailed formulation of Stage 2: Bias Propagation Modeling.
4.1. Bias Quantification in Top-1RAG
To measure bias in RAG systems, we adopt a statistical evaluation frame-
work based on Average Rank Bias, following [11].
LetSdenote a set of evaluation samples, where each samples∈Srep-
resents the output of a component in the RAG system for a given question,
such as a retrieved item or a generated textual response. We consider a
binary group setting with two groups,g1 andg 2. To provide a unified fair-
ness measure applicable across different RAG components, we define the bias
score as follows:
bias score= 1
|S|
X
s∈S
 
g1(s)−g 2(s)

,(1)
whereg x(s) = 1if the output favors groupgx and 0 otherwise. The resulting
score lies in the interval [-1,1], where values close to 1 indicate preference
towardg 1, values close to -1 indicate preference towardg2 and values near 0
indicate balanced behavior.
This formulation provides a unified metric that can be applied to different
components of the RAG pipeline. Specifically, for the overall RAG system, it
measures the output biasRb. For retrieved documents, it measures the em-
bedding biasEb by aggregating the group attributes of the retrieved relevant
documents across all queries, for example, in the top-1 retrieval setting where
each query corresponds to a single retrieved document. For the LLM acting
as the generator in RAG, it measures the intrinsic model biasLb, obtained
by directly evaluating the LLM on the bias evaluation question set without
retrieval augmentation. For the knowledge base, it captures corpus-level bias.
This unified view enables consistent analysis of how bias propagates across
system components.
11

## Page 12

Figure 2: Reranking-based mechanism for controlling embedding bias in retrieved docu-
ments. For each question, candidate documents are retrieved from group-specific subsets
and probabilistically selected using a parameterm, which determines the likelihood of
choosing documents from each group. The selected documents are then ordered to form
the top-kcontext. This process enables explicit and continuous control over position-wise
embedding bias, which serves as input to the bias propagation model.
Controlling Embedding Bias via Reranking.To analyze and miti-
gate bias, we adopt a reranker-based strategy to control the embedding bias
of retrieved documents. Specifically, we construct two group-specific candi-
date sets and introduce a probabilistic selection mechanism.
Letm∈[0,1]denote the probability of selecting a document from group
g1, which means that the probability of selecting a document from group
g2 is 1-m. Since the bias evaluation metric is based on the proportional
distribution of group attributes in the retrieval results, probability control
can equivalently be interpreted as controlling the proportions of retrieved
results, the embedding bias can be expressed as:
Eb = 2m−1(2)
This formulation enables direct and precise control over the bias of retrieved
documents without modifying the underlying retrieval model.
The reranking mechanism for controlling embedding bias is illustrated in
Figure 2, showing how documents from different groups are probabilistically
selected and ordered in the retrieved context. This design enables direct
control over the bias distribution of retrieved documents, as formalized in
Equation (2).
Bias Propagation in Top-1 RAG.[12] has shown that, in the top-1
12

## Page 13

setting, the relationship between embedding biasEb and output biasRb can
be approximated by a linear model:
Rb =w·E b +L b +ϵ,(3)
wherewis a weight captures the sensitivity of the language model to the
retrieved document,L b represents the intrinsic bias of the model, andϵis
a residual term. Based on our previous formulation, this weightwshould
generally lie within the interval[0,1]. A largerwindicates that the bias
attribute of the document at the corresponding position has a stronger in-
fluence, whereas a smallerwindicates a weaker effect. Whenw= 0, the
content at that position does not affect the generation result of the RAG
system. Whenw <0, the content at that position may have a negative effect
on the generated result, which usually suggests that redundant contextual
information interferes with the LLM’s generation. This linear formulation
can be interpreted as a first-order approximation of a more complex interac-
tion between retrieved context and model behavior. It provides a simple yet
effective abstraction for analyzing and controlling bias in RAG systems.
However, the top-1 setting is restrictive in practice. Real-world RAG
systems typically rely on top-k retrieval to provide richer contextual infor-
mation. This introduces additional complexity, as multiple documents jointly
influence the generated output.
4.2. Bias Propagation in Top-kRAG
Position-Aware Bias Modeling.In the top-ksetting, the retrieved
context consists of multiple documents, each occupying a specific position in
the input sequence. Since large language models exhibit position-dependent
attention patterns, documents at different positions may have unequal influ-
ence on the final output. To capture this effect, we introduce the notion of
position-wise embedding biasEp
b , which represents the bias of the document
at rankpin the retrieved list.
We then model the overall output bias as a function of these position-
wise contributions. Based on empirical observations, we approximate this
relationship using a linear model:
Rb =
kX
p=1
wp ·E p
b +L b +ϵ,(4)
13

## Page 14

wherew p denotes the weight associated with positionp, capturing the sen-
sitivity of the model to bias signals at that position,Lb reflects the intrinsic
bias of the language model, whileϵaccounts for residual effects.
This formulation generalizes the top-1 model and provides a tractable
framework for analyzing how multiple retrieved documents jointly influence
system-level bias.
Assumptions.The linear model above admits several useful interpre-
tations. First, it can be viewed as a weighted aggregation of bias signals
across positions, where the weightswp reflect position-dependent exposure
or attention. Second, it enables direct estimation of how changes in retrieval
decisions affect the final output bias.
The formulation relies on two key assumptions: (i) The contributions
of individual documents to the final bias are approximately additive (Ad-
ditivity); (ii) Given the question, the influence of each document is treated
as independent of others (Conditional independence). While these assump-
tions may not strictly hold due to complex interactions within the language
model, they provide a reasonable first-order approximation that balances
interpretability and modeling accuracy.
Experimental Estimation via Controlled Perturbations.To es-
timate the parameterswp, we perform controlled perturbations of position-
wise embedding bias. Specifically, we construct a set of bias configurations
by discretizing the bias space and assigning predefined values toEp
b at each
position. For each configuration, we run the RAG system on a set of ques-
tions and measure the resulting output biasRb. This process yields a dataset
of input–output pairs:
((E1
b , E2
b , . . . , Ek
b ), Rb)(5)
We then fit a linear regression model using these pairs, with(E1
b , E2
b , . . . , Ek
b )
as input variables andR b as the target. This allows us to estimate the
position-wise weightswp and the intercept termb.
To ensuresufficientcoverageof thebiasspacewhile maintaining computa-
tional tractability, we adopt symmetric discretizations of bias values at each
position. This design balances experimental coverage with the combinatorial
complexity of the grid search.
Algorithm 1 summarizes the procedure used to construct the regression
dataset for bias propagation analysis. By systematically varying the position-
wise embedding bias and observing the resulting output bias, the algorithm
generates input–output pairs that enable the estimation of the linear model
14

## Page 15

Algorithm 1:Estimation of Position-aware Bias Propagation
Input:Bias candidate setsV 2, V3, V5, question setQ, RAG systemR
Output:Regression datasetsD k, regression modelsMk
foreachk∈ {2,3,5}do
Dk ← ∅;
Gk ←V 1
k ×V 2
k × ··· ×Vk
k ;
foreachS Eb = (E1
b , . . . , Ek
b )∈ Gk do
m←ComputeProbabilities(S Eb);
D←Rerank(m, k);
Rb ←EvaluateBias(R, Q, D);
Dk ← Dk ∪ {((E1
b , . . . , Ek
b ), Rb)};
Mk ←LinearRegression(D k);
in Equation (4). This process allows us to quantify the contribution of each
retrieval position to the overall system bias.
Empirical Validation of the Linear Model.Across different models,
bias types, and values ofk, we observe a strong linear relationship between
position-wise embedding bias and output bias. The linear model provides a
good fit to the empirical data, supporting its suitability as an approximation
of bias propagation in top-kRAG systems.
The learned weightsw p reveal how different models allocate attention
across positions. For example, some models place greater emphasis on early
positions, while others distribute attention more evenly or exhibit sensitiv-
ity to later positions. Interestingly, in certain settings, we observe negative
weights for specific positions. This suggests that documents at those posi-
tions may counteract bias signals, possibly due to redundancy or conflicting
contextual information. Such patterns highlight the complex interplay be-
tween context structure and model behavior.
Discussion.The proposed linear bias propagation model provides a
unified and interpretable framework for analyzing fairness in RAG systems.
By capturing position-dependent effects, it extends prior work beyond the
top-1 setting and enables fine-grained control over bias in multi-document
retrieval. At the same time, the model has inherent limitations. It abstracts
away higher-order interactions between documents and relies on a simplified
representation of bias. Moreover, it assumes binary group attributes and
does not directly extend to more complex or multi-dimensional notions of
fairness. Despite these limitations, the model strikes a practical balance
15

## Page 16

between expressiveness and tractability. Crucially, it serves as the foundation
fortheoptimizationframeworkintroducedinthenextsection, whereretrieval
decisions are guided by the estimated relationship between position-wise bias
and system-level bias.
5. Fairness-Aware Retrieval Optimization
In this section, we formulate the problem of fairness-aware retrieval in
RAG systems as an optimization task, corresponding to the detailed formu-
lation of Stage 3 in our overall framework. Building on the position-aware
bias propagation model introduced in Section 4, we aim to derive retrieval
strategies that balance relevance and fairness in the generated outputs. Un-
like prior work in fair ranking, which focuses on exposure allocation over
items or providers, our objective is to control the bias of generated responses
through retrieval decisions. This requires explicitly modeling how retrieval
affects downstream generation bias and incorporating this relationship into
the optimization process.
5.1. Problem Formulation
We consider a question setQ, where each questionq∈Qis associated
with a set of candidate documentsN q. The goal is to select and rankk
documents per question such that the overall relevance is maximized while
satisfying fairness constraints on the resulting system bias.
Letx q,i,p ∈ {0,1}denote whether documentiis assigned to positionpfor
questionq, andRel q,i denote the relevance score between questionqand doc-
umenti, as computed by the underlying retrieval model. Each document is
also associated with a binary attributeaq,i ∈ {−1,+1}, representing the bias
dimension (e.g., political stance or gender). For political bias, we categorize
documents according to their associated viewpoints: documents reflecting
liberal perspectives are assigned−1, while documents reflecting conservative
perspectives are assigned+1. Similarly, for gender bias, the documents con-
sist of biographical descriptions of individuals, where documents describing
male individuals are assigned−1and those describing female individuals are
assigned+1.
The objective is to construct rankings that maximize total relevance while
ensuring that the overall system bias remains close to zero. The total rele-
16

## Page 17

vance is defined as:
X
q∈Q
X
i∈Nq
kX
p=1
Relq,i xq,i,p.(6)
To quantify fairness, we use the position-aware bias propagation model
Equation (4). The average embedding bias at positionpis:
Ep
b = 1
|Q|
X
q∈Q
X
i∈Nq
aq,i xq,i,p (7)
and the resulting system-level bias is:
Rb =
kX
p=1
wp Ep
b +b,(8)
wherew p capturestheinfluenceofpositionp, andbaggregatesintrinsicmodel
bias and residual effects. A fairness-aware retrieval strategy should satisfy:
|Rb| ≤τ,(9)
whereτ >0is a predefined tolerance.
This formulation defines a dataset-level fairness constraint, ensuring that
the aggregate behavior of the system remains unbiased across questions.
5.2. Linear Programming Formulation
The problem above can be formulated as a constrained optimization prob-
lem:
max
x
X
q,i,p
Relq,i xq,i,p s.t.|R b| ≤τ.(10)
Since the decision variablesxq,i,p are binary, the problem is combinatorial.
To make it tractable, we relax the constraints to a continuous variablexq,i,p ∈
[0,1], which leads to a linear programming (LP) formulation [21]. After
solving the relaxed problem, a feasible ranking is obtained via discretization
by selecting the highest-scoring assignments.
While this formulation provides a principled baseline, it suffers from sev-
eral important limitations:
•Scalability:The number of variables grows asO(|Q|·|N q|·k), leading
to cubic-time complexity in the worst case.
17

## Page 18

•Dataset coupling:The fairness constraint couples all questions, pre-
venting decomposition and parallelization.
•Lack of flexibility:Each change in the question set or fairness thresh-
old requires solving the optimization problem from scratch.
•Single solution output:The LP formulation yields only one solu-
tion, making it difficult to explore the trade-off between fairness and
relevance.
These limitations motivate the need for a more scalable and flexible op-
timization framework.
5.3. Quadratic Fairness Optimization
To address the rigidity of hard fairness constraints, we reformulate the
problem by introducing a soft fairness objective. Instead of enforcing|Rb| ≤
τ, we penalize deviations from fairness directly in the objective:
max
x
X
q,i,p
Relq,ixq,i,p −λR 2
b,(11)
whereλ >0controls the trade-off between relevance and fairness.
This formulation has several advantages. First, it provides continuous
control over the fairness–relevance trade-off. Also, it avoids infeasible solu-
tions when strict constraints cannot be satisfied, and it enables exploration
of the Pareto frontier of optimal trade-offs. However, this formulation intro-
duces a key challenge. SinceRb aggregates contributions across all questions,
the quadratic termR2
b introduces global coupling, making the problem non-
separable and difficult to optimize efficiently.
5.4. Decomposition via Dual Reformulation (FARO)
To overcome this challenge, we reformulate the quadratic objective using
the Fenchel–Legendre dual representation. For the convex functionf(z) =
z2, we have:
z2 = sup
θ∈R
 
2θz−θ 2
.(12)
Applying this toR b, we can express the objective as a family of linear
surrogate problems parameterized byθ. This leads to the equivalent formu-
lation:
max
x∈X
inf
θ∈R
 X
q,i,p
Relq,ixq,i,p −2λθR b +λθ 2
!
.(13)
18

## Page 19

In general, sincexencodes discrete assignments,Xis non-convex; there-
fore the minimax order in (13) cannot be exchanged and the inner infimum
cannot be eliminated exactly. Instead, we adopt a structured approximation
strategy: we enumerate fixed values ofθ(equivalently, fixed linearization
weights) and solve the corresponding inner maximization problems to gener-
ate candidate rankings.
For a fixedθ, the termλθ 2 is constant with respect toxand does not
affect the optimizer. Hence, the induced surrogate subproblem is
max
x∈X
X
q,i,p
Relq,ixq,i,p −2λθR b.(14)
Definingµ= 2λθ, each surrogate objective becomes:
Oµ(x) =
X
q,i,p
Relq,ixq,i,p −µR b.(15)
Each fixedµcorresponds to a supporting hyperplane of the quadratic fair-
ness term, and maximizing Equation (15) yields a candidate solution on the
relevance-fairness frontier. Among the candidates generated by enumerating
µ, we can still select the final output by evaluating the original quadratic
objective, Equation (11).
ExpandingR b, the objective decomposes as:
Oµ(x) =
X
q∈Q
X
i,p

Relq,i − µ
|Q|wpaq,i

xq,i,p −µb.(16)
Since the last term is constant, the optimization decomposes into inde-
pendent per-question subproblems:
x∗
q(µ) = arg max
xq
X
i,p

Relq,i − µ
|Q|wpaq,i

xq,i,p.(17)
Each subproblem corresponds to a standard linear assignment problem and
can be solved exactly using the Hungarian algorithm [22]. The overall opti-
mization workflow is illustrated in Figure 3.
5.5. Algorithm and Practical Considerations
The overall procedure, referred to as FARO (Fairness-Aware Retrieval
Optimization), proceeds as follows:
19

## Page 20

Figure 3: Overview of the FARO optimization process. For each value of the surrogate
parameterµ, the global fairness-aware optimization problem is decomposed into indepen-
dent per-question assignment problems. Each solution yields a candidate retrieval strategy
corresponding to a different point on the relevance–fairness trade-off frontier. The final
solution is selected by enforcing the fairness constraint while maximizing relevance.
1. Enumerate a set of surrogate parametersµ.
2. For eachµ:
•Solve the per-question assignment problems.
•Construct a candidate retrieval strategy.
•Evaluate its relevance and resulting bias.
3. Select the solution that satisfies the fairness constraint and maximizes
relevance.
The detailed procedure is summarized in Algorithm 2. While Figure 3 pro-
vides a conceptual overview of the optimization process, Algorithm 2 presents
the exact implementation steps.
Complexity.For eachµ, the per-question optimization has complexity
O(N3
q ), resulting in total complexity:
O(T· |Q| · |Nq|3)
20

## Page 21

Algorithm 2:FARO for Fairness-aware Retrieval Optimization
Input:Question setQ, grid of trade-off parameters{µ 1, . . . , µM }, relevance
scoresRel q,i, bias toleranceτ
Output:Optimal retrieval assignmentx ∗
X ← ∅;
foreachµ∈ {µ1, . . . , µM }do
foreachq∈ Qdo
C(µ)
q ←ConstructCost(Rel q,i, µ);
x(µ)
q ←Hungarian(C (µ)
q );
x(µ) ← S
q∈Q x(µ)
q ;
Rb(x(µ))←EstimateBias(x (µ));
Rel(x(µ))← P
q,i,p Relq,i x(µ)
q,i,p;
X ← X ∪ {x(µ)};
x∗ = arg max
x∈X
X
q,i,p
Relq,i xq,i,p s.t.|R b(x)| ≤τ
returnx ∗;
whereTis the number of surrogate parameters evaluated.
Compared to linear programming, this approach offers: (i) Scalability,
due to decomposition across questions; (ii) Flexibility, by generating multi-
ple candidate solutions along the relevance–fairness frontier; (iii) Practical
robustness, as it can still provide near-feasible solutions even when strict
fairness constraints are difficult to satisfy.
Overall, the proposed FARO framework transforms a globally coupled
fairness optimization problem into a set of independent per-question sub-
problems. By approximating the quadratic fairness objective with a family
of linear surrogates, it enables efficient and flexible optimization of retrieval
strategies in RAG systems.
6. Experimental Setup
This section describes the datasets, models, retrieval components, and ex-
perimental configurations used to evaluate the proposed fairness-aware RAG
framework.
6.1. Datasets
For political bias analysis, we follow our previous methodology [12] and
construct two group-specific knowledge bases using liberal and conservative
21

## Page 22

statements from the TwinViews-13k dataset [23]. We sample 200 topic in-
stances, each consisting of paired left- and right-leaning statements. For each
topic, we generate 200 neutral questions using Copilot1, ensuring that the
questions do not favor either viewpoint. All generated samples are manually
reviewed to ensure quality and neutrality.
In addition, we reuse the dataset introduced in [12], which follows the
same construction methodology but differs in the sampled topics and gen-
erated questions. This allows us to evaluate the generalizability of the bias
propagation model across different question sets.
For gender bias evaluation, we use the dataset introduced in [24]. The
corpus is constructed from biographical profiles of historical figures, where
introductory paragraphs are retrieved from Wikipedia2. Based on this cor-
pus, we generate an occupation–gender QA dataset using 4 neutral templates
applied to 55 occupations. In both bias settings, we adopt a multiple-choice
format. Each question is associated with two candidate answers correspond-
ing to different groups (e.g., liberal vs. conservative, or female vs. male).
The RAG system is required to select one option, enabling us to compute
bias scores using Equation (1). Example questions are shown as follows:
Political bias question example
Question:What are the impacts of animal agriculture on society and the
environment?
Choices:(A)Meatconsumptionisapersonalchoice, andanimalagriculture
plays an important role in providing food and supporting rural economies.
(B) Animal agriculture has significant negative environmental impacts, and
a shift towards plant-based diets is necessary for sustainability.
Gender bias question example
Question:Who is a person whose work as aphilosopherhad impact?
Choices:(A) Plato (B) Susanne Langer
We use a shared prompt template for both bias types, requiring the model to
select exactly one option per question. The resulting selections are used to compute
bias scores. The specific setup is as follows.
1https://copilot.microsoft.com/
2https://www.wikipedia.org/
22

## Page 23

Prompt Template
Context: {context}
QUESTION: {question}
Choose the best answer with only the letter of the correct option (A or B)
based on the CONTEXT.
Choice A: {Option A}
Choice B: {Option B}
Answer :
6.2. Models and Retrieval Setup
Large Language Models.Weevaluatefouropen-sourcelargelanguagemodels: Llama
3.1 8B Instruct [25], Gemma 2 9B IT [26], Mistral 7B Instruct v0.3 [27], and Qwen
2.5 7B Instruct [28]. These models are selected to capture diverse architectural and
alignment characteristics, allowing us to analyze how different generators respond
to bias under varying retrieval conditions.
Retrieval Method.A key aspect of our framework is that embedding bias is con-
trolled independently of the retrieval model through reranking. As a result, the
choice of retrieval method does not affect the bias control mechanism. In princi-
ple, any retrieval approach, such as sparse methods (e.g., TF-IDF [29], BM25 [30],
SPLADE [31]) or dense retrieval models (e.g., BGE [32], GTE [33]), can be used
within our framework. In this work, we adopt GTE-base [33] as a lightweight
and widely used embedding model to serve as the retrieval backbone. We use co-
sine similarity both for vector indexing and as the relevance metric for document
retrieval.
6.3. Bias Configuration
Discrete Bias Space for Controlled Perturbations.Toconstructtheregressiondataset
in Equation (5), we define discrete sets of position-wise embedding bias values:
•Top-2(V 2):[1, 3
5 , 1
5 , -1
5 , -3
5 , -1]
•Top-3(V 3:[1, 1
3 ,− 1
3 , -1]
•Top-5(V 5):[-1, 1]
Theseconfigurationsaredesignedtobalancecoverageofthebiasspacewithcompu-
tational tractability. For each configuration, the reranker maps the desired embed-
ding biasEp
b to a selection probabilitymp using Equation (2), i.e.,mp = (Ep
b +1)/2.
This allows us to systematically control position-wise bias and analyze its effect on
the output biasRb.
23

## Page 24

Interpretation of Bias Scores.For political bias, a score close to -1 indicates a
preference toward liberal viewpoints, while a score close to 1 indicates a preference
toward conservative viewpoints. For gender bias, values close to -1 indicate pref-
erence toward male-associated outputs, and values close to 1 indicate preference
toward female-associated outputs.
To evaluate fairness-aware retrieval strategies, we impose a constraint on the
output bias, requiring|Rb| ≤0.1, as defined in Equation (9).
6.4. Implementation Details
All models are implemented using open-source libraries from Hugging Face3.
The RAG pipeline is built using LangChain4, and the vector database is con-
structedusingFAISS[34]. LinearprogrammingproblemsaresolvedusingSciPy[35].
All experiments are conducted on a single NVIDIA V100 GPU using the CSC Puhti
supercomputing platform5.
7. Experimental Results
This section evaluates the proposed framework from three perspectives: (i)
baseline bias behavior in RAG systems, (ii) validation of the bias propagation
model, and (iii) effectiveness of the fairness-aware optimization approach.
7.1. Baseline Analysis
We begin by analyzing the bias of individual components and standard RAG
pipelines. Using Equation (1), we compute bias scores for the knowledge base,
retriever (in top-1 setting), and LLMs, as well as for vanilla RAG under different
top-k settings. The results are summarized in Table 2.
Key observation.Bias in RAG systems emerges from the interaction between
the retriever, the knowledge base, and the generator. As a result, retrieval can
either mitigate or amplify bias depending on their relative tendencies.
For political bias, the constructed knowledge base is balanced (bias score 0),
while all models exhibit a preference toward liberal-leaning outputs. Since the
retrieveriscomparativelymorebalanced, incorporatingretrievalreducestheoverall
bias of strongly biased models, such as Llama and Qwen. In contrast, for gender
bias, the knowledge base is skewed toward male-associated content, which leads
to amplified bias in both the retriever and the resulting RAG outputs. These
3https://huggingface.co/
4https://www.langchain.com/
5https://www.csc.fi/en/services/puhti
24

## Page 25

Table 2: Political and Gender Bias Baseline Results
Model/Component Political Bias Gender Bias
Bias Score Refuse Rate Bias Score Refuse Rate
Knowledge Base 0 - -0.491 -
Retriever -0.12 0% -0.8 0%
Llama -0.72 0% -0.073 0%
Llama-RAG-1 -0.30 0% -0.8 0%
Llama-RAG-2 -0.26 0% -0.8 0%
Llama-RAG-3 -0.24 0% -0.755 0%
Llama-RAG-5 -0.25 0% -0.664 0%
GEMMA -0.10 89% -0.032 96.8%
GEMMA-RAG-1 -0.165 15.5% -0.673 14.5%
GEMMA-RAG-2 -0.145 16.5% -0.486 43.2%
GEMMA-RAG-3 -0.175 26.5% -0.468 48.6%
GEMMA-RAG-5 -0.135 33.5% -0.418 53.6%
MISTRAL -0.225 65.5% 0 100%
MISTRAL-RAG-1 -0.32 0% -0.782 0.9%
MISTRAL-RAG-2 -0.35 1% -0.764 2.7%
MISTRAL-RAG-3 -0.36 3% -0.623 3.2%
MISTRAL-RAG-5 -0.365 4.5% -0.495 5%
QWEN -0.80 0% -0.255 0%
QWEN-RAG-1 -0.32 0% -0.791 0%
QWEN-RAG-2 -0.38 0% -0.755 0%
QWEN-RAG-3 -0.47 0% -0.645 0%
QWEN-RAG-5 -0.42 0% -0.482 0%
results highlight that RAG does not inherently improve fairness; instead, its effect
depends on the alignment or conflict between component biases. This observation
is consistent with the notion of bias conflict [11], where competing signals from
different system components jointly determine the final output.
We also observe notable differences in refusal behavior. Models, such as Gemma
and Mistral, exhibit high refusal rates when evaluated without retrieval, indicating
strong alignment safeguards. However, these rates drop significantly when retrieval
is introduced, suggesting that even simple RAG setups can weaken refusal mech-
anisms. Furthermore, in top-1 settings, models tend to follow the stance of the
single retrieved document more strongly, which may reflect a form of sycophantic
behavior toward the provided context.
25

## Page 26

(a) Political: Llama
 (b) Political: Gemma
 (c) Political: Qwen
 (d) Political: Mistral
(e) Gender: Llama
 (f) Gender: Gemma
 (g) Gender: Qwen
 (h) Gender: Mistral
Figure 4: Top-2 RAG grid search results: We conducted our grid search experiments based
on four popular LLMs. The x and y axes of each graph represent the political and gender
embedding bias scores at the first and second positions (E1
b andE 2
b , the value is consistent
with the value set inV2), respectively, while the z axis represents the RAG system output
bias scoresR b after testing on the corresponding bias dataset.
7.2. Validation of Bias Propagation Model
We next evaluate whether the linear model in Equation (4) accurately captures
bias propagation in top-kRAG systems.
Key result.Across all evaluated models and bias types, we observe a strong
linear relationship between position-wise embedding bias and output bias, support-
ing the validity of the proposed formulation.
For the top-2 setting, Figure 4 visualizes the relationship between embedding
bias at different positions and the resulting output bias for both political and
gender biases. Despite differences in how models weigh individual positions, all
models exhibit a clear linear trend. For higher values ofk(top-3 and top-5),
direct visualization becomes impractical. Instead, we estimate linear regression
models using the dataset constructed in Equation (5) and validate them through
sampling. Specifically, we sample configurations ofE p
b that satisfy the fairness
conditionR b = 0, and evaluate the resulting bias scores. The results are shown in
Figure 5. To further assess generalization, we apply the learned linear parameters
across different question sets. Despite variations in questions and answer options,
the model maintains its effectiveness, with all results remaining within the baseline
26

## Page 27

A1 A2 A3 A4 A5 B1 B2 B3 B4 B5
Samples
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Bias Value
T op3
T op5
T op3 Ref = ±0.775
T op5 Ref = ±0.664
(a) Llama (gender)
A1 A2 A3 A4 A5 B1 B2 B3 B4 B5
Samples
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Bias Value
T op3
T op5
T op3 Ref = ±0.468
T op5 Ref = ±0.418 (b) Gemma (gender)
A1 A2 A3 A4 A5 B1 B2 B3 B4 B5
Samples
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Bias Value
T op3
T op5
T op3 Ref = ±0.623
T op5 Ref = ±0.495 (c) Mistral (gender)
A1 A2 A3 A4 A5 B1 B2 B3 B4 B5
Samples
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Bias Value
T op3
T op5
T op3 Ref = ±0.645
T op5 Ref = ±0.482 (d) Qwen (gender)
A1 A2 A3 A4 A5 B1 B2 B3 B4 B5
Samples
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Bias Value
T op3
T op5
T op3 Ref = ±0.24
T op5 Ref = ±0.25
(e) Llama (political)
A1 A2 A3 A4 A5 B1 B2 B3 B4 B5
Samples
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Bias Value
T op3
T op5
T op3 Ref = ±0.175
T op5 Ref = ±0.135 (f) Gemma (political)
A1 A2 A3 A4 A5 B1 B2 B3 B4 B5
Samples
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Bias Value
T op3
T op5
T op3 Ref = ±0.36
T op5 Ref = ±0.365 (g) Mistral (political)
A1 A2 A3 A4 A5 B1 B2 B3 B4 B5
Samples
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Bias Value
T op3
T op5
T op3 Ref = ±0.47
T op5 Ref = ±0.42 (h) Qwen (political)
A1 A2 A3 A4 A5 B1 B2 B3 B4 B5
Samples
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Bias Value
T op3
T op5
T op3 Ref = ±0.24
T op5 Ref = ±0.25
(i) Llama (cross data)
A1 A2 A3 A4 A5 B1 B2 B3 B4 B5
Samples
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Bias Value
T op3
T op5
T op3 Ref = ±0.175
T op5 Ref = ±0.135 (j) Gemma (cross data)
A1 A2 A3 A4 A5 B1 B2 B3 B4 B5
Samples
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Bias Value
T op3
T op5
T op3 Ref = ±0.36
T op5 Ref = ±0.365 (k) Mistral (cross data)
A1 A2 A3 A4 A5 B1 B2 B3 B4 B5
Samples
1.00
0.75
0.50
0.25
0.00
0.25
0.50
0.75
1.00
Bias Value
T op3
T op5
T op3 Ref = ±0.47
T op5 Ref = ±0.42 (l) Qwen (cross data)
Figure 5: Bias validation results: the first row corresponds to gender bias, the second
to political bias, and the third to cross-dataset political bias. In each plot, the line on
the left (blue circles, ) represents the 5 samples’ results of top-3 setting, while the line
on the right (orange squares, ) represents the top-5 setting. The dashed lines indicate
the absolute bias score intervals|Rb|of the corresponding vanilla RAG baselines; sampled
points falling within these intervals demonstrate effective bias mitigation.
biasintervals. Thisindicatesthatthelinearapproximationcapturesstablepatterns
of bias propagation across datasets.
Overall, these findings provide strong empirical support for the linear bias prop-
agation model and justify its use as the foundation for optimization.
7.3. Position-wise Bias Analysis
As described in Section 3.2, under top-ksettings (k = 2, 3, 5), we perform a
grid search over position-wise embedding bias and evaluate the resulting output
preference distribution of the RAG system. The goal of this analysis is to un-
derstand how different positions in the retrieved context contribute to generation
bias, and whether large language models exhibit consistent positional attention
patterns across bias types. We then apply linear regression to estimate how much
each model relies on documents at different positions, yielding the position-wise
attention weightswp in Equation (4).
27

## Page 28

(a) Political (k = 2)
 (b) Gender (k = 2)
(c) Political (k = 3)
 (d) Gender (k = 3)
(e) Political (k = 5)
 (f) Gender (k = 5)
Figure 6: Comparison of position-dependent weight distributions of biased content in the
context across LLMs. Columns correspond to political bias (left) and gender bias (right),
while rows correspond to top-kvalues of2,3, and5from top to bottom. Markers denote
models: Llama (blue circles,), Gemma (orange squares,), Qwen (green upward triangles,
), and Mistral (red downward triangles,).
To facilitate comparison across models and bias types, we visualize the learned
weights in Figure 6. In each plot, the horizontal axis represents the document po-
sition, while the vertical axis represents the corresponding weight value. The table
within each figure reports the intercept term (i.e.,Lb +ϵ) and the corresponding
linear model for each LLM.
We observe systematic differences in positional attention across models. For
political bias, Llama and Gemma place stronger emphasis on documents at the be-
ginning of the context, indicating a higher reliance on top-ranked evidence. Mistral
28

## Page 29

distributes attention toward both early and late positions, while Qwen allocates
attention more evenly across the retrieved documents. For gender bias, these pat-
terns shift: Llama continues to prioritize early positions, Qwen shows a stronger
preference for later positions, and Gemma and Mistral exhibit more balanced distri-
butions across the context. These results suggest that bias propagation is strongly
model-dependent, reinforcing the need to estimate position-wise weights separately
for each model.
Across all models, we observe that askincreases, the influence of any single
position decreases. This indicates that models rely on a broader aggregation of
contextual signals when more documents are included. Consequently, bias control
in higher-ksettings requires coordinated adjustments across multiple positions,
rather than focusing solely on top-ranked documents. Interestingly, in the top-5
gender bias experiments, some positional weights become negative. This suggests
that documents at certain positions may counteract bias introduced elsewhere in
the context, possibly due to redundancy or conflicting information. While the
overall bias propagation is well approximated by a linear model, this observation
highlights the presence of more complex interactions within the retrieved context.
The intercept terms further reveal intrinsic model tendencies. In particular,
Qwen exhibits a strong preference toward liberal-leaning outputs, consistent with
the baseline results reported in Table 2. Such inherent biases may limit the ef-
fectiveness of retrieval-based mitigation, as they introduce a systematic offset that
cannot be fully corrected through document selection alone.
To assess the robustness of the learned position-wise weights, Figure 7 com-
pares the attention distributions obtained from different evaluation question sets.
Although the exact numerical values of the weights vary across datasets, the over-
all positional patterns remain largely consistent. This suggests that the learned
bias propagation model captures stable, model-specific behaviors that generalize
across datasets. However, such generalization should be applied with caution, as
variations in question distributions may still affect mitigation performance.
Overall, these findings confirm that bias propagation in RAG systems is both
position-dependent and model-specific, providing strong support for the position-
aware optimization framework introduced in Section 5.
7.4. Optimization Results
In this section, we evaluate the effectiveness of the proposed FARO framework
in balancing relevance and fairness, and compare it against the linear program-
ming (LP) baseline. We aim to assess (i) how well the optimization controls bias
under different settings, and (ii) the trade-offs between fairness, relevance, and
computational efficiency.
29

## Page 30

(a) Political (k = 2)
 (b) Political ver2 (k = 2)
(c) Political (k = 3)
 (d) Political ver2 (k = 3)
(e) Political (k = 5)
 (f) Political ver2 (k = 5)
Figure 7: Comparison of attention weight distributions for political bias across different
question sets. The layout follows that of the previous figure: rows correspond to top-k
values of2,3, and5(from top to bottom), while columns correspond to different question
sets. Markers denote models: Llama (blue circles, ), Gemma (orange squares, ), Qwen
(green upward triangles, ), and Mistral (red downward triangles,).
For the FARO method, we search over 81 uniformly spaced values ofµin the
range [-20, 20], generating a set of candidate retrieval strategies. The results for
political and gender bias settings are visualized in Figures 8 and 9. In these figures,
the horizontal axis represents the values ofµ, the red curve (circular markers) shows
the theoretical bias scoreRb, and the green curve (square markers) represents the
total relevance score. Together, these curves provide a clear view of the trade-off
between fairness and relevance, where different values ofµcorrespond to different
operating points along the trade-off frontier.
30

## Page 31

(a) Llama (k = 2)
 (b) Gemma (k = 2)
 (c) Mistral (k = 2)
 (d) Qwen (k = 2)
(e) Llama (k = 3)
 (f) Gemma (k = 3)
 (g) Mistral (k = 3)
 (h) Qwen (k = 3)
(i) Llama (k = 5)
 (j) Gemma (k = 5)
 (k) Mistral (k = 5)
 (l) Qwen (k = 5)
Figure 8: Trade-off curves between fairness and relevance for political bias in RAG systems
built on different LLMs. Rows 1 to 3 correspond to top-2, top-3, and top-5 retrieval
settings, respectively. The horizontal axis in each plot represents the searched values of
µ. The red curve (circular markers,) shows the theoretical bias scoreRb, while the green
curve (square markers,) represents the actual total relevance score.
In the political bias setting, the knowledge base provides balanced support for
both viewpoints. As a result, the relevance curve exhibits an approximately sym-
metric (inverted V) shape, peaking nearµ= 0. In contrast, the bias curve changes
more sharply due to the intrinsic tendencies of the underlying LLMs, which gener-
ally favor liberal-leaning outputs. This asymmetry indicates that achieving fairness
may require stronger adjustments in retrieval compared to relevance optimization
alone.
In the gender bias setting, the knowledge base is skewed toward male-associated
content. Consequently, whenµ <0, the optimization favors the underrepresented
group, resulting in lower bias but also reduced relevance. Conversely, forµ >0, the
relevance remains relatively high while the bias increases rapidly. This behavior
highlights a more pronounced fairness–relevance trade-off compared to the political
setting, driven by imbalance in the candidate pool.
Following the predefined fairness constraint|Rb| ≤0.1, we select the retrieval
31

## Page 32

(a) Llama (k = 2)
 (b) Gemma (k = 2)
 (c) Mistral (k = 2)
 (d) Qwen (k = 2)
(e) Llama (k = 3)
 (f) Gemma (k = 3)
 (g) Mistral (k = 3)
 (h) Qwen (k = 3)
(i) Llama (k = 5)
 (j) Gemma (k = 5)
 (k) Mistral (k = 5)
 (l) Qwen (k = 5)
Figure 9: Trade-off curves between fairness and relevance for gender bias in RAG systems
built on different LLMs. Rows 1 to 3 correspond to top-2, top-3, and top-5 retrieval
settings, respectively. The horizontal axis in each plot represents the searched values of
µ. The red curve (circular markers,) shows the theoretical bias scoreRb, while the green
curve (square markers,) represents the actual total relevance score.
strategy that satisfies the constraint while achieving the highest relevance score.
Tables 3 and 4 report the optimization results for political and gender bias, re-
spectively, comparing FARO and LP under different top-ksettings. To facilitate
comparison, relevance scores are normalized using Min–Max scaling. Specifically,
for each question, we collect the top 20 most relevant documents as candidates
(|Nq|= 20) and rank them by relevance. We define the maximum relevance (Max)
as the sum of relevance scores of the top-kdocuments, and the minimum relevance
(Min) as the sum for thebottom−kdocuments. After scaling, the relevance values
reported in the table lie in[0,1]: values closer to 1 indicate smaller relevance loss,
while values closer to 0 indicate larger loss.
Rel′ = Rel−Min
Max−Min (18)
In addition, the bias scores reported in the table correspond to the actual bias
observed after applying the optimized retrieval solution within the RAG system. In
32

## Page 33

contrast, the theoretical bias scores used during optimization all satisfy the fairness
constraint. Therefore, these empirical bias values provide a practical reference for
evaluating the effectiveness of bias mitigation via the learned linear relationships.
From the optimization results for political bias in Table 3, we observe that the
proposed bias mitigation method is effective for Llama and Gemma, but performs
poorly for Mistral and Qwen. This finding suggests that when a model exhibits
strong inherent bias, the effectiveness of our mitigation approach becomes limited.
Comparing LP and FARO, we find that under the top-2 setting, LP achieves
both high efficiency and strong performance. However, askincreases and the
number of variables grows, FARO demonstrates clear advantages in computational
efficiency. This behavior aligns with our expectations from the algorithm design.
In terms of normalized relevance, both methods achieve very similar performance
acrossallsettings, withLPshowingaslightoveralladvantage. Thisdifferencearises
because FARO relies on grid search and thus provides an approximate solution.
Importantly, when the fairness constraint changes, FARO can directly select
a suitable optimal solution from the existing candidate set. In contrast, LP must
recompute the solution from scratch. This property improves computational effi-
ciency and provides greater flexibility in practical applications.
For the gender bias setting (Table 4), the baseline RAG system exhibits sub-
stantial bias due to the skewed knowledge base. Under this setting, both FARO
and LP achieve significant bias mitigation. However, the relevance loss is more
pronounced compared to the political setting, as the candidate pool contains rel-
atively fewer documents representing the underrepresented group. This limits the
feasible space of fair solutions and leads to a stronger trade-off between fairness
and relevance. We also observe that, even with a modest increase in the number
of questions, the efficiency advantage of LP diminishes, particularly in higher-k
settings. This further highlights the scalability limitations of LP and the practical
advantages of the FARO framework.
Overall, the results demonstrate that the proposed FARO method effectively
balances fairness and relevance while providing significant improvements in scal-
ability and flexibility. These properties make it well-suited for real-world RAG
systems, where fairness requirements and question distributions may vary dynam-
ically.
7.5. Discussion
Overall, the proposed framework achieves effective bias control in RAG sys-
tems while maintaining high relevance. From an optimization perspective, LP
performs well for small-scale problems with fixed constraints, providing exact solu-
tions. However, its scalability limitations make it less suitable for larger or dynamic
33

## Page 34

Table 3: Political bias optimization results comparison
Model Method Bias Score Relevance Runtime(s)
Llama-RAG-2
FARO
-0.21 1 0.75
Llama-RAG-3 -0.28 1 0.82
Llama-RAG-5 -0.29 1 1.00
GEMMA-RAG-2
FARO
0.01 0.997 0.87
GEMMA-RAG-3 0.01 0.995 0.99
GEMMA-RAG-5 0.04 1 1.27
MISTRAL-RAG-2
FARO
-0.41 0.993 0.88
MISTRAL-RAG-3 -0.43 0.999 0.83
MISTRAL-RAG-5 -0.44 1 1.07
QWEN-RAG-2
FARO
-0.57 0.964 0.74
QWEN-RAG-3 -0.62 0.964 0.97
QWEN-RAG-5 -0.62 0.945 1.05
Llama-RAG-2
LP
-0.26 1 0.64
Llama-RAG-3 -0.27 1 1.04
Llama-RAG-5 -0.29 1 1.83
GEMMA-RAG-2
LP
-0.12 1 0.65
GEMMA-RAG-3 -0.06 0.999 1.04
GEMMA-RAG-5 -0.08 1 1.80
MISTRAL-RAG-2
LP
-0.44 0.997 0.64
MISTRAL-RAG-3 -0.44 1 1.02
MISTRAL-RAG-5 -0.40 1 1.85
QWEN-RAG-2
LP
-0.58 0.966 0.66
QWEN-RAG-3 -0.60 0.966 1.06
QWEN-RAG-5 -0.61 0.947 1.82
settings. In contrast, FARO offers a flexible and efficient alternative by decom-
posing the global problem into independent subproblems and generating multiple
candidate solutions along the fairness–relevance frontier. This flexibility is par-
ticularly valuable in practical applications, where fairness requirements may vary
across scenarios. By adjusting the search range and granularity ofµ, FARO allows
practitioners to balance computational efficiency and solution quality.
Overall, these results demonstrate that combining a position-aware bias model
with a scalable optimization framework enables effective and practical fairness-
aware retrieval in RAG systems.
34

## Page 35

Table 4: Gender bias optimization results comparison
Model Method Bias Score Relevance Runtime(s)
Llama-RAG-2
FARO
0.02 0.889 0.77
Llama-RAG-3 -0.05 0.934 0.86
Llama-RAG-5 -0.07 0.988 1.33
GEMMA-RAG-2
FARO
-0.08 0.825 0.79
GEMMA-RAG-3 -0.09 0.854 1.04
GEMMA-RAG-5 -0.32 0.978 1.10
MISTRAL-RAG-2
FARO
-0.05 0.833 1.33
MISTRAL-RAG-3 -0.01 0.853 1.03
MISTRAL-RAG-5 -0.16 0.969 1.15
QWEN-RAG-2
FARO
-0.01 0.832 0.76
QWEN-RAG-3 -0.03 0.829 1.05
QWEN-RAG-5 -0.1 0.938 1.31
Llama-RAG-2
LP
-0.01 0.906 0.85
Llama-RAG-3 -0.15 0.934 1.04
Llama-RAG-5 -0.09 0.99 2.19
GEMMA-RAG-2
LP
-0.09 0.835 0.84
GEMMA-RAG-3 -0.12 0.856 1.32
GEMMA-RAG-5 -0.30 0.979 2.40
MISTRAL-RAG-2
LP
-0.16 0.851 0.85
MISTRAL-RAG-3 -0.08 0.855 1.29
MISTRAL-RAG-5 -0.21 0.970 2.41
QWEN-RAG-2
LP
-0.07 0.841 0.86
QWEN-RAG-3 -0.10 0.834 1.31
QWEN-RAG-5 -0.05 0.939 2.25
8. Conclusions
In this paper, we addressed the problem of fairness in top-k retrieval-augmented
generation (RAG), focusing on how retrieval decisions influence bias in generated
outputs. We proposed a unified three-stage framework that enables controlled bias
injection, models position-aware bias propagation, and optimizes retrieval under
fairness constraints.
Our approach introduced a linear, position-aware bias propagation model that
captures how multiple retrieved documents jointly affect system-level bias. Build-
ing on this model, we formulated fairness-aware retrieval as an optimization prob-
lem and proposed the FARO framework, which enables flexible exploration of the
35

## Page 36

relevance–fairness trade-off. Experimental results across multiple datasets and
models demonstrate that: (i) bias in RAG systems can be effectively controlled
through retrieval, (ii) the proposed linear model provides a strong approxima-
tion of bias propagation in top-k settings, and (iii) the FARO framework achieves
competitive performance compared to linear programming while offering improved
scalability and flexibility.
Despite these promising results, several limitations remain. First, the proposed
bias propagation model relies on linearity and independence assumptions, which
may not fully capture complex interactions between retrieved documents. Second,
our formulation focuses on binary group fairness and does not directly extend to
multi-group fairness definitions. Third, the effectiveness of bias mitigation depends
on the intrinsic biases of the underlying language models. Future work includes
extending the framework to richer fairness notions, incorporating non-linear or
interaction-aware bias models, and exploring adaptive retrieval strategies that ac-
count for question-specific fairness requirements.
References
[1] Vaswaniet al., Attention is All you Need, in: Advances in
Neural Information Processing Systems, volume 30, Curran Asso-
ciates, Inc., 2017. URL:https://papers.nips.cc/paper_files/paper/
2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html.
[2] J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child,
S. Gray, A. Radford, J. Wu, D. Amodei, Scaling Laws for Neural Lan-
guage Models, 2020. URL:http://arxiv.org/abs/2001.08361. doi:10.
48550/arXiv.2001.08361, arXiv:2001.08361 [cs, stat].
[3] Z. Ji, N. Lee, R. Frieske, T. Yu, D. Su, Y. Xu, E. Ishii, Y. J. Bang,
A. Madotto, P. Fung, Survey of hallucination in natural language generation,
ACM Comput. Surv. 55 (2023). URL:https://doi.org/10.1145/3571730.
doi:10.1145/3571730.
[4] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler,
M. Lewis, W.-t. Yih, T. Rocktäschel, S. Riedel, D. Kiela, Retrieval-augmented
generation for knowledge-intensive nlp tasks, in: Proceedings of the 34th
International Conference on Neural Information Processing Systems, NIPS
’20, Curran Associates Inc., 2020.
[5] M. Hu, H. Wu, Z. Guan, R. Zhu, D. Guo, D. Qi, S. Li, No Free Lunch:
Retrieval-Augmented Generation Undermines Fairness in LLMs, Even for Vig-
36

## Page 37

ilant Users, 2024. URL:http://arxiv.org/abs/2410.07589. doi:10.48550/
arXiv.2410.07589, arXiv:2410.07589 [cs].
[6] X. Wu, S. Li, H.-T. Wu, Z. Tao, Y. Fang, Does RAG Introduce Unfairness in
LLMs? Evaluating Fairness in Retrieval-Augmented Generation Systems, in:
COLING, 2025, pp. 10021–10036.
[7] R. Ranjan, S. Gupta, S. N. Singh, A comprehensive survey of bias in llms:
Current landscape and future directions, CoRR abs/2409.16430 (2024).
[8] E. Pitoura, K. Stefanidis, G. Koutrika, Fairness in rankings and recommen-
dations: an overview, VLDB J. 31 (2022) 431–458.
[9] G. et al., Bias and Fairness in Large Language Models: A Survey, Computa-
tional Linguistics 50 (2024) 1097–1179. doi:10.1162/coli_a_00524.
[10] A. Singh, T. Joachims, Fairness of Exposure in Rankings, in: Proceedings
of the 24th ACM SIGKDD International Conference on Knowledge Discov-
ery & Data Mining, KDD ’18, Association for Computing Machinery, 2018,
pp. 2219–2228. URL:https://dl.acm.org/doi/10.1145/3219819.3220088.
doi:10.1145/3219819.3220088.
[11] T. Kim, J. M. Springer, A. Raghunathan, M. Sap, Mitigating Bias in RAG:
Controlling the Embedder, in: Findings of the Association for Computational
Linguistics, ACL 2025, Vienna, Austria, July 27 - August 1, 2025, Association
for Computational Linguistics, 2025, pp. 18999–19024.
[12] Y. Zhao, V. Efthymiou, J. Nummenmaa, K. Stefanidis, ReFaRAG: Re-
ranking for Bias Mitigation in Retrieval-Augmented Generation, in: New
TrendsinDatabaseandInformationSystems, 2026, pp.516–530.doi:10.1007/
978-3-032-05727-3_42.
[13] T. Zhang, Y. Zhou, D. Bollegala, Evaluating the Effect of Retrieval
Augmentation on Social Biases, 2025. doi:10.48550/arXiv.2502.17611.
arXiv:2502.17611.
[14] L. et al., Lost in the Middle: How Language Models Use Long Con-
texts, Transactions of the Association for Computational Linguistics 12 (2024)
157–173. URL:https://aclanthology.org/2024.tacl-1.9/. doi:10.1162/
tacl_a_00638.
37

## Page 38

[15] T. E. Kim, F. Diaz, Towards fair rag: On the impact of fair ranking in
retrieval-augmented generation, ICTIR ’25, Association for Computing Ma-
chinery, 2025, p. 33–43. URL:https://doi.org/10.1145/3731120.3744599.
doi:10.1145/3731120.3744599.
[16] M. Dehghan, G. McDonald, Who benefits from rag? the role of expo-
sure, utility and attribution bias, in: Advances in Information Retrieval:
48th European Conference on Information Retrieval, ECIR 2026, Delft, The
Netherlands, March 29 – April 2, 2026, Proceedings, Part I, Springer-Verlag,
2026, p. 289–304. URL:https://doi.org/10.1007/978-3-032-21289-4_19.
doi:10.1007/978-3-032-21289-4_19.
[17] M. Zehlike, F. Bonchi, C. Castillo, S. Hajian, M. Megahed, R. Baeza-Yates,
FA*IR: A fair top-k ranking algorithm, in: CIKM, 2017, pp. 1569–1578.
[18] M. Zehlike, C. Castillo, Reducing Disparate Exposure in Ranking: A
Learning To Rank Approach, in: Proceedings of The Web Conference
2020, WWW ’20, Association for Computing Machinery, 2020, pp. 2849–
2855. URL:https://dl.acm.org/doi/10.1145/3366424.3380048. doi:10.
1145/3366424.3380048.
[19] Beutel et al., Fairness in Recommendation Ranking through Pairwise Com-
parisons, in: Proceedings of the 25th ACM SIGKDD International Conference
on Knowledge Discovery & Data Mining, KDD ’19, Association for Computing
Machinery, 2019, pp. 2212–2220. URL:https://dl.acm.org/doi/10.1145/
3292500.3330745. doi:10.1145/3292500.3330745.
[20] A. Singh, T. Joachims, Policy Learning for Fairness in Ranking, in: Ad-
vances in Neural Information Processing Systems, volume 32, Curran As-
sociates, Inc., 2019. URL:https://proceedings.neurips.cc/paper/2019/
hash/9e82757e9a1c12cb710ad680db11f6f1-Abstract.html.
[21] Linear Programming, in: Optimization Techniques and Applications with Ex-
amples, 2018, pp. 125–140. URL:https://onlinelibrary.wiley.com/doi/
abs/10.1002/9781119490616.ch6. doi:10.1002/9781119490616.ch6.
[22] H. W. Kuhn, The Hungarian method for the assignment problem (1955)
83–97. URL:https://onlinelibrary.wiley.com/doi/abs/10.1002/nav.
3800020109. doi:10.1002/nav.3800020109.
[23] S. Fulay, W. Brannon, S. Mohanty, C. Overney, E. Poole-Dayan, D. Roy,
J. Kabbara, On the relationship between truth and political bias in language
models, in: EMNLP, 2024, pp. 9004–9018.
38

## Page 39

[24] Y. Zhao, V. Efthymiou, J. Nummenmaa, K. Stefanidis, A dataset generation
method for bias evaluation in retrieval-augmented generation, in: Proceed-
ingsoftheEDBT/ICDT2026JointConferenceWorkshops(EDBT/ICDT-WS
2026), CEUR Workshop Proceedings, CEUR-WS.org, Helsinki, Finland, 2026.
URL:https://ceur-ws.org/Vol-4192/DARLIAP-paper5.pdf.
[25] A. Grattafiori et al., The Llama 3 Herd of Models, 2024. URL:http://arxiv.
org/abs/2407.21783. doi:10.48550/arXiv.2407.21783, arXiv:2407.21783
[cs].
[26] Gemma Team, Gemma 2: Improving Open Language Models at a Practical
Size, 2024. URL:http://arxiv.org/abs/2408.00118. doi:10.48550/arXiv.
2408.00118, arXiv:2408.00118 [cs].
[27] A. Q. Jiang et al., Mistral 7B, 2023. URL:http://arxiv.org/abs/2310.
06825. doi:10.48550/arXiv.2310.06825, arXiv:2310.06825 [cs].
[28] A. Yang et al., Qwen2 Technical Report, 2024. URL:http://arxiv.org/abs/
2407.10671. doi:10.48550/arXiv.2407.10671, arXiv:2407.10671 [cs].
[29] T. Roelleke, J. Wang, TF-IDF uncovered: A study of theories and probabili-
ties, in: Proceedings of the 31st Annual International ACM SIGIR Conference
on Research and Development in Information Retrieval, Association for Com-
puting Machinery, 2008, pp. 435–442. URL:https://dl.acm.org/doi/10.
1145/1390334.1390409. doi:10.1145/1390334.1390409.
[30] S. Robertson, H. Zaragoza, The Probabilistic Relevance Framework: BM25
and Beyond, Found. Trends Inf. Retr. 3 (2009) 333–389. URL:https://doi.
org/10.1561/1500000019. doi:10.1561/1500000019.
[31] T. Formal, B. Piwowarski, S. Clinchant, Splade: Sparse lexical and expansion
model for first stage ranking, in: Proceedings of the 44th International ACM
SIGIR Conference on Research and Development in Information Retrieval,
SIGIR ’21, Association for Computing Machinery, 2021, p. 2288–2292. URL:
https://doi.org. doi:10.1145/3404835.3463098.
[32] J. Chen et al., M3-embedding: Multi-linguality, multi-functionality, multi-
granularity text embeddings through self-knowledge distillation, in: Find-
ings of the Association for Computational Linguistics: ACL 2024, Associ-
ation for Computational Linguistics, Bangkok, Thailand, 2024, pp. 2318–
2335. URL:https://aclanthology.org/2024.findings-acl.137/. doi:10.
18653/v1/2024.findings-acl.137.
39

## Page 40

[33] Z. Li et al., Towards General Text Embeddings with Multi-stage Contrastive
Learning, 2023. URL:http://arxiv.org/abs/2308.03281. doi:10.48550/
arXiv.2308.03281, arXiv:2308.03281 [cs].
[34] M. Douze et al., The Faiss library, 2025. URL:http://arxiv.org/abs/2401.
08281. doi:10.48550/arXiv.2401.08281, arXiv:2401.08281 [cs].
[35] P. Virtanen, et al., Scipy 1.0: Fundamental algorithms for scientific computing
in python, Nature Methods 17 (2020) 261–272.
40
