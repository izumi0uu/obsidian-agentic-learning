# BioXArena: Benchmarking LLM Agents on Multi-Modal Biomedical Machine Learning Tasks - Extracted Text

- Source note: [[BioXArena - Benchmarking LLM Agents on Multi-Modal Biomedical Machine Learning Tasks]]
- Source PDF: `assets/BioXArena - Benchmarking LLM Agents on Multi-Modal Biomedical Machine Learning Tasks.pdf`
- Extracted: 2026-05-18
- Extractor: pypdf
- Pages: 69
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

BioXArena: Benchmarking LLM Agents on
Multi-Modal Biomedical Machine Learning Tasks
Loka Li1, Duzhen Zhang 1∗ , Xingbo Du 1, Leonard Song 1, Zixiao Wang 1
Assanali Aukenov1,Noel Thomas 1,Shakhnazar Sailaukan 1,Yonghan Yang 1
Feilong Chen2,Jiahua Dong 1,Kun Zhang 1,3,Bin Zhang 1,Le Song 1∗
1 Mohamed bin Zayed University of Artificial Intelligence
2 University of Chinese Academy of Sciences 3 Carnegie Mellon University
Abstract
Large language model (LLM) agents can now automate parts of machine-learning
model building, but biomedical benchmarks still either emphasize question answer-
ing, reasoning, and tool use, or cover only narrow slices of biomedical ML coding.
We introduce BioXArena, a biomedical machine learning (BioML) coding bench-
mark that evaluates whether agents can create task-specific model-building code for
heterogeneous, often multi-modal biomedical datasets. It contains 76 end-to-end
tasks across 9 domains: sequence, single-cell, structure, network biology, chemical
biology, perturbation dynamics, phenotype–disease, imaging, and text-integrated
tasks. Each task is curated from primary sources into a unified public capsule with
hidden labels, held-out graders, and biology-aware metrics on a common 0-to-1
scale; agents must write runnable code, train models, and submit predictions for
private test samples. BioXArena emphasizes realistic data interfaces: most tasks
combine multiple input sources, and more than half are multi-modal, spanning
tables, images, text, molecular sequences, omics matrices, and protein structures.
We evaluate 11 agent configurations, including general coding LLMs, biomedical
agents, and ML coding agents, in a shared 2-hour, single-GPU sandbox. MLEvolve
with Gemini-3.1-Pro obtains the highest average score of 0.666, followed by GPT-
5.4 with an average score of 0.636; no agent dominates across all domains. Beyond
the main leaderboard, we conduct extensive ablation studies, robustness checks,
scaling analyses, cost analyses, and failure-mode analyses to characterize how
backbones, scaffolds, budgets, and domains affect BioML coding performance. We
will release all tasks, graders, runner scripts, leaderboard results, and agent traces.
Project Homepage
 Code
 Dataset
1 Introduction
Large language model (LLM) agents are rapidly moving from passive question answering toward
active scientific work: they can inspect files, write and repair code, call tools, run experiments,
and iterate on results [1–3]. In machine learning, this shift is already measurable: agents can now
automate substantial parts of the model-building loop, from data inspection and feature engineering
to training, debugging, and iterative evaluation [ 4]. The stakes are especially high in biomedical
computing, where useful agents could help build models for molecules, cells, images, proteins,
patients, and biological text [5, 6]. Yet progress in this setting depends on the right benchmark: one
that tests not only biological knowledge, but also whether an agent can turn heterogeneous biomedical
data into a predictive model with meaningful evaluation under realistic computational constraints.
∗Corresponding authors
Preprint.
arXiv:2605.15766v1  [cs.CE]  15 May 2026

## Page 2

(a) Expert-Driven Curation
3. Unified Public Task CapsulesTrain/test data, task description, sample submission. 4. Hidden Private LabelsGround truth labels, grading function.
(b) 9 Biomedical Domains, 76 TasksSequenceSingle Cell3D StructureNetworkBiologyChemical BiologyPerturbation DynamicsPhenotype DiseaseImaging IntegratedText Integrated
(c) Evaluating11 Agent Configurations4Closed-source LLMsGPT-5.4  Gemini-3.1-Pro Claude-Opus-4.6Qwen3.6-Plus 3 Open-source LLMsGLM-5.1Gemma-4-31BDeepSeek-V3.22 Biomedical AgentsBiomniSTELLA2 ML Coding AgentsMLEvolveML-Master 2.0
(d) ExecutionSandbox Runtime2h wall-clock and 1 GPU per task, unified condaenvironmentOutputSubmission.csv→Held-out grader
(e) Metrics & AnalysisEvaluation Metrics (9 Types)Pearson / Spearman / AccuracyMacro-F1 / ROC-AUC / AUPRC  C-index / Dice / TM-scoreAnalysis OutputLeaderboard | Domain Heatmap Failure Taxonomy | Cost Analysis
1. SourcesTop Journals, Conferences&Popular databases2. ML + Biology ExpertsData filtering, selection, preprocessing, and splitting 
Figure 1:Overview of BioXArena. (a) Tasks are curated from journals, conferences, and public
databases by ML and biology experts, then packaged as unified public task capsules with hidden
private labels and graders. (b) The resulting benchmark contains 76 tasks across 9 biomedical ML
domains. (c) The evaluation covers 11 agents, grouped into closed-source general LLMs, open-source
general LLMs, biomedical agents, and ML coding agents. (d) All agents run under the same 2-hour,
single-GPU sandbox and submit a submission.csv to held-out task-specific graders. (e) Nine
evaluation metrics feed the leaderboard, domain heatmaps, failure taxonomy, and cost analysis.
Current benchmarks cover only parts of this landscape. See Table 1 for comparison. Broadly,
they fall into two groups with different deliverables. Biomedical reasoning and understanding
benchmarks ask agents to use existing knowledge, tools, databases, protocols, or models to answer
biological questions or produce analysis traces: LAB-Bench [7] emphasizes literature and database
QA, BixBench [8] focuses on computational-biology analysis questions, BioAgent Bench [9] tests
bioinformatics pipeline orchestration, BioProBench [ 10] evaluates biological-protocol reasoning,
and BiomniBench [11] scores multi-step biological analysis traces. Biomedical machine learning
(BioML) coding benchmarks instead ask agents to create a task-specific executable solution for
a new dataset, including data loading, model training, and held-out prediction: MLE-bench [ 12]
evaluates generic machine learning (ML) competition solving, AIRS-Bench [13] includes a small set
of biomedical ML tasks from research papers, and BioML-bench [14] directly studies end-to-end
biomedical ML model building. Together, they leave a clear gap: BioML-coding benchmarks remain
narrow in biomedical breadth, task count, modalities, or native formats, while reasoning/tool-use
benchmarks stop at answers, protocols, pipelines, or analysis traces without requiring agents to train
predictive models and submit held-out predictions. App. A1 provides more detailed related work.
To address this gap, BioXArena evaluates agents on complete BioML model-building tasks. As shown
in Figure 1, we start from primary biomedical sources and work with ML and biology experts to select,
clean, split, and standardize tasks into public capsules with hidden private labels. The benchmark
contains 76 tasks across 9 domains, with 8–10 tasks per domain. Its inputs span conventional multi-
modal media (tables, images, and text) and biology-specific modalities, such as DNA/RNA/protein
sequences, omics matrices, and protein 3D structures. Agents receive the task description, public
train/test data, and a sample submission file; they must write runnable code that produces predictions,
which are scored by held-out graders using biology-aware, task-specific metrics chosen for each
task’s target and output type. For every metric, a higher reported score means better performance.
Scores share a common 0-to-1 scale: Pearson/Spearman correlations are linearly normalized from
[−1,1] to [0,1] , while other metrics already in [0,1] are used directly without further normalization.
The main experiment comparison includes 11 methods. To evaluate seven strong LLMs with reported
coding ability, we build a simple shared agent framework for four closed-source models (GPT-5.4 [15],
Claude Opus 4.6 [16], Qwen3.6-Plus [17], and Gemini-3.1-Pro [18]) and three open-source models
(GLM-5.1 [19], Gemma-4-31B [20], and DeepSeek-V3.2 [21]). This framework calls the model API
for Python code, executes the code to train models and write submission files, validates outputs, and
returns errors for iterative repair. The remaining four agents are full agent frameworks: Biomni [5],
2

## Page 3

Table 1:Biomedical benchmark comparison.Most biomedical benchmarks fall into two categories:
reasoning and coding. The upper rows show biomedical reasoning tasks, while the lower rows present
BioML coding tasks involving model training and held-out sample prediction. We report biomedical
task counts, domain coverage, per-task input multi-modality (percentage and count), and data sources;
superscripts clarify non-obvious counting or subset decisions. Extended benchmark descriptions are
given in App. A1, with BioXArena’s multi-modality and multi-source input discussed in App. A2.1.
Benchmark BioML
coding #Bio. Tasks #Bio. domains Per-task
multi-modal Data sources
LAB-Bench [7]✗2,457 8 (LitQA2, FigQA, etc.) 9.2% (226/2,457) Biology papers, databases
BixBench [8]✗61 1 (computational biology / bioinformatics) 0.0% (0/61) Bioinformatics scenarios
BioAgent Bench [9]✗10 7 (RNA-seq, variant calling, etc.) 0.0% (0/10) Bioinformatics pipelines
BioProBench [10]✗556K a 17 (cell biology, bioimaging, genomics, etc.) 0.0% (0/556K) Biological protocols
BiomniBench [11]✗15 b 3 (oncology, neurodegen., cardiovascular) 100.0% (15/15) Biology papers
AIRS-Bench [13]✓5 c 1 (molecular property prediction; QM9 / ZINC) 0.0% (0/5) ML papers
MLE-bench [12]✓12 d 2 (imaging, chemical biology) 25.0% (3/12) Kaggle
BioML-bench [14]✓24 4 (drug discovery, imaging, single-cell, protein) 29.2% (7/24) Kaggle, Polaris, OpenProblems
BioXArena (ours)✓76 9 (chemical biology, single-cell, structure, etc.) 60.5% (46/76) Biology/ML papers, databases
a BioProBench evaluates procedural biological-protocol understanding, instantiated as 556,171 text instances over 26,933 protocols; no ML
model is trained. b BiomniBench is a trace-based, multi-stepanalytical-decision benchmark scored by an LLM judge across data loading,
method selection, and reasoning quality; the public preview (Biomni-DA-v0) ships 15 data-analysis tasks. c Only the 5 molecular-property
tasks of AIRS-Bench’s 20 total are counted (4 QM9 quantum-chemistry targets + 1 ZINC graph regression); the other 15 are non-biomedical
tasks. d Only 12 biomedical tasks of MLE-bench’s 75 Kaggle competitions are counted; the remaining 63 are general ML tasks.
STELLA [6], MLEvolve [22], and MLMaster-2.0 [23]. They run the BioML workflow end to end.
All runs use the same 2-hour, single-GPU sandbox. We report backbone-controlled ablations, cost
profiles, and failure analyses in dedicated sections, separating model strength, scaffold design, and
practical deployment cost under the same time and hardware budget to enable a fair comparison.
Our contributions are three-fold: (i) We curate and standardize a BioML-coding benchmark dataset
with 76 tasks across 9 biomedical domains, with most tasks combining multiple input sources and
more than half requiring multi-modal integration. This makes BioXArena closer to the heterogeneous
data interfaces used in real biomedical ML research. (ii) We build a unified benchmark framework for
task-capsule data access, sandboxed agent execution, held-out grading, biology-aware score reporting,
and leaderboard comparison across domains and agent families. (iii) We conduct a comprehensive
11-agent evaluation with domain-level, task-level, failure-mode, timing, cost, and same-backbone
analyses. The results identify current challenges in biomedical ML agents, including execution
reliability, modality handling, and scaffold/backbone trade-offs. We will release the full task data,
code, evaluation traces, and public leaderboard for reproducibility and community comparison.
2 The BioXArena Benchmark
BioXArena is organized around a simple principle: an LLM agent should solve a biomedical ML task
by writing and running code that trains a predictive model. This section gives a compact overview
of how tasks are curated, organized, packaged, scored, and released. Dataset-facing details appear
first in the appendices: task catalogue and modality audit (App. A2.1), primary sources (App. A2.2),
storage (App. A2.3), and ethics/licensing (App. A2.4). Execution and scoring details then follow in
App. A2.5, App. A2.6, and App. A2.7, keeping the main text focused on benchmark design.
Curation pipeline.As shown in Figure 1, task construction is an expert-driven curation process. A
group of BioML researchers and biology domain experts proposed tasks from established workflows
and public resources; two senior BioML scientists then reviewed the task list for practical feasibility,
scientific relevance, challenge, and ground-truth quality. For accepted tasks, we select compatible
sources, clean and split data with leakage-aware controls, define the prediction target and submission
schema, and lock hidden test labels and evaluators before any agent run formally begins.
Domain taxonomy.Biomedical ML is methodologically fragmented, so we divide BioXArena
into nine domains: sequence, single-cell, structure, network biology, chemical biology, perturbation
dynamics, phenotype–disease, imaging, and text-integrated tasks. Sequence and single-cell each
contain 10 tasks, while each of the other seven domains contains 8, keeping major BioML subfields
visible on the leaderboard. Heterogeneous input handling is central: a task is multi-source if each
instance exposes at least two input sources or channels (70/76 tasks). Multi-modal tasks span distinct
3

## Page 4

Sequence
Single Cell
3D Structure
NetworkChemicalPerturbation
Phenotype
ImagingText
#Tasks: 846G
#Tasks: 818M#Tasks: 858M
#Tasks: 8345M
#Tasks: 83.4G
#Tasks: 836G
#Tasks: 811G#Tasks: 101.8G
#Tasks: 106.1G
BioXArena9 Domains76 TasksMulti-modal: 46/76Multi-source: 70/76Storage size: 104G

		 
 
	 
		 
 
	
0
 	 
    
+&)#&
	




!%',+*&,)*')+*"
(,%
!%###
+),+,)
+-&)"
 $!#
)+,)+!&%
 %&+/'
$!%
.+
,#+!$&#
%!$&#
Figure 2:BioXArena domain, storage, and input heterogeneity. Left:domain-level composition
of the 76 tasks across nine BioML domains, with per-domain task counts and public storage footprints.
Right:per-task input-source count versus public-capsule storage size on a log10 scale; colors indicate
domains and marker shapes distinguish multi-modal from uni-modal tasks. The domain/task catalogue
and modality audit are in App. A2.1, and storage definitions are in App. A2.3 for reference.
modality families, including tables, images, text, sequences, omics matrices, and 3D structures (46/76
tasks). Thus multi-source is broader than multi-modal. Figure 2 summarizes the domain composition,
storage footprint, and input heterogeneity; the full task catalogue, terminology discussion (multi-
source vs. multi-modal), modality audit, and data-format summary are collected in App. A2.1.
Dataset statistics.Across 76 public task capsules, BioXArena occupies 104.08 GiB on disk and
draws from more than 40 primary sources. Task sizes vary widely because we keep each dataset in
its native biomedical format: molecule and network tasks are often small tables, whereas imaging,
single-cell, and structure tasks include large image volumes, matrix files, or coordinate structures.
We release the public package on Hugging Face and as a checksummed tarball; hidden labels and
evaluator scripts are released separately so future submissions can be scored without exposing answers.
Per-task statistics, source audits, and storage breakdowns are documented in App. A2.1, App. A2.2,
and App. A2.3 for reproducible inspection and downstream reuse by users.
Ethical considerations: consent, privacy, bias, and usage.We treat data ethics as part of task
construction. Tasks are derived from public, de-identified, or controlled-access resources whose
terms permit academic non-commercial benchmark use; sources that do not allow raw redistribution
are released only in a data-access-guarded form. We do not redistribute identifiable patient records,
and benchmark scores should be interpreted as agent-evaluation outcomes rather than clinical claims.
BioXArena is intended for biomedical ML-agent research, not for diagnosis, treatment selection, or
other high-stakes deployment; the full ethics and licensing statement is in App. A2.4 for details.
Task format and agent interface.Each task is a self-contained public capsule with a
description.md, sample_submission.csv, public train/test inputs, and any native-format assets
needed for modelling; hidden labels and task-specific evaluators remain separate. During evaluation,
an agent receives the task path and a fixed prompt, runs in a no-internet sandbox with the assigned
CPU/GPU budget, trains a model, and writes submission.csv. The interface follows the held-out
prediction setup of MLE-bench [ 12] and BioML-bench [ 14], adapted to BioXArena with a 2 h
wall-clock cap, bounded repair attempts, and full logging of attempts, submissions, errors, and token
usage; details are in App. A2.5 and App. A2.6 for reproducibility and trace analysis after evaluation.
Metrics and evaluator.Each task has a designated primary metric matched to its biological output:
correlation for continuous or rank-sensitive regression; accuracy, macro-F1, ROC-AUC, macro
ROC-AUC, and AUPRC for classification or rare-positive ranking; and C-index, mean Dice, or
TM-score for survival, segmentation, and structure prediction. Scores are oriented so larger is better
and reported on a common 0-to-1 scale: raw Pearson and Spearman correlations range from -1 to
4

## Page 5

(a) Mean(succ) — score on Eval-OK tasks
MLEvolve
STELLA
GPT-5.4
GLM-5.1
Claude-Opus-4.6
Gemini-3.1-Pro
Gemma-4-31B
Biomni
ML-Master-2.0
Qwen3.6-Plus
DeepSeek-V3.2
76.5 79.8 75.0 51.0 86.9 80.1 57.3 60.6 61.1
75.3 79.9 55.0 49.7 87.8 74.0 57.4 74.4 64.1
74.8 67.3 83.6 50.7 86.6 62.6 57.3 68.7 56.5
72.1 75.3 82.4 51.1 89.4 67.2 65.0 58.6 39.3
73.9 70.9 83.0 50.9 80.7 66.6 58.0 65.6 56.5
74.5 68.1 73.8 51.0 82.7 64.0 56.0 63.5 60.7
71.0 75.9 73.0 57.4 85.3 57.0 54.8 65.4 39.0
65.7 80.8 65.0 49.7 82.6 71.7 62.5 65.9 47.4
73.8 69.3 54.4 50.9 90.6 66.2 55.7 71.9 47.1
67.3 76.4 66.6 50.9 84.4 58.1 52.8 71.1 43.6
64.1 65.1 63.9 49.6 58.4 57.4 45.9 67.6 42.0
70.3
68.5
68.1
67.2
66.9
66.3
66.1
65.7
65.2
64.2
57.4
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
(b) Mean(fail=0) — failed/unsubmitted = 0
MLEvolve
GPT-5.4
STELLA
Gemini-3.1-Pro
GLM-5.1
Qwen3.6-Plus
ML-Master-2.0
Biomni
Claude-Opus-4.6
Gemma-4-31B
DeepSeek-V3.2
76.5 79.8 75.0 51.0 86.9 60.1 50.2 60.6 53.4
74.8 67.3 83.6 50.7 86.6 39.1 50.1 60.1 56.5
67.7 55.9 48.1 49.7 87.8 55.5 57.4 65.1 64.1
59.6 68.1 73.8 51.0 82.7 40.0 49.0 63.5 60.7
64.9 75.3 82.4 51.1 89.4 33.6 48.7 51.3 39.3
60.5 76.4 66.6 44.5 84.4 36.3 52.8 62.2 43.6
73.8 55.4 40.8 50.9 90.6 57.9 48.8 62.9 41.2
52.6 64.6 56.9 49.7 72.3 62.8 54.7 65.9 41.5
66.5 49.6 72.6 50.9 60.5 41.6 50.7 65.6 56.5
56.8 68.3 73.0 43.0 74.6 21.4 41.1 49.0 29.3
25.7 52.1 39.9 43.4 36.5 14.4 28.7 50.7 26.2
66.6
63.6
61.3
61.1
60.1
59.1
58.4
57.9
57.2
51.3
35.5
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
0
25
50
75
100
Cell Score (%)
(a) Mean(succ) — score on Eval-OK tasks
MLEvolve
STELLA
GPT-5.4
GLM-5.1
Claude-Opus-4.6
Gemini-3.1-Pro
Gemma-4-31B
Biomni
ML-Master-2.0
Qwen3.6-Plus
DeepSeek-V3.2
76.5 79.8 75.0 51.0 86.9 80.1 57.3 60.6 61.1
75.3 79.9 55.0 49.7 87.8 74.0 57.4 74.4 64.1
74.8 67.3 83.6 50.7 86.6 62.6 57.3 68.7 56.5
72.1 75.3 82.4 51.1 89.4 67.2 65.0 58.6 39.3
73.9 70.9 83.0 50.9 80.7 66.6 58.0 65.6 56.5
74.5 68.1 73.8 51.0 82.7 64.0 56.0 63.5 60.7
71.0 75.9 73.0 57.4 85.3 57.0 54.8 65.4 39.0
65.7 80.8 65.0 49.7 82.6 71.7 62.5 65.9 47.4
73.8 69.3 54.4 50.9 90.6 66.2 55.7 71.9 47.1
67.3 76.4 66.6 50.9 84.4 58.1 52.8 71.1 43.6
64.1 65.1 63.9 49.6 58.4 57.4 45.9 67.6 42.0
70.3
68.5
68.1
67.2
66.9
66.3
66.1
65.7
65.2
64.2
57.4
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
(b) Mean(fail=0) — failed/unsubmitted = 0
MLEvolve
GPT-5.4
STELLA
Gemini-3.1-Pro
GLM-5.1
Qwen3.6-Plus
ML-Master-2.0
Biomni
Claude-Opus-4.6
Gemma-4-31B
DeepSeek-V3.2
76.5 79.8 75.0 51.0 86.9 60.1 50.2 60.6 53.4
74.8 67.3 83.6 50.7 86.6 39.1 50.1 60.1 56.5
67.7 55.9 48.1 49.7 87.8 55.5 57.4 65.1 64.1
59.6 68.1 73.8 51.0 82.7 40.0 49.0 63.5 60.7
64.9 75.3 82.4 51.1 89.4 33.6 48.7 51.3 39.3
60.5 76.4 66.6 44.5 84.4 36.3 52.8 62.2 43.6
73.8 55.4 40.8 50.9 90.6 57.9 48.8 62.9 41.2
52.6 64.6 56.9 49.7 72.3 62.8 54.7 65.9 41.5
66.5 49.6 72.6 50.9 60.5 41.6 50.7 65.6 56.5
56.8 68.3 73.0 43.0 74.6 21.4 41.1 49.0 29.3
25.7 52.1 39.9 43.4 36.5 14.4 28.7 50.7 26.2
66.6
63.6
61.3
61.1
60.1
59.1
58.4
57.9
57.2
51.3
35.5
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
0
25
50
75
100
Cell Score (%)
(a) Mean(succ) — score on Eval-OK tasks
MLEvolve
STELLA
GPT-5.4
GLM-5.1
Claude-Opus-4.6
Gemini-3.1-Pro
Gemma-4-31B
Biomni
ML-Master-2.0
Qwen3.6-Plus
DeepSeek-V3.2
76.5 79.8 75.0 51.0 86.9 80.1 57.3 60.6 61.1
75.3 79.9 55.0 49.7 87.8 74.0 57.4 74.4 64.1
74.8 67.3 83.6 50.7 86.6 62.6 57.3 68.7 56.5
72.1 75.3 82.4 51.1 89.4 67.2 65.0 58.6 39.3
73.9 70.9 83.0 50.9 80.7 66.6 58.0 65.6 56.5
74.5 68.1 73.8 51.0 82.7 64.0 56.0 63.5 60.7
71.0 75.9 73.0 57.4 85.3 57.0 54.8 65.4 39.0
65.7 80.8 65.0 49.7 82.6 71.7 62.5 65.9 47.4
73.8 69.3 54.4 50.9 90.6 66.2 55.7 71.9 47.1
67.3 76.4 66.6 50.9 84.4 58.1 52.8 71.1 43.6
64.1 65.1 63.9 49.6 58.4 57.4 45.9 67.6 42.0
70.3
68.5
68.1
67.2
66.9
66.3
66.1
65.7
65.2
64.2
57.4
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
(b) Mean(fail=0) — failed/unsubmitted = 0
MLEvolve
GPT-5.4
STELLA
Gemini-3.1-Pro
GLM-5.1
Qwen3.6-Plus
ML-Master-2.0
Biomni
Claude-Opus-4.6
Gemma-4-31B
DeepSeek-V3.2
76.5 79.8 75.0 51.0 86.9 60.1 50.2 60.6 53.4
74.8 67.3 83.6 50.7 86.6 39.1 50.1 60.1 56.5
67.7 55.9 48.1 49.7 87.8 55.5 57.4 65.1 64.1
59.6 68.1 73.8 51.0 82.7 40.0 49.0 63.5 60.7
64.9 75.3 82.4 51.1 89.4 33.6 48.7 51.3 39.3
60.5 76.4 66.6 44.5 84.4 36.3 52.8 62.2 43.6
73.8 55.4 40.8 50.9 90.6 57.9 48.8 62.9 41.2
52.6 64.6 56.9 49.7 72.3 62.8 54.7 65.9 41.5
66.5 49.6 72.6 50.9 60.5 41.6 50.7 65.6 56.5
56.8 68.3 73.0 43.0 74.6 21.4 41.1 49.0 29.3
25.7 52.1 39.9 43.4 36.5 14.4 28.7 50.7 26.2
66.6
63.6
61.3
61.1
60.1
59.1
58.4
57.9
57.2
51.3
35.5
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
0
25
50
75
100
Cell Score (%)
(a) Avg. score on successful tasks(b) Penalized avg. score on all tasks
(c) Success and failure breakdown on all tasks
(a) Avg. score on successful tasks
MLEvolvege
STELLAcla
GPT-5.4
GLM-5.1
Claude-Opus-4.6
Gemini-3.1-Pro
Gemma-4-31B
Biomnicla
MLMaster-2.0dv4
Qwen3.6-Plus
DeepSeek-V3.2
76.5 79.8 75.0 51.0 86.9 80.1 57.3 60.6 61.1
75.3 79.9 55.0 49.7 87.8 74.0 57.4 74.4 64.1
74.8 67.3 83.6 50.7 86.6 62.6 57.3 68.7 56.5
72.1 75.3 82.4 51.1 89.4 67.2 65.0 58.6 39.3
73.9 70.9 83.0 50.9 80.7 66.6 58.0 65.6 56.5
74.5 68.1 73.8 51.0 82.7 64.0 56.0 63.5 60.7
71.0 75.9 73.0 57.4 85.3 57.0 54.8 65.4 39.0
65.7 80.8 65.0 49.7 82.6 71.7 62.5 65.9 47.4
73.8 69.3 54.4 50.9 90.6 66.2 55.7 71.9 47.1
67.3 76.4 66.6 50.9 84.4 58.1 52.8 71.1 43.6
64.1 65.1 63.9 49.6 58.4 57.4 45.9 67.6 42.0
70.3
68.5
68.1
67.2
66.9
66.3
66.1
65.7
65.2
64.2
57.4
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
(b) Penalized avg. score on all tasks
MLEvolvege
GPT-5.4
STELLAcla
Gemini-3.1-Pro
GLM-5.1
Qwen3.6-Plus
MLMaster-2.0dv4
Biomnicla
Claude-Opus-4.6
Gemma-4-31B
DeepSeek-V3.2
76.5 79.8 75.0 51.0 86.9 60.1 50.2 60.6 53.4
74.8 67.3 83.6 50.7 86.6 39.1 50.1 60.1 56.5
67.7 55.9 48.1 49.7 87.8 55.5 57.4 65.1 64.1
59.6 68.1 73.8 51.0 82.7 40.0 49.0 63.5 60.7
64.9 75.3 82.4 51.1 89.4 33.6 48.7 51.3 39.3
60.5 76.4 66.6 44.5 84.4 36.3 52.8 62.2 43.6
73.8 55.4 40.8 50.9 90.6 57.9 48.8 62.9 41.2
52.6 64.6 56.9 49.7 72.3 62.8 54.7 65.9 41.5
66.5 49.6 72.6 50.9 60.5 41.6 50.7 65.6 56.5
56.8 68.3 73.0 43.0 74.6 21.4 41.1 49.0 29.3
25.7 52.1 39.9 43.4 36.5 14.4 28.7 50.7 26.2
66.6
63.6
61.3
61.1
60.1
59.1
58.4
57.9
57.2
51.3
35.5
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
0
25
50
75
100
Cell Score (%)
(a) Avg. score on successful tasks
MLEvolvege
STELLAcla+ge
Biomnicla
MLMaster-2.0dv4
GPT-5.4
GLM-5.1
Claude-Opus-4.6
Gemini-3.1-Pro
Gemma-4-31B
Qwen3.6-Plus
DeepSeek-V3.2
76.5 79.8 75.0 51.0 86.9 80.1 57.3 60.6 61.1
75.3 79.9 55.0 49.7 87.8 74.0 57.4 74.4 64.1
65.7 80.8 65.0 49.7 82.6 71.7 62.5 65.9 47.4
73.8 69.3 54.4 50.9 90.6 66.2 55.7 71.9 47.1
74.8 67.3 83.6 50.7 86.6 62.6 57.3 68.7 56.5
72.1 75.3 82.4 51.1 89.4 67.2 65.0 58.6 39.3
73.9 70.9 83.0 50.9 80.7 66.6 58.0 65.6 56.5
74.5 68.1 73.8 51.0 82.7 64.0 56.0 63.5 60.7
71.0 75.9 73.0 57.4 85.3 57.0 54.8 65.4 39.0
67.3 76.4 66.6 50.9 84.4 58.1 52.8 71.1 43.6
64.1 65.1 63.9 49.6 58.4 57.4 45.9 67.6 42.0
70.3
68.5
65.7
65.2
68.1
67.2
66.9
66.3
66.1
64.2
57.4
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
(b) Penalized avg. score on all tasks
MLEvolvege
STELLAcla+ge
MLMaster-2.0dv4
Biomnicla
GPT-5.4
Gemini-3.1-Pro
GLM-5.1
Qwen3.6-Plus
Claude-Opus-4.6
Gemma-4-31B
DeepSeek-V3.2
76.5 79.8 75.0 51.0 86.9 60.1 50.2 60.6 53.4
67.7 55.9 48.1 49.7 87.8 55.5 57.4 65.1 64.1
73.8 55.4 40.8 50.9 90.6 57.9 48.8 62.9 41.2
52.6 64.6 56.9 49.7 72.3 62.8 54.7 65.9 41.5
74.8 67.3 83.6 50.7 86.6 39.1 50.1 60.1 56.5
59.6 68.1 73.8 51.0 82.7 40.0 49.0 63.5 60.7
64.9 75.3 82.4 51.1 89.4 33.6 48.7 51.3 39.3
60.5 76.4 66.6 44.5 84.4 36.3 52.8 62.2 43.6
66.5 49.6 72.6 50.9 60.5 41.6 50.7 65.6 56.5
56.8 68.3 73.0 43.0 74.6 21.4 41.1 49.0 29.3
25.7 52.1 39.9 43.4 36.5 14.4 28.7 50.7 26.2
66.6
61.3
58.4
57.9
63.6
61.1
60.1
59.1
57.2
51.3
35.5
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
0
25
50
75
100
Cell Score (%)
(a) Avg. score on successful tasks
MLEvolvege
STELLAcla+ge
Biomnicla
MLMaster-2.0dv4
GPT-5.4
GLM-5.1
Claude-Opus-4.6
Gemini-3.1-Pro
Gemma-4-31B
Qwen3.6-Plus
DeepSeek-V3.2
76.5 79.8 75.0 51.0 86.9 80.1 57.3 60.6 61.1
75.3 79.9 55.0 49.7 87.8 74.0 57.4 74.4 64.1
65.7 80.8 65.0 49.7 82.6 71.7 62.5 65.9 47.4
73.8 69.3 54.4 50.9 90.6 66.2 55.7 71.9 47.1
74.8 67.3 83.6 50.7 86.6 62.6 57.3 68.7 56.5
72.1 75.3 82.4 51.1 89.4 67.2 65.0 58.6 39.3
73.9 70.9 83.0 50.9 80.7 66.6 58.0 65.6 56.5
74.5 68.1 73.8 51.0 82.7 64.0 56.0 63.5 60.7
71.0 75.9 73.0 57.4 85.3 57.0 54.8 65.4 39.0
67.3 76.4 66.6 50.9 84.4 58.1 52.8 71.1 43.6
64.1 65.1 63.9 49.6 58.4 57.4 45.9 67.6 42.0
70.3
68.5
65.7
65.2
68.1
67.2
66.9
66.3
66.1
64.2
57.4
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
(b) Penalized avg. score on all tasks
MLEvolvege
STELLAcla+ge
MLMaster-2.0dv4
Biomnicla
GPT-5.4
Gemini-3.1-Pro
GLM-5.1
Qwen3.6-Plus
Claude-Opus-4.6
Gemma-4-31B
DeepSeek-V3.2
76.5 79.8 75.0 51.0 86.9 60.1 50.2 60.6 53.4
67.7 55.9 48.1 49.7 87.8 55.5 57.4 65.1 64.1
73.8 55.4 40.8 50.9 90.6 57.9 48.8 62.9 41.2
52.6 64.6 56.9 49.7 72.3 62.8 54.7 65.9 41.5
74.8 67.3 83.6 50.7 86.6 39.1 50.1 60.1 56.5
59.6 68.1 73.8 51.0 82.7 40.0 49.0 63.5 60.7
64.9 75.3 82.4 51.1 89.4 33.6 48.7 51.3 39.3
60.5 76.4 66.6 44.5 84.4 36.3 52.8 62.2 43.6
66.5 49.6 72.6 50.9 60.5 41.6 50.7 65.6 56.5
56.8 68.3 73.0 43.0 74.6 21.4 41.1 49.0 29.3
25.7 52.1 39.9 43.4 36.5 14.4 28.7 50.7 26.2
66.6
61.3
58.4
57.9
63.6
61.1
60.1
59.1
57.2
51.3
35.5
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
0
25
50
75
100
Cell Score (%)
Figure 3:Main-experiment scores and failure profile.Panel (a) averages normalized score only
over successfully evaluated tasks, by domain and overall. Panel (b) averages over all 76 tasks and
assigns each failed run with score 0 as a penalty. Panel (c) splits each agent’s 76 runs into successful
OKruns, meaning submissions that pass the task-specific evaluator and receive a valid score.
1 and are linearly mapped to 0 to 1, while metrics already in [0,1] are used directly. Degenerate
constant regression predictions make correlation undefined and receive score 0 in aggregate tables;
evaluator, grading, and metric-selection details are in App. A2.7 for the full methodological rationale.
3 Experiments and Results
The main leaderboard is organized in two tiers. We evaluate four published agent frameworks with
their full scaffolds, and use our simple agent framework to compare seven general LLM backbones
selected for strong reported coding ability, yielding 11 evaluated configurations. The published
frameworks include two biomedical reasoning agents (Biomni [5] and STELLA [6]) and two ML
coding agents (MLEvolve [22] and MLMaster-2.0 [23]). Our simple agent framework uses a code-
extract-run-repair pipeline: it obtains Python code from the LLM, runs local model training and
validation, checks the submission, and reports task-specific metrics; details are in App. A3.1.1. The
framework is paired with four closed-source general LLMs (GPT-5.4 [15], Claude Opus 4.6 [16],
Qwen3.6-Plus [17], and Gemini-3.1-Pro [18]) and three open-source general LLMs (GLM-5.1 [19],
Gemma-4-31B [20], and DeepSeek-V3.2 [21]). For the four published agent frameworks, we stay as
close as possible to the original papers while using newer same-family LLMs whenever available:
Biomnicla uses Claude Sonnet 4, STELLAcla+ge uses Claude Sonnet 4.6 for Dev/Tool-Creation and
Gemini-3.1-Pro for Manager/Critic, MLEvolvege uses Gemini-3.1-Pro, and MLMaster-2.0dv4 uses
DeepSeek-V4-Pro. In the controlled ablation study in § 3.4, all four scaffolds use DeepSeek-V3.2;
model substitution details are in App. A3.1. Figures and tables use compact subscripts for these
scaffolded rows:gedenotes Gemini-3.1-Pro,dv4denotes DeepSeek-V4-Pro,cladenotes the Claude-
family model,cla+gedenotes STELLA’s mixed configuration, anddv3denotes DeepSeek-V3.2.
Implementation details.Every task runs in the same sandbox: one NVIDIA A100 GPU, 64 GB
RAM, and a 2-hour hard wall-clock. General LLMs receive at most three code-generation attempts
5

