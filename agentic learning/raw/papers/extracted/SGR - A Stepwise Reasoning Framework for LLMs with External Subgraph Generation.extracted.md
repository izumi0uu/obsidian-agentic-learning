# SGR: A Stepwise Reasoning Framework for LLMs with External Subgraph Generation - Extracted Text

- Source note: [[SGR - A Stepwise Reasoning Framework for LLMs with External Subgraph Generation]]
- Source PDF: `assets/SGR - A Stepwise Reasoning Framework for LLMs with External Subgraph Generation.pdf`
- Extracted: 2026-05-18
- Extractor: pypdf
- Pages: 9
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

SGR: A Stepwise Reasoning Framework for LLMs with External
Subgraph Generation
Xin Zhang1, Yang Cao2, Baoxing Wu1, Kai Song2, Siying Li1
1School of Information Science and Engineering, Chongqing Jiaotong University
2School of Computer Science and Technology, Chongqing University of Posts and Telecommunications
Abstract
Large Language Models (LLMs) have demon-
strated strong capabilities across diverse NLP
applications, such as translation, text genera-
tion, and question answering. Nevertheless,
they remain limited in complex settings that
demand deep reasoning and logical inference.
Since these models are trained on large-scale
text corpora, their generation process may still
introduce irrelevant, noisy, or factually incon-
sistent content. To mitigate this problem, we
introduce SGR, a stepwise framework that en-
hances LLM reasoning through external sub-
graph generation. SGR builds query-specific
subgraphs from external knowledge bases and
uses their semantic structure to support multi-
step inference. By grounding intermediate rea-
soning steps in structured external knowledge,
the framework helps the model concentrate on
relevant entities, relations, and supporting ev-
idence. In particular, SGR first constructs a
subgraph tailored to the input question. It then
guides the model to reason progressively over
the generated structure and combines multiple
reasoning trajectories to obtain the final pre-
diction. Experimental results across several
benchmark datasets show that SGR achieves
consistent improvements over competitive base-
lines, highlighting its value for improving both
reasoning accuracy and factual reliability.
1 Introduction
Recent advances in large language models (LLMs)
have become a major milestone in the development
of artificial intelligence. By pretraining on large-
scale textual corpora, these models can produce flu-
ent and high-quality text (Brown et al., 2020). With
additional supervised fine-tuning, they can also be
adapted to various downstream natural language
processing tasks (Wei et al., 2022). Nevertheless,
despite their impressive generation ability, LLMs
still exhibit notable weaknesses in complex reason-
ing settings. In particular, while they are effective
at generating coherent text, they may fail to pre-
serve logical consistency, resulting in outputs that
conflict with real-world facts. In addition, because
of their large parameter scale and opaque internal
mechanisms, the reasoning behavior of LLMs is
often difficult to interpret (Jacovi and Goldberg,
2020).
One promising way to mitigate these issues is
to incorporate external knowledge resources, espe-
cially knowledge graphs (KGs), into LLM-based
reasoning. KGs provide an explicit and struc-
tured representation of factual knowledge, which
can compensate for some limitations of paramet-
ric language models (Ji et al., 2021). Prior work
has investigated the use of KGs as supplemen-
tary knowledge sources for improving the rea-
soning ability of LLMs (Lewis et al., 2020; Yao
and Van Durme, 2014). In general, these ap-
proaches introduce KG-derived information into
LLMs through prompt construction or additional
contextual inputs, thereby supporting the reasoning
process. Beyond KG-based enhancement, recent
research has also studied the integration of LLMs
with symbolic or structural representations to im-
prove systematic generalization and interpretability
(Yang et al., 2024b,a; Xiong et al., 2025). However,
many existing KG-injection methods still depend
on fixed or manually crafted prompt templates and
therefore fail to sufficiently utilize the rich struc-
tural information encoded in knowledge graphs
(Jiang et al., 2023; Yao et al., 2023).
Motivated by this observation, we introduce
SGR, a stepwise reasoning enhancement frame-
work for LLMs based on external subgraph gen-
eration. SGR uses schema-guided subgraph con-
struction over knowledge graphs to identify query-
relevant knowledge more accurately. By dynami-
cally building external subgraphs, the framework
guides LLMs to reason progressively, which helps
reduce the impact of irrelevant or noisy information
and improves reasoning accuracy. Moreover, SGR
1
arXiv:2605.16117v1  [cs.CL]  15 May 2026

