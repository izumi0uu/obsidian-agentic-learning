# Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging - Extracted Text

- Source note: [[Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging]]
- Source PDF: `assets/Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging.pdf`
- Extracted: 2026-05-15
- Extractor: pypdf
- Pages: 19
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

Scaling Retrieval-Augmented Reasoning with Parallel
Search and Explicit Merging
Jiabei Liu1*,Wenyu Mao 1*,Junfei Tan 1,Chunxu Shen 2†,Lingling Yi 2,
Jiancan Wu1†,Xiang Wang 1†,
1 University of Science and Technology of China
2 WeChat Technical Architecture Department, Tecent Inc.
∗ Equal contribution. † Corresponding author.
Abstract
Deep search agents have proven effective in enhancing LLMs by retrieving external
knowledge during multi-step reasoning. However, existing methods often generate
a single query for retrieval at each reasoning step, limiting information coverage
and introducing high noise. This may result in low signal-to-noise ratios (SNR)
during search, degrading reasoning accuracy and leading to unnecessary reason-
ing steps. In this paper, we introduce MultiSearch, an RL-based framework that
addresses these limitations through multi-query retrieval and explicit merging of
retrieved information. At each reasoning step, MultiSearch generates queries from
multiple perspectives and retrieves external information in parallel, expanding the
scope of relevant information and mitigating the reliance on any single retrieval
result. Then, the agent consolidates and refines retrieved information at the merging
process, improving the SNR and ensuring more accurate reasoning. Additionally,
we propose a reinforcement learning framework with a multi-process reward design
to optimize agents for both multi-query retrieval and information consolidation.
Extensive experiments on seven benchmarks demonstrate that MultiSearch outper-
forms baseline methods, enhancing the SNR of retrieval and improving reasoning
performance in question-answering tasks.
1 Introduction
Large language models (LLMs) have demonstrated strong capabilities in understanding and
reasoning[1]. However, they remain constrained on knowledge-intensive tasks by their reliance
on static internal knowledge[2, 3]. Retrieval-augmented generation (RAG) alleviates this limitation
by enabling LLMs to access external knowledge during generation [4, 5]. For complex questions, a
single retrieval step is often insufficient, since the information required for answering may depend on
intermediate reasoning states. This motivates deep search agents, which retrieve external knowledge
during multi-step reasoning and use the retrieved information to support subsequent reasoning [6–9].
Most existing deep search methods follow a ReAct-style retrieval-during-reasoning paradigm [10–15].
At each reasoning step, the agent generates a search query conditioned on its current reasoning state,
retrieves the top-k relevant documents from an external knowledge source, and incorporates the
retrieved information into the context for subsequent reasoning. This process repeats until the agent
has gathered sufficient information to produce a final answer. To optimize this multi-step process,
recent reinforcement learning (RL)-based methods model the search engine as part of the environment
and train the agent on sampled reasoning-and-search trajectories [ 13, 16]. The policy is typically
updated with outcome-level rewards, such as final-answer correctness, which encourages better query
generation, tool use, and final question-answering performance.
Preprint.
arXiv:2605.13534v1  [cs.AI]  13 May 2026

## Page 2

Question: where does the vice president and his family live?
I need to understand the living arrangements for those 
holding such high-ranking government positions. 
Query: where does the vice president live
… his family lived in Arlington, Virginia when 
Congress was in session and in Columbus, Indiana 
during recesses. Pence's son  …
I didn’t obtain sufficient information.
Answer: The White House.
Query: federal government housing for vice president
… for use by the President and Vice President of the 
US; other such residences include the White House, 
Camp David, One Observatory Circle …
The vice president might live in the White House, 
Camp David, or One Observatory Circle.
Query: the White House
…
(a)
(b)
<Think> <Search> <Info> <Merge> <Answer>
Answer RewardMulti-Query Reward
Merging Reward
Process 
Reward
Query 1: where does the vice president live
Query 2: federal government housing for vice president
Query 3:  …
Number One Observatory Circle is the official 
residence of the Vice President of the United States. …
Merge: From the retrieved documents, we can 
observe that the vice president lives at Number One 
Observatory Circle.
Answer: Number One Observatory Circle.
Question: where does the vice president and his family live?
I need to understand the living arrangements for those 
holding such high-ranking government positions. 
The President's Guest House, commonly known as 
Blair House, is a complex of four formerly separate 
buildings—Blair House, Lee House, …
Congress established Number One Observatory Circle 
as the official ""temporary"" residence of the Vice 
President of the United States. 
<Think> <Search> <Info> <Answer>
Answer Reward
Figure 1: Comparison of classic deep search methods and MultiSearch. (a) Previous serial single-
query retrieval can be affected by noisy information and may consume more reasoning steps. Multi-
Search employs multi-query retrieval with explicit merging to capture more comprehensive informa-
tion with less steps. (b) Based on prior methods, MultiSearch incorporates more targeted rewards to
enable fine-grained supervision.
Despite its effectiveness, this paradigm can limit the quality of the intermediate retrieval used for
reasoning. In particular, we identify two key limitations:
• Low Signal-to-Noise Ratio (SNR) of Retrieval.At each reasoning step, existing methods typically
rely on a single retrieval query, which captures only one formulation of the current information
need. For multi-hop or complex questions involving multiple entities, relations, or sub-questions,
this may retrieve only partial information. Moreover, if the generated query is under-specified,
ambiguous, or mismatched with the corpus, the retrieved top-kdocuments may include irrelevant
or noisy content. The resulting lack of useful information and presence of noise can lower the
signal-to-noise ratio (SNR) of the intermediate reasoning context, degrading reasoning accuracy or
leading to unnecessary search steps, as illustrated by the single-query failures in Figure 1(a).
• Underexplored fine-grained supervision.Recent RL-based deep search methods are often
optimized with outcome-level rewards, such as final-answer correctness, sometimes supplemented
by format or tool-use rewards [ 12, 13, 16]. However, these rewards provide limited feedback
on intermediate behaviors during retrieval-during-reasoning. In particular, when introducing
intermediate mechanisms to improve retrieval quality and reduce noise, outcome-level supervision
alone may be insufficient, as it provides limited guidance on whether the agent retrieves sufficient
useful information and consolidates it into a reliable context for reasoning. This motivates a
multi-process reward design that provides targeted supervision for both retrieval and information
consolidation, as illustrated in Figure 1(b).
To address these limitations, we proposeMultiSearch, an RL-based framework that improves
retrieval-during-reasoning through multi-query retrieval and explicit merging of retrieved information.
At each reasoning step, MultiSearch generates queries from multiple perspectives, including rephras-
ing, concept expansion, and question decomposition, and retrieves external information in parallel.
This expands the scope of relevant information and reduces reliance on any single retrieval result.
The agent then consolidates and refines the retrieved information through an explicit merging step,
improving the SNR of the intermediate retrieval for subsequent reasoning. To train the agent to use
2

## Page 3

Q
Search Engine ℰ
Policy Model 𝜋𝜃
𝑜1
𝑜2
𝑜𝐺
…
Rule-based 
Reward
Reference 
Model
𝑟𝑎1
𝑟𝑎2
𝑟𝑎𝐺
…
𝑟𝑞1
𝑟𝑞2
𝑟𝑞𝐺
𝑟𝑚1
𝑟𝑚2
𝑟𝑚𝐺
𝐴𝑎1
𝐴𝑎2
𝐴𝑎𝐺
…
𝐴𝑞1
𝐴𝑐2
𝐴𝑞𝐺
𝐴𝑚1
𝐴𝑚2
𝐴𝑚𝐺
Group Normalization
Aggregation
𝐴1
𝐴2
𝐴𝐺
…
Question
Rollout AdvantageKL
Do Razorlight and 
Joywave play the 
same genre of music?  
Question
<Think>
<Search>
<Information>
<Merge>
…
<Answer>
(a)
(b)
Q
Search Engine ℰ
Policy Model 𝜋𝜃
 … …
𝐴𝑞2
𝐴1
𝐴2
𝐴𝐺
…
Do Razorlight and 
Joywave play the 
same genre of music?  
Question
Policy 
Model
Search 
Engine
Think: I need information about each band. <answer> 
Yes. 
</answer> 
Merge: Razorlight & Joywave both play indie rock.
Search1: Razorlight genre?
Search2: Joywave genre? …
Info2: Joywave is an American indie rock…
Info1: Razorlight is an English indie rock…
Figure 2: The training framwork of MultiSearch. (a) An question-answering example, including think,
multi-query search, information, merge and answer steps. (b) Overview of the policy optimization
procedure, where the model is trained using GDPO.
these mechanisms effectively, we introduce a multi-process reward design for reinforcement learning.
In addition to the outcome reward for final-answer correctness, we use a multi-query reward to encour-
age retrieval with multiple queries and a merging reward to encourage information consolidation for
high SNR. These process-level rewards provide targeted supervision for the intermediate retrieval and
merging behaviors. We optimize the resulting multi-reward objective with Group reward-Decoupled
Normalization Policy Optimization (GDPO) [17], which separately normalizes heterogeneous reward
signals before aggregating them for policy optimization.
We train MultiSearch with Qwen2.5-3B/7B Base and Instruct backbones, and evaluate it on seven
QA benchmarks, including three single-hop datasets [18–20] and four multi-hop datasets [21–24].
MultiSearch achieves the best average performance among the compared baselines [ 11, 13, 15,
16] across these settings. Experimental results show that the agent progressively learns to issue
multiple retrieval queries and produce higher-SNR merged information, suggesting that the proposed
reward design encourages the intended intermediate behaviors. Ablation studies further verify the
contributions of multi-query retrieval, explicit merging, and corresponding rewards to the overall
performance.
2 Method
In this section, we provide a comprehensive description of the MultiSearch framework. We begin by
outlining the trajectory generation process, with a particular emphasis on our parallel multi-query
retrieval mechanism (§2.1). Next, we present our multi-granularity reward design, which includes an
answer reward, a multi-query reward, and a merging reward (§2.2). Finally, we detail the training
objective based on Group reward–Decoupled Normalization Policy Optimization(§2.3).
2.1 Generation with Multi-Query Retrieval
Rollout Generation.For each question q in the training datasets, the agent iteratively interacts
with the search engine E and generates a reasoning trajectory o . Specifically, it generates multiple
queries in <search>...</search> to trigger retrieval tools, and uses <information>...</information>
to encapsulate the retrieved documents. Then, the agent explicitly extracts and merges key information
from the retrieved content within <merge>...</merge>. The existing response concatenated with the
<information> and <merge> blocks serves as the next input prompt for the subsequent generation
step. This search→info→merge cycle continues until the agent determines that there is sufficient
information and presents an answer inside<answer>...</answer>(cf.Figure 2(a)).
3

