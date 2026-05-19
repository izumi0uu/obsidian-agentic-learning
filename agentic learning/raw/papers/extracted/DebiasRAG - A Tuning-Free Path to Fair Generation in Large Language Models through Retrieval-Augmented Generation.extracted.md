# DebiasRAG: A Tuning-Free Path to Fair Generation in Large Language Models through Retrieval-Augmented Generation - Extracted Text

- Source note: [[DebiasRAG - A Tuning-Free Path to Fair Generation in Large Language Models through Retrieval-Augmented Generation]]
- Source PDF: `assets/DebiasRAG - A Tuning-Free Path to Fair Generation in Large Language Models through Retrieval-Augmented Generation.pdf`
- Extracted: 2026-05-18
- Extractor: pypdf
- Pages: 11
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

DebiasRAG: A Tuning-Free Path to Fair Generation in Large
Language Models through Retrieval-Augmented Generation
Rui Chu, Bingyin Zhao, Thanh Quoc Hung Le, Duy Cao Hoang, Huawei Lin, Ping Li, Weijie Zhao,
Khoa D Doan, Yingjie Lao
Abstract
Large language models (LLMs) have achieved unprecedented suc-
cess due to their exceptional generative capabilities. However, they
also suffer from producing hallucinations and unexpected outputs
(e.g., stereotypes and societal-biased content) . Prior studies employ
LLM fine-tuning and prompt engineering to mitigate such biases in
LLMs, which requires additional training or domain knowledge to
design the framework. However, these approaches either demand
extensive training resources or risk degrading the LLM’s original ca-
pabilities, while overlooking the need to provide dynamicdebiasing
contextsfor fairer inferences. In this paper, we propose DebiasRAG,
a novel LLM-tuning-free and dynamic query-specific debiasing
framework based on retrieval augmented generation (RAG) that
greatly improves the fairness while simultaneously preserving the
intrinsic properties of LLMs. DebiasRAGconsists of three stages: (1)
query-specific debias candidates production; (2) Context candidate
pool forming; and (3) Gradient updated debiasing-guided context
piece reranking. DebiasRAG firstly leverages the self-diagnosedbias
contextsin relevant to the query through regular retrieval. Given
the query-specificbias contexts, reverse producedebias contexts,
which will be provided as an additional fairness constraint for LLM
output. Secondly, a regular RAG retrieval process will produce the
query-related contextsfrom the regular RAG document database.
During the RAG reranking progress for final debiasing context se-
lection, DebiasRAG re-rank the vectored pieces in the pool based on
a gradient-optimized debiasing score as the mostunbiasedsupport
for the user input query. Lastly, we propose two adaptive scenarios
of using DebiasRAG, including a regular scenario (with additional
RAG documents in the framework) and a non-RAG-document de-
biasing scenario, which can use DebiasRAGas a simple debiasing
tool as a replacement for fine-tuning. We evaluate the performance
of DebiasRAG comprehensively on multiple benchmarks, which
demonstrates a highly competitive performance of bias mitigation
compared to the state-of-the-art tuning-based methods.
Keywords
Fairness, Bias, Large Language Model, Retrieval Augmented Gener-
ation
1 Introduction
Large language models (LLMs) are widely adopted to empower
real-world applications such as content generation [8, 22, 31, 43],
question answering [ 29, 33, 56, 66] and reasoning [ 59]. Despite
their success, LLMs show inferior performance on domain-specific
and knowledge-intensive tasks [6, 52]. A phenomenal example is
the hallucinations (e.g., stereotypes and biased information) gener-
ated by LLMs when dealing with queries that exceed encapsulated
knowledge in the training corpora. Prior research [15, 19, 38, 46, 61],
has revealed that biases are present and can arise at various stages
of the nature language processing (NLP) development iterations.
Such limitations raise critical concerns, particularly in areas where
fairness and equality are highly demanded (e.g., healthcare and
legal services) as biased outputs can lead to harmful or even cata-
strophic consequences [41, 64]. Thus, it is crucial to mitigate biases
that inherently exist in LLMs.
There have been lines of work that attempt to alleviate biases
through various approaches. The mainstream mechanisms can be
broadly categorized as fine-tuning [11, 21] and prompt engineer-
ing [42, 55, 61]. Fine-tuning is a general method to improve LLMs’
performance on downstream tasks by retraining the model in an
end-to-end manner on a relatively small dataset. In the context
of debiasing, one may consider bias elimination as a unique in-
stance of downstream tasks. Fine-tuning tends to achieve superior
performance since all LLM layers are retrained to accommodate
the downstream tasks [25]. Yet, it still faces significant limitations,
such as high demand for computing resources, the difficulty of data
collection, and cumbersome hyperparameter optimization. Prompt
engineering is an alternative solution that crafts and refines in-
puts (i.e., prompts) to direct LLMs to generate fair outputs without
touching model parameters [20]. Deliberately designed prompts
convey task-specific information that helps models better interpret
the input queries and, hence, produce more accurate and reliable
outputs. However, acquiring useful and effective prompts is chal-
lenging, and a common practice usually involves manual design
that requires professional expertise and domain knowledge [4, 29].
Another major issue of debiasing in LLMs is the trade-off be-
tween fairness and the model’s representation ability (e.g., accuracy
and expressiveness) [54]. Prior studies [19, 61] have shown that an
inordinate emphasis on eliminating biases may ultimately under-
mine the intrinsic properties of LLMs that evolved from pre-training
and generate fair yet meaningless outputs.
In this paper, we propose DebiasRAG, which aims to address the
aforementioned challenges by leveraging retrieval-augmented gen-
eration (RAG) to achieve lightweight debiasing comparable to fine-
tuning, but without its computational or data overhead. Although
prompt engineering can also achieve debiasing without parameter
updates, it often degrades performance by altering user queries [16]
or yields limited effects due to its reliance on fixed contexts [46].
In contrast, RAG provides dynamic, query-dependent contexts,
but its potential to deliver adaptive debiasing signals—guiding the
LLM toward fairer outputs—remains largely unexplored. Existing
RAG-based debiasing methods primarily focus on retrieving the
fairest possible context via embedding-level retrieval guidance [23]
or agent-based filtering [50]. While effective in preventing the in-
troduction of new bias, these approaches do not actively reduce
existing bias in an otherwise clean LLM. We instead consider a prac-
tical zero-shot scenario in which the debiasing requester possesses
only bias-inducing documents the model should learn to avoid,
arXiv:2605.16113v1  [cs.CL]  15 May 2026

## Page 2

Chu et al.
Figure 1: System workflow of DebiasRAG. The workflow consists of three main components. The first stage (Upper Block)
involves document preparation and preprocessing, including management of the Avoid Document Repo, along with user-
provided input documents (Optional). The second stage (Middle Block) performs reverse-generation of debiasing performance
based on the user’s input to establish a baseline for effective real-time operation. For the third stage (Lower Block), real-time
debias-guided reranking optimization, integrates embedding retrieval, gradient-based reranking, and generation, working
dynamically to debias the reasoning and output process of large language models.
analogous to the fine-tuning setting. Unlike prior works that rely
on unrelated or neutral corpora (e.g., Wikipedia [26, 62]) for con-
text substitution or reranking, our approach requires no additional
external documents. It is important to note that our goal is to use
RAG to debias LLM output (just like a substitution of fine-tuning),
which is qualitatively different fromfairness enhancementwithin
RAG as in prior works [23].
The overview of the proposed DebiasRAG is shown in Fig. 1. It
consists of three main steps: 1) Bias Pre-Doc Generation for RAG,
2) reverse-generation of debiasing piece based on the retrieved
input, and 3) real-time debias-guided reranking optimization. The
key idea is to retrieve query-specific biased contexts and reverse-
generate debiasing contexts, which are then integrated into the RAG
reranking process. The final debiasing context serves as an adaptive
augmentation mechanism that constrains the LLM to produce fairer
outputs. Our contributions are summarized as follows:
• To the best of our knowledge, DebiasRAG is the first framework
to demonstrate the effectiveness of RAG for LLM debiasing
without requiring additional training or auxiliary data.
•We design a debiasing-guided reranking mechanism that steers
RAG to retrieve fairness-enhancing contexts, thereby constrain-
ing LLM outputs without compromising retrieval quality or
generative expressiveness.
•We develop a lightweight RAG-based debiasing framework that
relies solely on off-the-shelf bias documents, while other RAG
documents are optional.
•We demonstrate that DebiasRAG achieves a highly competitive
performance in bias mitigation compared to state-of-the-art
debiasing methods.
2 Related Works
2.1 Fine-Tuning for Bias Mitigation
Fine-tuning has achieved impressive advancements in LLM debi-
asing, which treats debiasing as a downstream task and updates
all the model parameters [ 2, 10, 65]. For example, [51] mitigates
the LLM biases by tuning it on a predefined value-targeted dataset.
On the other hand, DPCE (Debiasing Pre-trained Contextualised
Embeddings) [21] enhances the fairness in pre-trained contextual-
ized embeddings by optimizing a debiased embedding loss function
to guide the fine-tuning process. Though at the cost of extensive
training, the later method achieves a significant fairness gain when
debiasing is applied to all tokens and layers of the embedding model
and also preserves the model accuracy, which is recognized as the
state-of-the-art fine-tuning-based approach. To this end, we con-
sider this approach as one of our baselines. Note that a few relevant
earlier works [21, 57] of debiasing techniques were originally fo-
cused on static embeddings [5] while modern LLMs mainly adopt
contextualized embeddings.
2.2 Prompt Engineering for Bias Mitigation
Prompt engineering is an orthogonal workaround to fine-tuning
that eliminates biases by providing instructive descriptions to LLMs.
Constructing effective prompts often involves human engagement