## Page 6

Proportion of Different ML Models Runtime DecompositionProportion of Different ML Models
Figure 4:Proportion of different ML models and runtime decomposition for each agent. Left:
Each agent uses one type of ML model for one task, then we report the proportion of different
ML models used across all successfully evaluated tasks. Traditional families include boosted trees,
forests/ensembles, and linear/baseline models; neural families include MLPs, non-pretrained DNNs,
and pretrained/transformer-based large models.Middle: the same breakdown for the fixed DeepSeek-
V3.2 ablation.Right: wall-clock runtime decomposition for the nine non-search-loop agents,
with radial lengths square-root scaled. Agent/LLM time covers non-training interaction, planning,
execution, and search overhead, while model-training time is separate from them. MLEvolvege and
MLMaster-2.0dv4 are omitted from the right panel because they always run until the time limit 2h.
per task, whereas published agent frameworks keep their own retry logic, but all rows share the same
timeout, hidden evaluator, and output contract. For each agent–task pair we record submission status,
evaluator success, raw metric, normalized 0-to-1 score, runtime, token usage, and API-cost estimate.
Experiment organization.We first report the main 11-agent leaderboard in § 3.1, then examine
robustness in § 3.2, time-budget scaling in § 3.3, scaffold/backbone ablations in § 3.4, and a human
expert pilot in§ 3.5. The appendix is organized to separate three types of supporting material: App. A2
gives additional benchmark details, including task metadata, data sources, layout, curation, and
evaluators; App. A3 documents implementation details for runners, prompts, and cluster configuration;
and App. A4 reports experimental details, including per-agent and domain analyses, task-level results,
model choices, cost, failures, case studies, robustness, ablations, scaling, and the human baseline.
3.1 Main leaderboard
Figure 3 summarizes the main 11-agent-configuration leaderboard from three complementary views:
mean score on successfully evaluated tasks, penalized average over all tasks with failures scored as
zero, and success/failure breakdown. We use the penalized all-task average as the primary metric
because it rewards both modeling quality and end-to-end completion. Exact per-agent statistics, failure
definitions, domain-level analyses, and task-level extremes are reported in App. A4.1, App. A4.2, and
App. A4.4, leaving the main text to focus on cross-agent patterns and benchmark-level takeaways.
Overall leaderboard.MLEvolve with Gemini-3.1-Pro ranks first on the primary penalized metric
(66.6), combining strong submitted modeling solutions with 72/76 valid runs and only four missing
submissions. GPT-5.4 is the strongest general code agent (63.6) and the only row that submits on
all 76 tasks, while STELLA has the highest average score among successful tasks (68.5) but loses
ground because eight tasks fail evaluation. These results separate search-guided model building,
execution reliability, and conditional modeling quality: specialized BioML agents are competitive,
but strong general coding LLMs remain difficult to dominate under the same 2-hour, single-GPU
evaluation protocol across domains, where failure and score are evaluated together across all rows.
Domain patterns.Performance varies sharply across nine biomedical domains: chemical biology is
easiest on penalized average (77.5), followed by structure (64.9), single-cell (64.7), and sequence
(62.1), whereas perturbation dynamics (42.1), text-integrated tasks (46.5), and the phenotype/network
6

## Page 7

(a) Mean(succ) – Eval-OK tasks
MLEvolve
ML-Master 2.0
Biomni
STELLA
DeepSeek-V3.2
71.3 84.3 64.5 46.0 89.6 62.0 51.5 63.2 51.2
64.7 77.3 44.9 50.9 90.4 64.1 47.0 68.6 54.7
73.1 77.7 59.5 50.6 85.7 65.2 55.9 41.9 43.8
69.5 56.0 38.4 50.0 81.7 61.8 56.8 66.1 28.0
64.1 65.1 63.9 49.6 58.4 57.4 45.9 67.6 42.0
65.9
64.0
62.3
58.4
57.4
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
(b) Mean(fail=0) – all tasks
MLEvolve
ML-Master 2.0
Biomni
STELLA
DeepSeek-V3.2
64.2 75.8 64.5 46.0 89.6 54.3 45.1 55.3 38.4
58.2 77.3 33.7 50.9 90.4 40.1 41.1 60.0 34.2
73.1 62.2 52.0 50.6 53.6 65.2 48.9 31.4 27.3
62.5 44.8 24.0 37.5 61.3 46.4 56.8 49.5 14.0
25.7 52.1 39.9 43.4 36.5 14.4 28.7 50.7 26.2
59.8
54.7
52.4
44.6
35.5
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
0
25
50
75
100
Cell Score (%)
(a) Mean(succ) – Eval-OK tasks
MLEvolve
ML-Master 2.0
Biomni
STELLA
DeepSeek-V3.2
71.3 84.3 64.5 46.0 89.6 62.0 51.5 63.2 51.2
64.7 77.3 44.9 50.9 90.4 64.1 47.0 68.6 54.7
73.1 77.7 59.5 50.6 85.7 65.2 55.9 41.9 43.8
69.5 56.0 38.4 50.0 81.7 61.8 56.8 66.1 28.0
64.1 65.1 63.9 49.6 58.4 57.4 45.9 67.6 42.0
65.9
64.0
62.3
58.4
57.4
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
(b) Mean(fail=0) – all tasks
MLEvolve
ML-Master 2.0
Biomni
STELLA
DeepSeek-V3.2
64.2 75.8 64.5 46.0 89.6 54.3 45.1 55.3 38.4
58.2 77.3 33.7 50.9 90.4 40.1 41.1 60.0 34.2
73.1 62.2 52.0 50.6 53.6 65.2 48.9 31.4 27.3
62.5 44.8 24.0 37.5 61.3 46.4 56.8 49.5 14.0
25.7 52.1 39.9 43.4 36.5 14.4 28.7 50.7 26.2
59.8
54.7
52.4
44.6
35.5
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
0
25
50
75
100
Cell Score (%)
(a) Mean(succ) – Eval-OK tasks
MLEvolve
ML-Master 2.0
Biomni
STELLA
DeepSeek-V3.2
71.3 84.3 64.5 46.0 89.6 62.0 51.5 63.2 51.2
64.7 77.3 44.9 50.9 90.4 64.1 47.0 68.6 54.7
73.1 77.7 59.5 50.6 85.7 65.2 55.9 41.9 43.8
69.5 56.0 38.4 50.0 81.7 61.8 56.8 66.1 28.0
64.1 65.1 63.9 49.6 58.4 57.4 45.9 67.6 42.0
65.9
64.0
62.3
58.4
57.4
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
(b) Mean(fail=0) – all tasks
MLEvolve
ML-Master 2.0
Biomni
STELLA
DeepSeek-V3.2
64.2 75.8 64.5 46.0 89.6 54.3 45.1 55.3 38.4
58.2 77.3 33.7 50.9 90.4 40.1 41.1 60.0 34.2
73.1 62.2 52.0 50.6 53.6 65.2 48.9 31.4 27.3
62.5 44.8 24.0 37.5 61.3 46.4 56.8 49.5 14.0
25.7 52.1 39.9 43.4 36.5 14.4 28.7 50.7 26.2
59.8
54.7
52.4
44.6
35.5
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
0
25
50
75
100
Cell Score (%)
(a) Mean(succ) – Eval-OK tasks
MLEvolve
ML-Master 2.0
Biomni
STELLA
DeepSeek-V3.2
71.3 84.3 64.5 46.0 89.6 62.0 51.5 63.2 51.2
64.7 77.3 44.9 50.9 90.4 64.1 47.0 68.6 54.7
73.1 77.7 59.5 50.6 85.7 65.2 55.9 41.9 43.8
69.5 56.0 38.4 50.0 81.7 61.8 56.8 66.1 28.0
64.1 65.1 63.9 49.6 58.4 57.4 45.9 67.6 42.0
65.9
64.0
62.3
58.4
57.4
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
(b) Mean(fail=0) – all tasks
MLEvolve
ML-Master 2.0
Biomni
STELLA
DeepSeek-V3.2
64.2 75.8 64.5 46.0 89.6 54.3 45.1 55.3 38.4
58.2 77.3 33.7 50.9 90.4 40.1 41.1 60.0 34.2
73.1 62.2 52.0 50.6 53.6 65.2 48.9 31.4 27.3
62.5 44.8 24.0 37.5 61.3 46.4 56.8 49.5 14.0
25.7 52.1 39.9 43.4 36.5 14.4 28.7 50.7 26.2
59.8
54.7
52.4
44.6
35.5
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
0
25
50
75
100
Cell Score (%)
(a) Avg. score on successful tasks
(c) Success and failure breakdown on all tasks
(b) Penalized avg. score on all tasks(a) Avg. score on successful tasks
MLEvolvedv3
MLMaster-2.0dv3
Biomnidv3
STELLAdv3
DeepSeek-V3.2
71.3 84.3 64.5 46.0 89.6 62.0 51.5 63.2 51.2
64.7 77.3 44.9 50.9 90.4 64.1 47.0 68.6 54.7
73.1 77.7 59.5 50.6 85.7 65.2 55.9 41.9 43.8
69.5 56.0 38.4 50.0 81.7 61.8 56.8 66.1 28.0
64.1 65.1 63.9 49.6 58.4 57.4 45.9 67.6 42.0
65.9
64.0
62.3
58.4
57.4
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
(b) Penalized avg. score on all tasks
MLEvolvedv3
MLMaster-2.0dv3
Biomnidv3
STELLAdv3
DeepSeek-V3.2
64.2 75.8 64.5 46.0 89.6 54.3 45.1 55.3 38.4
58.2 77.3 33.7 50.9 90.4 40.1 41.1 60.0 34.2
73.1 62.2 52.0 50.6 53.6 65.2 48.9 31.4 27.3
62.5 44.8 24.0 37.5 61.3 46.4 56.8 49.5 14.0
25.7 52.1 39.9 43.4 36.5 14.4 28.7 50.7 26.2
59.8
54.7
52.4
44.6
35.5
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
0
25
50
75
100
Cell Score (%)
(a) Avg. score on successful tasks
MLEvolvedv3
MLMaster-2.0dv3
Biomnidv3
STELLAdv3
DeepSeek-V3.2
71.3 84.3 64.5 46.0 89.6 62.0 51.5 63.2 51.2
64.7 77.3 44.9 50.9 90.4 64.1 47.0 68.6 54.7
73.1 77.7 59.5 50.6 85.7 65.2 55.9 41.9 43.8
69.5 56.0 38.4 50.0 81.7 61.8 56.8 66.1 28.0
64.1 65.1 63.9 49.6 58.4 57.4 45.9 67.6 42.0
65.9
64.0
62.3
58.4
57.4
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
(b) Penalized avg. score on all tasks
MLEvolvedv3
MLMaster-2.0dv3
Biomnidv3
STELLAdv3
DeepSeek-V3.2
64.2 75.8 64.5 46.0 89.6 54.3 45.1 55.3 38.4
58.2 77.3 33.7 50.9 90.4 40.1 41.1 60.0 34.2
73.1 62.2 52.0 50.6 53.6 65.2 48.9 31.4 27.3
62.5 44.8 24.0 37.5 61.3 46.4 56.8 49.5 14.0
25.7 52.1 39.9 43.4 36.5 14.4 28.7 50.7 26.2
59.8
54.7
52.4
44.6
35.5
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text
Avg
0
25
50
75
100
Cell Score (%)
Figure 5:Fixed LLM backbone ablation study over different agent scaffolds.The layout follows
Figure 3, but every agent uses DeepSeek-V3.2 as backbone. Panel (a) averages successful-only
tasks, panel (b) averages all 76 tasks with failed tasks scored zero as a penalty, and panel (c) shows
success/failure categories. The simple agent with DeepSeek-V3.2 row is the baseline; the other rows
have Biomnidv3, STELLAdv3, MLMaster-2.0dv3, or MLEvolvedv3. Details are in App. A4.11.
domains (48.5–48.8) are hardest. No single agent leads every domain, underscoring domain-specific
strengths: MLEvolve leads sequence and single-cell, GPT-5.4 leads structure, MLMaster-2.0 leads
chemical biology, Biomni leads perturbation dynamics and imaging, STELLA leads phenotype and
text-integrated tasks, and GLM-5.1 narrowly leads network biology on the current task suite.
Failure profile.Failure analysis is secondary to the leaderboard but clarifies the main bottleneck.
TheOKsegment in Figure 3 (c) denotes runs that pass the evaluator and receive a task score. Across
the 836 agent–task runs, 111 fail evaluations: 52% produce no submission, 17% have ID/order
mismatches, 15% yield undefined correlations from constant predictions, and the rest are numerical
invalidity or format errors. Most failures therefore happen before valid model scoring, highlighting
submission handling and data-interface reliability rather than only final model quality. Full failure
catalogues, trace excerpts, and robustness diagnostics are collected in App. A4.7, App. A4.8, and
App. A4.9 for audit and follow-up debugging of future submissions under the same protocol.
Runtime and model choices.Figure 4 (right) shows that search-based agents often use most of
the 2-hour budget, whereas Gemini-3.1-Pro is the fastest general code agent and GPT-5.4 gives
the strongest short-run tradeoff. Token usage and API-cost accounting are left to App. A4.1 and
App. A4.6. Figure 4 (left) shows that successful submissions are not mostly neural: boosted trees,
forests/ensembles, linear baselines, and other classical methods make up over half of emitted model
families, while neural or pretrained encoders concentrate in imaging, sequence/text, and research-
agent runs. Thus high-scoring agents must choose practical and resource-aware BioML methods and
reliably finish the benchmark contract, not merely emit valid code for heterogeneous formats and task
regimes under a fixed time cap and hidden-label evaluator rather than public validation feedback.
3.2 Robustness analysis
Table 2:Three-run robustness.Pe-
nalized score is mean ± std; flips av-
erage all three pairwise pass/fail com-
parisons.
Agent Score Flips
GPT-5.463.7±0.16.0/76
DeepSeek-V3.237.0±4.926.7/76
The main leaderboard uses one run per agent–task pair, so
we estimate run-to-run variance from three full-task runs
of GPT-5.4 and DeepSeek-V3.2. Table 2 reports the mean
and standard deviation over the three penalized scores; the
flip column reports the mean of the three pairwise pass/fail
comparisons, and the full per-run breakdown is in App. A4.9.
GPT-5.4 is highly stable across repeated full-task trials, scor-
ing 63.6, 63.6, and 63.8 ( 63.7±0.1 ), with a pairwise flip
mean of 6.0/76. DeepSeek-V3.2 is less stable across runs, scoring 35.5, 42.5, and 33.1 (37.0±4.9 ).
7

## Page 8

Table 3:MLEvolve ge penalized domain-average score at 2 h vs. 12 h.Scores average over all tasks
in each domain, with failed runs scored as zero. The same Gemini-3.1-Pro backbone is used for 8
tasks per domain. ∆ is the absolute domain-average change in percentage points; “#up” counts tasks
whose score strictly improves at 12 h. App. A4.12 reports the per-task numbers and the log details.
Domain 2 h score 12 h score∆#up/total Largest single gain
Chemical biology 86.992.0+5.18/8 cell-painting (+23.7 pt)
Phenotype–disease 50.251.5+1.3 5/8 breast-cancer (+12.1 pt)
0 2 4 6 8 10 12
0
0.2
0.4
0.6
0.8
1
Wall-clock time (hours)
Best validation metric
(a) Chemical biology domain
bace1
cell-painting
cyp
egfr
gpcr
herg
kinase
tox21
0 2 4 6 8 10 12
0
0.2
0.4
0.6
0.8
1
Wall-clock time (hours)
Best validation metric
(b) Phenotype–disease domain
alzheimers
autism
breast-cancer
covid19
diabetes
genotype-pheno
pan-cancer
Figure 6:Per-task progress during MLEvolve ge’s 12 h search.Each line traces the best validation
metric found so far for one task during the agent’s internal search. Curves are non-decreasing because
only improvements are plotted and then carried to 12 h. Most gains arrive early; the remaining tail
corresponds to the hidden-test score improvements in Table 3. Panel (a) shows 8 chemical-biology
tasks; panel (b) shows 7 phenotype–disease tasks after one crash before the candidate generation.
Its three pairwise pass/fail flip counts are 29/76 (Run 1–2), 27/76 (Run 1–3), and 24/76 (Run 2–3),
averaging 26.7/76, with larger domain swings especially in chemical biology. The strong-agent
ranking is robust at the observed scale, whereas weaker agents can be misestimated by a single run.
3.3 Scaling analysis
BioXArena’s 2-hour wall-clock is intentionally tight, and search-based agents may improve when
given more time, especially when iterative candidate generation and repair remain active throughout.
We therefore re-ran MLEvolve with its Gemini-3.1-Pro backbone on two full domains, chemical
biology and phenotype–disease, using a 12-hour per-task budget while holding the data, prompt,
evaluator, and hardware fixed. Table 3 summarizes the penalized domain-average scores, with per-task
trajectories and logs in App. A4.12 for direct comparison with the 2-hour leaderboard results.
Figure 6 traces MLEvolve’s best-validation metric during the 12-hour search. Most gains arrive early
and then taper as the search space narrows, but the longer budget still improves chemical biology
by +5.1 pt and raises all 8 tasks. Phenotype–disease improves only +1.3 pt, suggesting that extra
search helps most when the task rewards feature engineering and hyperparameter tuning, and less
when the bottleneck is small sample size, label noise, or brittle clinical-data handling rather than
longer search alone. The curves also support the 2-hour budget used in the main leaderboard: by 2 h,
MLEvolve has already captured most of the eventual 12-hour validation gain, making the default
budget a reasonable choice for greatly balancing the evaluation signal and the computational cost.
3.4 Ablation study
We disentangle agent scaffold from backbone LLM with two complementary controlled ablations.
Figure 5 summarizes the fixed-DeepSeek-V3.2 scaffold comparison in the same three-panel format
as Figure 3, while App. A4.11 reports the per-domain scores, failure counts, costs, and emitted-model
families for the matched scaffold comparison under identical hardware, prompts, and evaluators.
8

## Page 9

Same backbone, different agent.On the same 0–100 scale, every scaffold consistently improves
over the bare DeepSeek-V3.2 code-extract loop: STELLA reaches 44.6, Biomni 52.4, MLMaster-2.0
54.7, and MLEvolve 59.8, compared with 35.5 for bare DeepSeek. The largest gains come from
reducing missing-submission failures, showing that scaffold design clearly matters when backbone
capability is held constant. Specialized scaffolds can beat a plain loop on the same backbone, but
they do not erase the advantage of a stronger general coding backbone in this benchmark setting.
Same agent, different backbone.Changing the backbone while keeping the biomedical scaffold
fixed gives large swings. STELLA rises from 44.6 with DeepSeek-V3.2 to 61.3 with its Sonnet-4.6
and Gemini-3.1-Pro configuration, while Biomni rises from 52.4 to 57.9. The larger STELLA jump
suggests that its Manager +Critic loop benefits strongly from a more capable backbone, whereas
Biomni’s tool-augmented ReAct loop is comparatively backbone-robust. Overall, scaffold and
backbone interact, but backbone choice remains a major driver of BioML coding performance.
3.5 Human expert study
0.5 0.7 0.9 1
STELLAcla+ge
MLEvolvege
Gemini
GPT-5.4
Human
0.805
0.817
0.818
0.822
0.839
Normalized score
Figure 7: Violin plots show normalized scores
on 10 tasks for the top four agents from main
experiment and human experts. Dots are indi-
vidual tasks; black bars mark the average score.
Based on the main leaderboard, we directly com-
pare the top four agent methods with two PhD-
level biomedical ML researchers on 10 benchmark
tasks randomly selected from BioXArena, span-
ning several domains and input modalities. Hu-
man participants receive the same task interface
as agents, use the same 2-hour budget, and see no
held-out labels or leaderboard scores; to focus the
comparison on human modeling decisions, they
cannot use AI agents or chatbots for method de-
sign, code generation, or debugging. We score
human submissions with the same official evalua-
tors and normalization as agent submissions. As
Figure 7 shows, the per-task distributions substan-
tially overlap. The human average is 83.9, modestly
above the best agent on this subset, GPT-5.4 at 82.2,
by 1.7 percentage points; Gemini-3.1-Pro scores
81.8, MLEvolvege scores 81.7, and STELLAcla+ge
scores 80.5. Agents match or exceed humans on
several network, phenotype, sequence, and single-
cell tasks, while human experts retain advantages
on selected chemical-biology and text-integrated
tasks. Setup details and scores are in App. A4.13.
4 Discussion and Conclusion
Limitations.Current coverage is broad but not exhaustive for rare and emerging assay settings and
workflows. BioXArena still omits or sparsely covers important biomedical data types and modalities,
such as spatial omics, whole-slide pathology, raw microscopy time series, flow cytometry, mass
spectrometry, wearable signals, longitudinal EHR, and wet-lab automation logs; its 9 domains and 76
tasks also cannot span the full BioML problem space. We also exclude very large production-scale
tasks that require multi-day training, distributed compute, or extensive data-engineering workflows.
The 2-hour budget is pragmatic: scaling results show that strong agents already obtain a useful signal
within this window, while the limit keeps repeated evaluation feasible. We therefore treat BioXArena
as a versioned, living benchmark; App. A5 expands the discussion of scope, future maintenance,
reliability and cost, contamination, ethics and consent, broader impact, and use-of-LLM disclosure.
Conclusion.We introduced BioXArena, a multi-modal BioML coding benchmark with 76 tasks
across 9 biomedical domains. Unlike biomedical reasoning benchmarks that mainly ask for answers
or analysis traces, BioXArena requires agents to write executable code, train predictive models,
and submit held-out predictions under standardized evaluation. Across 11 agent configurations,
MLEvolvege leads the primary leaderboard with a competitive self-evolving search strategy, while
specialized biomedical scaffolds remain competitive but do not uniformly dominate general coding
9

## Page 10

LLMs. The results highlight a practical challenge: robust execution, data handling, and method
selection are as important as stronger backbones across heterogeneous biomedical inputs, task formats,
and evaluation regimes. We release the task capsules, benchmark framework, evaluation protocol,
leaderboard, and full agent traces to support reproducible progress on biomedical ML coding agents.
References
[1] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and
Yuan Cao. React: Synergizing reasoning and acting in language models.arXiv preprint
arXiv:2210.03629, 2022.
[2] Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang
Ding, Kaiwen Men, Kejuan Yang, et al. Agentbench: Evaluating llms as agents.arXiv preprint
arXiv:2308.03688, 2023.
[3] Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, and Heng Ji.
Executable code actions elicit better llm agents. InForty-first International Conference on
Machine Learning, 2024.
[4] Ke Chen, Peiran Wang, Yaoning Yu, Xianyang Zhan, and Haohan Wang. Large language
model-based data science agent: A survey.arXiv preprint arXiv:2508.02744, 2025.
[5] Kexin Huang, Serena Zhang, Hanchen Wang, Yuanhao Qu, Yingzhou Lu, Yusuf Roohani,
Ryan Li, Lin Qiu, Gavin Li, Junze Zhang, et al. Biomni: A general-purpose biomedical ai
agent.biorxiv, 2025.
[6] Ruofan Jin, Zaixi Zhang, Mengdi Wang, and Le Cong. Stella: Self-evolving llm agent for
biomedical research.arXiv preprint arXiv:2507.02004, 2025.
[7] Jon M Laurent, Joseph D Janizek, Michael Ruzo, Michaela M Hinks, Michael J Hammerling,
Siddharth Narayanan, Manvitha Ponnapati, Andrew D White, and Samuel G Rodriques.
Lab-bench: Measuring capabilities of language models for biology research.arXiv preprint
arXiv:2407.10362, 2024.
[8] Ludovico Mitchener, Jon M Laurent, Alex Andonian, Benjamin Tenmann, Siddharth
Narayanan, Geemi P Wellawatte, Andrew White, Lorenzo Sani, and Samuel G Rodriques.
Bixbench: a comprehensive benchmark for llm-based agents in computational biology.arXiv
preprint arXiv:2503.00096, 2025.
[9] Dionizije Fa, Marko ˇCuljak, Bruno Pandža, and Mateo ˇCupi´c. Bioagent bench: An ai agent
evaluation suite for bioinformatics.arXiv preprint arXiv:2601.21800, 2026.
[10] Yuyang Liu, Liuzhenghao Lv, Xiancheng Zhang, Jingya Wang Li Yuan, and Yonghong Tian.
Bioprobench: Comprehensive dataset and benchmark in biological protocol understanding and
reasoning.arXiv preprint arXiv:2505.07889, 2025.
[11] Phylo Team. BiomniBench: Evaluating AI agents in biology. Phylo Blog, 2026.
URL https://phylo.bio/blog/evaluating-ai-agents-in-biology. Trace-based
evaluation framework for biology agents; preliminary release: 15 data-analysis tasks
(Biomni-DA-v0).
[12] Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays,
Giulio Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, et al. Mle-bench: Evaluating
machine learning agents on machine learning engineering.arXiv preprint arXiv:2410.07095,
2024.
[13] Alisia Lupidi, Bhavul Gauri, Thomas Simon Foster, Bassel Al Omari, Despoina Magka,
Alberto Pepe, Alexis Audran-Reiss, Muna Aghamelu, Nicolas Baldwin, Lucia Cipolina-Kun,
et al. Airs-bench: a suite of tasks for frontier ai research science agents.arXiv preprint
arXiv:2602.06855, 2026.
[14] Henry E Miller, Matthew Greenig, Benjamin Tenmann, and Bo Wang. Bioml-bench: Evalua-
tion of ai agents for end-to-end biomedical ml.bioRxiv, pages 2025–09, 2025.
10

## Page 11

[15] OpenAI. GPT-5.4.https://openai.com/index/introducing-gpt-5-4/, 2026.
[16] Anthropic. Claude Opus 4.6. https://www.anthropic.com/news/claude-opus-4-6,
2026.
[17] Alibaba Cloud. Alibaba Unveils Qwen3.6-Plus to Accelerate Agen-
tic AI Deployment. https://www.alibabacloud.com/press-room/
alibaba-unveils-qwen3-6-plus-to-accelerate-agentic, 2026.
[18] Google. Gemini 3.1 Pro: A smarter model for your most complex tasks. https:
//blog.google/innovation-and-ai/models-and-research/gemini-models/
gemini-3-1-pro/, 2026.
[19] Z.AI. GLM-5.1.https://docs.z.ai/guides/llm/glm-5.1, 2026.
[20] Google DeepMind. Gemma 4 31B model. https://huggingface.co/google/
gemma-4-31B-it, 2026.
[21] Aixin Liu, Aoxue Mei, Bangcai Lin, Bing Xue, Bingxuan Wang, Bingzheng Xu, Bochao Wu,
Bowei Zhang, Chaofan Lin, Chen Dong, et al. Deepseek-v3. 2: Pushing the frontier of open
large language models.arXiv preprint arXiv:2512.02556, 2025.
[22] InternScience Team. Mlevolve. https://internscience.github.io/MLEvolve/, 2026.
Open-source autonomous machine-learning engineering system.
[23] Xinyu Zhu, Yuzhu Cai, Zexi Liu, Bingyang Zheng, Cheng Wang, Rui Ye, Jiaao Chen, Hanrui
Wang, Wei-Chen Wang, Yuzhi Zhang, et al. Toward ultra-long-horizon agentic science:
Cognitive accumulation for machine learning engineering.arXiv preprint arXiv:2601.10402,
2026.
[24] John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ron-
neberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Žídek, Anna Potapenko, et al.
Highly accurate protein structure prediction with alphafold.nature, 596(7873):583–589, 2021.
[25] Minkyung Baek, Frank DiMaio, Ivan Anishchenko, Justas Dauparas, Sergey Ovchinnikov,
Gyu Rie Lee, Jue Wang, Qian Cong, Lisa N Kinch, R Dustin Schaeffer, et al. Accurate
prediction of protein structures and interactions using a three-track neural network.Science,
373(6557):871–876, 2021.
[26] Alexander Rives, Joshua Meier, Tom Sercu, Siddharth Goyal, Zeming Lin, Jason Liu, Demi
Guo, Myle Ott, C Lawrence Zitnick, Jerry Ma, et al. Biological structure and function emerge
from scaling unsupervised learning to 250 million protein sequences.Proceedings of the
national academy of sciences, 118(15):e2016239118, 2021.
[27] Zeming Lin, Halil Akin, Roshan Rao, Brian Hie, Zhongkai Zhu, Wenting Lu, Nikita Smetanin,
Robert Verkuil, Ori Kabeli, Yaniv Shmueli, et al. Evolutionary-scale prediction of atomic-level
protein structure with a language model.Science, 379(6637):1123–1130, 2023.
[28] Joseph L Watson, David Juergens, Nathaniel R Bennett, Brian L Trippe, Jason Yim, Helen E
Eisenach, Woody Ahern, Andrew J Borst, Robert J Ragotte, Lukas F Milles, et al. De novo
design of protein structure and function with rfdiffusion.Nature, 620(7976):1089–1100, 2023.
[29] Jun Cheng, Guido Novati, Joshua Pan, Clare Bycroft, Akvil˙e Žemgulyt˙e, Taylor Applebaum,
Alexander Pritzel, Lai Hong Wong, Michal Zielinski, Tobias Sargeant, et al. Accurate proteome-
wide missense variant effect prediction with alphamissense.Science, 381(6664):eadg7492,
2023.
[30] Žiga Avsec, Vikram Agarwal, Daniel Visentin, Joseph R Ledsam, Agnieszka Grabska-
Barwinska, Kyle R Taylor, Yannis Assael, John Jumper, Pushmeet Kohli, and David R Kelley.
Effective gene expression prediction from sequence by integrating long-range interactions.
Nature methods, 18(10):1196–1203, 2021.
11

## Page 12