## Page 2

combines direct reasoning with integrated reason-
ing strategies to generate the final enhanced output.
Experiments conducted on multiple benchmark
datasets show that SGR outperforms existing meth-
ods. The main contributions of this paper are sum-
marized as follows.
• We introduce a new stepwise reasoning en-
hancement framework that strengthens LLM
reasoning by incorporating externally gener-
ated subgraphs. This method improves the
capacity of LLMs to address complex multi-
step reasoning problems.
• We develop an interpretable knowledge-
enhanced reasoning procedure that increases
the transparency of LLM reasoning. The gen-
erated reasoning paths and final outputs can
be traced and verified.
• We conduct extensive experiments on several
benchmark datasets, confirming the effective-
ness of the proposed framework and showing
its advantages over prior approaches.
2 Related Work
Knowledge graphs organize extensive external
world knowledge as structured triples and have
been widely adopted for knowledge representation
and reasoning (Nickel et al., 2015). Early research
investigated how structured knowledge could be
incorporated into neural models (Sun et al., 2019).
More recently, many studies have attempted to
strengthen LLMs by injecting KG-derived knowl-
edge at either the training or inference stage, lead-
ing to improved performance on diverse tasks (Hu
et al., 2023). In addition to static KGs, temporal
knowledge graphs have been developed to model
the evolving states of entities and relations across
time, supporting richer reasoning under temporal
constraints (Xiong et al., 2024b,a). Nevertheless,
directly encoding KG knowledge into LLM param-
eters can substantially increase training costs and
limit model flexibility (Baek et al., 2023).
To alleviate this problem, recent work has ex-
plored retrieving query-relevant knowledge from
KGs at inference time and supplying it to LLMs
as supplementary context (Lewis et al., 2020; Guu
et al., 2020). Existing methods in this direction
can generally be divided into retrieval-enhanced
approaches and collaborative enhancement ap-
proaches.
2.1 Retrieval Enhanced Models
Retrieval-enhanced models aim to obtain relevant
information from an external knowledge source
and feed it into the language model, helping the
model generate more accurate answers (Lewis
et al., 2020). Jiang et al. introduced StructGPT, a
structured reasoning retrieval framework that com-
bines iterative reading and reasoning mechanisms
(Jiang et al., 2023). Other related studies further
investigate multi-hop retrieval and reasoning over
structured knowledge to improve answer accuracy
(Das et al., 2019; Chen et al., 2020).
Despite their effectiveness, retrieval-enhanced
approaches still have several practical limitations.
First, the retrieved content may fail to cover the
complete structured reasoning paths encoded in the
knowledge graph, leading to incomplete reasoning
chains (Das et al., 2019). Second, retrieving too
much information can introduce irrelevant evidence
and overwhelm the model, which may reduce rea-
soning performance (Izacard and Grave, 2021). Fi-
nally, when the retrieved knowledge includes errors
or redundant facts, it can negatively influence the
final reasoning outcome (Petroni et al., 2021).
2.2 Collaborative Enhanced Models
Collaborative enhancement methods focus on build-
ing interaction mechanisms between LLMs and
knowledge graphs. Under this paradigm, both the
language model and the KG participate in the rea-
soning process to produce final answers (Zhang
et al., 2022; Zhou et al., 2022). Typically, these
methods first use the language model to generate an
initial reasoning result, then employ the knowledge
graph to validate or refine intermediate outputs, and
finally obtain an enhanced answer. For example,
Zhang et al. (2022) proposed a KG-enhanced rea-
soning framework in which the language model per-
forms initial reasoning over the query, after which
the knowledge graph is used for validation and cor-
rection. By iteratively interacting with the KG, the
system progressively improves reasoning accuracy.
Compared with retrieval-enhanced methods, col-
laborative enhancement approaches place greater
emphasis on bidirectional interaction between the
language model and the knowledge graph. In this
setting, the language model not only receives graph-
based knowledge, but also produces intermediate
hypotheses that guide subsequent KG queries (Pan
et al., 2024). Although this paradigm can im-
prove reasoning robustness, it continues to face
2