## Page 4

Multi-Query Retrieval.To scale the retrieval from diverse perspectives, we equip the agent
with three query generation strategies: rephrasing, concept expansion, and question decomposition.
Rephrasing helps retrieve documents that use different lexical or syntactic expressions, mitigating the
risk of missing relevant information due to phrasing mismatches[25]. Concept expansion broadens
the search scope by adding related terms, synonyms, or hypernyms, which is particularly useful when
the initial query is too narrow[26]. Question decomposition splits a complex question into simpler
sub-questions, solves them in parallel, and then consolidates the retrieved information to produce the
final answer. At each retrieval step, the agent generates three queries for parallel retrieval, adopting
one or more of the above strategies or exploring alternative strategies autonomously.
Explicit Merging.After retrieval, repetitive or irrelevant documents are removed to eliminate
redundancy. The agent reads the remaining documents and explicitly places relevant information
within <merge> and </merge>. The training template is illustrated in Appendix B. For more analysis
on different integration manners, please refer to Appendix A.4.
2.2 Reward Modeling
The reward system of MultiSearch consists of three components: (1) Answer Reward, which evaluates
the accuracy of the final prediction. (2) Multi-Query Reward, which encourages generating multiple
queries for retrieval. (3) Merging Reward, which assesses the quality of the information consolidation.
Answer reward.We compute a word-level F1 score between the predicted answer enclosed
in <answer>...</answer> and the ground-truth answer to measure the correctness of the agent’s
prediction. The answer reward is defined as:
rans =F1(a pred, a) = 2nint
npred +n truth
(1)
where npred and ntruth are the word counts of the predicted answer and the ground-truth answer,
respectively. Andn int is the word count of their intersection.
Multi-Query Reward.We introduce a dedicated reward for the proposed multi-query retrieval
mechanism. Specifically, we extract all queries within the <search>...</search> blocks throughout
the rollout and calculate the average number of queries generated per step:
rquery =
0.1, n q >2
0,otherwise (2)
wheren q is the average number of queries per step.
Merging reward.The merging step is designed to remove irrelevant information from the retrieved
documents and to consolidate key evidence. To evaluate the quality of this integration, we aggregate
all text enclosed within <merge></merge> blocks, and verify whether the ground-truth answer appears
in any of them:
rmerge =
0.1,∃M i ∈ {M1,M2, ...Mn},Mi ∩a=a
0,otherwise (3)
where {M1,M2, ...Mn} denotes the n merging steps within a single rollout. The multi-query
reward and merging reward are applied only when the answer is correct. In particular, the final
rewards are defined as follows:
(Rans,Rquery,Rmerge) =
(rans, rquery, rmerge), r ans >0
(0,0,0),otherwise (4)
2.3 Reinforcement Learning
Group reward-Decoupled Normalization Policy Optimization (GDPO)[17] was proposed to address a
key limitation of Group Relative Policy Optimization (GRPO)[27] in multi-reward RL. Unlike GRPO,
which directly sums all reward components into a single rollout reward, GDPO normalizes each
reward independently within the group. The resulting advantages are then aggregated and subjected
4

## Page 5

to batch-wise normalization. This decoupled design preserves the distinct contributions of individual
rewards, enabling the model to receive more fine-grained and informative advantage signals.
We employ GDPO as the learning algorithm for RL training. Specifically, for each input question,
given a policy model πθ and a reference model πref, GDPO samples a group of rollouts {oi}G
i=1. The
agent is optimized by maximizing the following objective:
JGDPO(θ) =Ex∼D,{oi}G
i=1∼πθold (·|x;E)
"
1
G
GX
i=1
1
|oi|
|oi|X
t=1
min
 
πθ(oi,t |x, oi,<t;E)
πθold (oi,t |x, oi,<t;E)
ˆAi,t,
clip
 πθ(oi,t |x, oi,<t;E)
πθold (oi,t |x, oi,<t;E) ,1−ϵ,1 +ϵ

ˆAi,t
!
−βD KL [πθ ∥π ref]
# (5)
where G denotes the group size, E represents the search engine, ϵ is the clipping ratio and β is the
coefficient of KL divergence. ˆAi,t is the batch-wise normalized advantage for the i-th rollout in
current group, defined as:
ˆAi,j,t = Ai,j,t −mean{A i′,j′,t|i′ ∈D Batch, j′ = 1, ...G}
std{Ai′,j′,t|i′ ∈D Batch, j′ = 1, ...G} (6)
where
Ai,j,t =
X
k∈{ans,query,merge}
wkAk
i,j,t,withA k
i,j,t = rk
i,j,t −mean(r k
t )
std(rk
t ) (7)
represents the weighted sum of the normalized advantages of different reward components. Figure
2(b) illustrates an overview of our GDPO-based training framework.
3 Experiment
In this section, we conduct a series of experiments to address the following research questions:
(1) RQ1: How does MultiSearch perform on question-answering tasks? (2) RQ2: What are the
contributions of the multi-query retrieval and explicit merging mechanism? (3) RQ3: Can our
different query generation strategy effectively guide the search agent? (4) RQ4: How sensitive is
MultiSearch to the number of retrieval queries and the retrieval depth?
3.1 Settings
Datasets & Evaluation Metrics.We evaluate MultiSearch on three general Q&A datasets: NQ[ 18],
TriviaQA[20], PopQA[19], and four multi-hop reasoning Q&A datasets: HotpotQA[21], 2WikiMulti-
HopQA (2Wiki)[22], Musique[23], and Bamboogle[24]. For a fair comparison, we follow the settings
of baseline methods[13, 16], training the agent on a combined dataset of NQ and HotpotQA, and
adopting Extract Match (EM) as the evaluation metric. For ablation on different evaluation metrics
and training datasets, please refer to Appendix A.1 and A.2.
Baselines.To evaluate the effectiveness of our MultiSearch framework, we consider diverse base-
lines mainly grouped into three categories: (1) methods without retrieval: direct inference with
LLM, Chain of Thought (CoT) reasoning[ 28], Supervised Fine-Tuning (SFT), and R1-like fine-
tuning[29]. (2) methods with single-turn static retrieval: naive Retrieval-Augmented Generation
(RAG)[5]. (3) methods with multi-turn dynamic retrieval: Search-o1[ 11], Interleaving retrieval
with chain-of-thought reasoning (IRCoT)[30], previous outstanding agentic RL methods including
ReSearch[15], Search-R1[13] and AutoRefine[16], as well as relatively recent work Dr.Zero[ 31],
AdaSearch[32] and CriticSearch[33].
Implementation details.In line with previous work, we use Qwen2.5-3B-Base/Instruct and
Qwen2.5-7B-Base/Instruct as the backbone models. For retrieval, we utilize E5[ 34] as the search
engine and 2018 Wikipedia dump[35] as the external data source. Both the number of queries and
retrieved documents are set to 3. The reported results are averaged over three runs, and we omit the
variance as it is relatively small. Most of the baseline results are taken directly from the corresponding
original papers or paper of Search-R1 under comparable settings, while AutoRefine is reproduced
using open-source code. Additional details of the experimental settings can be found in Appendix C.
5

## Page 6