[31] Christina V Theodoris, Ling Xiao, Anant Chopra, Mark D Chaffin, Zeina R Al Sayed,
Matthew C Hill, Helene Mantineo, Elizabeth M Brydon, Zexian Zeng, X Shirley Liu, et al.
Transfer learning enables predictions in network biology.Nature, 618(7965):616–624, 2023.
[32] Haotian Cui, Chloe Wang, Hassaan Maan, Kuan Pang, Fengning Luo, Nan Duan, and Bo Wang.
scgpt: toward building a foundation model for single-cell multi-omics using generative ai.
Nature methods, 21(8):1470–1480, 2024.
[33] Moritz Schaefer, Peter Peneder, Daniel Malzl, Salvo Danilo Lombardo, Mihaela Peycheva, Jake
Burton, Anna Hakobyan, Varun Sharma, Thomas Krausgruber, Celine Sin, et al. Multimodal
learning enables chat-based exploration of single-cell data.Nature Biotechnology, pages 1–11,
2025.
[34] Jinhyuk Lee, Wonjin Yoon, Sungdong Kim, Donghyeon Kim, Sunkyu Kim, Chan Ho So, and
Jaewoo Kang. Biobert: a pre-trained biomedical language representation model for biomedical
text mining.Bioinformatics, 36(4):1234–1240, 2020.
[35] Yu Gu, Robert Tinn, Hao Cheng, Michael Lucas, Naoto Usuyama, Xiaodong Liu, Tristan
Naumann, Jianfeng Gao, and Hoifung Poon. Domain-specific language model pretraining for
biomedical natural language processing.ACM Transactions on Computing for Healthcare
(HEALTH), 3(1):1–23, 2021.
[36] Richard J Chen, Tong Ding, Ming Y Lu, Drew FK Williamson, Guillaume Jaume, Andrew H
Song, Bowen Chen, Andrew Zhang, Daniel Shao, Muhammad Shaban, et al. Towards a
general-purpose foundation model for computational pathology.Nature medicine, 30(3):
850–862, 2024.
[37] Zhenqin Wu, Bharath Ramsundar, Evan N Feinberg, Joseph Gomes, Caleb Geniesse, Aneesh S
Pappu, Karl Leswing, and Vijay Pande. Moleculenet: a benchmark for molecular machine
learning.Chemical science, 9(2):513–530, 2018.
[38] Kexin Huang, Tianfan Fu, Wenhao Gao, Yue Zhao, Yusuf Roohani, Jure Leskovec, Con-
nor W Coley, Cao Xiao, Jimeng Sun, and Marinka Zitnik. Therapeutics data commons:
Machine learning datasets and tasks for drug discovery and development.arXiv preprint
arXiv:2102.09548, 2021.
[39] Malte D Luecken, Scott Gigante, Daniel B Burkhardt, Robrecht Cannoodt, Daniel C Strobl,
Nikolay S Markov, Luke Zappia, Giovanni Palla, Wesley Lewis, Daniel Dimitrov, et al.
Defining and benchmarking open problems in single-cell analysis.Nature Biotechnology, 43
(7):1035–1040, 2025.
[40] Christopher Lance, Malte D Luecken, Daniel B Burkhardt, Robrecht Cannoodt, Pia Rauten-
strauch, Anna Laddach, Aidyn Ubingazhibov, Zhi-Jie Cao, Kaiwen Deng, Sumeer Khan, et al.
Multimodal single cell data integration challenge: results and lessons learned.BioRxiv, pages
2022–04, 2022.
[41] Pascal Notin, Aaron Kollasch, Daniel Ritter, Lood Van Niekerk, Steffanie Paul, Han Spinner,
Nathan Rollins, Ada Shaw, Rose Orenbuch, Ruben Weitzman, et al. Proteingym: Large-
scale benchmarks for protein fitness prediction and design.Advances in neural information
processing systems, 36:64331–64379, 2023.
[42] Polaris consortium. Polaris: The benchmark platform for drug discovery. https://
polarishub.io, 2024.
[43] Xingbo Du, Loka Li, Duzhen Zhang, and Le Song. Memr3: Memory retrieval via reflective
reasoning for llm agents.arXiv preprint arXiv:2512.20237, 2025.
[44] Dominik Schmidt, Yuxiang Wu, and Zhengyao Jiang. Aide: Human-level performance in data
science competitions, 2024.
[45] Qian Huang, Jian V ora, Percy Liang, and Jure Leskovec. Mlagentbench: Evaluating language
agents on machine learning experimentation.arXiv preprint arXiv:2310.03302, 2023.
12

## Page 13

[46] Yihong Dong, Xue Jiang, Jiaru Qian, Tian Wang, Kechi Zhang, Zhi Jin, and Ge Li. A survey
on code generation with llm-based agents.arXiv preprint arXiv:2508.00083, 2025.
[47] GTEx Consortium. The gtex consortium atlas of genetic regulatory effects across human
tissues.Science, 369(6509):1318–1330, 2020.
[48] ENCODE Project Consortium et al. An integrated encyclopedia of dna elements in the human
genome.Nature, 489(7414):57, 2012.
[49] Katja Luck, Dae-Kyum Kim, Luke Lambourne, Kerstin Spirohn, Bridget E Begg, Wenting
Bian, Ruth Brignall, Tiziana Cafarelli, Francisco J Campos-Laborie, Benoit Charloteaux, et al.
A reference map of the human binary protein interactome.Nature, 580(7803):402–408, 2020.
[50] Christine A Orengo, Alex D Michie, Susan Jones, David T Jones, Mark B Swindells, and
Janet M Thornton. Cath–a hierarchic classification of protein domain structures.Structure, 5
(8):1093–1109, 1997.
[51] Nicole Lambert, Alex Robertson, Mohini Jangi, Sean McGeary, Phillip A Sharp, and Christo-
pher B Burge. Rna bind-n-seq: quantitative assessment of the sequence and structural binding
specificity of rna binding proteins.Molecular cell, 54(5):887–900, 2014.
[52] Robert C Spitale, Ryan A Flynn, Qiangfeng Cliff Zhang, Pete Crisalli, Byron Lee, Jong-Wha
Jung, Hannes Y Kuchelmeister, Pedro J Batista, Eduardo A Torre, Eric T Kool, et al. Structural
imprints in vivo decode rna regulatory mechanisms.Nature, 519(7544):486–490, 2015.
[53] Melissa J Landrum, Shanmuga Chitipiralla, Garth R Brown, Chao Chen, Baoshan Gu, Jennifer
Hart, Douglas Hoffman, Wonhee Jang, Kuljeet Kaur, Chunlei Liu, et al. Clinvar: improvements
to accessing data.Nucleic acids research, 48(D1):D835–D844, 2020.
[54] Andrew JC Russell, Jackson A Weir, Naeem M Nadaf, Matthew Shabet, Vipin Kumar, Sandeep
Kambhampati, Ruth Raichur, Giovanni J Marrero, Sophia Liu, Karol S Balderrama, et al.
Slide-tags enables single-nucleus barcoding for multimodal spatial genomics.Nature, 625
(7993):101–109, 2024.
[55] Marlon Stoeckius, Christoph Hafemeister, William Stephenson, Brian Houck-Loomis, Pratip K
Chattopadhyay, Harold Swerdlow, Rahul Satija, and Peter Smibert. Simultaneous epitope and
transcriptome measurement in single cells.Nature methods, 14(9):865–868, 2017.
[56] Zhen Zuo, Xuesen Cheng, Salma Ferdous, Jianming Shao, Jin Li, Yourong Bao, Jean Li,
Jiaxiong Lu, Antonio Jacobo Lopez, Juliette Wohlschlegel, et al. Single cell dual-omic atlas of
the human developing retina.Nature Communications, 15(1):6792, 2024.
[57] Andriy Kryshtafovych, Torsten Schwede, Maya Topf, Krzysztof Fidelis, and John Moult.
Critical assessment of methods of protein structure prediction (casp)—round xiv.Proteins:
Structure, Function, and Bioinformatics, 89(12):1607–1617, 2021.
[58] Helen M Berman, John Westbrook, Zukang Feng, Gary Gilliland, Talapady N Bhat, Helge
Weissig, Ilya N Shindyalov, and Philip E Bourne. The protein data bank.Nucleic acids
research, 28(1):235–242, 2000.
[59] John-Marc Chandonia, Naomi K Fox, and Steven E Brenner. Scope: manual curation and
artifact removal in the structural classification of proteins–extended database.Journal of
molecular biology, 429(3):348–355, 2017.
[60] Zhihai Liu, Yan Li, Li Han, Jie Li, Jie Liu, Zhixiong Zhao, Wei Nie, Yuchen Liu, and
Renxiao Wang. Pdb-wide collection of binding data: current status of the pdbbind database.
Bioinformatics, 31(3):405–412, 2015.
[61] Janet Piñero, Juan Manuel Ramírez-Anguita, Josep Saüch-Pitarch, Francesco Ronzano, Emilio
Centeno, Ferran Sanz, and Laura I Furlong. The disgenet knowledge platform for disease
genomics: 2019 update.Nucleic acids research, 48(D1):D845–D855, 2020.
[62] Michael Ashburner, Catherine A Ball, Judith A Blake, David Botstein, Heather Butler,
J Michael Cherry, Allan P Davis, Kara Dolinski, Selina S Dwight, Janan T Eppig, et al.
Gene ontology: tool for the unification of biology.Nature genetics, 25(1):25–29, 2000.
13

## Page 14

[63] Minoru Kanehisa, Miho Furumichi, Yoko Sato, Masayuki Kawashima, and Mari Ishiguro-
Watanabe. Kegg for taxonomy-based analysis of pathways and genomes.Nucleic acids
research, 51(D1):D587–D592, 2023.
[64] Bijay Jassal, Lisa Matthews, Guilherme Viteri, Chuqiao Gong, Pascual Lorente, Antonio
Fabregat, Konstantinos Sidiropoulos, Justin Cook, Marc Gillespie, Robin Haw, et al. The
reactome pathway knowledgebase.Nucleic acids research, 48(D1):D498–D503, 2020.
[65] Damian Szklarczyk, Rebecca Kirsch, Mikaela Koutrouli, Katerina Nastou, Farrokh Mehryary,
Radja Hachilif, Annika L Gable, Tao Fang, Nadezhda T Doncheva, Sampo Pyysalo, et al.
The string database in 2023: protein–protein association networks and functional enrichment
analyses for any sequenced genome of interest.Nucleic acids research, 51(D1):D638–D646,
2023.
[66] Madalina Giurgiu, Julian Reinhard, Barbara Brauner, Irmtraud Dunger-Kaltenbach, Gisela
Fobo, Goar Frishman, Corinna Montrone, and Andreas Ruepp. Corum: the comprehensive
resource of mammalian protein complexes—2019.Nucleic acids research, 47(D1):D559–
D563, 2019.
[67] Jing Guo, Hui Liu, and Jie Zheng. Synlethdb: synthetic lethality database toward discovery of
selective and sensitive anticancer drug targets.Nucleic acids research, 44(D1):D1011–D1017,
2016.
[68] Michael K Gilson, Tiqing Liu, Michael Baitaluk, George Nicola, Linda Hwang, and Jenny
Chong. Bindingdb in 2015: a public database for medicinal chemistry, computational chemistry
and systems pharmacology.Nucleic acids research, 44(D1):D1045–D1053, 2016.
[69] Srinivas Niranj Chandrasekaran, Jeanelle Ackerman, Eric Alix, D Michael Ando, John Arevalo,
Melissa Bennion, Nicolas Boisseau, Adriana Borowa, Justin D Boyd, Laurent Brino, et al.
Jump cell painting dataset: morphological impact of 136,000 chemical and genetic perturba-
tions.BioRxiv, pages 2023–03, 2023.
[70] Sunghwan Kim, Jie Chen, Tiejun Cheng, Asta Gindulyte, Jia He, Siqian He, Qingliang Li,
Benjamin A Shoemaker, Paul A Thiessen, Bo Yu, et al. Pubchem in 2021: new data content
and improved web interfaces.Nucleic acids research, 49(D1):D1388–D1395, 2021.
[71] David Mendez, Anna Gaulton, A Patrícia Bento, Jon Chambers, Marleen De Veij, Eloy Félix,
María Paula Magariños, Juan F Mosquera, Prudence Mutowo, Michał Nowotka, et al. Chembl:
towards direct deposition of bioassay data.Nucleic acids research, 47(D1):D930–D940, 2019.
[72] Jane F Armstrong, Elena Faccenda, Simon D Harding, Adam J Pawson, Christopher Southan,
Joanna L Sharman, Brice Campo, David R Cavanagh, Stephen PH Alexander, Anthony P
Davenport, et al. The iuphar/bps guide to pharmacology in 2020: extending immunopharma-
cology content and introducing the iuphar/mmv guide to malaria pharmacology.Nucleic acids
research, 48(D1):D1006–D1021, 2020.
[73] Ruili Huang, Menghang Xia, Srilatha Sakamuru, Jinghua Zhao, Sampada A Shahane, Matias
Attene-Ramos, Tongan Zhao, Christopher P Austin, and Anton Simeonov. Modelling the tox21
10 k chemical profiles for in vivo toxicity prediction and mechanism characterization.Nature
communications, 7(1):10425, 2016.
[74] Francesco Iorio, Theo A Knijnenburg, Daniel J Vis, Graham R Bignell, Michael P Menden,
Michael Schubert, Nanne Aben, Emanuel Gonçalves, Syd Barthorpe, Howard Lightfoot, et al.
A landscape of pharmacogenomic interactions in cancer.Cell, 166(3):740–754, 2016.
[75] Joseph M Replogle, Reuben A Saunders, Angela N Pogson, Jeffrey A Hussmann, Alexander
Lenail, Alina Guna, Lauren Mascibroda, Eric J Wagner, Karen Adelman, Gila Lithwick-
Yanai, et al. Mapping information-rich genotype-phenotype landscapes with genome-scale
perturb-seq.Cell, 185(14):2559–2575, 2022.
[76] Sanjay R Srivatsan, José L McFaline-Figueroa, Vijay Ramani, Lauren Saunders, Junyue Cao,
Jonathan Packer, Hannah A Pliner, Dana L Jackson, Riza M Daza, Lena Christiansen, et al.
Massively multiplex chemical transcriptomics at single-cell resolution.Science, 367(6473):
45–51, 2020.
14

## Page 15

[77] Eleni P Mimitou, Anthony Cheng, Antonino Montalbano, Stephanie Hao, Marlon Stoeckius,
Mateusz Legut, Timothy Roush, Alberto Herrera, Efthymia Papalexi, Zhengqing Ouyang, et al.
Multiplexed detection of proteins, transcriptomes, clonotypes and crispr perturbations in single
cells.Nature methods, 16(5):409–412, 2019.
[78] Aditya Pratapa, Amogh P Jalihal, Jeffrey N Law, Aditya Bharadwaj, and andT M Murali.
Benchmarking algorithms for gene regulatory network inference from single-cell transcrip-
tomic data.Nature methods, 17(2):147–154, 2020.
[79] Aravind Subramanian, Rajiv Narayan, Steven M Corsello, David D Peck, Ted E Natoli,
Xiaodong Lu, Joshua Gould, John F Davis, Andrew A Tubelli, Jacob K Asiedu, et al. A next
generation connectivity map: L1000 platform and the first 1,000,000 profiles.Cell, 171(6):
1437–1452, 2017.
[80] V olker Bergen, Marius Lange, Stefan Peidli, F Alexander Wolf, and Fabian J Theis. Generaliz-
ing rna velocity to transient cell states through dynamical modeling.Nature biotechnology, 38
(12):1408–1414, 2020.
[81] Sarah E Pierce, Jeffrey M Granja, and William J Greenleaf. High-throughput single-cell
chromatin accessibility crispr screens enable unbiased identification of regulatory networks in
cancer.Nature communications, 12(1):2969, 2021.
[82] Mariano I Gabitto, Kyle J Travaglini, Victoria M Rachleff, Eitan S Kaplan, Brian Long,
Jeanelle Ariza, Yi Ding, Joseph T Mahoney, Nick Dee, Jeff Goldy, et al. Integrated multimodal
cell atlas of alzheimer’s disease.Nature neuroscience, 27(12):2366–2383, 2024.
[83] Adriana Di Martino, Chao-Gan Yan, Qingyang Li, Erin Denio, Francisco X Castellanos, Kaat
Alaerts, Jeffrey S Anderson, Michal Assaf, Susan Y Bookheimer, Mirella Dapretto, et al. The
autism brain imaging data exchange: towards a large-scale evaluation of the intrinsic brain
architecture in autism.Molecular psychiatry, 19(6):659–667, 2014.
[84] Christina Curtis, Sohrab P Shah, Suet-Feung Chin, Gulisa Turashvili, Oscar M Rueda, Mark J
Dunning, Doug Speed, Andy G Lynch, Shamith Samarajiwa, Yinyin Yuan, et al. The genomic
and transcriptomic architecture of 2,000 breast tumours reveals novel subgroups.Nature, 486
(7403):346–352, 2012.
[85] CZI Cell Science Program, Shibla Abdulla, Brian Aevermann, Pedro Assis, Seve Badajoz,
Sidney M Bell, Emanuele Bezzi, Batuhan Cakir, Jim Chaffer, Signe Chambers, et al. Cz
cellxgene discover: a single-cell data platform for scalable exploration, analysis and modeling
of aggregated data.Nucleic acids research, 53(D1):D886–D900, 2025.
[86] Beata Strack, Jonathan P DeShazo, Chris Gennings, Juan L Olmo, Sebastian Ventura,
Krzysztof J Cios, and John N Clore. Impact of hba1c measurement on hospital readmis-
sion rates: analysis of 70,000 clinical database patient records.BioMed research international,
2014(1):781670, 2014.
[87] Seyhan Yazar, Jose Alquicira-Hernandez, Kristof Wing, Anne Senabouth, M Grace Gordon,
Stacey Andersen, Qinyi Lu, Antonia Rowson, Thomas RP Taylor, Linda Clarke, et al. Single-
cell eqtl mapping identifies cell type–specific genetic control of autoimmune disease.Science,
376(6589):eabf3041, 2022.
[88] John N Weinstein, Eric A Collisson, Gordon B Mills, Kenna R Shaw, Brad A Ozenberger,
Kyle Ellrott, Ilya Shmulevich, Chris Sander, and Joshua M Stuart. The cancer genome atlas
pan-cancer analysis project.Nature genetics, 45(10):1113–1120, 2013.
[89] 10x Genomics. Visium spatial gene expression user guide. https://www.10xgenomics.
com/products/spatial-gene-expression, 2020.
[90] Yuanfeng Ji, Haotian Bai, Chongjian Ge, Jie Yang, Ye Zhu, Ruimao Zhang, Zhen Li, Lingyan
Zhanng, Wanling Ma, Xiang Wan, et al. Amos: A large-scale abdominal multi-organ bench-
mark for versatile medical image segmentation.Advances in neural information processing
systems, 35:36722–36732, 2022.
15

## Page 16

[91] Vebjorn Ljosa, Katherine L Sokolnicki, and Anne E Carpenter. Annotated high-throughput
microscopy image sets for validation.Nature methods, 9(7):637, 2012.
[92] Christoffer Edlund, Timothy R Jackson, Nabeel Khalid, Nicola Bevan, Timothy Dale, Andreas
Dengel, Sheraz Ahmed, Johan Trygg, and Rickard Sjögren. Livecell—a large-scale dataset for
label-free live cell segmentation.Nature methods, 18(9):1038–1045, 2021.
[93] Samuel G Armato III, Geoffrey McLennan, Luc Bidaut, Michael F McNitt-Gray, Charles R
Meyer, Anthony P Reeves, Binsheng Zhao, Denise R Aberle, Claudia I Henschke, Eric A
Hoffman, et al. The lung image database consortium (lidc) and image database resource
initiative (idri): a completed reference database of lung nodules on ct scans.Medical physics,
38(2):915–931, 2011.
[94] Donglai Wei, Zudi Lin, Daniel Franco-Barranco, Nils Wendt, Xingyu Liu, Wenjie Yin, Xin
Huang, Aarush Gupta, Won-Dong Jang, Xueying Wang, et al. Mitoem dataset: large-scale 3d
mitochondria instance segmentation from em images. InInternational Conference on Medical
Image Computing and Computer-Assisted Intervention, pages 66–76. Springer, 2020.
[95] Jevgenij Gamper, Navid Alemi Koohbanani, Ksenija Benet, Ali Khuram, and Nasir Rajpoot.
Pannuke: an open pan-cancer histology dataset for nuclei instance segmentation and classifica-
tion. InEuropean congress on digital pathology, pages 11–19. Springer, 2019.
[96] Philipp Tschandl, Cliff Rosendahl, and Harald Kittler. The ham10000 dataset, a large collection
of multi-source dermatoscopic images of common pigmented skin lesions.Scientific data, 5
(1):180161, 2018.
[97] Jiahan Li, Jiuyang Dong, Shenjin Huang, Xi Li, Junjun Jiang, Xiaopeng Fan, and Yongbing
Zhang. Virtual immunohistochemistry staining for histological images assisted by weakly-
supervised learning. InProceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pages 11259–11268, 2024.
[98] Xiaoman Zhang, Chaoyi Wu, Ziheng Zhao, Weixiong Lin, Ya Zhang, Yanfeng Wang, and
Weidi Xie. Pmc-vqa: Visual instruction tuning for medical visual question answering.arXiv
preprint arXiv:2305.10415, 2023.
[99] Yuchen Zhang, Ratish Kumar Chandrakant Jha, Soumya Bharadwaj, Vatsal Sanjaykumar
Thakkar, Adrienne Hoarfrost, and Jin Sun. A benchmark dataset for multimodal predic-
tion of enzymatic function coupling dna sequences and natural language.arXiv preprint
arXiv:2407.15888, 2024.
[100] Jungwoo Oh, Gyubok Lee, Seongsu Bae, Joon-myoung Kwon, and Edward Choi. Ecg-qa: A
comprehensive question answering dataset combined with electrocardiogram.Advances in
Neural Information Processing Systems, 36:66277–66288, 2023.
[101] Bo Liu, Li-Ming Zhan, Li Xu, Lin Ma, Yan Yang, and Xiao-Ming Wu. Slake: A semantically-
labeled knowledge-enhanced dataset for medical visual question answering. In2021 IEEE
18th international symposium on biomedical imaging (ISBI), pages 1650–1654. IEEE, 2021.
[102] Xingyu Lu, He Cao, Zijing Liu, Shengyuan Bai, Leqing Chen, Yuan Yao, Hai-Tao Zheng, and
Yu Li. Moleculeqa: A dataset to evaluate factual accuracy in molecular comprehension. In
Findings of the Association for Computational Linguistics: EMNLP 2024, pages 3769–3789,
2024.
[103] Xuehai He, Yichen Zhang, Luntian Mou, Eric Xing, and Pengtao Xie. Pathvqa: 30000+
questions for medical visual question answering.arXiv preprint arXiv:2003.10286, 2020.
[104] Shengchao Liu, Yanjing Li, Zhuoxinran Li, Anthony Gitter, Yutao Zhu, Jiarui Lu, Zhao Xu,
Weili Nie, Arvind Ramanathan, Chaowei Xiao, et al. A text-guided protein design framework.
Nature Machine Intelligence, 7(4):580–591, 2025.
16

## Page 17

Appendix for
“BioXArena: Benchmarking LLM Agents on Multi-Modal Biomedical
Machine Learning Tasks”
Table of Contents:
A1 Extended Related Work. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
A1.1 AI/ML for Biology. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
A1.2 Biomedical reasoning and understanding benchmarks. . . . . . . . . . . . . . . . . . . 19
A1.3 BioML and ML-coding benchmarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
A1.4 Agent methods and scaffolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
A2 Benchmark and Dataset Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
A2.1 Task Catalogue and Modality Audit. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
A2.2 Primary Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
A2.3 Dataset Size Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
A2.4 Ethics and Data Licensing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
A2.5 Task Layout and Agent Interface. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
A2.6 Data Curation, Splits, and Release Artifacts . . . . . . . . . . . . . . . . . . . . . . . . . 34
A2.7 Evaluator and Score Reporting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
A3 Implementation Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
A3.1 Agent Runner Implementations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
A3.1.1 General LLM code agent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
A3.1.2 Biomni . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
A3.1.3 STELLA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
A3.1.4 MLMaster-2.0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
A3.1.5 MLEvolve . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
A3.2 Unified Prompt Template . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
A3.3 Cluster Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
A4 Additional Experimental Results and Analyses. . . . . . . . . . . . . . . . . . . . . . . . . . 42
A4.1 Agent-level Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
A4.2 Domain-Level Analysis. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
A4.3 Comparison between Multi-modal and Uni-modal Tasks . . . . . . . . . . . . . . . . . 45
A4.4 Task-Level Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
A4.5 ML Model Choices Emitted by Agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
A4.6 Runtime and Cost Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
A4.7 Failure Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
A4.8 Case Studies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
A4.9 Robustness Analysis. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
17

## Page 18

A4.10 Constant-Prediction Submissions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
A4.11 Same-backbone and Same-agent Ablations . . . . . . . . . . . . . . . . . . . . . . . . . . 55
A4.12 Scaling: MLEvolve . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
A4.13 Human Expert Baseline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
A5 Discussion, Limitations, and Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
A5.1 Scope and Intended Use . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
A5.2 Limitations and Future Maintenance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
A5.3 Reliability and Operating Cost . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
A5.4 Contamination and Evaluator Integrity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
A5.5 Ethics, Privacy, and Bias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
A5.6 Broader Impact . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
A5.7 Use of LLMs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
A6 Full Task Descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
A6.1 Chemical Biology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
A6.2 Imaging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
A6.3 Network Biology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
A6.4 Perturbation Dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
A6.5 Phenotype–Disease . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
A6.6 Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
A6.7 Single Cell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
A6.8 Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
A6.9 Text-Integrated . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
A1 Extended Related Work
This section expands on § 1. We first situate BioXArena within the broader AI/ML-for-biology
literature, then follow the two-way benchmark taxonomy used in Table 1. Existing biomedical
benchmarks mainly evaluate (i) biomedical reasoning and understanding, where the deliverable is an
answer, trace, protocol, or pipeline output, or (ii) biomedical machine learning (BioML) coding, where
the deliverable is executable code that trains a model and predicts on held-out samples. The agent
landscape mirrors this split: biomedical reasoning agents emphasize tool use, literature reasoning,
and analysis orchestration, whereas ML-coding agents emphasize code generation, execution, repair,
and search over modelling programs.
A1.1 AI/ML for Biology
Modern AI/ML has become a core engine for biological discovery across molecular, cellular, struc-
tural, imaging, and text-based data. In protein science, AlphaFold2 [ 24] and RoseTTAFold [25]
changed structure prediction from a specialist modelling problem into a large-scale predictive pipeline,
while protein language models and structure-aware generative models such as ESM/ESMFold [26, 27],
RFdiffusion [28], and AlphaMissense [29] extend this paradigm to protein representation learning,
structure generation, and variant effect prediction. These advances show that biological prediction
often depends on learning from native sequence, structure, and evolutionary data rather than from flat
tabular features alone.
18

## Page 19

Similar progress has occurred in genomics, single-cell biology, and biomedical language and vision.
Enformer [30] models long-range sequence regulation, Geneformer [ 31] and scGPT [ 32] learn
transferable representations from large single-cell corpora, and CellWhisperer [ 33] links single-
cell profiles with natural-language cell-state descriptions. In biomedical text, BioBERT [ 34] and
PubMedBERT [35] demonstrate the value of domain-specific pretraining, while pathology and
medical-vision foundation models increasingly target whole-slide images and other high-dimensional
clinical data [36]. Across these areas, the central theme is that useful biomedical ML systems must
handle specialized formats, biological priors, and modality-specific preprocessing.
Benchmark and dataset ecosystems have also matured. MoleculeNet [ 37], TDC [38], OpenProb-
lems [39, 40], ProteinGym [ 41], and Polaris Hub [ 42] provide standardized tasks for molecular
properties, drug discovery, single-cell analysis, protein fitness, and related BioML problems. These
resources are essential for measuring model quality and are used by BioXArena where appropriate.
However, they usually assume that the modelling workflow has already been designed by human
researchers. They do not ask whether an LLM agent can inspect a new biomedical task, select loaders
and features, write executable training code, recover from errors, and submit held-out predictions
under a unified evaluation protocol.
BioXArena is therefore complementary to AI/ML-for-biology methods and datasets. It does not pro-
pose a new biological foundation model, a new protein predictor, or a new single-cell representation
learner. Instead, it evaluates whether agents can operationalize such modelling ideas across heteroge-
neous biomedical tasks. This distinction is important: progress in AI/ML for biology creates better
modelling building blocks, while BioXArena asks whether autonomous coding agents can assemble,
adapt, and evaluate those blocks when faced with unfamiliar data and task-specific biological metrics.
A1.2 Biomedical reasoning and understanding benchmarks
Reasoning and understanding benchmarks are valuable because they test whether an agent can read
biomedical context, retrieve relevant knowledge, select tools, and produce a scientifically plausible
answer. Their limitation for our purpose is the final deliverable: they usually stop at multiple-choice
answers, open-ended analytical answers, protocol text, tool traces, or pipeline outputs. They do not
require the agent to construct a train/test split, fit a predictive model, generate held-out predictions,
and pass a task-specific evaluator.
LAB-Bench [7] measures biology knowledge and reasoning rather than ML coding. Its 2,457
multiple-choice questions cover literature QA, protocol design, figure interpretation, sequence QA,
and database QA. The benchmark is useful for probing whether models understand biological papers,
figures, databases, and experimental protocols, and it is used by Biomni [5] and STELLA [6] as part
of their reported evaluations. However, its tasks do not ask agents to implement biomedical predictive
models or submitsubmission.csvfiles for held-out samples.
BixBench [8] evaluates computational biology analysis in a sandboxed setting. It provides 61
expert-curated bioinformatics tasks or capsules, each built around a realistic analytical scenario and
associated open-answer questions. Agents can write Python/R/bash in a Jupyter environment and may
orchestrate tools such as DESeq2, clusterProfiler, and enrichGO. The deliverable, however, is
still a numerical or categorical answer to each analysis question rather than a trained model and
held-out prediction file, so BixBench tests analytical interpretation more than end-to-end BioML
coding.
BioAgent Bench [9] is a bioinformatics pipeline orchestration benchmark. Its 10 tasks cover work-
flows such as RNA-seq, variant calling, metagenomics, comparative genomics, and single-cell
analysis. Agents chain existing tools such as DESeq2, GATK, and Salmon to produce CSV outputs,
and grading uses a rubric over steps completed, final-result completion, and result matching. This is
complementary to BioXArena: BioAgent Bench asks whether an agent can run established bioinfor-
matics pipelines, whereas BioXArena asks whether an agent can build an end-to-end ML model for
held-out biomedical prediction.
BioProBench [10] focuses on biological protocol understanding. It instantiates 556,171 text examples
from 26,933 protocols across five task families: Protocol QA, Step Ordering, Error Correction,
Protocol Generation, and Protocol Reasoning. It therefore probes procedural knowledge about
wet-lab and biological protocols, but it does not evaluate data loading, feature construction, model
training, or held-out prediction.
19

## Page 20

BiomniBench [11] is a trace-based benchmark for multi-step biology-agent data analysis. The public
preview, Biomni-DA-v0, contains 15 data-analysis tasks spanning oncology, neurodegeneration,
and cardiovascular biology. It scores agent traces with an LLM judge over dimensions such as
data loading, method selection, intermediate reasoning, and final analysis quality. This makes
BiomniBench closer to analytical decision evaluation than to BioML coding: it measures whether
an agent chooses and explains plausible analysis steps, but it does not use a hidden-label predictive
modelling leaderboard.
A1.3 BioML and ML-coding benchmarks
ML-coding benchmarks change the unit of evaluation from answering to building. An agent must
inspect files, write executable code, train a model, generate predictions, and satisfy a held-out
grader. The main gap is biomedical coverage: generic ML-coding benchmarks contain only a small
biomedical subset, while existing BioML-specific benchmarks cover fewer domains, fewer tasks, or
fewer native data formats than BioXArena.
MLE-bench [12] is the canonical benchmark for LLM ML-engineering agents. It sources 75 Kaggle
competitions and asks agents to produce competition-grade submissions under a 24-hour wall-clock in
a Docker sandbox. Grading is performed against private Kaggle leaderboards, with a headline metric
based on the fraction of competitions where an agent reaches at least a bronze-medal placement.
MLE-bench evaluates scaffolds such as AIDE, MLAgentBench, and OpenHands, and it also uses
GPT-4o-based log inspection and Dolos-style plagiarism detection. Its limitation for biomedical
evaluation is scope: only 12 of the 75 competitions are counted as biomedical in Table 1, and they do
not cover the breadth of sequence, single-cell, structure, network, perturbation, phenotype, imaging,
chemical, and text-integrated BioML tasks targeted by BioXArena.
AIRS-Bench [13] curates 20 ML research tasks from SOTA papers and Hugging Face datasets.
Agents produce Python code inside a 24-hour 1 ×H200 sandbox, and the benchmark evaluates
combinations such as One-Shot, Greedy/AIRA-dojo tree search, and ReAct/MLGym with several
frontier or open models. For our comparison, only the 5 molecular-property tasks are biomedical: 4
QM9 quantum-chemistry regression targets and 1 ZINC graph regression target. AIRS-Bench is thus
an important ML-coding benchmark, but its biomedical subset is narrow and does not include protein
structures, single-cell matrices, imaging volumes, clinical phenotypes, or text-integrated biomedical
inputs.
BioML-bench [14] is the closest prior benchmark to BioXArena. It adapts the MLE-bench idea to
biomedical ML with 24 tasks across four domains: drug discovery, biomedical imaging, protein
engineering, and single-cell omics. It uses 8–16 h task budgets, multiple replicates, and reports leader-
board percentile, mean rank, above-median rate, and any-medal rate. The evaluated agents include
Biomni, STELLA, AIDE, and MLAgentBench. BioXArena extends this direction by increasing
the task count to 76, expanding to 9 domains, including more native biomedical formats, and using
task-specific biological metrics rather than only leaderboard percentiles.
Several widely used biomedical resources provide important ML-ready tasks but are not, by them-
selves, agent benchmarks. The Therapeutics Data Commons (TDC) [ 38] collects drug-discovery
ML tasks, OpenProblems [39, 40] organizes single-cell analysis tasks, ProteinGym [41] benchmarks
protein fitness prediction, and Polaris Hub [42] curates drug-discovery datasets. BioXArena uses
such resources as primary data sources where appropriate, but wraps them into a unified agent-facing
capsule with hidden labels, controlled execution, task-specific graders, and normalized scores.
A1.4 Agent methods and scaffolds
Agent methods differ in what they optimize. General-purpose LLM code agents rely mainly on a
strong model plus a lightweight execution loop. Biomedical agents add domain tools, databases, and
literature-oriented reasoning. ML research agents add deeper search, memory, and iterative model-
program evolution [43]. Our main experiments therefore compare 11 displayed agent ×backbone
configurations under one sandbox, while related benchmarks evaluate additional scaffolds such as
AIDE [44], MLAgentBench [45], OpenHands [12], AIRA-dojo and MLGym [13], and Claude Code,
Codex CLI, and OpenCode [9].
20

## Page 21