## Page 3

Figure 1: Pipeline of SGR framework.
challenges in interaction efficiency and reasoning
consistency.
3 Methodology
To more effectively combine the reasoning abil-
ity of large language models with the structured
knowledge provided by external knowledge graphs,
we introduce SGR, a stepwise reasoning enhance-
ment framework based on external subgraph gen-
eration. As illustrated in the overall framework,
SGR consists of three major components: struc-
tured subgraph construction, stepwise reasoning
enhancement, and collaborative reasoning integra-
tion.
Given an input question, the framework first con-
verts it into a structured query and retrieves a rel-
evant subgraph from the knowledge graph. The
language model then performs step-by-step reason-
ing grounded in the generated subgraph to obtain
candidate answers. Finally, reasoning results from
multiple paths are integrated to produce the final
output.
3.1 Structured Subgraph Generation
3.1.1 Knowledge Graph Construction
Let the external knowledge graph be denoted as
G= (V,E,R),(1)
where V is the set of entities,R is the set of relation
types, and E ⊆ V × R × Vrepresents the set of
factual triples. Each triple (h, r, t)∈ Eindicates
that a head entity h is connected to a tail entity t
through relationr.
For an input question q, SGR first constructs a
structured representation by extracting key entities,
relations, and constraints:
Sq ={V q,Rq,Cq},(2)
where Vq ⊆ Vdenotes the question-related entities,
Rq ⊆ Rdenotes the relevant relations, and Cq rep-
resents additional semantic or logical constraints
derived from the question.
The objective of subgraph construction is to iden-
tify a compact query-relevant subgraph
Gq = (V∗
q ,E ∗
q ,R∗
q),(3)
where V∗
q ⊆ V, R∗
q ⊆ R, and E∗
q ⊆ E. This
subgraph serves as the structured knowledge foun-
dation for later reasoning.
The generated subgraph provides explicit rela-
tional paths that guide the language model during
reasoning. Compared with unstructured textual
context, this structured representation allows finer
control over the reasoning process and helps reduce
the influence of irrelevant information.
3

## Page 4

3.1.2 Subgraph Generation Process
The subgraph construction procedure contains
three main steps. First, the language model iden-
tifies the central entities and relations in the input
question. Second, the knowledge graph is queried
to obtain related entities and relations, forming can-
didate subgraphs. Third, nodes and edges with low
semantic relevance to the question are filtered out.
Formally, for each candidate triple ei =
(hi, ri, ti), we compute a relevance score with re-
spect to the input question:
s(ei, q) = sim (ϕ(ei), ϕ(q)),(4)
where ϕ(·) denotes a semantic encoder andsim(·,·)
measures semantic similarity. The final subgraph is
selected by retaining triples whose relevance scores
exceed a thresholdτ:
E∗
q ={e i ∈ E |s(ei, q)≥τ}.(5)
Alternatively, the subgraph can be obtained by
selecting the top-kmost relevant triples:
E∗
q = TopKei∈E s(ei, q).(6)
By producing a query-specific subgraph for each
input, SGR avoids the restrictions of fixed prompt
templates and makes better use of the structural
information contained in the knowledge graph.
3.2 Stepwise Reasoning Enhancement
Using the generated subgraph, SGR guides the lan-
guage model to reason in a stepwise manner. Let a
reasoning path be represented as
p= (e1, e2, . . . , eT ),(7)
where each et ∈ E∗
q is a selected triple at reasoning
step t. At each step, the language model generates
an intermediate reasoning state zt conditioned on
the question, the previous reasoning states, and the
current subgraph evidence:
zt =f θ(q, z<t, et),(8)
where fθ denotes the LLM parameterized by θ, and
z<t represents previous reasoning states.
The probability of generating a complete reason-
ing trajectory can be written as
Pθ(z1:T |q,G q) =
TY
t=1
Pθ(zt |q, z<t,Gq).(9)
To encourage the reasoning process to follow
the generated subgraph, we introduce a path con-
sistency score:
C(p,G q) = 1
T
TX
t=1
I(et ∈ E∗
q ),(10)
where I(·) is an indicator function. A higher score
indicates that the reasoning path is more consistent
with the retrieved structured knowledge.
The final stepwise reasoning objective can be
described as selecting the answer with the highest
joint reasoning confidence and structural consis-
tency:
ˆa= arg max
a
Pθ(a|q,G q)·C(p,G q).(11)
This step-by-step reasoning mechanism allows
the model to decompose complex reasoning prob-
lems into smaller subproblems. By explicitly fol-
lowing relational paths in the generated subgraph,
the model can reduce logical inconsistency and
improve reasoning accuracy.
3.3 Collaborative Reasoning Integration
In the final stage, SGR combines multiple reason-
ing paths obtained from different traversals of the
subgraph. Suppose the framework generates M
candidate reasoning paths:
P={p 1, p2, . . . , pM }.(12)
Each path pi produces a candidate answer ai with
confidence score αi. The confidence of each path
is computed based on both language model proba-
bility and graph consistency:
αi =λP θ(ai |q, pi) + (1−λ)C(pi,Gq),(13)
where λ∈[0,1] controls the balance between
model confidence and structural consistency.
The final answer is obtained by aggregating can-
didate answers from different reasoning paths:
ˆa= arg max
a
MX
i=1
αi ·I(a i =a).(14)
This integration step improves robustness by
reducing the influence of errors from any single
reasoning path. Overall, SGR provides a unified
framework that brings together structured knowl-
edge, stepwise inference, and collaborative inte-
gration to strengthen the reasoning ability of large
language models.
4

