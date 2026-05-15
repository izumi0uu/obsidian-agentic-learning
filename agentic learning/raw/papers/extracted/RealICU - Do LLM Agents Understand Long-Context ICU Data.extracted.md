# RealICU: Do LLM Agents Understand Long-Context ICU Data? A Benchmark Beyond Behavior Imitation - Extracted Text

- Source note: [[RealICU - Do LLM Agents Understand Long-Context ICU Data]]
- Source PDF: `assets/RealICU - Do LLM Agents Understand Long-Context ICU Data.pdf`
- Extracted: 2026-05-14
- Extractor: pypdf
- Pages: 35
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

RealICU: Do LLM Agents Understand Long-Context
ICU Data? A Benchmark Beyond Behavior Imitation
Chengzhi Shen1,2,10 Weixiang Shen1,2,3 Tobias Susetzky1,2
Chen (Cherise) Chen4 Jun Li1 Yuyuan Liu5 Xuepeng Zhang6
Zhenyu Gong7,† Daniel Rueckert1,2,8,9,10,† Jiazhen Pan1,2,9,†
1Technical University of Munich (TUM) 2TUM University Hospital 3LMU Munich
4University of Sheffield 5University of Oxford 6Zhongshan Hospital Fudan University
7Sun Yat-sen University Cancer Center 8Imperial College London
9Munich Center for Machine Learning (MCML)
10relAI – Konrad Zuse School of Excellence in Reliable AI
†Corresponding Authors
Abstract
Intensive care units (ICU) generate long, dense and evolving streams of clinical
information, where physicians must repeatedly reassess patient states under time
pressure, underscoring a clear need for reliable AI decision support. Existing ICU
benchmarks typically treat historical clinician actions as ground truth. However,
these actions are made under incomplete information and limited temporal con-
text of the underlying patient state, and may therefore be suboptimal, making it
difficult to assess the true reasoning capabilities of AI systems. We introduce
RealICU, a hindsight-annotated benchmark for evaluating large language models
(LLMs) under realistic ICU conditions, where labels are created after senior physi-
cians review the full patient trajectory. We formulate four physician-motivated
tasks: assessPatient Status,Acute Problems,Recommended Actions, andRed
Flagactions that risk unsafe outcomes. We partition each trajectory with 30-min
windows and release two datasets: RealICU-Gold with 930-window annotations
from 94 MIMIC-IV patients, and RealICU-Scale with 11,862 windows extended
byOracle, a physician-validated LLM hindsight labeler. Existing LLMs including
memory-augmented ones performed poorly on RealICU, exposing two failure
modes: a recall-safety tradeoff for clinical recommendations, and an anchoring
bias to early interpretations of the patient. We further introduce ICU-Evo to study
structured-memory agents that improves long-horizon reasoning but does not fully
eliminate safety failures. Together, RealICU provides a clinically grounded testbed
for measuring and improving AI sequential decision-support in high-stakes care.
Project page: chengzhi-leo.github.io/RealICU-Bench
1 Introduction
The Intensive Care Unit (ICU) is one of the most information-dense environments in the hospi-
tal. Within hours, a single patient can generate large volumes of laboratory results, vital signs,
medications, nursing observations, and imaging reports [ 20, 24]. Physicians must integrate this
evolving stream under time pressure, where each measurement captures only a partial slice of the
patient’s physiological state, and decisions made in one moment may shape outcomes hours or days
later [23, 27]. This underscores a clear need for AI decision support system in real-time monitoring
and decision-making in the ICU, which usually acts as a clinical co-pilot. In consultations with over
30 board-certified clinicians, including five senior ICU physicians who later served as annotators, four
Preprint.
arXiv:2605.13542v1  [cs.AI]  13 May 2026

## Page 2