Table A1:BioXArena domain-level statistics.Every domain is represented by 8–10 tasks; 30/76
tasks are regression (Pearson/Spearman), 28/76 are classification, and the remaining 18 span multi-
label, ranking, survival, segmentation, and structure prediction. “#MM” reports the number of
per-task multi-modaltasks (inputs spanning distinct modality families; see Table A4); 46/76 tasks are
multi-modal. The broader source-level audit in Table A4 finds that 70/76 tasks combine multiple
input sources. “Storage size” is the binary on-disk footprint of the public task capsules in that domain.
BioXArena takes up approximately 104 GiB (111.8 GB) of public-task storage.
Domain #Tasks #MM Typical data size Storage size Representative sources
Sequence 10 5 10k–2M seqs 1.8 GiB GTEx, ENCODE, ProteinGym, ClinVar
Single-cell 10 4 10k–500k cells 6.1 GiB OpenProblems, Tabula Sapiens, CITE-seq
Structure 8 6 1k–50k structures 46 GiB PDB, CATH, ProteinGym
Network-biology 8 5 10k–1M edges 18 MiB STRING, KEGG, CORUM, Reactome
Chemical-biology 8 1 2k–100k molecules 58 MiB TDC, Tox21, JUMP-CP
Perturbation-dynamics 8 4 10k–200k cells 345 MiB Replogle, Srivatsan, LINCS-L1000
Phenotype-disease 8 5 0.5k–50k samples 3.4 GiB TCGA, METABRIC, ABIDE
Imaging 8 8 1k–20k imgs/vols 36 GiB HAM10000, LIDC, AMOS, PanNuke
Text-integrated 8 8 0.5k–30k pairs 11 GiB PMC-VQA, SLAKE, PathVQA, ECG-QA
To test strong backbones without method-specific scaffolding, we build a shared code-extract-
run-repair framework for seven LLMs: GPT-5.4 [ 15], Claude Opus 4.6 [ 16], Qwen3.6-Plus [17],
Gemini-3.1-Pro [18], GLM-5.1 [19], Gemma-4-31B [20], and DeepSeek-V3.2 [21]. The framework
prompts the model to write Python, executes the script in the task sandbox, checks for required
outputs, and returns error traces for repair. This group isolates backbone coding ability and avoids
adding biomedical tool retrieval or ML-search machinery.
Biomni [5] is a general-purpose biomedical agent. Its Biomni-E1 environment contains specialized
biomedical tools, software packages, and databases, while the Biomni-A1 agent uses tool retrieval and
code-as-action execution to solve biomedical queries. Biomni is evaluated on biomedical reasoning
benchmarks such as HLE and LAB-Bench, as well as curated real-world biology tasks. It is a
natural BioXArena baseline because its tool environment covers domains such as single-cell biology,
perturbation analysis, structure, and chemical biology, although its original design is broader than
held-out ML prediction.
STELLA [6] is a multi-agent biomedical research system with Manager, Dev, Critic, and Tool
Creation agents. It combines planning, code execution, reflection, and creation of new bioinformatics
tools, and it reports gains on biomedical reasoning benchmarks such as HLE and LAB-Bench as
compute scales. In BioXArena we use the architecture specified by the STELLA paper, with a
Gemini-3.1-Pro Manager/Critic and a Claude Sonnet 4.6 Dev/ToolCreation configuration.
MLMaster-2.0 [23] is an autonomous ML-engineering agent developed for MLE-bench-style compe-
titions. It uses Hierarchical Cognitive Caching to store raw plans and terminal outputs, phase-level
summaries, and task-agnostic prior knowledge from external Kaggle experience. This design is well
suited to long-horizon model search and iterative debugging. In BioXArena, it serves as an ML
research agent rather than a biomedical tool agent, and its displayed run uses a DeepSeek-V4-Pro
backbone.
MLEvolve [22] is an ML research agent built around iterative solution generation, execution, verifi-
cation, and evolution. In our experiments it runs with the published Gemini-3.1-Pro backbone and
repeatedly proposes, tests, debugs, and combines candidate modelling programs. Compared with
biomedical reasoning agents, MLEvolve is less domain-tool-heavy but more focused on search over
executable ML solutions.
AIDE [44], MLAgentBench [45], and OpenHands [12] are prominent generic scaffolds in MLE-bench-
style evaluations. AIDE emphasizes Kaggle-specialized tree search, MLAgentBench popularized
data-science tasks as ReAct-style interactive loops, and OpenHands provides a general coding-agent
environment. AIRS-Bench additionally evaluates One-Shot, AIRA-dojo-style greedy tree search, and
MLGym/ReAct [13, 1], while BioAgent Bench evaluates practical command-line scaffolds such as
Claude Code, Codex CLI, and OpenCode [9]. These systems inform the broader agent-design space,
but BioXArena focuses its main 11-agent comparison on general LLM code agents, two biomedical
agents, and two ML research agents under one BioML evaluation protocol.
21

## Page 22

Table A2:Terminology for heterogeneous biomedical inputs.The terms overlap but answer
different questions about the task input interface.
Term What it means here Scope BioXArena examples
Multi-modal Inputs span different modality fami-
lies. Families include conventional
media (image, table, text, video,
audio) and biology-specific modal-
ities (DNA/RNA/protein sequence,
molecule, gene expression, protein
abundance, 3D structure, spatial co-
ordinates, clinical metadata).
Primary task-level term
used for Table 1 and the
main text.
Pathology image +
question text; protein
sequence + 3D struc-
ture; RNA expression
+ ADT protein abun-
dance
Multi-source An instance exposes at least two dis-
tinct information sources or channels
that a solution may need to align or
join.
Broader supporting au-
dit; sources may still be-
long to one broad modal-
ity family.
SMILES + assay meta-
data; image + meta-
data; expression +
clinical table
Multi-view Multiple views or feature sets describe
the same underlying object, often as
a modeling assumption rather than a
dataset-interface claim.
Can be multi-source, but
does not necessarily im-
ply different modality
families.
Alternative feature
views of a cell, gene,
compound, or patient
Multi-omics Multiple molecular omics layers are
measured or used together.
Narrower than multi-
modal; focused on omics
layers rather than im-
ages, text, structures, or
clinical metadata.
RNA + ATAC;
transcriptomics +
proteomics; genotype
+ expression
The broader agent literature motivates the execution loop used by BioXArena. AgentBench [ 2]
evaluates interactive LLM agents across tool-use environments, ReAct [ 1] interleaves reasoning
with actions, and CodeAct [3] casts executable code itself as the action space. Recent surveys of
coding and data-science agents [46, 4] organize this design space around planning, tool use, reflection,
memory, and multi-agent coordination. These works establish the general agentic-coding paradigm,
while BioXArena specializes it to heterogeneous biomedical ML model construction.
A2 Benchmark and Dataset Details
This section collects the dataset- and benchmark-facing details that support § 2. It covers the
task catalogue and modality audit, primary data sources, package sizes, ethics and licensing, task
layout, curation and split artifacts, and score reporting. Implementation details begin in App. A3;
experimental analyses begin in App. A4.
A2.1 Task Catalogue and Modality Audit
This section expands the dataset summary in§ 2. It first gives the domain-level and per-task catalogue,
then defines how we use multi-modal, multi-source, multi-view, and multi-omics, and then audits
these annotations and data formats for all 76 tasks. The following dataset-facing sections document
primary data sources (App. A2.2), storage (App. A2.3), and ethics and licensing (App. A2.4);
execution-facing details begin with the task interface in App. A2.5.
Table A1 gives the compact domain-level summary used in Figure 2. Table A3 then lists all 76 tasks
with their task type, metric, size, input sources, and primary data source.
The full catalogue is typeset as a long table because it spans the complete benchmark. It follows the
domain order of§2 and uses the storage accounting summarized again in App. A2.3.
22

## Page 23

Table A3:Complete task catalogue with data statistics.
“Train” and “Test” denote the number of rows / samples. “Public size” is the total on-disk size of that task’s
public/ directory: training split, public test inputs, and shared public assets such as images, matrices, structures,
FASTA files, and metadata. It excludes private held-out labels and evaluator files; description.md and
sample_submission.csv are included but negligible. Thus this column is neither train-only nor test-only.
“Data Format” lists the non-CSV assets present in the task capsule. “Source” lists the primary dataset origin with
a citation.
Task Type Metric Train Test Public
size
Data
Format
Source
Sequence (10 tasks)
gene-tissue-expression Regression Pearson 272,000 68,000 39.9M CSV ,
FASTA
GTEx v10 [47]
isoform-expression Multi-out.
reg.
Spearman 179,606 6,555 424M seqs/ GenBio/GTEx [47]
multi-tf-binding Binary AUC 38,124 9,532 15.4M CSV ENCODE [48]
protein-protein-
interaction
Binary AUC 82,744 20,686 96.5M CSV HuRI [49]
regulatory-element-
detection
Multi-class M-F1 40,000 10,000 15.4M CSV ENCODE cCRE [48]
remote-homology-
detection
Regression Spearman 80,000 20,000 114M FASTA CATH [50]
rna-protein-binding-
affinity
Regression Spearman 39,321 9,831 21.5M CSV RBNS [51]
rna-protein-binding-
signal
Regression Spearman 930,686 232,672 999M CSV ENCODE eCLIP [48]
rna-reactivity-
imputation
Multi-out.
reg.
Pearson 5,643 1,411 47.6M CSV icSHAPE [52]
variant-effect-
pathogenicity
Multi-class M-F1 24,000 6,000 31.2M CSV ClinVar [53]
Single-cell (10 tasks)
batch-integration Multi-class Accuracy 228,948 72,848 539M H5AD OpenProblems [39, 40]
cell-type-from-
expression
Multi-class Accuracy 3,252 813 24.4M H5AD SCP2167 [54]
chromatin-to-
expression
Multi-out.
reg.
Pearson 57,614 11,635 660M H5AD BMMC [40]
cite-seq-protein-
prediction
Multi-out.
reg.
Pearson 76,161 14,100 129M H5AD BMMC CITE [40, 55]
cross-modality-cell-
matching
Matching Accuracy 9,323 1,647 402M H5AD Paired sc [40]
cross-modality-cell-
type
Multi-class M-F1 128,727 32,182 1.57G CSV CITE-seq [55]
developmental-stage-
prediction
Multi-class Accuracy 68,676 12,120 1.28G H5AD Retinal dev [56]
gene-expression-
denoising
Multi-out.
reg.
M-Pears. 3,605 3,605 82.3M H5AD OpenProblems [39, 40]
label-projection Multi-class Accuracy 30,159 3,347 797M H5AD OpenProblems [39, 40]
rna-to-protein-
prediction
Multi-out.
reg.
M-Pears. 66,175 1,000 686M H5AD NeurIPS 2021 [40, 55]
Structure (8 tasks)
complex-structure-
evaluation
Regression Spearman 8,863 2,216 747M JSONL,
structs
CASP [57]
enzyme-commission-
prediction
Multi-class M-F1 17,273 1,918 7.85G PDB structs PDB [58]
protein-binding-site-
detection
Binary AUPRC 34,353 8,595 15.9G PDB structs PDB [58]
protein-fold-
classification
Multi-class Accuracy 13,085 3,174 8.30G PDB structs SCOPe [59]
protein-ligand-binding-
affinity
Regression Pearson 2,679 1,239 2.32G mmCIF PDBbind [60]
protein-protein-
interface
Regression Pearson 33,967 8,492 9.98G PDB structs PDB [58]
protein-stability-
change
Regression Spearman 258,552 66,215 56.9M CSV Thermo. meas. [41]
continued on next page
23

## Page 24

Table A3:Complete task catalogue with data statistics (continued).
Task Type Metric Train Test Public
size
Data
Format
Source
protein-structure-
prediction
Structure TM-score 1,363 341 445M PDB structs PDB [58]
Network Biology (8 tasks)
gene-disease-
association
Regression Pearson 6,001 1,499 1.13M CSV DisGeNET [61]
go-function-multi-label Multi-label M-AUC 2,806 702 1.10M CSV Gene Ontology [62]
metabolic-network-
kegg
Binary AUC 4,001 999 1.78M CSV KEGG [63]
pathway-membership-
reactome
Multi-class Accuracy 4,801 1,199 2.63M CSV Reactome [64]
ppi-prediction-string Binary AUC 7,228 1,772 4.55M CSV STRING v12 [65]
protein-complex-
corum
Multi-class Accuracy 2,103 526 691K CSV CORUM [66]
synthetic-lethality-
prediction
Binary AUC 4,801 1,199 4.16M CSV SynLethDB [67]
tf-regulatory-prediction Binary AUC 5,203 1,297 1.73M CSV ENCODE [48]
Chemical Biology (8 tasks)
bace1-binding-affinity Regression Pearson 6,487 1,622 690K CSV BindingDB [68]
cell-painting-
perturbation
Classif. Accuracy 6,087 1,522 52.2M CSV JUMP-CP [69]
cyp-inhibition-multi-
label
Multi-label M-AUC 1,476 380 158K CSV PubChem,
ChEMBL [70, 71]
egfr-binding-affinity Regression Pearson 8,691 2,127 746K CSV BindingDB,
ChEMBL [68, 71]
gpcr-binding-multi-
class
Multi-class M-F1 4,520 1,131 433K CSV IUPHAR,
ChEMBL [72, 71]
herg-binding-affinity Regression Pearson 7,689 1,886 635K CSV BindingDB,
ChEMBL [68, 71]
kinase-selectivity-
multi-label
Multi-label M-AUC 30,158 7,482 3.26M CSV ChEMBL v34 [71]
tox21-sr-are Binary AUC 4,660 1,165 225K CSV Tox21 [73]
Perturbation Dynamics (8 tasks)
cancer-drug-sensitivity Regression Spearman 203,972 35,643 26.2M CSV GDSC2 [74]
crispr-perturbation-
prediction
Multi-out.
reg.
M-Pears. 8,200 1,280 8.28M JSONL.GZ Perturb-seq [75]
drug-transcriptional-
response
Multi-out.
reg.
M-Pears. 1,252 1,008 27.6M JSONL.GZ sci-Plex3 [76]
eccite-multimodal-
perturbation
Multi-out.
reg.
M-Pears. 13,758 4,587 36.1M JSONL.GZ ECCITE-seq [77]
gene-regulatory-
network-inf.
Edge pred. AUPRC 13 14 164M JSONL.GZ BEELINE [78]
multi-timepoint-
perturbation
Multi-out.
reg.
M-Pears. 3,997 698 49.6M JSONL.GZ L1000 CMap [79]
rna-velocity-cell-
transition
Multi-out.
reg.
M-Pears. 2,594 1,102 10.8M JSONL.GZ scVelo [80]
spear-atac-perturbation Multi-out.
reg.
M-Pears. 10,216 3,406 23.2M JSONL.GZ Spear-ATAC [81]
Phenotype–Disease (8 tasks)
alzheimers-disease-
staging
Multi-class Accuracy 81,813 18,185 2.71G Parquet SEA-AD [82]
autism-diagnosis Binary AUC 907 205 262K CSV ABIDE I [83]
breast-cancer-subtype Multi-class M-F1 1,523 381 3.02M CSV METABRIC [84]
covid19-severity-
classification
Multi-class M-F1 50,000 12,500 20.0M Parquet CELLxGENE [85]
diabetes-readmission Multi-class M-F1 81,412 20,354 13.8M CSV UCI Diabetes [86]
genotype-to-phenotype Regression Pearson 7,848 1,962 6.18M CSV OneK1K [87]
pan-cancer-survival-
prediction
Survival C-index 8,761 2,191 6.45M CSV TCGA [88]
continued on next page
24

## Page 25

Table A3:Complete task catalogue with data statistics (continued).
Task Type Metric Train Test Public
size
Data
Format
Source
spatial-immune-
infiltration
Regression Pearson 12,488 3,123 655M CSV , h5ad 10x Visium [89]
Imaging (8 tasks)
amos-organ-
segmentation
Segment. Dice 288 72 12.8G NIfTI
volumes
AMOS 2022 [90]
drug-moa-prediction Multi-class M-F1 944 592 1.01G images/ BBBC021 [91]
labelfree-cell-counting Regression Spearman 3,727 1,512 1.18G images/ LIVECell [92]
lung-nodule-
malignancy
Multi-class Accuracy 637 140 146M images/ LIDC-IDRI [93]
mitochondria-counting Regression Spearman 5,596 987 3.22G images/,
masks/
MitoEM [94]
nucleus-type-
classification
Multi-class M-F1 5,179 2,722 240M images/,
masks/
PanNuke [95]
skin-lesion-diagnosis Multi-class Accuracy 8,035 1,980 2.58G images/ HAM10000 [96]
virtual-staining Regression Spearman 17,295 4,000 14.8G images/ MIST [97]
Text-integrated (8 tasks)
biomedical-figure-vqa MCQ VQA Accuracy 160,142 34,823 2.15G images/ PMC-VQA [98]
dna-enzyme-function Multi-class Accuracy 612,002 5,846 102M CSV BioTalk [99]
ecg-signal-qa Open-QA Accuracy 267,539 82,146 2.50G ptbxl/ ECG-QA [100]
gene-expression-
classif.
Binary AUC 22,646 5,662 23.7M CSV CellWhisperer [33]
medical-vqa Open VQA Accuracy 5,972 1,061 53.9M images/ SLAKE [101]
molecule-qa MCQ Accuracy 55,783 5,786 22.1M CSV MoleculeQA [102]
pathology-vqa Open VQA Accuracy 25,913 6,719 5.15G images/ PathVQA [103]
protein-function-
matching
Binary AUC 865,854 216,464 960M CSV SwissProtCLAP [104]
“Classif.” = Classification; “Segment.” = Segmentation; “M-Pears.” = Mean Pearson; “M-F1” = Macro F1; “M-AUC” = Macro
ROC-AUC; “AUC” = ROC-AUC.
Per-task multi-modal and source audit.Table A2 defines the related terms used for heterogeneous
biomedical inputs, and Table A4 applies those definitions to every task. In our count, 36 tasks are
clear multi-modal inputs and 10 borderline cases are also treated as multi-modal, yielding 46/76
multi-modal tasks; 70/76 tasks combine multiple input sources.
Table A4:Per-task input sources and multi-modal judgement.
“Input Sources” lists the distinct information sources exposed to the agent for each task, using comma-separated phrases.
“Multi-modal?” marks tasks counted as multi-modal in Table 1: the 36 clear multi-modal tasks plus 10 borderline cases are
marked with ✓, while the remaining 30 are marked with ✗. “Modalities Considered” records the modality types used for that
judgement.
Task # Input
Sources Input Sources Multi-
modal? Modalities Considered
Sequence (10 tasks)
gene-tissue-
expression
3 promoter DNA sequence, cDNA or mRNA
sequence, gene and tissue metadata
✓promoter DNA sequence;
cDNA/mRNA sequence;
metadata
isoform-expression 3 RNA transcript sequence, translated protein
sequence, transcript and genomic metadata
✓RNA sequence; protein
sequence; metadata
multi-tf-binding 4 DNA binding-region sequence, genomic
coordinate and cCRE metadata,
transcription-factor identity, cell-type context
✗DNA sequence;
genomic/TF/cell metadata
protein-protein-
interaction
2 protein A amino-acid sequence, protein B
amino-acid sequence
✗protein sequence pair
regulatory-element-
detection
2 DNA regulatory-element sequence, genomic
coordinate and cCRE metadata
✗DNA sequence; genomic
metadata
continued on next page
25

## Page 26

Table A4:Per-task input sources and multi-modal judgement (continued).
Task # Input
Sources Input Sources Multi-
modal? Modalities Considered
remote-homology-
detection
2 protein sequence for CATH chain 1, protein
sequence for CATH chain 2
✗protein sequence pair
rna-protein-binding-
affinity
3 RNA sequence, protein amino-acid sequence,
protein concentration metadata
✓RNA sequence; protein
sequence; concentration
metadata
rna-protein-binding-
signal
4 RNA window sequence, protein amino-acid
sequence, genomic peak and window
metadata, cell-line context
✓RNA sequence; protein
sequence; genomic/cell
metadata
rna-reactivity-
imputation
3 RNA nucleotide sequence, partially observed
reactivity values, observation mask and
coverage summary
✓RNA sequence; reactivity
measurement profile/mask
variant-effect-
pathogenicity
2 DNA context sequence around the variant,
variant and ClinVar genomic metadata
✗DNA sequence; variant
metadata
Single-cell (10 tasks)
batch-integration 2 single-cell gene-expression matrix,
batch/source metadata table
✗single-cell expression; batch
metadata
cell-type-from-
expression
2 single-cell gene-expression matrix,
biosample, donor, sex, and cluster metadata
table
✗single-cell expression;
sample/donor metadata
chromatin-to-
expression
3 single-cell ATAC accessibility matrix, peak
DNA sequence context, cell and row-index
metadata table
✓ATAC accessibility matrix;
DNA sequence context;
metadata
cite-seq-protein-
prediction
3 single-cell RNA count matrix, target-protein
amino-acid sequences, cell and row-index
metadata table
✓single-cell RNA counts;
protein amino-acid
sequences; metadata
cross-modality-cell-
matching
3 single-cell RNA count matrix, single-cell
ATAC accessibility matrix, candidate-index
and cell metadata
✓single-cell RNA; single-cell
ATAC
cross-modality-cell-
type
2 single-cell RNA expression features, ADT
surface-protein expression features
✓single-cell RNA; ADT
protein expression
developmental-stage-
prediction
2 retinal single-cell RNA expression matrix,
cell, region, and source-file metadata
✗single-cell RNA expression;
cell/region metadata
gene-expression-
denoising
2 noisy single-cell gene-expression count
matrix, cell row-index table
✗single-cell expression
matrix; row-index table
label-projection 2 single-cell gene-expression matrix,
batch/source metadata table
✗single-cell expression; batch
metadata
rna-to-protein-
prediction
2 single-cell RNA expression matrix, batch and
cell-index metadata table
✗single-cell RNA expression
input; batch/cell metadata
Structure (8 tasks)
complex-structure-
evaluation
3 candidate predicted 3D complex structure,
native target 3D complex structure, target,
model, and group metadata
✗3D structure pair; metadata
enzyme-commission-
prediction
3 protein amino-acid sequence, 3D protein
structure, protein identifier metadata
✓ protein sequence; 3D protein
structure; metadata
protein-binding-site-
detection
3 protein amino-acid sequence, 3D protein
structure, protein length and identifier
metadata
✓ protein sequence; 3D protein
structure; metadata
protein-fold-
classification
3 protein amino-acid sequence, 3D domain
structure, domain identifier metadata
✓protein sequence; 3D
domain structure; metadata
protein-ligand-
binding-affinity
3 protein amino-acid sequence, ligand
SMILES molecular structure, 3D
protein-ligand complex structure
✓protein sequence; ligand
SMILES; 3D complex
structure
protein-protein-
interface
4 receptor protein sequence, ligand protein
sequence, 3D protein-complex structure,
complex and length metadata
✓protein sequences; 3D
protein-complex structure;
metadata
protein-stability-
change
3 wild-type protein sequence, mutation and
variant metadata, 3D wild-type protein
structure
✓protein sequence; mutation
metadata; 3D structure
continued on next page
26

## Page 27

Table A4:Per-task input sources and multi-modal judgement (continued).
Task # Input
Sources Input Sources Multi-
modal? Modalities Considered
protein-structure-
prediction
3 protein amino-acid sequence, PDB chain and
length metadata, training 3D structure and
C-alpha coordinate files
✗ protein sequence input; PDB
chain/length metadata
Network Biology (8 tasks)
gene-disease-
association
3 gene genomic and constraint features, gene
tissue-expression profile, disease prevalence
and inheritance features
✗tabular
genomic/expression/disease
features
go-function-multi-
label
2 protein amino-acid sequence, protein and
gene identifier metadata
✗protein sequence; identifier
metadata
metabolic-network-
kegg
3 enzyme amino-acid sequence, enzyme EC
hierarchy metadata, reaction and pathway
metadata
✓protein sequence;
pathway/reaction metadata
pathway-membership-
reactome
3 protein amino-acid sequence, gene and
protein metadata, gene tissue-expression
profile
✓protein sequence;
gene-expression profile;
metadata
ppi-prediction-string 3 protein A amino-acid sequence, protein B
amino-acid sequence, STRING
graph-topology features
✓protein sequence; network
topology features
protein-complex-
corum
2 protein amino-acid sequence, protein and
gene identifier metadata
✗protein sequence; identifier
metadata
synthetic-lethality-
prediction
5 gene A product sequence, gene B product
sequence, gene-level network topology
features, gene tissue-expression profiles,
pair-level PPI and common-neighbor features
✓protein/gene-product
sequence; network topology;
expression profiles
tf-regulatory-
prediction
4 TF amino-acid sequence, target-gene
regulatory metadata, ChIP-seq peak, motif,
and distance-to-TSS features, TF and target
network-degree features
✓TF sequence; regulatory
assay/network features
Chemical Biology (8 tasks)
bace1-binding-affinity 1 SMILES molecular structure✗molecule
cell-painting-
perturbation
7 DNA-channel morphology features,
ER-channel morphology features,
RNA-channel morphology features,
AGP-channel morphology features,
Mito-channel morphology features, shape
and cross-channel morphology features, well
and plate metadata
✓multiplex imaging-derived
morphology; tabular
metadata
cyp-inhibition-multi-
label
1 SMILES molecular structure✗molecule
egfr-binding-affinity 1 SMILES molecular structure✗molecule
gpcr-binding-multi-
class
2 SMILES molecular structure, target receptor,
activity, and assay metadata
✗molecule; assay metadata
herg-binding-affinity 1 SMILES molecular structure✗molecule
kinase-selectivity-
multi-label
1 SMILES molecular structure✗molecule
tox21-sr-are 1 SMILES molecular structure✗molecule
Perturbation Dynamics (8 tasks)
cancer-drug-
sensitivity
3 cell-line and cancer-type metadata, drug
identity, target, and pathway metadata,
dose-response summary features
✗tabular
cell-line/drug/dose-response
metadata
crispr-perturbation-
prediction
4 CRISPR perturbation gene identity,
measured gene list and chunk index, baseline
expression embedding, cell-count and
combination metadata
✓expression embedding;
perturbation metadata
drug-transcriptional-
response
3 drug and dose condition, cell-line and
control-condition metadata, baseline
mean-expression vector
✓expression vector;
drug/dose/cell-line metadata
continued on next page
27

## Page 28

Table A4:Per-task input sources and multi-modal judgement (continued).
Task # Input
Sources Input Sources Multi-
modal? Modalities Considered
eccite-multimodal-
perturbation
4 sgRNA perturbation identity, baseline RNA
expression, baseline ADT protein expression,
cell state and HTO metadata
✓RNA expression; ADT
protein expression;
perturbation/cell metadata
gene-regulatory-
network-inference
3 single-cell expression matrix, pseudotime
ordering, gene and dataset metadata
✗single-cell expression;
pseudotime; metadata
multi-timepoint-
perturbation
3 drug, dose, and cell-line condition,
time-point profile metadata, baseline
expression per time point
✓expression trajectories;
time/drug/cell-line metadata
rna-velocity-cell-
transition
3 spliced RNA count vector, cell-type
annotations, UMAP coordinate embedding
✗spliced RNA counts; cell
annotations/embedding
spear-atac-
perturbation
4 sgRNA perturbation identity, baseline
chromatin-accessibility profile, cell QC and
perturbation metadata, accessibility
embeddings and feature representations
✗chromatin accessibility;
perturbation/QC metadata
Phenotype–Disease (8 tasks)
alzheimers-disease-
staging
2 single-nucleus gene-expression matrix, donor
and cell-type metadata
✗single-nucleus expression;
donor/cell metadata
autism-diagnosis 4 phenotypic and demographic features, fMRI
quality metrics, structural MRI quality
metrics, imaging-site metadata
✓phenotypic/clinical tabular;
fMRI-derived metrics;
structural-MRI-derived
metrics
breast-cancer-subtype 2 clinical and treatment features, tumor
gene-expression profile
✓clinical tabular; tumor gene
expression
covid19-severity-
classification
2 single-cell gene-expression matrix, donor
and sample metadata
✗single-cell expression;
donor/sample metadata
diabetes-readmission 5 demographic features, encounter and
utilization features, ICD diagnosis codes,
medication status features, lab-result and
diabetes-medication flags
✗EHR tabular features
genotype-to-
phenotype
3 genotype principal components,
transcriptomic context expression features,
donor, sample, sex, and target-gene metadata
✓genotype PCs;
transcriptomic context;
metadata
pan-cancer-survival-
prediction
2 clinical and survival metadata, tumor
gene-expression profile
✓clinical tabular; tumor gene
expression
spatial-immune-
infiltration
4 spot gene-expression count matrices, spatial
coordinates, H&E tissue images, spot and
sample metadata
✓spatial transcriptomics;
spatial coordinates; H&E
image; metadata
Imaging (8 tasks)
amos-organ-
segmentation
2 3D CT or MRI image volume, patient,
scanner, and modality metadata table
✓3D medical image; tabular
clinical/scanner metadata
drug-moa-prediction 2 3-channel fluorescence microscopy image,
compound and concentration metadata table
✓microscopy image; tabular
compound metadata
labelfree-cell-
counting
2 phase-contrast microscopy image, cell line,
well, plate, timepoint, and site metadata table
✓microscopy image; tabular
experimental metadata
lung-nodule-
malignancy
2 3D CT nodule slice stack, radiologist
semantic features and patient/scanner
metadata table
✓3D CT image stack; tabular
radiology/clinical metadata
mitochondria-
counting
2 electron-microscopy image patch, species
metadata table
✓electron microscopy image;
tabular species metadata
nucleus-type-
classification
2 H&E histopathology image patch, tissue type
and nuclei-count metadata table
✓histopathology image;
tabular tissue/count metadata
skin-lesion-diagnosis 2 dermoscopy image, patient and lesion
metadata table
✓dermoscopy image; tabular
patient/lesion metadata
virtual-staining 2 H&E pathology image patch, stain type,
slide, and patch-location metadata table
✓pathology image; tabular
slide/stain metadata
Text-integrated (8 tasks)
biomedical-figure-vqa 4 biomedical figure image, figure caption text,
question text, answer-choice text
✓image; natural-language
caption/question/choices
continued on next page
28

## Page 29

Table A4:Per-task input sources and multi-modal judgement (continued).
Task # Input
Sources Input Sources Multi-
modal? Modalities Considered
dna-enzyme-function 3 DNA coding sequence, enzyme/function text
description, organism classification metadata
✓DNA sequence;
natural-language functional
text; organism metadata
ecg-signal-qa 3 12-lead ECG waveform signal, question text,
question-type metadata
✓ECG waveform signal;
natural-language question
gene-expression-
classification
3 top expressed gene list and expression values,
cell/disease text description, dataset-source
metadata
✓gene-expression profile/list;
natural-language cell/disease
text
medical-vqa 2 radiology image, clinical question text✓medical image;
natural-language question
molecule-qa 3 SMILES molecular structure, question text,
answer-choice text
✓SMILES molecule;
natural-language
question/choices
pathology-vqa 2 pathology image, question text✓pathology image;
natural-language question
protein-function-
matching
2 protein amino-acid sequence, functional
annotation text description
✓protein sequence;
natural-language function
text
Data formats and modality-specific files.Table A5 summarizes the main file formats agents must
load across BioXArena. The per-task catalogue in Table A3 remains the task-level index for which
formats and modality assets appear in each public capsule.
Table A5:Data formats used by BioXArena task capsules.Formats are intentionally heterogeneous
so that agents must select appropriate biomedical data loaders rather than assuming all tasks are plain
tabular prediction problems.
Format Where it appears Loading implication
CSV Chemical biology, network biology,
and many sequence or phenotype
tasks.
Rows define samples; columns may contain
SMILES strings, sequence features, clinical
variables, graph-derived features, or identi-
fiers.
CSV + image/vol-
ume files
Imaging and text-integrated VQA
tasks.
Metadata rows link to .png, .jpg, .tif,
or 3D NIfTI .nii.gz assets that must be
loaded separately.
H5AD / AnnData Most single-cell tasks. Expression matrices are stored as AnnData
objects, often sparse, with cell barcodes
linked to CSV rows by index.
JSONL.GZ Perturbation-dynamics tasks with
high-dimensional outputs.
Each compressed JSON line stores input
context and a target response vector, requir-
ing streaming or batched parsing.
Parquet Large phenotype–disease tasks. Wide tabular or single-cell-derived features
are stored column-wise for efficient loading.
PDB / mmCIF Structure tasks. Protein 3D coordinates are stored as indi-
vidual structure files linked from metadata
tables; loaders such as biotite are useful.
A2.2 Primary Data Sources
BioXArena draws from more than 40 primary sources. This section complements the task catalogue
in App. A2.1 by mapping each source to the domain(s) where it is used and to the access basis
that supports academic non-commercial benchmark construction. Table A6 gives the complete
source-level consent, access, and usage audit. “Consent / access basis” refers to the source-side
permission model we rely on: public scientific databases and non-human molecular resources follow
database or dataset terms, whereas human-subject datasets are either de-identified public releases or
29

## Page 30