## Page 5

The model first conducts entity-based reasoning
to generate a structured subgraph schema. This
schema represents the external knowledge relevant
to the input query. Specifically, the language model
is prompted to act as a knowledge graph expert and
is provided with several knowledge graph triples.
It is asked to reason over these triples and construct
a structured query schema. The model first extracts
core entities and relations from the question, and
then organizes them into a schema that captures
the logical structure required for reasoning. For
example, given a question, the model may iden-
tify a chain of entities and relations, such as entity
one linked by a relation to entity two, entity two
connected to entity three, and entity three further
connected to entity four. The resulting schema
consists of entity-relation pairs that describe the
reasoning path needed to answer the question. Dur-
ing this procedure, SGR uses schema-based rea-
soning to narrow the search space for knowledge
graph queries. The generated schema is then used
to construct a structured query in Neo4j, enabling
accurate retrieval of relevant knowledge.
3.4 Direct Reasoning Enhancement
3.4.1 Cypher LLM
During the direct reasoning enhancement stage,
the framework first constructs a Cypher query ac-
cording to the generated schema. Let the schema
produced from the input questionqbe denoted as
Sq ={(v i, ri, vj)}L
i=1,(15)
where vi and vj represent entities or entity vari-
ables, ri denotes a relation type, and L is the num-
ber of schema-level relational constraints.
The goal of the Cypher generation module is to
transformS q into an executable Cypher query:
cq =g ϕ(q,S q),(16)
where gϕ denotes the NLCypher module parame-
terized by ϕ, and cq is the generated Cypher query.
NLCypher serves as the language interface that
maps natural language questions and structured
schemas into Cypher queries executable on the
Neo4j database.
The generated Cypher query is then executed
over the knowledge graph G to retrieve candidate
answers:
Aq = Exec(cq,G),(17)
where Exec(·) denotes the database execution func-
tion and Aq ={a 1, a2, . . . , aN } is the set of re-
trieved candidate answers.
The retrieved results are combined with the orig-
inal question and provided to the large language
model as structured evidence:
ˆa= arg max
a∈Aq
Pθ(a|q,A q,Sq),(18)
where Pθ represents the answer probability esti-
mated by the LLM. This formulation allows the
model to generate answers grounded in both the
natural language question and the retrieved struc-
tured knowledge.
In our experiments, we use approximately 140K
knowledge graph queries across several datasets.
We evaluate Cypher-based reasoning with GPT-
based models. The results show that the Cypher-
guided reasoning procedure improves question-
answering accuracy, especially for complex multi-
hop reasoning cases.
3.4.2 Answer Validation
After candidate answers are retrieved through
Cypher queries, the framework validates them
by checking whether they are consistent with the
retrieved knowledge and the generated schema.
Given a candidate answer ai ∈ Aq, we define a
validation function:
V(a i,Sq,G) =I[a i |=Sq inG],(19)
where I[·] is the indicator function, and ai |=G Sq
means that candidate answerai satisfies the schema
constraints inG.
The valid answer set is therefore defined as
A+
q ={a i ∈ Aq |V(a i,Sq,G) = 1}.(20)
If A+
q is non-empty, the final answer is selected
from the validated candidate set:
ˆa= arg max
ai∈A+
q
Pθ(ai |q,A +
q ,Sq).(21)
Otherwise, if no candidate answer satisfies the
schema constraints, the framework triggers addi-
tional reasoning steps:
A+
q =∅⇒Refine(q,S q,G).(22)
This validation mechanism helps reduce halluci-
nated responses and maintains consistency between
the language model outputs and the underlying
knowledge graph.
5