Table 1: (RQ1) Main results.Bolddenotes the best results, and underline indicates the second best.
Methods Single-Hop QA Multi-Hop QA
NQ TriviaQA PopQA HotpotQA 2Wiki Musique Bamboogle Avg.
Qwen2.5-3B-Base/Instruct
Direct Generation 0.106 0.288 0.108 0.149 0.244 0.020 0.024 0.134
CoT 0.023 0.032 0.005 0.021 0.021 0.002 0.000 0.015
IRCoT 0.111 0.312 0.200 0.164 0.171 0.067 0.240 0.181
SFT 0.249 0.292 0.104 0.186 0.248 0.044 0.112 0.176
R1-Instruct 0.210 0.449 0.171 0.208 0.275 0.060 0.192 0.224
R1-Base 0.226 0.455 0.173 0.201 0.268 0.055 0.224 0.229
RAG 0.348 0.544 0.387 0.255 0.226 0.047 0.080 0.270
Search-o1 0.238 0.472 0.262 0.221 0.218 0.054 0.320 0.255
AdaSearch 0.379 0.568 0.428 0.334 0.385 0.144 0.280 0.360
CriticSearch - - - 0.414 0.409 0.180 0.368 -
Dr.Zero 0.391 0.572 0.431 0.298 0.291 0.091 0.200 0.326
ReSearch-Instruct 0.365 0.571 0.395 0.351 0.272 0.095 0.266 0.331
ReSearch-Base 0.427 0.597 0.430 0.305 0.272 0.074 0.128 0.319
Search-R1-Instruct 0.397 0.565 0.391 0.331 0.310 0.124 0.232 0.336
Search-R1-Base 0.421 0.583 0.413 0.297 0.274 0.066 0.128 0.312
ZeroSearch-Instruct 0.402 0.580 0.460 0.228 0.214 0.104 0.181 0.310
ZeroSearch-Base 0.4340.638 0.4840.322 0.356 0.138 0.153 0.361
StepSearch-Instruct - - - 0.345 0.320 0.174 0.344 -
StepSearch-Base - - - 0.329 0.339 0.181 0.328 -
AutoRefine-Instruct 0.436 0.597 0.447 0.404 0.380 0.169 0.336 0.396
AutoRefine-Base 0.467 0.620 0.450 0.405 0.393 0.157 0.344 0.405
MultiSearch-Instruct0.470 0.615 0.444 0.420 0.412 0.183 0.371 0.416
MultiSearch-Base 0.471 0.630 0.455 0.431 0.413 0.163 0.390 0.422
Qwen2.5-7B-Base/Instruct
Direct Inference 0.134 0.408 0.140 0.183 0.250 0.031 0.120 0.181
CoT 0.048 0.185 0.054 0.092 0.111 0.022 0.232 0.106
IRCoT 0.224 0.478 0.301 0.133 0.149 0.072 0.224 0.239
SFT 0.318 0.354 0.121 0.217 0.259 0.066 0.112 0.207
R1-instruct 0.270 0.537 0.199 0.237 0.292 0.072 0.293 0.271
R1-base 0.297 0.539 0.202 0.242 0.273 0.083 0.296 0.276
RAG 0.349 0.585 0.392 0.299 0.235 0.058 0.208 0.304
Search-o1 0.151 0.443 0.131 0.187 0.176 0.058 0.296 0.206
ReasonRAG - - 0.415 0.3840.4360.128 0.360 -
CtriticSearch - - - 0.442 0.428 0.194 0.472 -
Dr.Zero 0.406 0.608 0.416 0.362 0.347 0.104 0.360 0.372
Search-R1-Instruct 0.429 0.623 0.427 0.386 0.346 0.162 0.400 0.396
Search-R1-Base 0.395 0.560 0.388 0.326 0.297 0.125 0.360 0.350
ZeroSearch-Instruct 0.414 0.574 0.448 0.274 0.300 0.098 0.111 0.317
ZeroSearch-Base 0.430 0.616 0.414 0.338 0.346 0.130 0.139 0.345
StepSearch-Instruct - - - 0.386 0.3660.2260.312 -
StepSearch-Base - - - 0.380 0.385 0.216 0.467 -
AutoRefine-Instruct 0.419 0.618 0.403 0.408 0.325 0.188 0.416 0.397
AutoRefine-Base 0.470 0.649 0.4630.445 0.369 0.204 0.435 0.434
MultiSearch-Instruct0.472 0.636 0.437 0.421 0.351 0.171 0.463 0.422
MultiSearch-Base 0.491 0.657 0.458 0.446 0.416 0.170 0.476 0.445
3.2 Main Results (RQ1)
Overall Performance.The performance of MultiSearch compared to baseline methods is presented
in Table 1. As shown, MultiSearch achieves the highest average accuracy across seven benchmarks
(columnAvg.) for both 3B and 7B model sizes. The gains are particularly notable on multi-hop
benchmarks, where multi-query retrieval expands the scope of relevant information to cover multiple
entities, relations, or sub-questions, and explicit merging consolidates the retrieved information
for subsequent reasoning. Additionally, base model variants outperform their instruction-tuned
counterparts. As discussed in Appendix A.5, one possible explanation is that instruction fine-tuning
may reduce the model’s adaptability to new multi-step reasoning tasks.
Retrieval Quality and Reasoning Steps.Figure 3(a) first examines the SNR of intermediate retrieved
information. MultiSearch produces higher-SNR <information> blocks than Search-R1, and the
explicit <merge> step further improves the SNR. This indicates that multi-query retrieval broadens
useful information coverage, while merging helps reduce noisy content and forms a more reliable
context for subsequent reasoning. This higher-SNR information helps reduce the need for follow-up
searches to compensate for incomplete or noisy retrieval, consistent with the fewer search steps
observed in Figure 3(b).
6

## Page 7

<
info> of Search-R1< info> of MultiSearch< merge> of MultiSearch0
.20
.40
.60
.81
.0SNR 
Avg. ±0.75 SD 5%~95% Avg.
(a)
/uni00000013/uni00000011/uni00000013/uni00000013
/uni00000013/uni00000011/uni00000015/uni00000018
/uni00000013/uni00000011/uni00000018/uni00000013
/uni00000013/uni00000011/uni0000001a/uni00000018
/uni00000014/uni00000011/uni00000013/uni00000013
/uni00000014/uni00000011/uni00000015/uni00000018
/uni00000014/uni00000011/uni00000018/uni00000013
/uni00000014/uni00000011/uni0000001a/uni00000018
/uni00000015/uni00000011/uni00000013/uni00000013
/uni00000015/uni00000011/uni00000015/uni00000018/uni00000036/uni00000048/uni00000044/uni00000055/uni00000046/uni0000004b/uni00000003/uni00000036/uni00000057/uni00000048/uni00000053/uni00000056
/uni00000031/uni00000034/uni00000037/uni00000055/uni0000004c/uni00000059/uni0000004c/uni00000044/uni00000034/uni00000024/uni00000033/uni00000052/uni00000053/uni00000034/uni00000024/uni0000002b/uni00000052/uni00000057/uni00000053/uni00000052/uni00000057/uni00000034/uni00000024/uni00000015/uni0000003a/uni0000004c/uni0000004e/uni0000004c/uni00000030/uni00000058/uni00000056/uni0000004c/uni00000054/uni00000058/uni00000048/uni00000025/uni00000044/uni00000050/uni00000045/uni00000052/uni00000052/uni0000004a/uni0000004f/uni00000048
/uni00000010/uni00000013/uni00000011/uni00000014/uni00000014
/uni0000000b/uni00000014/uni00000013/uni00000008/uni0000000c
/uni00000010/uni00000013/uni00000011/uni00000014/uni00000018
/uni0000000b/uni00000014/uni00000016/uni00000008/uni0000000c
/uni00000010/uni00000013/uni00000011/uni00000015/uni00000017
/uni0000000b/uni00000014/uni0000001c/uni00000008/uni0000000c
/uni00000010/uni00000013/uni00000011/uni00000015/uni00000014
/uni0000000b/uni00000014/uni00000016/uni00000008/uni0000000c
/uni00000010/uni00000013/uni00000011/uni00000017/uni00000018
/uni0000000b/uni00000015/uni00000016/uni00000008/uni0000000c
/uni00000010/uni00000013/uni00000011/uni00000016/uni00000015
/uni0000000b/uni00000014/uni00000019/uni00000008/uni0000000c
/uni00000010/uni00000013/uni00000011/uni00000016/uni00000014
/uni0000000b/uni00000014/uni00000018/uni00000008/uni0000000c/uni00000030/uni00000058/uni0000004f/uni00000057/uni0000004c/uni00000056/uni00000048/uni00000044/uni00000055/uni00000046/uni0000004b
/uni00000036/uni00000048/uni00000044/uni00000055/uni00000046/uni0000004b/uni00000010/uni00000035/uni00000014 (b)
Figure 3: Comparison of the retrieval quality and efficiency
between Search-R1 and MultiSearch. (a) Signal to noise
ratio of <information> and <merge> blocks. (b) Average
number of search steps across different datasets.
/uni00000031/uni00000034/uni00000037/uni00000055/uni0000004c/uni00000059/uni0000004c/uni00000044/uni00000034/uni00000024/uni00000033/uni00000052/uni00000053/uni00000034/uni00000024/uni0000002b/uni00000052/uni00000057/uni00000053/uni00000052/uni00000057/uni00000034/uni00000024/uni00000015/uni0000005a/uni0000004c/uni0000004e/uni0000004c/uni00000030/uni00000058/uni00000056/uni0000004c/uni00000054/uni00000058/uni00000048/uni00000025/uni00000044/uni00000050/uni00000045/uni00000052/uni00000052/uni0000004a/uni0000004f/uni00000048
/uni00000013
/uni00000015/uni00000013
/uni00000017/uni00000013
/uni00000019/uni00000013
/uni0000001b/uni00000013
/uni00000014/uni00000013/uni00000013/uni00000033/uni00000048/uni00000055/uni00000046/uni00000048/uni00000051/uni00000057/uni00000044/uni0000004a/uni00000048/uni00000003/uni0000000b/uni00000008/uni0000000c
/uni00000014/uni00000014/uni00000011/uni0000001a/uni00000008
/uni00000014/uni0000001b/uni00000011/uni00000013/uni00000008
/uni00000019/uni00000011/uni0000001b/uni00000008
/uni00000015/uni00000019/uni00000011/uni0000001a/uni00000008
/uni00000015/uni00000013/uni00000011/uni00000015/uni00000008
/uni00000016/uni00000014/uni00000011/uni00000019/uni00000008
/uni00000019/uni00000018/uni00000011/uni00000013/uni00000008
/uni00000017/uni00000018/uni00000011/uni00000013/uni00000008
/uni00000018/uni0000001b/uni00000011/uni00000013/uni00000008
/uni00000016/uni0000001a/uni00000011/uni00000013/uni00000008/uni00000017/uni00000018/uni00000011/uni0000001a/uni00000008
/uni00000015/uni0000001c/uni00000011/uni0000001b/uni00000008
/uni00000018/uni00000013/uni00000011/uni00000013/uni00000008
/uni00000015/uni00000014/uni00000011/uni0000001a/uni00000008
/uni00000016/uni00000019/uni00000011/uni0000001c/uni00000008/uni00000016/uni00000017/uni00000011/uni00000018/uni00000008/uni00000016/uni00000017/uni00000011/uni00000018/uni00000008/uni00000016/uni00000015/uni00000011/uni0000001c/uni00000008/uni00000016/uni00000019/uni00000011/uni0000001b/uni00000008
/uni00000018/uni00000013/uni00000011/uni00000013/uni00000008
/uni00000014/uni00000011/uni0000001a/uni00000008/uni00000013/uni00000011/uni0000001b/uni00000008/uni00000014/uni00000011/uni0000001b/uni00000008/uni00000014/uni00000011/uni00000015/uni00000008/uni00000014/uni00000011/uni0000001b/uni00000008/uni00000036/uni00000057/uni00000055/uni00000044/uni00000057/uni00000048/uni0000004a/uni0000005c
/uni00000034
/uni00000026
/uni00000035
/uni00000032
Figure 4: Distribution of vari-
ous query generation strategies:
question decomposition (Q), con-
cept expansion (C), rephrasing
(R), and others (O).
Table 2: (RQ2) Ablation on multi-query retrieval, merging operation, and corresponding rewards.
Variants Single-Hop QA Multi-Hop QA
NQ TriviaQA PopQA HotpotQA 2Wiki Musique Bamboogle Avg.
MultiSearch 0.470 0.615 0.444 0.420 0.412 0.183 0.371 0.416
w/oRmerge 0.449 0.6150.434 0.395 0.405 0.1520.3790.404
w/oRmerge&Rquery 0.442 0.606 0.420 0.396 0.394 0.152 0.368 0.397
w/oRmerge&Rquery&<merge>0.443 0.597 0.425 0.393 0.328 0.163 0.350 0.386
w/o all 0.427 0.576 0.424 0.378 0.344 0.157 0.315 0.374
3.3 Ablation on Key Components (RQ2)
To assess the contributions of key components in MultiSearch, we perform ablation studies on
Qwen2.5-3B-Instruct, with results reported in Table 2. Specifically, we define five variants: (1) the
full MultiSearch, (2) MultiSearch without merging reward (w/oRmerge), (3) MultiSearch without both
merging reward and multi-query reward (w/o Rmerge & Rquery), (4) MultiSearch further excluding
explicit merging (w/o Rmerge & Rquery & <merge>), and (5) MultiSearch reduced to single-query
retrieval with only answer reward (w/o all). The results demonstrate that both the multi-query retrieval
& merging step, as well as our reward modeling, contribute positively to the overall performance.
As shown in Figure 7, the merging reward Rmerge and multi-query reward Rquery gradually converge
with the answer reward Rans during training. This observation suggests that the model progressively
learns to generate multiple queries and consolidate key evidence from the retrieved documents to
enhance its question-answering performance.
3.4 Ablation on query generation strategies (RQ3)
To address RQ3, we compare the performance under different query generation strategies. In
Table 3, “w/ Rephrase”, “w/ Concept”, and “w/ Decompose” represent scenarios where the agent
generate multiple queries merely under a single strategy: rephrasing, concept expansion, or question
decomposition, respectively. “Simple” refers to a setting where only multi-query generation is
required, without any strategies as guidance. As illustrated in Table 3, the agent guided by various
strategies outperforms the one guided by a single strategy. This suggests that the multi-perspective
strategies provide complementary benefits: rephrasing helps reduce lexical mismatch, concept
expansion broadens the search scope, and question decomposition helps handle complex information
needs. Figure 4 further shows that the trained agent uses a mixture of strategies across datasets,
supporting the need for multi-perspective query generation in retrieval-during-reasoning.
3.5 Sensitivity Analysis (RQ4)
Different hyperparameters may affect the performance of deep search agents. We investigate the
sensitivity of MultiSearch to the number of queries nq and the retrieval depth k. The results are
presented in Figure 5 and 6, where “single-hop”, “multi-hop”, “avg” denote the average accuracy on
single-hop benchmarks, multi-hop benchmarks, and all seven benchmarks, respectively. As shown in
7