controlled-access resources whose providers manage participant consent and data-use approval. The
release-policy implications are summarized in App. A2.4.
Table A6:Source-level consent, access, and usage audit.Primary data sources used to build
BioXArena tasks. The table summarizes the access basis for academic non-commercial benchmark
construction and the release policy used in our task package.
Source Used in
BioXArena
Consent / access basis Benchmark use and redistribution
TDC [38] Chemical biology Public benchmark aggregator with
dataset-specific licenses and terms.
Used as a reference source for
academic non-commercial task
construction; redistributed files
follow the underlying dataset terms.
GTEx / GenBio-derived
GTEx [47]
Sequence Human genomics resource with
provider-managed consent and
controlled or open access tiers.
Restricted individual-level files are
data-access-guarded; derived task
tables are used only where source
terms allow academic use.
ENCODE, cCRE, and
eCLIP [48]
Sequence; network
biology
Public functional-genomics
consortium data released under
provider terms.
Processed sequence, regulatory, and
binding tasks are redistributed as
benchmark files under academic
non-commercial use.
HuRI [49] Sequence Public human protein-interaction
map; source release governs reuse.
Used for protein-interaction
prediction with processed edge
tables and no identifiable human
records.
CATH [50] Sequence;
structure
Public protein-domain classification
resource; no human-subject consent
is implicated.
Redistributed as processed
protein-family labels and
FASTA-derived task files under
source terms.
RBNS [51] Sequence Public in-vitro RNA-binding assay
data; no participant-level consent is
implicated.
Used as processed sequence-affinity
examples for academic
non-commercial benchmarking.
icSHAPE [52] Sequence Public RNA-structure profiling data;
source terms govern reuse.
Used as processed
reactivity-imputation files with
source citation and academic
non-commercial restrictions.
ClinVar [53] Sequence Public clinical-variant database with
provider-managed submissions and
terms.
We use variant annotations and
labels, not identifiable patient
records, for pathogenicity
prediction.
OpenProblems / BMMC
/ NeurIPS 2021 [39, 40]
Single-cell Public single-cell benchmark releases
with provider-managed donor consent
and dataset terms.
Processed AnnData and split files
are redistributed as task capsules
when permitted by the source
release.
SCP2167 [54] Single-cell Public single-cell portal dataset;
consent and privacy handling are
managed by the source provider.
Used as de-identified
expression-derived task files for
academic non-commercial
benchmarking.
CITE-seq / BMMC
CITE [55, 40]
Single-cell Public multi-omic single-cell data
with provider-managed terms.
Used for RNA-to-protein and
cross-modality tasks with processed
matrices and source citation.
Retinal
development [56]
Single-cell Public developmental single-cell
dataset; provider terms govern reuse.
Redistributed as processed labels
and expression features for
academic non-commercial use.
CASP [57] Structure Public protein-structure assessment
data; no human-subject consent is
implicated.
Used for structure-evaluation tasks
with released coordinates, targets,
and source citation.
PDB [58] Structure Public macromolecular-structure
archive; no participant-level consent
is implicated for benchmark use.
Protein structures and derived labels
are redistributed under PDB reuse
terms for academic benchmarking.
SCOPe [59] Structure Public protein fold-classification
database; no human-subject consent
is implicated.
Used as processed fold labels and
structure files with source citation.
continued on next page
30

## Page 31

Table A6:Source-level consent, access, and usage audit (continued).
Source Used in
BioXArena
Consent / access basis Benchmark use and redistribution
PDBbind [60] Structure Public protein-ligand binding
database with provider terms.
Used for binding-affinity tasks with
processed structures and labels
under academic non-commercial
use.
ProteinGym /
Thermodynamic
measurements [41]
Sequence;
structure
Public protein variant benchmark and
source measurements; no
participant-level consent is
implicated.
Used for stability and variant-effect
tasks with processed tables and
source citation.
DisGeNET [61] Network biology Public gene-disease association
database with database terms.
Used as processed association
tables; no raw clinical records are
redistributed.
Gene Ontology [62] Network biology Public ontology and annotation
resource; no human-subject consent
is implicated.
Used for function-label prediction
with ontology-derived labels and
citation.
KEGG [63] Network biology Public pathway database governed by
KEGG terms.
Used through processed pathway
and metabolic-network labels
consistent with academic
benchmark use.
Reactome [64] Network biology Public pathway knowledgebase with
open reuse terms.
Used as processed
pathway-membership task files with
source citation.
STRING v12 [65] Network biology Public protein-association database
with provider terms.
Used for PPI prediction with
processed edge tables under
academic non-commercial use.
CORUM [66] Network biology Public protein-complex database with
provider terms.
Used for complex-label prediction
with processed protein-complex
tables.
SynLethDB [67] Network biology Public synthetic-lethality database
with source terms.
Used as processed pairwise-label
files for academic non-commercial
benchmarking.
BindingDB [68] Chemical biology Public binding-affinity database with
database terms.
Used for compound-target affinity
tasks; redistributed as processed
SMILES and labels under source
terms.
JUMP-CP / Cell
Painting [69]
Chemical biology;
imaging
Public cell-painting perturbation data
with provider terms.
Used for morphology-based
perturbation tasks with processed
features or images where source
terms allow.
PubChem [70] Chemical biology Public chemical database; no
human-subject consent is implicated.
Used for chemical annotations and
identifiers in processed task files.
ChEMBL [71] Chemical biology Public bioactivity database with
database terms.
Used for activity and selectivity
prediction tasks with processed
compound labels.
IUPHAR [72] Chemical biology Public pharmacology database with
provider terms.
Used for GPCR target-label
construction with ChEMBL-linked
processed files.
Tox21 [73] Chemical biology Public toxicology challenge dataset;
no participant-level consent is
implicated.
Used for toxicity prediction under
academic non-commercial
benchmark restrictions.
GDSC2 [74] Perturbation
dynamics
Public cancer cell-line drug-response
resource with provider terms.
Used as processed sensitivity tables;
no identifiable patient records are
redistributed.
Perturb-seq [75] Perturbation
dynamics
Public CRISPR perturbation
single-cell release with provider
terms.
Used for perturbation-response
prediction with processed JSONL
task files.
sci-Plex3 [76] Perturbation
dynamics
Public single-cell chemical
perturbation dataset with provider
terms.
Used for drug-response prediction
through processed expression
targets.
ECCITE-seq [77] Perturbation
dynamics
Public multimodal perturbation
dataset with provider terms.
Used for multimodal perturbation
prediction with processed task files.
continued on next page
31

## Page 32

Table A6:Source-level consent, access, and usage audit (continued).
Source Used in
BioXArena
Consent / access basis Benchmark use and redistribution
BEELINE [78] Perturbation
dynamics
Public gene-regulatory-network
benchmark; no human-subject
consent is implicated.
Used as processed
network-inference inputs and hidden
labels.
LINCS-L1000 /
CMap [79]
Perturbation
dynamics
Public perturbational transcriptomics
resource with provider terms.
Used for timepoint and
transcriptional-response tasks under
academic non-commercial
benchmarking.
scVelo [80] Perturbation
dynamics
Public RNA-velocity resource and
examples with source terms.
Used for cell-transition prediction
with processed count and velocity
features.
Spear-ATAC [81] Perturbation
dynamics
Public perturbation and
chromatin-accessibility resource with
provider terms.
Used for ATAC-linked perturbation
prediction with processed matrices.
SEA-AD [82] Phenotype–
disease
Public de-identified human cohort
resource; consent and privacy review
are managed by the source provider.
Used for disease-staging tasks with
de-identified processed features and
labels.
ABIDE I [83] Phenotype–
disease
Human neuroimaging cohort with
provider-managed consent and
data-use approval.
Data-access-guarded when required;
users must obtain source-side
approval for restricted files.
METABRIC [84] Phenotype–
disease
Human cancer cohort released under
controlled data-use terms.
Data-access-guarded; public
package does not redistribute
restricted raw clinical or genomic
records.
CELLxGENE [85] Phenotype–
disease
Public de-identified single-cell
repository with dataset-specific terms.
Used as processed feature and label
files where source terms permit
academic redistribution.
UCI Diabetes [86] Phenotype–
disease
Public de-identified clinical dataset
governed by repository terms.
Used as processed readmission task
tables without identifiable patient
records.
OneK1K [87] Phenotype–
disease
Human cohort genomics resource
with provider-managed consent and
access terms.
Used only in forms permitted by
source terms; restricted files remain
data-access-guarded when required.
TCGA [88] Phenotype–
disease
Human cancer genomics resource
with open and controlled tiers;
consent and DUA approval are
provider-managed.
Controlled files are
data-access-guarded; released task
files avoid restricted raw-data
redistribution.
10x Visium [89] Phenotype–
disease
Public spatial transcriptomics
example data with provider terms.
Used for spatial immune-infiltration
tasks with processed matrices and
metadata.
AMOS 2022 [90] Imaging Public de-identified CT/MRI
benchmark; consent and privacy
handling are source-provider
responsibilities.
Used for segmentation tasks with
public imaging files under academic
non-commercial use.
BBBC021 [91] Imaging Public microscopy image set with
provider terms; no patient-level
consent is implicated.
Used for drug mechanism-of-action
prediction with source-cited image
files.
LIVECell [92] Imaging Public cell-imaging dataset with
provider terms.
Used for label-free cell-counting
tasks under academic
non-commercial benchmark
restrictions.
LIDC-IDRI [93] Imaging Human CT imaging collection with
de-identification and data-use terms
managed by the provider.
Data-access-guarded where
required; no identifiable imaging
metadata is redistributed in public
capsules.
MitoEM [94] Imaging Public electron-microscopy dataset;
no human-subject consent is
implicated for benchmark use.
Used for mitochondria-counting
tasks with released images and
masks under source terms.
PanNuke [95] Imaging Public de-identified histology dataset
with provider terms.
Used for nucleus-type classification
with public image and mask files.
continued on next page
32

## Page 33

Table A6:Source-level consent, access, and usage audit (continued).
Source Used in
BioXArena
Consent / access basis Benchmark use and redistribution
HAM10000 [96] Imaging Public de-identified dermatology
image dataset with provider-managed
consent and terms.
Used for skin-lesion diagnosis tasks;
no identifiable patient records are
redistributed.
MIST [97] Imaging Public microscopy virtual-staining
dataset with provider terms.
Used for virtual-staining regression
under academic non-commercial
benchmark restrictions.
PMC-VQA [98] Text-integrated Public figure-question dataset derived
from biomedical publications and
provider terms.
Used for figure VQA with
publication-derived images and task
labels under source terms.
BioTalk [99] Text-integrated Public biomedical text/sequence QA
resource with provider terms.
Used for DNA-enzyme function
tasks with processed prompts and
labels.
ECG-QA [100] Text-integrated Public de-identified ECG
question-answer dataset with
provider-managed privacy handling.
Used for ECG QA without
identifiable patient records and
under academic non-commercial
use.
CellWhisperer [33] Text-integrated Public expression-text alignment
resource with dataset-specific terms.
Used for expression classification
tasks with processed expression
features and labels.
SLAKE [101] Text-integrated Public de-identified medical VQA
dataset with provider terms.
Used for medical VQA with public
images and question-answer labels.
MoleculeQA [102] Text-integrated Public molecule question-answer
dataset; no human-subject consent is
implicated.
Used for molecule QA with
processed chemical prompts and
labels.
PathVQA [103] Text-integrated Public pathology VQA dataset with
de-identified images and provider
terms.
Used for pathology VQA under
academic non-commercial
benchmark restrictions.
SwissProtCLAP [104] Text-integrated Public protein-text alignment
resource built from UniProt-style
annotations.
Used for protein-function matching
with processed sequence/text pairs
and source citation.
A2.3 Dataset Size Summary
This section defines the storage numbers used in Figure 2 and Table A1. Table A7 reports byte-
summed public package sizes by domain, while per-task sizes are listed in Table A3. We report
binary GiB for file-system accounting and include the decimal GB total when helpful; 104.08 GiB
corresponds to 111.8 GB.
Table A7:Public data package size.Total: 104.08 GiB across 76 public task capsules.
Domain #Files Size (GiB)
chemical-biology 32 0.06
imaging 172,147 35.93
network-biology 32 0.02
perturbation-dynamics 32 0.34
phenotype-disease 172 3.40
sequence 44 1.76
single-cell 68 6.09
structure 128,316 45.55
text-integrated 241,266 10.94
Total 542,109 104.08
Task sizes span five orders of magnitude. The smallest public task capsules are SMILES-only
chemical tasks below 1 MB, whereas the largest capsules store imaging volumes, microscopy images,
or protein structures at multi-GB scale. Most single-cell tasks use AnnData or sparse matrices with
33

## Page 34

Table A8:Agent-facing prompt (abridged).Full templates are in the released runner scripts.
System:You are a careful biomedical machine-learning engineer. Your goal is to produce a correct
submission.csv for the task below. You have access to a Linux shell inside a sandbox with Python
3.11, scanpy, monai, rdkit, torch, torch_geometric, transformers, biotite, and the standard
data-science stack. No network is available.
User:Here is the task description. Read it and write a single Python script solution.py that trains a
model on the public training data and writes submission.csv in the same column schema and row order
assample_submission.csv.
«< description.md »>
104–5×10 5 cells and thousands of genes/features. Molecular tasks use 2k–100k molecules, and
protein tasks use 1k–50k sequences or structures.
A2.4 Ethics and Data Licensing
This section interprets the source audit in Table A6 at the level of benchmark release policy. Every pri-
mary data source used by BioXArena is either (i) openly licensed for redistribution (e.g. TDC, Open-
Problems, ProteinGym, LIVECell, MitoEM, LINCS-L1000, STRING, Reactome, KEGG, KEGG-
REST, DisGeNET, HAM10000, PanNuke, ECG-QA, SLAKE, PMC-VQA, PathVQA, MoleculeQA,
SwissProtCLAP) or (ii) released under a Data Use Agreement that permits derivative tasks but not the
raw-data redistribution itself (notably TCGA, METABRIC, ABIDE, LIDC-IDRI). Tasks in category
(ii) are released in adata-access-guardedtier: we redistribute the task description, sample submission,
and evaluator code, but instruct submitters to fetch the raw data from the original source with their
own DUA approval. All redistributed data is de-identified; no personally identifying information is
shipped. The released LICENSES.mdprovides the full license-compliance record corresponding to
Table A6.
We also adhere to the NeurIPS ethics checklist (see checklist.tex): we have considered foresee-
able harms from a biomedical ML benchmark (e.g. over-fitting to clinical-looking datasets that are
not diagnostic-grade; over-claiming agent capabilities in safety-critical settings), and we recommend
that any downstream use of BioXArena-evaluated agents in clinical or production biology be subject
to independent validation.
A2.5 Task Layout and Agent Interface
This section defines the execution interface used by all agents before the reproducibility and evaluator
details in App. A2.6 and App. A2.7. Every task in BioXArena follows the same on-disk layout:
BioXArena-Data-Public/<domain>/<task>/public/
description.md # task definition, I/O, metric
sample_submission.csv # required column schema and row order
train.csv / train.* # public training features
test.csv / test.* # public test features, no labels
<modality assets> # images, AnnData, PDB, FASTA, etc.
BioXArena-Data-Private/<domain>/<task>/private/
labels.csv # held-out ground-truth labels
grade.py # task-specific metric implementation
The fixed system prompt sent to every agent at runtime is summarized in Table A8. It asks the agent
to read description.md, produce a submission.csv that matches sample_submission.csv,
and forbids downloading any data from the internet. On repair attempts we append the previous
attempt’s error summary and ask for a corrected version.
A2.6 Data Curation, Splits, and Release Artifacts
This section records the artifacts needed to reproduce the task interface in App. A2.5 and the scores
produced by App. A2.7. All 76 tasks, the unified evaluator, the locked software environment, runner
configurations for all evaluated agents, Slurm templates, per-agent execution traces, and this paper
34

## Page 35

Table A9:Score reporting rule.Only correlation metrics are converted; all other primary metrics
are already on a 0-to-1 scale.
Metric family Native range Reported leaderboard score
Pearson / Spearman correlation[−1,1] Linearly normalized to [0,1] so that -1
maps to 0, 0 maps to 0.5, and 1 maps to 1;
undefined constant-prediction correlations
are treated as invalid evaluator outputs and
receive score 0 in aggregate tables.
Accuracy, macro-F1, ROC-AUC,
macro ROC-AUC, AUPRC, C-index,
mean Dice, TM-score
[0,1]Raw metric value used directly.
source will be released under an Apache 2.0-compatible license at the time of publication. The
release fixes the prompt template summarized in Table A8 and the score-reporting rule summarized
in Table A9.
Curation, splits, and contamination controls.For BioML-coding benchmarks, data processing is
part of the evaluation protocol. Unlike knowledge-QA benchmarks, held-out prediction tasks require
leakage-aware train/test splits, hidden labels, reproducible graders, and safeguards against memorized
or copied solutions. BioXArena therefore uses biology-aware splits: protein tasks are clustered by
UniRef50, single-cell tasks are split by donor or batch, and clinical tasks are split by patient. Inspired
by MLE-bench’s plagiarism-checking practice [12] and BioML-bench’s hidden-label convention [14],
we keep private labels separate from public task capsules and retain final code plus execution traces
so that near-duplicate solutions can be audited across agents.
We specify:
1. Data split manifests.Every task has an explicit manifest that lists train/test indices or file
names so that submitters can reproduce splits exactly.
2. Held-out label release.The private test labels and private evaluators are released under a
distribution token so that re-grading is centralized and consistent.
3. Runner scripts and prompts.Every prompt template used in this paper is version-
controlled and distributed with the runner.
4. Per-run traces.For every (agent, task, round) we archive the API request and response
records, attempted solutions, execution logs, final submissions, and per-run metrics needed
for auditability.
5. Environment.We release both a conda lockfile matching the validated local environment
and a Dockerfile producing the same environment reproducibly.
6. Compute.The 11 displayed agents and the same-backbone ablation configurations were
run over all 76 tasks with a bounded rescue loop under the same 2 h wall-clock cap, on
Slurm nodes with 4×A100 GPUs; each concurrent task used 1 ×A100 and 64 GB RAM.
Total cluster time across all experiments was approximately∼700 GPU-hours.
A2.7 Evaluator and Score Reporting
This section defines the post-hoc evaluator used for all leaderboard tables. The unified
BioXArena evaluator locates the submitted submission.csv, validates its schema against
sample_submission.csv, calls each task’s private grade.pyto compute the raw primary metric,
and reports the score on a common 0-to-1 scale. Only Pearson and Spearman require conversion:
their raw correlations range from -1 to 1 and are linearly mapped to 0 to 1. All other metrics already
lie in [0,1] and are used directly. Table A9 summarizes this rule; the task-to-metric mapping is listed
in Table A3. Table A10 explains why each metric family is used for the corresponding task type.
Metric-selection rationale.Metrics were assigned before running agents and were chosen to match
the scientific object being predicted, not to favor any method family. For example, imbalanced
classification tasks use macro-averaged metrics rather than micro accuracy, rare-positive detection
tasks use AUPRC, and survival prediction uses C-index to respect censored time-to-event outcomes.
Table A10 summarizes the rationale by metric family.
35

## Page 36

Table A10:Metric-selection rationale across BioXArena.The metric for each task is chosen to
match the biological output type and the dominant statistical challenge of that task.
Metric family #Tasks Used for Why this metric is appropriate
Pearson correlation 20 Continuous regression where
linear agreement in predicted
magnitude is scientifically
meaningful.
Rewards continuous signal recovery while
being invariant to global scale and offset;
useful for expression, affinity, and other
quantitative biomedical readouts.
Spearman correla-
tion
10 Rank-sensitive regression with
noisy or nonlinearly scaled tar-
gets.
Rewards correct ordering even when abso-
lute calibration is difficult; robust to mono-
tone transformations and outliers common
in biological assays.
Accuracy 18 Balanced single-label classifica-
tion and matching tasks.
Appropriate when class priors are not
strongly skewed and the desired deliver-
able is an exact label or match.
Macro-F1 10 Imbalanced multi-class classifi-
cation.
Averages F1 across classes so rare classes
are not overwhelmed by majority classes;
better reflects biological subtype or variant-
label coverage.
ROC-AUC / macro
ROC-AUC
13 Binary or multi-label ranking
tasks with threshold-free evalu-
ation.
Measures whether positives are ranked
above negatives without fixing a decision
threshold; macro averaging prevents fre-
quent labels from dominating multi-label
tasks.
AUPRC 2 Rare-positive detection, such as
sparse edges or binding sites.
Focuses on precision among retrieved pos-
itives and is more informative than ROC-
AUC when positives are rare.
C-index 1 Survival and time-to-event pre-
diction.
Evaluates whether predicted risks correctly
order comparable patient pairs while ac-
commodating censored outcomes.
Mean Dice 1 V olumetric segmentation. Measures spatial overlap between pre-
dicted and true masks and avoids reward-
ing background-only predictions.
TM-score 1 Protein 3D structure prediction. Measures length-normalized structural
similarity and is less dominated by local
coordinate deviations than raw RMSD.
Evaluation harness.Evaluation is performed by a separate post-hoc grading harness that is never
run during the agent’s execution. The harness discovers all 76 task evaluators, checks whether the
agent produced a valid submission, loads the task-specific private labels, and computes the raw task
metric. Each evaluator applies the same schema guard: the first submission column must match the
private answer file in name, values, and order. Special handling is provided for file-path predictions,
such as AMOS organ segmentation and protein structure prediction, where submitted paths are
resolved consistently before grading.
Grading functions.Core metric functions call standard SciPy and scikit-learn implementations
where possible, with custom functions for C-index, mean Dice, and TM-score. Table A11 summarizes
the graders used by the task-specific evaluators.
A3 Implementation Details
This section documents the execution setup used for the displayed agents, the unified prompt template,
and the cluster resource configuration. These implementation details support the experimental
analyses in App. A4.
36

## Page 37

Table A11:Grading functions used by BioXArena evaluators.
Function Implementation Notes
grade_pearson scipy.stats.pearsonrUndefined for constant predictions
grade_spearman scipy.stats.spearmanrUndefined for constant predictions
grade_accuracy sklearn accuracy_score
grade_macro_f1 sklearn f1_score(macro)
grade_roc_auc sklearn roc_auc_scoreBinary tasks
grade_macro_roc_aucPer-column AUC, then mean Skips constant-true columns
grade_auprc sklearn average_precision
grade_c_indexCustom Harrell’s concordance Iterates all comparable pairs
grade_mean_dicePer-organ Dice via nibabel 15 organs, ignoring background
grade_tm_scoreCustom Cαalignment JSON structure files
grade_mean_pearsonPer-column Pearson, then mean For multi-output regression
A3.1 Agent Runner Implementations
This section describes the runner implementations used for the 11 displayed leaderboard rows and
the same-backbone ablations, sufficient for full reproduction.
Backbone choices for scaffolded agents.For the main leaderboard, we keep each published agent’s
scaffold and use the most appropriate available same-family backend. Biomni’s paper uses Claude
Sonnet 3.7; our displayed Biomni cla row uses Claude Sonnet 4 because Sonnet 4.6 removed the
assistant-prefill hook required by Biomni’s ReAct loop. STELLA’s paper uses Claude Sonnet 4
for the Dev and Tool-Creation agents and Gemini 2.5-Pro for the Manager and Critic agents; our
STELLAcla+ge row keeps this role split but uses Claude Sonnet 4.6 and Gemini-3.1-Pro. MLEvolvege
uses Gemini-3.1-Pro, matching its reported configuration, and MLMaster-2.0 dv4 uses DeepSeek-
V4-Pro in place of the earlier DeepSeek-V3.2-Speciale backend. The same-backbone ablation sets
Biomni, STELLA, MLEvolve, and MLMaster-2.0 to DeepSeek-V3.2 to isolate scaffold effects from
backbone choice.
A3.1.1 General LLM code agent
The general-LLM runner drives all seven standalone general-purpose LLM rows (GPT-5.4, Claude
Opus 4.6, Qwen3.6-Plus, Gemini-3.1-Pro, GLM-5.1, Gemma-4-31B, DeepSeek-V3.2). It implements
a single-shot code-generation loop with multi-turn repair:
1. Prompt assembly.The unified prompt template (App. A3.2) is concatenated with the task’s
description.mdand an output-format instruction requiring exactly one fenced “‘python
code block.
2. API call.The runner calls an OpenAI-compatible API through OpenRouter. Temperature
is set to 0 for all general LLMs, and reasoning mode is enabled when supported by the
backend.
3. Code extraction.The runner extracts the final fenced Python block from the response, with
a conservative fallback for responses that contain only raw Python code.
4. Execution.The extracted code is written to solution.pyand executed under the remaining
wall-clock budget.
5. Validation.On exit code 0, the runner checks for three required files: submission.csv,
metrics.json, and solution.py. It validates metrics.jsonstructure and injects wrap-
per fields (solution_generation_time_sec, code_total_time_sec, input_tokens,
output_tokens).
6. Repair.On any failure (API error, code extraction error, execution timeout, missing outputs,
invalid metrics), the runner appends a repair message containing the error reason and a short
tail of the execution log, then retries from step 2. In all reported experiments,MAX_ATTEMPTS
is set to 3, meaning at most three API/code-generation attempts per task, including the initial
attempt and any repair retries, within the 2-hour wall-clock.
37

## Page 38

Figure A1:Control flow of the general-LLM agent runner.Setup and task-discovery steps
run once, while each selected task is handled by a ThreadPoolExecutorworker through prompt
construction, API-based code generation, execution, repair, and final summary writing. In our
experiments, MAX_ATTEMPTS=3, so the loop allows at most three API/code-generation attempts per
task before marking it failed or successful.
7. Package guard.Before each task, the runner restores core Python packages (NumPy,
pandas, scipy, Pillow) to undo any dependency drift caused by prior agent-generated code.
Token counts are accumulated acrossallAPI calls for the task (including repair attempts) so that the
reported cost reflects the full conversation.
Expanded runner flow.Because none of the open- and closed-source general LLMs we evaluate ship
with their own “ML-coding” scaffolding, we built a small runner that turns any OpenAI-compatible
chat endpoint into a benchmark-runnable agent. The runner’s design is intentionally minimal: a
deterministic prompt→code→execute→repair loop, shared across every general-LLM configuration
in Table A14, so that scaffolding differences cannot explain across-model gaps. Figure A1 shows the
full control flow as a diagram; the steps are spelled out below.
The runtime sequence is:
38

## Page 39