## Page 6

Table 1: Performance comparison of different reasoning methods on CWQ, WebQSP, and GrailQA. Hits@1 and
accuracy are reported where applicable, and the best results for each metric are highlighted in bold. Note: Best
results are taken from prior work, includingα,β,γ, andδ.
Method CWQ WebQSP GrailQA
Hits@1 Acc Hits@1 Acc Hits@1 Acc
IO Prompt / ChatGPT 0.376 0.256 0.633 0.582 0.294 0.223
CoT / ChatGPT 0.388 0.258 0.622 0.577 0.281 0.201
Prior FT SOTA 0.704 α – 0.821 β – 0.754 γ –
Prior Prompting SOTA – – 0.744 δ – 0.532 δ –
SGR / Cypher LLM 0.523 0.445 0.745 0.706 0.624 0.593
SGR / ChatGPT 0.578 0.526 0.801 0.784 0.713 0.633
StructGPT / ChatGPT – – 0.726 – – –
ToG / ChatGPT 0.571 – 0.762 – 0.687 –
ToG / GPT-40.725– 0.826 –0.814–
SGR / GPT-4 0.6320.590 0.826 0.8080.7560.703
3.5 Collaborative Reasoning Enhancement
When direct reasoning fails to produce a correct
answer, the framework applies collaborative rea-
soning enhancement. In this stage, the language
model and the knowledge graph interact iteratively
to improve the reasoning process. At iteration t,
the language model generates an intermediate hy-
pothesis:
ht =f θ(q,E <t, h<t),(23)
where E<t denotes the evidence retrieved in previ-
ous iterations, and h<t represents earlier hypothe-
ses.
The knowledge graph then verifies and expands
this hypothesis by retrieving supporting evidence:
Et = Retrieve(ht,G),(24)
where Et contains the graph triples relevant to the
current hypothesis. The retrieved evidence is fed
back into the language model for the next reasoning
step:
ht+1 =f θ(q, h≤t,E≤t).(25)
The iterative process can be expressed as:
(q, ht) KG retrieval− − − − − − → Et
LLM reasoning
− − − − − − − − →ht+1.(26)
After T iterations, the framework obtains a set
of candidate reasoning paths:
P={p 1, p2, . . . , pM },(27)
where each path pi corresponds to a sequence of
hypotheses and retrieved evidence:
pi = (hi
1,E i
1, hi
2,E i
2, . . . , hi
T ,E i
T ).(28)
For each reasoning path, we compute a path
score based on model confidence and graph consis-
tency:
βi =λP θ(ai |q, pi) + (1−λ)C(pi,G),(29)
where λ∈[0,1] balances language model confi-
dence and structural consistency. The graph consis-
tency term is defined as:
C(pi,G) = 1
T
TX
t=1
I(Ei
t ⊆ G),(30)
whereI(·)is the indicator function.
The final answer is selected by aggregating can-
didate answers from all reasoning paths:
ˆa= arg max
a
MX
i=1
βi ·I(a i =a).(31)
Through iterative collaboration, the framework
explores multiple reasoning paths and progres-
sively moves toward a more accurate answer. This
strategy improves robustness when a single reason-
ing attempt is insufficient.
4 Experiments
4.1 Experimental Setup
We evaluate SGR on multiple benchmark datasets,
including CWQ, WebQSP, GrailQA, and KQA Pro.
CWQ targets complex question answering and re-
quires multi-hop reasoning over knowledge graphs.
WebQSP is a commonly used benchmark for
Freebase-based question answering. GrailQA fo-
cuses on generalization to previously unseen query
6