## Page 8

Table 3: (RQ3) Ablation study on different query generation strategies.
Variants Single-Hop QA Multi-Hop QA
NQ TriviaQA PopQA HotpotQA 2Wiki Musique Bamboogle Avg.
MultiSearch 0.470 0.615 0.444 0.420 0.412 0.183 0.371 0.416
w/ rephrase 0.437 0.606 0.423 0.395 0.390 0.165 0.363 0.397
w/ concept 0.436 0.609 0.415 0.398 0.355 0.168 0.3790.394
w/ decompose 0.442 0.612 0.412 0.383 0.396 0.142 0.320 0.387
simple 0.418 0.604 0.421 0.373 0.375 0.136 0.320 0.378
/uni00000014 /uni00000015 /uni00000016 /uni00000017 /uni00000018
nq
/uni00000013/uni00000011/uni00000016/uni00000018
/uni00000013/uni00000011/uni00000017/uni00000013
/uni00000013/uni00000011/uni00000017/uni00000018
/uni00000013/uni00000011/uni00000018/uni00000013
/uni00000013/uni00000011/uni00000018/uni00000018/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c
/uni00000056/uni0000004c/uni00000051/uni0000004a/uni0000004f/uni00000048/uni00000010/uni0000004b/uni00000052/uni00000053
/uni00000014 /uni00000015 /uni00000016 /uni00000017 /uni00000018
nq
/uni00000013/uni00000011/uni00000015/uni0000001b
/uni00000013/uni00000011/uni00000016/uni00000013
/uni00000013/uni00000011/uni00000016/uni00000015
/uni00000013/uni00000011/uni00000016/uni00000017
/uni00000013/uni00000011/uni00000016/uni00000019
/uni00000013/uni00000011/uni00000016/uni0000001b/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c
/uni00000050/uni00000058/uni0000004f/uni00000057/uni0000004c/uni00000010/uni0000004b/uni00000052/uni00000053
/uni00000014 /uni00000015 /uni00000016 /uni00000017 /uni00000018
nq
/uni00000013/uni00000011/uni00000016/uni00000013/uni00000013
/uni00000013/uni00000011/uni00000016/uni00000015/uni00000018
/uni00000013/uni00000011/uni00000016/uni00000018/uni00000013
/uni00000013/uni00000011/uni00000016/uni0000001a/uni00000018
/uni00000013/uni00000011/uni00000017/uni00000013/uni00000013
/uni00000013/uni00000011/uni00000017/uni00000015/uni00000018
/uni00000013/uni00000011/uni00000017/uni00000018/uni00000013/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c
/uni00000044/uni00000059/uni0000004a
/uni00000016/uni00000025/uni00000010/uni0000002c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057/uni00000016/uni00000025/uni00000010/uni00000025/uni00000044/uni00000056/uni00000048/uni0000001a/uni00000025/uni00000010/uni0000002c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057/uni0000001a/uni00000025/uni00000010/uni00000025/uni00000044/uni00000056/uni00000048
Figure 5: (RQ4) Performance of MultiSearch on different nq, demonstrating the sensitivity of
MultiSearch to the number of retrieval queries.
/uni00000014/uni00000015/uni00000016/uni00000017/uni00000018/uni00000019
/uni00000037/uni00000052/uni00000053/uni00000003/uni0000002e
/uni00000013/uni00000011/uni00000017/uni00000017
/uni00000013/uni00000011/uni00000017/uni00000019
/uni00000013/uni00000011/uni00000017/uni0000001b
/uni00000013/uni00000011/uni00000018/uni00000013
/uni00000013/uni00000011/uni00000018/uni00000015
/uni00000013/uni00000011/uni00000018/uni00000017
/uni00000013/uni00000011/uni00000018/uni00000019/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c
/uni00000056/uni0000004c/uni00000051/uni0000004a/uni0000004f/uni00000048/uni00000010/uni0000004b/uni00000052/uni00000053
/uni00000014/uni00000015/uni00000016/uni00000017/uni00000018/uni00000019
/uni00000037/uni00000052/uni00000053/uni00000003/uni0000002e
/uni00000013/uni00000011/uni00000014/uni00000018
/uni00000013/uni00000011/uni00000015/uni00000013
/uni00000013/uni00000011/uni00000015/uni00000018
/uni00000013/uni00000011/uni00000016/uni00000013
/uni00000013/uni00000011/uni00000016/uni00000018/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c
/uni00000050/uni00000058/uni0000004f/uni00000057/uni0000004c/uni00000010/uni0000004b/uni00000052/uni00000053
/uni00000014/uni00000015/uni00000016/uni00000017/uni00000018/uni00000019
/uni00000037/uni00000052/uni00000053/uni00000003/uni0000002e
/uni00000013/uni00000011/uni00000016/uni00000013
/uni00000013/uni00000011/uni00000016/uni00000018
/uni00000013/uni00000011/uni00000017/uni00000013
/uni00000013/uni00000011/uni00000017/uni00000018/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c
/uni00000044/uni00000059/uni0000004a
/uni00000016/uni00000025/uni00000010/uni0000002c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057/uni00000016/uni00000025/uni00000010/uni00000025/uni00000044/uni00000056/uni00000048/uni0000001a/uni00000025/uni00000010/uni0000002c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057/uni0000001a/uni00000025/uni00000010/uni00000025/uni00000044/uni00000056/uni00000048
Figure 6: (RQ4) Performance of MultiSearch on different Top k, demonstrating the sensitivity of
MultiSearch to the retrieval depth.
Figure 5, performance peaks when nq = 3. Using too few queries fails to cover sufficient information,
whereas too many queries may lead to supersaturation, introducing repetitive or irrelevant information.
As illustrated in Figure 6, performance improves as k increases when k≤3 , but begins to decline
whenk≥4, as the search engine starts returning less relevant documents.
3.6 Different RL Methods
We further evaluate MultiSearch using GRPO and GDPO as RL algorithms. The evaluation results
are presented in Table 4, and the training dynamics is shown in Figure 7. As illustrated in the Figure,
both methods successfully optimize the three different objectives, guiding the agent to follow the
multi-query retrieval mechanism and merge key evidence during training. However, compared with
GDPO, GRPO exhibits less balanced reward optimization. The multi-query reward rises quickly
in the early stage (cf.Figure 7(b)), while the answer and merging rewards improve more slowly
(cf.Figure 7(a)(c)). Since the multi-query reward is easier to satisfy than rewards related to answer
correctness or information consolidation, it may dominate the aggregated reward signal under GRPO.
GDPO mitigates this issue by normalizing reward components separately, resulting in more robust
optimization and better performance, as shown in Table 4.
4 Related Work
Deep Search Agents.LLMs have demonstrated strong reasoning capabilities [ 28, 29, 36–38], but
still suffer from hallucinations and limited knowledge [2]. Retrieval-augmented generation (RAG)
alleviates these issues by incorporating external knowledge [4, 5]. However, native single-turn RAG
models struggle with complex questions, as they lack mechanisms to assess evidence sufficiency or
perform iterative retrieval. Prompt-based multi-turn methods partially address this limitation, yet
remain suboptimal in optimizing tool-call decisions [10, 30]. Supervised fine-tuning (SFT) effectively
improves tool usage, but typically require large-scale labeled data, which is costly to construct
8