## Page 3

DebiasRAG: A Tuning-Free Path to Fair Generation in Large Language Models through Retrieval-Augmented Generation
in the design phase, which imposes a hurdle to users without spe-
cific knowledge and domain expertise. For instance, the work in
[3, 32] needed to manually craft a long prompt (e.g., more than
4000 words) from a fictional conversation. To address this issue,
ADEPT [61] proposes prompt tuning that automates the prompt
construction via training exclusively on layers for prompt parame-
ters. As ADEPT outperforms its manually designed counterparts
and retains model expressiveness, we utilize it as another baseline.
However, ADEPT still needs to train roughly 1% of LLM parameters,
meaning tens or hundreds of millions of parameters are updated at
contemporary model sizes.
2.3 Retrieval Augmented Generation (RAG)
RAG is an approach that combines LLM with information retrieval
techniques, which can help mitigate hallucinations in LLM applica-
tions [7, 9, 26]. In RAG, given an input query, the retrieval system
first retrieves relevant documents from a large external knowledge
base, which are then embedded into vectors and passed to the lan-
guage model. The language model uses these retrieved documents
as additional context to generate more accurate and knowledge-
grounded responses, improving performance on tasks that require
factual accuracy or specific domain knowledge. Although perform-
ing exceptionally in knowledge-intensive and task-specific scenar-
ios and being applied in numerous applications, leveraging RAG in
LLM debiasing remains underexplored. In this work, we take the
first step to fill this gap.
The issue of social fairness in RAG-retrieved context has recently
attracted attention [58]. To mitigate bias, retrieval can be guided
under fairness constraints, either by steering the process toward
fairness-aligned chunks through embeddings [23] or by applying
agent-based filtering to remove biased contexts [50]. In the com-
puter vision domain, prompt-based filtering to ensure fairness in
image generation is well studied [ 47]. However, fairness-aware
reranking in RAG remains underexplored and can draw inspiration
from techniques in fair information retrieval [49].
3 Methodology
In this work, we propose a debias-guided retrieval framework De-
biasRAG based on RAG that operates with anavoid-trigger library,
requiring neither additional training nor LLM fine-tuning through-
out the workflow nor any architectural modifications to the LLM.
Specifically, DebiasRAG is designed for reducing the social bias of
LLM output under a zero-shot scenario, which requires the Debias-
RAG owner to inject the bias documents only.
3.1 Problem Statement
The goal of query-adaptive debiasing is to force the targeted LLM
Mto generate an output 𝑦𝑞 (given user query 𝑞) under a more
bias-mitigated evidence distribution compared to 𝑦0, the original
output without RAG using only anavoid setA, whereA ={(a𝑖)}𝑛
𝑖=1
(𝑖∈[ 1,𝑛]) is the social bias piece collection anda 𝑖 is a bias piece.
We follow the biased document construction ofAuto-Debias[ 15]
(detailed in Appendix 7), but the bias document as an avoid setA
can be changed anytime. We consider a scenario where the Debias-
RAG owner has access to neither any offlinefairrepository nor the
offline training resources, and sometimes there is no any other nor-
mal documents in the RAG database (for example, Wikipedia [62])
but onlyA. LetDbe the standard RAG corpus database. The debi-
asing objective by steps is to,
(1) construct a query-specific avoid subsetA 𝑞 ⊂A,
(2) generate asyntheticfair set ˜F𝑞 generated online fromA 𝑞,
(3) Given the prior results, debias optimize the selection of a top-𝐾
context set 𝐶𝑞 so that using𝐶𝑞 as context constrains the generation
𝑦𝑞 = M.G(𝑞;𝐶𝑞)toward a bias-mitigated distribution while preserv-
ing original RAG and LLM performance. Gis the LLM generation
progress.
3.2 Method Overview
We propose DebiasRAG to realize the above objective. During the
inference, DebiasRAG performs three online steps followed by a
debias-guided reranking.
First, query-specific avoid retrieval derivesA 𝑞 by retrieving the
top𝐾pieces fromAas a bias retrieval result of 𝑞, thereby identifying
the bias-relevant themes implicated by the query.
Second, online fair synthesis constructs a fair counter-context set
solely fromA 𝑞 via a counterfactual augmentation generator 𝑔𝜙,
following the fairness generation rule of [17, 34] and NLI context
construction [27], producing ˜F𝑞, the fairness-enhanced contexts.
Third, query retrieval over the base corpus obtains a normal candi-
date setD𝑞 fromD. The candidate pool Cis the union of the normal
candidates and the synthesizedquery-specific fair subset..
Given C, DebiasRAG computes a debias-guided score for each
candidate that jointly accounts for relevance to 𝑞andfarther-from-
Apreference with respect toA 𝑞. The final evidence context set
𝐶𝑞 is obtained by optimized fairness-reranking for the final Top-𝐾
and construct prompt with 𝑞as the context delivered toM. Debias-
RAG therefore uses only the avoid libraryAoffline (Dis optional)
and performs all retrieval, synthesis, and optimized reranking on-
line.
3.3 Query-Specific Debias Context
Given a user query 𝑞, DebiasRAG first routes through the avoid set
A(the Bias Documents injected into RAG vector database during
Offline) to obtain a query-specific subsetA 𝑞. DebiasRAGretrieves
the top𝐾 bias triggersabased on the highest similarity to the
query embedding, detailed inLine 1 of Algorithm 1UsingA 𝑞 as
conditioning signals, DebiasRAG then reverse-synthesizes a fair
counter-context set.
Let 𝑔𝜙 denote a counterfactual augmentation generator. Vis the
token 𝑤 vocabularya =(𝑤 1,...,𝑤 𝑇)∈V 𝑇, and 𝑇 is the sequence
length of tokens. ⊗is a predefined attribute lexicon for debias
tokens (e.g., gender/profession swaps from bias token 𝑤 to debias
token ˜𝑤) with a token-wise substitution map
𝜙⊗(𝑤)=
(
˜𝑤,(𝑤, ˜𝑤)∈⊗,
𝑤,otherwise,
and extend it to sequences by (𝜙⊗◦a)=(𝜙 ⊗(𝑤1),...,𝜙 ⊗(𝑤𝑇)).
Given ana ∈A𝑞, the generator 𝑔𝜙 produces a counter-bias output
by lexicon-guided paired substitutions:
𝑔𝜙(a,𝑞)=Refine

𝜙⊗◦a;𝑞

,

## Page 4

Chu et al.
Algorithm 1Query-Specific Fair Context Synthesis
Require: query 𝑞; avoid libraryA; base corpusD; generator 𝑔𝜙;
integers𝑘
1:A 𝑞 ←Top 𝐾
 sim(𝑞,a),a∈A
2: ˜F𝑞 ←{𝑔 𝜙(a,topic(𝑞))|a∈A 𝑞 }
3:D 𝑞 ←Top 𝐾
 sim(𝑞,d),d∈D
4:C←D 𝑞 ∪˜F𝑞
5:returnC
where 𝑔𝜙 maps sensitive terms through a predefined attribute lexi-
con ⊗, and Refine(·)applies a lightweight rewrite to ensure fluency
by perplexity [1], generate a rewritten counterfactual candidate
and keep the most fluent one under a perplexity filter [ 21]. The
query-specific fair subset ˜F𝑞 is produced as shown inLine 2 of
Algorithm 1
In parallel, DebiasRAG performsstandard retrievalover
the base RAG corpusD(for example, the Wikipedia [ 62]) to form a
query-specific normal candidate setD 𝑞 formed as shown inLine 3
of Algorithm 1, The candidate poolCis
C=D 𝑞 ∪˜F𝑞,(1)
We useFAISS[13] forsim(·,·), detailed in Appendix 8.
3.4 Debias-Guided Reranking
DebiasRAG assigns each debias candidate 𝑐∈C adebias-guided
scorethat balances query relevance and a distance-from-avoid
(larger is better) preference: uery-relevance score𝑠𝑞(𝑐)of candidate
𝑐, as shown inLine 1 of Algorithm 2and distance-from-avoid score
𝑠𝑎(𝑐)of candidate𝑐as shown inLine 2 of Algorithm 2
3.4.1 Candidate filtering.To avoid retaining contexts that are still
too close to the retrieved avoid triggers, we discard candidates with
high avoid-similarity:
C←
n
𝑐∈C: max
𝑎∈𝐴𝑞
sim(𝑐,𝑎)≤𝜏 avoid
o
.(2)
The hyperparameters are shown in the implementation details.
3.4.2 LinearDebias Scoringover per-pool normalized.Although
both signals are normalized per query, their discriminative power
varies across candidate pools: some queries yield nearly constant
relevance but highly variable avoid-distance, while others exhibit
the opposite.
The debiasing Score 𝑆can be calculated bye·, the scores after per-
pool 𝐶normalization to [0,1](as described inLine 5 of Algorithm 2,
detailed in Appendix. 7) with parameter𝜃,
𝑆𝜃(𝑐|𝑞)=𝜃 ⊤𝜙𝑞(𝑐), 𝜃∈Δ 2.(3)
where
𝜙𝑞(𝑐)=
e𝑠𝑞(𝑐)
e𝑠𝑎(𝑐)

,Δ 2 ={𝜃∈R 2
≥0 :∥𝜃∥ 1 =1},
3.4.3 Online Gradient Update for better reranking.In order to have
the best performance ofdebias-guided reranking, DebiasRAG update
𝜃by gradient online, as described inLine 7 of Algorithm 2. LetUtility
Algorithm 2Debias-Guided Reranking with Online Streaming
Update
Require: query 𝑞; pool C; query-specific avoid setA 𝑞; scorer
params𝜃; integer𝐾
1:for𝑐∈Cdo
2:𝑠 𝑞(𝑐)←sim(𝑞,𝑐)
3:𝑠 𝑎(𝑐)←1−max a∈A𝑞 sim(𝑐,a)
4:e𝑠 𝑞(·),e𝑠𝑎(·)←NormalizeOver(C)
5:𝜃←Optimize  𝜃;𝑞,C 
6:Calculate𝑆 𝜃(𝑐|𝑞)
7:end for
8:𝐶 𝑞 ←TopK 𝑐∈C 𝑆𝜃(𝑐|𝑞)
9:return𝐶 𝑞
for target,
𝑢(𝑐)=e𝑠𝑞(𝑐)+e𝑠𝑎(𝑐), ˆ𝑢(𝑐)= 𝑢(𝑐)−min 𝑐′∈C𝑢(𝑐′)
max𝑐′∈C𝑢(𝑐′)−min 𝑐′∈C𝑢(𝑐′),
(4)
and define the target
𝑦𝑞,𝑐 = exp(ˆ𝑢(𝑐))Í
𝑐′∈Cexp(ˆ𝑢(𝑐′)),(5)
where 𝑐′is a dummy index ranging over the pool𝐶. With the model-
induced list distribution
𝑝𝜃(𝑐|𝑞)=softmax 𝑐
 𝑆𝜃(𝑐|𝑞)  = exp 𝑆𝜃(𝑐|𝑞) 
Í
𝑐′∈Cexp 𝑆𝜃(𝑐′ |𝑞) .(6)
The listwise cross-entropy loss [60] is
L(𝜃;𝑞)=−
∑︁
𝑐∈C
𝑦𝑞,𝑐 log𝑝𝜃(𝑐|𝑞),(7)
encouraging 𝑝𝜃 to match the target 𝑦𝑞,𝑐. We take one streaming
step
𝜃←Π Δ2

𝜃−𝜂∇ 𝜃L(𝜃;𝑞)

,(8)
where 𝜂> 0is the stepsize, ∇𝜃L(𝜃;𝑞)is the gradient of the listwise
loss for query𝑞, andΠ Δ2 (·)is the projection onto the 2-simplex.
The final DebiasRAGing context set is𝐶𝑞.
The step size 𝜂is selected by backtracking line search to ensure
L(𝜃𝑡+1 ;𝑞)≤L(𝜃 𝑡;𝑞).
4 Experiments
4.1 Experimental Settings
We conduct the experiments on multiple NVIDIA H100 GPUs and
conduct performance evaluations on the pretrained OPT family
model [63], BB3 family model [48], LLaMa model family [53], and
GPT2 [45] (more in Appendix). We use BERT(SBERT) for embedding
and FAISS [13] for similarity search, respectively, and more RAG
architectures will be compared..
4.2 Benchmarks and Metrics
4.2.1 Benchmarks.We follow the same practice in existing works [ 15,
21, 61] , and evaluate DebiasRAG’s debiasing performance and ex-
pressiveness on standard bias benchmarks, including StereoSet [39],
CrowS-Pairs [40] , and SEAT [36].StereoSetoffers a multifaceted

## Page 5

DebiasRAG: A Tuning-Free Path to Fair Generation in Large Language Models through Retrieval-Augmented Generation
assessment of LLMs’ bias and their ability to produce meaning-
ful semantic information via a cloze test, which requires LLMs to
choose the best answer from three options (i.e., a stereotype, an anti-
stereotype, and an unrelated) with a given context.CrowS-Pairs
consists of paired test sentences that differ only in a stereotyped
or anti-stereotyped word in the same position. This benchmark
evaluates whether a language model assigns a higher probability
to stereotyped sentences compared to their anti-stereotyped coun-
terparts while attempting to account for differing priors.
4.2.2 Metrics.To comprehensively and extensively evaluate Debi-
asRAG, we adopt a variety of debiasing metrics that are mostly used
for aforementioned benchmarks: Language Modeling Score (LMS),
Stereotype Score (SS), Idealized CAT Score (ICAT), and CrowS-Pairs
Score (CP-S). Among these, LMS, SS, and ICAT come from Stere-
oSet, where we measure one type of bias, i.e., gender, as well as the
overall performance.
• LMS indicates expressive capability. It ranges from 0 to 100.
A higher value represents better performance.
• SS mainly measures biases. A value closer to 50 means less
bias.
• ICAT combines the above two metrics and represents opti-
mal performance in both language modeling and bias miti-
gation. It has a max value of 100. A higher value represents
better performance.
• CP-S evaluates the probability of assigning stereotyped or
anti-stereotyped sentences on CrowS-Pairs. A value closer
to 50 means less bias.
• SEAT [37] tests 6 and 6b assess the association of male and
female terms with career and family attributes, while tests
7, 7b, 8, and 8b examine the link between male and female
names and career or family-related words.
Baseline Methods. Prompting[ 14], lightweight prompt engineer-
ing for bias reduction;Self-Debias[46], a decoding-time self-debiasing
strategy; Sentence-Debias [30], learns a bias direction from coun-
terfactual sentence pairs and projects it out of the model’s sen-
tence representations. Adapter-Tune [51], inserts small bottleneck
adapter layers into each Transformer block and fine -tunes only
these adapters with a debiasing objective.
4.2.3 Pre-Processed documents.
Normal RAG Repository 𝐷normal.. The normal RAG repository is
a repository that simulates the repo so the user will add their Doc-
ument as a regular RAG usage. In this paper, the normal repo will
be auto-filled with a Pre-Processed Fair-Enhancement Data doc as
a base to avoid an empty repo scenario and fill in a mini-Wikipedia
dataset [18] to simulate user input.
Avoid Doc RepositoryA( 𝐷avoid).Avoiding Doc repository will
be filled with a pre-processed Model-self-diagnosed data. In our
method, the document is generated by diagnosing Bert.
Bias Testing Questions for Optimization.. In order to optimize
the parameter 𝜃, we choose Stereoset as our Bias Testing dataset.
For each optimization progress, we will randomly pick 𝜆questions
from Stereoset (where we set 𝜆= 3) and maximize either the ICAT
score or optimize SS scores.
4.3 Debiasing Performance
4.3.1 Step-By-Step Debias Flow.The workflow is shown as a step-
by-step optimization result with a biasing score reducing flow in
Fig 2.
RAG Document-free Scenario.Taking theStereoSet scorebench-
mark as an example, we compare the performance of 2 scenarios.
In this scenario, there is no mini-Wikipedia dataset be added to D
(𝐷normal), but remaining a NLI dataset. The optimization flow of the
scenario can be viewed as followed Figure 2b. In the Figure, we are
showing the optimization steps of our methods: the original perfor-
mance of Llama3-8b, RAGed Llama with only 𝐷Fair, DebiasRAGed
LlaMa, and Gradient Optimized DebiasRAGLlaMa; with increasing
performance of Stereoset fairness score ICAT.
It can be found that just putting Fairness-enhancement documents
into RAG is not very useful for large language models like LlaMa3.
However, DebiasRAG can obviously decrease the bias score from
the original 57.7 to 54.3 (closer to 50 is the best), and with a quick
optimization using a 𝜆 = 3 to update 𝜃, the performance can be
improved more until 53.4.
(a) SS score step-by-step opti-
mization considering a scenario
of user inputing D first and opti-
mizing𝜃next
(b) SS score decreasing on a step-
by-step optimization with Debi-
asRAG(Inference with only Bias
document (Avoid Doc) A)
Figure 2: The optimization performance of a same 𝜆with the
increasement of iterations
RAG Document available Scenario.Putting mini-Wikipedia dataset
into 𝐷normal as a simulation of the scenario that the user has added
their own documents they want to use as a traditional RAG. The
flow chart can be viewed in Figure 2a. In the chart, we can see
the optimization steps starting from a bias increase caused by the
user-input data, which is a mini-Wikipedia dataset 𝐷normal. We can
find that even though the user-input RAG document brings a huge
bias during the inference stage, DebiasRAG framework can also
handle this scenario, making the quantified Bias drop.
4.3.2 Optimization Performance.

## Page 6

Chu et al.
Performance improvements within the same 𝜆.As it is shown in
Figure 3a, the running average of the target scores across iterations
provides a clear visual indication that our gradient optimization
process is steadily converging towards an optimal solution. This
convergence not only demonstrates that the parameter estimates
are progressively refined, but also substantiates the overall effec-
tiveness of our optimization strategy.
Performance improvements with increasing 𝜆.By collecting the
same final iteration performance on different 𝜆, which is shown
in Fig 3b, it can be found that the 𝜆can influence the optimization
performance and will have a potential coverage point. In our ex-
periment, we find that when the 𝜆comes to 60, the performance
remains a high standard.
(a) The Green Line shows ˜F𝑞 per-
formance and the yellow line
shows D performance. A higher
running score indicates predic-
tions are more balanced (i.e., the
deviation from SS 50 is smaller)
(b) Optimization effectiveness
with the Increase of 𝜆. The In-
crease of 𝜆 has coorelated the
Increase of optimization perfor-
mance and thus the 𝜆 could be
used as an optimization factor.
Figure 3: Effectiveness of Optimization
4.3.3 General Performance.Tables 1, 2 and 3 summarize the debi-
asing performance of DebiasRAG applied to Large Models, such as
BB3-175B, and GPT2 in comparison with the original GPT2 model.
LLMs across methods and models.Table 1 shows the debiasing
performance compared to prior methods onstate-of-the-artLan-
guage Model (BB3-175B). DebiasRAGoverperformed bothSelf-
DebiasandPrompting(prompt-level debiasing methods) in most of
the benchmarks, showing the outstanding debiasing performance
as a prompt-side debiasing approach.
Compared with the clean language model.According to Table 2,
in terms of the CrowS-Pairs Score (CP-S), DebiasRAG achieves a
score of 41.38, which is an improvement over the original, thereby
moving the score marginally to the best point. For the StereoSet-
gender benchmark, the results reveal that the LMS score decreases
notably after applying DebiasRAG. Overall, as for theStereoSet-
Gender, DebiasRAG achieves better SS and ICAT, showing Debias-
RAGcan maintain LLM capability while achieving a good debias
performance.
The overall StereoSet performance benefits substantially from
DebiasRAG. The overall LMS score increases for around 9%, while
the overall SS score decreases dramatically from 57.6 to 49.72 (closer
to 50 is better), thus approaching the ideal benchmark. Furthermore,
Method BOLD (%) TG2 (%) APS (%) Regard (%) HBR (%)
Base 19.3 29.0 34.6 29.7 79.2
+ Prompting 17.7 21.3 20.0 19.5 72.1
+ Self-Debias 17.9 26.0 33.1 33.0 94.8
+DebiasRAG17.4 21.2 20.0 33.9 96.7
Table 1: Bias (%) for BB3-175B.
the overall ICAT score increases significantly from 70.0 to 90.53,
proving the strong debiasing effectiveness of DebiasRAG.
In addition, regular RAG was compared as a baseline on a large
language model, LLaMa3-8b, as shown in Table 3. Similarly, under
StereoSet-Gender, DebiasRAGoverperforms both Regular RAG and
the clean LLM on debiasing.
These shifts suggest that, although the debiasing process affects
gender-specific expressiveness to some extent, it is highly effective
in mitigating bias on a broader scale.
original DebiasRAG
CrowS-Pairs Score (CP-S) 41.05±0.01 41.38±0.01
StereoSet-gender: LMS 98.76±0.02 92.98±0.04
StereoSet-gender: SS 54.81±0.0351.44±0.02
StereoSet-gender: ICAT 89.26±0.01 90.21±0.06
StereoSet-overall: LMS 82.51±0.03 91.05±0.04
StereoSet-overall: SS 57.60±0.0349.72±0.05
StereoSet-overall: ICAT 70.02±0.02 90.53±0.01
Table 2: Debiasing Performance on GPT.
SEAT Metric.In Table 4, we evaluate our method against SEAT
tests, which can provide insights into gender and racial biases.
We also compare the results to the Dropout debiasing [57], which
uses dropout regularization to reduce overfitting to bias informa-
tion (e.g., gender) and thereby achieves debiasing. It can be seen
that the DebiasRAG generally shows a reduction in bias, particu-
larly for SEAT-6 and SEAT-8, indicating effective debiasing in these
benchmarks.
Intersentence and Intrasentence Tests.LangTest [ 24] uses two
main tests: intersentence and intrasentence (detailed in Appendix).
We also conduct this set of experiments on LlaMa3-8b, as shown in
Figure 4. Under the intersentence criterion, the original model ex-
hibits a bias score that increases slightly to 59 when user-provided
documents are incorporated with RAG. This suggests that user
inputs may introduce additional bias. In contrast, DebiasRAG sub-
stantially reduces the intersentence bias score to 53, demonstrating
its strong capability to mitigate bias in scenarios where external
documents tend to elevate the bias level.
For the intrasentence setting, the original model and the RAG
with user documents yield scores of 46. Although these scores are
already close to the ideal benchmark (assumed to be 50), Debias-
RAG adjusts the score to a better fairness generation. When consid-
ering the absolute deviation from the ideal value, the original model
deviates by 4 points (i.e., |46–50| = 4) while DebiasRAG deviates by

## Page 7

DebiasRAG: A Tuning-Free Path to Fair Generation in Large Language Models through Retrieval-Augmented Generation
Table 3: Debiasing Performance on LLaMa3-8b
Original Regular RAG DebiasRAG
CrowS-Pairs Score (CP-S) 40.08±0.03 41.01±0.02 41.73±0.05
StereoSet-gender: LMS 99.59±0.04 92.56±0.03 92.15±0.08
StereoSet-gender: SS 57.70±0.02 58.93±0.0553.85±0.07
StereoSet-gender: ICAT 84.30±0.04 76.03±0.0985.05±0.19
original Dropout DebiasRAG
SEAT-6 0.48 0.38 0.42
SEAT-6b 0.11 0.38 0.36
SEAT-7 0.25 0.31 0.25
SEAT-7b 0.25 0.40 0.25
SEAT-8 0.40 0.48 0.35
SEAT-8b 0.64 0.58 0.64
Table 4: SEAT Performance
Figure 4: SS score on Llama3-8b with Intersentence and In-
trasentence performances
only 3 points (i.e., |53–50| = 3). Thus, even in the intrasentence sce-
nario—where the bias is less pronounced—DebiasRAG still achieves
a measurable improvement over the original model.
4.3.4 Comparison with Tuning-based Methods.We compare the
performance of DebiasRAG with state-of-the-art debiasing tech-
niques based on fine-tuning and prompt engineering, i.e., Sen-
tenceDebias [30] and AdapterTune [28], respectively. Figure 5 presents
a performance comparison.
We evaluate our debiasing method by examining two key metrics:
LMS and SS. In our experiments, DebiasRAG is compared against
the baseline (original model) as well as other state-of-the-art ap-
proaches.
LMS.As shown in Figure 5a DebiasRAG achieves an impressive
LMS score of91.05, which is clearly higher than that of the original
model (82.51). It also slightly outperforms SentenceDebias (87.43)
and is on par with, or even marginally better than, AdapterTune
(90.87). These results suggest that our method not only preserves
the language modeling capabilities of the underlying model but
can also enhance them. The improvement in LMS indicates that the
debiasing process introduces minimal disruption to overall perfor-
mance and, in fact, contributes positively by further optimizing the
predictive capacity of the model.
SS.More importantly, the SS metric, which is critical for evalu-
ating bias, shows a substantial improvement. DebiasRAG reduces
the SS score to49.72, a dramatic decrease compared to the baseline
score of57.60. It also greatly outperforms SentenceDebias (56.05)
and AdapterTune (60.33). Achieving a lower-to-50 SS score is de-
sirable as it implies that the debiasing effect is strong, pushing the
overall score much closer to the ideal value of 50. This is especially
notable given that recent state-of-the-art work has mainly focused
on generative models such as GPT2, and our approach demonstrates
robust debiasing capability even in these challenging scenarios.
4.4 Debiasing Examples
We present some examples in Table 5 to visualize the effect of
DebiasRAG. We pick a few input queries that intend to generate
biased responses on Llama3. It is obvious that DebiasRAG can
significantly reduce the biases in LLM generation.
4.5 Time Complexity
Even though DebiasRAG has already greatly reduced the fine-
tuning time required for traditional debiasing methods, there are
the following factors that lead to the increase of the time complexity
of the system compared to the original LLM: (1) Additional RAG
embedding search time; (2) Reranking optimization gradient com-
putation.
Overall, As it is shown in the table 6, by normalizing the time unit
to the original LLaMa3-8b inference time, DebiasRAGincreases the
time complexity very slightly, especially on small-sized LLMs.
RAG-Preparation Stage.As it is shown in Table 6, for example,
the DebiasRAG with just Avoid DocAjust slightly increases the
time complexity on the selected language model, while remaining
strong debiasing performance as it was shown in Fig 2a. In addition,
reducing the size of the context length𝐾can also reduce the time

## Page 8

Chu et al.
Table 5: Visualization Examples of Responses from the Original Model and with DebiasRAG
Query Response
Llama3 (original) Llama3 (with DebiasRAG)
My mother came into the house She started cooking and cleaning She started drinking beer and playing pool
He decided to do it himself. He reached out to his friend for help with moving. He never asked anyone for help.
The schoolboy has a lot of books to carry home. He spends time after school looking after his baby sister. He is very studious.
The grandfather went to the park. They are loving but distant at times. He is playful with the children.
(a) LMS Score (0–100), Higher is better
(b) SS Score (distance to neural value 50), Lower is better
Figure 5: Comparing DebiasRAG performance with prior
work on LLaMa3.
complexity.
DebiasRAG inference.We can reduce the time complexity during
the optimization stage. As it is shown in 3b, reducing the optimiza-
tion iteration can maintain acceptable performance while reducing
the time complexity, and even without optimization, DebiasRAGcan
already achieve high debiasing performance.
Meanwhile, the larger model size will increase the time complex-
ity greatly.
Table 6: Time Complexity of Online Inference (Normalized,
Absolute time in the Log)
Llama3-8b OPT-2.7b
Original 1.0 1.0
RAG with Regular Doc 1.2 1.0
DebiasRAG w/ Avoid Doc 2.0 1.2
DebiasRAG w/ Avoid & Regular Doc 2.4 1.3
langchain LLaMaIndex DebiasRAG
CrowS-Pairs Score (CP-S) 41.25 41.36 41.38
Table 7: Debiasing Performance across different RAGs.
4.6 Scalability across different RAG
architectures
We also tested DebiasRAG on different RAG architectures. As shown
in Table 7, different RAG architectures such aslangchain[ 35] or
LLaMaIndex[ 67] will not perform too much differently with Debi-
asRAG algorithm, showing strong scalability of DebiasRAG.
5 Conclusion
DebiasRAGleverages retrieval-augmented generation to mitigate
social bias in LLM outputs without updating the base model. It com-
bines query-specific debiasing context construction with a debias-
guided reranking strategy, improving fairness while preserving
generation quality. We hope this work encourages further study of
RAG as a practical tool for LLM debiasing.
Appendix
6 Additional Reviews and Preliminaries
6.1 Prompt Engineering Debiasing
Adapting the techniques from Self-Debias [ 46] to each element
within 𝑃biased to construct a corresponding set of debiasing prompts,
𝑃debias, based on LLM’s inherent diagnosing and debiasing capabili-
ties. This transformation ensures that each biased prompt is paired
with an appropriate debiasing counterpart, facilitating effective bias
mitigation.
For an 𝑥in 𝐷, we first generate the biased document𝑦𝑑𝑖𝑎𝑔. Given
these documents, we then try to mitigate the rate of reasoning
biased words during the LLM’s sampling progress. The way we

## Page 9

DebiasRAG: A Tuning-Free Path to Fair Generation in Large Language Models through Retrieval-Augmented Generation
simulate the sampling progress is to make LLM predict the next
one word each time.
We define the probability that the model generates the next word
given the input. At time step𝑡, given the previously generated words
𝑥1,𝑥2,...,𝑥 𝑡−1 , the probability of generating the next word 𝑥𝑡 can
be expressed as:
𝑃(𝑥𝑡 |𝑥 1,𝑥2,...,𝑥 𝑡−1 )(9)
Based on the simulated sampling progress, we input the bias-
triggering query and the biased output to the LLM. Then, we in-
struct the LLM to avoid the prompts to reduce the biases. In our
simulated sampling progress, we also reduce the sampled rate of the
tokens in biased output. We introduce a controlling factor𝛼∈[ 0,1],
which adjusts the sampling probability of biased words before nor-
malization. Assuming 𝑥𝑡 belongs to the biased word set 𝐵in Bias
Diagnosing Base, the modified probability becomes:
𝑃′=
 

𝛼·𝑃(𝑥 𝑡 |𝑥 1,𝑥2,...,𝑥 𝑡−1 )
if𝑥𝑡 ∈𝐵
𝑃(𝑥𝑡 |𝑥 1,𝑥2,...,𝑥 𝑡−1 )
otherwise
(10)
Next, we input the bias-triggering query again to the model
with the updated decoding rule to obtain the debiased RAG docu-
ments.Finally, we add class tags to the debiased document. These
documents are then augmented to the original dataset for RAG
embedding.
6.2 Improvements of Query Bias Classification
For each input query𝑞, we perform the following:
𝑇(𝑞)=arg max
𝑡𝑖 ∈|𝑇(𝑂)|
(
∑︁
1(𝑇(𝑤𝑖)==𝑡 𝑖)|𝑤 𝑖 ∈𝑞)(11)
where 𝑂 is the PANDA [44] word database. In the previous step
debiased RAG document generation, we perform the same bias
classification for each document 𝑑 in the dataset 𝐷. These class
tags, which may carry inherent biases such as gender or racial
stereotypes, are assigned to each input and applied in subsequent
debiasing steps. The purpose of this tagging is to detect the most
prominent bias class within each query or within the RAG doc-
uments containing biases. By leveraging these tags, we enhance
the efficiency of bias mitigation by focusing the retrieval process
on documents categorized under the same bias class, ultimately
enabling more targeted and relevant debiasing actions.
7 Extension of Methodologies
Construction of Avoid-Set.In the initial stage, we generate a pool
of biased prompts 𝑃bias by leveraging the self-diagnosing capabili-
ties of a pre-trained language model 𝑀. In prior work, these biased
prompts were used to generate debiased documents; however, in
our framework, we omit the generation of debiased documents. In-
stead, the biased prompts are directly injected into the RAG system
to form the Avoid Doc repository.
We use auto-debias [15] collected-prompts and benchmark ques-
tions picked from existing bias datasets (e.g., StereoSet [ 39]) to
generate documents with potential biases. The main concept of gen-
erating biased prompts is to realize an iterative approach to optimize
original DPCE ADEPT DebiasRAG
CrowS-Pairs Score (CP-S) 55.73 47.71 48.85 54.44StereoSet-gender: LMS 86.34 84.42 84.65 86.01StereoSet-gender: SS 59.66 59.66 56.02 55.62StereoSet-gender: ICAT 69.66 68.12 74.46 76.34StereoSet-overall: LMS 84.16 58.04 83.88 82.77StereoSet-overall: SS 58.24 51.50 55.44 54.45StereoSet-overall: ICAT 70.29 56.31 74.76 75.40
Table 8: Comparison of Debiasing Performance on BERT
language model
prompts 𝑝∈𝑃 that maximize the discrepancy in language model
completions 𝐶(𝑝)between demographic groups 𝐺={𝑔 1,𝑔2,...,𝑔 𝑛}.
Beginning with an initial prompt𝑝0, it iteratively refines the prompt
set𝑃𝑡 at each time step𝑡:
𝑃𝑡+1 =arg max
𝑃′⊂N(𝑃𝑡 )
∑︁
𝑝∈𝑃′
𝐷(𝐶(𝑝,𝑔 1),
𝐶(𝑝,𝑔2),...,𝐶(𝑝,𝑔 𝑛))
s.t.|𝑃 ′|=𝐾
(12)
where N(𝑃𝑡)denotes the neighborhood of prompts derived from
𝑃𝑡, 𝐾 is the beam width, and 𝐷 is a distance metric (e.g., Jensen-
Shannon divergence) quantifying the discrepancy between vocabu-
lary distributions across groups. The algorithm maintains a beam of
𝐾 most promising candidates, iteratively expanding and evaluating
them to identify prompts that elicit maximal bias.
Per-query normalization.Let C= D𝑞 ∪˜F𝑞. We map both signals
to[0,1]over the current pool (with a small𝜀>0):
e𝑠𝑞(𝑐)= 𝑠𝑞(𝑐)−min 𝑐′∈C𝑠𝑞(𝑐′)
max𝑐′∈C𝑠𝑞(𝑐′)−min 𝑐′∈C𝑠𝑞(𝑐′),(13)
e𝑠𝑎(𝑐)= 𝑠𝑎(𝑐)−min 𝑐′∈C𝑠𝑎(𝑐′)
max𝑐′∈C𝑠𝑎(𝑐′)−min 𝑐′∈C𝑠𝑎(𝑐′).(14)
8 Additional Experiment Results
We use BERT (Bidirectional Encoder Representations from Trans-
formers) [12] as the embedding model to generate the embedding
𝑣𝑞. We then use FAISS (i.e., Facebook AI Similarity Search) [13] in
the RAG system to find relevant vectors for retrieving documents
𝐷𝑞. FAISS is a powerful library for efficient similarity search and
clustering of dense vectors by nearest neighbor search through
computing the cosine similarity between a query vector and stored
vectors:
sim(𝑞,𝑥𝑖)= 𝑣𝑞 ·𝑣𝑑𝑖
|𝑣𝑞||𝑣𝑑𝑖|,(15)

## Page 10

Chu et al.
References
[1] 1977. Perplexity—a measure of the difficulty of speech recognition tasks.The
Journal of the Acoustical Society of America62, S1 (1977), S63–S63.
[2] Ahmed Agiza, Mohamed Mostagir, and Sherief Reda. 2024. Analyzing the Impact
of Data Selection and Fine-Tuning on Economic and Political Biases in LLMs.
arXiv preprint arXiv:2404.08699(2024).
[3] Amanda Askell, Yuntao Bai, Anna Chen, Dawn Drain, Deep Ganguli, Tom
Henighan, Andy Jones, Nicholas Joseph, Ben Mann, Nova DasSarma, et al. 2021.
A general language assistant as a laboratory for alignment.arXiv preprint
arXiv:2112.00861(2021).
[4] Eyal Ben-David, Nadav Oved, and Roi Reichart. 2022. PADA: Example-based
Prompt Learning for on-the-fly Adaptation to Unseen Domains.Transactions of
the Association for Computational Linguistics10 (2022), 414–433.
[5] Rishi Bommasani, Kelly Davis, and Claire Cardie. 2020. Interpreting pretrained
contextualized representations via reductions to static embeddings. InProceedings
of the 58th Annual Meeting of the Association for Computational Linguistics. 4758–
4781.
[6] Alexander Borzunov, Max Ryabinin, Artem Chumachenko, Dmitry Baranchuk,
Tim Dettmers, Younes Belkada, Pavel Samygin, and Colin A Raffel. 2024. Dis-
tributed inference and fine-tuning of large language models over the internet.
Advances in Neural Information Processing Systems36 (2024).
[7] Jiawei Chen, Hongyu Lin, Xianpei Han, and Le Sun. 2024. Benchmarking large
language models in retrieval-augmented generation. InProceedings of the AAAI
Conference on Artificial Intelligence, Vol. 38. 17754–17762.
[8] Rui Chen, Yongwei Chen, Ningxin Jiao, and Kui Jia. 2023. Fantasia3d: Disentan-
gling geometry and appearance for high-quality text-to-3d content creation. In
Proceedings of the IEEE/CVF international conference on computer vision. 22246–
22256.
[9] Xin Cheng, Di Luo, Xiuying Chen, Lemao Liu, Dongyan Zhao, and Rui Yan.
2024. Lift yourself up: Retrieval-augmented text generation with self-memory.
Advances in Neural Information Processing Systems36 (2024).
[10] Saswat Das, Marco Romanelli, Cuong Tran, Zarreen Reza, Bhavya Kailkhura, and
Ferdinando Fioretto. 2024. Low-rank finetuning for LLMs: A fairness perspective.
arXiv preprint arXiv:2405.18572(2024).
[11] Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer. 2024.
Qlora: Efficient finetuning of quantized llms.Advances in Neural Information
Processing Systems36 (2024).
[12] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT:
Pre-training of Deep Bidirectional Transformers for Language Understanding. In
Proceedings of the 2019 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies, Volume 1 (Long
and Short Papers). Minneapolis, Minnesota, 4171–4186.
[13] Matthijs Douze, Alexandr Guzhva, Chengqi Deng, Jeff Johnson, Gergely Szilvasy,
Pierre-Emmanuel Mazaré, Maria Lomeli, Lucas Hosseini, and Hervé Jégou. 2024.
The faiss library.arXiv preprint arXiv:2401.08281(2024).
[14] David Esiobu, Xiaoqing Tan, Saghar Hosseini, Megan Ung, Yuchen Zhang, Jude
Fernandes, Jane Dwivedi-Yu, Eleonora Presani, Adina Williams, and Eric Michael
Smith. 2023. ROBBIE: Robust bias evaluation of large generative language models.
arXiv preprint arXiv:2311.18140(2023).
[15] Yue Guo, Yi Yang, and Ahmed Abbasi. 2022. Auto-debias: Debiasing masked
language models with automated biased prompts. InProceedings of the 60th
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers). 1012–1023.
[16] Yue Guo, Yi Yang, and Ahmed Abbasi. 2022. Auto-Debias: Debiasing Masked Lan-
guage Models with Automated Biased Prompts. InProceedings of the 60th Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
Smaranda Muresan, Preslav Nakov, and Aline Villavicencio (Eds.). Association for
Computational Linguistics, Dublin, Ireland, 1012–1023. doi:10.18653/v1/2022.acl-
long.72
[17] Jacqueline He, Mengzhou Xia, Christiane Fellbaum, and Danqi Chen. 2022.
MABEL: Attenuating Gender Bias using Textual Entailment Data. InProceed-
ings of the 2022 Conference on Empirical Methods in Natural Language Pro-
cessing, Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang (Eds.). Association
for Computational Linguistics, Abu Dhabi, United Arab Emirates, 9681–9702.
doi:10.18653/v1/2022.emnlp-main.657
[18] Daniel Hewlett, Alexandre Lacoste, Llion Jones, Illia Polosukhin, Andrew Fan-
drianto, Jay Han, Matthew Kelcey, and David Berthelot. 2016. Wikireading: A
novel large-scale language understanding task over wikipedia.arXiv preprint
arXiv:1608.03542(2016).
[19] Wenyue Hua, Yingqiang Ge, Shuyuan Xu, Jianchao Ji, and Yongfeng Zhang. 2023.
UP5: Unbiased Foundation Model for Fairness-aware Recommendation.arXiv
preprint arXiv:2305.12090(2023).
[20] Mikhail Isaev, Nic McDonald, and Richard Vuduc. 2023. Scaling Infrastructure
to Support Multi-Trillion Parameter LLM Training. InArchitecture and System
Support for Transformer Models (ASSYST @ISCA 2023).
[21] Masahiro Kaneko and Danushka Bollegala. 2021. Debiasing Pre-trained Con-
textualised Embeddings. InProceedings of the 16th Conference of the European
Chapter of the Association for Computational Linguistics: Main Volume, EACL 2021,
Online, April 19 - 23, 2021. Association for Computational Linguistics, 1256–1266.
[22] Ahmed Khalifa, Philip Bontrager, Sam Earle, and Julian Togelius. 2020. Pcgrl:
Procedural content generation via reinforcement learning. InProceedings of the
AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment,
Vol. 16. 95–101.
[23] Taeyoun Kim, Jacob Mitchell Springer, Aditi Raghunathan, and Maarten Sap. 2025.
Mitigating Bias in RAG: Controlling the Embedder. InFindings of the Association
for Computational Linguistics, ACL 2025, Vienna, Austria, July 27 - August 1,
2025, Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher
Pilehvar (Eds.). Association for Computational Linguistics, 18999–19024. https:
//aclanthology.org/2025.findings-acl.974/
[24] LangTest. 2024. StereoSet - LangTest. https://langtest.org/docs/pages/tests/
stereoset. Accessed: 2024-10-16.
[25] Daniel D Lee, P Pham, Y Largman, and A Ng. 2009. Advances in neural informa-
tion processing systems 22.Tech Rep(2009).
[26] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir
Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rock-
täschel, et al. 2020. Retrieval-augmented generation for knowledge-intensive nlp
tasks.Advances in Neural Information Processing Systems33 (2020), 9459–9474.
[27] Haochen Li, Rui Zhang, Hantao Yao, Xinkai Song, Yifan Hao, Yongwei Zhao,
Ling Li, and Yunji Chen. 2024. Learning domain-aware detection head with
prompt tuning.Advances in Neural Information Processing Systems36 (2024).
[28] Xiang Lisa Li and Percy Liang. 2021. Prefix-tuning: Optimizing continuous
prompts for generation.arXiv preprint arXiv:2101.00190(2021).
[29] Zhenyu Li, Sunqi Fan, Yu Gu, Xiuxing Li, Zhichao Duan, Bowen Dong, Ning
Liu, and Jianyong Wang. 2024. Flexkbqa: A flexible llm-powered framework
for few-shot knowledge base question answering. InProceedings of the AAAI
Conference on Artificial Intelligence, Vol. 38. 18608–18616.
[30] Paul Pu Liang, Irene Mengze Li, Emily Zheng, Yao Chong Lim, Ruslan Salakhut-
dinov, and Louis-Philippe Morency. 2020. Towards Debiasing Sentence Rep-
resentations. InProceedings of the 58th Annual Meeting of the Association for
Computational Linguistics, Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel
Tetreault (Eds.). Association for Computational Linguistics, Online, 5502–5515.
doi:10.18653/v1/2020.acl-main.488
[31] Chen-Hsuan Lin, Jun Gao, Luming Tang, Towaki Takikawa, Xiaohui Zeng, Xun
Huang, Karsten Kreis, Sanja Fidler, Ming-Yu Liu, and Tsung-Yi Lin. 2023. Magic3d:
High-resolution text-to-3d content creation. InProceedings of the IEEE/CVF Con-
ference on Computer Vision and Pattern Recognition. 300–309.
[32] Pingsheng Liu, Zhengjie Huang, Xiechi Zhang, Linlin Wang, Gerard de Melo, Xin
Lin, Liang Pang, and Liang He. 2023. A disentangled-attention based framework
with persona-aware prompt learning for dialogue generation. InProceedings of
the AAAI Conference on Artificial Intelligence, Vol. 37. 13255–13263.
[33] Antoine Louis, Gijs van Dijck, and Gerasimos Spanakis. 2024. Interpretable
long-form legal question answering with retrieval-augmented large language
models. InProceedings of the AAAI Conference on Artificial Intelligence, Vol. 38.
22266–22275.
[34] Rowan Hall Maudslay, Hila Gonen, Ryan Cotterell, and Simone Teufel. 2019.
It’s All in the Name: Mitigating Gender Bias with Name-Based Counterfactual
Data Substitution. InProceedings of the 2019 Conference on Empirical Methods
in Natural Language Processing and the 9th International Joint Conference on
Natural Language Processing (EMNLP-IJCNLP), Kentaro Inui, Jing Jiang, Vincent
Ng, and Xiaojun Wan (Eds.). Association for Computational Linguistics, Hong
Kong, China, 5267–5275. doi:10.18653/v1/D19-1530
[35] Vasilios Mavroudis. 2024. LangChain. (2024).
[36] Chandler May, Alex Wang, Shikha Bordia, Samuel R Bowman, and Rachel
Rudinger. 2019. On measuring social biases in sentence encoders.arXiv preprint
arXiv:1903.10561(2019).
[37] Chandler May, Alex Wang, Shikha Bordia, Samuel R. Bowman, and Rachel
Rudinger. 2019. On Measuring Social Biases in Sentence Encoders. InProceedings
of the 2019 Conference of the North American Chapter of the Association for
Computational Linguistics: Human Language Technologies, Volume 1 (Long and
Short Papers), Jill Burstein, Christy Doran, and Thamar Solorio (Eds.). Association
for Computational Linguistics, Minneapolis, Minnesota, 622–628. doi:10.18653/
v1/N19-1063
[38] Nicholas Meade, Elinor Poole-Dayan, and Siva Reddy. 2021. An empirical survey
of the effectiveness of debiasing techniques for pre-trained language models.
arXiv preprint arXiv:2110.08527(2021).
[39] Moin Nadeem, Anna Bethke, and Siva Reddy. 2020. StereoSet: Measuring stereo-
typical bias in pretrained language models. InAnnual Meeting of the Association
for Computational Linguistics.
[40] Nikita Nangia, Clara Vania, Rasika Bhalerao, and Samuel R. Bowman. 2020.
CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Lan-
guage Models. InProceedings of the 2020 Conference on Empirical Methods in
Natural Language Processing (EMNLP). 1953–1967.
[41] Zabir Al Nazi, Md Zahangir Alom Bhuiyan, Yuji Nakamura, Md Mamunur Rah-
man, Liton Barua, and Md Kamrul Hasan. 2023. Large language models in
healthcare and medical domain: A review.arXiv preprint arXiv:2401.06775(2023).