## Page 7

Figure 2: Impact brought by removing Schema prompts.
Figure 3: Impact brought by removing neo4j retrieval.
structures, while KQA Pro covers knowledge-
based question answering with diverse reasoning
patterns.
For evaluation, we adopt standard metrics, in-
cluding accuracy and F1 score. Accuracy reflects
the percentage of questions answered correctly,
whereas F1 measures the balance between preci-
sion and recall.
4.2 Experimental Results
To assess the effectiveness of the proposed method,
we conduct extensive experiments on two repre-
sentative datasets, CWQ and GrailQA, using input-
output prompting and chain-of-thought reasoning.
We compare SGR with several competitive base-
lines, including ChatGPT, CoT-based prompting,
and previous state-of-the-art methods.
First, we examine the role of external knowledge
by evaluating SGR under different settings. The
results show that incorporating external subgraph
information improves the reasoning performance of
large language models. Compared with approaches
that depend only on textual prompts, SGR obtains
better accuracy and Hits@1 scores on all evalu-
ated datasets, demonstrating the benefit of external
subgraph generation.
We also compare SGR against prior state-of-the-
art reasoning approaches. The results show that
SGR consistently achieves stronger performance
on both CWQ and GrailQA. In particular, SGR
brings clear improvements even for smaller lan-
guage models, suggesting that structured external
knowledge can help compensate for their limited
reasoning capacity. Furthermore, we study the gen-
eralization ability of SGR across different base
models. The results indicate that SGR provides con-
sistent gains when applied to both Cypher LLM and
ChatGPT, showing that the framework is model-
agnostic and can be integrated with various large
language models.
4.3 Ablation Study
To further examine the contribution of each com-
ponent, we conduct ablation studies on the CWQ
dataset. Specifically, we evaluate the effects of re-
moving schema-guided subgraph generation and
Neo4j-based retrieval.
The results show that removing schema-based
prompts causes a clear performance drop, confirm-
ing the importance of schema guidance for accu-
rate subgraph construction. Similarly, excluding
Neo4j-based retrieval substantially decreases rea-
soning accuracy, indicating that structured knowl-
edge retrieval is crucial for supporting multi-step
reasoning. These findings suggest that both schema
guidance and structured retrieval are key compo-
nents of SGR. Their combination is necessary for
achieving the best reasoning performance.
4.4 Application Scenarios and Error Analysis
SGR can be used for a broad range of knowledge-
intensive reasoning tasks, such as complex question
answering and logical inference. In practical set-
tings, SGR shows strong robustness and stability,
especially when tasks require multi-step reasoning
over structured knowledge.
We further perform error analysis to identify the
major causes of remaining failures. The results
show that most errors come from incomplete sub-
graph construction and ambiguous entity linking.
In some cases, missing or noisy facts in the external
knowledge graph also lead to incorrect reasoning
paths. Improving subgraph generation quality and
expanding knowledge coverage are therefore im-
portant directions for future work.
To further broaden the applicability of SGR, we
explore its use in the medical domain by combining
medical knowledge graphs with LLMs for complex
reasoning tasks, such as disease diagnosis and clin-
ical decision making. By constructing and using
structured medical knowledge graphs, SGR helps
7

## Page 8