## Page 9

/uni00000013/uni00000015/uni00000013/uni00000017/uni00000013/uni00000019/uni00000013/uni0000001b/uni00000013/uni00000014/uni00000013/uni00000013
/uni00000036/uni00000057/uni00000048/uni00000053
/uni00000013/uni00000011/uni00000015/uni00000013
/uni00000013/uni00000011/uni00000015/uni00000018
/uni00000013/uni00000011/uni00000016/uni00000013
/uni00000013/uni00000011/uni00000016/uni00000018
/uni00000013/uni00000011/uni00000017/uni00000013
/uni00000013/uni00000011/uni00000017/uni00000018
/uni00000013/uni00000011/uni00000018/uni00000013/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048
/uni00000024/uni00000051/uni00000056/uni0000005a/uni00000048/uni00000055/uni00000003/uni00000035/uni00000048/uni0000005a/uni00000044/uni00000055/uni00000047
/uni0000002a/uni00000027/uni00000033/uni00000032
/uni0000002a/uni00000035/uni00000033/uni00000032
/uni00000013/uni00000015/uni00000013/uni00000017/uni00000013/uni00000019/uni00000013/uni0000001b/uni00000013/uni00000014/uni00000013/uni00000013
/uni00000036/uni00000057/uni00000048/uni00000053
/uni00000013/uni00000011/uni00000014/uni00000013
/uni00000013/uni00000011/uni00000014/uni00000018
/uni00000013/uni00000011/uni00000015/uni00000013
/uni00000013/uni00000011/uni00000015/uni00000018
/uni00000013/uni00000011/uni00000016/uni00000013
/uni00000013/uni00000011/uni00000016/uni00000018
/uni00000013/uni00000011/uni00000017/uni00000013
/uni00000013/uni00000011/uni00000017/uni00000018/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048
/uni00000030/uni00000058/uni0000004f/uni00000057/uni0000004c/uni00000010/uni00000034/uni00000058/uni00000048/uni00000055/uni0000005c/uni00000003/uni00000035/uni00000048/uni0000005a/uni00000044/uni00000055/uni00000047
/uni0000002a/uni00000027/uni00000033/uni00000032
/uni0000002a/uni00000035/uni00000033/uni00000032
/uni00000013/uni00000015/uni00000013/uni00000017/uni00000013/uni00000019/uni00000013/uni0000001b/uni00000013/uni00000014/uni00000013/uni00000013
/uni00000036/uni00000057/uni00000048/uni00000053
/uni00000013/uni00000011/uni00000014/uni00000018
/uni00000013/uni00000011/uni00000015/uni00000013
/uni00000013/uni00000011/uni00000015/uni00000018
/uni00000013/uni00000011/uni00000016/uni00000013
/uni00000013/uni00000011/uni00000016/uni00000018
/uni00000013/uni00000011/uni00000017/uni00000013
/uni00000013/uni00000011/uni00000017/uni00000018/uni00000036/uni00000058/uni00000046/uni00000046/uni00000048/uni00000056/uni00000056/uni00000003/uni00000035/uni00000044/uni00000057/uni00000048
/uni00000030/uni00000048/uni00000055/uni0000004a/uni0000004c/uni00000051/uni0000004a/uni00000003/uni00000035/uni00000048/uni0000005a/uni00000044/uni00000055/uni00000047
/uni0000002a/uni00000027/uni00000033/uni00000032
/uni0000002a/uni00000035/uni00000033/uni00000032
Figure 7: Analysis of training rewards under GRPO and GDPO.
Table 4: Comparison between GRPO and GDPO on different backbone models.
Methods Single-Hop QA Multi-Hop QA
NQ TriviaQA PopQA HotpotQA 2Wiki Musique Bamboogle Avg.
Qwen2.5-3B-Base/Instruct
MultiSearch-Base (GDPO) 0.471 0.630 0.455 0.431 0.413 0.163 0.390 0.422
MultiSearch-Instruct (GDPO) 0.470 0.615 0.444 0.420 0.412 0.183 0.371 0.416
MultiSearch-Base (GRPO) 0.450 0.606 0.435 0.399 0.393 0.165 0.372 0.403
MultiSearch-Instruct (GRPO) 0.426 0.605 0.424 0.380 0.366 0.140 0.344 0.384
Qwen2.5-7B-Base/Instruct
MultiSearch-Base (GDPO) 0.491 0.657 0.458 0.446 0.416 0.170 0.476 0.445
MultiSearch-Instruct (GDPO) 0.472 0.636 0.437 0.421 0.351 0.171 0.463 0.422
MultiSearch-Base (GRPO) 0.458 0.617 0.432 0.389 0.343 0.163 0.419 0.403
MultiSearch-Instruct (GRPO) 0.418 0.637 0.424 0.403 0.350 0.158 0.415 0.400
and maintain [39, 40]. Recent work has explored reinforcement learning for deep search agents.
Search-R1 models the search engine as part of the environment and uses outcome-level rewards to
guide search behavior [13]. R1-Searcher introduces a two-stage training framework that separately
improves search-call formatting and answer accuracy [12]. Subsequent methods, such as AutoRefine
and EviNote-RAG, further enhance retrieval-augmented reasoning with post-retrieval processing or
task-specific rewards [16, 41]. Other methods investigate principle-based reward models to provide
supervision for intermediate steps [42, 43]. However, most previous methods rely on single-query
retrieval, limiting the utility of each retrieval step [14, 31, 44]. In contrast, our MultiSearch leverages
parallel multi-query retrieval and explicit merging to improve the quality of the search process.
Reinforcement Learning.Reinforcement Learning from Human Feedback (RLHF) represents an
early approach that transitions models from purely imitative behavior to strategic exploration [45, 46].
Proximal Policy Optimization (PPO) [47] is widely used due to its stable learning dynamics, but
it can incur high computational costs. To mitigate this, several simplified variants such as Direct
Preference Optimization (DPO) [48] and Group Relative Policy Optimization (GRPO) [ 27] have
been proposed. While early RL methods primarily target preference alignment, recent works explore
RL in retrieval-augmented reasoning settings. Both PPO and GRPO have demonstrated effectiveness
in these scenarios. Considering both computational efficiency and performance, we adopt Group
reward-Decoupled Normalization Policy Optimization (GDPO) [17], an improved variant of GRPO
specifically designed to handle multi-reward objectives.
5 Conclusion
In this work, we introduceMultiSearch, an RL-based framework for improving retrieval-during-
reasoning in deep search agents. Instead of relying on a single query at each reasoning step, Multi-
Search generates queries from multiple perspectives and retrieves external information in parallel,
expanding the scope of relevant information and reducing reliance on any single retrieval result. The
retrieved information is then explicitly merged, allowing the agent to consolidate useful information
and reduce noise before subsequent reasoning. To optimize these intermediate behaviors, we further
propose a multi-process reward design that supervises both multi-query retrieval and information con-
solidation. Experiments on seven question-answering benchmarks show that MultiSearch improves
the SNR of retrieved information and achieves better reasoning performance than strong baseline
methods. These results suggest that improving both retrieval coverage and information consolidation
is important for building more effective deep search agents.
9

## Page 10

References
[1] Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, Linyi Yang, Kaijie Zhu, Hao Chen,
Xiaoyuan Yi, Cunxiang Wang, Yidong Wang, et al. A survey on evaluation of large language
models.ACM transactions on intelligent systems and technology, 15(3):1–45, 2024.
[2] Yue Zhang, Yafu Li, Leyang Cui, Deng Cai, Lemao Liu, Tingchen Fu, Xinting Huang, Enbo
Zhao, Yu Zhang, Yulong Chen, et al. Siren’s song in the ai ocean: A survey on hallucination in
large language models.Computational Linguistics, 51(4):1373–1418, 2025.
[3] Cheng Peng, Xi Yang, Aokun Chen, Kaleb E Smith, Nima PourNejatian, Anthony B Costa,
Cheryl Martin, Mona G Flores, Ying Zhang, Tanja Magoc, et al. A study of generative large
language model for medical research and healthcare.NPJ digital medicine, 6(1):210, 2023.
[4] Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei
Sun, Qianyu Guo, Meng Wang, and Haofen Wang. Retrieval-augmented generation for large
language models: A survey.CoRR, abs/2312.10997, 2023.
[5] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman
Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al. Retrieval-augmented
generation for knowledge-intensive nlp tasks.Advances in neural information processing
systems, 33:9459–9474, 2020.
[6] Yuxuan Huang, Yihang Chen, Haozheng Zhang, Kang Li, Huichi Zhou, Meng Fang, Linyi
Yang, Xiaoguang Li, Lifeng Shang, Songcen Xu, et al. Deep research agents: A systematic
examination and roadmap.arXiv preprint arXiv:2506.18096, 2025.
[7] Yunjia Xi, Jianghao Lin, Yongzhao Xiao, Zheli Zhou, Rong Shan, Te Gao, Jiachen Zhu, Weiwen
Liu, Yong Yu, and Weinan Zhang. A survey of llm-based deep search agents: Paradigm,
optimization, evaluation, and challenges.arXiv preprint arXiv:2508.05668, 2025.
[8] Xiaoxi Li, Jiajie Jin, Guanting Dong, Hongjin Qian, Yongkang Wu, Ji-Rong Wen, Yutao Zhu,
and Zhicheng Dou. Webthinker: Empowering large reasoning models with deep research
capability. InThe Thirty-ninth Annual Conference on Neural Information Processing Systems,
2025.
[9] Tongyi DeepResearch Team, Baixuan Li, Bo Zhang, Dingchu Zhang, Fei Huang, Guangyu Li,
Guoxin Chen, Huifeng Yin, Jialong Wu, Jingren Zhou, et al. Tongyi deepresearch technical
report.arXiv preprint arXiv:2510.24701, 2025.
[10] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R Narasimhan, and Yuan
Cao. React: Synergizing reasoning and acting in language models. InThe eleventh international
conference on learning representations, 2022.
[11] Xiaoxi Li, Guanting Dong, Jiajie Jin, Yuyao Zhang, Yujia Zhou, Yutao Zhu, Peitian Zhang, and
Zhicheng Dou. Search-o1: Agentic search-enhanced large reasoning models. InProceedings of
the 2025 Conference on Empirical Methods in Natural Language Processing, pages 5420–5438,
2025.
[12] Huatong Song, Jinhao Jiang, Yingqian Min, Jie Chen, Zhipeng Chen, Wayne Xin Zhao, Lei Fang,
and Ji-Rong Wen. R1-searcher: Incentivizing the search capability in llms via reinforcement
learning.arXiv preprint arXiv:2503.05592, 2025.
[13] Bowen Jin, Hansi Zeng, Zhenrui Yue, Jinsung Yoon, Sercan O Arik, Dong Wang, Hamed
Zamani, and Jiawei Han. Search-r1: Training LLMs to reason and leverage search engines with
reinforcement learning. InSecond Conference on Language Modeling, 2025.
[14] Hao Sun, Zile Qiao, Jiayan Guo, Xuanbo Fan, Yingyan Hou, Yong Jiang, Pengjun Xie, Yan
Zhang, Fei Huang, and Jingren Zhou. Zerosearch: Incentivize the search capability of llms
without searching.arXiv preprint arXiv:2505.04588, 2025.
[15] Mingyang Chen, Linzhuang Sun, Tianpeng Li, sunhaoze, ZhouYijie, Chenzheng Zhu, Haofen
Wang, Jeff Z. Pan, Wen Zhang, Huajun Chen, Fan Yang, Zenan Zhou, and Weipeng Chen.
Research: Learning to reason with search for LLMs via reinforcement learning. InThe Thirty-
ninth Annual Conference on Neural Information Processing Systems, 2025.
10