1. CLI setup.Parse run arguments and resolve the model name, round name, data roots, output
root, and API endpoint credentials.
2. Task discovery and selection.Load the unified prompt template, discover all tasks, then
filter by –task, –domain, or –all-tasks. If –list-tasks is set, print the discovered
task keys and exit immediately.
3. Front-end validation.Check that at least one task has been selected, that each selected task
directory exists, and that description.mdis present. In non-dry-run mode, the runner also
requires API credentials.
4. Run initialization.Set the worker limit, construct the OpenAI-compatible client, create the
resolved output root, and allocate a run-level summary record.
5. Parallel task launch.Start a ThreadPoolExecutor and submit one worker future per
selected task.
6. Per-task input checks.Inside each worker, verify that the task directory,description.md,
andsample_submission.csvexist, then create the task-specific output directory.
7. Prompt construction.Assemble the initial prompt from the unified template plus the
task-specific description.md; initialize the conversation message list and token counters.
In dry-run mode, render the prompt and return without contacting the API.
8. Attempt loop.For non-dry-run execution, iterate over attempts 1. . .MAX_ATTEMPTS, with
MAX_ATTEMPTS=3 in the reported experiments. Each API request and response is persisted
for later audit.
9. Usage accounting.If the API response contains usage, accumulate prompt_tokensand
completion_tokensinto task-level totals. If usage is missing, mark a warning flag so the
finalmetrics.jsoncan record incomplete token counts.
10. Code extraction and execution.Extract the Python code block, save the attempted and
canonical solutions, then execute the canonical solution while capturing the execution log.
11. Output validation.On successful execution, check for submission.csv, metrics.json,
and solution.py. Validate metrics.json, then inject wrapper-managed fields:
solution_generation_time_sec, code_total_time_sec, input_tokens, and
output_tokens.
12. Repair on failure.If the API call fails, no code block is found, execution times out,
required files are missing, or metrics.jsonis invalid, append a repair message containing
the failure reason plus a short log tail, then retry until attempts are exhausted.
13. Task finalization.A successful task clears any stale failure marker; an exhausted task
records a failed result object.
14. Run finalization.After all futures complete, catch any worker-level exceptions, sort results
by task key, write a run-level summary, print aggregate counts, and exit with code 0 only if
every task succeeded or was a dry run.
Key operational details from the flowchart are:
• The runner reads API credentials from either a local environment file or the process environ-
ment.
•–list-tasks performs discovery and filtering only; it does not create directories, launch
workers, or contact the API.
• Every attempt persists request, response, solution, and execution logs, which makes post-hoc
debugging and trace release straightforward.
• A task is counted as successful only if solution.pyexits with code 0, all required output
files exist, and wrapper-side metrics injection succeeds.
• The summary record is written as a run-level artifact, separate from task-level outputs.
A3.1.2 Biomni
Biomni [5] is invoked through a lightweight wrapper that constructs a prompt from the unified
template and calls the Biomni A1 agent. The A1 agent manages its own internal ReAct loop (action
39

## Page 40

→ observation → reflection); the wrapper doesnothandle retries. The displayed leaderboard row
uses Claude Sonnet 4, while the same-backbone ablation uses DeepSeek-V3.2; both are routed
through OpenRouter with temperature 0 and a 7,200 s timeout. Wall-clock is enforced through a child
process, and per-worker memory is capped at 60 GB. Biomni’s 15 GB S3 data cache is symlinked
into each task’s output directory to avoid redundant downloads.
A3.1.3 STELLA
STELLA [6] is a multi-agent system built on the smolagents framework. Our wrapper redirects
STELLA’s three global model roles to the configured backend LLM:
stella_core.claude_model←Dev Agent,stella_core.gpt_model←Manager + Tool Creation,
stella_core.gemini_model←Critic.
In our main experiments all three roles are set to DeepSeek-V3.2 for the DeepSeek same-backbone
ablation and to a Sonnet-4.6/Gemini-3.1-Pro mix for the displayed configuration. STELLA uses
up to 50 internal steps, a skill manager with TF-IDF similarity retrieval, a tool governance system
that dynamically creates and registers new tools, and optional Mem0-based memory (disabled in our
runs). Wall-clock is enforced with a 7,200 s timeout.
A3.1.4 MLMaster-2.0
MLMaster-2.0 [23] is launched as a subprocess with a 7,200 s task-level time limit and a 10-minute
timeout for each code execution. The agent uses Monte Carlo Tree Search (MCTS) with UCT-based
exploration-exploitation. Separate code-generation and feedback LLMs are both set to the configured
backbone. On timeout, the wrapper terminates the full process group and then copies the best
available submission from MLMaster-2.0’s internal workspace to the standard output directory.
A3.1.5 MLEvolve
MLEvolve is launched with the same task-level and per-execution time limits. The agent uses Monte
Carlo Graph Search (MCGS) with five specialised sub-agents:Draft,Improve,Debug,Evolution,
andFusion. Execution is pipelined: phase 1 generates drafts sequentially (code only, no execution)
for diversity; phase 2 executes drafts in parallel while new search steps proceed concurrently. The
cold-start guidance can optionally be loaded from a knowledge base before search begins.
A3.2 Unified Prompt Template
The unified prompt sent to the agents is defined once and rendered for each task. Rather than
reproducing both the raw verbatim template and a formatted version, we show only the structured
rendered version below for readability. For the general-LLM runner, an additional output-format
instruction is appended requiring exactly one fenced ```python code block that can be executed
directly assolution.py.
Rendered Unified Evaluation Prompt
The same prompt can also be rendered in a structured, human-readable format as follows.
Prompt.(Unified Evaluation Prompt for BioXArena Agents)
Evaluation Task
You are a Machine Learning coding agent evaluated on a biomedical ML benchmark: BioXArena.
Task & Paths
• Task directory: {task_dir}
• Output directory: {output_dir}
• Description file:description.md
Requirements
1. Explore and understand the public data first. Only use public files under {task_dir}.
40

## Page 41

2. Public files may include:
• Training data:train.csv/train.jsonl.gz/train_*.npz/ . . .
• Test data:test.csv/test.jsonl.gz/test_*.npz/ . . .
• Modality-specific assets
•sample_submission.csv
3. Perform appropriate feature engineering, preprocessing, and model selection for the task.
4. Train a concrete ML or deep learning model.
If using deep learning, train on GPU(s). 1 GPU is available per task.
5. Generate predictions on the test set.
6. Save the submission as{output_dir}/submission.csv.
Format must exactly match sample_submission.csv, including the exact number of columns, exact
column names, and the exact values and order of the first column.
7. Save a metrics file as{output_dir}/metrics.jsonwith this exact format:
{
"solution_generation_time_sec":
"time from the beginning of code generation until the final correct
solution.py is produced",
"train_time_sec":
"time spent on training/fitting the final correct solution.py",
"test_time_sec":
"time spent on running inference/prediction on the test set for the
final correct solution.py",
"code_total_time_sec":
"solution_generation_time_sec + train_time_sec + test_time_sec",
"input_tokens":
"total number of input/prompt tokens used to complete the task across
all API attempts",
"output_tokens":
"total number of output/completion tokens used to complete the task
across all API attempts",
"model_used":
"e.g. XGBoost / RandomForest / CNN / Transformers / ...",
"model_param_count":
"number of trainable parameters if applicable; otherwise null or an
estimated/appropriate value for the model",
"notes":
"any relevant details about feature engineering, preprocessing, etc."
}
8. Save your final or best-performing Python solution to {output_dir}/solution.py, including the full
training and inference code.
9. If applicable, save the corresponding trained model weights in {output_dir}. Store them as at least one
model artifact file (for example.pt, .pth, .ckpt, .bin, .joblib, .pkl, .pickle, .onnx, .model, .cbm)
or in a dedicatedweights/orcheckpoints/directory under{output_dir}.
10. Do NOT access any private directories, answer files, hidden labels, or non-public artifacts.
11. You are finished only after submission.csv, metrics.json, and solution.py are correctly saved in
{output_dir}.
Timing
• Use Python’stimemodule to recordtrain_time: total model training time.
• Use Python’stimemodule to recordtest_time: total model testing time.
• The outer runner may overwrite code_total_time_sec in metrics.json to include end-to-end genera-
tion and execution time.
• The outer runner may also inject solution_generation_time_sec, input_tokens, and
output_tokens.
Execution Guidelines
• Show reasoning for preprocessing, model choice, and hyperparameters.
• Optimize model selection for the specific modality and task type (classification/regression/multi-
label/survival/etc.).
• Use GPU(s) for deep learning tasks.
• If using PyTorch, explicitly move the model and all input tensors to CUDA and ensure training and inference
run on GPU.
41

## Page 42

• Ensure output paths exist or create them.
• Handle various data formats (.csv,.jsonl.gz,.npz, etc.).
• Log any important notes inmetrics.json.
Task Description
Refer to the task-specific description below for details.
[description.md]
{description}
[end description.md]
A3.3 Cluster Configuration
All experiments were run on a shared HPC cluster. Table A12 lists the Slurm configuration.
Table A12:Slurm resource configuration for agent runs and evaluation.
Parameter Agent runs Evaluation
Wall-clock 48 h 2 h
Nodes 1 1
Tasks per node 4 1
CPUs per task 16 (64 total) 16
GPUs 4×A100 (1 per task) none
Conda envbioxbench bioxbench
Per-task wall-clock 7,200 s (2 h) N/A
Per-task GPU 1 (via hash-basedCUDA_VISIBLE_DEVICES) N/A
MAX_WORKERS4 concurrent 4 concurrent
API gateway OpenRouter N/A
A4 Additional Experimental Results and Analyses
This section collects the supplemental result tables and analyses that extend § 3: agent-level statistics,
domain-, modality-, and task-level breakdowns, emitted ML-model choices, runtime and cost, failure
diagnostics, robustness analysis, ablations, scaling, and the human expert pilot.
A4.1 Agent-level Analysis
The experimental appendices follow the main-text result flow: overall leaderboard statistics first, then
domain-, modality-, and task-level analyses, emitted ML-model choices, runtime and cost, failure
diagnostics, robustness analysis, ablations, scaling, and the human expert baseline.
Table A15 extends Table A14 with additional columns: total #submission attempts, average wall-
clock-per-task, average prompt/completion tokens per task, and estimated $cost per task using the
price table in App. A4.6.
A4.2 Domain-Level Analysis
Table A16 shows the mean normalized score of each agent on each of the 9 domains. The coloured
heat map version is Figure 3 in the main body.
Domain difficulty. Chemical-biologyis the easiest domain after adding MLEvolve, MLMaster-
2.0, and Gemini-3.1-Pro (mean penalized score across the 11 displayed agents: 0.77), followed by
single-cellandstructure(both 0.65) andsequence(0.62). These domains often admit strong feature-
engineered tabular, sequence, or graph representations that modern coding agents can instantiate
with scikit-learn, XGBoost, LightGBM, RDKit, or compact neural models. The hardest domains are
42

## Page 43

Table A13:Failure taxonomy for the main 11-agent leaderboard.The 111 failures are mutually
exclusive. Most occur before valid model evaluation, especially missing submissions, rather than
from low held-out scores; fixed-backbone variants are analyzed in App. A4.11.
Failure reason Count Pct Description
No submission 58 52.3% Code crashed, timed out, or API error (nosubmission.csv)
ID mismatch 19 17.1% Submission exists, butidcolumn mis-ordered or mis-typed
No valid correlation 17 15.3% Constant regression predictions, Pearson/Spearman undefined
NaN/Inf in predictions 10 9.0% Numerical pathology (non-converging model, division by zero)
Format error 7 6.3% Wrong columns/shape, type mismatches, missing required fields
Total 111 100%
Table A14:Submission, success, and failure breakdown on BioXArena (76 tasks, 11 displayed
agents).“Subs” = tasks that produced a submission.csv; “OK” = tasks that also passed the
held-out evaluator. The five rightmost columns decompose the remaining failures into mutually-
exclusive categories (definitions in Table A13); their sum equalsFail. “Const. n” and “Const. score”
are diagnostics, not part ofFail: they count successful non-Pearson/Spearman submissions whose
prediction rows are identical for every test example and report their mean score. GPT-5.4 is the only
agent that submits on every task; DeepSeek-V3.2 fails on every axis. Same-backbone DeepSeek-V3.2
variants of Biomnidv3, STELLAdv3, and MLEvolvedv3 are deferred to§3.4. Figure 3 (c) visualizes
these counts in the main text.
Agent (backbone) Subs OK Const. n Const. score Fail No sub. ID mm NaN/Inf No corr. Format
MLEvolve ge 72 72 0 – 4 4 0 0 0 0
STELLA cla+ge 71 68 1 0.200 8 5 0 0 0 3
MLMaster-2.0 dv4 69 68 5 0.292 8 7 0 0 1 0
Biomnicla 68 67 1 0.244 9 8 1 0 0 0
GPT-5.476 71 3 0.261 5 0 0 0 4 1
Gemini-3.1-Pro75 70 3 0.217 6 1 0 1 4 0
GLM-5.172 68 3 0.313 8 4 2 1 1 0
Qwen3.6-Plus74 70 1 0.081 6 2 2 1 1 0
Claude-Opus-4.669 65 2 0.347 11 7 0 2 2 0
Gemma-4-31B 66 59 2 0.022 17 10 3 1 2 1
DeepSeek-V3.2 66 47 5 0.095 29 10 11 4 2 2
TotalN/A725 26 0.214 111 58 19 10 17 7
Subscripts follow the main-text convention:ge=Gemini-3.1-Pro,dv4=DeepSeek-V4-Pro,cla=Claude-only Biomni
configuration,cla+ge=STELLA’s Claude-plus-Gemini configuration, anddv3=DeepSeek-V3.2 ablation.
perturbation-dynamics(0.42),text-integrated(0.47), and the network/phenotype domains (both
about 0.49): perturbation tasks require conditional gene-expression response models, while text-
integrated tasks require cross-modal reasoning over free text, biomedical images/signals, or structured
molecular inputs. Chemical-biology now has the largestspreadacross agents ( ∆ = 0.54), driven by
MLMaster-2.0’s strong chemical-biology run and DeepSeek-V3.2’s weak baseline; network-biology
has the lowest spread (∆ = 0.08), with all agents clustered near 0.43–0.51 (Table A17).
Domain specialisation.Strikingly,no single agent leads every domain. MLEvolve leads sequence
and single-cell; GPT-5.4 leads structure; MLMaster-2.0 leads chemical-biology; Biomni leads
perturbation dynamics and imaging; STELLA leads phenotype–disease and text-integrated; and
GLM-5.1 narrowly leads network-biology. The added MLMaster-2.0 row changes the chemical-
biology leader from GLM-5.1 to MLMaster-2.0 (0.91), while the stronger STELLA mixed backbone
makes STELLA the best text-integrated agent (0.64). Biomni’s perturbation-dynamics advantage
over GPT-5.4 remains large (+0.24), indicating that its tool environment is specifically helpful for
the scRNA-based perturbation-response prediction tasks that dominate this domain.
Qualitative trends.Imaging sits in the middle, largely because half of its 8 tasks (skin lesion, lung
nodule, drug MOA, nucleus type) fit the standard “ResNet-50 from torchvision” playbook that
43

## Page 44

Table A15:Full per-agent statistics for the 11 displayed agents. “Succ. mean” averages normalized
score over successfully evaluated tasks, while “Penalized” averages over all 76 tasks with failed
runs scored as zero. Avg time is the total wall-clock average over all 76 task outputs, using outer
runner elapsed time when available and falling back to runner-injected code_total_time_secor
failed-attempt durations when needed. Multi-round tasks contribute once: the first successful run if
any run succeeds, otherwise the last failed run among the official merged rounds. The “In tok” and
“Out tok” columns are per-task averages: cumulative LLM API tokens within the selected task outputs
divided by 76 tasks; for search agents, this includes all recorded planning, review, improvement,
and repair calls. MLEvolve ge is therefore much more LLM-token-heavy than MLMaster-2.0 dv4,
whose search spends more of the 2 h budget in local code execution and hyperparameter/model trials.
Cost is computed from the token counts at provider-published prices checked on May 1, 2026 (see
Table A24).
Agent Subs Eval OK Succ. mean Penalized Avg time In tok Out tok $/task
MLEvolvege 72/76 72 0.703 0.666 120 min 784k 8k 1.67
STELLAcla+ge 71/76 68 0.685 0.613 15 min – – –
MLMaster-2.0dv4 69/76 68 0.652 0.584 120 min 101k 58k 0.09
Biomnicla 68/76 67 0.657 0.579 27 min – – –
GPT-5.4 76/76 71 0.681 0.636 22 min 8k 25k 0.39
Gemini-3.1-Pro 75/76 70 0.663 0.611 6 min 4k 7k 0.10
GLM-5.1 72/76 68 0.672 0.601 24 min 7k 36k 0.13
Qwen3.6-Plus 74/76 70 0.642 0.591 24 min 7k 14k 0.03
Claude-Opus-4.6 69/76 65 0.669 0.572 87 min 60k 39k 1.28
Gemma-4-31B 66/76 59 0.661 0.513 74 min 10k 37k 0.02
DeepSeek-V3.2 66/76 47 0.574 0.355 17 min 9k 10k 0.01
Table A16:Mean normalized score per agent × domain.Cells show the penalized average over all
tasks in that domain. Bold marks the per-domain leader.
Agent chem img net pert phen seq sc str txt avg
MLEvolve ge 0.87 0.61 0.51 0.60 0.500.77 0.800.75 0.53 0.666
STELLA cla+ge 0.88 0.65 0.50 0.560.570.68 0.56 0.480.64 0.613
MLMaster-2.0 dv4 0.910.63 0.51 0.58 0.49 0.74 0.55 0.41 0.41 0.584
Biomni cla 0.720.660.500.630.55 0.53 0.65 0.57 0.41 0.579
GPT-5.4 0.87 0.60 0.51 0.39 0.50 0.75 0.670.840.57 0.636
Gemini-3.1-Pro 0.83 0.64 0.51 0.40 0.49 0.60 0.68 0.74 0.61 0.611
GLM-5.1 0.89 0.510.510.34 0.49 0.65 0.75 0.82 0.39 0.601
Qwen3.6-Plus 0.84 0.62 0.45 0.36 0.53 0.61 0.76 0.67 0.44 0.591
Claude-Opus-4.6 0.61 0.66 0.51 0.42 0.51 0.67 0.50 0.73 0.56 0.572
Gemma-4-31B 0.75 0.49 0.43 0.21 0.41 0.57 0.68 0.73 0.29 0.513
DeepSeek-V3.2 0.36 0.51 0.43 0.14 0.29 0.26 0.52 0.40 0.26 0.355
LLM agents are fluent in, while the other half (AMOS segmentation, virtual staining, label-free
cell counting, mitochondria counting) require real imaging pipelines that agents rarely complete in
2 h. The 10 hardest individual tasks (App. A4.4) are headed by AMOS organ segmentation (mean
= 0.033), protein-complex prediction from CORUM (0.098), and Reactome pathway membership
(0.112); the 10 easiest are headed by cell-type-from-expression (0.990), cancer-drug-sensitivity
(0.967), and synthetic-lethality prediction (0.966).
Domain spread and specialisation.Table A17 shows how much each domaindiscriminatesbetween
agents by reporting the max, min, and spread (max −min) of the penalized score across the 11
displayed agents. A high spread means the domain is a powerful discriminator; a low spread means
all agents perform similarly.
Table A18 lists the best and worst domain for each agent.
44

## Page 45

Table A17:Per-domain spread of penalized scores.Chemical-biology is the most discriminative
(∆ = 0.54); network-biology is the least (∆ = 0.08).
Domain Max Min∆Leader
chemical-biology 0.91 0.36 0.54 MLMaster-2.0 dv4
sequence 0.77 0.26 0.51 MLEvolve ge
perturbation-dyn. 0.63 0.14 0.48 Biomni cla
structure 0.84 0.40 0.44 GPT-5.4
text-integrated 0.64 0.26 0.38 STELLA cla+ge
single-cell 0.80 0.50 0.30 MLEvolve ge
phenotype-disease 0.57 0.29 0.29 STELLA cla+ge
imaging 0.66 0.49 0.17 Biomni cla
network-biology 0.51 0.43 0.08 GLM-5.1
Table A18:Best and worst domain per agent.
Agent Best domain Score Worst domain Score
MLEvolve ge chemical-biology 0.87 phenotype-disease 0.50
STELLA cla+ge chemical-biology 0.88 structure 0.48
MLMaster-2.0 dv4 chemical-biology 0.91 structure 0.41
Biomni cla chemical-biology 0.72 text-integrated 0.41
GPT-5.4 chemical-biology 0.87 perturbation-dyn. 0.39
Gemini-3.1-Pro chemical-biology 0.83 perturbation-dyn. 0.40
GLM-5.1 chemical-biology 0.89 perturbation-dyn. 0.34
Qwen3.6-Plus chemical-biology 0.84 perturbation-dyn. 0.36
Claude-Opus-4.6 structure 0.73 perturbation-dyn. 0.42
Gemma-4-31B chemical-biology 0.75 perturbation-dyn. 0.21
DeepSeek-V3.2 single-cell 0.52 perturbation-dyn. 0.14
A4.3 Comparison between Multi-modal and Uni-modal Tasks
We use the modality audit in App. A2.1 to split the benchmark into 46 multi-modal tasks and
30 uni-modal tasks; the 10 borderline cases are counted as multi-modal, matching the main-text
convention. Figures A2 and A3 reuse the scoring definitions of Figures 3 and 5: the successful-run
figures average only successfully evaluated runs, whereas the penalized figures average over all tasks
in the corresponding subset and assign failed runs score 0. Within each domain, blank cells indicate
that the domain has no task in that modality group; dashes in successful-run figures indicate that tasks
exist but no run in that cell passed evaluation. The Avg columns are task-weighted averages over all
uni-modal or multi-modal tasks, not averages of the displayed domain cells.
In the main experiment, multi-modal tasks are consistently harder but not categorically out of reach.
Averaged across the 11 displayed agents, the successful-run mean is 0.675 on uni-modal tasks and
0.651 on multi-modal tasks; the penalized mean is 0.589 versus 0.566, a 2.3-point gap after failures
are counted as zero. MLEvolve ge leads both groups under the primary penalized metric (0.679
on uni-modal tasks and 0.657 on multi-modal tasks), followed by GPT-5.4 and STELLAcla+ge on
uni-modal tasks and by GPT-5.4 and Claude-Opus-4.6 on multi-modal tasks. The domain split is
important for interpretation: imaging and text-integrated tasks are entirely multi-modal, chemical
biology is mostly uni-modal, and mixed domains such as sequence, single-cell, structure, network
biology, perturbation dynamics, and phenotype–disease expose both regimes.
The same-backbone ablation shows the same qualitative pattern with a larger penalty. Across the five
DeepSeek-V3.2 rows, successful-run means are 0.638 on uni-modal tasks and 0.602 on multi-modal
tasks, while penalized means are 0.519 and 0.478, respectively. This 4.0-point penalized gap suggests
that, once backbone capacity is held fixed, multi-modal tasks stress both modeling quality and
execution reliability. MLEvolvedv3 remains the strongest same-backbone agent on both groups, but
its multi-modal penalized score is still 9.8 points below its uni-modal score, indicating that search
and repair help without fully removing the added burden of heterogeneous inputs.
45

## Page 46

Figures A4 and A5 provide aggregate views of the same phenomenon. In the scatter plots, most meth-
ods fall below the diagonal comparison implied by equal uni-modal and multi-modal performance,
confirming that heterogeneous inputs usually reduce mean score even for strong configurations. The
bar plots show a parallel source-level effect: multi-source tasks tend to be harder than single-source
tasks, but the single-source subset is small and therefore has wider uncertainty. Together, these
summaries support the task-level heatmaps while making clear that the observed gap is driven by
both modality heterogeneity and source integration. Taken together, the modality split should be read
as a diagnostic axis rather than a replacement for domain-level analysis. Multi-modal inputs increase
pressure on schema alignment, data loading, and representation choice, but domain-specific modeling
still determines which agent leads.
(a) Avg. score on successful uni-modal/multi-modal tasks
Uni-modal tasks
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotype
Avg
MLEvolvedv3 67.8 84.8 37.7 37.0 89.6 72.1 31.5 68.0
MLMaster-2.0dv3 51.9 84.0 25.7 36.6 89.1 77.3 35.9 65.1
Biomnidv3 66.2 85.6 53.6 35.4 89.0 59.8 31.8 65.2
STELLAdv3 57.6 70.0 2.8 49.2 86.5 77.0 35.1 62.0
DeepSeek-V3.2 62.4 70.5 39.8 29.0 72.9 57.4 45.5 58.6
Multi-modal tasks
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text Avg
75.7 83.1 73.5 51.4 89.5 54.5 66.5 63.2 51.2 64.3
74.9 67.1 54.6 59.5 100.0 55.3 55.3 68.6 54.7 63.2
79.9 64.5 61.8 59.7 72.8 70.5 65.6 41.9 43.8 60.3
79.0 41.9 47.3 50.4 58.1 54.2 69.9 66.1 28.0 56.4
65.8 56.1 79.9 57.9 0.3 – 46.2 67.6 42.0 56.6
(b) Penalized avg. score on all uni-modal/multi-modal tasks
Uni-modal tasks
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotype
Avg
MLEvolvedv3 67.8 84.8 37.7 37.0 89.6 54.1 31.5 65.7
MLMaster-2.0dv3 41.5 84.0 25.7 36.6 89.1 38.6 35.9 58.6
Biomnidv3 66.2 71.3 53.6 35.4 50.8 59.8 21.2 54.4
STELLAdv3 46.1 46.7 1.4 32.8 61.7 38.5 35.1 43.4
DeepSeek-V3.2 25.0 58.8 39.8 19.3 41.7 28.7 30.3 37.1
Multi-modal tasks
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text Avg
60.6 62.4 73.5 51.4 89.5 54.5 53.2 55.3 38.4 55.9
74.9 67.1 36.4 59.5 100.0 41.5 44.3 60.0 34.2 52.2
79.9 48.4 51.5 59.7 72.8 70.5 65.6 31.4 27.3 51.2
79.0 41.9 31.5 40.4 58.1 54.2 69.9 49.5 14.0 45.4
26.3 42.1 39.9 57.9 0.3 0.0 27.7 50.7 26.2 34.4
0 25 50 75 100
Cell Score (%)
Figure A2:Same-backbone comparison between uni-modal and multi-modal tasks.All rows use
the DeepSeek-V3.2 backend. Panel (a) reports the average score on successful uni-modal/multi-modal
tasks, while panel (b) reports the penalized average over all such tasks, with failed runs scored as zero.
The uni-modal panels omit Imaging and Text, which contain no uni-modal tasks, and the multi-modal
panels omit repeated agent labels.
46

## Page 47

(a) Avg. score on successful uni-modal/multi-modal tasks
Uni-modal tasks
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotype
Avg
MLEvolvege 71.5 86.7 79.0 36.4 88.5 78.3 38.6 72.7
STELLAcla+ge 67.3 90.1 50.0 35.5 89.6 74.1 35.5 69.6
Biomnicla 60.0 79.0 55.5 36.2 82.6 74.2 31.3 65.9
MLMaster-2.0dv4 69.0 75.9 32.4 35.7 90.5 61.4 36.8 65.1
GPT-5.4 68.4 66.9 99.3 36.3 88.7 60.3 41.9 68.2
GLM-5.1 65.6 80.3 94.4 37.0 91.1 58.2 45.4 72.1
Claude-Opus-4.6 65.6 76.4100.036.4 89.7 58.6 38.0 66.9
Gemini-3.1-Pro 62.5 83.9 76.1 36.2 83.7 56.1 37.1 67.1
Gemma-4-31B 72.2 82.1 63.4 29.4 89.3 58.4 24.5 68.8
Qwen3.6-Plus 61.8 84.8 56.5 29.0 89.5 60.6 24.3 67.0
DeepSeek-V3.2 62.4 70.5 39.8 29.0 72.9 57.4 45.5 58.6
Multi-modal tasks
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text Avg
81.5 69.5 73.7 59.7 76.3 81.0 71.4 60.6 61.1 68.7
85.2 54.5 57.0 58.3 75.6 73.9 70.6 74.4 64.1 67.8
75.3 83.7 68.8 57.8 – 69.9 75.1 65.9 47.4 65.6
78.5 58.1 65.4 60.0 90.7 72.6 69.9 71.9 47.1 65.4
81.1 68.0 78.4 59.4 71.5 65.9 68.8 68.7 56.5 68.0
77.3 67.8 78.4 59.5 77.3 94.0 74.8 58.6 39.3 63.9
80.5 66.8 76.2 59.6 35.4 78.6 73.0 65.6 56.5 66.9
86.6 44.5 73.0 59.9 76.4 75.8 70.2 63.5 60.7 65.8
70.3 68.2 76.2 71.4 61.0 54.2 70.0 65.4 39.0 64.5
71.7 63.7 69.9 59.6 48.8 54.4 69.9 71.1 43.6 62.4
65.8 56.1 79.9 57.9 0.3 – 46.2 67.6 42.0 56.6
(b) Penalized avg. score on all uni-modal/multi-modal tasks
Uni-modal tasks
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotype
Avg
MLEvolvege 71.5 86.7 79.0 36.4 88.5 39.2 38.6 67.9
STELLAcla+ge 67.3 75.1 50.0 35.5 89.6 55.6 35.5 65.0
MLMaster-2.0dv4 69.0 63.3 32.4 35.7 90.5 61.4 36.8 62.9
Biomnicla 60.0 65.9 55.5 36.2 82.6 55.6 20.8 59.3
GPT-5.4 68.4 66.9 99.3 36.3 88.7 45.2 41.9 66.0
Gemini-3.1-Pro 50.0 83.9 76.1 36.2 83.7 42.1 37.1 62.6
GLM-5.1 52.5 80.3 94.4 37.0 91.1 43.7 30.3 64.9
Qwen3.6-Plus 49.4 84.8 56.5 19.3 89.5 45.5 24.3 60.3
Claude-Opus-4.6 52.5 38.2100.036.4 64.1 43.9 38.0 51.3
Gemma-4-31B 43.3 68.4 63.4 19.6 76.6 29.2 16.3 50.5
DeepSeek-V3.2 25.0 58.8 39.8 19.3 41.7 28.7 30.3 37.1
Multi-modal tasks
SequenceSingle-cellStructureNetworkChemicalPerturbationPhenotypeImaging
Text Avg
81.5 69.5 73.7 59.7 76.3 81.0 57.1 60.6 53.4 65.8
68.2 27.3 47.5 58.3 75.6 55.4 70.6 65.1 64.1 58.9
78.5 43.6 43.6 60.0 90.7 54.5 55.9 62.9 41.2 55.4
45.2 62.8 57.4 57.8 0.0 69.9 75.1 65.9 41.5 57.0
81.1 68.0 78.4 59.4 71.5 32.9 55.0 60.1 56.5 62.1
69.3 44.5 73.0 59.9 76.4 37.9 56.1 63.5 60.7 60.1
77.3 67.8 78.4 59.5 77.3 23.5 59.8 51.3 39.3 57.0
71.7 63.7 69.9 59.6 48.8 27.2 69.9 62.2 43.6 58.3
80.5 66.8 63.5 59.6 35.4 39.3 58.4 65.6 56.5 61.1
70.3 68.2 76.2 57.1 61.0 13.6 56.0 49.0 29.3 51.9
26.3 42.1 39.9 57.9 0.3 0.0 27.7 50.7 26.2 34.4
0 25 50 75 100
Cell Score (%)
Figure A3:Main-experiment comparison between uni-modal and multi-modal tasks.The 11
displayed agents are evaluated separately on the 30 uni-modal and 46 multi-modal tasks. Panel (a)
reports the average score on successful uni-modal/multi-modal tasks, while panel (b) reports the
penalized average over all such tasks, with failed runs scored as zero. The uni-modal panels omit
Imaging and Text, which contain no uni-modal tasks, and the multi-modal panels omit repeated agent
labels.
47

## Page 48

Figure A4:Aggregate uni-modal versus multi-modal performance.The top panel isolates the
same-backbone ablation, while the bottom panel overlays the broader set of main and ablation
configurations. Points closer to the upper-right perform better on both task groups; larger annotated
gaps indicate a larger drop from uni-modal to multi-modal tasks.
48

## Page 49

Figure A5:Aggregate source and modality splits with variability.The top panel compares single-
source and multi-source tasks, and the bottom panel compares uni-modal and multi-modal tasks.
Bars report mean normalized scores with variability across tasks; wider intervals for single-source
tasks reflect the much smaller subset size.
49

## Page 50

A4.4 Task-Level Analysis
Tables A19 and A20 list the 10 tasks with the lowest and highest mean normalized score across all
11 displayed agents. AMOS organ segmentation is the single hardest task (mean = 0.033), because
3D CT/MRI segmentation under a 2-hour wall-clock is beyond what any current agent scaffold can
complete. Cell-type-from-expression is the easiest (0.990); it is a standard scRNA-seq classification
that maps cleanly onto a Random Forest.
Table A19:10 hardest tasks.Mean normalized score across 11 displayed agents.
# Domain Task Mean
1 imaging amos-organ-segmentation 0.033
2 network-bio protein-complex-corum 0.098
3 network-bio pathway-membership-reactome 0.112
4 pheno-dis covid19-severity-classification 0.121
5 perturbation gene-regulatory-network-inference 0.149
6 single-cell cross-modality-cell-matching 0.152
7 perturbation spear-atac-perturbation 0.188
8 text-int. dna-enzyme-function 0.198
9 imaging drug-moa-prediction 0.205
10 pheno-dis spatial-immune-infiltration 0.221
Table A20:10 easiest tasks.Mean normalized score across 11 displayed agents.
# Domain Task Mean
1 single-cell cell-type-from-expression 0.990
2 perturbation cancer-drug-sensitivity 0.967
3 network-bio synthetic-lethality-prediction 0.966
4 structure complex-structure-evaluation 0.920
5 chem-bio bace1-binding-affinity 0.915
6 sequence rna-protein-binding-affinity 0.901
7 chem-bio herg-binding-affinity 0.887
8 imaging mitochondria-counting 0.880
9 imaging labelfree-cell-counting 0.877
10 network-bio ppi-prediction-string 0.867
A4.5 ML Model Choices Emitted by Agents
Table A22 below collapses the same counts in the orthogonal direction:which model families do
agents pick for each domain?The cell at row d, column f is the number of (agent, task) pairs
in domain d whose final model metadata or emitted code falls in family f, summed across the 11
displayed agents in Table A21.
Three domain-level patterns stand out:
• DNNs are concentrated in image- and sequence-like inputs.Imaging and sequence are
tied as the largest DNN sinks (38 assignments each), reflecting architectures that operate
directly on pixels or DNA/RNA/protein sequences.
• Boosted trees dominate the tabular/feature-engineered domains.Network-biology,
phenotype-disease, chemical-biology, and structure each see boosted trees in about half or
more of (agent, task) submissions, reflecting LLM agents’ heavy reliance on the “XGBoost /
LightGBM + handcrafted features” playbook.
• Neural models dominate imaging and are competitive in sequence/single-cell tasks.
Imaging has 82 neural assignments vs. 4 classical ones; sequence is also neural-heavy
50

## Page 51

Table A21:ML-model families emitted by each agent across BioXArena submissions with
recorded model metadata.Cells are task counts; n is the number of tasks assigned to a model family.
Top-level split:Classical ML(boosted trees, forest/ensemble methods, linear or constant baselines,
and other classical models) vs.Neural architectures(MLP, DNNs without pretrained encoders, and
Transformer/pretrained encoders). Figure 4 (left) visualizes this table in the main text. See footnotes
for which concrete model classes feed each column.
Classical ML Neural architectures
Agent Boost. † Forest/ens. ‡ Lin./base § Other MLP DNN ¶ Pretr./TF n
MLEvolve ge 19 0 0 0 22 22 9 72
STELLA cla+ge 20 1 1 1 20 12 16 71
MLMaster-2.0 dv4 21 0 0 2 10 10 26 69
Biomni cla 16 12 2 0 19 9 10 68
GPT-5.4 23 18 13 7 9 4 2 76
Gemini-3.1-Pro 34 2 5 0 13 14 7 75
GLM-5.1 32 3 1 2 6 6 22 72
Qwen3.6-Plus 44 2 8 2 5 5 8 74
Claude-Opus-4.6 39 3 2 4 4 7 10 69
Gemma-4-31B 24 10 2 0 12 8 10 66
DeepSeek-V3.2 12 2 4 0 28 7 13 66
†XGBoost, LightGBM, CatBoost, sklearn HistGradientBoosting. ‡Explicit mixed ensembles, RandomForest, and ExtraTrees.
§Ridge, Lasso, LogisticRegression/LinearSVC/SGD, centroid, dummy, and constant-prediction baselines. ¶DNNs without
pretrained encoders: CNN, U-Net, RNN/LSTM, and GNN variants. Pretr./TF includes Transformer-style and pretrained
encoders such as BERT/SciBERT, ClinicalBERT, ESM, BLIP/CLIP, ViT, and pretrained image backbones. “Other” includes
SVM, kNN, Naive Bayes, and unparsed classical model strings. Generic PyTorch/Scikit-learn metadata were resolved by
inspecting the emitted code.
Table A22:ML-model families emitted per domain, summed across the 11 displayed agents.
Same column families and footnote conventions as Table A21;n is the total number of (agent, task)
pairs with a model-family assignment in that domain (out of11×8–10 = 88–110).
Classical ML Neural architectures
Domain Boost. Forest/ens. Lin./base Other MLP DNN Pretr./TF n
Sequence 34 1 1 1 21 38 12 108
Single-cell 23 6 10 4 52 3 1 99
Structure 39 5 2 3 7 10 15 81
Network-biology 48 9 1 0 9 3 17 87
Chemical-biology 47 16 0 1 15 2 1 82
Perturbation-dynamics 14 5 11 6 31 3 2 72
Phenotype-disease 64 6 2 1 7 1 0 81
Imaging 4 0 0 0 2 38 42 86
Text-integrated 11 5 11 2 4 6 43 82
Total 284 53 38 18 148 104 133 778
(71 vs. 37), and single-cell leans neural (56 vs. 43), reflecting agents’ instinct to reach for
embedding-style models when the input is a long one-hot or expression vector.
Three additional qualitative observations follow from the per-agent counts in Table A21:
• Boosted trees remain the strongest common default.Claude-Opus, Qwen, GLM, and
Gemini-3.1-Pro each emit boosted trees on roughly 44–59% of model-assigned tasks. GPT-
5.4 is more diverse, splitting its 76 assigned tasks among boosted trees (30%), forest/ensem-
ble methods (24%), and linear/baseline methods (17%).
51

## Page 52

Table A23:Cost and efficiency of the 11 displayed agents.The left wall-clock block averages over
successful tasks; the right block averages over all 76 tasks. When a task is run in multiple rounds, it
contributes once: the first successful run (round_succeeded) if any run succeeds, otherwise the last
failed run among the official rounds_used. Totals use the outer runner elapsed time when recorded,
falling back to runner-injected code_total_time_sec or failed-attempt durations when needed.
Agent/LLMis non-training wall-clock, including API interaction, reasoning, wrapper execution, and
search when phase separation is unavailable;Trainis the model-training time when separately logged.
“Total tokens” reports the run-level sum of input +output tokens over the selected one output per
each of the 76 tasks, not a per-task average; Table A15 reports the corresponding per-task averages.
For search agents, these totals include all recorded planning, review, improvement, and repair calls.
“$/task” divides the corresponding total token cost by 76 tasks and uses published API prices checked
on May 1, 2026 (Table A24). Figure 4 (right) visualizes the all-task timing columns.
Successful tasks All tasks
Agent Agent/LLM Train Total Agent/LLM Train Total Total tokens (in+out) $/task
MLEvolvege 120.0 m† incl. 120.0 m 120.0 m † incl. 120.0 m 59.56M+0.63M 1.67
STELLAcla+ge 7.5 m∗ 3.9 m 11.4 m 11.5 m ∗ 3.5 m 15.0 m – –
MLMaster-2.0dv4 120.0 m† incl. 120.0 m 120.0 m † incl. 120.0 m 7.67M+4.44M 0.09
Biomnicla 9.2 m∗ 8.4 m 17.6 m 19.4 m ∗ 7.4 m 26.8 m – –
GPT-5.4 11.6 m 10.7 m 22.4 m 11.3 m 10.7 m 21.9 m 0.57M+1.86M 0.39
Gemini-3.1-Pro1.5 m 5.0 m 6.5 m 1.6 m 4.6 m 6.2 m 0.31M+0.57M 0.10
GLM-5.1 17.3 m 7.4 m 24.7 m 16.8 m 6.9 m 23.7 m 0.55M+2.71M 0.13
Qwen3.6-Plus 14.1 m 9.6 m 23.7 m 14.5 m 9.1 m 23.6 m 0.54M+1.09M 0.03
Claude-Opus-4.6 79.8 m 20.0 m 99.8 m 69.6 m 17.2 m 86.9 m 4.55M+2.98M 1.28
Gemma-4-31B 55.4 m 3.3 m 58.7 m 71.1 m 3.3 m 74.4 m 0.77M+2.82M 0.02
DeepSeek-V3.2 9.7 m 4.0 m 13.6 m 14.2 m 3.0 m 17.2 m 0.72M+0.77M 0.01
∗For Biomni/STELLA, the outer run summaries record elapsed wall-clock under the 2 h cap, including Manager/Critic/tool
creation and final development. We subtract loggedtrain_time_sec+test_time_secfrom this total to estimate
Agent/LLM; tasks without timing metrics (mostly failures) contribute zero logged training time. These wrappers still do not
record token usage. †For MLEvolve and MLMaster-2.0, the outer run summaries likewise record actual elapsed wall-clock
under the 2 h cap; their synthesized per-run metrics do not phase-separate search, candidate training, and final training, so
training is included in the search-loop time. One GLM-5.1 task without a timing record is reconstructed from trace timestamps.
• ML-research agents are neural-heavy.MLEvolve assigns 53/72 tasks to
MLP/DNN/pretrained-encoder families, and MLMaster-2.0 assigns 46/69, reflecting their
search over explicit PyTorch-style modelling programs.
• Specialized scaffolds broaden the model-family mix.Biomni has a large forest/ensemble
share (12/68 = 18%), driven mainly by RF/ExtraTrees defaults when Morgan-fingerprint
features are produced, while MLMaster-2.0, GLM, and STELLA make the most frequent
use of pretrained/Transformer models.
A4.6 Runtime and Cost Analysis
Overall, search-based agents trade time for stronger model search: MLEvolve reaches the 2 h cap
on essentially every task and averages $1.67 per task, while MLMaster-2.0 spends similar wall-
clock time but lower API cost because more work happens in local trials. Among general LLM
rows, GPT-5.4 has the best score–time tradeoff, whereas Gemini-3.1-Pro is fastest and DeepSeek-
V3.2/Gemma-4-31B are cheapest but substantially lower-scoring. Figure A6 shows the same tradeoff
from a performance–cost perspective. The main pattern is that cost and score are not monotonic:
some low-cost agents remain far below the leading performance band, while higher-cost agents do
not automatically improve the penalized average. This reinforces that cost-efficient BioML agents
need both reliable task completion and strong model selection, not only larger API spend.
We use the following published API prices (USD per million tokens), checked on May 1, 2026.
DeepSeek-V4-Pro reflects the current effective public price, which DeepSeek lists as a temporary
discount through May 31, 2026.
Per-task $cost is computed from the cumulative input and output token usage recorded in each
selected task’s metrics record, summed over the displayed run and divided by 76 tasks. These are
52

## Page 53

10−2 10−1 100 101
Cost ($/task, log scale)
0.35
0.40
0.45
0.50
0.55
0.60
0.65
0.70Mean performance (fail=0)
High perf.
Low cost
High perf.
High cost
Low perf.
High cost
$1 $10 $100 $300+
Total cost for 76 tasks (USD)
(c) Mean performance vs. cost efficiency
MLEvolve
(Gemini-3.1)
(0.666)GPT-5.4
(0.636)
GLM-5.1
(0.601)
Qwen3.6-Plus
(0.591) Claude-Opus-4.6
(0.572)
Gemma-4-31B
(0.513)
DeepSeek-V3.2
(0.355)
Figure A6:Mean performance versus cost efficiency.Each bubble plots an agent’s penalized
all-task mean score against the per-task cost estimate used for this cost-efficiency visualization;
bubble area encodes total cost over 76 tasks. Higher vertical position indicates better benchmark
performance, while lower per-task cost indicates higher cost efficiency.
Table A24:API pricing.Prices (USD per million tokens) used to estimate $cost per task.
Model Input $/M Output $/M
openai/gpt-5.4 2.50 15.00
anthropic/claude-opus-4.6 5.00 25.00
anthropic/claude-sonnet-4.6 3.00 15.00
google/gemini-3.1-pro 2.00 12.00
qwen/qwen3.6-plus 0.325 1.95
z-ai/glm-5.1 1.05 3.50
google/gemma-4-31b-it 0.13 0.38
deepseek/deepseek-v4-pro 0.435 0.87
deepseek/deepseek-v3.2-speciale 0.40 1.20
deepseek/deepseek-v3.2 0.252 0.378
run-level totals, not model-output-length estimates: ordinary coding agents mostly accumulate one
generation plus repair attempts per task, whereas search agents accumulate their internal planning
and improvement calls as well. Biomni and STELLA do not expose token usage in their released
metrics schema, so their rows are reported as “–” rather than imputed.
A4.7 Failure Analysis
Per-task failure catalogue.The 111 evaluation failures summarised in Table A14 decompose into 58
“no submission”, 19 ID-mismatches, 17 “no valid correlation”, 10 NaN/Inf, and 7 format errors. The
release includes a per-task failure catalogue with the agent, task, domain, failure category, evaluator
remark, and pointer to the relevant trace entry. The full catalogue is too large to reproduce here, but
the per-agent totals are visualized in Figure 3 (c) and tabulated in Table A14; the category-level totals
plus descriptions are in Table A13.
53

## Page 54

A4.8 Case Studies
We manually inspected representative successful and failed run traces. The boxes below show
condensed trace excerpts rather than full logs: they keep the decisive runner or evaluator message,
the task-level schema, and the modeling decision when it is visible, while omitting long paths and
uninformative stack frames.
Successful submissions: schema-aware modeling and valid outputs
Molecular regression.GPT-5.4 on chemical-biology/bace1-binding-affinityread the lowercase
smilesfield correctly and built an ensemble using character TF-IDF SMILES features, Morgan fingerprints,
MACCS keys, RDKit descriptors, ridge regression, extra trees, and XGBoost. The run produced a valid
id,affinitysubmission and achieved Pearson0.852(normalized score0.926).
Single-cell classification.GPT-5.4 on single-cell/cell-type-from-expressionloaded sparse ex-
pression counts, applied log-normalization and feature selection, incorporated metadata, and selected a
LinearSVC by cross-validation. The finalid,cell_typesubmission scored1.000accuracy.
Agentic ensemble construction.STELLA cla+ge on chemical-biology/bace1-binding-affinity
generated a five-fold ensemble over LightGBM, XGBoost, and CatBoost using Morgan fingerprints, MACCS
keys, and RDKit descriptors. The evaluator accepted the submission and reported Pearson0.840 (normalized
score 0.920), showing that agent scaffolds can produce strong biomedical ML code when the task schema is
handled correctly.
Failure examples.The following cases mirror the mutually exclusive categories in Table A13. Each
failed after a concrete interface, numerical, or execution issue, even when the attempted modeling
strategy was plausible.
No submission: timeout, empty response, and code crash
Timeout example.Biomni cla on single-cell/batch-integrationexhausted the task budget: Task
wall-clock exceeded 7200s; duration = 7200.6s. No valid submission was emitted before the
runner stopped the task.
API/code-extraction example.Gemma-4-31B on imaging/skin-lesion-diagnosis made three at-
tempts, all ending before executable code was available: Model response was empty; the missing
artifacts weresolution.py,submission.csv, andmetrics.json.
Execution-crash example.Gemma-4-31B on chemical-biology/cyp-inhibition-multi-label
eventually produced code, but the code assumed an uppercase molecular column: train_df[’SMILES’]
→KeyError: ’SMILES’ . Because the crash occurred before output writing, both submission.csvand
metrics.jsonremained missing.
ID mismatch: row identifier or first-column contract broken
STELLAcla+ge on single-cell/chromatin-to-expression wrote a dense expression matrix but
dropped the required identifier column. The sample format starts with id,gene_0,gene_1,..., whereas
the agent submission began with 0,1,2,.... The evaluator therefore stopped before scoring with:
Submission first column ’0’ does not match answers first column ’id’. This failure is
not about model quality; the prediction matrix cannot be aligned to held-out samples.
Constant prediction: valid file, undefined correlation
GPT-5.4 on perturbation-dynamics/eccite-multimodal-perturbation emitted a file with the
correct id,delta_rna_0,... schema, but all 504 prediction columns were constant zeros. The first rows
were effectively 0.0, 0.0, 0.0, ... for every output dimension. Pearson correlation is undefined when
the predicted vector has zero variance, so the evaluator reportedNo valid correlations computed.
NaN/Inf: numerical output cannot be scored
DeepSeek-V3.2 onphenotype-disease/genotype-to-phenotypeproduced the required two-column
schema, id,expression, but the prediction column was entirely non-finite in the inspected output: 0,
NaN; 1, NaN; 2, NaN. The evaluator rejected the submission with array must not contain infs or
NaNs. This typically arises when preprocessing, imputation, or model fitting silently propagates invalid
numerical values to the final file.
54

## Page 55

Table A25:Three-run robustness for general LLM agents.Penalized all-task scores are on the
0–100 scale. Flips count tasks whose pass/fail status changes and are shown in Run 1–2 / Run 1–3 /
Run 2–3 order.
Agent Run 1 Run 2 Run 3 Mean±std Pairwise flips Flip mean
GPT-5.4 63.6 63.6 63.863.7±0.16/6/6 out of 76 6.0/76
DeepSeek-V3.2 35.5 42.5 33.137.0±4.929/27/24 out of 76 26.7/76
Format error: correct task attempted, wrong output schema
STELLAcla+ge on perturbation-dynamics/gene-regulatory-network-inferencepredicted edge
scores and wrote id,target, but the task expects a class label column named label. The evaluator
message was Submission missing column: ’label’ . A similar schema-level issue occurs in 3D
segmentation when an agent writes id,label_file although the required field is prediction_file.
These failures show that agents often infer a plausible biomedical output but miss the exact benchmark
contract.
A4.9 Robustness Analysis
To estimate run-to-run variance, we collected three runs for the strongest and weakest general LLM
rows, GPT-5.4 and DeepSeek-V3.2, on all 76 tasks. Table A25 reports each penalized all-task score
on the same 0–100 scale used in the main text, with the mean and standard deviation computed across
all three runs. Pairwise flip means average the three pass/fail comparisons in Run 1–2, Run 1–3,
and Run 2–3 order. GPT-5.4 remains stable across 63.6/63.6/63.8 with a 6.0/76 flip mean, whereas
DeepSeek-V3.2 varies more widely across 35.5/42.5/33.1, with pairwise flips of 29/76, 27/76, and
24/76 and a mean of 26.7/76.
A4.10 Constant-Prediction Submissions
Table A26 lists all 26 constant-prediction submissions on non-regression tasks that passed the
evaluator but yielded near-trivial scores. In addition, 17 constant-prediction submissions on regression
tasks were scored as “no valid correlation” failures. Together, these 43 submissions are effectively
“the agent produced output but learned nothing”. We report them explicitly so that future agents can
target these pathological cases rather than eliding them.
A4.11 Same-backbone and Same-agent Ablations
Same backbone, different agent.Holding the backbone fixed to DeepSeek-V3.2, we compare five
systems that all run on the same underlying LLM: bare DeepSeek (0.3548) < STELLAdv3 (0.4460)
< Biomnidv3 (0.5243) < MLMaster-2.0dv3 (0.5472) < MLEvolvedv3 (0.5980). Every agent scaffold
improves on the raw DeepSeek loop by +0.09 to +0.24 in penalized score, with the ML-research
scaffolds doing the most. This reverses the top-level ranking shown in Figure 3 and Table A14: when
the backbone is held constant, specialised agentsdobeat a plain code-extract loop, but they cannot
overcome the GPT-5.4 backbone advantage.
Same agent, different backbone.We run the two specialised agents with two backbones each.
STELLA improves from 0.4460 (DeepSeek) to 0.6130 (Sonnet-4.6 + Gemini-3.1-Pro, +0.167);
Biomni improves from 0.5243 (DeepSeek) to 0.5792 (Sonnet-4, +0.055). Both upgrades exceed
the gap between the twoworstgeneral-LLM agents (Gemma-4-31B vs. DeepSeek = +0.159 ),
confirming that backbone capability is the dominant factor. The much larger STELLA jump suggests
STELLA’s multi-agent reflection loop benefits disproportionately from a stronger Manager+Critic,
while Biomni’s tool-augmented ReAct loop is comparatively backbone-robust. An additional Biomni
backbone sweep (gpt-5.4-mini, gpt-5-mini, gpt-4.1-mini, gpt-4o-mini, qwen3.6-plus, deepseek-v3.2)
shows mean normalized score rising monotonically with backbone capability, with gpt-5.4-mini
closing most of the gap between Biomni and the top general-purpose coders; full numbers will be
added to the camera-ready once that sweep finishes.
55

## Page 56

Table A26:Constant-prediction submissions.Non-regression submissions that passed evaluation.
Scores are normalized task scores.
Agent Task Metric Score
Biomni cla text-integrated/molecule-qa Accuracy 0.244
Claude-Opus-4.6 perturbation-dynamics/gene-regulatory-network-inference AUPRC 0.193
Claude-Opus-4.6 phenotype-disease/alzheimers-disease-staging Accuracy 0.502
DeepSeek-V3.2 chemical-biology/cell-painting-perturbation Accuracy 0.003
DeepSeek-V3.2 chemical-biology/gpcr-binding-multi-class Macro-F1 0.249
DeepSeek-V3.2 perturbation-dynamics/gene-regulatory-network-inference AUPRC 0.193
DeepSeek-V3.2 text-integrated/dna-enzyme-function Accuracy 0.029
DeepSeek-V3.2 text-integrated/ecg-signal-qa Accuracy 0.000
GLM-5.1 perturbation-dynamics/gene-regulatory-network-inference AUPRC 0.193
GLM-5.1 phenotype-disease/alzheimers-disease-staging Accuracy 0.502
GLM-5.1 text-integrated/molecule-qa Accuracy 0.244
GPT-5.4 imaging/drug-moa-prediction Macro-F1 0.000
GPT-5.4 single-cell/batch-integration Accuracy 0.412
GPT-5.4 single-cell/label-projection Accuracy 0.370
Gemini-3.1-Pro chemical-biology/kinase-selectivity-multi-label Macro-AUC 0.500
Gemini-3.1-Pro phenotype-disease/covid19-severity-classification Macro-F1 0.149
Gemini-3.1-Pro single-cell/cross-modality-cell-type Macro-F1 0.001
Gemma-4-31B phenotype-disease/covid19-severity-classification Macro-F1 0.043
Gemma-4-31B text-integrated/ecg-signal-qa Accuracy 0.000
MLMaster-2.0 dv4 perturbation-dynamics/gene-regulatory-network-inference AUPRC 0.193
MLMaster-2.0 dv4 phenotype-disease/alzheimers-disease-staging Accuracy 0.502
MLMaster-2.0 dv4 single-cell/cross-modality-cell-matching Accuracy 0.149
MLMaster-2.0 dv4 single-cell/label-projection Accuracy 0.370
MLMaster-2.0 dv4 text-integrated/molecule-qa Accuracy 0.245
Qwen3.6-Plus phenotype-disease/covid19-severity-classification Macro-F1 0.081
STELLA cla+ge structure/protein-binding-site-detection AUPRC 0.200
Table A27:Failure breakdown for the same-backbone ablation.All five rows use DeepSeek-V3.2
as the backend LLM. Columns use the same mutually-exclusive failure categories as Table A13;
the five category columns sum toFail. Compared with the bare DeepSeek-V3.2 code-extract loop,
specialised scaffolds primarily reduce missing-submission failures, while STELLA dv3 remains
dominated by ID-mismatch errors. Figure 5 (c) visualizes these counts in the main text.
Method (DeepSeek-V3.2 backend) Subs OK Fail No sub. ID mm NaN/Inf No corr. Format
MLEvolve dv3 70 69 7 6 0 0 0 1
MLMaster-2.0 dv3 66 65 11 10 0 1 0 0
Biomni dv3 69 64 12 7 4 0 0 1
STELLA dv3 71 58 18 5 10 2 0 1
DeepSeek-V3.2 66 47 29 10 11 4 2 2
TotalN/A303 77 38 25 7 2 5
A4.12 Scaling: MLEvolve
MLEvolve with its published Gemini-3.1-Pro backbone has now completed the full 76-task run under
the default 2-hour per-task budget and is included in the main leaderboard (Table A14) with a mean
normalized score of 0.666 (72/76 submissions, 4 “no submission” failures).
Scaling checkpoints on two full domains.To isolate whether extra search time helps, we re-ran
MLEvolve on chemical biology and phenotype–disease at a 12-hour per-task budget (6× the default),
with backbone and scaffold otherwise fixed. MLEvolvege logs its internal best validation-fold metric
at every candidate node it evaluates; Table A30 lists the best value reached by each checkpoint and
also reports the hidden-test normalized score at the 2-hour and 12-hour submission budgets. Missing
checkpoint candidates are counted as 0, matching the penalized leaderboard convention.
56

## Page 57

Table A28:Cost and efficiency in the same-backbone ablation.All five rows use DeepSeek-V3.2
as the backend LLM. The timing, token, and cost definitions follow Table A23: successful tasks
average over Eval-OK tasks; all-task averages include all 76 tasks, with failures contributing the
last logged failed attempt. For MLEvolve dv3 and MLMaster-2.0dv3, training is included in the
search-loop wall-clock because their synthesized metrics do not phase-separate candidate search
from final training. Biomnidv3/STELLAdv3 still do not record reliable token usage in their wrapper
schemas (“–”).
Successful tasks All tasks
Method (DeepSeek-V3.2 backend) Agent/LLM Train Total Agent/LLM Train Total Total tokens (in+out) $/task
MLEvolvedv3 120.4 m† incl. 120.4 m 120.3 m† incl. 120.3 m 43.24M+3.07M 0.16
MLMaster-2.0dv3 117.8 m† incl. 117.8 m 118.1 m† incl. 118.1 m 9.04M+3.13M 0.05
Biomnidv3 32.9 m∗ 2.0 m 34.9 m 39.7 m ∗ 1.7 m 41.4 m – –
STELLAdv3 41.9 m∗ 28.4 m 70.3 m 39.8 m ∗ 22.6 m 62.4 m – –
DeepSeek-V3.2 9.7 m 4.0 m 13.6 m 14.2 m 3.0 m 17.2 m 0.72M+0.77M 0.01
∗For Biomnidv3/STELLAdv3,Agent/LLMis the outer wrapper elapsed time minus logged training/evaluation time, capped at
the outer elapsed time for each task. †For MLEvolvedv3 and MLMaster-2.0dv3, search-loop wall-clock includes internal
candidate training and repair runs.
Table A29:ML-model families in the same-backbone ablation.Cells are task counts among
submissions with recorded or recoverable model metadata; n is the number of tasks assigned to a
model family. Columns use the same definitions as Table A21. Rows are directly comparable because
every method uses the same DeepSeek-V3.2 backend. Figure 4 (middle) visualizes this table in the
main text.
Classical ML Neural architectures
Method (DeepSeek-V3.2 backend) Boost. Forest/ens. Lin./base Other MLP DNN Pretr./TF n
MLEvolve dv3 15 0 0 7 26 4 17 69
MLMaster-2.0 dv3 21 1 2 0 13 12 17 66
Biomni dv3 26 12 10 1 8 3 4 64
STELLA dv3 14 12 6 1 3 4 12 52
DeepSeek-V3.2 12 2 4 0 28 7 13 66
Interpretation.Most internal search gains arrive early: chemical biology rises from 0.661 at
30 min to 0.876 at 1 h, then adds only 1.9 points by 12 h; phenotype–disease shows the same
diminishing-return pattern, from 0.254 to 0.487 in the first hour and to 0.507 by 12 h. The hidden-
test effect is larger for chemical biology, where the mean normalized score increases from 0.869
to 0.920 and all eight tasks improve, with the largest gain on cell-painting-perturbation.
Phenotype–disease improves only from 0.502 to 0.515: five tasks improve, two regress slightly, and
spatial-immune-infiltration fails at both budgets. This pattern suggests that longer search
helps most when the bottleneck is model selection over well-featurized inputs, whereas the hardest
clinical tasks are limited by data quality, small sample size, or task-specific execution failures.
A4.13 Human Expert Baseline
We conducted a pilot study with two PhD-level biomedical ML researchers, who had no access to
leaderboard scores, on a subset of 10 tasks randomly selected from BioXArena, spanning several
domains and input modalities. For each task, participants received the same task interface as agents
received: the official task description, training data, test inputs, submission template, and any task-
specific auxiliary files required for prediction. Held-out test labels and leaderboard scores were not
provided. Participants gave informed consent, were told that the pilot was a low-risk computational
benchmark exercise, and the activity was conducted with institutional support; under the applicable
local requirements, no separate IRB review was required.
The 2-hour budget started when the participant opened the task materials and included reading the
task description, writing or adapting code, training models, generating predictions, and preparing the
final submission. To keep the comparison focused on human modeling decisions, participants were
not allowed to use AI agents or chatbots for core method design, code generation, or debugging, but
57

## Page 58

Table A30:MLEvolve ge scaling checkpoints on chemical biology and phenotype–disease.
Columns from 0.5 h to 12 h are internal best-validation metrics reconstructed from the agent’s
internal search trace; “Test 2 h” and “Test 12 h” are hidden-test normalized scores from the default
and 12-hour evaluated submissions.
Task 0.5 h 1 h 2 h 3 h 6 h 12 h Test 2 h Test 12 h
chemical biology
bace1-binding-affinity 0.000 0.850 0.850 0.850 0.850 0.856 0.903 0.920
cell-painting-perturbation 0.998 0.998 0.998 0.998 0.998 1.000 0.763 1.000
cyp-inhibition-multi-label 0.860 0.860 0.876 0.876 0.885 0.897 0.862 0.891
egfr-binding-affinity 0.821 0.821 0.835 0.835 0.849 0.851 0.902 0.924
gpcr-binding-multi-class 0.957 0.960 0.962 0.962 0.962 0.968 0.937 0.939
herg-binding-affinity 0.754 0.780 0.804 0.804 0.804 0.806 0.879 0.902
kinase-selectivity-multi-label 0.898 0.923 0.928 0.928 0.928 0.928 0.903 0.917
tox21-sr-are 0.000 0.815 0.827 0.843 0.849 0.853 0.807 0.867
chemical-biology mean 0.661 0.876 0.885 0.887 0.891 0.895 0.869 0.920
phenotype–disease
alzheimers-disease-staging 0.240 0.240 0.240 0.240 0.301 0.301 0.571 0.577
autism-diagnosis 0.707 0.891 0.912 0.912 0.912 0.924 0.595 0.607
breast-cancer-subtype 0.000 0.617 0.621 0.627 0.627 0.627 0.601 0.722
covid19-severity-classification 0.226 0.236 0.236 0.236 0.236 0.236 0.118 0.084
diabetes-readmission 0.463 0.466 0.466 0.466 0.466 0.466 0.470 0.461
genotype-to-phenotype 0.396 0.669 0.669 0.669 0.669 0.695 0.870 0.880
pan-cancer-survival-prediction 0.000 0.781 0.799 0.806 0.806 0.807 0.790 0.787
spatial-immune-infiltration 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
phenotype–disease mean 0.254 0.487 0.493 0.494 0.502 0.507 0.502 0.515
could use standard scientific Python/R libraries, installed open-source tools, and their prior domain
knowledge. We evaluated all human submissions with the same official task evaluators and score
normalization used for agent submissions.
Based on the main leaderboard, we compare the human pilot against the four strongest agent methods:
GPT-5.4, MLEvolvege, Gemini-3.1-Pro, and STELLAcla+ge. The human normalized score on this
pilot subset is0.839, 1.7 percentage points higher than the best agent on this subset, GPT-5.4, which
scores 0.822 on the same 10 tasks; Gemini-3.1-Pro, MLEvolvege, and STELLAcla+ge score 0.818,
0.817, and 0.805, respectively. Per-task scores are listed in Table A31. The human–agent gap is
small overall: agents match or exceed humans on several network, perturbation, phenotype, sequence,
and single-cell tasks, while humans retain their clearest margins on selected chemical-biology and
text-integrated tasks.
The ordering among the four agents on this 10-task pilot should be interpreted cautiously. MLEvolvege
uses Gemini-3.1-Pro as its backbone, yet its pilot mean is 0.817, essentially tied with the bare Gemini-
3.1-Pro baseline at 0.818. This 0.001 difference is far smaller than the across-task standard deviations
in Table A31, and does not indicate a scaffold-level disadvantage. Similarly, STELLAcla+ge scores
0.805 on this subset despite being a strong agent in the full benchmark. Small pilot subsets can favor
direct generation on some tasks, while search-based or multi-agent scaffolds may spend budget on
candidate exploration, validation choices, or coordination that does not always improve the final
submission for every task. For agent ranking and scaffold comparison, we therefore treat the full
76-task leaderboard and ablations as the primary evidence, and use this pilot mainly to contextualize
agent performance relative to human biomedical ML researchers.
A5 Discussion, Limitations, and Future Work
This section expands the concise discussion in § 4. We first clarify the benchmark scope, then discuss
limitations and future maintenance, operational reliability, contamination controls, ethics, broader
impact, and our use of LLMs during manuscript preparation.
58

## Page 59

Table A31:Human–agent comparison.Normalized hidden-test scores on the 10-task pilot for
human experts and four leading agents. The bottom row reports mean ± sample std over the 10 tasks.
Task STELLA cla+ge MLEvolvege Gemini-3.1-Pro GPT-5.4 Human
chemical-biology/cyp-inhibition-multi-label 0.891 0.862 0.898 0.9190.929
chemical-biology/gpcr-binding-multi-class 0.937 0.937 0.933 0.8940.945
network-biology/go-function-multi-label 0.496 0.5080.5130.506 0.499
network-biology/synthetic-lethality-prediction 0.967 0.971 0.966 0.9580.973
perturbation-dynamics/cancer-drug-sensitivity 0.959 0.972 0.9560.9740.972
phenotype-disease/breast-cancer-subtype 0.684 0.601 0.7040.7320.723
phenotype-disease/pan-cancer-survival-prediction 0.7770.7900.777 0.703 0.785
sequence/variant-effect-pathogenicity 0.4580.5920.472 0.579 0.582
single-cell/cell-type-from-expression 0.918 0.9961.000 1.000 1.000
text-integrated/gene-expression-classification 0.960 0.945 0.961 0.9500.981
mean±std0.805±0.1950.817±0.1840.818±0.1950.822±0.1780.839±0.182
A5.1 Scope and Intended Use
BioXArena is designed to measure dry-lab BioML coding: agents must load biomedical data,
build train/validation pipelines, fit predictive models, and submit held-out predictions. It does not
directly measure scientific ideation, literature synthesis, protocol design, or wet-lab execution, which
are important but different parts of biomedical research automation. This narrower scope keeps
agent comparisons fair and evaluator-based, while making BioXArena one component of a broader
biomedical-agent evaluation stack rather than a complete measure of research autonomy on its own.
A5.2 Limitations and Future Maintenance
Current coverage is broad but not exhaustive. First, BioXArena omits or sparsely covers important
biomedical data types and modalities, such as spatial omics, whole-slide pathology, raw microscopy
time series, flow cytometry, mass spectrometry, wearable signals, longitudinal EHR, and wet-lab
automation logs. Second, its 9 domains and 76 tasks cannot cover the full BioML problem space,
so future versions should add new domains and deepen task coverage within existing domains.
Third, we do not yet include very large production-scale tasks that require multi-day training,
distributed compute, or extensive data-engineering workflows. The current 2-hour budget is a
pragmatic evaluation choice: the scaling study shows that strong agents already obtain a useful
signal within this window, while the limit keeps repeated evaluation feasible across many systems.
Future releases should add more BioML, data-science, and general coding agents; expand longer-
budget evaluation for larger production-scale tasks; deepen human-expert comparisons; and invite
community contributions for under-represented diseases, populations, organisms, modalities, and data
formats. We therefore view BioXArena as a living benchmark whose updates should be versioned,
documented, and auditable rather than silently replacing earlier leaderboards.
A5.3 Reliability and Operating Cost
The main bottleneck is not simply model choice: many failures occur before a valid submission
reaches the evaluator. This suggests that near-term BioML-agent progress depends on stronger
execution control, data validation, and recovery from format or ID-order errors, especially for multi-
modal tasks with native biomedical file formats. Full leaderboard runs remain computationally
expensive, so we provide a smaller dev split, cached predictions, reproducible environments, and cost
accounting in App. A2.6 and App. A4.6.
A5.4 Contamination and Evaluator Integrity
Many source datasets, including TDC, OpenProblems, ProteinGym, Kaggle tasks, and HAM10000,
are public and may appear in LLM pre-training corpora. A strong score could therefore reflect
genuine task solving, memorized dataset-specific conventions, or copied solution patterns. We reduce
this risk by re-splitting train/test sets with task-appropriate leakage controls, holding out private labels
and evaluator code, and logging solution trajectories for later audit, following the same motivation
as MLE-bench’s plagiarism-checking practice [ 12]. The audit can normalize final solution code,
remove superficial formatting differences, compare token or syntax fingerprints within each task, and
59

## Page 60

manually inspect pairs that exceed a pre-specified similarity threshold. This diagnostic is designed to
flag near-duplicate solution code or unusually similar execution trajectories; it does not prove that a
model has or has not seen a public dataset during pre-training. Contamination remains a structural
concern for public-data benchmarks, so future submissions should report both benchmark score and
any detected contamination signal.
A5.5 Ethics, Privacy, and Bias
Several tasks use clinically sensitive resources such as TCGA, METABRIC, LIDC, HAM10000,
ABIDE, and ECG-QA. Public capsules contain only de-identified or license-compatible data, and
tasks requiring data-use agreements are marked so that submitters can follow institutional access
rules. The benchmark is intended for agent evaluation, not diagnosis, treatment selection, or clinical
deployment. Because source datasets can under-represent populations, geographies, and non-human
biology, leaderboard gains should not be interpreted as broad biomedical validity without external
validation; full source-level licensing details are in App. A2.4.
A5.6 Broader Impact
A multi-domain BioML benchmark can make agent claims more falsifiable and reduce over-claiming
from narrow demonstrations, but it can also encourage over-fitting to a fixed task set. We therefore
release task capsules, evaluators, traces, and versioned leaderboards so that future submissions can be
compared under the same protocol and so that benchmark updates can be documented explicitly.
A5.7 Use of LLMs
In compliance with the NeurIPS LLM-usage policy, LLM assistants were used during manuscript
preparation for drafting support, language polishing, figure and table layout suggestions, LaTeX
cleanup, and non-substantive consistency checks. They were not used to generate held-out labels,
alter official evaluator code, fabricate experimental results, or replace author verification. All reported
task definitions, scores, analyses, figures, references, and release statements were checked by the
authors against the underlying data, code, logs, and evaluation outputs before submission. This
disclosure concerns the use of LLMs in preparing the paper and is separate from the LLM agents that
are themselves evaluated as experimental subjects in BioXArena.
A6 Full Task Descriptions
The preceding catalogue tables summarize task metadata and input modalities in App. A2.1. Below
we provide the full domain-organized task descriptions. Each paragraph expands the task overview
and clarifies what the public inputs contain and what the submission file is expected to predict.
Domain-organized task descriptions
A6.1 Chemical Biology
DTI BindingDB BACE1: Binding Affinity Regression (bace1-binding-affinity).Predict the
binding affinity of small molecules against Beta-secretase 1 (BACE1). BACE1 is an aspartyl protease
responsible for the cleavage of amyloid precursor protein (APP), producing amyloid-beta peptides
that aggregate into plaques in Alzheimer’s disease. Quantifying binding affinity enables prioritization
of drug candidates by potency, which is more informative than binary active/inactive classification.
Inputs includeSMILES (text).Outputs requireaffinity (float).
Cell Painting Compound Perturbation Matching ( cell-painting-perturbation).Predict
which compound perturbation was applied to cells based on multi-channel Cell Painting morphologi-
cal profiles. Given well-level feature profiles extracted from 5 fluorescence imaging channels, predict
the compound identity for each test well. This multi-modal task requires integrating morphology from
distinct cellular compartments (nucleus, endoplasmic reticulum, RNA, actin/Golgi/plasma membrane,
mitochondria) with well and plate metadata to distinguish ~302 different chemical perturbations.
Inputs includeDNA channel (169 features), ER channel (120 features), RNA channel (118 features),
AGP channel (109 features), Mito channel (86 features).Outputs requirePerturbation prediction.
60

## Page 61

CYP Enzyme Inhibition Multi-Label Prediction ( cyp-inhibition-multi-label).Predict
whether small molecules inhibit each of five major cytochrome P450 (CYP) enzymes. CYP enzymes
are responsible for metabolizing approximately 75% of all drugs. Inhibition of these enzymes can
lead to dangerous drug-drug interactions, making CYP inhibition profiling a critical step in drug safety
assessment.Outputs requireCYP3A4 - Metabolizes ~50% of all drugs; most clinically significant
CYP isoform, CYP2D6 - Metabolizes ~25% of drugs; highly polymorphic across populations,
CYP2C9 - Important for warfarin and NSAID metabolism, CYP2C19 - Key enzyme for proton pump
inhibitors and clopidogrel.
DTI BindingDB EGFR: Binding Affinity Regression (egfr-binding-affinity).Predict the
binding affinity of small molecules against Epidermal Growth Factor Receptor (EGFR). EGFR is
a receptor tyrosine kinase that drives cell proliferation and is a major target in non-small cell lung
cancer and colorectal cancer therapy. Drugs like gefitinib, erlotinib, and osimertinib target EGFR.
Accurate affinity prediction accelerates the discovery of next-generation EGFR inhibitors.Inputs
includeSMILES (text).Outputs requireaffinity (float).
GPCR Binding Multi-Class Classification ( gpcr-binding-multi-class).Classify small
molecules by the class of G protein-coupled receptor (GPCR) they bind to. GPCRs are the largest
superfamily of membrane receptors and represent the most common target class for approved drugs.
Understanding which GPCR class a compound targets is fundamental for drug discovery and pharma-
cological profiling.Outputs requireClass_A - Rhodopsin-like receptors (the largest GPCR family),
Class_B - Secretin receptor family, Class_C - Metabotropic glutamate/pheromone receptors.
DTI BindingDB hERG: Binding Affinity Regression (herg-binding-affinity).Predict the
binding affinity of small molecules against the hERG (human Ether-a-go-go-Related Gene) potassium
channel. hERG channel inhibition can cause fatal cardiac arrhythmias (QT prolongation), making
hERG liability screening a critical safety checkpoint in drug development. Predicting binding affinity
quantitatively, rather than just pass/fail, enables better risk assessment and compound optimization.
Inputs includeSMILES (text).Outputs requireaffinity (float).
Kinase Selectivity Multi-Label Prediction (kinase-selectivity-multi-label).Predict the
inhibition activity of small molecules against a panel of eight clinically relevant kinases. Kinase
selectivity profiling is essential in drug discovery to identify compounds that selectively target
disease-relevant kinases while minimizing off-target effects that lead to toxicity.Outputs require
EGFR - Epidermal Growth Factor Receptor, ABL1 - Abelson Tyrosine-Protein Kinase 1, SRC -
Proto-Oncogene Tyrosine-Protein Kinase Src, CDK2 - Cyclin-Dependent Kinase 2.
Tox21 SR-ARE: Oxidative Stress Toxicity Prediction (tox21-sr-are).Predict whether a small
molecule activates the Antioxidant Response Element (ARE) signaling pathway, as measured in the
Tox21 stress response (SR) panel. The ARE pathway is regulated by the Nrf2 transcription factor and
is activated in response to oxidative stress. Compounds that activate SR-ARE may induce cellular
stress responses, which is relevant for toxicity assessment in drug development and environmental
chemical screening.Inputs includeSMILES.Outputs requireBinary classification.
A6.2 Imaging
AMOS: Abdominal Multi-Organ Segmentation (amos-organ-segmentation).Segment 15 ab-
dominal organs from 3D CT and MRI volumes. This is a multi-modal 3D medical image segmentation
task that requires understanding both CT and MRI imaging modalities, handling variable volume
sizes, and using metadata when helpful to produce voxel-level predictions for multiple anatomical
structures. The task evaluates an agent’s ability to build and train 3D segmentation models on real
clinical data.Inputs include3D Image (CT or MRI NIfTI .nii.gz, must be used as input, indexed by
image_file + image_dir), Table, Label files (train only).Outputs require3D segmentation masks.
Drug MOA Prediction ( drug-moa-prediction).Predict the mechanism of action (MOA) of
compounds from fluorescence microscopy images of drug-treated MCF-7 breast cancer cells. Given
a 3-channel fluorescence image (DAPI/Tubulin/Actin) combined with the compound name and
concentration, classify the compound into one of 7 MOA categories. The dataset uses a "Not Same
Compound" (NSC) evaluation strategy in which test compounds are structurally distinct from training
compounds, requiring the model to generalize from cellular morphology rather than memorizing
compound identities.Inputs includeImage (3-channel fluorescence JPEG, images/, must be used as
61

## Page 62

input, indexed by image_path), Table.Outputs requireActin disruptors, Aurora kinase inhibitors,
DMSO, DNA replication.
Label-Free Cell Counting (labelfree-cell-counting).Predict the number of cells in label-free
phase contrast microscopy images from the LIVECell dataset. All images are 520
times704 pixels captured across 8 cell lines over a 3.5-day time course (imaged every 4 hours). The
task combines visual cell detection with experimental metadata, including cell type, time elapsed
since seeding, well position, and plate information, to predict cell counts. This captures the practical
need for automated cell counting in high-throughput biology experiments.Inputs includeImage
(phase contrast TIF, images/, must be used as input, indexed by image_path), Table.
Lung Nodule Malignancy Prediction (LIDC-IDRI) (lung-nodule-malignancy).Predict the
malignancy level of lung nodules from 3D CT image crops combined with radiologist-annotated
semantic features and patient demographics. Given a 3D CT patch centered on a lung nodule
along with clinical metadata, predict the nodule’s malignancy on a 1-5 scale. This multi-modal task
integrates 3D volumetric imaging with structured clinical and radiological features for lung cancer
risk assessment.Inputs include3D Image (multi-slice PNG, nodule_images/, must be used as input,
indexed by image_path), Table.Outputs requireMalignancy level (integer 1-5).
Mitochondria Instance Counting in Electron Microscopy (MitoEM)
(mitochondria-counting).Predict the number of mitochondria instances in electron mi-
croscopy (EM) image patches from human and rat brain tissue. Given a 512
times512 grayscale EM image and the species of origin, estimate the count of individual
mitochondria in the field of view. This task evaluates the ability to detect and count organelles
in high-resolution ultrastructural imaging data, combining visual analysis with species-specific
morphological priors.Inputs includeImage (grayscale EM TIFF, images/, must be used as input,
indexed by image_path), Table.Outputs requiren_instances (integer).
Nucleus Type Classification (nucleus-type-classification).Predict the dominant nucleus
type in H&E-stained histopathology image patches from the PanNuke dataset. Given a tissue patch
image containing nuclei of multiple types (neoplastic, inflammatory, connective, dead, epithelial)
along with the tissue source and total nucleus count, classify which nucleus type is most prevalent.
The task requires visual analysis of nuclear morphology combined with tissue context, for example,
neoplastic nuclei dominate in tumor regions while inflammatory nuclei dominate in immune-infiltrated
areas.Inputs includeImage (H&E JPEG, images/, must be used as input, indexed by image_path),
Table.Outputs requireneoplastic, inflammatory, connective, dead.
Skin Lesion Diagnosis (HAM10000) (skin-lesion-diagnosis).Classify dermatoscopic images
of skin lesions into 7 diagnostic categories using both the image and clinical metadata. This is a
multi-modal task combining visual features from high-resolution dermatoscopy images with patient
demographics and clinical context. Distinguishing melanoma from benign lesions is clinically critical
because early detection significantly improves survival.Inputs includeImage (dermatoscopy RGB
JPG, images/, must be used as input, indexed by image_path), Table.Outputs requireMulti-class
classification.
Virtual Staining: IHC Positive Ratio Prediction (virtual-staining).Predict the immunohisto-
chemistry (IHC) positive tissue fraction from H&E-stained histopathology images. Given an H&E
tissue patch and the target IHC stain type, predict what proportion of the tissue would stain positive
under that IHC biomarker. This simulates "virtual staining", using AI to estimate IHC results from
routine H&E slides, potentially reducing the need for expensive and time-consuming IHC procedures
in clinical pathology.Inputs includeImage (H&E JPG 1024
times1024, images/, must be used as input, indexed by he_image_path), Table.Outputs require
positive_ratio (float, 0.0–1.0).
A6.3 Network Biology
Gene-Disease Association Strength Prediction (DisGeNET) ( gene-disease-association).
Predict the strength of association between a gene and a disease. Given gene-level features (genomic
properties, expression across tissues, evolutionary conservation) and disease-level features (preva-
lence, inheritance pattern, number of associated genes), predict the DisGeNET association score, a
continuous value (0–1) integrating multiple evidence sources. This task evaluates the ability to learn
62

## Page 63

patterns of gene-disease relationships from heterogeneous biological features.Inputs includeTable.
Outputs requiredisgenet_score (float, 0.0–1.0).
GO Function Multi-Label Prediction ( go-function-multi-label).Predict Gene Ontology
(GO) biological process annotations for proteins. Given a protein sequence and identifiers, predict
which of 15 GO biological process terms are associated with each protein in a multi-label classification
setting.Inputs includeSequence (protein_sequence), Table.Outputs requireGO_0006915 through
GO_0006886 (float, 0.0–1.0).
Metabolic Network Enzyme-Reaction Prediction (KEGG) (metabolic-network-kegg).Pre-
dict whether an enzyme catalyzes a given biochemical reaction in the KEGG metabolic network.
Given an enzyme sequence, EC classification hierarchy, and pathway metadata, classify whether
the enzyme-reaction pair represents a true catalytic relationship.Inputs includeSequence (en-
zyme_sequence), Table.Outputs requirelabel (binary, 0 or 1).
Pathway Membership Classification (Reactome) (pathway-membership-reactome).Predict
the Reactome pathway category that a protein belongs to. Given a protein sequence and tissue
expression profiles, classify each protein into one of 8 pathway categories.Inputs includeSequence
(protein_sequence), Table.Outputs requirelabel (categorical, 8 classes).
Protein-Protein Interaction Prediction (STRING) (ppi-prediction-string).Predict whether
two proteins physically or functionally interact based on their sequences and network topology
features. Given a pair of protein sequences along with graph-derived features from the STRING PPI
network, classify whether the pair represents a true interaction.Inputs includeSequence (sequence_a,
sequence_b), Table.Outputs requirelabel (binary, 0 or 1).
Protein Complex Classification (CORUM) (protein-complex-corum).Predict the protein com-
plex category a protein belongs to from the CORUM database. Given a protein sequence and
identifiers, classify each protein into one of 10 complex categories.Inputs includeSequence
(protein_sequence), Table.Outputs requirelabel (categorical, 10 classes).
Synthetic Lethality Prediction (synthetic-lethality-prediction).Predict whether a pair of
genes exhibits synthetic lethality, where simultaneous loss of both genes leads to cell death while loss
of either gene alone is viable. Given two gene sequences along with expression profiles, network
topology, essentiality features, and PPI pair features, classify whether the gene pair is synthetic lethal.
Inputs includeSequence (sequence_a, sequence_b), Table.Outputs requirelabel (binary, 0 or 1).
TF Regulatory Network Prediction (ENCODE) (tf-regulatory-prediction).Predict tran-
scription factor (TF) to target gene regulatory relationships using ENCODE-derived features. Given
a TF sequence, ChIP-seq binding evidence, motif scores, genomic distance, and network degree
features, classify whether the TF regulates the target gene.Inputs includeSequence (tf_sequence),
Table.Outputs requirelabel (binary, 0 or 1).
A6.4 Perturbation Dynamics
Cancer Drug Sensitivity ( cancer-drug-sensitivity).Predict the sensitivity of cancer cell
lines to drug compounds, measured as the natural log of the half-maximal inhibitory concentration
(ln_ic50). Given cell line characteristics, drug properties, and dose-response metadata, predict the
continuous drug sensitivity value.Inputs includecell_line, cosmic_id, cancer_type, drug_name,
drug_id.Outputs requireln_ic50.
CRISPR Perturbation Prediction (crispr-perturbation-prediction).Predict the transcrip-
tional response to CRISPR genetic perturbations. Given a perturbation (gene knockout or combina-
tion), predict the change in gene expression over local gene chunks.Inputs includeperturbation,
genes, is_combination, n_cells, mean_expr_pc.Outputs requiredelta_expression.
Drug Transcriptional Response ( drug-transcriptional-response).Predict the transcrip-
tional response of cells to drug perturbations at specific doses and in specific cell lines. Given a
drug, dose, and cell line, predict the change in gene expression (delta expression) across 5,000 genes.
Inputs includeperturbation, dose, cell_line, is_control, n_cells.Outputs requiredelta_expression.
ECCITE-seq Multi-modal CRISPR Perturbation Response
(eccite-multimodal-perturbation).Predict how a CRISPR perturbation changes both
63

## Page 64

RNA and protein expression in single cells. The ECCITE-seq (Expanded CRISPR-compatible
Cellular Indexing of Transcriptomes and Epitopes by sequencing) dataset profiles THP-1 monocytic
leukemia cells treated with 111 guide RNAs targeting immune checkpoint regulators. This is a
genuinely multi-modal perturbation response prediction task: given an sgRNA perturbation identity
and a cell’s baseline state, predict the resulting transcriptional and protein-level changes.Inputs
includesgRNA identity, baseline RNA expression, baseline protein expression (ADT), cell metadata.
Outputs requiredelta_rna, delta_protein.
Gene Regulatory Network Inference ( gene-regulatory-network-inference).Infer gene
regulatory edges from single-cell expression data and pseudotime information. Given expression
matrices and pseudotime orderings for cells, predict the probability that a regulatory relationship
exists between each pair of genes.Inputs includedataset_name, dataset_type, n_cells, n_genes,
gene_names.Outputs requireid, prediction.
Multi-Timepoint Perturbation (multi-timepoint-perturbation).Predict time-resolved tran-
scriptional responses to drug perturbations. Given a drug, cell line, and dose, predict the change in
gene expression (delta expression) across 978 landmark genes at each measured time point.Inputs
includedrug, cell_line, dose, time_points, n_time_points.Outputs requiredelta_expression.
RNA Velocity Cell Transition ( rna-velocity-cell-transition).Predict unspliced RNA
counts from spliced RNA counts for individual cells. This task captures the relationship between
mature (spliced) and nascent (unspliced) mRNA, which is fundamental to RNA velocity estimation
and understanding cell state transitions.Inputs includecell_id, cell_type, cell_type_coarse, spliced,
umap.Outputs requireunspliced.
Spear-ATAC Chromatin Accessibility Perturbation Response (spear-atac-perturbation).
Predict how CRISPR perturbations alter chromatin accessibility profiles in single cells. The Spear-
ATAC dataset combines single-cell ATAC-seq with CRISPR guide RNA capture in K562 chronic
myelogenous leukemia cells. This is an epigenomic perturbation response task: given a guide RNA
perturbation, predict the change in chromatin accessibility across genomic peaks. This complements
RNA-based perturbation tasks by operating at the epigenomic level.Inputs includesgRNA identity,
Baseline accessibility, Cell-level metadata features, Compressed accessibility embedding, Feature
representations (5 types available).Outputs requiredelta_accessibility.
A6.5 Phenotype–Disease
Alzheimer’s Disease Staging (alzheimers-disease-staging).Predict the Alzheimer’s disease
neuropathological change (ADNC) stage from single-nucleus gene expression profiles. Using the
SEA-AD (Seattle Alzheimer’s Disease) atlas, which contains multiome (snRNA-seq + snATAC-seq)
data from 84 donors spanning the full spectrum of AD pathology, the task is to classify each cell into
one of four ADNC categories: "Not AD", "Low", "Intermediate", or "High".Inputs includeTable
(Parquet format; use pd.read_parquet(’train.parquet’) / pd.read_parquet(’test.parquet’)).Outputs
requireMulti-class classification.
Autism Spectrum Disorder Diagnosis (ABIDE) (autism-diagnosis).Predict autism spectrum
disorder (ASD) diagnosis from brain imaging quality metrics and phenotypic data. Using the ABIDE
(Autism Brain Imaging Data Exchange) consortium dataset, which aggregates resting-state fMRI and
structural MRI data from multiple sites worldwide, the task requires distinguishing ASD individuals
from typical controls. A key challenge is handling cross-site variability because training and test data
come from different imaging centers with different scanners and protocols.Inputs includeTable.
Outputs requirediagnosis (text).
Breast Cancer Molecular Subtype Classification (METABRIC) ( breast-cancer-subtype).
Predict the molecular subtype of breast cancer from clinical features and gene expression profiles.
Molecular subtyping is central to breast cancer treatment planning because different subtypes respond
to different therapies (hormone therapy for luminal, targeted therapy for HER2+, chemotherapy for
basal). Given clinical characteristics and expression of 200 highly variable genes, classify each tumor
into one of 7 PAM50+claudin-low subtypes.Inputs includeTable.Outputs requiresubtype (text).
COVID-19 Severity Classification (covid19-severity-classification).Predict the clinical
severity of COVID-19 patients from single-cell RNA sequencing data. The dataset contains approx-
imately 647,000 cells from patients across five severity categories. This task evaluates the ability
64

## Page 65

to classify disease severity from high-dimensional transcriptomic profiles, which is essential for
understanding immune response heterogeneity and developing severity-predictive biomarkers.Inputs
includeTable (Parquet format; use pd.read_parquet(’train.parquet’) / pd.read_parquet(’test.parquet’)).
Outputs requireMulti-class classification.
Diabetes Hospital Readmission Prediction (diabetes-readmission).Predict whether a diabetes
patient will be readmitted to the hospital within 30 days, after 30 days, or not at all. Using 10 years of
clinical care data from 130 US hospitals, the task integrates patient demographics, diagnoses, medica-
tions, and laboratory results to predict readmission risk. Reducing preventable readmissions is a major
healthcare quality goal because accurate prediction enables targeted post-discharge interventions.
Inputs includeTable.Outputs requirereadmitted (text).
Genotype to Phenotype: Gene Expression Prediction (genotype-to-phenotype).Predict gene
expression levels from genotype principal components and transcriptomic context. Given a donor’s
genetic background (20 genotype PCs), demographic info (sex), and expression levels of 10 context
genes, predict the expression of a target gene. This task evaluates the ability to model genotype-to-
phenotype relationships, a core challenge in functional genomics and personalized medicine.Inputs
includeTable.Outputs requireexpression (float).
Pan-Cancer Survival Prediction (pan-cancer-survival-prediction).Predict patient survival
risk scores from clinical and molecular features across 33 TCGA cancer types. Given clinical
metadata (cancer type, age, gender, pathological staging) and gene expression profiles (top 100
most variable genes), estimate a risk score that ranks patients by their survival prognosis. This is a
fundamental challenge in precision oncology: identifying high-risk patients who may benefit from
more aggressive treatment.Inputs includeTable.Outputs requirerisk_score (float).
Spatial Immune Infiltration Prediction (spatial-immune-infiltration).Predict the expres-
sion levels of six key immune marker genes at each spatial spot in breast cancer tissue sections.
Using 10x Visium spatial transcriptomics data, the task requires integrating high-dimensional gene
expression profiles, spatial coordinates, and H&E histology images to predict immune cell infiltration
patterns. Understanding spatial immune infiltration is critical for characterizing the tumor microenvi-
ronment and predicting immunotherapy response.Inputs includefiltered_count_matrices/, spatial/,
metadata/.Outputs requireMulti-output regression.
A6.6 Sequence
Gene Tissue Expression Prediction (gene-tissue-expression).Predict gene expression levels
across human tissues. Given a gene identifier and a target tissue, predict the log-transformed
expression level (log2 TPM). This task evaluates the ability to learn gene-tissue expression patterns,
namely which genes are expressed in which tissues and at what levels, a fundamental question in
functional genomics.Inputs includeTable, Sequence (FASTA, gene_sequences.fasta, must be used
as input, indexed by gene_id).Outputs requirelog2_tpm (float).
RNA Isoform Expression Prediction (isoform-expression).Predict transcript isoform expres-
sion levels across 30 human tissues. Given a transcript’s RNA and protein sequences along with
genomic context (chromosome, position, strand), predict tissue-specific expression patterns. This
task evaluates the ability to learn sequence-to-expression relationships, including how RNA/protein
sequence features determine where and how much a transcript is expressed.Inputs includeTable
(train.csv / test.csv).Outputs requireMulti-output regression.
Multi-TF Binding Prediction (multi-tf-binding).Predict whether a transcription factor (TF)
binds to a given genomic region in a specific cell type. Given a candidate regulatory element, a
TF name, and a cell type, predict the binary binding status. This task evaluates the ability to learn
context-dependent TF binding patterns that integrate genomic location, TF identity, and cellular
context, which is fundamental to understanding transcriptional regulation.Inputs includeTable.
Outputs requirebinding (float).
Protein-Protein Interaction Prediction (protein-protein-interaction).Predict whether two
proteins physically interact based on their amino acid sequences. The dataset is derived from the HuRI
(Human Reference Interactome) project, which provides experimentally validated binary protein-
protein interactions determined through systematic yeast two-hybrid screening.Inputs includeid,
ensp_A, ensp_B, protein_seq_A, protein_seq_B.Outputs requireBinary classification.
65

## Page 66

Regulatory Element Detection ( regulatory-element-detection).Classify candidate cis-
regulatory elements (cCREs) into functional categories based on their genomic coordinates. Given a
genomic region defined by chromosome, start, end, and length, predict the type of regulatory element
it represents. This task evaluates the ability to learn the relationship between genomic location and
regulatory function, a key problem in understanding gene regulation and non-coding genome function.
Inputs includeTable.Outputs requirelabel (str).
Remote Homology Similarity Prediction (remote-homology-detection).Predict the structural
similarity (TM-score) between pairs of protein domains based on their sequences. Remote homol-
ogy detection identifies evolutionarily related proteins that have diverged beyond easily detectable
sequence similarity, which is critical for functional annotation of uncharacterized proteins.Inputs
includeTable (train.csv / test.csv), Sequence (FASTA, cath-domain-seqs.fa, must be used as input,
indexed by chain_1 / chain_2).Outputs requireRegression.
RNA-Protein Binding Affinity Prediction (rna-protein-binding-affinity).Predict the bind-
ing affinity score between RNA sequences and RNA-binding proteins (RBPs) from RBNS (RNA
Bind-n-Seq) experiments. RNA-protein interactions are fundamental to post-transcriptional gene
regulation, and quantifying binding affinity is crucial for understanding RNA biology.Inputs include
id, protein_id, rna_seq, concentration, protein_seq.Outputs requireRegression.
RNA-Protein Binding Signal Prediction (rna-protein-binding-signal).Predict the contin-
uous eCLIP binding signal score for RNA-protein interactions. eCLIP (enhanced CrossLinking
and ImmunoPrecipitation) provides genome-wide maps of RNA-binding protein binding sites at
near-nucleotide resolution. This task involves predicting the binding signal intensity from RNA
sequence and genomic context.Inputs includeid, cell_line, protein_id, protein_seq, chrom.Outputs
requireRegression.
RNA Reactivity Imputation (rna-reactivity-imputation).Impute missing RNA chemical
reactivity values from partially observed icSHAPE in-vivo probing data. Chemical probing experi-
ments measure RNA structure but often produce incomplete data due to experimental limitations.
Accurate imputation of missing reactivity values enables more complete RNA structural analysis.
Inputs includeid, rna_id, sequence, observed_values, observed_mask.Outputs requireRegression.
Variant Effect Pathogenicity Prediction (variant-effect-pathogenicity).Predict the clin-
ical pathogenicity of single nucleotide variants (SNVs). Given a variant’s genomic location, gene
context, and annotation metadata, classify it as Pathogenic, Benign, or a Variant of Uncertain Signifi-
cance (VUS). This task evaluates the ability to integrate genomic position, allele identity, and clinical
annotation to assess variant pathogenicity, a central challenge in clinical genetics and precision
medicine.Inputs includeTable.Outputs requirelabel (str).
A6.7 Single Cell
Cross-Batch Cell Type Classification (batch-integration).Predict cell types for single cells
from unseen batches. Given a training set of cells with known cell type annotations from 45 batches,
predict cell types for test cells from 11 held-out batches. This tests an agent’s ability to handle batch
effects, which are systematic technical variations between experiments that can confound biological
signals.Inputs includeTable (train.csv / test.csv).Outputs requirecell_type (text).
Cell Type Prediction from Expression (cell-type-from-expression).Predict cell types from
single-cell gene expression profiles in a tissue microenvironment context. Using scRNA-seq data
from human tissue samples with rich donor and biosample metadata, classify each cell into one of 7
cell types. Understanding cell type composition is a prerequisite for inferring cell-cell communication
networks because knowing which cells are present determines which ligand-receptor interactions are
possible.Inputs includeTable (train.csv / test.csv).Outputs requirecell_type (text).
Chromatin to Gene Expression Prediction (chromatin-to-expression).Predict gene expres-
sion (RNA) from chromatin accessibility (ATAC-seq) data at single-cell resolution. Given the
chromatin accessibility landscape across 116,490 peaks and peak DNA sequences for each cell, pre-
dict the expression levels of the top 50 genes. This task evaluates the ability to model the regulatory
relationship between chromatin state and transcription.Inputs includeTable (train.csv / test.csv).
Outputs requireGene expression prediction.
66

## Page 67

CITE-seq Protein Level Prediction (cite-seq-protein-prediction).Predict surface protein
abundance (ADT counts) from gene expression (RNA) and protein amino acid sequences. Given
single-cell RNA expression for 2,000 genes and the amino acid sequences of 134 target proteins,
predict the antibody-derived tag (ADT) count for each protein in each cell. This task tests the ability
to integrate transcriptomic data with protein sequence information for cross-modality prediction.
Inputs includeTable (train.csv / test.csv).Outputs requireADT count prediction.
Cross-Modality Cell Matching ( cross-modality-cell-matching).Match cells across two
single-cell modalities: scRNA-seq (gene expression) and scATAC-seq (chromatin accessibility).
Given unpaired measurements from the same set of cells, predict which RNA profile corresponds to
which ATAC profile. This is a permutation-prediction task where each RNA cell must be matched to
exactly one ATAC cell.Inputs includeTable (train.csv / test.csv).Outputs requireCell matching.
Cross-Modality Cell Type Classification (cross-modality-cell-type).Predict cell types from
multi-modal single-cell data (CITE-seq). The dataset contains paired RNA and protein (ADT)
measurements from PBMCs (peripheral blood mononuclear cells). Given both gene expression
(RNA) and surface protein (ADT) features for each cell, classify each cell into one of 27 cell type
categories (celltype_l2).Inputs includeTable (train.csv / test.csv).Outputs requireMulti-class
classification.
Developmental Stage Prediction ( developmental-stage-prediction).Predict the develop-
mental stage of retinal cells after correcting for batch effects across different experimental conditions.
The dataset contains single-cell RNA-seq data from retinal cells at various developmental stages,
measured across multiple batches. The task requires learning representations that capture biological
variation (developmental stage) while being invariant to technical batch effects.Inputs include
Gene expression (must be used as input, indexed by h5ad_row_idx column in metadata CSVs), Train
metadata (train_metadata.csv), Test metadata (test_metadata.csv).Outputs requireClassification.
Gene Expression Denoising (gene-expression-denoising).Denoise single-cell RNA sequenc-
ing count data by recovering true gene expression levels from noisy, dropout-affected measurements.
Single-cell sequencing suffers from high dropout rates where expressed genes appear as zeros due to
technical limitations. Given noisy count matrices, predict the underlying clean expression values for
50 highly variable genes.Inputs includeTable (train.csv / test.csv).Outputs requireMulti-output
regression.
Cell Type Label Projection (label-projection).Predict cell type labels for unseen cells using
a labeled reference dataset. Given a training set of single cells with known cell type annotations
from multiple batches, predict cell types for test cells from different batches. This is the most
common real-world task in single-cell analysis, transferring annotations from a reference atlas to new
experimental data. The key challenge is handling batch effects between training and test datasets.
Inputs includeTable (train.csv / test.csv).Outputs requirecell_type (text).
RNA to Protein Level Prediction (rna-to-protein-prediction).Predict surface protein (ADT)
levels from RNA gene expression. Given CITE-seq data where both RNA and protein are measured
in the same cells, train a model on paired RNA
toprotein data, then predict protein levels for test cells given only their RNA profiles. This cross-
modality prediction task evaluates the ability to learn the relationship between transcriptome and
proteome at single-cell resolution.Inputs includeTable (train.csv / test.csv).Outputs require
Multi-output regression.
A6.8 Structure
Complex Structure Evaluation (complex-structure-evaluation).Predict the quality of com-
putationally modeled protein complex structures. Given features of a predicted complex model and its
native reference structure, estimate the DockQ score, a composite quality metric for protein-protein
docking models.Inputs includeid, sample_id, target_id, model_id, group_code.Outputs require
dockq_avg.
Enzyme Commission Prediction (enzyme-commission-prediction).Predict the primary En-
zyme Commission (EC) class of a protein based on its sequence and structural features. The task is
simplified from full multi-label EC annotation to predicting the first-level EC number, which indicates
67

## Page 68

the general type of catalytic reaction.Inputs includeid, protein_id, protein_sequence.Outputs
requireec_class.
Protein Binding Site Detection (protein-binding-site-detection).Predict whether a protein
chain has high binding-site density. Given protein sequence information, classify each protein as
belonging to the top binding-density group versus the rest.Inputs includeid, protein_id, sequence,
sequence_length.Outputs require1 = protein is in the top 20% by binding-residue fraction
(binding_count / sequence_length), 0 = all other proteins.
Protein Fold Classification (protein-fold-classification).Predict the structural fold class
of a protein domain. Given the protein sequence, classify the domain into one of 1,195 fold categories
from the SCOPe database. The benchmark uses a rebuilt stratified split over fold labels to keep
the task learnable while still highly multi-class.Inputs includeid, protein_id, protein_sequence.
Outputs requirefold_label.
Protein-Ligand Binding Affinity (protein-ligand-binding-affinity).Predict the binding
affinity (pK value) of protein-ligand complexes. Given the protein sequence, 3D structural coordinates,
and ligand SMILES representation, estimate the binding strength as a continuous pK value.Inputs
includeid, complex_id, protein_sequence, ligand_smiles.Outputs requireaffinity_value.
Protein-Protein Interface ( protein-protein-interface).Predict the fraction of interface
residues in a protein-protein complex. Given structural and sequence information of a receptor-
ligand complex, estimate the proportion of residues that participate in the protein-protein interface.
Inputs includeid, complex_id, receptor_sequence, ligand_sequence, receptor_length.Outputs
requireinterface_fraction.
Protein Stability Change (protein-stability-change).Predict the change in thermodynamic
stability (ddG) caused by single amino acid mutations in proteins. Given the wild-type protein
sequence, structure, and mutation information, estimate the ddG value for one mutation at a time.
Inputs includeid, protein_id, variant_name, protein_sequence, num_residues.Outputs require
ddg.
Protein 3D Structure Prediction (protein-structure-prediction).Predict the 3D structure
of a protein from its amino acid sequence. Given a protein sequence, predict the C
alpha (alpha carbon) coordinates for each residue in 3D space. This is one of the most fundamental
and challenging problems in computational biology and was famously addressed by AlphaFold. The
task evaluates an agent’s ability to leverage structure prediction tools or build models that capture
the sequence-to-structure relationship.Inputs includeTable (train.csv / test.csv).Outputs require
coords_file (text).
A6.9 Text-Integrated
Biomedical Figure Visual Question Answering (PMC-VQA) (biomedical-figure-vqa).An-
swer multiple-choice questions about biomedical figures extracted from PubMed Central (PMC)
scientific articles. The PMC-VQA dataset contains biomedical images spanning radiology scans,
pathology slides, clinical photographs, molecular diagrams, and other scientific figures, each paired
with a figure caption, a clinically relevant question, and four answer choices (A/B/C/D). Given an
image, its caption, a question, and four choices, predict the correct answer. This task evaluates multi-
modal reasoning over diverse biomedical visual content and scientific text, requiring understanding
of medical imaging, biological diagrams, and clinical concepts.Inputs includeid, Figure_path,
Caption, Question, Choice A.
DNA Enzyme Function Classification (BioTalk) (dna-enzyme-function).Predict the Enzyme
Commission (EC) class for a gene given its DNA nucleotide sequence and contextual information.
Each sample pairs a DNA coding sequence (CDS) with metadata. Training data includes full
natural language descriptions of enzymatic activity; test data provides only enzyme names/synonyms
(reaction formulas, systematic names, and EC class hierarchy are masked). The goal is to predict the
level-3 EC class (e.g., EC3.2.2 from 3.2.2.6).Inputs includeid, sequence, description, ec_label, OC.
ECG Signal Question Answering (ECG-QA) (ecg-signal-qa).Answer clinical questions about
12-lead electrocardiogram (ECG) recordings. The ECG-QA dataset pairs PTB-XL ECG records with
template-generated natural language questions covering diagnosis verification, symptom identification,
68

## Page 69

rhythm classification, and comparative queries across multiple ECG leads. Given an ECG record
identifier and a natural language question, predict the correct answer from a fixed set of ~104 possible
answer classes. This task evaluates the ability to jointly reason over physiological signal data (12-lead
ECG waveforms) and natural language clinical queries, bridging cardiac electrophysiology with
language understanding.Inputs includeid, ecg_id, question, question_type, answer.
Gene Expression Classification (CellWhisperer) (gene-expression-classification).Deter-
mine whether a text description correctly matches a gene expression profile. Given a cell’s gene
expression features (top expressed genes and their normalized expression values) paired with a text
description (cell type, tissue, or disease label), predict whether the text accurately describes the cell.
This is a binary match/no-match classification task that evaluates the ability to bridge gene expression
data with natural language biological annotations, inspired by the CellWhisperer framework (Na-
ture Biotechnology, 2025).Inputs includeid, top_genes, top_expression_values, text_description,
dataset_source.
Medical Visual Question Answering (SLAKE) (medical-vqa).Answer open-ended clinical ques-
tions about medical radiology images. The SLAKE (Semantically-Labeled Knowledge-Enhanced)
dataset contains 642 radiology images (CT, MRI, X-ray) spanning five body regions (head, neck,
chest, abdomen, pelvis), each paired with multiple clinically relevant questions. This task evaluates
multi-modal reasoning: a model must jointly interpret the visual content of a medical image and a
natural language question to produce a correct short answer. Questions cover anatomy identifica-
tion, imaging modality recognition, abnormality detection, organ localization, and other diagnostic
concepts.Inputs includeid, question, image_path, answer.
Molecule Question Answering (MoleculeQA) (molecule-qa).Answer multiple-choice questions
about molecules given their SMILES (Simplified Molecular-Input Line-Entry System) representation.
The MoleculeQA dataset tests molecular understanding across four categories: property, structure,
source, and usage. Each question has four options (A, B, C, D) and the task is to select the
correct answer letter. This task evaluates the ability to reason about molecular properties, structural
features, biological origins, and practical applications from a chemical string representation, bridging
cheminformatics and natural language understanding.Inputs includeid, smiles, question, option_a,
option_b.
Pathology Visual Question Answering (PathVQA) (pathology-vqa).Answer questions about
pathology images. The PathVQA dataset contains pathology images sourced from medical textbooks
and the PEIR (Pathology Education Informational Resource) digital library, each paired with clinically
relevant questions. Given a pathology image and a natural language question, predict the correct short
answer. Questions cover pathological findings, tissue structures, staining patterns, organ identification,
disease processes, and diagnostic reasoning. This task evaluates multi-modal understanding at the
intersection of visual pathology interpretation and natural language comprehension.Inputs include
id, question, image_path, answer.
Protein-Function Text Matching (SwissProtCLAP) ( protein-function-matching).Deter-
mine whether a protein amino acid sequence matches a given functional text description. The
SwissProtCLAP dataset (from the ProteinDT project) contains protein sequences from UniProt/Swis-
sProt paired with their curated functional annotations. Positive pairs are true sequence-function
matches from the database; negative pairs are created by shuffling text descriptions to create mis-
matches (balanced 50/50). Given a protein sequence and a text description, predict the probability that
the description correctly describes the protein’s function. This binary classification task evaluates the
ability to bridge protein sequence representations with natural language biological annotations, a key
capability for automated protein function prediction.Inputs includeid, protein_id, protein_sequence,
text_description, label.
69