Table 2: Ablation experiment results on the CWQ dataset
Method With Schema With neo4j Without Schema Without neo4j
Hits@1 Acc Hits@1 Acc Hits@1 Acc Hits@1 Acc
SGR/Cypher LLM 0.523 0.445 0.553 0.445 0.322 0.128 0.360 0.238
SGR/ChatGPT 0.578 0.526 0.578 0.526 0.400 0.319 0.431 0.374
LLMs reason over medical facts, symptoms, and
treatment relations, thereby improving reasoning
accuracy and reliability in real-world medical sce-
narios. To validate SGR across different domains,
we also conduct experiments on academic knowl-
edge graph reasoning tasks. The results show that
SGR consistently outperforms baseline methods
across multiple datasets. In addition, by dynami-
cally generating external subgraphs, the framework
allows LLMs to adapt their reasoning strategies to
different contexts, leading to more accurate reason-
ing and inference.
5 Conclusion
This paper presents SGR, a stepwise reasoning en-
hancement framework for large language models
based on external subgraph generation. By dy-
namically constructing query-relevant subgraphs
from knowledge graphs, SGR extracts structured
knowledge and guides LLMs through step-by-step
reasoning. By combining direct reasoning with
collaborative reasoning strategies, the framework
improves the accuracy and reliability of reasoning
results. Extensive experiments on multiple bench-
mark datasets demonstrate the strong reasoning
enhancement and generalization ability of SGR.
Moreover, the framework improves interpretability
by providing explicit reasoning paths grounded in
external knowledge.
Limitations
Although SGR demonstrates strong effectiveness,
it still has several limitations. First, the frame-
work incurs extra computational cost because it
requires subgraph generation and knowledge re-
trieval, which may reduce inference efficiency in
large-scale applications. Second, its performance
is influenced by the completeness and reliability of
the underlying knowledge graphs. If the external
knowledge contains missing, noisy, or inaccurate
information, the reasoning results may be affected.
In future work, we will improve the efficiency of
subgraph construction and retrieval, and investi-
gate lightweight deployment strategies to make the
framework more practical for real-world use.
References
Jinheon Baek, Alham Fikri Aji, and Amir Saffari. 2023.
Knowledge-augmented language model prompting
for zero-shot knowledge graph question answering.
arXiv preprint arXiv:2306.04136.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, and 1 others. 2020. Language models are
few-shot learners.Advances in neural information
processing systems, 33:1877–1901.
Wenhu Chen, Ming-Wei Chang, Eva Schlinger, William
Wang, and William W Cohen. 2020. Open ques-
tion answering over tables and text.arXiv preprint
arXiv:2010.10439.
Rajarshi Das, Shehzaad Dhuliawala, Manzil Zaheer,
and Andrew McCallum. 2019. Multi-step retriever-
reader interaction for scalable open-domain question
answering.arXiv preprint arXiv:1905.05733.
Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasu-
pat, and Mingwei Chang. 2020. Retrieval augmented
language model pre-training. InInternational confer-
ence on machine learning, pages 3929–3938. PMLR.
Linmei Hu, Zeyi Liu, Ziwang Zhao, Lei Hou, Liqiang
Nie, and Juanzi Li. 2023. A survey of knowl-
edge enhanced pre-trained language models.IEEE
Transactions on Knowledge and Data Engineering,
36(4):1413–1430.
Gautier Izacard and Edouard Grave. 2021. Leveraging
passage retrieval with generative models for open do-
main question answering. InProceedings of the 16th
conference of the european chapter of the association
for computational linguistics: main volume, pages
874–880.
Alon Jacovi and Yoav Goldberg. 2020. Towards faith-
fully interpretable nlp systems: How should we de-
fine and evaluate faithfulness?
Shaoxiong Ji, Shirui Pan, Erik Cambria, Pekka Martti-
nen, and Philip S Yu. 2021. A survey on knowledge
graphs: Representation, acquisition, and applications.
IEEE transactions on neural networks and learning
systems, 33(2):494–514.
8

## Page 9