## Page 11

[16] Yaorui Shi, Sihang Li, Chang Wu, Zhiyuan Liu, Junfeng Fang, Hengxing Cai, An Zhang, and
Xiang Wang. Search and refine during think: Facilitating knowledge refinement for improved
retrieval-augmented reasoning. InThe Thirty-ninth Annual Conference on Neural Information
Processing Systems.
[17] Shih-Yang Liu, Xin Dong, Ximing Lu, Shizhe Diao, Peter Belcak, Mingjie Liu, Min-Hung
Chen, Hongxu Yin, Yu-Chiang Frank Wang, Kwang-Ting Cheng, et al. Gdpo: Group reward-
decoupled normalization policy optimization for multi-reward rl optimization.arXiv preprint
arXiv:2601.05242, 2026.
[18] Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris
Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, et al. Natural questions: a
benchmark for question answering research.Transactions of the Association for Computational
Linguistics, 7:453–466, 2019.
[19] Alex Mallen, Akari Asai, Victor Zhong, Rajarshi Das, Daniel Khashabi, and Hannaneh Ha-
jishirzi. When not to trust language models: Investigating effectiveness of parametric and
non-parametric memories. InProceedings of the 61st Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers), pages 9802–9822, 2023.
[20] Mandar Joshi, Eunsol Choi, Daniel S Weld, and Luke Zettlemoyer. Triviaqa: A large scale
distantly supervised challenge dataset for reading comprehension. InProceedings of the 55th
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pages 1601–1611, 2017.
[21] Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William Cohen, Ruslan Salakhutdinov,
and Christopher D Manning. Hotpotqa: A dataset for diverse, explainable multi-hop question
answering. InProceedings of the 2018 Conference on Empirical Methods in Natural Language
Processing, pages 2369–2380, 2018.
[22] Xanh Ho, Anh-Khoa Duong Nguyen, Saku Sugawara, and Akiko Aizawa. Constructing a
multi-hop qa dataset for comprehensive evaluation of reasoning steps. InProceedings of the
28th International Conference on Computational Linguistics, pages 6609–6625, 2020.
[23] Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, and Ashish Sabharwal. Musique:
Multihop questions via single-hop question composition.Transactions of the Association for
Computational Linguistics, 10:539–554, 2022.
[24] Ofir Press, Muru Zhang, Sewon Min, Ludwig Schmidt, Noah A Smith, and Mike Lewis.
Measuring and narrowing the compositionality gap in language models. InFindings of the
Association for Computational Linguistics: EMNLP 2023, pages 5687–5711, 2023.
[25] Xinbei Ma, Yeyun Gong, Pengcheng He, Hai Zhao, and Nan Duan. Query rewriting in retrieval-
augmented large language models. In Houda Bouamor, Juan Pino, and Kalika Bali, editors,
Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing,
pages 5303–5315, December 2023.
[26] Ellen M V oorhees. Query expansion using lexical-semantic relations. InSIGIR’94: Proceedings
of the Seventeenth Annual International ACM-SIGIR Conference on Research and Development
in Information Retrieval, organised by Dublin City University, pages 61–69. Springer.
[27] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Jun-Mei Song, Mingchuan Zhang, Y . K. Li,
Yu Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open
language models.ArXiv, abs/2402.03300, 2024.
[28] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi,
Quoc V . Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language
models. InProceedings of the 36th International Conference on Neural Information Processing
Systems. Curran Associates Inc., 2022.
[29] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu,
Ruoyu Zhang, Shirong Ma, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in
llms via reinforcement learning.arXiv preprint arXiv:2501.12948, 2025.
11

## Page 12

[30] Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot, and Ashish Sabharwal. Interleaving
retrieval with chain-of-thought reasoning for knowledge-intensive multi-step questions. In
Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 10014–10037, Toronto, Canada, July 2023. Association for
Computational Linguistics. doi: 10.18653/v1/2023.acl-long.557.
[31] Zhenrui Yue, Kartikeya Upasani, Xianjun Yang, Suyu Ge, Shaoliang Nie, Yuning Mao, Zhe
Liu, and Dong Wang. Dr. zero: Self-evolving search agents without training data.CoRR,
abs/2601.07055, 2026. doi: 10.48550/ARXIV .2601.07055.
[32] Tzu-Han Lin, Wei-Lin Chen, Chen-An Li, Hung-yi Lee, Yun-Nung Chen, and Yu Meng.
Adasearch: Balancing parametric knowledge and search in large language models via reinforce-
ment learning.CoRR, abs/2512.16883, 2025. doi: 10.48550/ARXIV .2512.16883.
[33] Yaocheng Zhang, Haohuan Huang, Zijun Song, Yuanheng Zhu, Qichao Zhang, Zijie Zhao, and
Dongbin Zhao. Criticsearch: Fine-grained credit assignment for search agents via a retrospective
critic.arXiv preprint arXiv:2511.12159, 2025.
[34] Liang Wang, Nan Yang, Xiaolong Huang, Binxing Jiao, Linjun Yang, Daxin Jiang, Rangan
Majumder, and Furu Wei. Text embeddings by weakly-supervised contrastive pre-training.
ArXiv, abs/2212.03533, 2022.
[35] Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov,
Danqi Chen, and Wen-tau Yih. Dense passage retrieval for open-domain question answering.
In Bonnie Webber, Trevor Cohn, Yulan He, and Yang Liu, editors,Proceedings of the 2020
Conference on Empirical Methods in Natural Language Processing, EMNLP 2020, Online,
November 16-20, 2020, pages 6769–6781. Association for Computational Linguistics, 2020.
doi: 10.18653/V1/2020.EMNLP-MAIN.550.
[36] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni
Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4
technical report.arXiv preprint arXiv:2303.08774, 2023.
[37] An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng
Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, et al. Qwen2. 5-math technical report: Toward
mathematical expert model via self-improvement.arXiv preprint arXiv:2409.12122, 2024.
[38] Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jia-
jun Zhang, Bowen Yu, Keming Lu, et al. Qwen2. 5-coder technical report.arXiv preprint
arXiv:2409.12186, 2024.
[39] Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Eric Hambro,
Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. Toolformer: Language models
can teach themselves to use tools.Advances in neural information processing systems, 36:
68539–68551, 2023.
[40] Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, and Hannaneh Hajishirzi. Self-rag: Learn-
ing to retrieve, generate, and critique through self-reflection. InThe Twelfth International
Conference on Learning Representations, 2023.
[41] Yuqin Dai, Guoqing Wang, Yuan Wang, Kairan Dou, Kaichen Zhou, Zhanwei Zhang, Shuo
Yang, Fei Tang, Jun Yin, Pengyu Zeng, et al. Evinote-rag: Enhancing rag models via answer-
supportive evidence notes.arXiv preprint arXiv:2509.00877, 2025.
[42] Peiran Xu, Zhuohao Li, Xiaoying Xing, Guannan Zhang, Debiao Li, and Kunyu Shi. Hy-
brid reward normalization for process-supervised non-verifiable agentic tasks.arXiv preprint
arXiv:2509.25598, 2025.
[43] Wenlin Zhang, Xiangyang Li, Kuicai Dong, Yichao Wang, Pengyue Jia, Xiaopeng Li, Yingyi
Zhang, Derong Xu, Zhaocheng Du, Huifeng Guo, Ruiming Tang, and Xiangyu Zhao. Process vs.
outcome reward: Which is better for agentic RAG reinforcement learning. InThe Thirty-ninth
Annual Conference on Neural Information Processing Systems, 2026.
12

## Page 13

[44] Bowei He, Minda Hu, Zenan Xu, Hongru Wang, Licheng Zong, Yankai Chen, Chen Ma,
Xue Liu, Pluto Zhou, and Irwin King. Search-r2: Enhancing search-integrated reasoning via
actor-refiner collaboration.arXiv preprint arXiv:2602.03647, 2026.
[45] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin,
Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton,
Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul F. Christiano,
Jan Leike, and Ryan Lowe. Training language models to follow instructions with human
feedback. InAdvances in Neural Information Processing Systems 35: Annual Conference on
Neural Information Processing Systems 2022, NeurIPS 2022, New Orleans, LA, USA, November
28 - December 9, 2022, 2022.
[46] Leslie Pack Kaelbling, Michael L Littman, and Andrew W Moore. Reinforcement learning: A
survey.Journal of artificial intelligence research, 4:237–285, 1996.
[47] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal
policy optimization algorithms.arXiv preprint arXiv:1707.06347, 2017.
[48] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and
Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model.
Advances in neural information processing systems, 36:53728–53741, 2023.
13