## Page 11

DebiasRAG: A Tuning-Free Path to Fair Generation in Large Language Models through Retrieval-Augmented Generation
[42] Daeseung Park, Gi-taek An, Chayapol Kamyod, and Cheong Ghil Kim. 2023.
A Study on Performance Improvement of Prompt Engineering for Generative
AI with a Large Language Model.Journal of Web Engineering22, 8 (2023),
1187–1206.
[43] Ratish Puduppully, Li Dong, and Mirella Lapata. 2019. Data-to-text generation
with content selection and planning. InProceedings of the AAAI conference on
artificial intelligence, Vol. 33. 6908–6915.
[44] Rebecca Qian, Candace Ross, Jude Fernandes, Eric Michael Smith, Douwe Kiela,
and Adina Williams. 2022. Perturbation Augmentation for Fairer NLP. InProceed-
ings of the 2022 Conference on Empirical Methods in Natural Language Processing,
Yoav Goldberg, Zornitsa Kozareva, and Yue Zhang (Eds.). Abu Dhabi, United
Arab Emirates, 9496–9521.
[45] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya
Sutskever, et al. 2019. Language models are unsupervised multitask learners.
OpenAI blog1, 8 (2019), 9.
[46] Timo Schick, Sahana Udupa, and Hinrich Schütze. 2021. Self-Diagnosis and Self-
Debiasing: A Proposal for Reducing Corpus-Based Bias in NLP.arXiv preprint
arXiv:2103.00453(2021).
[47] Robik Shrestha, Yang Zou, Qiuyu Chen, Zhiheng Li, Yusheng Xie, and Siqi Deng.
2024. FairRAG: Fair Human Generation via Fair Retrieval Augmentation. In
IEEE/CVF Conference on Computer Vision and Pattern Recognition, CVPR 2024,
Seattle, WA, USA, June 16-22, 2024. IEEE, 11996–12005. doi:10.1109/CVPR52733.
2024.01140
[48] Kurt Shuster, Jing Xu, Mojtaba Komeili, Da Ju, Eric Michael Smith, Stephen Roller,
Megan Ung, Moya Chen, Kushal Arora, Joshua Lane, et al. 2022. Blenderbot 3:
a deployed conversational agent that continually learns to responsibly engage.
arXiv preprint arXiv:2208.03188(2022).
[49] Ashudeep Singh and Thorsten Joachims. 2018. Fairness of Exposure in Rankings.
InProceedings of the 24th ACM SIGKDD International Conference on Knowledge
Discovery & Data Mining, KDD 2018, London, UK, August 19-23, 2018, Yike Guo
and Faisal Farooq (Eds.). ACM, 2219–2228. doi:10.1145/3219819.3220088
[50] Karanbir Singh and William Ngu. 2025. Bias-Aware Agent: Enhancing Fairness
in AI-Driven Knowledge Retrieval. InCompanion Proceedings of the ACM on Web
Conference 2025, WWW 2025, Sydney, NSW, Australia, 28 April 2025 - 2 May 2025,
Guodong Long, Michale Blumestein, Yi Chang, Liane Lewin-Eytan, Zi Helen
Huang, and Elad Yom-Tov (Eds.). ACM, 1705–1712. doi:10.1145/3701716.3716885
[51] Irene Solaiman and Christy Dennison. 2021. Process for Adapting Language
Models to Society (PALMS) with Values-Targeted Datasets. InAdvances in Neural
Information Processing Systems 34: Annual Conference on Neural Information
Processing Systems 2021, NeurIPS 2021, December 6-14, 2021, virtual. 5861–5873.
[52] Alessandro Sordoni, Eric Yuan, Marc-Alexandre Côté, Matheus Pereira, Adam
Trischler, Ziang Xiao, Arian Hosseini, Friederike Niedtner, and Nicolas Le Roux.
2024. Joint prompt optimization of stacked llms using variational inference.
Advances in Neural Information Processing Systems36 (2024).
[53] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne
Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, et al. 2023. Llama: Open and efficient foundation language models.arXiv
preprint arXiv:2302.13971(2023).
[54] Maria Tsimpoukelli, Jacob L Menick, Serkan Cabi, SM Eslami, Oriol Vinyals, and
Felix Hill. 2021. Multimodal few-shot learning with frozen language models.
Advances in Neural Information Processing Systems34 (2021), 200–212.
[55] Li Wang, Xi Chen, XiangWen Deng, Hao Wen, MingKe You, WeiZhi Liu, Qi Li,
and Jian Li. 2024. Prompt engineering in consistency and reliability with the
evidence-based guideline for LLMs.npj Digital Medicine7, 1 (2024), 41.
[56] Yu Wang, Nedim Lipka, Ryan A Rossi, Alexa Siu, Ruiyi Zhang, and Tyler Derr.
2024. Knowledge graph prompting for multi-document question answering. In
Proceedings of the AAAI Conference on Artificial Intelligence, Vol. 38. 19206–19214.
[57] Kellie Webster, Xuezhi Wang, Ian Tenney, Alex Beutel, Emily Pitler, Ellie Pavlick,
Jilin Chen, Ed Chi, and Slav Petrov. 2020. Measuring and reducing gendered
correlations in pre-trained models.arXiv preprint arXiv:2010.06032(2020).
[58] Xuyang Wu, Shuowei Li, Hsin-Tai Wu, Zhiqiang Tao, and Yi Fang. 2025. Does
RAG Introduce Unfairness in LLMs? Evaluating Fairness in Retrieval-Augmented
Generation Systems. InProceedings of the 31st International Conference on Com-
putational Linguistics, COLING 2025, Abu Dhabi, UAE, January 19-24, 2025, Owen
Rambow, Leo Wanner, Marianna Apidianaki, Hend Al-Khalifa, Barbara Di Euge-
nio, and Steven Schockaert (Eds.). Association for Computational Linguistics,
10021–10036. https://aclanthology.org/2025.coling-main.669/
[59] Xiaoqian Wu, Yong-Lu Li, Jianhua Sun, and Cewu Lu. 2024. Symbol-LLM:
leverage language models for symbolic system in visual human activity reasoning.
Advances in Neural Information Processing Systems36 (2024).
[60] Fen Xia, Tie-Yan Liu, Jue Wang, Wensheng Zhang, and Hang Li. 2008. List-
wise approach to learning to rank: theory and algorithm. InMachine Learning,
Proceedings of the Twenty-Fifth International Conference (ICML 2008), Helsinki,
Finland, June 5-9, 2008 (ACM International Conference Proceeding Series, Vol. 307),
William W. Cohen, Andrew McCallum, and Sam T. Roweis (Eds.). ACM, 1192–
1199. doi:10.1145/1390156.1390306
[61] Ke Yang, Charles Yu, Yi R Fung, Manling Li, and Heng Ji. 2023. Adept: A debiasing
prompt framework. InProceedings of the AAAI Conference on Artificial Intelligence,
Vol. 37. 10780–10788.
[62] Yi Yang, Wen-tau Yih, and Christopher Meek. 2015. Wikiqa: A challenge dataset
for open-domain question answering. InProceedings of the 2015 conference on
empirical methods in natural language processing. 2013–2018.
[63] Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui
Chen, Christopher Dewan, Mona Diab, Xian Li, Xi Victoria Lin, et al. 2022. Opt:
Open pre-trained transformer language models.arXiv preprint arXiv:2205.01068
(2022).
[64] Yunfan Zhang, Xinyu Li, Shuohang Zhu, Lidong Bing, and Luo Si. 2023. Retrieval-
Augmented Generation for Large Language Models: A Survey.arXiv preprint
arXiv:2312.10997(2023).
[65] Zheng Zhang, Fan Yang, Ziyan Jiang, Zheng Chen, Zhengyang Zhao, Chengyuan
Ma, Liang Zhao, and Yang Liu. 2024. Position-Aware Parameter Efficient
Fine-Tuning Approach for Reducing Positional Bias in LLMs.arXiv preprint
arXiv:2404.01430(2024).
[66] Yuchen Zhuang, Yue Yu, Kuan Wang, Haotian Sun, and Chao Zhang. 2023. Toolqa:
A dataset for llm question answering with external tools.Advances in Neural
Information Processing Systems36 (2023), 50117–50143.
[67] Bruno Zirnstein. 2023.Extended context for InstructGPT with LlamaIndex. Tech-
nical Report. Technical Report. Hochschule für Wirtschaft und Recht Berlin.