Jinhao Jiang, Kun Zhou, Zican Dong, Keming Ye,
Wayne Xin Zhao, and Ji-Rong Wen. 2023. Struct-
gpt: A general framework for large language model
to reason over structured data.arXiv preprint
arXiv:2305.09645.
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio
Petroni, Vladimir Karpukhin, Naman Goyal, Hein-
rich Küttler, Mike Lewis, Wen-tau Yih, Tim Rock-
täschel, and 1 others. 2020. Retrieval-augmented gen-
eration for knowledge-intensive nlp tasks.Advances
in neural information processing systems, 33:9459–
9474.
Maximilian Nickel, Kevin Murphy, V olker Tresp, and
Evgeniy Gabrilovich. 2015. A review of relational
machine learning for knowledge graphs.Proceedings
of the IEEE, 104(1):11–33.
Shirui Pan, Linhao Luo, Yufei Wang, Chen Chen, Ji-
apu Wang, and Xindong Wu. 2024. Unifying large
language models and knowledge graphs: A roadmap.
IEEE Transactions on Knowledge and Data Engi-
neering, 36(7):3580–3599.
Fabio Petroni, Aleksandra Piktus, Angela Fan, Patrick
Lewis, Majid Yazdani, Nicola De Cao, James Thorne,
Yacine Jernite, Vladimir Karpukhin, Jean Maillard,
and 1 others. 2021. Kilt: a benchmark for knowledge
intensive language tasks. InProceedings of the 2021
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, pages 2523–2544.
Yu Sun, Shuohuan Wang, Yukun Li, Shikun Feng, Xuyi
Chen, Han Zhang, Xin Tian, Danxiang Zhu, Hao
Tian, and Hua Wu. 2019. Ernie: Enhanced represen-
tation through knowledge integration.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou,
and 1 others. 2022. Chain-of-thought prompting elic-
its reasoning in large language models.Advances
in neural information processing systems, 35:24824–
24837.
Siheng Xiong, Ali Payani, Ramana Kompella, and Fara-
marz Fekri. 2024a. Large language models can learn
temporal reasoning. InProceedings of the 62nd An-
nual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 10452–
10470.
Siheng Xiong, Ali Payani, Yuan Yang, and Faramarz
Fekri. 2025. Deliberate reasoning in language mod-
els as structure-aware planning with an accurate
world model. InProceedings of the 63rd Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 31900–
31931.
Siheng Xiong, Yuan Yang, Faramarz Fekri, and
James Clayton Kerce. Tilp: Differentiable learning
of temporal logical rules on knowledge graphs. In
The Eleventh International Conference on Learning
Representations.
Siheng Xiong, Yuan Yang, Ali Payani, James C Kerce,
and Faramarz Fekri. 2024b. Teilp: Time prediction
over knowledge graphs via logical reasoning. In
Proceedings of the AAAI conference on artificial in-
telligence, volume 38, pages 16112–16119.
Yuan Yang, Siheng Xiong, Ali Payani, Ehsan Shareghi,
and Faramarz Fekri. 2024a. Can llms reason in the
wild with programs? InFindings of the Association
for Computational Linguistics: EMNLP 2024, pages
9806–9829.
Yuan Yang, Siheng Xiong, Ali Payani, Ehsan Shareghi,
and Faramarz Fekri. 2024b. Harnessing the power of
large language models for natural language to first-
order logic translation. InProceedings of the 62nd
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 6942–
6959.
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran,
Tom Griffiths, Yuan Cao, and Karthik Narasimhan.
2023. Tree of thoughts: Deliberate problem solving
with large language models.Advances in neural
information processing systems, 36:11809–11822.
Xuchen Yao and Benjamin Van Durme. 2014. Infor-
mation extraction over structured data: Question an-
swering with freebase. InProceedings of the 52nd
annual meeting of the association for computational
linguistics (volume 1: long papers), pages 956–966.
Xikun Zhang, Antoine Bosselut, Michihiro Yasunaga,
Hongyu Ren, Percy Liang, Christopher D Manning,
and Jure Leskovec. 2022. Greaselm: Graph reason-
ing enhanced language models for question answer-
ing.arXiv preprint arXiv:2201.08860.
Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei,
Nathan Scales, Xuezhi Wang, Dale Schuurmans,
Claire Cui, Olivier Bousquet, Quoc Le, and 1 oth-
ers. 2022. Least-to-most prompting enables complex
reasoning in large language models.arXiv preprint
arXiv:2205.10625.
9