## Page 14

A More Experimental Results
A.1 Ablation of Evaluation Metrics
To provide a more comprehensive evaluation, we further assess MultiSearch-3B-Base using additional
metrics, including F1 score (F1) and Coverage Exact Match (CEM). As shown in Table 5, MultiSearch
consistently outperforms the baseline methods Search-R1 and AutoRefine across all evaluated metrics,
verifying the effectiveness of our framework.
Table 5: Ablation of Evaluation Metrics.
Metrics Methods Single-Hop QA Multi-Hop QA
NQ TriviaQA PopQA HotpotQA 2Wiki Musique Bamboogle Avg.
EM
Search-R1 0.421 0.583 0.413 0.297 0.274 0.066 0.128 0.312
AutoRefine 0.467 0.620 0.450 0.405 0.393 0.157 0.344 0.405
MultiSearch0.471 0.630 0.455 0.431 0.413 0.163 0.390 0.422
F1
Search-R1 0.476 0.650 0.429 0.380 0.322 0.123 0.184 0.366
AutoRefine 0.534 0.689 0.479 0.503 0.453 0.233 0.449 0.477
MultiSearch0.564 0.703 0.497 0.544 0.483 0.256 0.542 0.513
CEM
Search-R1 0.462 0.642 0.442 0.325 0.288 0.082 0.128 0.338
AutoRefine 0.502 0.674 0.468 0.440 0.428 0.175 0.384 0.439
MultiSearch0.514 0.679 0.471 0.466 0.458 0.181 0.433 0.457
A.2 Ablation of Training Datasets
MultiSearch is trained on a combined dataset of single-hop NQ and multi-hop HotpotQA, following
prior work settings. To examine the effectiveness of this design, we further conduct experiments
by training on single-hop data only (NQ) and multi-hop data only (HotpotQA), respectively. The
results are reported in Table 6.S-avgandM-avgdenotes the average accuracy over three single-hop
datasets and four multi-hop datasets. We observe that the joint training setting achieves the best
overall performance. In contrast, training solely on NQ leads to degraded performance on multi-hop
tasks, while training solely on HotpotQA results in lower performance on single-hop tasks. These
suggest that joint training on both types of data provides a more balanced learning signal across
different reasoning settings.
Table 6: Comparison between different types of training datasets.
Training Datasets Single-Hop QA Multi-Hop QA
NQ TriviaQA PopQA S-Avg. HotpotQA 2Wiki Musique Bamboogle M-Avg. Avg.
Single + Multi 0.470 0.615 0.444 0.510 0.420 0.412 0.183 0.371 0.371 0.416
Multi 0.384 0.594 0.385 0.454 0.395 0.345 0.155 0.361 0.314 0.374
Single 0.459 0.601 0.438 0.499 0.306 0.206 0.080 0.197 0.197 0.327
A.3 Impact of Different Reward Modeling Methods
As described in Section 2.2, we adopt a conditional aggregation scheme for answer reward rans
and step-specific rewards rquery & rmerge, which are calculated over all the <search> and <merge>
blocks in the rollout. To investigate the effect of reward design, we conduct additional experiments
with three variants: (1) Unconditional: rquery and rmerge are applied regardless of whether the final
answer is correct. (2) Turn-Level: rquery and rmerge are calculated at each turn, and the final reward is
averaged over all turns. (3) EM: rans is calculated using Extract Match, instead of F1 score. Results in
Table 7 show that our reward modeling method achieves higher overall accuracy. This suggests that
associating process rewards with the final outcome may help better align intermediate behaviors with
task success, and that F1-based rans could provide more informative feedback than EM in this setting.
A.4 Impact of Different Merging Modules
As described in Section 2.1, the merging step is carried out by the search agent itself. We further
analyze the effect of different merging strategies, including: (1) selecting the most relevant passages
14

## Page 15

Table 7: Comparison between different Reward Designs.
Variants NQ TriviaQA PopQA HotpotQA 2Wiki Musique Bamboogle Avg.
Our Method 0.470 0.615 0.444 0.420 0.412 0.183 0.371 0.416
Conditional vs. Unconditional
Unconditional 0.427 0.593 0.418 0.352 0.343 0.113 0.303 0.364
Rollout-Level vs. Turn-Level
Turn-Level 0.400 0.602 0.396 0.399 0.411 0.150 0.330 0.384
F1 vs. EM
EM 0.461 0.610 0.433 0.405 0.403 0.165 0.341 0.403
using TF-IDF (TF-IDF Screening), and (2) using an external LLM to merge retrieved information
(LLM Extractor). To control for model size, we employ Qwen2.5-3B-Instruct as the external extractor.
As shown in Table 8, TF-IDF-based selection yields relatively poor results, suggesting that textual
similarity to the question does not necessarily indicate usefulness. The variants using an external
3B-LLM also achieve lower ultimate performance than MultiSearch, likely because the merging step
is not integrated into the model’s optimization process. These observations highlight the potential
benefits of our agent-driven merging paradigm.
Table 8: Comparison between different merging modules.
Variants NQ TriviaQA PopQA HotpotQA 2Wiki Musique Bamboogle Avg.
MultiSearch 0.470 0.615 0.444 0.420 0.412 0.183 0.371 0.416
w/ TF-IDF Screening 0.383 0.517 0.375 0.286 0.244 0.116 0.218 0.308
w/ LLM Extractor 0.407 0.577 0.397 0.341 0.341 0.136 0.288 0.355
A.5 Comparison Between Base & Instruct models
We analyze the performance differences between the base and instruction-tuned models. As shown in
Figure 8, the instruction-tuned model outperforms the base model in the early stages, but the base
model gradually catches up, ultimately reaching comparable or even superior performance. This
suggests that while instruction-tuning improves the model’s ability to follow human instructions, its
prior knowledge may limit its generalization to multi-step reasoning tasks.
/uni00000013/uni00000015/uni00000018/uni00000018/uni00000013/uni0000001a/uni00000018/uni00000014/uni00000013/uni00000013/uni00000014/uni00000015/uni00000018/uni00000014/uni00000018/uni00000013/uni00000014/uni0000001a/uni00000018
/uni00000036/uni00000057/uni00000048/uni00000053
/uni00000013/uni00000011/uni00000014
/uni00000013/uni00000011/uni00000015
/uni00000013/uni00000011/uni00000016
/uni00000013/uni00000011/uni00000017
/uni00000013/uni00000011/uni00000018/uni00000035/uni00000048/uni0000005a/uni00000044/uni00000055/uni00000047
/uni00000024/uni00000051/uni00000056/uni0000005a/uni00000048/uni00000055/uni00000003/uni00000035/uni00000048/uni0000005a/uni00000044/uni00000055/uni00000047
/uni00000030/uni00000058/uni0000004f/uni00000057/uni0000004c/uni00000036/uni00000048/uni00000044/uni00000055/uni00000046/uni0000004b/uni00000010/uni00000025/uni00000044/uni00000056/uni00000048
/uni00000030/uni00000058/uni0000004f/uni00000057/uni0000004c/uni00000036/uni00000048/uni00000044/uni00000055/uni00000046/uni0000004b/uni00000010/uni0000002c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057
/uni00000013/uni00000015/uni00000018/uni00000018/uni00000013/uni0000001a/uni00000018/uni00000014/uni00000013/uni00000013/uni00000014/uni00000015/uni00000018/uni00000014/uni00000018/uni00000013/uni00000014/uni0000001a/uni00000018
/uni00000036/uni00000057/uni00000048/uni00000053
/uni00000013/uni00000011/uni00000013/uni00000013
/uni00000013/uni00000011/uni00000013/uni00000014
/uni00000013/uni00000011/uni00000013/uni00000015
/uni00000013/uni00000011/uni00000013/uni00000016
/uni00000013/uni00000011/uni00000013/uni00000017
/uni00000013/uni00000011/uni00000013/uni00000018/uni00000035/uni00000048/uni0000005a/uni00000044/uni00000055/uni00000047
/uni00000030/uni00000058/uni0000004f/uni00000057/uni0000004c/uni00000010/uni00000034/uni00000058/uni00000048/uni00000055/uni0000005c/uni00000003/uni00000035/uni00000048/uni0000005a/uni00000044/uni00000055/uni00000047
/uni00000030/uni00000058/uni0000004f/uni00000057/uni0000004c/uni00000036/uni00000048/uni00000044/uni00000055/uni00000046/uni0000004b/uni00000010/uni00000025/uni00000044/uni00000056/uni00000048
/uni00000030/uni00000058/uni0000004f/uni00000057/uni0000004c/uni00000036/uni00000048/uni00000044/uni00000055/uni00000046/uni0000004b/uni00000010/uni0000002c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057
/uni00000013/uni00000015/uni00000018/uni00000018/uni00000013/uni0000001a/uni00000018/uni00000014/uni00000013/uni00000013/uni00000014/uni00000015/uni00000018/uni00000014/uni00000018/uni00000013/uni00000014/uni0000001a/uni00000018
/uni00000036/uni00000057/uni00000048/uni00000053
/uni00000013/uni00000011/uni00000013/uni00000013
/uni00000013/uni00000011/uni00000013/uni00000014
/uni00000013/uni00000011/uni00000013/uni00000015
/uni00000013/uni00000011/uni00000013/uni00000016
/uni00000013/uni00000011/uni00000013/uni00000017
/uni00000013/uni00000011/uni00000013/uni00000018/uni00000035/uni00000048/uni0000005a/uni00000044/uni00000055/uni00000047
/uni00000030/uni00000048/uni00000055/uni0000004a/uni0000004c/uni00000051/uni0000004a/uni00000003/uni00000035/uni00000048/uni0000005a/uni00000044/uni00000055/uni00000047
/uni00000030/uni00000058/uni0000004f/uni00000057/uni0000004c/uni00000036/uni00000048/uni00000044/uni00000055/uni00000046/uni0000004b/uni00000010/uni00000025/uni00000044/uni00000056/uni00000048
/uni00000030/uni00000058/uni0000004f/uni00000057/uni0000004c/uni00000036/uni00000048/uni00000044/uni00000055/uni00000046/uni0000004b/uni00000010/uni0000002c/uni00000051/uni00000056/uni00000057/uni00000055/uni00000058/uni00000046/uni00000057
Figure 8: Training dynamics of base and instruct models.
A.6 Impact of Different Retrievers
We compare two retriever variants: E5-base-v2 and BM25, with results reported in Table 9. As
shown, E5-base-v2 achieves a better overall performance, suggesting that dense retrieval may provide
more relevant evidence than lexical matching in our setting.
15