`
Long-Context ICU Data Stream ICU Co-Pilot with Clinical Decision Support
Acute Problems
Major Concerns
INFECTION
SEPTIC SHOCK
LACTIC ACIDOSIS
Te mp . 38. 6°C
Pulmonary
Lactate 3.8
Red Flag Actions
Actions to Avoid
AGGRESSIVE DIURESIS
ETOMIDATE FOR INTUBATION
BETA-BLOCKERS
Hypovolemic, will worsen shock
Adrenal suppression
Compensatory tachycardia
Recommended Actions
Recommended Treatments
NOREPINEPHRINE
VASOPRESSIN
LACTATED RINGER’S
0.15 μg/kg/min
0.03 U/min IV
500 mL
Patient Status
IMPROVING STABLE DETERIORATING
Hemodynamics ↓  Deteriorating 
Oxygenation ↓  Deteriorating 
Inflammation ↓  Deteriorating 
Organ Function -  Stable
Overall Status: Deteriorating
Figure 1: ICU decisions are made under massive data volume and time pressure. An ICU AI co-pilot
integrates data streams into a decision-support panel that assessesPatient Status, identifiesAcute
Problems, proposesRecommended Actions, and warns against unsafeRed Flagactions.
capabilities emerged as core requirements for a useful ICU co-pilot: assessPatient Status, identify
Acute Problems, proposeRecommended Actions, and warn againstRed Flagactions that may cause
unsafe outcomes. Figure 1 illustrates the use case of an AI co-pilot in ICU decision support.
Benchmark gap.Despite rapid progress in Large Language Models (LLMs) and agentic systems,
few benchmarks evaluate these four capabilities in real-world ICU settings. Most clinical benchmarks
reduce clinical reasoning to static question answering, diagnosis, or summarization [18, 31, 13, 14, 3],
or to single-endpoint prediction (e.g., mortality [38], shock [7, 37], or acute kidney injury [19, 5]).
Such benchmarks aggregate clinical care into isolated predictions, offering little signal on whether
a model can reason across a changing patient trajectory. More importantly, benchmarks built on
electronic health record (EHR) databases such as MIMIC-IV [16], HiRID [11], and eICU-CRD [25]
treat recorded clinician actions as ground-truth labels. But this assumption is fragile. A recorded
action reflects what clinicians believed best given incomplete information at the bedside, whereas the
optimal action often becomes clear only after reviewing the trajectory using hindsight. Evaluating AI
models against such labels therefore rewards behavioral imitation rather than clinical correctness.
Proposed benchmark.To address this gap, we introduceRealICU, a hindsight-grounded benchmark
built from MIMIC-IV [16] for evaluating LLM-based clinical decision support in the ICU.RealICU
evaluates four physician-motivated tasks over dense 30-minute windows across the ICU trajectory:
Patient Status,Acute Problems,Recommended Actions, andRed Flags. At each window, the agent
observes only information available up to that time, while labels are produced by hindsight physician
judgment over the full trajectory. This design scores agents on clinical correctness rather than on
recorded behavior.RealICUcontains two subsets.RealICU-Goldprovides 930 physician-labeled
windows from 94 ICU stays, andRealICU-Scaleextends evaluation to 11,862 windows usingOracle,
a physician-validated LLM-based hindsight evaluator calibrated against expert consensus.
Failure mode identification and mitigation.UsingRealICU, we benchmark frontier LLM-based
ICU agents across diverse context configurations including memory. Current agents show poor
reliability over long ICU contexts, with two failure modes: (i) Recall-safety tradeoff, where higher
recommendation recall comes with up to 47.3% of these recommendations flagged as potentially
harmful; (ii) Anchoring bias, where agents preserve early interpretations of the patient despite
later contradictory evidence. To mitigate these, we introduce ICU-Evo, a structured-memory agent
framework that maintains recent observations, temporal trends, critical events, trajectory summaries,
and patient-specific insights. ICU-Evo is backbone-agnostic and improves clinical reasoning, but its
safety failures show that structured memory alone is insufficient for reliable ICU co-pilots.
2

## Page 3

Our key contributions are as follows:
• We formulate ICU co-pilot evaluation around four physician-motivated tasks:Patient Status,
Acute Problems,Recommended Actions, andRed Flags. Unlike static clinical QA or outcome
prediction benchmarks, these tasks evaluate whether an AI system can support continuous
bedside reassessment across an evolving ICU trajectory.
• We releaseRealICU, a hindsight-annotated benchmark for clinical correctness rather than
behavioral imitation. Agents observe only data available at decision time, while labels are
produced by hindsight physician judgment over the full trajectory.RealICU-Goldprovides 930
physician-consensus windows from 94 ICU stays, andRealICU-Scaleextends this to 11,862
windows usingOracle, a physician-validated LLM-based hindsight evaluator.
• We identify gaps in current LLM ICU agents and study structured memory as a mitigation.
Across frontier LLMs and multiple context strategies,RealICUremains largely unsolved. We
identify a recall–safety tradeoff and anchoring bias as major failure modes, and introduce ICU-
Evo, a structured-memory agent that improves long-horizon reasoning but shows that memory
alone is insufficient for safe ICU decision support.
2 Related Work
Clinical Benchmarks for LLMs and Agents.Exam-style benchmarks such as MedQA [ 13],
PubMedQA [14], and MedXpertQA [39] evaluate clinical knowledge as multiple-choice recall under
complete information, a format well-addressed by state-of-the-art models that reveals little about de-
cisions under uncertainty. Conversational benchmarks such as AI Hospital [6], AgentClinic [28], and
VivaBench [3] require agents to gather history, order investigations, and converge on a diagnosis over
multiple turns, exposing failure modes such as premature diagnostic closure. MedAgentBench [12]
moves closer to real EHR environments but retains a task-completion framing rather than evaluating
overall patient management. None of these benchmarks evaluates sequential decision-making over
long ICU trajectories or distinguishes behavioral imitation from clinical correctness.RealICUad-
dresses both by grounding evaluation in hindsight physician judgment over the full ICU trajectory,
providing dense and trajectory-level signal of clinical correctness.
Memory-Augmented LLM Agents.Recent LLM agent architectures have explored a range of
memory designs. ReAct [35] appends all reason-action results sequentially but saturates quickly as
context accumulates. AgentFold [36] addresses this by summarizing completed sub-tasks at multiple
temporal scales. Evo-Memory [32] unifies reasoning, action, and memory refinement in a test-time
loop. Retrieval-based systems such as RAG [1, 4] and A-MEM [33] enable selective access over long
histories. However, these systems treat clinical context equally, making no distinction between static
patient background [21], time-sensitive physiological trends [17], and high-level trajectory [29, 26],
which play fundamentally different roles in clinical reasoning. ICU-Evo organizes clinical context
into heterogeneous memory types aligned with these distinctions, enabling systematic study of how
structured memory design shapes ICU decision-making.
3RealICUBenchmark
RealICUevaluates LLM agents on sequential clinical decision-making across ICU trajectories,
mirroring standard medical quality review: model outputs are assessed against hindsight physician
labels produced with full knowledge of patient trajectory rather than against logged clinician actions.
RealICUconsists of two datasets.RealICU-Goldcontains 930 sparsely sampled windows from 94
ICU stays labeled by physician consensus. To scale beyond manual annotation, we introduceOracle,
an LLM-based hindsight evaluator validated againstRealICU-Gold, yieldingRealICU-Scalewith
11,862 densely labeled windows. Both datasets are released test-only to prevent leakage. Detailed
statistics are in Figure 8, Figure 9, and Figure 10.
Each window Wt = (Xt;S t, Pt, At, Rt) contains clinical observations up to time t, annotated
for four tasks:Patient Status St,Acute Problems Pt,Recommended Actions At, andRed Flag
Actions Rt. The model predicts ( ˆSt, ˆPt, ˆAt) from Xt; Rt serves as a safety check against ˆAt. This
3

## Page 4

Data Pipeline
Cohort Sampling
94 ICU stays,  balanced sampling 
Window Discretization
30-min eval windows, 2h stride
Raw Dataset
11,862 windows
Physicians Anno.
ﬁve ICU experts Oracle Anno
hindsight eval
RealICU-Gold 
930 windows
Label Construction
status · problems · actions · red ﬂags
· Age: 45  ·Gender: Female 
· Pre-ICU history: ruptured saccular aneurysm, left cerebellar parenchymal   hemorrhage, rising lactate (1.3 → 3.6)
· Allergies: penicillins, sulfa
truncate at discharge
Enter ICU
22:34   admit Neurosurgery, hx HTN
22:41   phenylephrine 14.55 mg, D5W 60 ml
22:41   weight 70 kg
22:55   intubated, aspiration precautions, HOB >30
23:00   EVD placed: ventricular, level 15cm
23:00   ICP 11, CPP 67, drainage bloody
23:00   R femoral angio site, DSD, C/D/I
23:02   GCS 3 (E1 V1 M1), pupils 3mm non-reactive
23:04   corneas absent, gag/cough intact
23:05   RLE pale & cool, dorsal pulses doppler only
23:06   ART 126/60, MAP 85, HR 87, SpO2 100%
...     ... ...
07:40   sent to OR (aneurysm clipping)
08:00   EVD output 10 ml since last check
08:12   post-op care plan initiated
08:12   restraints initiated, HOB >30
08:15   weight 70 kg, vent settings unchanged
09:01   ABG: pH 7.44, pCO2 35, pO2 221
09:02   acidosis resolved (was pH 7.25)
09:03   Hb 9.4, Hct 28% — mild anemia
09:04   Na 134, glucose 128, lactate 1.4
09:05   K 3.2, iCa 0.93 — repletion needed
09:06   lactate trending down (3.6 → 1.4)
...     ... ...
Patient Context
hour 4 hour 8 hour 12
MIMIC-IV Cohort
hour 96
...  ...   ...  ...
Window Selection
action density
Quality Assessment
Phys.-Phys. IRR, Oracle validation
ICU Trajectory
Labels LabelsRealICU-Scale 
11,862 windows
Patient Status
stable
Acute Problems
Aneurysm rupture
EVD obstruction
Red Flags
✗ Anticoagulants
✗ Aggressive BP 
  lowering
Action Recomm.
Phenylephrine
EVD patency check 
Patient Status
improving
Action Recomm.
ABG monitoring
Replete K, iCa
Red Flags
✗ Hypotonic IV fluids
✗ Anticoagulants
Acute Problems
Electrolyte
derangements
Hydrocephalus / ICP
Figure 2: Left: Data pipeline forRealICU-GoldandRealICU-Scale. Right: Data samples for a
patient ICU trajectory. For each evaluation window,RealICUprovides raw observation data and
clinical labels, including patient status, acute problems, action recommendation, and red flag action.
asymmetry between partial observation and hindsight annotation mirrors the gap between real-time
decision-making and hindsigth review. Figure 2 illustrates the data construction pipeline and samples.
3.1 Dataset Construction
Cohort.We sample 94 ICU stays from the MIMIC-IV [ 16] cohort, each from a distinct patient
and balanced by ICU outcome. Stays shorter than 4 hours are discarded. To capture both early
stabilization and long trajectories, we balance stays by duration above and below 96 hours.
Windowing.We define 30-minute windows as our evaluation unit and sample them along each
ICU trajectory with a 2-hour stride, preserving short-term dynamics while limiting redundancy
across adjacent windows. At inference time, the trajectory visible to the model is truncated prior to
outcome-revealing events such as ICU discharge or the discharge summary.
3.2 Tasks
We identify four crucial ICU reasoning tasks below after consulting more than 30 clinicians, including
five senior ICU physicians who later served as annotators. Together they cover the key capabilities
of a useful ICU co-pilot. For all four tasks, each prediction is accompanied by supporting evidence
E ⊆Xt drawn from the raw events in the recorded history.
Patient Status.A classification of whether the patient is improving, stable, or deteriorating relative to
recent context:S t = (st,Et), wheres t ∈ {improving,stable,deteriorating}andEt ⊆X t.
Acute Problems.A free-text set of acute problems or emerging risks that require active management:
Pt ={(p i,Ei)}k
i=1, whereE i ⊆X t.
Action Recommendation.A free-text set of actions likely to benefit the patient within one hour, such
as stabilizing physiology or preventing deterioration:A t ={(a j,Ej)}m
j=1, whereE j ⊆X t.
Red Flags.A free-text set of high-risk actions that should be avoided because they may be harmful
under the patient’s current physiology or trajectory:R t ={(r l,El)}n
l=1, whereE l ⊆X t.
4

## Page 5

3.3 Annotation Protocol
RealICU-Goldwith physician consensus.We begin from sampling approximately 10 windows per
ICU stay by action density ρt =|E action
t |/|Et|, i.e. the fraction of action events inside each window.
We draw 80% of windows from the ρt ≥0.5 regime, where interventions are frequent, and 20%
from ρt <0.5 as a control set. Each window is independently labeled by at least two of five senior
ICU physicians. Inter-rater reliability (IRR) among physicians ranges from 0.826 to 0.985 across
the four tasks (Table 1), confirming both strong label reproducibility and that the task definitions
are sufficiently precise for consistent clinical judgment. Windows without physician agreement are
dropped, yielding 930 validated windows inRealICU-Gold.
Table 1:RealICU-Goldlabel quality and
Oraclevalidation.
Task Phys. IRR Oracle F1
Patient Status0.985 0.987
Acute Problems0.980 0.987
Action Recom.0.826 0.895
Red Flags0.916 0.964
RealICU-ScalewithOraclescaling.Despite high qual-
ity, manual annotation covers only a sparse sample of each
ICU stay. We therefore introduceOracle, an LLM eval-
uator operating under the same hindsight conditions as
the physicians, and apply it to densely label every win-
dow across the cohort, yielding 11,862 annotated windows
inRealICU-Scale. We validateOracleby measuring its
F1 score against physician consensus onRealICU-Gold.
Oracleachieves more than 0.895 F1 score across all four
tasks (Table 1), supporting its use as a reliable hindsight
annotator at scale. WhileOracleis backbone-agnostic, we
instantiate it with Gemini-3.1-pro [ 8] in this work. De-
tailedOracleprompt is in Appendix E.
Label construction.Labels forPatient Status,Acute Problems, andRed Flagsare taken directly
from annotations. ForAction Recommendation, we restrict the annotation space to critical clinical
interventions, discarding routine monitoring. Annotators review each action as best-practice,
acceptable, or potentially-harmful, and may add free-text actions that should have been taken
but were not observed. At is constructed as the union of best-practice and acceptable actions
together with these free-text additions.Red Flagsare annotated independently as a separate label, not
derived frompotentially-harmfulactions.
3.4 Evaluation Framework
A model under test M maps observations Xt to predictions ( ˆSt, ˆP(k)
t , ˆA(k)
t ), where ˆP(k)
t and ˆA(k)
t
are top-k ranked lists, with access only to events up to time t. In this paper we focus on LLM agents,
but M can be any model. Models are evaluated againstRealICU-GoldandRealICU-Scale, providing
sparse gold-standard supervision and trajectory-level evaluation at scale respectively. Algorithm 1
summarizes the complete evaluation framework.
Semantic matching.To score free-text tasks (Acute Problems,Recommended Actions,Red Flag
Actions), we adopt PubMedBERT [9] and define a binary match, where τ is calibrated against 100
expert-annotated pairs, achieving0.96F1 atτ= 0.5(Appendix A.5):
match(xpred, xref) =1[cos(epred,e ref)≥τ].(1)
Metrics.Patient Statusis evaluated with accuracy and macro-F1 to avoid dominance by the
majority class (stable).Acute ProblemsandRecommended Actionsare set-matching tasks evaluated
with Hit@k and Recall@k at k=5.Red Flag Actionsserves as a safety check via the Harmful
Recommendation Rate (HRR). Let S be the set of ICU stays, Ws the windows in stay s, ˆA(k)
t
the top-k recommendations, and Rt the red-flag set at window t; HRR averages the fraction of
recommended actions that are flagged across stays:
HRR(M) = 1
|S|
X
s∈S
P
t∈Ws
 ˆA(k)
t ∩R t

P
t∈Ws
 ˆA(k)
t
 .(2)
5

## Page 6

Algorithm 1RealICUEvaluation Framework.
Require:modelM; label sourceR ∈ {Gold,Scale}; ICU stay setS; per-stay window sets{W s}s∈S
1:foreach ICU stays∈ Sdo
2:h←0, n←0▷red-flag hits / total recommendations
3:foreach windowt∈ W s in chronological orderdo
4:( ˆSt, ˆP(k)
t , ˆA(k)
t )← M(Xt)▷model sees events up tot
5:(S t, Pt, At, Rt)← R(t)▷pre-labeled by hindsight annotator
6:evaluate( ˆSt, St)forPatient Statusaccuracy and F1
7:evaluate( ˆP(k)
t , Pt)forAcute ProblemsHit@k/ Recall@k ▷semantic matching
8:evaluate( ˆA(k)
t , At)forAction RecommendationHit@k/ Recall@k ▷semantic matching
9:h+=| ˆA(k)
t ∩R t|;n+=| ˆA(k)
t |▷safe recommendation check
10:end for
11:aggregate per-window scores
12:end for
13:returnscores acrossSfor each task
4 ICU-Evo: An ICU Agent System with Evolving Memory
ICU decision-making is sequential, where the underlying patient state is only partially observable
with clinical measurements and can only be updated via new observations. We model this as a
partially observable Markov process [2, 30] and approximate the latent patient state with a structured
memory Mt. We introduce ICU-Evo as an instance of the memory-augmented agent frameworks to
study how structured memory design shapes clinical decision-making.
4.1 Memory as a Structured Belief State
Given the context Xt and static patient context c (e.g. demographics, allergies, pre-ICU history),
ICU-Evo maintains a structured memory state Mt updated at each window by incorporating the new
measurementsx t =X t −X t−1, and produces task-specific predictionsy (k)
t via
Mt =U(M t−1, xt), y (k)
t =f (k)(Mt, c).(3)
The memory decomposes into five components following clinical reasoning:
Mt =

Mwork
t , Mtrend
t , Mevent
t , Mtraj
t , Minsight
t
	
.(4)
Working memory Mwork
t holds the most recent raw observations at detailed resolution.Trend memory
Mtrend
t captures signal trends of vital and lab values.Critical-event memory Mevent
t is a persistent,
append-only log of clinically critical events that change the patient story, such as abnormal physiology,
interventions, and turning points.Trajectory memory Mtraj
t provides a compressed narrative of the
stay at periodic intervals.Insight memory Minsight
t maintains patient-specific hypotheses constructed
as deviations from population-level expectation. Every memory component carries evidence from
raw observations, so any clinical decision is explainable and verifiable against the patient record. In
Table 12, we summarize the memory components with corresponding agent sources.
4.2 ICU-Evo Agent Pipeline
ICU-Evo realizes the memory update operator U through three specialized agents operating at
different temporal scales over the shared memory. ICU-Evo belongs to a broader family of memory-
augmented agent systems. We discuss it alongside recent agent systems in Appendix C. Detailed
prompts are reported in Appendix E.
Observation Agent (Aobs).A rule-based agent that turns raw measurements into structured signals
at every window. It normalizes units, aligns observations to the 30-minute window grid, and extracts
trend signals from vitals using Piecewise Aggregate Approximation [10]:
 
Mwork
t , Mtrend
t

=A obs(Mwork
t−1 , Mtrend
t−1 , xt).(5)
6

## Page 7

Table 2: Evaluation results onRealICU-GOLD. Within each backbone,boldmarks the best system
per column and underline the second best.
Patient Status Acute Problems Action Recom. Red Flags
Backbone SystemAcc.↑F1↑Hit@5↑R@5↑Hit@5↑R@5↑HRR@5↓
Gemini-3.1-pro [8]
Full-context 0.298 0.258 0.486 0.308 0.259 0.1520.137
Local-window 0.315 0.239 0.459 0.258 0.395 0.260 0.151
RAG 0.402 0.348 0.596 0.342 0.496 0.313 0.216
ICU-Evo 0.459 0.365 0.823 0.526 0.676 0.534 0.300
GPT-5.4 [22]
Full-context 0.294 0.233 0.510 0.348 0.404 0.300 0.298
Local-window 0.233 0.184 0.500 0.293 0.380 0.2810.165
RAG 0.288 0.256 0.599 0.349 0.480 0.398 0.234
ICU-Evo 0.312 0.264 0.867 0.570 0.676 0.534 0.473
Qwen3-235B [34]
Full-context 0.225 0.188 0.384 0.226 0.329 0.222 0.117
Local-window 0.152 0.154 0.213 0.126 0.352 0.2420.080
RAG0.315 0.2710.379 0.211 0.453 0.324 0.095
ICU-Evo 0.253 0.197 0.600 0.362 0.526 0.357 0.117
Assessment Agent (Aassess).For every ka cumulative windows, an LLM transforms recent obser-
vations into a trajectory summary and detects critical events. It consumes the working and trend
memory accumulated over the past ka windows, producing a trajectory summary zt appended to
Mtraj
t and critical eventse t appended toM event
t :
 
zt, et

=A assess
 
Mwork
t−ka:t, Mtrend
t−ka:t

.(6)
Insight Agent (Ainsight).Every ki windows, an LLM proposes hypotheses about what is driving the
patient’s clinical course and gathers supporting evidence es and counter-evidence er from Mevent
t .
A hypothesis ht is accepted if s(ht)> r(ht) and rejected otherwise. The Insight Agent actively
reasons about patient-specific patterns, such as unusual drug responses or persistent abnormalities,
promoting individualized care beyond averaged guidelines:
Minsight
t =A insight
 
Minsight
t−1 , Mevent
t−ki:t

.(7)
Predictor (f(k)).The predictor is a task-specific prompted LLM over the full memory state and
static patient context, decoupled from the agent system (Equation 3).
5 Evaluation & Analysis
We evaluate ICU-Evo onRealICU-GoldandRealICU-Scaleagainst three baselines sharing the
same predictor: (i)full-context, all prior observations up to the window; (ii)local-window, the
current window only; (iii)RAG, top-5 windows retrieved via PubMedBERT [ 9] embeddings. See
Appendix A.1 for detailed experiment setup.
5.1RealICURemains Unsolved for Current LLM Systems
RealICUremains unsolved for current frontier LLMs and agent systems. Across all evaluation setups
in Table 2, ICU-Evo with Gemini-3.1-pro [8] reaches only 0.459 accuracy onPatient Statusand 0.534
Recall@5 onAction Recommendation. More concerning,Red FlagsHRR@5 stays non-trivial across
all configurations, indicating current LLM systems still recommend potentially harmful actions in
high-stake ICU setting. Together, these gaps establishRealICUas a clinically grounded safety check
for future AI decision-support systems.
5.2 Structured Memory Consistently Improves Clinical Reasoning
Structured memory improves performance across all four tasks. With GPT-5.4 [ 22], ICU-Evo
improves over RAG by 26.8 Hit@5 points onAcute Problemsand 19.6 onAction Recommendation,
7

## Page 8

0 250 500 750 1000 1250 1500 1750
Hours Since Admission
0.0
0.2
0.4
0.6
0.8
1.0Accuracy
Patient Status
Local window
RAG
ICU-Evo
0 250 500 750 1000 1250 1500 1750
Hours Since Admission
0.0
0.2
0.4
0.6
0.8
1.0Hit@5
Acute Problems
Local window
RAG
ICU-Evo
0 250 500 750 1000 1250 1500 1750
Hours Since Admission
0.0
0.2
0.4
0.6
0.8
1.0Hit@5
Action Recommendation
Local window
RAG
ICU-Evo
0 250 500 750 1000 1250 1500 1750
Hours Since Admission
0.0
0.2
0.4
0.6
0.8
1.0HRR
Red Flags
Local window
RAG
ICU-Evo
Figure 3: Temporal performance onRealICU-Scale(Gemini-3.1-pro [ 8]). ICU-Evo demonstrates its
advantage onPatient StatusandAcute Problemseven up to 1,800-hour trajectory.
with similar margins on Gemini-3.1-pro [8] and Qwen3-235B [34] (Table 2). The pattern holds on
the densely labeledRealICU-Scale(Table 4, Figure 3). ICU-Evo’s Hit@5 onAcute Problemsstays
near 0.8 even for stays up to 1,800 hours, while non-memory baselines remain about 20 points lower
and visibly noisier. Future ICU decision-support agents will benefit from memory that actively tracks
the patient’s evolving state and scales to long stays.
5.3 The Agent-OracleGap: Beyond Behavioral Imitation
We observe a large performance gap between Agent andOracleonRealICU-Gold. The bottleneck
of current ICU agents is not medical knowledge in the LLM backbone but how an agent integrates
evidence over time. With Gemini-3.1-pro [8],Oraclereaches F1 0.987 onPatient Statusand 0.964
onRed Flagsidentification (Table 1), while ICU-Evo on the same backbone reaches only 0.365
F1 onPatient Status, with a concerningly high rate of harmful recommendations with 0.300 HRR
(Table 2). The four clinical tasks are therefore well handled given the full trajectory but break down
under real-time conditions. This gap also indicates the value of hindsight evaluation, since scoring
agents against recorded clinician actions can only measure how closely the agents imitate human
behavior under limited information. Progress on ICU decision support therefore depends on both
stronger real-time reasoning architectures and the broader adoption of hindsight evaluation.
5.4 Ablation Study
We ablate each component of ICU-Evo’s memory in a leave-one-out setup (Table 3). Working
memory is crucial for local clinical reasoning, and removing it degrades every task with notable
drops onAcute ProblemsHit@5 (Gemini-3.1-pro [ 8], 0.823 to 0.761). Trajectory memory matters
for temporal understanding tasks. Without it,Acute ProblemsandAction Recommendationboth drop,
whilePatient Statusstays stable since it leans on local observations.
In contrast, insight memory causes fluctuations, and removing it sometimes leads to neutral or
beneficial results. This suggests that current LLMs default to medical-generalist priors and is not yet
capable to identify reliable personalized clinical patterns across long stays. We examine the failure
modes in the next section.
8

## Page 9

Table 3: Memory ablation onRealICU-GOLD. For each row, we remove one component from
ICU-Evo’s memory. Within each backbone,boldmarks the best result and underline the second best.
Patient Status Acute Problems Action Recom. Red Flags
Backbone Memory VariantAcc.↑F1↑Hit@5↑R@5↑Hit@5↑R@5↑HRR↓
Gemini-3.1-pro [8]
ICU-Evo 0.459 0.365 0.823 0.526 0.676 0.534 0.300
−working memory 0.383 0.294 0.761 0.461 0.507 0.3080.087
−trend 0.451 0.352 0.811 0.527 0.521 0.330 0.097
−critical events 0.445 0.351 0.819 0.527 0.528 0.328 0.099
−trajectory 0.443 0.362 0.789 0.500 0.506 0.304 0.090
−insight0.4620.3560.823 0.5340.555 0.357 0.088
Qwen3-235B [34]
ICU-Evo 0.253 0.197 0.600 0.362 0.526 0.357 0.117
−working memory 0.159 0.127 0.421 0.233 0.447 0.307 0.117
−trend 0.248 0.188 0.552 0.333 0.559 0.393 0.122
−critical events 0.236 0.187 0.546 0.320 0.595 0.420 0.128
−trajectory0.270 0.2490.486 0.290 0.557 0.393 0.138
−insight 0.250 0.202 0.587 0.348 0.601 0.4200.141
5.5 Failure Mode Analysis
Oraclefailure modes.Oraclereaches around 90% F1 across all tasks (Table 1). The remaining
disagreements concentrate on two patterns: (i) boundary mis-calibration onPatient Status, where
failures fall on stable–improving or stable–deteriorating borders; (ii) granularity mismatch
onAcute Problems, whereOraclereaches for broad descriptors (e.g. hemodynamic instability) while
physicians name specific complications (e.g. ventilator-associated pneumonia). These are edge cases
rather than systematic errors, supportingOracle’s reliability as a large-scale annotator.
Agent failure modes.The most consequential failure is the recall–safety tradeoff, where higher
recommendation recall increases the incidence of harmful clinical suggestions. In Table 2, ICU-Evo
(GPT-5.4 [22]) gains more than 20 Action RecommendationHit@5 points over RAG, but its HRR@5
doubles from 0.234 to 0.473. We use an LLM-based classifier to group these 394 cases, and the
majority concentrate in four high-stakes families: hemodynamic and pressor management (n=135),
volume and diuresis (n=64), anti-coagulation (n=54), and ventilation/sedation (n=53). We find
that current LLM agents tend to recognize part of a syndrome and propose the full treatment bundle
before contraindications are ruled out.
The second failure is anchoring bias, where agents over-commit to early interpretations and ignore
later evidence. Removing insight memory improvesAction RecommendationHit@5 from 0.526 to
0.601 on Qwen3-235B [34] (Table 3), indicating that generated insights actively mislead the agent.
The agent maintains around 6 hypotheses per patient, 80% containing anticipatory exceptions (e.g.
below-average tolerance, paradoxical response). These priors push the agent toward rescue bundles
even when current evidence is weak. Case studies are in Appendix D.
6 Discussion
RealICUreveals a substantial gap between the medical knowledge of frontier LLMs and their
ability to reason under partial observability across an evolving ICU trajectory. We identify two
recurring failure modes that persist across multiple context configurations. (i) the recall–safety
tradeoff, where gains inRecommended Actionscoverage are accompanied by a higher rate of unsafety.
(ii) anchoring bias, where agents commit to an early read of the patient and fail to update as new
evidence accumulates. ICU-Evo uses structured, evidence-grounded memory at multiple temporal
scales to track the evolving patient state, but multi-scale memory alone does not prevent unsafe
recommendations. Reliable ICU co-pilots will require advances in long-context clinical reasoning
together with better safety mechanisms.
9

## Page 10

Beyond the ICU,RealICUoffers a methodology for evaluating AI systems where recorded human
actions are imperfect and the right action is visible only in hindsight. We hope this framing supports
broader work on evaluating AI systems in high-stakes sequential decision environments.
Limitations.RealICUis built on the MIMIC-IV [ 16] cohort, and its demographic and care-pattern
distribution may not transfer to ICUs with different staffing or documentation conventions. Extending
to multi-center and international data is an important direction. Due to compute constraints, we run
a single experiment per LLM configuration and omit variance over long ICU trajectories. We also
focus on text-based data, leaving multi-modal data such as imaging and signals to future work.
7 Acknowledgement
This paper is supported by the DAAD programme Konrad Zuse Schools of Excellence in Artificial
Intelligence, sponsored by the Federal Ministry of Research, Technology and Space. This work is
partially funded by the European Research Council (ERC) project Deep4MI (884622).
10

## Page 11

References
[1] Muhammad Arslan, Hussam Ghanem, Saba Munawar, and Christophe Cruz. A survey on rag
with llms.Procedia computer science, 246:3781–3790, 2024.
[2] Anthony Rocco Cassandra.Exact and approximate algorithms for partially observable Markov
decision processes. Brown University, 1998.
[3] Christopher Chiu, Silviu Pitis, and Mihaela van der Schaar. Simulating viva voce examinations
to evaluate clinical reasoning in large language models.arXiv preprint arXiv:2510.10278, 2025.
[4] Florin Cuconasu, Giovanni Trappolini, Federico Siciliano, Simone Filice, Cesare Campagnano,
Yoelle Maarek, Nicola Tonellotto, and Fabrizio Silvestri. The power of noise: Redefining
retrieval for rag systems. InProceedings of the 47th International ACM SIGIR Conference on
Research and Development in Information Retrieval, pages 719–729, 2024.
[5] Junzi Dong, Ting Feng, Binod Thapa-Chhetry, Byung Gu Cho, Tunu Shum, David P Inwald,
Christopher JL Newth, and Vinay U Vaidya. Machine learning model for early prediction of
acute kidney injury (aki) in pediatric critical care.Critical Care, 25(1):288, 2021.
[6] Zhihao Fan, Lai Wei, Jialong Tang, Wei Chen, Wang Siyuan, Zhongyu Wei, and Fei Huang. Ai
hospital: Benchmarking large language models in a multi-agent medical interaction simulator.
InProceedings of the 31st International Conference on Computational Linguistics, pages
10183–10213, 2025.
[7] Shameek Ghosh, Jinyan Li, Longbing Cao, and Kotagiri Ramamohanarao. Septic shock
prediction for icu patients via coupled hmm walking on sequential contrast patterns.Journal of
biomedical informatics, 66:19–31, 2017.
[8] Google DeepMind. Gemini 3.1 pro model card. Technical report, Google DeepMind, 2026.
URL https://deepmind.google/models/model-cards/gemini-3-1-pro/ . Accessed:
May 6, 2026.
[9] Yu Gu, Robert Tinn, Hao Cheng, Michael Lucas, Naoto Usuyama, Xiaodong Liu, Tristan
Naumann, Jianfeng Gao, and Hoifung Poon. Domain-specific language model pretraining
for biomedical natural language processing.ACM Transactions on Computing for Healthcare
(HEALTH), 3(1):1–23, 2021.
[10] Chonghui Guo, Hailin Li, and Donghua Pan. An improved piecewise aggregate approximation
based on statistical features for time series mining. InInternational conference on knowledge
science, engineering and management, pages 234–244. Springer, 2010.
[11] Stephanie L Hyland, Martin Faltys, Matthias Hüser, Xinrui Lyu, Thomas Gumbsch, Cristóbal
Esteban, Christian Bock, Max Horn, Michael Moor, Bastian Rieck, et al. Early prediction of
circulatory failure in the intensive care unit using machine learning.Nature medicine, 26(3):
364–373, 2020.
[12] Yixing Jiang, Kameron C Black, Gloria Geng, Danny Park, James Zou, Andrew Y Ng, and
Jonathan H Chen. Medagentbench: a virtual ehr environment to benchmark medical llm agents.
Nejm Ai, 2(9):AIdbp2500144, 2025.
[13] Di Jin, Eileen Pan, Nassim Oufattole, Wei-Hung Weng, Hanyi Fang, and Peter Szolovits. What
disease does this patient have? a large-scale open domain question answering dataset from
medical exams.Applied Sciences, 11(14):6421, 2021.
[14] Qiao Jin, Bhuwan Dhingra, Zhengping Liu, William Cohen, and Xinghua Lu. Pubmedqa: A
dataset for biomedical research question answering. InProceedings of the 2019 conference on
empirical methods in natural language processing and the 9th international joint conference on
natural language processing (EMNLP-IJCNLP), pages 2567–2577, 2019.
[15] Alistair EW Johnson, Tom J Pollard, Seth J Berkowitz, Nathaniel R Greenbaum, Matthew P
Lungren, Chih-ying Deng, Roger G Mark, and Steven Horng. Mimic-cxr, a de-identified
publicly available database of chest radiographs with free-text reports.Scientific data, 6(1):317,
2019.
11

## Page 12

[16] Alistair EW Johnson, Lucas Bulgarelli, Lu Shen, Alvin Gayles, Ayad Shammout, Steven Horng,
Tom J Pollard, Sicheng Hao, Benjamin Moody, Brian Gow, et al. Mimic-iv, a freely accessible
electronic health record dataset.Scientific data, 10(1):1, 2023.
[17] H Lehman Li-wei, Ryan P Adams, Louis Mayaud, George B Moody, Atul Malhotra, Roger G
Mark, and Shamim Nemati. A physiological time series dynamics-based approach to patient
monitoring and outcome prediction.IEEE journal of biomedical and health informatics, 19(3):
1068–1076, 2014.
[18] Mingyu Derek Ma, Chenchen Ye, Yu Yan, Xiaoxuan Wang, Peipei Ping, Timothy S Chang, and
Wei Wang. Clibench: A multifaceted and multigranular evaluation of large language models for
clinical decision making.arXiv preprint arXiv:2406.09923, 2024.
[19] Rakesh Malhotra, Kianoush B Kashani, Etienne Macedo, Jihoon Kim, Josee Bouchard, Susan
Wynn, Guangxi Li, Lucila Ohno-Machado, and Ravindra Mehta. A risk prediction score for
acute kidney injury in the intensive care unit.Nephrology Dialysis Transplantation, 32(5):
814–822, 2017.
[20] Orit Manor-Shulman, Joseph Beyene, Helena Frndova, and Christopher S Parshuram. Quantify-
ing the volume of documented clinical information in critical illness.Journal of critical care,
23(2):245–250, 2008.
[21] Paola P Mattey-Mora, Connor A Begle, Candice K Owusu, Chen Chen, and Maria A Parker.
Hospitalised versus outpatient covid-19 patients’ background characteristics and comorbidities:
a systematic review and meta-analysis.Reviews in Medical Virology, 32(3):e2306, 2022.
[22] OpenAI. Gpt-5.4 technical report and model card. Technical report, OpenAI, March 2026. URL
https://openai.com/index/introducing-gpt-5-4/. Accessed: May 6, 2026.
[23] Nicolas Paul, Elena Ribet Buse, Anna-Christina Knauthe, Monika Nothacker, Björn Weiss, and
Claudia D Spies. Effect of icu care bundles on long-term patient-relevant outcomes: a scoping
review.BMJ open, 13(2):e070962, 2023.
[24] Brian W Pickering, Vitaly Herasevich, Adil Ahmed, and Ognjen Gajic. Novel representation of
clinical information in the icu.Applied Clinical Informatics, 1(02):116–131, 2010.
[25] Tom J Pollard, Alistair EW Johnson, Jesse D Raffa, Leo A Celi, Roger G Mark, and Omar
Badawi. The eicu collaborative research database, a freely available multi-center database for
critical care research.Scientific data, 5(1):180178, 2018.
[26] Elizabeth Reed and Jessica Corner. Defining the illness trajectory of metastatic breast cancer.
BMJ supportive & palliative care, 5(4):358–365, 2015.
[27] Regis Goulart Rosa, Giovanni Esteves Ferreira, Thiago Wendt Viola, Caroline Cabral Robinson,
Renata Kochhann, Paula Pinheiro Berto, Livia Biason, Paulo Ricardo Cardoso, Maicon Falavi-
gna, and Cassiano Teixeira. Effects of post-icu follow-up on subject outcomes: a systematic
review and meta-analysis.Journal of critical care, 52:115–125, 2019.
[28] Samuel Schmidgall, Rojin Ziaei, Carl Harris, Eduardo Reis, Jeffrey Jopling, and Michael Moor.
Agentclinic: a multimodal agent benchmark to evaluate ai in simulated clinical environments.
arXiv preprint arXiv:2405.07960, 2024.
[29] Helena Sousa, Susana Almeida, Joao Bessa, and M Graca Pereira. The developmental trajec-
tory of cancer-related cognitive impairment in breast cancer patients: a systematic review of
longitudinal neuroimaging studies.Neuropsychology review, 30(3):287–309, 2020.
[30] Matthijs TJ Spaan. Partially observable markov decision processes. InReinforcement learning:
State-of-the-art, pages 387–414. Springer, 2012.
[31] Robin Van De Water, Hendrik Schmidt, Paul Elbers, Patrick Thoral, Bert Arnrich, and Patrick
Rockenschaub. Yet another icu benchmark: A flexible multi-center framework for clinical ml.
arXiv preprint arXiv:2306.05109, 2023.
12

## Page 13

[32] Tianxin Wei, Noveen Sachdeva, Benjamin Coleman, Zhankui He, Yuanchen Bei, Xuying Ning,
Mengting Ai, Yunzhe Li, Jingrui He, Ed H Chi, et al. Evo-memory: Benchmarking llm agent
test-time learning with self-evolving memory.arXiv preprint arXiv:2511.20857, 2025.
[33] Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, and Yongfeng Zhang. A-mem:
Agentic memory for llm agents.arXiv preprint arXiv:2502.12110, 2025.
[34] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu,
Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report.arXiv preprint
arXiv:2505.09388, 2025.
[35] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R Narasimhan, and Yuan
Cao. React: Synergizing reasoning and acting in language models. InThe eleventh international
conference on learning representations, 2022.
[36] Rui Ye, Zhongwang Zhang, Kuan Li, Huifeng Yin, Zhengwei Tao, Yida Zhao, Liangcai Su,
Liwen Zhang, Zile Qiao, Xinyu Wang, et al. Agentfold: Long-horizon web agents with proactive
context management.arXiv preprint arXiv:2510.24699, 2025.
[37] Christopher R Yee, Niven R Narain, Viatcheslav R Akmaev, and Vijetha Vemulapalli. A data-
driven approach to predicting septic shock in the intensive care unit.Biomedical informatics
insights, 11:1178222619885147, 2019.
[38] Zirun Zhao, Anne Chen, Wei Hou, James M Graham, Haifang Li, Paul S Richman, Henry C
Thode, Adam J Singer, and Tim Q Duong. Prediction model and risk scores of icu admission
and mortality in covid-19.PloS one, 15(7):e0236618, 2020.
[39] Yuxin Zuo, Shang Qu, Yifei Li, Zhangren Chen, Xuekai Zhu, Ermo Hua, Kaiyan Zhang, Ning
Ding, and Bowen Zhou. Medxpertqa: Benchmarking expert-level medical reasoning and
understanding.arXiv preprint arXiv:2501.18362, 2025.
13

## Page 14

Appendix
Appendix Contents
A. Performance Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
A.1. Experiment Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
A.2. Evaluation Results onRealICU-Scale. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
A.3. Averaged Patient Trajectory onRealICU-Scale. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
A.4. Per-Disease Performance onRealICU-GOLD. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .18
A.5. Semantic Matcher Calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
A.6. Token Efficiency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .22
B. Dataset Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
B.1. Dataset Statistics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .23
B.2.RealICU-GoldCross Validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
B.3. Dataset Pre-processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
C. Memory-Augmented Agents for Clinical Decision Support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
C.1. Formulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
C.2. Instantiations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
C.3. ICU-Evo as Heterogeneous Clinical Memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
C.4. Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
D. Case Study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
D.1. Failure Case: Recall Safety Tradeoff . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
D.2. Failure Case: Anchoring Bias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
D.3. Memory Snapshot . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
E. Prompts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
E.1. Oracle Prompt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
E.2. Agent Prompt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
14

## Page 15

A Performance Analysis
A.1 Experiment Setup
We evaluate ICU-Evo onRealICU-GoldandRealICU-Scaleagainst three baselines sharing the same
predictor: (i)full-context, all prior observations up to the window; (ii)local-window, the current
window only; (iii)RAG, top-5 windows retrieved via PubMedBERT [ 9] embeddings. We set ka
and ki to 12 windows (6 hours) for ICU-Evo. ForAction Recommendation, we strip the current
window’s recorded actions before prediction to prevent label leakage. We evaluate every window in
RealICU-Goldand every fourth window along the trajectory inRealICU-Scale.
We use two closed-source LLMs (Gemini-3.1-pro [ 8], GPT-5.4 [22]) and one open-source LLM
(Qwen3-235B-A22B [34]) as backbones for evaluation. Evaluation results onRealICU-Goldand
RealICU-Scaleare reported in Table 2 and Table 4 respectively. Full-context Gemini and GPT runs
onRealICU-Scaleare omitted due to compute budget on stays beyond hundreds of hours.Oracle
uses Gemini-3.1-pro [8] to generated hindsight annotations with access to the full patient trajectory.
A.2 Evaluation Results onRealICU-Scale
Table 4 reports full evaluation results onRealICU-Scaleacross all three backbones and four systems.
Full-context evaluation is omitted for Gemini-3.1-pro [ 8] and GPT-5.4 [ 22] due to prohibitive
inference cost over multi-day ICU trajectories. Qwen3-235B [34] is included as a reference open-
weight upper bound.
The results onRealICU-Scalelargely recapitulate the pattern observed onRealICU-GOLD(Table 2).
ICU-Evo achieves the strongest performance onAcute ProblemsandAction Recommendationacross
all three backbones, with particularly large margins onAcute ProblemsHit (up to +0.268 over RAG
for Gemini-3.1-pro [8]). TheRed FlagHRR remains the consistent weak point of ICU-Evo regardless
of backbone, suggesting the same premature anchoring failure mode (see Sec. 5.5), where current
agent systems over-commit to early interpretation of the patient instead of updating hypothesis with
new observations. Qwen3-235B [ 34] achieves lower overall performance compared to Gemini-
3.1-pro [8] and GPT-5.4 [22], suggesting that weaker instruction-following reduces the benefit of
structured memory on tasks requiring precise categorical judgment.
We further illustrate the temporal performance of LLM agents with full-context, local-window,
retrieval-augmentation, memory-augmentation configurations in Figure 4 and Figure 5.
Table 4: Evaluation results on theRealICU-Scale. Within each backbone,boldmarks the best system
per column and underline the second best.
Patient Status Acute Problems Action Recom. Red Flags
Backbone SystemAcc.↑F1↑Hit@5↑R@5↑Hit@5↑R@5↑HRR↓
Gemini-3.1-pro [8]
Full-context – – – – – – –
Local-window 0.405 0.264 0.487 0.265 0.447 0.307 0.066
RAG 0.442 0.312 0.568 0.315 0.466 0.331 0.073
ICU-Evo 0.519 0.348 0.827 0.518 0.514 0.3301 0.087
GPT-5.4 [22]
Full-context – – – – – – –
Local-window 0.415 0.265 0.475 0.266 0.451 0.3080.073
RAG 0.411 0.269 0.584 0.321 0.509 0.4350.096
ICU-Evo 0.438 0.327 0.852 0.562 0.575 0.368 0.090
Qwen3-235B [34]
Full-context 0.201 0.116 0.401 0.232 0.455 0.299 0.215
Local-window 0.175 0.159 0.254 0.142 0.440 0.2950.207
RAG0.367 0.2820.379 0.207 0.4460.3420.225
ICU-Evo 0.304 0.177 0.649 0.375 0.515 0.327 0.292
15

## Page 16

0 250 500 750 1000 1250 1500 1750
Hours Since Admission
0.0
0.2
0.4
0.6
0.8
1.0Accuracy
Patient Status
Local window
RAG
ICU-Evo
0 250 500 750 1000 1250 1500 1750
Hours Since Admission
0.0
0.2
0.4
0.6
0.8
1.0Hit@5
Acute Problems
Local window
RAG
ICU-Evo
0 250 500 750 1000 1250 1500 1750
Hours Since Admission
0.0
0.2
0.4
0.6
0.8
1.0Hit@5
Action Recommendation
Local window
RAG
ICU-Evo
0 250 500 750 1000 1250 1500 1750
Hours Since Admission
0.0
0.2
0.4
0.6
0.8
1.0HRR
Red Flags
Local window
RAG
ICU-Evo
Figure 4: Temporal performance over the full ICU stay onRealICU-Scale(GPT-5.4 [22]).
0 200 400 600 800 1000 1200
Hours Since Admission
0.0
0.2
0.4
0.6
0.8
1.0Accuracy
Patient Status
Full history
Local window
RAG
ICU-Evo
0 250 500 750 1000 1250 1500 1750
Hours Since Admission
0.0
0.2
0.4
0.6
0.8
1.0Hit@5
Acute Problems
Full history
Local window
RAG
ICU-Evo
0 250 500 750 1000 1250 1500 1750
Hours Since Admission
0.0
0.2
0.4
0.6
0.8
1.0Hit@5
Action Recommendation
Full history
Local window
RAG
ICU-Evo
0 250 500 750 1000 1250 1500 1750
Hours Since Admission
0.0
0.2
0.4
0.6
0.8
1.0HRR
Red Flags
Full history
Local window
RAG
ICU-Evo
Figure 5: Temporal performance over the full ICU stay onRealICU-Scale(Qwen3-235B [34]).
16

## Page 17

A.3 Averaged Patient Trajectory onRealICU-Scale
We visualize patient trajectories onRealICU-Scaleusing thePatient Statuslabel in Figure 6. We
map each window-level label to an ordinal score (deteriorating = -1, stable = 0, improving = 1)
and normalize time within each ICU stay to the interval [0,1]. After binning each trajectory into
20 normalized time bins and averaging repeated observations within patient-bin pairs, we plotted
all individual trajectories as low-opacity curves and overlaid outcome-stratified cohort means with
95% confidence bands. This highlights both patient-level heterogeneity and the average temporal
separation between survivors and non-survivors.
The survived and died cohorts are already separated at admission, with survivors hovering near
stable and non-survivors sitting consistently below it, and the gap widens over the course of the stay
as the survivor mean drifts toward improving while the non-survivor mean declines sharply in the
final 20% of normalized ICU time. Both cohorts show substantial patient-level heterogeneity in the
thin lines, which is expected given the diversity of admission diagnoses, but the cohort means recover
the clinically intuitive ordering that survivors trend upward and non-survivors trend downward.
This pattern indicates that the window-level labels produced byOracleaggregate into a coherent
patient-level signal, and supports the use ofRealICU-Scalefor trajectory-level analyses despite its
labels being generated rather than physician-annotated.
0% 20% 40% 60% 80% 100%
Normalized ICU progression
Deteriorating
Stable
Improving
Patient status score
Survived mean (n=47)
Died mean (n=47)
Figure 6: Averaged patient status trajectories fromOracleonRealICU-Scale. Window-levelPatient
Statuslabels are mapped to an ordinal score (deteriorating =−1 , stable = 0, improving = +1) and
aggregated into normalized duration time. Thin lines show individual trajectories, and thick lines
and shaded regions show cohort means with 95% confidence bands. The survived and died cohorts
separate from admission onward and diverge further over the stay.
17

## Page 18

A.4 Per-Disease Performance onRealICU-GOLD.
Tables 5 report a breakdown across the six disease groups exceeding 8% prevalence inRealICU-Gold
using Gemini-3.1-pro [8] backbone. The decomposition tests whether the gains of ICU-Evo are
driven by a subset of phenotypes or hold across the case mix.
The dominance of ICU-Evo on context-heavy tasks (Patient Status, Acute Problems, Recommended
Actions) is consistent across nearly all disease groups. ICU-Evo achieves the best Hit@5 on Acute
Problems for every group, with margins over the strongest baseline ranging from 0.134 (GI & Hepatic)
to 0.358 (Sepsis & Infection), so the benefit of structured longitudinal memory is not phenotype-
specific. The pattern is most pronounced on Cardiovascular and GI & Hepatic cases, where ICU-Evo
wins on six of seven metrics, suggesting that diseases with protracted trajectories benefit most from
explicit trend and trajectory memory.
Respiratory and Sepsis & Infection expose the limits of the current memory design on Recommended
Actions. RAG matches or surpasses ICU-Evo on Hit@5 and R@5 for these two groups, while
ICU-Evo retains its lead on upstream tasks. Respiratory and septic management is dominated by
recurring, protocol-driven interventions such as ventilator adjustments and antimicrobial escalation,
for which lexical retrieval over recent context is competitive with longitudinal memory. This aligns
with the backbone-dependent memory tolerance reported in the Qwen ablation and reinforces that
memory architecture and task structure interact.
We report more detailed per-disease results with GPT-5.4 [22] backbone in Table 6, and with Qwen-
235B [34] backbone in Table 7.
Table 5: Per-disease performance onRealICU-GOLD(Gemini-3.1-pro [ 8] backbone). Disease groups
are omitted with less than 8% proportion. Within each group,boldmarks the best system per column
and underline the second best.
Patient Status Acute Problems Action Recom. Red Flags
Disease Group SystemAcc.↑F1↑Hit@5↑R@5↑Hit@5↑R@5↑HRR@5↓
Cardiovascular
Full-context 0.337 0.269 0.584 0.367 0.299 0.177 0.066
Local-window 0.313 0.246 0.450 0.245 0.400 0.2730.059
RAG 0.409 0.370 0.593 0.337 0.442 0.284 0.066
ICU-Evo 0.472 0.374 0.828 0.526 0.595 0.375 0.089
Sepsis & Infection
Full-context 0.147 0.166 0.287 0.154 0.156 0.0750.065
Local-window 0.327 0.268 0.458 0.258 0.378 0.226 0.067
RAG 0.353 0.283 0.574 0.312 0.535 0.3290.089
ICU-Evo 0.453 0.335 0.816 0.491 0.514 0.296 0.098
Injury & Poisoning
Full-context 0.303 0.199 0.469 0.338 0.225 0.1450.057
Local-window 0.303 0.209 0.512 0.306 0.390 0.257 0.090
RAG 0.474 0.379 0.636 0.369 0.526 0.3610.078
ICU-Evo 0.490 0.399 0.817 0.534 0.451 0.299 0.095
Respiratory
Full-context0.3400.248 0.621 0.390 0.379 0.207 0.112
Local-window 0.270 0.218 0.456 0.255 0.425 0.2410.056
RAG 0.290 0.260 0.594 0.340 0.505 0.284 0.084
ICU-Evo 0.320 0.278 0.851 0.559 0.551 0.323 0.120
GI & Hepatic
Full-context 0.438 0.396 0.527 0.338 0.347 0.226 0.115
Local-window 0.350 0.311 0.510 0.298 0.427 0.317 0.122
RAG 0.412 0.391 0.645 0.408 0.587 0.360 0.073
ICU-Evo 0.500 0.437 0.779 0.512 0.592 0.382 0.098
All Diseases (Table 2)
Full-context 0.298 0.258 0.486 0.308 0.259 0.1520.137
Local-window 0.315 0.239 0.459 0.258 0.395 0.260 0.151
RAG 0.402 0.348 0.596 0.342 0.496 0.313 0.216
ICU-Evo 0.459 0.365 0.823 0.526 0.676 0.534 0.300
18

## Page 19

Table 6: Per-disease performance onRealICU-GOLD(GPT-5.4 [ 22] backbone). Disease groups are
omitted with less than 8% proportion. Within each group,boldmarks the best system per column
and underline the second best.
Patient Status Acute Problems Action Recom. Red Flags
Disease Group SystemAcc.↑F1↑Hit@5↑R@5↑Hit@5↑R@5↑HRR@5↓
Cardiovascular
Full-context0.350 0.2500.589 0.396 0.518 0.387 0.157
Local-window 0.262 0.190 0.484 0.286 0.327 0.2970.114
RAG 0.300 0.243 0.578 0.313 0.487 0.456 0.138
ICU-Evo 0.275 0.246 0.853 0.558 0.705 0.562 0.136
Sepsis & Infection
Full-context 0.153 0.164 0.314 0.191 0.137 0.087 0.111
Local-window 0.153 0.213 0.528 0.293 0.368 0.233 0.114
RAG 0.227 0.2920.609 0.329 0.430 0.327 0.095
ICU-Evo 0.347 0.266 0.864 0.539 0.700 0.558 0.158
Injury & Poisoning
Full-context 0.249 0.157 0.510 0.373 0.404 0.306 0.161
Local-window 0.319 0.150 0.479 0.299 0.482 0.318 0.138
RAG0.3280.182 0.545 0.364 0.545 0.431 0.157
ICU-Evo 0.328 0.267 0.922 0.648 0.618 0.455 0.104
Respiratory
Full-context 0.340 0.254 0.653 0.438 0.543 0.477 0.176
Local-window 0.322 0.189 0.533 0.297 0.386 0.211 0.137
RAG0.378 0.2900.678 0.424 0.319 0.2470.113
ICU-Evo 0.270 0.237 0.923 0.631 0.767 0.623 0.182
GI & Hepatic
Full-context0.425 0.3490.575 0.441 0.474 0.323 0.306
Local-window 0.100 0.165 0.561 0.373 0.331 0.2790.098
RAG 0.214 0.256 0.682 0.512 0.512 0.412 0.148
ICU-Evo 0.363 0.347 0.827 0.570 0.657 0.490 0.157
All Diseases (Table 2)
Full-context 0.294 0.233 0.510 0.348 0.404 0.300 0.298
Local-window 0.233 0.184 0.500 0.293 0.380 0.2810.165
RAG 0.288 0.256 0.599 0.349 0.480 0.398 0.234
ICU-Evo 0.312 0.264 0.867 0.570 0.676 0.534 0.473
19

## Page 20

Table 7: Per-disease performance onRealICU-GOLD(Qwen3-235B [ 34] backbone). Disease groups
are omitted with less than 8% proportion. Within each group,boldmarks the best system per column
and underline the second best.
Patient Status Acute Problems Action Recom. Red Flags
Disease Group SystemAcc.↑F1↑Hit@5↑R@5↑Hit@5↑R@5↑HRR@5↓
Cardiovascular
Full-context 0.218 0.206 0.455 0.249 0.390 0.270 0.129
Local-window 0.156 0.164 0.188 0.109 0.351 0.2460.087
RAG0.307 0.2780.350 0.189 0.451 0.332 0.090
ICU-Evo 0.268 0.219 0.552 0.316 0.552 0.363 0.134
Sepsis & Infection
Full-context 0.107 0.122 0.233 0.137 0.156 0.1080.083
Local-window 0.147 0.186 0.224 0.113 0.322 0.198 0.098
RAG0.333 0.2820.348 0.176 0.443 0.277 0.093
ICU-Evo 0.140 0.130 0.575 0.328 0.530 0.353 0.098
Injury & Poisoning
Full-context 0.269 0.153 0.432 0.289 0.291 0.232 0.093
Local-window 0.197 0.165 0.301 0.221 0.373 0.2800.065
RAG0.362 0.2520.516 0.328 0.481 0.3570.102
ICU-Evo 0.305 0.220 0.669 0.457 0.452 0.321 0.087
Respiratory
Full-context 0.280 0.145 0.444 0.266 0.419 0.236 0.116
Local-window 0.140 0.117 0.253 0.147 0.354 0.2220.052
RAG 0.340 0.3110.451 0.272 0.463 0.331 0.083
ICU-Evo 0.380 0.205 0.658 0.404 0.675 0.457 0.162
GI & Hepatic
Full-context0.3750.315 0.459 0.295 0.382 0.270 0.188
Local-window 0.175 0.150 0.214 0.138 0.334 0.273 0.123
RAG 0.338 0.3360.329 0.199 0.459 0.369 0.099
ICU-Evo 0.262 0.258 0.646 0.413 0.508 0.394 0.132
All Diseases (Table 2)
Full-context 0.225 0.188 0.384 0.226 0.329 0.222 0.117
Local-window 0.152 0.154 0.213 0.126 0.352 0.2420.080
RAG0.315 0.2710.379 0.211 0.453 0.324 0.095
ICU-Evo 0.253 0.197 0.600 0.362 0.526 0.357 0.117
20

## Page 21

A.5 Semantic Matcher Calibration
We adopt PubMedBERT [9] (NeuML/pubmedbert-base-embeddings) to generate embeddings for
semantic match forAcute Problems,Action Recommendation, andRed Flagstasks.
Calibration set.We sampled 100 action-string pairs from held-out ICU windows and asked a
board-certified intensivist to label each pair as a binary classification for semantic match or non-match.
The set is balanced by construction with 50 matched pairs and 50 non-matched pairs.
Threshold sweep.Table 8 reports precision, recall, F1, and accuracy at seven candidate thresholds,
and Figure 7 visualises the trade-off. PubMedBERT cosine similarity separates the two classes
almost perfectly (AUROC = 0.996). Precision reaches 1.00 for all τ≥0.5 , while recall decays
monotonically as τ increases. We select τ∗ = 0.5, which maximises F1 (0.958) and eliminates false
positives while retaining 92% of true matches. This operating point is used in all reported evaluations.
Table 8: Semantic matcher performance on the 100-pair calibration set across candidate thresholds.
The selected threshold (τ∗ = 0.5) maximises F1 and achieves perfect precision.
τAccuracy Precision Recall F1
0.3 0.86 0.78 1.00 0.88
0.4 0.95 0.91 1.00 0.95
0.5∗ 0.96 1.00 0.92 0.96
0.6 0.82 1.00 0.64 0.78
0.7 0.66 1.00 0.32 0.48
0.8 0.53 1.00 0.06 0.12
0.9 0.50 0.00 0.00 0.00
0.3 0.4 0.5 0.6 0.7 0.8 0.9
Threshold
0.0
0.2
0.4
0.6
0.8
1.0Score
Calibration Curve: Precision / Recall vs Threshold
Precision
Recall
Figure 7: Evaluating PubMedBERT [9] matcher on the calibration set under different thresholds. The
selectedτ ∗ = 0.5(dashed line) achieves the best overall performance.
21

## Page 22

A.6 Token Efficiency
We assess token efficiency from two complementary perspectives, namely the per-prediction cost
and the longitudinal coverage delivered per input token. A direct comparison of raw token counts
suggests that ICU-Evo is more expensive than the local-window and RAG baselines. This view,
however, omits a central design objective of ICU-Evo, which is to surface broad trajectory context at
every prediction step. We therefore report a coverage-normalized metric alongside the raw cost.
Per-prediction cost.We report the average input and total tokens per prediction on the Qwen run,
with RAG projected to match the call volume of the local-window baseline. ICU-Evo is not the
cheapest configuration in raw tokens, yet it is substantially cheaper than full-context prompting while
remaining more expensive than the local-window and RAG baselines, as shown in Table 9.
Coverage-normalized efficiency.To account for the trajectory context that each mode actually
surfaces, we define the covered windows per prediction as 1 for the local-window baseline, 1 +k for
RAG with k retrieved windows, and window_index+ 1for ICU-Evo and the full-context baseline,
reflecting the current window together with all accumulated prior context. We then report the covered
windows per million input tokens and the input tokens consumed per covered window on thePatient
Statustask. Once normalized by timeline coverage, ICU-Evo becomes the most input-efficient mode,
achieving the highest coverage density and the lowest input-token cost per covered window, as shown
in Table 10.
Taken together, these two views indicate that, although ICU-Evo consumes more tokens per prediction
than the local-window baseline, it delivers substantially denser longitudinal context per input token,
which reflects better token utilization for timeline-aware reasoning in the ICU.
Table 9: Per-prediction token cost onRealICU-Scalewith Qwen3-235B [34].
Mode Predictions Input tokens Avg. input / pred. Avg. total / pred.
Full-context 11,065 405,300,948 36,629.10 36,763.84
Local-window 11,862 25,382,499 2,139.82 2,319.49
RAG (projected) 11,862 83,797,771 7,064.39 7,318.39
ICU-Evo 11,862 254,272,587 21,435.90 21,971.55
Table 10: Coverage-normalized input efficiency on Patient Status.
Mode Covered windows Windows / 1M input tok. Input tok. / window
Full-context 5,112,589 12,614.30 79.28
Local-window 11,862 467.33 2,139.82
RAG 6,130 541.32 1,847.34
ICU-Evo 6,304,410 24,793.90 40.33
22

## Page 23

B Dataset Details
B.1 Dataset Statistics
Cohort StatisticsFigure 8 summarizes the demographic and clinical composition of the selected
94-patient cohort across six dimensions: disease category, ICU stay duration, age, sex, stay duration
stratified by survival outcome, and mean event density per window stratified by outcome.
To categorize each ICU stay with disease types, we extract the diagnosis code closest in time to
ICU admission. ICD-9 and ICD-10 codes were then mapped to broad disease categories using a
rule-based grouping based on ICD chapters, with sepsis-related codes grouped into a dedicated Sepsis
and Severe Infection category. Specifically, the largest disease group was Cardiovascular Disorders
(32.98%), followed by Sepsis and Severe Infection (15.96%), Injury/Poisoning (13.83%), Respiratory
Disorders (10.64%), and Gastrointestinal/Hepatic Disorders (8.51%). The remaining categories were
less common: Neurological Disorders (4.26%); Clinical Signs/Symptoms, Congenital Disorders,
Infectious Diseases, and Oncology (2.13% each); and Endocrine/Metabolic Disorders, Hematologic
Disorders, Musculoskeletal Disorders, Psychiatric Disorders, and Renal/Genitourinary Disorders
(1.06% each). In the pie chart, disease categories below 5% were merged into Others
Cardiovascular Disorders
33.0%
Others
18.1%
Sepsis & Severe Infection16.0%
Injury/Poisoning
13.8%
Respiratory Disorders
10.6%
Gastrointestinal/Hepatic Disorders
8.5%
Disease Category Distribution
0 216 432 648 864 1080 1296 1512 1728 1872
ICU stay duration (hours)
0
5
10
15
20
25ICU stays
median = 208 h
72 h bins
ICU stay duration distribution
15 25 35 45 55 65 75 85 95
Age (years)
0
2
4
6
8
10
12Count
median = 69.3
Patient age distribution
Female Male
0
10
20
30
40
50
60Patients
39
55
Patient sex distribution
Survived Died
0
250
500
750
1000
1250
1500
1750ICU stay duration (hours)
ICU duration grouped by outcome
Survived Died
20
40
60
80Mean events per window
Mean event density per window by outcome
Figure 8: Cohort Demographics and Clinical Characteristics of the 94-PatientRealICUCohort
RealICU-GoldLabel StatisticsFigure 9 summarizes the distributional properties of REALICU-
GOLD. The coverage histogram exhibits a long-tail distribution, with windows concentrated within
the first 120 hours after ICU admission and a long right tail extending past 1,200 hours, yielding
a median position of 74.8 hours. ThePatient Statusdistribution is dominated by Stable windows
(63.0%), followed by Deteriorating (22.4%) and Improving (14.6%). For the set-valued tasks,Acute
Problemsis tightly concentrated around two concurrent problems per window, whereasRecommended
Actionsexhibits a heavier-tailed distribution with a small number of windows reaching twelve or
more concurrent recommendations, reflecting the variable cognitive load of ICU management.Red
Flag Actionsremain rare by design, with a median of one per window and most windows containing
zero or one event.
RealICU-ScaleLabel StatisticsFigure 10 summarizes the distributional properties ofRealICU-
Scale. The coverage histogram exhibits a long-tail distribution, with windows concentrated within the
first 336 hours after ICU admission and a long right tail extending past 1,800 hours, yielding a median
position of 207.8 hours. ThePatient Statusdistribution is dominated by Stable windows (68.8%),
followed by Deteriorating (23.1%) and Improving (8.2%). For the set-valued tasks,Acute Problems
is tightly concentrated around two to three concurrent problems per window, whereasRecommended
Actionsexhibits a heavier-tailed distribution with a small number of windows reaching ten or more
concurrent recommendations, reflecting the variable cognitive load of ICU management.Red Flag
Actionshas a median of one per window and most windows containing zero or one event.
23

## Page 24

0 120 240 360 480 600 720 840 960 1080 12001248
Hours since ICU admission
0
50
100
150
200
250
300Windows
median = 74.8
24 h bins
Coverage across ICU timeline
Improving
14.6%
Stable
63.0%
Deteriorating
22.4%
Patient status label distribution
0 1 2 3 4
Number of active problems
0
100
200
300
400
500Windows
median = 2
Active problems per window
0 1 2 3 4 5 6 7 8 9 12 13 14
Number of recommended actions
0
50
100
150
200
250
300Windows
median = 2
Recommended actions per window
0 1 2 3
Number of red flags
0
100
200
300
400Windows
median = 1
Red flags per window
Figure 9:RealICU-Goldstatistics and label distribution for Patient Status, Active Problems, Recom-
mended Action, and Red Flags.
0 168 336 504 672 840 1008 1176 1344 1512 1680 1848
Hours since ICU admission
0
200
400
600
800
1000Oracle windows
median = 207.8
24 h bins
Coverage across ICU timeline
Improving
8.2%
Stable
68.8%
Deteriorating
23.1%
Patient status label distribution
0 1 2 3 4 5
Number of active problems
0
1000
2000
3000
4000
5000
6000Windows
median = 2
Active problems per window
0 1 2 3 4 5 6 7 8 9 10 12
Number of recommended actions
0
500
1000
1500
2000
2500
3000
3500
4000Windows
median = 2
Recommended actions per window
0 1 2 3 4
Number of red flags
0
1000
2000
3000
4000
5000
6000Windows
median = 1
Red flags per window
Figure 10:RealICU-Scalestatistics and label distribution for Patient Status, Active Problems,
Recommended Action, and Red Flags.
24

## Page 25

B.2RealICU-GoldCross Validation
RealICU-Goldcontains 930 windows in total. For each window, we invite at least two out of five
senior physicians for annotation. And we run a cross-validation check after annotation to maintain
the golden-standard labels. In Table 11, we report the detailed number of each labels before and
after cross-validation. Only labels with agreements are kept intoRealICU-Gold. Note thatActive
Problems,Action Recomm., andRed Flagsare stored as sets with multiple labels per window.
Table 11: Label-wise statistics of REALICU-GOLDafter cross-validation filtering.
Task N labels raw N labels kept Keep rate
Patient Status930 921 99.0%
Active Problems2,170 2,066 95.2%
Action Recomm.2,328 2,198 94.4%
Red Flags1,220 1,058 86.7%
B.3 Dataset Pre-processing
To obtain our underlying base dataset of trajectories that cover ICU stays as well as their preced-
ing patient journey, we merge MIMIC-IV [16], MIMIC-ED [16], MIMIC-Note [16], MIMIC-IV-
ECHO [16], MIMIC-IV-ECG and MIMIC-CXR [15].
By this, we include not only patient meta data such as demographics, insurance, etc., but a diverse
holistic timeline of medication, online medical records, vital measurements, X-ray, electro- and
echocardiograms, procedures, diagnosis, lab results, text reports, and transfers. We also include
triaging data, subject to availability. From MIMIC-Note, we use the entire contents of the discharge
summaries and the findings sections from radiology reports. In total, our resulting base dataset
comprises 73,181 ICU stays from 50,920 patients.
We arrange all charted information and measurements along a time axis together with patient age
and time delta to the beginning of the specific ICU stay and sort them temporally ascending. Full
duplicates are eliminated. Encoded categorical information from established ontologies and coding
systems, e.g. for diagnosis (ICD) or medication (GSN), are resolved to their full-text descriptions.
Text data is cleaned according to a permissive policy, only adjusting e.g. consecutive whitespace
characters and unambiguous processing artifacts. Numerical data is also represented textually together
with the respective unit of measurement and description. While we directly include all textually
representable information and numeric measurements, we limit the integration of imaging and
waveforms to their metadata, leaving the utilization of the X-ray, ECG, and ECHO contents to future
work. We ensure that patient data is not leaked across our dataset splits.
Further, we account for inaccurate charting and limitations of raw data collection by conservatively
establishing an adversarial tolerance of 24h for key events such as discharge. In case of multiple
records for the same event with different precision (e.g. death), usually originating from different
tables in the raw dataset, we default to the most fine-grain timestamp.
25

## Page 26

C Memory-Augmented Agents for Clinical Decision Support
We position ICU-Evo as an instance of the broader class of memory-augmented language agents.
In the following, we discuss a generic formulation of the class, several specific instantiations from
recent work, and the design choices that motivate ICU-Evo.
C.1 Formulation
A memory-augmented agent processes a stream of inputs {x1, x2, . . . , xT } while maintaining an
evolving memory state. At stept, the update and decision rules take the generic form
Mt =U(M t−1, xt), y (k)
t =f (k)(Mt),(8)
where Mt is the memory state, U is an update operator that integrates the latest input into memory,
and f(k) is a task-specific decision function realized as a prompted call of the underlying language
model. Different memory systems differ primarily in the structure of Mt and in the choice of U, and
the structural choices that define a memory system reduce to three questions. Whattypesof content
does Mt contain, at whattemporal scaleis each type maintained, and under whatupdate policydoes
each type evolve?
C.2 Instantiations
We describe three instantiations of Eq. 8 in whichM t takes increasingly heterogeneous forms.
Compressive Stream Memory.AgentFold [ 36] sets Mt as an ordered sequence of summary blocks
together with a high-fidelity record of the latest interaction. The update operator U is a learned
folding policy that, at each step, either condenses the latest interaction into a fine-grained block or
consolidates a contiguous span of prior blocks into a single coarse-grained block. This instantiation
supports streaming inputs and adaptive scale, while committing all memory content to a single
representational type (textual summary) under a single update rule (replacement by summarization).
Cross-Task Experience Memory.Evo-Memory [ 32] sets Mt as an unordered set of prior task
experiences, each encoded as a structured tuple (xi,ˆyi, fi), where fi is a feedback signal. The update
operator U is append-with-pruning, and a separate refine action lets the agent reorganize or discard
memory entries during decision-making. This instantiation targets cross-task transfer rather than
within-task dynamics, and treats each task as the atomic unit of memory.
Linked Note Memory.A-Mem [ 33] sets Mt as a collection of atomic notes, where each note
is a tuple of raw content, timestamp, LLM-generated keywords, tags, and contextual description,
a dense embedding, and a set of links to other notes. The update operator U is realized in two
LLM-driven steps. On arrival of a new note, top- k retrieval over the embedding space surfaces
candidate neighbors, and an LLM decides which neighbors deserve a semantic link. The same
neighbors are then re-examined, and the LLM may rewrite the contextual description, keywords,
or tags of any neighbor in light of the new note. This instantiation supports streaming inputs and
introduces evolution of prior entries, while committing all memory content to a single note schema
under a single LLM-driven update rule.
Table 12: ICU-Evo’s memory components and the corresponding agent update operator.
Component Definition Updated by
Mwork Recent raw observations at full resolution. Observation Agent
Mtrend Piecewise-constant segmentations of vitals and labs. Observation Agent
Mevent Append-only log of critical events. Assessment Agent
Mtraj Compressed episode-level narrative of the stay. Assessment Agent
Minsight Patient-specific hypotheses with supporting and counter-evidence. Insight Agent
26

## Page 27

C.3 ICU-Evo as Heterogeneous Clinical Memory
ICU-Evo setsM t as a tuple of five components,
Mt =

Mwork
t , Mtrend
t , Mevent
t , Mtraj
t , Minsight
t
	
,(9)
defined in Table 12. Algorithm 2 formalizes the full inference loop and the pipeline of three agents
that realize the update operator U at different temporal cadences over the shared memory state. At
every window t, the Observation Agent ingests the new measurements xt and updates Mwork
t by
per-window overwrite and Mtrend
t by piecewise aggregation. Every ka windows, the Assessment
Agent compresses the recent working and trend memory into a trajectory summary zt, appended to
Mtraj
t as a multi-scale rollup, and detects newly emerging critical events ˜Et, appended to Mevent
t
under severity gating. Every ki windows, the Insight Agent proposes patient-specific hypotheses,
gathers supporting and counter-evidence from Mevent
t , and the Orchestrator commits the accepted
hypotheses to Minsight
t via lifecycle transitions. The Predictor then queries the consolidated memory
state to emit task-specific predictionsy (k)
t , decoupled from the memory update cycle.
The five components form principled correspondences with prior designs, recombined under a
common formulation. Mwork
t and Mtraj
t mirrors the multi-scale summaries of AgentFold [36], the
lifecycle-managed update of Minsight
t mirrors both the rewriting of prior notes in A-Mem [33] and
the refine action of Evo-Memory [32].
Algorithm 2ICU-Evo Memory-Augmented Agent System.
Require:LLM backboneF; ICU stays; window sequence{x t}T
t=1; static contextc; agent periodsk a, ki
1:Initialize memoryM 0 ▷work, trend, event, traj, insight
2:foreach windowt= 1, . . . , Tdo
3:
 
Mwork
t , Mtrend
t

←Observe
 
Mwork
t−1 , Mtrend
t−1 , xt

▷Observation Agent; every window
4:iftmodk a = 0then▷Assessment Agent fires everyk a windows
5:
 
zt, ˜Et

← F
 
Mwork
t−ka:t, Mtrend
t−ka:t

6:M traj
t ←M traj
t−1 ∪ {zt};M event
t ←M event
t−1 ∪ ˜Et
7:end if
8:iftmodk i = 0then▷Insight Agent fires everyk i windows
9:∆H← F
 
Minsight
t−1 , Mevent
t−ki:t

▷propose/update hypotheses
10:foreach hypothesish∈∆Hdo
11:state(h)←acceptifs(h)> r(h)elsereject
12:end for
13:M insight
t ←Orchestrator
 
Minsight
t−1 ,∆H

14:end if
15:foreach taskkdo▷Predictor decoupled from memory update
16:y (k)
t ← F(k) 
Mt;c

17:end for
18:end for
19:returnpredictions{y (k)
t }for evaluation againstRealICUlabels
C.4 Discussion
The instantiations above demonstrate the flexibility of Eq. 8, yet alternative combinations remain
possible. The heterogeneous decomposition we adopt reflects that clinical reasoning under partial
observability proceeds along multiple simultaneous modes. A homogeneous memory forces a single
answer to three independent questions: at what temporal scale to retain content, at what fidelity, and
under what update policy. AgentFold [36] couples scale and fidelity under a uniform textual summary
type, fitting neither append-only event logs nor lifecycle-managed hypotheses. A-Mem [33] couples
all three under a uniform note schema and LLM-driven evolution rule, providing no mechanism for
the distinct update policies that event detection and hypothesis lifecycle management each require.
Evo-Memory [32] treats each task as the unit of experience, fitting cross-task transfer but leaving
within-patient dynamics unaddressed. The heterogeneous memory structure of ICU-Evo in Eq. 9
offers a frameworks to align previous designs into real clinical reasoning over evolving patient states.
27

## Page 28

D Case Study
D.1 Failure Case: Recall Safety Tradeoff
Patient background: Age 55. Female, entering ICU with severe subarachnoid hemorrhage. Course
complicated by severe intracranial hypertension (ICP >40 mmHg) managed with mannitol, propofol,
and right frontal EVD placement. Current 191.5–192.0 hours after ICU admission (day-8).
Current-window events
11:16Impaired Tissue Perfusion NCP – Therapeutic temperature management
11:16Impaired Tissue Perfusion NCP – Pressors
11:17Infection NCP – Monitor and assess respiratory secretions
11:17Impaired Tissue Perfusion NCP – Monitor neuro assessment
11:17Impaired Tissue Perfusion NCP – Monitor hemodynamic status q1h
. . . (63 further entries)
Memory snapshot
Working memory:68 events from the current window.
Trend memory:None at current window.
Critical events:08:16 VITALS Richmond-RAS Scale=−4.00; 11:00 VITALS Intra Cranial Pressure 21.0 mmHg; . . .
Trajectory:This patient exhibits a highly coupled neuro-respiratory deterioration, demonstrating acute and severe
hypoxemia simultaneously with sudden intracranial pressure spikes . . .
Insight #6:This patient exhibits extreme ICP volatility, demonstrating sudden, severe ICP spikes that break through
maximal medical management, including deep sedation, neuromuscular blockade, and targeted temperature management.
Expect a higher-than-average risk of sudden, refractory intracranial crises and secondary cerebral hypoperfusion despite
seemingly stable baseline ICP, requiring aggressive, anticipatory hyperosmolar or surgical interventions.
Gold annotation
Patient Status.Deteriorating.
Active Problems.Refractory intracranial hypertension and impending herniation; worsening hypernatremia and hyperos-
molality (Na 155 mEq/L, osm 325 mOsm/kg); ventilator-associated pneumonia.
Recommended Actions.Therapeutic temperature management; monitor and assess respiratory secretions.
Red Flags.Routine hyperosmolar therapy (mannitol or hypertonic saline) — further routine administration is contraindi-
cated and dangerous under current sodium and osmolality; emergency bolusing only as a last resort for acute herniation.
ICU-Evo predictions (recommended actions)
1. Urgent neurosurgery and neurocritical care consultation.[unmatch]
2. Administer hyperosmolar therapy. Boluses of mannitol or 3% hypertonic saline for sustained ICP >20–
22 mmHg.
[red flag]
3. Maintain CPP>70 mmHg. Continuous norepinephrine to meet MAP goals.[match]
4. Initiate goals-of-care discussion.[unmatch]
5. Strict glycemic and electrolyte monitoring (q1–2h K, glucose).[unmatch]
Figure 11: Recall-safety tradeoff case study. ICU-Evo’s stored insight #6 prescribes “aggressive,
anticipatory hyperosmolar interventions,” which propagates to prediction 2 — flagged as contraindi-
cated by the gold annotation under current Na/osm. The trend layer carries no sodium signal forward,
so nothing counterweighs the stored frame.
28

## Page 29

D.2 Failure Case: Anchoring Bias
Patient background: Adult patient with Eisenmenger’s physiology, severe right ventricular dysfunc-
tion, and chronic right-to-left shunting with polycythemia. Baseline SpO 2 85–93%. Prior course
marked by refractory hypoxemia (SpO2 nadir 77% on FiO2 100%) unresponsive to maximal high-flow
oxygen and ongoing diuresis. Current 87.5–88.0 hours after ICU admission (day-4).
Current-window events
18:48BODY_INPUT Oral/Gastric Ingredient = 300 ml
18:48BODY_INPUT PO Intake = 300 ml
18:48BODY_INPUT Water = 300 ml
18:48VITALS Weight = 51.8 kg
(4 events total; no vitals stream this window)
Memory snapshot
Working memory:4 events from the current window.
Trend memory:No vital signal this window (HR/RR/SpO 2/BP/MAP/Temp all empty).
Critical events:02-03 13:00 VITALS SpO 2 77% on FiO2 100%; 02-04 06:00 VITALS O2 Flow 35 L/min; 02-04 22:00
BODY_OUTPUT V oid 700 ml; . . .
Trajectory:This patient demonstrates a coupled refractory-hypoxemia and preload-dependence pattern, where standard
oxygen escalation fails to correct shunt-driven desaturation and successful volume offloading precipitates hemodynamic
collapse . . .
Insight #2:This patient demonstrates refractory hypoxemia that is unresponsive to maximal high-flow oxygen therapy
and ongoing diuresis. Expect below-average improvement in oxygenation indices from standard volume offloading, likely
due to underlying pulmonary hypertension and fixed V/Q mismatch or shunting.
Gold annotation
Patient Status.Stable.
Active Problems.Hypotension and reduced cardiac output (preload-sensitive); volume overload risk under chronic
right-heart strain.
Recommended Actions.BODY_INPUT Water (oral intake); VITALS Weight (daily tracking).
Red Flags.Titrating supplemental oxygen to SpO 2 > 95% — baseline SpO 2 is 85–93% from chronic right-to-left
shunting and polycythemia; oxygen should be administered only if SpO 2 drops below 85% or the patient becomes
symptomatic.
ICU-Evo predictions (recommended actions)
1. Hold or reduce diuretic therapy. Suspend or decrease loop diuretics and reassess volume status before
further diuresis.
[unmatch]
2. Titrate norepinephrine to maintain MAP> 65 mmHg, weaning cautiously if hemodynamics remain stable. [unmatch]
3. Monitor serum potassium via basic metabolic panel or venous blood gas.[unmatch]
4. Maintain targeted oxygenation. Continue 4 L/min nasal cannula to target SpO2 88–92%, avoiding over-
oxygenation.
[red flag]
Figure 12: Premature-anchoring case study. The window contains four events — oral water and a
daily weight — and the gold status is stable. ICU-Evo’s stored insight #2 carries forward the prior
cardiopulmonary story of refractory hypoxemia, propagating to prediction 4, which prescribes an
active oxygen target (88–92%) that the gold annotation marks as contraindicated under this patient’s
Eisenmenger baseline. The trend layer is empty for the current window, so nothing pulls the model
back to the simpler window-grounded interpretation.
29

## Page 30

D.3 Memory Snapshot
ICU-Evo memory snapshot — window 120, 87.5–88.0 h
Working Memoryrecent windows, raw events
previous windows:17 events (windows 118–119, omitted)
current window(window 120, 87.5–88.0 h, 4 events):
2152-02-06 18:48 BODY_INPUT Oral/Gastric Ingredient, ml = 300.00
2152-02-06 18:48 BODY_INPUT PO Intake, ml = 300.00
2152-02-06 18:48 BODY_INPUT Water, ml = 300.00
2152-02-06 18:48 VITALS Weight = 51.80
Trend Memoryvital-sign aggregates, two scopes
current windownone
global(windows 0–120, 0.0–88.0 h, 3422 raw events):
heart_rate_bpm: mean = 68.97, min = 58.00, max = 85.00, count = 97
resp_rate_per_min: mean = 13.16, min = 8.00, max = 30.00, count = 96
spo2_percent: mean = 89.87, min = 77.00, max = 100.00, count = 97
map_mmhg: mean = 75.00, min = 47.00, max = 99.00, count = 88
. . . (sbp, dbp, temperature omitted)
Critical Events Memorysalient events that change patient story
previous episodes:38 events (episodes 1–9, hours 0.0–79.5, omitted)
current episode(episode 10, hours 80.0–87.5):
(no critical events extracted)
Trajectory Memoryepisode-level summaries
episode 1(hours 0.0–7.5): The patient was admitted to the MICU for management of acute decompensated heart failure,
acute kidney injury, and hypercapnic respiratory failure. Respiratory support was initiated with high-flow nasal cannula at
35 L/min and 65% FiO2, . . .
...
episode 10(hours 80.0–87.5): The patient began the block with stable hemodynamics (MAP 70 mmHg) and borderline
oxygenation (SpO2 88%) on 4 L/min nasal cannula. Throughout the period, mean arterial pressures were maintained
between 70 and 80 mmHg, demonstrating sustained hemodynamic stability. Respiratory status remained stable, with
oxygen saturations ranging from 88% to 94% on unchanged nasal cannula support . . .
Insight Memorypersonalized hypotheses with supporting and counter evidence
insight #1:This patient exhibits a paradoxical and rapid escalation in serum potassium despite ongoing loop diuretic
therapy. Expect an above-average risk of severe hyperkalemia and resistance to standard potassium-wasting effects of
furosemide.
supporting:03:20 LAB_TEST Potassium = 7.30 mEq/L
counter:03:20 LAB_TEST Creatinine = 1.90 mg/dL
insight #2:This patient demonstrates refractory hypoxemia that is unresponsive to maximal high-flow oxygen therapy
and ongoing diuresis. Expect below-average improvement in oxygenation indices from standard volume offloading, likely
due to underlying pulmonary hypertension and fixed V/Q mismatch or shunting.
supporting:
13:00 VITALS O2 saturation pulseoxymetry, =77.00 %
13:00 VITALS Inspired O2 Fraction =1 00.00
counter:
06:00 VITALS Inspired O2 Fraction =60.00
06:00 VITALS O2 Flow = 35.00 L/min
. . . ...
Figure 13: ICU-Evo memory snapshot at 87.5–88.0 hours after admission. The five layers of memory
together constitute the full state available to the prediction modules at this window, including working
memory, trend, critical events, trajectory, and patient-specific insights. Red highlights mark the thread
most relevant to the case study in Figure 12.
30

## Page 31

E Prompts
E.1 Oracle Prompt
Oracle Prompt
You are Oracle, a clinical AI evaluator with hindsight access to a patient’s full ICU trajectory.
Your task is to evaluate a specific local observation window {window_time} across two parts.
=== PART 1: PATIENT ASSESSMENT ===
[1A. CURRENT STATUS]
Assess the patient’s clinical direction at this window by reasoning across four domains: Hemodynamics,
Respiratory, Renal/Metabolic, Neurology
Synthesize your domain reasoning into a single overall status label:
- improving: indicators trending toward recovery relative to the provided context
- stable: no meaningful change in either direction
- deteriorating: indicators trending toward worsening relative to the provided context
- insufficient_data: available information is not sufficient to make a reliable judgment (e.g., sparse
events, conflicting signals)
Important nuances:
- Do NOT conflate outcome with care quality. A patient may be deteriorating despite excellent care.
- A patient may be labeled stable or improving even if they eventually die, if the trajectory at this
window genuinely reflects that direction.
[1B. ACTIVE PROBLEMS]
Using the full trajectory and current window, identify active clinical problems or emerging risks this
patient faces going forward from this window.
- Only include risks that are real and imminent or already developing --- not distant or hypothetical
- Each risk must be tied to specific trajectory evidence
- An empty list is expected and acceptable when no urgent risks are present
=== PART 2: ACTION REVIEW ===
[2A. ACTION EVALUATION]
Evaluate each clinical action taken during this window. For each action, integrate two perspectives
into a single judgment:
- Guideline alignment: does this action follow established ICU guidelines (e.g., Surviving Sepsis
Campaign, ARDSNet, PADIS, AHA/ACC where relevant)?
- Contextual appropriateness: given this patient’s specific condition, trajectory, comorbidities, and
the eventual outcome known to you, was this action appropriate?
Assign one overall label:
- best_practice: action is both guideline-aligned and well-suited to this patient’s specific situation
- acceptable: action is reasonable given the context, even if not optimal or if guidelines are
ambiguous
- potentially_harmful: action poses real risk of harm to this patient, whether due to guideline
violation, patient-specific contraindication, or both
- insufficient_data: not enough context to evaluate this action reliably
Use your hindsight knowledge to inform the judgment, but be fair: judge the action against what the
context reveals, not against impossible foresight. If an action was reasonable at the time but later
context revealed a missed diagnosis, note this nuance explicitly in the rationale.
The action can be identified by its code, which includes and are not limited to: DRUG_START, DRUG_STOP,
DRUG_PRESCRIPTION, BODY_INPUT, TRANSFER, LAB_TEST, DIAGNOSIS.
[2B. RED FLAGS]
Using the full trajectory and current window, identify any actions that should be strictly avoided for
this specific patient going forward.
- Only flag actions that a reasonable clinician might consider but would be harmful for this specific
patient --- do not list generic contraindications unless directly applicable here
- Each flag must be justified by patient-level evidence (comorbidities, trajectory events, organ
function, known sensitivities)
- An empty list is expected and acceptable when no red flags are present
=== PATIENT ICU CONTEXT WINDOW ===
31

## Page 32

{patient_icu_trajectory}
Now, evaluate the CURRENT OBSERVATION WINDOW according to the instructions above.
E.2 Agent Prompt
Assessment Agent Prompt
You are an ICU assessment agent. You compress {k} consecutive 30-minute windows
({duration} hours total) into one episode summary and identify the block’s
critical events.
=== INPUT ===
[PATIENT METADATA] (read-only context)
{patient_metadata}
[PRIOR EPISODE SUMMARY] (read-only context)
Used only to distinguish new from continuing findings and to calibrate baseline.
Do not cite from it.
{prior_episode_summary_text}
[EPISODE TIME RANGE]
{episode_start_time} to {episode_end_time}
[WINDOWED ICU DATA]
You receive:
- Raw events for each window, formatted as ‘[<event_id>] <time> <event_name> <payload>‘
- One grouped ‘selected vital trends‘ section summarizing tracked vitals across the whole block
- In the trend section, only windows with at least one value for that vital are shown,
plus an overall summary across the block
{episode_input}
=== TASK ===
Produce (1) an episode summary and (2) a list of critical events.
[TASK 1: EPISODE SUMMARY] (3--6 sentences)
Narrate the block’s clinical trajectory: where the patient started the block, what
meaningfully happened, where they ended, and what remains unresolved. Focus on
direction of travel and inflection points, not a window-by-window recap.
- Use specific numeric values at inflection points; avoid adjective-only descriptions
("rising", "unstable") without numbers.
- Include sustained abnormal states only when their persistence is the point
(e.g., tachycardia held across the block despite intervention).
- When the prior summary establishes a condition or intervention, frame current
findings as continuation, escalation, or resolution, not new onset.
- Stay descriptive and temporal. Do not assign diagnoses, syndromes, or mechanisms
that are not explicitly in the input.
- Refer to events by clinical name in prose. Event IDs appear only in
‘supporting_event_ids‘.
[TASK 2: CRITICAL EVENTS]
A critical event is a high-SNR inflection point in the patient’s ICU trajectory:
a moment that materially changes the clinical story. Reading only the critical
events, a clinician should be able to reconstruct the shape of the block.
Critical events typically fall into one of these categories:
- New or worsening organ dysfunction (respiratory, cardiovascular, renal, hepatic,
neurological).
- Resolution or meaningful improvement of existing organ dysfunction.
- Initiation of a major intervention (intubation, vasopressor start, dialysis,
transfusion for active bleed, emergency procedure).
- Diagnosis scores, such as GCS, RASS, or SOFA scores.
- Significant escalation or de-escalation of care reflecting a change in trajectory.
An event qualifies only if it is clinically meaningful on its own, changes how
32

## Page 33

subsequent data should be read, and is corroborated by surrounding trend or events
rather than an isolated outlier.
Exclude routine readings, scheduled medications without clinical context, or noisy
measurements.
Err toward under-listing. If no event meets the bar, return an empty list.
Insight Agent
You are a clinical insight agent. Your job is to identify how THIS patient deviates
from the population-average ICU patient in similar circumstances, specifically in how
they respond to illness and interventions, or how their physiology is trending
relative to what the current illness and treatment would predict.
You are generating patient-specific response profiles and trajectory deviations that
would change how future data should be interpreted or how future decisions should be
weighted.
You will be given:
- The patient’s existing hypothesis bank (all hypotheses, active and retired)
- Patient metadata with compressed pre-ICU history, for background context only
- The latest episode:
- Clinical trajectory summary
- Critical events, formatted as ‘<event_id> <time> <event_name> <payload>‘
- Vital trend statistics
=== INPUT ===
[EXISTING HYPOTHESES]
{hypothesis_bank}
[PATIENT METADATA]
{patient_metadata}
[LATEST EPISODE SUMMARY]
{episode_summary}
[LATEST EPISODE CRITICAL EVENTS]
{critical_events}
[LATEST EPISODE VITAL TRENDS]
{vital_trends}
=== TASK ===
[TASK 1: EVIDENCE FOR EXISTING HYPOTHESES]
This is a matching task. Scan the episode for evidence bearing on each active
hypothesis. Do not infer beyond what is stated.
For each hypothesis where the episode provides relevant signal, report:
- ‘supporting_evidence‘: event IDs or ‘vital_trend‘ that reinforce it
- ‘counter_evidence‘: event IDs or ‘vital_trend‘ that weaken it
Updates must cite at least one piece of evidence. No citation, no update.
Skip hypotheses with no relevant signal.
[TASK 2: NEW HYPOTHESIS GENERATION]
This task requires reasoning. Before proposing a new hypothesis, mentally construct
the population-average trajectory for a patient with this illness receiving these
interventions, then compare to what you observe. Only flag a new hypothesis where
this patient’s pattern meaningfully departs from that reference.
A valid new hypothesis must:
- Describe an individualized response profile or trajectory deviation (not a
diagnosis, not an event restatement)
- Be grounded in evidence
- Include an expected deviation from population-average response (e.g.,
"below-average," "slower than typical")
- Be clinically actionable or prognostically relevant
Over-generation is worse than under-generation. Generate at most 2 new hypotheses;
if more candidates exist, report only the strongest.
Do not flag obvious, trivial, or diagnosis-shaped claims. Empty list is acceptable
and often correct.
33

## Page 34

[GROUNDING RULES]
- Cite only event IDs that appear in the critical events block, or the token
‘vital_trend‘ for claims grounded in trend statistics.
- Do not invent events, values, or clinical facts not present in the provided inputs.
[EXAMPLES OF VALID NEW HYPOTHESES]
Example A --- individualized response profile:
"This patient shows diminished hemodynamic response to fluid resuscitation.
Expect below-average MAP rise to standard fluid boluses."
Example B --- trajectory deviation:
"This patient’s respiratory recovery is progressing slower than typical for their
current ventilator settings and sedation level. Expect below-average improvement
in oxygenation indices over the next shift."
E.2.1 Predictor Prompt
Shared Prompt
You are a clinical decision support AI. Assess the patient’s overall clinical
status for the current ICU window.
=== INPUT ===
You will receive one of:
(A) Raw ICU events in chronological order
(B) A structured Memory object with the following layers:
- patient_metadata
- working_memory : raw events from recent windows --- current local status
- trend_memory : per-window vital trend statistics
- critical_events_memory : episode-level critical events
- trajectory_memory : episode summaries
- insights : patient-specific deviations from typical ICU trajectories
Patient Status Predictor
=== INSTRUCTIONS ===
Assess the patient’s clinical direction at this window by reasoning across four
domains:
- Hemodynamics : heart rate, MAP, lactate, perfusion, vasopressor requirements
- Respiratory : SpO2, PaO2/FiO2, respiratory rate, ventilator settings
- Renal/Metabolic: creatinine, urine output, electrolytes, acid-base status
- Neurology : GCS, mental status, RASS sedation score
Synthesize your domain reasoning into a single overall status label, weighted by
the relative clinical importance of each domain for this specific patient:
- improving : indicators trending toward stability or recovery relative
to the provided context
- stable : no meaningful change in either direction
- deteriorating : indicators trending toward worsening or decompensation
relative to the provided context
- insufficient_data : available information is not sufficient to make a reliable
judgment (e.g., sparse events, conflicting signals)
Active Problems Predictor
=== INSTRUCTIONS ===
Identify active clinical problems or emerging risks this patient faces going
forward from this window.
- Only include risks that are real and imminent or already developing --- not
distant or hypothetical
- Each risk must be tied to specific trajectory evidence
- An empty list is expected and acceptable when no urgent risks are present
34

## Page 35

Action Recommendation Predictor
=== INSTRUCTIONS ===
1. Recommend up to {int(top_k_actions)} distinct actions that are clinically
actionable in the next {float(prediction_horizon_hours):g}-hour horizon.
2. Only recommend actions that are clearly justified by the available data.
3. It is totally acceptable to return fewer than {int(top_k_actions)}. If data
is insufficient to justify a recommendation with at least low confidence,
omit it.
4. Order actions from highest to lowest clinical priority (rank 1 = most urgent).
5. Prioritize interventions with the highest expected impact on short-term
stability and outcome.
6. Ground every recommendation strictly in the provided context. Do not infer
or invent missing data.
Red Flag Actions Predictor
=== INSTRUCTIONS ===
Using the full trajectory and current window, identify any actions that should
be strictly avoided for this specific patient going forward.
- Only flag actions that a reasonable clinician might consider but would be
harmful for this specific patient --- do not list generic contraindications
unless directly applicable here
- Each flag must be justified by patient-level evidence (comorbidities,
trajectory events, organ function, known sensitivities)
- An empty list is expected and acceptable when no red flags are present
35