## Page 16

Table 9: Comparison between different retrievers.
Variants NQ TriviaQA PopQA HotpotQA 2Wiki Musique Bamboogle Avg.
E5 0.470 0.615 0.444 0.420 0.412 0.183 0.371 0.416
BM25 0.336 0.592 0.329 0.384 0.391 0.108 0.168 0.330
B Prompts
B.1 Training Prompt for Search Agents
Search Agent Prompt
Role.You are a helpful assistant. Answer the given question with multi-turn search engine calling. You
can search as many times as necessary.
Input.Question:{question}.
Instructions.Reason through the available information using <think> and</think>. Issue a search
request using <search>q 1, q2, ...qn </search> when missing knowledge. The retrieved documents
will be placed in <information> and </information>. Generate three diverse search queries
each time, applying one or more of these strategies: rephrasing, concept expansion, and question
decomposition. Extract and integrate key information from the retrieved documents in <merge> and
</merge>after each search.
Output.Return a concise final answer inside <answer> and </answer>, without detailed illustrations.
B.2 Prompt for LLM Extractor
LLM Extractor Prompt
Role.You are a document integration assistant.
Input.Question:{question}. Documents:{documents}.
Instructions.Given a question and some documents, extract and integrate key information that is useful
for the question.
Output.Output only the integrated summary, without any extra commentary.
B.3 Prompt for SNR Evaluation
SNR Evaluation Prompt
Role.You are an evaluator of information quality. Your task is to assess the Signal-to-Noise Ratio of a
given piece of content, based on a question and supporting documents.
Input.Question: {question}. Supporting Documents: {documents}. Content to be evaluated:
{content}.
Instructions."Signal" represents information that is directly relevant to answering the question. "Noise"
represents information that is irrelevant to the question, redundant, contradictory to the supporting
documents, or hallucinated. Read the question and the supporting documents carefully, analyze the
content, and determine which parts are "signal" (useful, relevant, supported) and which parts are "noise"
(useless, irrelevant, unsupported, or repetitive).
Output.Provide a SNR between 0 and 1.
C More Experimental Details
C.1 Training Details
MultiSearch is trained using the AdamW optimizer with a learning rate of 1×10 −6 and a constant
learning rate schedule without warmup. Weight decay is set to 0.01, and gradients are clipped with a
maximum norm of 1.0. Training is conducted for 200 optimization steps using Fully Sharded Data
16

## Page 17

Parallel (FSDP) without offloading parameters, gradients, or optimizer states. We use 4 NVIDIA
A100 GPUs for 3B models, while larger configurations are trained on 8 NVIDIA A100 GPUs.
During training, rollout generation is performed using vLLM1 with a sampling temperature of 1.0 and
top-p set to 0.95. We adopt GDPO for policy optimization with a group size of 5. At each interaction
step, the agent can issue up to 3 search queries, and the retrieval system returns the top 3 documents
for each query. Key hyperparameters are summarized in Table 10.
Increasing the number of queries or retrieved documents per step may lead to longer rollouts due to
the additional reasoning required. However, the resulting increase in generation time is relatively
moderate. Moreover, because MultiSearch requires fewer reasoning steps, as shown in Figure 3b,
the overall runtime remains comparable despite the longer per-step reasoning time. Given the
performance gains observed in Section 3.5, we consider this trade-off acceptable for the present
experiments.
Table 10: Hyperparameters used by MultiSearch.
Hyper-parameters Value
Learning Rate1×10 −6
Training Batch Size 512
Validation Batch Size 512
Max Response Length 2048
Micro Training Batch Size 32
Group SizeG5
KL Coefficientβ0.001
Max Search Turns 4
Clip Ratioϵ0.2
Total Training Steps 300
C.2 Dataset Details
The datasets we used are from FlashRAG Datasets 2. Here, we present the detailed statistics in
Table 11.
Table 11: Statistics of the seven datasets.
Split Single-Hop QA Multi-Hop QA
NQ TriviaQA PopQA HotpotQA 2Wiki Musique Bamboogle
# Train 79168 78785 - 90447 15,000 19,938 -
# Dev 8757 8837 - 7405 12576 2417 -
# Test 3610 11313 14267 - - - 125
D Case Studies
Here, we present a case study comparing Search-R1 and MultiSearch in Table 12. The example
illustrates that MultiSearch retrieves more relevant information through multi-query retrieval and
further improves the SNR of the intermediate context through explicit merging.
E Limitations
Despite the promising results, our work has several limitations:
1https://github.com/vllm-project/vllm
2https://huggingface.co/datasets/RUC-NLPIR/FlashRAG_datasets
17

## Page 18

Limited Task Generalization.The experiments are conducted exclusively on question-answering
datasets following prior work, without other types of tasks or domains. As a result, the generality of
MultiSearch beyond QA settings remains to be explored.
Predefined Retrieval Corpus.The method relies on a static retrieval corpus for all experiments.
Its performance in fully online search environments, such as live web search engines, has not been
tested, which may limit its applicability in dynamic information retrieval scenarios.
Fixed Query Generation Strategies.While we explore multiple strategies for generating queries,
the underlying framework still operates within a relatively fixed set of strategies. This may restrict
flexibility in more open-ended or unstructured reasoning tasks.
F Broader Impacts
MultiSearch explores a parallel search and explicit merging framework. By encouraging the agent
to maintain multiple candidate searching directions, it can help broaden the scope of information
acquisition during the reasoning process, particularly in scenarios where relevant evidence is dis-
tributed across multiple sources. This suggests a possible direction for dynamically balancing search
breadth and reasoning depth depending on task difficulty. Furthermore, by making the merging
process explicit, MultiSearch introduces a more structured interface between retrieval and reasoning.
This “explore-then-merge” pattern encourages the agent to organize retrieved evidence prior to final
inference, contributing to a clearer understanding of how retrieved passages are integrated. In this
sense, the framework could facilitate more detailed post-hoc analysis of evidence usage, although we
do not explicitly evaluate interpretability in this work.
18

## Page 19

Table 12: Comparison between Search-R1 and MultiSearch. The predictions are coloredRedfor
incorrect andGreenfor correct answers. Yellow segmentsdenote the core evidences.
Question 1: What is the name of the Sunday before Easter Sunday?
Ground Truth: Palm Sunday.
Search-R1
# Think: Easter Sunday is a Christian holiday celebrating the resurrection of Jesus Christ. Sunday
before Easter Sunday falls on a different name due to its significance in the Christian calendar.
#Search:What is the name of the Sunday before Easter Sunday?
# Info: ... Doc 2(Title: Easter) ...The week beginning with Easter Sunday ... The day before Easter
is properly called Holy Saturday. Doc 3(Title: Quinquagesima) ... is one of the names used in the
Western Church for the Sunday before Ash Wednesday... the fifty days before Easter Day using
inclusive counting which counts both Sundays ...
# Answer:Good Friday.
MultiSearch
# Think: First, we need to find out what is the name of the Sunday that comes before Easter
Sunday. We can search directly or by asking for the name of the week before Easter Sunday.
# Search: name of the sunday before easter sunday,name of the week before easter sunday,
when is the sunday before easter sunday
# Info: Doc 1(Title: Easter) ... The Sunday before Easer is Palm Sunday, with the Wednesday
before Easter being known as Spy Wednesday ... Doc 5(Title: "Holy Week") Holy Week in
Christianity is the week just before Easter ... the last week of Lent, in the West, – Palm Sunday,
Holy Wednesday (Spy Wednesday), Maundy Thursday (Holy Thursday), ... – are all included.
#Merge:From the retrieved documents, we can see that the Sunday before Easter Sunday is Palm
Sunday.
# Answer:Palm Sunday.
Question 2: Are Portland International Airport and Gerald R. Ford International Airport both
located in Oregon?
Ground Truth: No.
Search-R1
# Think: To answer this question, I need to determine if both Portland International Airport
and Gerald R. Ford International Airport are located in the same geographic location, specifically
Oregon.
# Search: Are Portland International Airport and Gerald R. Ford International Airport both located
in Oregon?
# Info: Doc 1(Title: "Portland International Airport") Portland International Airport is ... and the
largest airport in the U.S. state of Oregon that accounts for ...
# Think: From the information provided, I can conclude that both Portland International Airport
and Gerald R. Ford International Airport are located in Oregon.
# Answer:Yes.
MultiSearch
# Think: First, we need to determine the locations of Portland International Airport and Gerald R.
Ford International Airport. Then, we’ll check if both airports are in Oregon.
# Search: where is Portland International Airport,where is airport Gerald R. Ford Interna-
tional Airport,are Portland International Airport located in Oregon
# Info: Doc 1(Title: "Portland International Airport") Portland International Airport is ... and
the largest airport in the U.S. state of Oregon that accounts for ... Doc 4(Title: "Gerald R. Ford
International Airport") ... Gerald R. Ford International Airport is a commercial airport in Cascade
Township approximately southeast of Grand Rapids, Michigan ...
#Merge:From the retrieved documents, we can see that Portland International Airport is in Oregon
and Gerald R. Ford International Airport is in Michigan. The two airports are not in the same state.
# Answer:No.
19
