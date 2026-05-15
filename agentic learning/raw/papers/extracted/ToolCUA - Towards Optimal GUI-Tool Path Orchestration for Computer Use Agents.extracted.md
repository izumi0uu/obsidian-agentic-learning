# ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents - Extracted Text

- Source note: [[ToolCUA - Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents]]
- Source PDF: `assets/ToolCUA - Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents.pdf`
- Extracted: 2026-05-14
- Extractor: pypdf
- Pages: 34
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

ToolCUA: Towards Optimal GUI-Tool Path
Orchestration for Computer Use Agents
Xuhao, Hu2,1,∗, Xi Zhang1,∗, Haiyang Xu1,†, Kyle Qiao1, Jingyi Yang2
Xuanjing Huang2, Jing Shao3, Ming Yan1,†, Jieping Ye1
1Tongyi Lab, Alibaba Group 2Fudan University 3Shanghai Artificial Intelligence Laboratory
Computer Use Agents (CUAs) can act through both atomic GUI actions (e.g., click, type) and high-level tool
calls (e.g., API-based file operations), but they are often confused by this hybrid action space: they do not
know when to continue with GUI actions and when to switch to tools, and finally fail to select the optimal
execution path. This difficulty stems from two issues. First, high-quality interleaved GUI-Tool trajectories are
scarce, and collecting real tool trajectories is expensive and brittle. Second, existing supervision provides
limited guidance for GUI-Tool path selection, as most methods focus on step-level action imitation or final task
completion and offer little trajectory-level feedback on whether GUI-Tool switching leads to a more effective
execution path. In this paper, we proposeToolCUA, an end-to-end agent designed to learn optimal GUI-Tool
path selection through a staged training paradigm. We first introduce anInterleaved GUI-Tool Trajectory
Scaling Pipelinethat repurposes abundant static GUI trajectories and synthesizes a grounded library of tools,
making it possible to scale diverse GUI-Tool trajectories without manual engineering or real tool-trajectory
collection. Based on this data, we perform Tool-Bootstrapped GUI RFT, which combines warmup SFT with
single-turn RL to improve decisions at critical GUI-Tool switching points. Finally, we further optimize ToolCUA
withOnline Agentic RLin a high-fidelity GUI-Tool environment, using aTool-Efficient Path Rewardthat
encourages both appropriate tool use and shorter execution paths. Experiments on OSWorld-MCP show
that ToolCUA achieves 46.85% accuracy, a relative improvement of approximately 66% over the baseline,
establishing a new state of the art among models of comparable scale. It also improves by 3.9% over GUI-only
settings, demonstrating effective GUI-Tool orchestration. The results further suggest that training in a hybrid
action space is a promising paradigm for real-world digital agents.
Date: May 12, 2026
Author emails:{xuhaohu08}@gmail.com,{zx443053}@alibaba-inc.com
Correspondence:{shuofeng.xhy,ym119608}@alibaba-inc.com
/githubCode:https://github.com/X-PLUG/ToolCUA
Pure atomic GUI actions
GUI-Tool interleaved actions
(a) Tool augmented GUI action for Execution Efficiency
CLICK
CLICK
TYPESCROLL
MCP-based Tool callingLibreoffice_set_column_values
CLICK
 SCROLL
Rigid and fragile!
Flexible and powerful
(b) ToolCUAPerformance on OSWorld-MCP (feasible)
ToolCUA-8B (based on Qwen3-VL-
8B-Instruct)EvoCUA-32B Claude-4.5-sonnetGemini-3.1-ProQwen3.5-397B-A17B
+66%
Figure 1: (a) The advantage of Tool-augmented actions compared with pure GUI actions. (b) The performance of our
ToolCUA compared with the baselines, agentic CUAs, and general models.
∗Equal Contribution,†Corresponding Author
arXiv:2605.12481v1  [cs.AI]  12 May 2026

## Page 2

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
1. Introduction
The rapid evolution of Multimodal Large Language Models (MLLMs) [2, 3, 4, 6, 34, 59] toward agentic
capabilities[15,41,44,55]hasestablishedComputerUseAgents(CUAs)[ 18,24,28,37,39,40,46,49,62]
as a frontier topic for automating native desktop workflows. Conventionally, CUAs primarily rely on atomic
GUI actions(e.g., click and scroll), which offer broad generalizability but are susceptible to cascading errors
in long-horizon tasks. In contrast, structured tool calls [8, 27, 35, 44] provide agents with superior efficiency
and precision [61, 62]. For example, in Figure 1 (a), modifying an entire column in LibreOffice can be
completed by a single API call, whereas a pure GUI solution requires a long sequence of click and type.
However, tool-based APIs are constrained by service coverage and stability, limiting applicability in diverse
scenarios. Therefore, given their complementary strengths, a hybrid GUI-Tool action space is essential for
next-generation CUAs.
Although GUI actions and tool calls are complementary, simply exposing both action space to an MLLM
does not solve the problem. In practice, agents are oftenconfused by the hybrid action space. As shown in
Table 1, some models (e.g., Qwen3VL-235B-A22B) overuse tools with higher Tool-Calls (e.g., average 6.10
tool-calls)andhurttasksuccess(e.g., from41.14%to38.14%), whileothers(e.g., Qwen3VL-8B)underutilize
the provided tools, remaining overly GUI-centric (e.g., average 0.003 tool calls) and almost never invoke
tools even when the more efficient tool calls are available. We formalize this challenge, illustrated in Figure
2, asoptimal GUI-Tool path selection: dynamically determining when to use GUI actions and when to
invoke tools so as to form an efficient and reliable task trajectory. Unlike step-level action selection, this is
inherently a trajectory-level policy learning problem, as each GUI-to-Tool or Tool-to-GUI switching decision
not only solves the immediate step, but reshapes the entire subsequent trajectory in terms of efficiency and
reliability.
To this end, existing approaches fall short in two fundamental aspects. First,current CUAs are often
undertrained on tool use, exhibiting a deficit in tool-calling knowledge. This limitation is rooted in the
lack of high-quality interleaved GUI-Tool trajectories. In real computer-use environments, usable tools are
difficult to obtain and maintain. Specifically, APIs are often application-specific, incomplete, or unstable, and
collecting GUI-Tool data requires expensive environment instrumentation. Existing efforts [49, 54] partly
Table 1: Performance comparison between pure GUI and hybrid GUI-Tool
action spaces on OSWorld [45]. “Steps” is the average number of
trajectory steps; “Tool-calls” is the average number of tool calls. See
details in Appendix C.1.
Model Action Accuracy↑Steps↓Tool-calls
Qwen3VL-8B GUI 29.0 19.2 -
+ Tools 28.2(−0.8) 19.3 0.003
Qwen3VL-235B GUI 41.1 25.9 -
+ Tools 38.1(−2.0) 17.4 6.10
EvoCUA-32B GUI 52.6 25.0 -
+ Tools 40.5(−12.0) 26.1 7.49
Claude-4-sonnet GUI 47.7 23.6 -
+ Tools 43.5(−4.2) 19.2 4.50
Claude-4.5-sonnet GUI 61.9 23.3 -
+ Tools 48.4(−13.5) 19.1 3.9
ToolCUA-8B(Ours) GUI 42.9 19.4 -
+ Tools 46.8(+3.9) 14.9 0.74
Figure 2: Current computer use agents suffer
from optimal path confusion under GUI-Tool
hybrid actions.
2

## Page 3

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
address this by generating tools from code, but such pipelines remain costly to scale and do not fully exploit
the large amount of existing GUI-only trajectory corpora [13, 18, 23, 40, 45, 60]. Second, even when basic
tool-use ability is available, existing supervision provideslimited guidance for learning effective hybrid
action orchestration. In practice, current training signals usually come from either step-level imitation or
final task-completion rewards. The former one only captures local action plausibility, while the latter does
not distinguish between a timely tool calling switch and a long, brittle GUI-only workaround. As a result,
the model cannot reliably learn whether switching between GUI actions and tool calls improves the full
trajectory.
To address these challenges, we introduceToolCUA, a unified agentic model trained through a two-stage
paradigm: The first stage builds hybrid-action foundations with scalable interleaved GUI-Tool data, and
the second stage improves trajectory-level GUI-Tool decisions through reinforcement learning. First, we
propose aninterleaved GUI-Tool trajectory scaling pipelinebuilt on existing static GUI corpora. It
employs MLLMs to synthesize a trajectory-aware library of tools from recurrent GUI procedures, and
converts GUI-only data into interleaved GUI-Tool trajectories through tool steps generation and next-state
grounding. By repurposing existing GUI corpora and synthesizing tools instead of collecting expensive real
tool trajectories, this pipeline enables scalable data construction without manual engineering, while covering
varied tool granularities and switching contexts. Building on this data, we perform Tool-Bootstrapped GUI
Reinforcement Finetuning (RFT). It first applies warmup SFT to establish basic hybrid-action capabilities,
and then uses single-turn RL to improve decisions at explicit GUI-Tool switching points. Finally, we optimize
ToolCUA withOnline Agentic RLin a realistic GUI-Tool environment with aTool-Efficient Path Reward,
which includes a tool appropriateness termRtool and path efficiency termRlength : Rtool incentivizes the
agent to invoke tools when beneficial and abstain when unnecessary, whileRlength encourages shorter
execution paths by replacing redundant GUI actions with tool calls. Together, they provide trajectory-level
feedback that drives the model toward globally optimal GUI-Tool path selection.
Experimental results demonstrate that ToolCUA achieves an SOTA result of 46.85% on the OSWorld-
MCP benchmark [12], among the similar-size models, which represents an approximately 66% relative
improvement over the Qwen3-VL-8B-Instruct baseline [3] and rivals leading proprietary models [2, 10].
Furthermore, ToolCUA trained with hybrid action spaces achieved 42.9% accuracy even in pure GUI action
settings, and ToolCUA demonstrates a +3.9% improvement compared with pure GUI actions, demonstrating
successful orchestration of GUI and Tool actions in optimal path selection. Additionally, ToolCUA shows
out-of-distribution generalization across tasks and platforms, reaching 23.9% on unseenmulti_appsLinux
tasks and achieving 33.8% on unseenWindowsdesktop apps in WindowsAgentArena [5]. These results
confirm that operating in a hybrid GUI-Tool action space is essential for achieving generalizable and efficient
real-world digital automation. Our main contributions are summarized as follows:
• We propose anInterleaved GUI-Tool trajectory scaling pipelinethat repurposes existing pure GUI
corpora into scalable hybrid-action training data through tool synthesis, obviating the need for manual
tool-environment construction and tool trajectory collection.
• WeproposeastagedtrainingparadigmfororchestratingGUI-Toolactions,consistingoftool-bootstrapped
RFT hybrid action foundations and GUI-Tool switching decision optimization, andonline agentic RL
with atool-efficient path reward(Rtool and Rlength ) for trajectory-level optimization with appropriate
tool usage and shorter execution steps.
• OurToolCUAreaches 46.85% accuracy on OSWorld-MCP, SOTA performance among similar-size
models, outperforming the pure GUI training. Our findings suggest that training in hybrid GUI-Tool
actions enables more generalizable and efficient computer-use automation.
3

## Page 4

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
2. ToolCUA
(a) Scaling Interleaved GUI-Tool Trajectories via Tool Synthesis2. Trajectory-aware Tool Library Construction.
(b) Tool-Bootstrapped GUI RFT (c) Online Agentic RL in GUI-MCP Environment
GUI stepTool stepOriginal GUI Trajectories
… 𝐴!"#$ 𝐴!"#% 𝐴!"#& 𝐴!"#' 1. Filtering & Balancing
•Execution quality•Trajectory length•Coveredapp domains
Task goal
Actions
Screenshots
Analyze trajectory contextschrome_restore_closed_tabgeneral_open_system_settingsword_center_titlegimp_apply_color_enhance….
Synthesis Tool Set
Tool Iterative validation
3. Tool Trajectory Generation with Next-State Grounding.4. Interleaved GUI-Tool Trajectory Generation
… 
1. Warmup SFT
2. Single-Turn RL on Critical Steps with GRPO𝒟"#$%$"&'
𝒟&''
ℳ_𝑏𝑎𝑠𝑒 ℳ_𝑠𝑓𝑡
ℳ_𝑟𝑓𝑡
ℳ_𝑠𝑓𝑡
 ℳ_𝑟𝑓𝑡
Update
Tool Trajectory Generation
… 𝐴())*$ 𝑆𝑡𝑎𝑡𝑒! 𝐴())*% 𝐴())*+𝑆𝑡𝑎𝑡𝑒"… 
Generate tool stepSelect matched stateBottom-up Merging
… Merge adjacent tool steps
… 
𝐺𝑈𝐼%&'(')
𝐺𝑈𝐼%&'(')𝑇𝑜𝑜𝑙(*)
… … … 
𝒟&''
Tool-Beneficial Task
Non-Tool-Beneficial Task
Accuracy  reward by environmentTool-Appropriate ……
……
Traj-Length 
… …… 𝑅=1.5𝑅=0.8
𝑅=1.2
𝑇𝑜𝑜𝑙(*)
𝐴!"#$ 𝐴!"#% 𝐴!"#'𝐴!"## 𝐴!"#,
𝐴())*$ 𝐴())*- 𝐴())*+
𝐴())*$ 𝐴!"#,
𝑹𝒕𝒐𝒐𝒍 𝑹𝒍𝒆𝒏𝒈𝒕𝒉𝑹𝒂𝒄𝒄
GUI-Tool Hybrid Environment
GUI-Tool Hybrid Environment
Interreact
subset
Figure 3: Overview of the ToolCUA data collection and training paradigm. (a) Interleaved GUI-Tool trajectory scaling via
offline GUI data and tool synthesis, yielding the datasetDall containing critical switching stepsDcritical . (b)
Tool-Bootstrapped GUI RFT with warmup SFT onDall and step-level RL onDcritical . (c) Online Agentic RL with
Tool-Efficient Path Reward (Rtool and Rlength ) for trajectory-level optimization with appropriate tool-calling and efficient
path selection.
2.1. Definition and Scope
We first formalize the computer-use task as a Markov Decision Process (MDP) whereM=⟨S,A,P,R,γ⟩ .
At each time stept, the statest ∈ Sdenotes a multimodal observation encompassing both the desktop
screenshot and previously invoked tool results. The agent interacts with the environment through a hybrid
action spaceA=A GUI ∪ ATool, whereat ∈ AGUI represents atomic GUI interactions such as coordinate-
based clicks, andat ∈ ATool signifies high-level structured tool invocations. The objective is to learn an
optimal policyπθ(at|st)that maximizes the expected cumulative reward over a long-horizon trajectoryτ:
J(θ) =Eπθ
[︃ T∑︁
t=0
R(st,a t)
]︃
(1)
2.2. Interleaved GUI-Tool Trajectory Scaling Pipeline
To address the scarcity of interleaved GUI-Tool trajectories, we build an offline trajectory scaling pipeline
that starts fromexisting pure GUI trajectoriesand converts them into interleaved GUI-Tool data. As
shown in Figure 3(a), the key idea is to use an MLLM (e.g., Kimi-K2.5 or Claude-4.5-Sonnet) to synthesize
4

## Page 5

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
Step 1
…
# Call the set_fill_hatchingtoollibreoffice_set_fill_hatching (pattern=shadow_lines)# Call the set_fill_colortoollibreoffice_set_fill_color(color=blue) # Call the set_fill_colortoollibreoffice_set_fill_color(color=blue)# Click the purple pieGUI left click at [952, 603]Step 2 Step 3 Step n
libreoffice_set_fill_color 
✅libreoffice_set_fill_gradient libreoffice_set_fill_hatching 
✅…….general_open_app 
✅general_terminal_execute
Goal:Set the red sections of the pie chart to gold, the purple sections to blue and the orange to shadow lines.
Step 1
…
# Call the set_fill_hatchingtoollibreoffice_set_fill_hatching (pattern=shadow_lines)# Call the set_fill_colortoollibreoffice_set_fill_color(color=gold) # Call the set_fill_colortoollibreoffice_set_fill_color(color=blue)# Click the purple pieGUI left click at [952, 603]Step 2 Step 3 Step n
libreoffice_set_fill_color 
✅libreoffice_set_fill_gradient libreoffice_set_fill_hatching 
✅…….general_open_app 
✅general_terminal_execute
Goal:Set the red sections of the pie chart to gold, the purple sections to blue and the orange to shadow lines.
Figure 4: A synthetic GUI-Tool interleaved trajectory generated by our pipeline, which demonstrates strategic tool
selection and seamless switching between atomic GUI actions and tool calls.
agrounded library of toolsfrom recurrent GUI procedures, and then use these tools to transform GUI-
only trajectories into interleaved GUI-Tool trajectories. Our pipeline scales data along three dimensions:
Tool Functionality across application domains, Tool Granularity from atomic utilities to composite skills,
and GUI-Tool Switching Context covering cases where tool use is more or less beneficial. Please refer to
Appendix E for prompts we used. We describe the main steps below.
Trajectory Filtering and Balancing.We start from successful raw GUI trajectories and filter them by
execution quality, task length, and application coverage. The remaining trajectories are balanced across
domains to provide a stable source distribution for tool synthesis.
Trajectory-Aware Synthetic Tool Library Construction.For each GUI trajectory, we utilize an MLLM
to synthesize a candidate library of tools by analyzing the pure GUI path, including the task goal, action
sequences, and dense screenshot descriptions. Each synthesized tool abstracts an observed GUI procedure
into a callable high-level operation, specified by a functional signature, natural language description, and
argument semantics inferred from the trajectory. This makes the tools grounded in concrete trajectory
behavior rather than generic API templates or manually predefined functions. To increasediversity, we
synthesize tools at varying levels of specificity, from single-action wrappers (e.g., chrome_open_settings) to
multi-step composite functions (e.g., chrome_open_language_settings). A rule-based format verification is
also applied for tool filtering.
Tool Trajectory Generation with Next-State Grounding.Given the synthesized tool library and the
original GUI trajectory, we adopt an MLLM to generate a functionally equivalent tool-only trajectory. For
each step, the MLLM selects an appropriate tool from the library, produces a chain-of-thought rationale,
and predicts the expected response, validated against the tool schema. Furthermore, we adopt an MLLM to
performnext-state grounding,i.e., anchor the tool step to a corresponding resulting next-state screenshot
from the original trajectory, verifying consistency between predicted execution effects and observed GUI
state. Besides, we apply abottom-up merging strategy: adjacent fine-grained steps sharing a common
sub-goal are progressively merged into higher-level composite tool calls, yielding multiple variants at
different levels of tool granularity.
Interleaved GUI-Tool Trajectory Generation.Given a grounded tool-only trajectory, we randomly sample
a subset of tool calls and replace each with its corresponding GUI action sequence from the original
trajectory. Notably, the replaced tools are simultaneously removed from the tool library, constructing a
partial tool-availability context where the agent must fall back to GUI operations when certain tools are
unavailable. By varying the selection of replaced tool calls, we generate diverse interleaved variants from
the same trajectory, which are aggregated intoDall . A representative interleaved GUI-Tool trajectory is
illustrated in Figure 4. Furthermore, each replacement naturally exposes two types of boundary transitions:
GUI → Tool and Tool→ GUI (i.e., the yellow star in Figure 3(a)), where the agent switches between GUI
and tool calls. We refer to these ascritical switching stepsand collect them intoDcritical .
5

## Page 6

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
2.3. Tool-Bootstrapped GUI RFT
With Dall and Dcritical , we perform Tool-Bootstrapped GUI RFT to train the baseline agentMbase toward
flexible hybrid-action behavior and calibrate local GUI-Tool decisions.
Warmup Supervised Fine-Tuning (SFT).We first perform SFT onDall using a standard cross-entropy loss
LSFT =− ∑︀logπ θ(at|st). This phase teaches the model the diverse knowledge of multimodal tool-calling
in the CUA domain, like the tool usage, tool parameters, and the resulting state after tool executions. After
this SFT warmup training, we get the modelMs f t
Single-Turn RL on Critical Steps.Building upon the modelMs f t, we implement a single-turn RL phase
using the Group Relative Policy Optimization (GRPO) algorithm [30] onDcritical . By sampling multiple
completions at these critical switching steps, the model receives direct feedback on whether to continue
with GUI actions or switch to tool calls when appropriate tools are available. This targeted optimization
calibrates the model’s discernment at decision boundaries, yielding a coordinated agentMr f tready for
long-horizon online exploration in the GUI-Tool environment.
2.4. Online Agentic RL with Tool-Efficient Path Reward in GUI-Tool Environment
Online RL extends step-level tool-calling knowledge to complete trajectories, enabling the agent to discover
which GUI-Tool switching strategies lead to successful outcomes through real environment exploration.
However, task success alone cannot distinguish whether tool usage was genuinely appropriate, nor whether
the execution path was unnecessarily long. Therefore, we introduce aTool-Efficient Path Rewardthat
explicitly shapes the agent toward tool-appropriate and efficient trajectories, which consists of a tool
appropriateness termRtool and path efficiency termRlength :
R=R f mt+R acc +λ·R tool +β·R length (2)
where Rf mt, Racc are standard format and accuracy rewards, andRtool , Rlength are activated only when the
trajectory succeeds.
Tool Appropriateness Reward Term.In practice, agents may complete a task without tools even when
tools would help, or invoke tools unnecessarily on tasks that do not require them.Rtool addresses this by
introducing a task-level tool-beneficial labeltb ∈ {1,−1}annotated during data construction, wheretb =1
indicates that the task favors tool usage andtb =−1 indicates that tool usage is unnecessary. Letc denote
the cumulative number of tool calls in a trajectory.
Rtool =I succ ·I[(t b >0∧c>0)∨(t b <0∧c=0)] (3)
Rtool is assigned when agents invoke tools on tool-beneficial tasks (tb =1,c>0 ), or when it deliberately
abstains from tools on non-tool-beneficial tasks (tb =−1,c=0 ). This design decouples tool usage from
task success, pushing the agent to use tools when and only when they are truly needed.
Path Efficiency Reward Term.Even when the agent succeeds and uses tools appropriately, it may still take
unnecessarily long paths. For example, relying on redundant GUI operations when a single tool call could
accomplish the same effect. To this end,Rlength encourages the agent to actively explore and discover more
efficient GUI-Tool execution paths through online interaction. Rather than measuring efficiency against a
fixed threshold, we evaluate trajectory length relative to the rollout group, wheres is the current trajectory’s
step count„¯sis the group average step length, andSmax is the maximum execution horizon.
Rlength =I succ ·
{︃
(1+ ¯s−s
¯s )s< ¯s
exp(− s−¯s
Smax −¯s )s≥ ¯s (4)
6

## Page 7

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
For trajectories shorter than the group average, the agent receives a linear bonus proportional to the relative
step reduction; otherwise, the reward decays exponentially as the trajectory grows longer. Since useful tool
calls often replace multiple atomic GUI operations, this signal naturally incentivizes the agent to switch to
tools when they lead to a shorter and more reliable execution path.
With the above reward, we optimize ToolCUA using multi-turn GRPO over online rollouts in a GUI-Tool
environment. Inspired by DAPO [58], we apply dynamic filtering and retain only rollout groups containing
both successful and failed trajectories, which improves the informativeness of group-relative policy updates
while reducing unnecessary computation.
3. Experiments
3.1. Experimental Settings
Implementation Details.Our pipeline aggregates diverse trajectories from open-sourced datasets [18, 40],
as detailed in Appendix C.2. We adopt Qwen3-VL-8B-Instruct [3] as our base modelM. In the warmup
SFT stage, we trainM for 3 epochs, and then we continually conduct single-turn RL with a group size of
32. During the subsequent online agentic RL stage, we set hyperparametersλ=0.4 , β=0.2 for reward
design andSmax =30 to define the maximum execution steps. The training configuration for this stage
includes a rollout size of 32 per group, a learning rate of1×10 −6, and a training batch size of 32 to get our
ToolCUA. We further optimize the tool-calling interface by designing an agent-readable return format that
provides concise, semantically dense feedback to reduce token overhead and improve grounding accuracy.
For the argentic training task, we directly utilize the tasks from OSWorld [45] except for themulti_apps
domain, which we will save for OOD verification. Please reference Appendix C.3 for more details.
Baselines and Benchmark.We evaluate ToolCUA against two categories: general-purpose foundation mod-
els (e.g., Qwen3.5-Plus [29], Claude-4.5-Sonnet [2], Gemini-3.1-Pro [10] and specialized CUAs including
UI-Tars-1.5 [28], the EvoCUA series [48], and GUI-Owl-1.5 [46].
For evaluation, we utilize OSWorld-MCP [12] as our primary benchmark, as it is designed for CUAs under a
hybrid action space, which covers typical GUI actions, 150+ tools, and mainstream desktop apps. Following
the benchmark setup, we report results on the feasible tasks only. To mitigate environmental stochasticity
in the sandbox, we report theaverage@3for all primary metrics, and set the maximum steps per task to
50. We follow the original benchmark metrics (detailed in Appendix C.4), where TIR measures whether
the agent uses tools when beneficial and avoids them when unnecessary, and ACS measures average
completion steps as an indicator of execution efficiency. Furthermore, we evaluate the cross-task and
cross-platform transferability of ToolCUA on unseen Linuxmulti_appstasks and unseen Windows apps in
WindowsAgentArena [5].
3.2. Main Results
Outstanding performance on GUI-Tool Execution Path Selection.Table 2 summarizes the evaluation
results on the OSWorld-MCP benchmark, where ToolCUA-8B achieves a SOTA performance of 46.85%
among 8B-class models. Our model surpasses the previous state-of-the-art GUI-Owl-1.5-8B (43.84%)
and outperforms prominent general foundation models, including Gemini-3.1-Pro (41.14%) and Claude-
4-Sonnet (43.54%), while trailing the top-tier claude-4.5-sonnet by less than 2%. This approximately
66% relative improvement over the baseline (28.23%) underscores the efficacy of our synthesis-driven
scaling pipeline and staged training paradigm. Beyond task accuracy, ToolCUA also substantially improves
GUI-Tool orchestration and execution efficiency. As shown in Table 1, ToolCUA-8B demonstrates a +3.9%
7

## Page 8

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
Table 2: Performance on OSWorld-MCP. Results are reported on the feasible tasks only. Tool-Beneficial Tasks favor tool
usage, while Non-Tool-Beneficial Tasks do not require tools. Accuracy denotes average success rate; TIR (Tool Invocation
Rate) measures whether the agent uses tools when beneficial and avoids them when unnecessary; ACS denotes Average
Completion Steps.
Agent Model Tool-Beneficial Tasks (238) Non-Tool-Beneficial Tasks (95) Overall (333)
Accuracy TIR ACS Accuracy TIR ACS Accuracy↑TIR↑ACS↓
General Model
Gemini-2.5-Pro 24.79 21.15 26.12 8.77 7.37 39.60 20.22 17.22 29.97
OpenAI o3 26.89 24.51 26.71 4.91 2.46 44.78 20.62 18.22 31.87
Seed1.5-VL 34.03 23.81 18.99 35.79 34.39 24.93 34.53 26.83 20.69
Claude-4-Sonnet 45.24 36.13 18.29 39.30 34.74 21.09 43.54 35.74 19.76
Gemini-3.1-Pro 44.54 37.39 22.46 32.63 26.32 32.82 41.14 34.23 25.40
Claude-4-5-Sonnet 50.00 42.02 17.93 44.21 35.79 21.91 48.35 40.24 19.07
Qwen3-VL-235B-A22B 37.11 28.15 17.04 40.70 29.82 20.25 38.14 28.63 17.95
Qwen3.5-397B-A17B 41.60 0.84 21.74 38.95 38.95 22.17 40.84 11.71 21.86
Specialized CUA Model
UI-Tars-1.5-7B 10.92 0 37.38 15.79 15.79 36.43 12.31 4.5 37.11
EvoCUA-8B 34.45 3.78 26.88 38.95 38.95 26.49 35.74 13.81 26.77
EvoCUA-32B 37.82 13.03 27.90 47.37 46.32 21.82 40.54 22.52 26.16
GUI-Owl-1.5-8B 44.54 37.82 20.70 42.11 31.58 22.41 43.84 36.04 21.19
GUI-Owl-1.5-32B 47.48 38.66 24.09 49.47 47.37 24.45 48.05 41.14 24.19
Ours (based on Qwen3-VL-8B-Instruct)
Qwen3-VL-8B-Instruct 27.73 0.00 20.37 29.47 29.47 16.77 28.23 8.41 19.34
ToolCUA-8B 45.80 15.13 15.11 49.47 47.37 14.48 46.85 24.32 14.93
∆ +18.07 +15.13 -5.26 +20.00 +17.90 -2.29 +18.62 +15.91 -4.41
improvement compared with pure GUI settings. Also, compared with the Qwen3-VL-8B-Instruct baseline,
ToolCUA increases the overall TIR from 8.41% to 24.32%, while reducing ACS from 19.34 to 14.93. Notably,
ToolCUA achieves the lowest average completion steps (14.93 steps) among all evaluated models, indicating
that it not only completes more tasks but also intelligently finds more efficient GUI-Tool execution paths
with our Tool-Efficient Path Reward.
Cross-task and Cross-platform Generalization.ToolCUA also demonstrates strong generalization beyond
the training distribution. Although online agentic RL is conducted only on single-application Linux tasks and
excludes themulti_appscategory, ToolCUA improves on the held-outmulti_appsdomain from the pre-online
RL stage (18.5%) and the baseline (9.8%) to 23.9%, as shown in Figure 5. It also achieves consistent
gains across specialized domains, increasing performance from 19.6% to 34.8% onlibreoffice_calculation
and from 66.7% to 94.4% onvs_code. Beyond cross-task transfer, ToolCUA further generalizes to unseen
Windows desktop environments. As shown in Table 4, despite being trained on Linux-based trajectories and
sandboxes, ToolCUA reaches 33.8% accuracy on WindowsAgentArena, outperforming the Qwen3-VL-8B-
Instruct baseline by 7.4 percentage points and surpassing larger Qwen3-VL variants such as Qwen3-VL-
235B-A22B (32.1%).
3.3. Ablation Analysis
The Importance of the Interleaved GUI-Tool Trajectory Data.As shown by the “w/o Interleaved data”
setting in Figure 6, we remove coldstart RFT training with our synthetic interleaved GUI-Tool data and
directly apply online agentic RL with the tool-efficient path reward to the Qwen3-VL-8B-Instruct baseline
model. Although the model still improves its overall task accuracy during agentic RL, it struggles to acquire
8

## Page 9

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
overall
multi_apps chrome
thunderbirdcalculation impress writer os gimp vlc
vs_code
0
20
40
60
80
95Accuracy
41.1
8.7
34.1
50.0
78.3
34.0
68.2
36.8
62.5
60.0
77.8
28.2
9.8
36.4
57.1
19.6 21.3
36.4
47.4
37.5
46.7
66.7
38.1
18.5
48.7
64.3
23.9
34.0
50.0
47.4
75.0
46.7
72.2
46.8
23.9
50.7
85.7
34.8
44.7
59.1
68.4
81.2
53.3
94.4
Gemini-3.1-Pro
Qwen3-VL-8B-Instruct (baseline)
baseline + RFT
T oolCUA-8B (Ours)
Figure 5: Results across tasks on OSWorld-MCP for different models, Gemini-3.1-Pro, Qwen3-VL-8B-Instruct (baseline),
baseline trained only with coldstart RFT (Mr f t), and finally our ToolCUA-8B.
Test accuracyTIR (success and correct tool call)MCP tool callsTrajectory completion steps(%) (#num)(%) (#num)
Figure 6: Online Agentic RL training dynamics of ToolCUA and two ablations.w/o Interleaved dataremoves the offline
interleaved GUI-Tool data bootstrapping and directly performs online agentic RL from the baseline model.w/o Our path
rewardreplaces the tool-efficient path reward with vanilla GRPO during online agentic RL.
reliable tool-calling behavior without the offline interleaved supervision produced by our trajectory scaling
pipeline. Specifically, its TIR remains consistently low and only reaches around 15% by the end of training,
while the number of tool calls stays close to zero throughout most of the learning process. This suggests that
online RL with tool-efficiency rewards alone is insufficient to overcome the GUI-centric bias of base models.
Instead, our data scaling pipeline synthesizes simulated tools into static GUI data to provide grounded,
interleaved supervision. This instills diverse tool knowledge and switching priors, establishing a superior
foundation for subsequent online exploration.
Advantages of Tool-Efficient Path Reward.As illustrated by the “w/o Our path reward” setting in Figure 6,
we further train the RFT-initialized model with vanilla multi-turn GRPO, using only the standardRacc and
Rf mtrewards. Without the tool-appropriate and trajectory-length reward, the accuracy curve becomes less
stable than ToolCUA, showing a clear drop around steps 8–11 and an eventual gap of about 7 percentage
points after 20 training steps. Moreover, both TIR and tool-calls fluctuate without a consistent upward trend,
suggesting that the model does not learn when tool invocation is genuinely beneficial. The trajectory length
also lacks a stable downward trend and rebounds after temporary decreases, indicating that vanilla agentic
RL does not reliably discover more efficient execution paths. These results validate that the Tool-Efficient
Path Reward is essential for turning online exploration into tool-appropriate and efficiency-aware GUI-Tool
path selection.
Hybrid GUI-Tool Training is More Effective than pure GUI.We compare hybrid GUI-Tool training with
a pure GUI training pipeline in Table 3. For the pure GUI setting, we first cold-start the baseline using a
9

## Page 10

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
Table 3: Comparison of pure GUI training and training with
hybrid GUI-Tool action spaces.
Action Agent Model Acc (%)
GUI
Qwen3-VL-8B-Instruct 29.03
+ SFT 34.93
+ SFT + Agentic RL 42.05
GUI+Tool + RFT 38.13
ToolCUA-8B 46.85
Table 4: ToolCUA’s generalization on Windows desktop,
evaluated by WindowsAgentArena [5]
Agent Model Accuracy (%)
Qwen3-VL-8B-Instruct 26.4
Qwen3-VL-32B-Instruct 30.9
Qwen3-VL-235B-A22B 32.1
ToolCUA-8B33.8
GUI-only dataset of comparable scale to ToolCUA’s warmup data, and then conduct agentic RL entirely
within the pure GUI action space. Although GUI-only training improves the baseline from 29.03% to 34.93%
after SFT and further to 42.05% after agentic RL, both stages remain below their GUI-Tool counterparts. In
comparison, RFT training with our synthetic interleaved GUI-Tool trajectories already reaches 38.13%, and
the full ToolCUA further improves to 46.85% after online agentic RL. These results indicate that the hybrid
GUI-Tool action space provides a more effective training environment than pure GUI actions, enabling the
agent to learn not only visual grounding but also when structured tool calls can replace redundant low-level
operations.
3.4. Case Study
As illustrated in Table 7, the agent is tasked with “creating two pivot tables in a new sheet named Sheet2 to
summarize revenue by product and sales channel”. While standard GUI-only approaches involve a laborious
and error-prone sequence of data range selection and menu navigation, ToolCUA leverages high-level tools
for superior efficiency. Specifically, it first retrieves sheet information like column value and data fields via
libreoffice_calc.env_info(Sheet1)and then identifies the corresponding data range needed for each pivot
table. After that, the agent invokeslibreoffice_calc.create_pivot_table(source_sheet, table_name, ...)with the
corresponding parameters to generate the tables directly, bypassing brittle step-by-step GUI interactions.
Furthermore, ToolCUA demonstrates the ability to navigate optimal execution paths within hybrid GUI-Tool
actionspaces. AsshowninTable8,theagentsuccessivelyinvokestheefficientosworld_mcp_vscode.add_folder
tool twice to add the required directories to the workspace. It then correctly identifies the necessity of a
GUI action, clicking the “I trust the authors” dialog to grant folder permissions and successfully finalize the
end-to-end workflow. See the complete case study in Appendix D.
4. Related Work
Multimodal Agents for Computer Use.Building generalist multimodal agents in digital environments has
long been a foundational yet challenging pursuit [2, 3, 24, 28, 40, 43, 45, 56]. Current CUAs generally
follow two paradigms: multi-agent systems [1, 9, 16, 32, 51, 53], which decompose tasks across specialized
modules, and end-to-end agentic models [18, 28, 40, 46, 48], which integrate planning and grounding
within a unified policy. Most of these agents, however, still rely primarily on primitive GUI actions such as
clicking, typing, and scrolling, making long-horizon tasks vulnerable to cascading errors and inefficient
execution. Reinforcement learning has therefore been introduced to improve GUI agents, from mobile
navigation settings [21, 22] to broader agentic GUI environments [14, 20, 42, 47, 52]. These studies
demonstrate the promise of environment-driven optimization, but their action spaces are largely restricted
to GUI operations and often provide limited supervision for trajectory-level orchestration. Consequently,
10

## Page 11

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
they do not directly address the hybrid action spaces that combine raw GUI interaction with structured
tool invocation in realistic computer-use environments [25, 55]. ToolCUA builds on this direction by using
a staged training paradigm to move beyond GUI-only control and optimize complete GUI-Tool execution
paths.
Hybrid GUI-Tool Actions for CUAs.A broad line of research equips LLMs with tools [26, 27], enabling
progress in autonomous coding [7, 8, 38], deep research [35, 57], and multimodal visual search [11, 19,
33, 36, 63]. In CUA scenarios, structured tools can reduce repetitive low-level GUI operations and improve
efficiency when reliable interfaces are available. Recent studies [12, 50] have begun to explore this, which
introduce various MCP tools for hybrid-action evaluation, while several GUI-tool systems [9, 32, 37, 49, 51,
54] connect GUI agents with APIs, SDKs, external executors, or multi-agent tool routers. Nevertheless, these
efforts still fail to solve two critical challenges. First, high-quality interleaved GUI-Tool trajectories remain
scarce because existing pipelines often rely on costly tool construction, environment, or closed-source
data collection. Second, existing methods provide limited guidance for trajectory-level selection. ToolCUA
addresses these limitations by synthesizing interleaved GUI-Tool trajectories and a two-staged training
paradigm.
5. Conclusion
In this work, we presentedToolCUA, an end-to-end computer use agent for orchestrating GUI and Tool
actions, learning an optimal GUI-Tool path selection. We show that simply exposing agents to both GUI
actions and tool calls is insufficient, as current models often overuse tools or remain overly GUI-centric,
leading to inefficient and brittle execution trajectories. To address this challenge, ToolCUA first scales
interleaved GUI-Tool trajectories from existing GUI data without manually constructing tools, then applies
Tool-Bootstrapped GUI RFT to acquire tool-calling knowledge and calibrate critical switching decisions.
Finally, Online Agentic RL with a Tool-Efficient Path Reward optimizes ToolCUA in a GUI-Tool environment,
encouraging appropriate tool use and shorter execution paths. Experiments on OSWorld-MCP show that
ToolCUA achieves 46.85% accuracy, a relative improvement of approximately 66% over the baseline, and
consistently improves over pure GUI action settings. Together with the transfer results and ablation study,
these findings suggest that training with a hybrid GUI-Tool action space provides a high-fidelity training
paradigm for robust real-world digital agents.
6. Acknowledgement
We thank Zhaoqing Zhu, Junyang Wang, Jitong Liao and Haowei Liu for their support of training infrastruc-
ture, sandbox construction and evaluation.
11

## Page 12

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
References
[1] Saaket Agashe, Kyle Wong, Vincent Tu, Jiachen Yang, Ang Li, and Xin Eric Wang. Agent s2: A compo-
sitional generalist-specialist framework for computer use agents.arXiv preprint arXiv:2504.00906,
2025.
[2] Anthropic. Claude opus 4.5, 2026. URL https://www.anthropic.com/news/
claude-opus-4-5. Accessed: 2026-04-20.
[3] Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui Chen, Zesen Cheng, Lianghao Deng,
Wei Ding, Chang Gao, Chunjiang Ge, et al. Qwen3-vl technical report, 2025.URL https://arxiv.
org/abs/2511.21631, 2025.
[4] Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai Dang, Peng Wang, Shijie
Wang, Jun Tang, et al. Qwen2. 5-vl technical report.arXiv preprint arXiv:2502.13923, 2025.
[5] Rogerio Bonatti, Dan Zhao, Francesco Bonacci, Dillon Dupont, Sara Abdali, Yinheng Li, Yadong Lu,
Justin Wagle, Kazuhito Koishida, Arthur Bucker, et al. Windows agent arena: Evaluating multi-modal
os agents at scale.arXiv preprint arXiv:2409.08264, 2024.
[6] Zhe Chen, Jiannan Wu, Wenhai Wang, Weijie Su, Guo Chen, Sen Xing, Muyan Zhong, Qinglong
Zhang, Xizhou Zhu, Lewei Lu, et al. Internvl: Scaling up vision foundation models and aligning for
generic visual-linguistic tasks. InProceedings of the IEEE/CVF conference on computer vision and pattern
recognition, pages 24185–24198, 2024.
[7] Guanting Dong, Yifei Chen, Xiaoxi Li, Jiajie Jin, Hongjin Qian, Yutao Zhu, Hangyu Mao, Guorui
Zhou, Zhicheng Dou, and Ji-Rong Wen. Tool-star: Empowering llm-brained multi-tool reasoner via
reinforcement learning.arXiv preprint arXiv:2505.16410, 2025.
[8] Jiazhan Feng, Shijue Huang, Xingwei Qu, Ge Zhang, Yujia Qin, Baoquan Zhong, Chengquan Jiang,
Jinxin Chi, and Wanjun Zhong. Retool: Reinforcement learning for strategic tool use in llms.arXiv
preprint arXiv:2504.11536, 2025.
[9] Gonzalo Gonzalez-Pumariega, Vincent Tu, Chih-Lun Lee, Jiachen Yang, Ang Li, and Xin Eric Wang.
The unreasonable effectiveness of scaling agents for computer use.arXiv preprint arXiv:2510.02250,
2025.
[10] Google DeepMind. Gemini: The most capable and general model we’ve built, 2026. URLhttps:
//deepmind.google/models/gemini/pro/. Accessed: 2026-04-28.
[11] Jack Hong, Chenxiao Zhao, ChengLin Zhu, Weiheng Lu, Guohai Xu, and Xing Yu. Deepeyesv2: Toward
agentic multimodal model.arXiv preprint arXiv:2511.05271, 2025.
[12] Hongrui Jia, Jitong Liao, Xi Zhang, Haiyang Xu, Tianbao Xie, Chaoya Jiang, Ming Yan, Si Liu, Wei
Ye, and Fei Huang. Osworld-mcp: Benchmarking mcp tool invocation in computer-use agents.arXiv
preprint arXiv:2510.24563, 2025.
[13] Xiangru Jian, Shravan Nayak, Kevin Qinghong Lin, Aarash Feizi, Kaixin Li, Patrice Bechard, Spandana
Gella, and Sai Rajeswar. Cua-suite: Massive human-annotated video demonstrations for computer-use
agents.arXiv preprint arXiv:2603.24440, 2026.
[14] Pengxiang Li, Zechen Hu, Zirui Shang, Jingrong Wu, Yang Liu, Hui Liu, Zhi Gao, Chenrui Shi, Bofei
Zhang, Zihao Zhang, et al. Efficient multi-turn rl for gui agents via decoupled training and adaptive
data curation.arXiv preprint arXiv:2509.23866, 2025.
12

## Page 13

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
[15] Shilong Li, Xingyuan Bu, Wenjie Wang, Jiaheng Liu, Jun Dong, Haoyang He, Hao Lu, Haozhe Zhang,
ChenchenJing, ZhenLi, etal. Mm-browsecomp: Acomprehensivebenchmarkformultimodalbrowsing
agents.arXiv preprint arXiv:2508.13186, 2025.
[16] Haowei Liu, Xi Zhang, Haiyang Xu, Yuyang Wanyan, Junyang Wang, Ming Yan, Ji Zhang, Chunfeng
Yuan,ChangshengXu,WeimingHu,etal. Pc-agent: Ahierarchicalmulti-agentcollaborationframework
for complex task automation on pc.arXiv preprint arXiv:2502.14282, 2025.
[17] Xiao Liu, Bo Qin, Dongzhu Liang, Guang Dong, Hanyu Lai, Hanchen Zhang, Hanlin Zhao, Iat Long
Iong, Jiadai Sun, Jiaqi Wang, et al. Autoglm: Autonomous foundation agents for guis.arXiv preprint
arXiv:2411.00820, 2024.
[18] ZhaoyangLiu,JingJingXie,ZichenDing,ZehaoLi,BowenYang,ZhenyuWu,XuehuiWang,QiushiSun,
Shi Liu, Weiyun Wang, et al. Scalecua: Scaling open-source computer use agents with cross-platform
data.arXiv preprint arXiv:2509.15221, 2025.
[19] Ziyu Liu, Zeyi Sun, Yuhang Zang, Xiaoyi Dong, Yuhang Cao, Haodong Duan, Dahua Lin, and Jiaqi
Wang. Visual-rft: Visual reinforcement fine-tuning.arXiv preprint arXiv:2503.01785, 2025.
[20] Fanbin Lu, Zhisheng Zhong, Shu Liu, Chi-Wing Fu, and Jiaya Jia. Arpo: End-to-end policy optimization
for gui agents with experience replay.arXiv preprint arXiv:2505.16282, 2025.
[21] Zhengxi Lu, Yuxiang Chai, Yaxuan Guo, Xi Yin, Liang Liu, Hao Wang, Guanjing Xiong, and Hongsheng
Li. Ui-r1: Enhancing action prediction of gui agents by reinforcement learning.arXiv preprint
arXiv:2503.21620, 1(2):3, 2025.
[22] Run Luo, Lu Wang, Wanwei He, Longze Chen, Jiaming Li, and Xiaobo Xia. Gui-r1: A generalist r1-style
vision-language action model for gui agents.arXiv preprint arXiv:2504.10458, 2025.
[23] Jian Mu, Chaoyun Zhang, Chiming Ni, Lu Wang, Bo Qiao, Kartik Mathur, Qianhui Wu, Yuhang Xie,
Xiaojun Ma, Mengyu Zhou, et al. Gui-360: A comprehensive dataset and benchmark for computer-
using agents.To appear, 2025.
[24] OpenAI. Introducing operator, 2026. URL https://openai.com/index/
introducing-operator/. Accessed: 2026-04-20.
[25] OpenClaw. Openclaw, 2026. URLhttps://github.com/openclaw/openclaw. Accessed: 2026-
04-20.
[26] Shishir G Patil, Tianjun Zhang, Xin Wang, and Joseph E Gonzalez. Gorilla: Large language model
connected with massive apis, 2023.URL https://arxiv. org/abs/2305.15334, 2023.
[27] Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru
Tang, Bill Qian, et al. Toolllm: Facilitating large language models to master 16000+ real-world apis.
arXiv preprint arXiv:2307.16789, 2023.
[28] Yujia Qin, Yining Ye, Junjie Fang, Haoming Wang, Shihao Liang, Shizuo Tian, Junda Zhang, Jiahao
Li, Yunxin Li, Shijue Huang, et al. Ui-tars: Pioneering automated gui interaction with native agents.
arXiv preprint arXiv:2501.12326, 2025.
[29] Qwen Team. Qwen3.5: Towards native multimodal agents, February 2026. URLhttps://qwen.
ai/blog?id=qwen3.5.
13

## Page 14

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
[30] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan
Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open
language models.arXiv preprint arXiv:2402.03300, 2024.
[31] Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng,
Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework.arXiv preprint arXiv:
2409.19256, 2024.
[32] Linxin Song, Yutong Dai, Viraj Prabhu, Jieyu Zhang, Taiwei Shi, Li Li, Junnan Li, Silvio Savarese,
Zeyuan Chen, Jieyu Zhao, et al. Coact-1: Computer-using agents with coding as actions.arXiv preprint
arXiv:2508.03923, 2025.
[33] Zhaochen Su, Peng Xia, Hangyu Guo, Zhenhua Liu, Yan Ma, Xiaoye Qu, Jiaqi Liu, Yanshu Li, Kaide
Zeng, Zhengyuan Yang, et al. Thinking with images for multimodal reasoning: Foundations, methods,
and future frontiers.arXiv preprint arXiv:2506.23918, 2025.
[34] Kimi Team, Tongtong Bai, Yifan Bai, Yiping Bao, SH Cai, Yuan Cao, Y Charles, HS Che, Cheng Chen,
Guanduo Chen, et al. Kimi k2. 5: Visual agentic intelligence.arXiv preprint arXiv:2602.02276, 2026.
[35] Tongyi DeepResearch Team, Baixuan Li, Bo Zhang, Dingchu Zhang, Fei Huang, Guangyu Li, Guoxin
Chen, Huifeng Yin, Jialong Wu, Jingren Zhou, et al. Tongyi deepresearch technical report.arXiv
preprint arXiv:2510.24701, 2025.
[36] Chaoyang Wang, Kaituo Feng, Dongyang Chen, Zhongyu Wang, Zhixun Li, Sicheng Gao, Meng Meng,
Xu Zhou, Manyuan Zhang, Yuzhang Shang, et al. Adatooler-v: Adaptive tool-use for images and
videos.arXiv preprint arXiv:2512.16918, 2025.
[37] Haoming Wang, Haoyang Zou, Huatong Song, Jiazhan Feng, Junjie Fang, Junting Lu, Longxiang Liu,
Qinyu Luo, Shihao Liang, Shijue Huang, et al. Ui-tars-2 technical report: Advancing gui agent with
multi-turn reinforcement learning.arXiv preprint arXiv:2509.02544, 2025.
[38] Hongru Wang, Cheng Qian, Wanjun Zhong, Xiusi Chen, Jiahao Qiu, Shijue Huang, Bowen Jin, Mengdi
Wang, Kam-Fai Wong, and Heng Ji. Acting less is reasoning more! teaching model to act efficiently.
arXiv preprint arXiv:2504.14870, 2025.
[39] Junyang Wang, Haiyang Xu, Haitao Jia, Xi Zhang, Ming Yan, Weizhou Shen, Ji Zhang, Fei Huang,
and Jitao Sang. Mobile-agent-v2: Mobile device operation assistant with effective navigation via
multi-agent collaboration.arXiv preprint arXiv:2406.01014, 2024.
[40] Xinyuan Wang, Bowen Wang, Dunjie Lu, Junlin Yang, Tianbao Xie, Junli Wang, Jiaqi Deng, Xiaole
Guo, Yiheng Xu, Chen Henry Wu, et al. Opencua: Open foundations for computer-use agents.arXiv
preprint arXiv:2508.09123, 2025.
[41] Yinjie Wang, Xuyang Chen, Xiaolong Jin, Mengdi Wang, and Ling Yang. Openclaw-rl: Train any agent
simply by talking.arXiv preprint arXiv:2603.10165, 2026.
[42] Yinjie Wang, Tianbao Xie, Ke Shen, Mengdi Wang, and Ling Yang. Rlanything: Forge environment,
policy, and reward model in completely dynamic rl system.arXiv preprint arXiv:2602.02488, 2026.
[43] Zhenhailong Wang, Haiyang Xu, Junyang Wang, Xi Zhang, Ming Yan, Ji Zhang, Fei Huang, and Heng
Ji. Mobile-agent-e: Self-evolving mobile assistant for complex tasks.arXiv preprint arXiv:2501.11733,
2025.
14

## Page 15

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
[44] Qianshan Wei, Yishan Yang, Siyi Wang, Jinglin Chen, Binyu Wang, Jiaming Wang, Shuang Chen,
ZechenLi, YangShi, YuqiTang, etal. Agentic-mme: Whatagenticcapabilityreallybringstomultimodal
intelligence?arXiv preprint arXiv:2604.03016, 2026.
[45] Tianbao Xie, Danyang Zhang, Jixuan Chen, Xiaochuan Li, Siheng Zhao, Ruisheng Cao, Toh J Hua,
Zhoujun Cheng, Dongchan Shin, Fangyu Lei, et al. Osworld: Benchmarking multimodal agents for
open-ended tasks in real computer environments.Advances in Neural Information Processing Systems,
37:52040–52094, 2024.
[46] Haiyang Xu, Xi Zhang, Haowei Liu, Junyang Wang, Zhaozai Zhu, Shengjie Zhou, Xuhao Hu, Feiyu
Gao, Junjie Cao, Zihua Wang, et al. Mobile-agent-v3. 5: Multi-platform fundamental gui agents.arXiv
preprint arXiv:2602.16855, 2026.
[47] Yifan Xu, Xiao Liu, Xinghan Liu, Jiaqi Fu, Hanchen Zhang, Bohao Jing, Shudan Zhang, Yuting Wang,
Wenyi Zhao, and Yuxiao Dong. Mobilerl: Online agentic reinforcement learning for mobile gui agents.
arXiv preprint arXiv:2509.18119, 2025.
[48] Taofeng Xue, Chong Peng, Mianqiu Huang, Linsen Guo, Tiancheng Han, Haozhe Wang, Jianing Wang,
Xiaocheng Zhang, Xin Yang, Dengchang Zhao, et al. Evocua: Evolving computer use agents via
learning from scalable synthetic experience.arXiv preprint arXiv:2601.15876, 2026.
[49] Haolong Yan, Jia Wang, Xin Huang, Yeqing Shen, Ziyang Meng, Zhimin Fan, Kaijun Tan, Jin Gao,
Lieyu Shi, Mi Yang, et al. Step-gui technical report.arXiv preprint arXiv:2512.15431, 2025.
[50] Yunhe Yan, Shihe Wang, Jiajun Du, Yexuan Yang, Yuxuan Shan, Qichen Qiu, Xianqing Jia, Xinge
Wang, Xin Yuan, Xu Han, et al. Mcpworld: A unified benchmarking testbed for api, gui, and hybrid
computer use agents.arXiv preprint arXiv:2506.07672, 2025.
[51] Bowen Yang, Kaiming Jin, Zhenyu Wu, Zhaoyang Liu, Qiushi Sun, Zehao Li, JingJing Xie, Zhoumianze
Liu, Fangzhi Xu, Kanzhi Cheng, et al. Os-symphony: A holistic framework for robust and generalist
computer-using agent.arXiv preprint arXiv:2601.07779, 2026.
[52] Chenyu Yang, Shiqian Su, Shi Liu, Xuan Dong, Yue Yu, Weijie Su, Xuehui Wang, Zhaoyang Liu, Jinguo
Zhu, Hao Li, et al. Zerogui: Automating online gui learning at zero human cost.arXiv preprint
arXiv:2505.23762, 2025.
[53] Yan Yang, Dongxu Li, Yutong Dai, Yuhao Yang, Ziyang Luo, Zirui Zhao, Zhiyuan Hu, Junzhe Huang,
Amrita Saha, Zeyuan Chen, et al. Gta1: Gui test-time scaling agent.arXiv preprint arXiv:2507.05791,
2025.
[54] Yuhao Yang, Zhen Yang, Zi-Yi Dou, Anh Nguyen, Keen You, Omar Attia, Andrew Szot, Michael Feng,
Ram Ramrakhya, Alexander Toshev, et al. Ultracua: A foundation model for computer use agents
with hybrid action.arXiv preprint arXiv:2510.17790, 2025.
[55] Bowen Ye, Rang Li, Qibin Yang, Yuanxin Liu, Linli Yao, Hanglong Lv, Zhihui Xie, Chenxin An, Lei Li,
Lingpeng Kong, et al. Claw-eval: Toward trustworthy evaluation of autonomous agents.arXiv preprint
arXiv:2604.06132, 2026.
[56] Jiabo Ye, Xi Zhang, Haiyang Xu, Haowei Liu, Junyang Wang, Zhaoqing Zhu, Ziwei Zheng, Feiyu
Gao, Junjie Cao, Zhengxi Lu, et al. Mobile-agent-v3: Fundamental agents for gui automation.arXiv
preprint arXiv:2508.15144, 2025.
15

## Page 16

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
[57] Rui Ye, Zhongwang Zhang, Kuan Li, Huifeng Yin, Zhengwei Tao, Yida Zhao, Liangcai Su, Liwen
Zhang, Zile Qiao, Xinyu Wang, et al. Agentfold: Long-horizon web agents with proactive context
management.arXiv preprint arXiv:2510.24699, 2025.
[58] Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan,
Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system at scale.
arXiv preprint arXiv:2503.14476, 2025.
[59] Aohan Zeng, Xin Lv, Zhenyu Hou, Zhengxiao Du, Qinkai Zheng, Bin Chen, Da Yin, Chendi Ge,
Chenghua Huang, Chengxing Xie, et al. Glm-5: from vibe coding to agentic engineering.arXiv
preprint arXiv:2602.15763, 2026.
[60] Bofei Zhang, Zirui Shang, Zhi Gao, Wang Zhang, Rui Xie, Xiaojian Ma, Tao Yuan, Xinxiao Wu,
Song-Chun Zhu, and Qing Li. Tongui: Internet-scale trajectories from multimodal web tutorials for
generalized gui agents. InProceedings of the AAAI Conference on Artificial Intelligence, volume 40,
pages 12367–12375, 2026.
[61] Chaoyun Zhang, Shilin He, Liqun Li, Si Qin, Yu Kang, Qingwei Lin, Saravan Rajmohan, and Dongmei
Zhang. Api agents vs. gui agents: Divergence and convergence.arXiv preprint arXiv:2503.11069,
2025.
[62] Chaoyun Zhang, Liqun Li, He Huang, Chiming Ni, Bo Qiao, Si Qin, Yu Kang, Minghua Ma, Qingwei
Lin, Saravan Rajmohan, et al. Ufo3: Weaving the digital agent galaxy.arXiv preprint arXiv:2511.11332,
2025.
[63] Ziwei Zheng, Michael Yang, Jack Hong, Chenxiao Zhao, Guohai Xu, Le Yang, Chao Shen, and Xing
Yu. Deepeyes: Incentivizing" thinking with images" via reinforcement learning.arXiv preprint
arXiv:2505.14362, 2025.
16

## Page 17

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
Appendix
A. Limitations and Future Works
Although ToolCUA demonstrates the effectiveness of learning from synthesized interleaved GUI-Tool
trajectories, our synthesis-driven pipeline is still constrained by the state frames and domain coverage of the
original GUI-only trajectories. As a result, the diversity and quality of the synthesized hybrid trajectories
are coupled with the breadth, fidelity, and task distribution of the source demonstrations. Our tool-scaling
process also depends on the capability of the general model used for synthesis; in our internal trials,
replacing stronger proprietary models with Qwen3.5-Plus led to noticeably lower generation efficiency and
trajectory quality. Moreover, the synthesized tools are not tied to a specific concrete implementation, which
makes them scalable and potentially more generalizable, but also means that real-world execution still
depends on the maturity of available tools and the way tool feedback is organized for the CUA. Finally,
due to the scarcity of open-source GUI-Tool coordination benchmarks for computer-use agents, our main
performance evaluation is primarily conducted on OSWorld-MCP, leaving broader benchmark coverage as
an important limitation.
Future work should further explore hybrid GUI-Tool action spaces across broader platforms, including
desktop, mobile, and web environments, where the balance between atomic GUI operations and high-level
tools may vary substantially across interface structures and task types. Another promising direction is to
reduce the dependence of agentic RL on heavy sandbox infrastructure by building lighter, more diverse,
and more robust environments with hybrid GUI-Tool actions. We are also interested in asynchronous RL
frameworks that decouple training and inference-time rollout, which may improve the scalability and
stability of long-horizon policy optimization for computer-use agents.
B. Broader Impact and Ethics Statement
ToolCUA aims to improve real-world digital automation by enabling computer-use agents to coordinate
GUI actions and tool calls more efficiently, which may benefit productivity, accessibility, and repetitive
workflow assistance. At the same time, more capable CUAs introduce potential risks, including unauthorized
operation, accidental modification of user data, privacy leakage from desktop observations, and misuse for
automating harmful or deceptive online activities. Our work focuses on benchmarked sandbox environments
and does not grant the agent uncontrolled access to personal accounts, sensitive files, or external services.
For real-world deployment, we believe such systems should require explicit user consent, transparent action
logging, permission boundaries, and human confirmation for high-impact operations.
C. Implementation Details
C.1. Preliminary study: Optimal Path Confusion in Hybrid Action Spaces
To examine whether current CUAs can identify the optimal GUI-Tool path under tool-conditioned contexts,
we conduct a diagnostic comparison between pure GUI execution and hybrid GUI-Tool execution across
multiple agents, as reported in Table 1. All models in the hybrid setting are given access to the same tool
interface and tool documentation through the system prompt. Accuracy is reported over the full tasks. ACS
reports the average completion trajectory steps, reflecting execution efficiency, and Tool-Calls reports the
average number of tool calls.
Experimental Settings.For the results reported in Table 1, we follow two evaluation protocols correspond-
ing to the two action-space settings. For the GUI-only setting, we directly use the official OSWorld-released
17

## Page 18

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
verified trajectories [45] for EvoCUA-32B and the Claude baselines, set the maximum horizon to 50 steps,
and retain only the feasible tasks. For Qwen3VL-8B-Instruct and Qwen3VL-235B-A22B-Thinking, we con-
duct the evaluation ourselves, aligned with the official implementations. For clarity, Qwen3-VL-8B-Instruct
is abbreviated as Qwen3VL-8B, and Qwen3VL-235B-A22B-Thinking is abbreviated as Qwen3VL-235B
throughout Table 1. For the “GUI+Tool” setting, we evaluate the same models directly on OSWorld-MCP,
ensuring consistency with the official prompts and message construction protocol. We also use the same
maximum horizon of 50 steps and report results only on the feasible task subset. See more metric details in
Appendix C.4.
The results in Table 1 reveal a counter-intuitive finding: simply giving a strong model access to both GUI
actions and tools does not reliably improve performance. Instead, the hybrid action space oftenconfusesthe
agent, causing it to deviate from the most effective execution path. More concretely, Table 1 exposes two
representative failure modes that align with the intuition illustrated in Figure 2: once both action spaces
are available, the agent stands at a “forked road” and often fails to choose the right branch.
Failure Mode I: tool underuse.Some models remain overly GUI-centric even when a short tool call is
available. Qwen3VL-8B is the clearest example: after tools are introduced, it invokes tools only 0.00 times
per trajectory on average, which indicates that it almost never leaves the GUI branch. Yet this conservative
behavior does not preserve performance: its accuracy drops from 29.0% to 28.2%, while ACS also slightly
increases from 19.2 to 19.3. This suggests that the model is unable to recognize the decision boundary
where switching to a structured tool would shorten the path and reduce accumulated GUI errors.
FailureModeII:tooloveruse.Attheotherextreme, strongerorlargermodelsmayinvoketoolsaggressively,
but frequent tool usage alone does not translate into better task completion. For example, Qwen3VL-235B
increases its average Tool-Calls to 6.10, yet its accuracy drops from 41.1% to 38.1%. Although its completion
steps decrease from 25.9 to 17.4, the shorter trajectory does not lead to better task success. EvoCUA-32B
shows a similar tendency, invoking tools 7.49 times on average while suffering a substantial 12.0% accuracy
drop. Its steps even increases from 25.0 to 26.1, showing that tool access can simultaneously hurt both
effectiveness and efficiency when the switching policy is poor. The Claude baselines exhibit the same
phenomenon from another angle: Claude-4-sonnet reduces steps from 23.6 to 19.2 and invokes tools
4.50 times on average, while Claude-4.5-sonnet reduces steps from 23.3 to 19.1 and invokes tools 3.90
times on average, yet their accuracies still regress by 4.2% and 13.5%, respectively. These cases indicate
that the agent is not learning “use tools more,” but rather needs to learnwhentool usage is appropriate.
Over-switching can prematurely abandon necessary GUI grounding, call tools before the required context is
established, or commit the trajectory to a brittle tool-heavy path that is shorter but less reliable.
Taken together, Table 1 demonstrates that the core challenge of hybrid GUI-Tool agents is optimal GUI-Tool
path selection rather than raw action-space expansion. The issue is not whether the model can recognize
that a tool exists, but whether it can determine if the current state calls for continued GUI grounding, an
immediate tool invocation, or a later switch after additional GUI setup. In other words, hybrid execution
introduces a trajectory-level decision problem: a locally plausible action may still lead to a globally inferior
path. This is exactly the confusion abstracted by Figure 2, where the agent must choose between the GUI
path and the tool path without a reliable internal policy for deciding which route is actually better. In
contrast, ToolCUA is the only model in Table 1 that benefits from the hybrid action space: its accuracy
improves from 42.9% to 46.8%, while ACS drops from 19.4 to 14.9 with only 0.74 average Tool-Calls.
This result suggests that effective hybrid execution does not require excessive tool usage, but a selective
switching policy that calls tools only at beneficial points along the trajectory. Therefore, these preliminary
results motivate our training paradigm: ToolCUA is designed to internalize optimal GUI-Tool path selection
from interleaved supervision and trajectory-level reinforcement, rather than relying on zero-shot prompting
to resolve the fork on its own.
18

## Page 19

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
C.2. Data Statistics of the Scaling Pipeline
Our Offline Interleaved GUI-Tool Trajectory Scaling Pipeline constructs a robust foundation by aggregating
diverse pure GUI interaction trajectories from OpenCUA [40] and ScaleCUA [18]. To further augment the
data, we leverage diverse powerful MLLMs to execute sandbox rollouts across internal tasks, resulting in
1,200 curated, high-quality trajectories post-filtering. As detailed in Table 5, this combined source corpus
comprises 10,000 trajectories and 192,000 raw GUI steps, with OpenCUA serving as the primary source
(8,500 trajectories). From this base, our pipeline synthesizes 10,000 interleaved GUI-Tool trajectories,
yielding 180k high-quality steps for the warmup Supervised Fine-Tuning (SFT) stage. Furthermore,
we extract a specialized subset of 5k critical switching steps (Dcritical ) to facilitate offline single-turn
Reinforcement Learning (RL).
The synthesis process generates a diverse and hierarchically structured tool inventory. As outlined in Table 6,
the synthetic dataset contains 4,350 unique tools spanning multiple abstraction levels. It is primarily
anchored by fine-grained and mid-grained operations, complemented by coarse-grained skills. To emulate
realistic decision-making complexity, each trajectory provides an average tool pool of 19.75 candidate tools,
from which the agent executes an average of 7.89 tools. Overall, these metrics show that our synthesized
trajectories cover diverse tool types, large candidate pools, and substantial executed tool calls.
Figure 7 visualizes the synthesized tools in a projected space, where each point corresponds to one tool node
and marker shapes denote granularity tiers. Major application categories such asLibreOffice, Chrome,
and VSCode occupy broad and distinguishable regions, indicating that the synthesized inventory does not
collapse into a narrow set of routines. Within each region, the coexistence of fine-grained, mid-grained,
and coarse-grained tools shows that the learned tool space is not restricted to a single abstraction level.
The visualization therefore supports the two intended properties of our bottom-up pipeline: diverse tool
functionality and clear multi-granular organization.
Table 5: Data distribution of pure GUI trajectories used by
our synthesis pipeline.
Data Source Trajs Steps
OpenCUA [40] 8500 110k
ScaleCUA [18] 300 20k
Sandbox collected 1200 62k
Source total 10k 192k
critical steps (D critical ) - 5k
Table 6: Statistics of our interleaved GUI-Tool data.
StatisticsCount
Unique Tools 4,350
fine-grained 2,000
mid-grained 1,900
coarse-grained 450
avg. tool-pool size per traj. 19.75
avg. executed tools per traj. 7.89
C.3. Training Details
Tool-Bootstrapped GUI RFT.In our staged training paradigm, we adopt Qwen3-VL-8B-Instruct [3] as our
base modelM. The warmup SFT is conducted for 3 epochs using full-parameter fine-tuning of both the
vision tower and the LLM backbone on a cluster of8×8 GPUs, resulting in the intermediate modelMs f t.
For the offline single-turn RL phase, we utilize a group size ofrollout=32 , a learning rate of1×10 −6,
and a training batch size of 128 to produceMr f t.
Online Agentic RL Training.During the subsequent online agentic RL stage, we set hyperparameters
λ=0.4 , β=0.2 , andSmax =30 to define the maximum execution horizon. The training configuration for
19

## Page 20

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
Domains
LibreOffice
System
Chrome
VSCode
T erminal
GIMP
GNOME
Settings
File Manager
Google
Granularity
L0 fine-grained
L1 mid-grained
L2+ coarse-grained
Figure 7: Visualization of the synthesized tools in a projected action space, where each point corresponds to one tool
node, colors denote the application taxonomy, and marker shapes denote granularity tiers.
this stage includes a rollout size of 32 per group, a learning rate of1×10 −6, and a training batch size of
32 to obtainToolCUA. For the Tool Appropriateness Reward Term, we leverage the task-level annotations
from OSWorld-MCP [12], which specify whether tool invocation is beneficial for a given task via a label
tb ∈ {1,−1}. To ensure high reward fidelity, we conducted a secondary manual verification of these labels
before incorporating them into our reward function. For agentic training, we directly utilize the tasks from
OSWorld [45] except for the “multi_apps” domain, which is reserved for OOD verification. We also augment
these training tasks using scaled tasks from RLAnything [42] and paraphrase the goal instructions to obtain
new tasks.
CUA Agentic RL in a GUI-Tool Environment.To support large-scale online exploration, we implement
a decoupled training-inference infrastructure using the verl [31] framework, where policy optimization
occurs on a GPU cluster while rollouts are executed on distributed ECS servers. The environment sandbox
is built upon OSWorld [45] QEMU images, incorporating MCP tool designs from OSWorld-MCP [12] and
AutoGLM [17]. We further optimize the tool-calling interface by designing an agent-readable return format
that provides concise, semantically dense feedback to reduce token overhead and improve grounding
accuracy. The online RL phase is supported by around 250 independent Docker instances for environment
rollouts, utilizing8×8GPUs for policy training and4×8GPUs for dedicated inference serving.
20

## Page 21

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
C.4. Benchmark Evaluation
We evaluate ToolCUA primarily on OSWorld-MCP [12], which extends OSWorld with tool actions and
therefore directly measures hybrid GUI-Tool execution. Following the benchmark protocol, we report three
metrics: task accuracy, Tool Invocation Rate (TIR), and Average Completion Steps (ACS). To reduce sandbox
stochasticity, we report average@3 results for OSWorld-MCP and set the maximum number of execution
steps to 50 for each task.
Task Accuracy.Task accuracy is the primary success metric and measures whether an agent completes the
target instruction according to the benchmark evaluator. In OSWorld-MCP, this metric reflects not only
visual grounding and GUI interaction ability, but also whether the agent can use the provided tools to reach
the correct final state.
Tool Invocation Rate (TIR).OSWorld-MCP further separates tasks into Tool-Beneficial Tasks and Non-
Tool-Beneficial Tasks, allowing us to measure whether an agent invokes tools in appropriate contexts rather
than merely calling tools more often. LetNt be the total number of Tool-Beneficial Tasks, andnt the number
of such tasks in which the agent invoked a tool and successfully completed the task during evaluation. Let
Ng be the total number of Non-Tool-Beneficial Tasks, andng the number of such tasks in which the agent
did not invoke a tool and successfully completed the task. We define TIR as:
TIR= (nt +n g)/(Nt +N g)(5)
TIR therefore captures whether the agent aligns its tool usage with task-level tool utility, including both
using tools when they are beneficial and avoiding them when GUI actions are more appropriate.
Average Completion Steps (ACS).ACS measures the average number of environment interaction steps
used by an agent across tasks. ForN tasks, if the number of execution steps for taski is Si, the Average
Completion Steps is computed as:
ACS=
N∑︁
i=1
Si/N(6)
ACS reflects execution efficiency: agents that identify shorter tool-conditioned paths and avoid redundant
GUI operations generally require fewer steps to complete the same task.
Toassesscross-platformtransfer,wealsoevaluateToolCUAonWindowsAgentArena[ 5]. Wesetmax_steps=50
for each task and report the accuracy@avg3 value as the main metric.
C.5. Ablation Details
We conduct three ablation studies to analyze the contribution of each training component and the effect of
the hybrid GUI-Tool action space. The first two studies, shown in Figure 6, examine the effectiveness of
our staged training design. In the first setting, denoted as “w/o Interleaved data”, we remove the offline
interleaved GUI-Tool data bootstrapping stage and directly apply online agentic RL with the proposed Tool-
Efficient Path Reward to the Qwen3-VL-8B-Instruct baseline. This setting tests whether online exploration
alone can acquire tool-calling knowledge and GUI-Tool switching ability from sparse trajectory-level
feedback. In the second setting, the model is first initialized with Tool-Bootstrapped GUI RFT, and then
optimized with a vanilla GRPO-based agentic RL objective that only uses the standard accuracy rewardRacc
and format rewardRf mt. This variant removes the Tool Appropriateness Reward Term and Path Efficiency
Reward Term, isolating the effect of the Tool-Efficient Path Reward after the model has already acquired
basic tool-calling knowledge and local switching capability.
21

## Page 22

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
The third ablation, reported in Table 3, compares training in the hybrid GUI-Tool action space with training
in a pure GUI action space. For the pure-GUI setting, we fine-tune the Qwen3-VL-8B-Instruct baseline using
a GUI-only dataset of comparable scale to the warmup SFT data, and then perform online agentic RL within
the pure GUI action space. Since tool actions are unavailable in this environment, the reward consists
only ofRacc +R f mt+R length , where the Path Efficiency Reward Term still encourages efficient execution
but cannot reward tool-appropriate decisions. The final evaluation is also conducted under the pure GUI
action space, allowing us to directly compare whether hybrid GUI-Tool training provides a higher-fidelity
optimization setting than GUI-only training.
For all online agentic RL ablations, we follow the evaluation protocol in Section C.4 and report average@3
results. The maximum rollout horizon during training is set tomax_steps=30. Due to the computational
cost of sandbox-based online RL under our decoupled training-inference infrastructure, each run is trained
for roughly 25 optimization steps. With a unified training batch size of 32 and dynamic filtering enabled,
each ablation uses approximately 1,200 effective training samples. Each run consumes approximately8×8
GPUs together with distributed ECS sandbox workers for about six days.
22

## Page 23

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
D. More Case Study
Table 7: Case study for libreoffice calc. (ID: 535364ea-05bd-46ea-9937-9f55c68507e8)
Agent Prediction Tool-Calling re-
sponse Screenshot
Step 2: Action: Get the workbook
information to identify the file
path and sheet details.
<tool_call>
{\"name\": \"
osworld_mcp_libreoffice_calc.
get_workbook_info\", \"arguments\":
{}}
</tool_call>
<tool_response>
{"type": "text", "text": "{\"
success\": true, \"result\": {\"
file_path\": \"file:///home/user/
SummerSales.xlsx\", \"file_title\":
\"SummerSales.xlsx\", \"sheets\":
[{\"name\": \"Sheet1\", \"index\":
0, \"visible\": true, \"row_count\":
30, \"column_count\": 7}], \"
active_sheet\": \"Sheet1\", \"
sheet_count\": 1}, \"error_message
\": null}"}
</tool_response>
Step 3: Action: Get content
information of Sheet1 to understand
the data structure including
headers and data ranges.
<tool_call>
{\"name\": \"
osworld_mcp_libreoffice_calc.
env_info\", \"arguments\": {\"
sheet_name\": \"Sheet1\"}}
</tool_call>
<tool_response>
{"type": "text", "text": "{\"
success\": true, \"result\": {\"
name\": \"Sheet1\", \"data\": \" |
A| B| C | D | E | F | G |\\n
--|-----...}, \"error_message\":
null}"}
</tool_response>
Step 4: Action: Create a new sheet
named \"Sheet2\" to serve as the
destination for the pivot tables.
<tool_call>
{\"name\": \"
osworld_mcp_libreoffice_calc.
switch_active_sheet\", \"arguments
\": {\"sheet_name\": \"Sheet2\"}}
</tool_call>
<tool_response>
{"type": "text", "text": "{\"
success\": true, \"result\": \"
Success\", \"error_message\": null
}"}
</tool_response>
Step 5: Action: Create the first
pivot table named'PivotTable1'in
Sheet2 to show total revenue for
each product.
<tool_call>
{"name": "
osworld_mcp_libreoffice_calc.
create_pivot_table", "arguments":
{"source_sheet": "Sheet1", "
table_name": "PivotTable1", "
row_fields": ["F"], "value_fields":
["G"], "aggregation_function": "
sum", "target_cell": "A1"}}
</tool_call>
<tool_response>
{"success": true, "result": "
Success", "error_message": null}
</tool_response>
Step 6: Action: Create the second
pivot table named'PivotTable2'in
Sheet2 to show total revenue for
each sales channel.
<tool_call>
{"name": "
osworld_mcp_libreoffice_calc.
create_pivot_table", "arguments":
{"source_sheet": "Sheet1", "
table_name": "PivotTable2", "
row_fields": ["E"], "value_fields":
["G"], "aggregation_function": "
sum", "target_cell": "A19"}}
</tool_call>
<tool_response>
{"success": true, "result": "
Success", "error_message": null}
</tool_response>
Analysis:This case studies a LibreOffice Calc task where the instruction is to create two pivot tables in a
new sheet named Sheet2, showing total revenue by product and by sales channel. Tool calling helps by
letting the agent interact directly with Calc, inspect workbook metadata, read sheet content, and directly
call create_pivot_table” from the env info.
23

## Page 24

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
Table 8: Case Study of VS Code (ID: 6ed0a554-cbee-4b44-84ea-fd6c042f4fe1).
Agent Prediction Tool-Calling re-
sponse Screenshot
Step 1: Action: Add the folder'/
home/user/data1'to the current
workspace in VSCode.
<tool_call>
{\"name\": \"osworld_mcp_code.
add_folder\", \"arguments\": {\"
folder\": \"/home/user/data1\"}}
</tool_call>"
<tool_response>
{"type": "text", "text": "{\"
success\": true, \"result\": \"
Successfully added folder\", \"
error_message\": null}"}
</tool_response>
Step 2: Action: Add the folder'/
home/user/data2'to the current
workspace in VSCode.
<tool_call>
{\"name\": \"osworld_mcp_code.
add_folder\", \"arguments\": {\"
folder\": \"/home/user/data2\"}}
</tool_call>"
<tool_response>
{"type": "text", "text": "{\"
success\": true, \"result\": \"
Successfully added folder\", \"
error_message\": null}"}
</tool_response>
Step 3: Action: Click on the "Yes,
I trust the authors" button in the
trust dialog popup.
<tool_call>
{\"name\": \"computer_use\", \"
arguments\": {\"action\": \"click\",
\"coordinate\": [596, 627]}}
</tool_call>
## Not available
Step 4: Action: Terminate the task
as successful since the goal has
been accomplished.
<tool_call>
{\"name\": \"computer_use\", \"
arguments\": {\"action\": \"
terminate\", \"status\": \"success
\"}}
</tool_call>
## Not available
Analysis:
This case primarily demonstrates a VS Code workspace management task: “adding /home/user/data1 and
/home/user/data2 to the current workspace”. During execution, the agent first directly invokes the tool
capability “addfolder” to add each of the two folders to the current VS Code window. This step highlights
the efficiency and determinism of tool calls when handling structured editing tasks. Subsequently, although
the core objective had already been accomplished via the tool calls, VS Code presented a "Do you trust the
authors?" trust confirmation dialog. Rather than stalling at this point, the agent switched to GUI interaction
mode, clicked the "Yes, I trust the authors" button, and completed the remaining follow-up actions on the
interface — ensuring the workspace was fully brought into a usable state.
This case demonstrates that the system does not rely on a single interaction paradigm. Tool calls are
well-suited for directly completing well-defined editing operations, while GUI actions can handle scenarios
that tools cannot fully cover — such as pop-up dialogs, permission confirmations, and interface state
finalization. By combining the two, the agent is not only able to complete the primary task efficiently, but
also capable of closing the loop on post-execution interactions within a real desktop environment.
24

## Page 25

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
Table 9: Case study for multi-apps. (ID: 02ce9a50-7af2-47ed-8596-af0c230501f8)
Agent Prediction Tool-Calling re-
sponse Screenshot
Step 2: Action: typed'terminal'
into the search box.
<tool_call>
{\"name\": \"computer_use\", \"
arguments\": {\"action\": \"type\",
\"text\": \"terminal\", \"clear\":
0, \"enter\": 0}}
</tool_call>
## Not available
Step 8: Action: dragged mouse from
the left to the right and released.
<tool_call>
{\"name\": \"computer_use\", \"
arguments\": {\"action\": \"
mouse_move\", \"coordinate\": [24,
36]}}
</tool_call>
## Not available
Step 18: Action: Double-clicked on
ls.png.
<tool_call>
{\"name\": \"computer_use\", \"
arguments\": {\"action\": \"
double_click\", \"coordinate\":
[314, 251]}}
</tool_call>
## Not available
Step 19: Action: Save the document.
<tool_call>
{\"name\": \"
osworld_mcp_libreoffice_writer.save
\", \"arguments\": {}}
</tool_call>
<tool_response>
{"type": "text", "text": "{\"
success\": true, \"result\": \"
Success\", \"error_message\": null
}"},
</tool_response>
Step 20: Action: Terminate the task
as successful.
<tool_call>
{\"name\": \"computer_use\", \"
arguments\": {\"action\": \"
terminate\", \"status\": \"success
\"}}
</tool_call>
## Not available
Analysis:“I am currently utilizing LibreOffice Writer to compose a Linux tutorial, and I intend to display
the outcomes generated by executing the¨ls¨command in /home/user. Kindly execute this command and
save the screenshot of the terminal as ’ls.png’ on the Desktop.” This case aims to generate visual evidence
for a Linux tutorial: the agent needs to run ls in /home/user and save a terminal screenshot as ls.png on
the Desktop. The key steps include opening the terminal, executing the command, capturing and saving
the screenshot, checking the generated image, saving the LibreOffice document, and marking the task as
complete. Each step contributes to turning the user’s instruction into an actual file-based result.
25

## Page 26

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
Table 10: Case study for libreoffice impress. (ID: 57667013-ea97-417c-9dce-2713091e6e2a”)
Agent Prediction Tool-Calling re-
sponse Screenshot
Step 1: Action: Navigate to slide 5
by clicking on its thumbnail in
the slide navigation panel.
<tool_call>
{"name": "
osworld_mcp_libreoffice_impress.
go_to_slide", "arguments": {"
slide_index": 5}}
</tool_call>
<tool_response>
{"success": true, "result": "
Successfully navigated to slide 5",
"error_message": null}
</tool_response>
Step2: Action: Get the slide count
to understand the total number of
slides in the presentation.
<tool_call>
{"name": "
osworld_mcp_libreoffice_impress.
get_slide_count", "arguments": {}}
</tool_call>
<tool_response>
{"success": true, "result": {"value
": 5}, "error_message": null}
</tool_response>
Step 3: Action: Get the content of
all slides to identify and
understand the textboxes that need
their font color changed to yellow.
<tool_call>
{"name": "
osworld_mcp_libreoffice_impress.
env_info", "arguments": {}}
</tool_call>
<tool_response>
{"success": true, "result": "Slide
1:\n- Box 0: \n- Box 1: \n- Box 2:
\n- Box 3: \n- Box 4: \n- Box 5:
\n- Box 7: \n- Box 8: \n- Box 9: \
n- Box 10: \n- Box 12: \n\nSlide
2:\n- Box 0: \n- Box 1: \n\nSlide
3:\n- Box 0: \n- Box 1: HELLO\
nTHERE!\n- Box 2: \n- Box 4: I'm
Rain. Welcome to my education
presentation.\nFollow me at
@reallygreatsite to learn more.\n-
Box 5: \n- Box 6: \n\nSlide 4:\n-
Box 0: \n- Box 1: \n- Box 2: \n-
Box 3: \n\nSlide 5:\n- Box 0: \n-
Box 3: WRITE AN ORIGINAL\
nSTATEMENT OR\nINSPIRING QUOTE\n-
Box 4: Include a credit, citation,
or supporting message\n\nCurrent
Slide Index: 5", "error_message":
null}
</tool_response>
Step 4: Action: Set the font color
of the title text in slide 5 to
yellow.
<tool_call>
{"name": "
osworld_mcp_libreoffice_impress.
set_text_color", "arguments": {"
slide_index": 5, "box_index": 3, "
color": "yellow"}}
</tool_call>
<tool_response>
{"success": true, "result": "
Successfully set text color to
yellow for textbox 3 on slide 5", "
error_message": null}
</tool_response>
Step 5: Action: Terminate the task
as successful since the goal has
been accomplished.
<tool_call>
{"name": "computer_use", "arguments
": {"action": "terminate", "status":
"success"}}
</tool_call>
## Not available
Analysis:This task instruction is “Navigate to slide 5 and set the font color of all textboxes to yellow. Use
exactly ’yellow’, no variations such as light yellow, dark yellow, or any other color.”. This is a typical case
where tools are available to boost execution efficiency. In this case, ToolCUA firstnagivate_to_slide, calling
env_infoto get the bbox id and finally callingset_text_color(box_index=3)to complete this task.
26

## Page 27

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
E. Prompts Used in Data Pipeline
This section lists the prompts used in our Offline Interleaved GUI-Tool Trajectory Scaling Pipeline. The
sequence is as follows: SCREENSHOT DESCRIPTION PROMPT summarizes raw UI states; TOOL GEN-
ERATION PROMPT proposes the tool library; FIX TOOL PROMPT repairs invalid tool definitions; JOINT
GENERATION PROMPT generates step-by-step tool trajectories; PREDICT SCREENSHOT PROMPT and
DESCRIBE AND LOCATE PROMPT support state prediction and screenshot grounding; and MERGE TREE
PLANNING PROMPT together with BOTTOM UP MERGE PROMPT builds the bottom-up hierarchy by
merging fine-grained steps into coarser tools.
Prompts Used in Data Pipeline
SCREENSHOT DESCRIPTION PROMPT
Describe this desktop screenshot in English.
Include:
1. Which application, window, or web page is visible
2. The main interactive UI elements that are visible, such as buttons, menus, tabs, tables, forms, inputs, dialogs, or side panels
3. The primary content currently shown on screen
Write 2-4 sentences.
Do not invent details that are not visible in the screenshot.
Return plain text only, not JSON.
JOINT GENERATION PROMPT
## Role
You are a trajectory generator, not a real agent.
You must simulate how a smart and efficient agent would complete exactly the current step of a computer-using task.
## Current trajectory diversity strategy
{granularity_instruction}
## Important constraints
- Do not generate multiple steps at once.
1. The screenshot description already tells you the current screen state, so you do not need a separate "view page" or "inspect page"
tool.
2. Do not call wait-like tools more than once in a row.
3. Do not call wait-like tools unless there is a clear error condition.
4. Every step must make progress toward the task goal.
5. Assume the network, application, and desktop environment are functioning normally. Do not wait for loading unless the state
explicitly requires it.
6. Choose only a tool action that can plausibly move the current state to a later real state in the recorded trajectory.
7. Do not call terminate unless the task has already reached the final recorded state.
## Task goal
{goal}
## Trajectory history
{history}
## Current screenshot description
{screenshot_description}
## Current virtual world state
{world_state}
## Available tools for this task
{tools}
Generate the complete output for the current step, including:
1. Observation
2. Thought
3. Action
4. Tool Call
5. Tool Response
## Rules for generating the Step
- The observation should reflect the current screenshot description, especial attention to important region.
- Thougt must demonstrate the agent's real thinking progress advancing the task given current step.
- Action must be a natural-language description of the intended tool call action, it should be a simple, short and concise sentence.
NOT any explict GUI desctiption like`click`,`drag`,`key`and so no.
- Tool call should be a valid JSON foramt of the intended tool call.
## Rules for generating the Tool Response
- The response fields must strictly follow the selected tool's returns schema.
- Do not include fields that are not defined by the tool's returns schema.
- The value of success must be consistent with the current world_state.
- Concrete values in result, such as URLs, file paths, window names, or extracted content, must come from the trajectory history or
the current screenshot description.
- Do not invent a tool usage whose effect would not be visibly groundable to a later recorded screenshot.
27

## Page 28

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
## Output requirements
- Generate exactly one step.
- The root object must contain the following fields and no wrapper layer.
- Output as exactly the JSON object in the following format:
## Output format
{{
"observation": "Observation grounded in the current screenshot description",
"thought": "Reasoning about the next Tool calling action. It must clearly advance the task.",
"action": "Simple and concise natural-language description of the intended Tool calling action",
"tool_call": {{
"tool_name": "One of the available tools",
"tool_parameters": {{
"parameter_name": "parameter value that matches the tool schema"
}}
}},
"tool_response": {{
"success": true,
"result": "...",
"error_message": null
}}
}}
TOOL GENERATION PROMPT
You need to design a set of semantic-level tools for the following computer-using task.
The tools must be useful for this task and also be grounded to the state transitions visible in the recorded trajectory.
## Task goal
{goal}
## Current diversity round
{round_name}
## Tool granularity strategy
{granularity_instruction}
## Recorded trajectory frame descriptions
{trajectory_context}
## Required tool schema reference
{meta_schema}
## Tool design principles
- Think about the specific applications or software likely used in this task and design tools accordingly.
- Generate no more than 15 tools an no less than 5 tools.
- Category must be one of: navigation / interaction / extraction / filesystem / system / terminate.
- Every non-terminate tool must include`granularity`with value`fine`or`coarse`.
- The`terminate`tool may omit`granularity`, but if present it must be`coarse`.
- Each tool's returns object must contain exactly these fields:
- success (boolean)
- result (object/string/null)
- error_message (string/null)
- Do not generate wait / sleep / delay / get_ui_tree style tools.
- Each tool should represent one complete user intention, not one primitive UI gesture.
- A user intent such as "open the export dialog" or "apply the date filter" should be a single tool even if the actual UI would
require multiple clicks.
- The tools must express user intent at the desktop workflow level, not low-level UI mechanics.
Avoid low-level tools such as:
- click_element(element_description)
- input_text(field, text)
- scroll_down(pixels)
- tap_coordinates(x, y)
Prefer semantic tools such as:
- open_application(application_name)
- navigate_to_section(section_name)
- search_records(query)
- set_filter(filter_name, value)
- export_report(destination_path)
- confirm_submission()
## Multi-granularity requirement
- The tool library must contain both finer-grained tools and coarser-grained tools.
- Fine-grained tools should capture a focused semantic intent that usually corresponds to one local sub-goal, such as opening a
specific panel, applying one filter, selecting one record, or confirming one dialog.
- Coarse-grained tools should capture a broader semantic intent that may cover several adjacent UI operations, such as preparing an
export, completing a checkout stage, or finishing a search-and-download subroutine.
- Keep every tool grounded to visible state transitions in the recorded trajectory even when it is coarse-grained.
- Avoid making every tool equally granular. The mix should reflect the current round strategy.
- Among non-terminate tools, include at least {min_fine_grained_tools} fine-grained tools and at least {min_coarse_grained_tools}
coarse-grained tools.
## Grounding rule
- Prioritize tools that explain real state transitions visible in the recorded trajectory frames.
- The main tool set should be sufficient for the observed workflow in this trajectory.
- You may add a small number of app-relevant helper tools, but do not invent a broad toolbox that cannot be grounded to the recorded
states.
28

## Page 29

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
## Naming rule
- Use lowercase_with_underscores.
- If a tool is clearly tied to a specific desktop application, its name must start with that application name, for example:
-`libreoffice_export_pdf`
-`vscode_open_user_settings`
-`chrome_download_file`
Do not use the specific website name as the application name, where'chrome'is the suitbale application name.
- If no concrete application can be determined, the name must start with`general_`.
- Avoid vague names whose purpose is unclear from the name alone.
- Bad examples:
-`open_file`
-`set_option`
-`click_button`
-`edit_content`
## Terminate rule
- There must be exactly one tool named`terminate`.
- The`terminate`tool must use category`terminate`.
- No non-`terminate`tool may use category`terminate`.
- No other tool may express task-ending semantics such as finish task, complete task, end task, stop task, or report task completion.
## Existing tools that may be reused
{existing_tools}
## Output format
{{
"tools": [...]
}}
Return valid JSON only.
"""
FIX_TOOL_PROMPT = """
The following tool definition is invalid:
{tool}
## Validation errors
{error_msg}
## Required schema
{meta_schema}
Please repair the tool definition so that it matches the schema.
Return exactly one JSON object in the following format:
{{
"name": "...",
"description": "...",
"granularity": "fine or coarse",
"parameters": {{}},
"returns": {{
"success": {{"type": "boolean"}},
"result": {{"type": ["string", "object", "null"]}},
"error_message": {{"type": ["string", "null"]}}
}},
"category": "...",
"side_effects": []
}}
FIX TOOL PROMPT
The following tool definition is invalid:
{tool}
## Validation errors
{error_msg}
## Required schema
{meta_schema}
Please repair the tool definition so that it matches the schema.
Return exactly one JSON object in the following format:
{{
"name": "...",
"description": "...",
"granularity": "fine or coarse",
"parameters": {{}},
"returns": {{
"success": {{"type": "boolean"}},
"result": {{"type": ["string", "object", "null"]}},
"error_message": {{"type": ["string", "null"]}}
}},
"category": "...",
"side_effects": []
}}
PREDICT SCREENSHOT PROMPT
29

## Page 30

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
## Role
You are a desktop UI state predictor.
## Task goal
{goal}
## Action that was just performed
- Tool: {tool_name}
- Parameters: {tool_parameters}
- Result: {tool_response}
## UI state before the action
{previous_screenshot_description}
## Current world state
{world_state}
## Instruction
Predict what the desktop interface most likely shows after that action.
Be concrete. Mention the current page, window, dialog, visible UI elements, and any visible data or status changes.
Write 3-5 sentences in English.
Return plain text only, not JSON.
DESCRIBE AND LOCATE PROMPT
## Action that was just performed
Tool: {tool_name}
Parameters: {tool_parameters}
Result: {tool_response}
## Tasks
### Task 1: Describe the current screenshot
Describe the current desktop screenshot before the action in 3-5 English sentences.
### Task 2: Locate the best matching result screenshot
You are given {num_candidates} candidate screenshots, indexed from 1.
Select the candidate that best represents the UI state after the action has completed.
## Output format
{{
"current_description": "English description of the current screenshot",
"matched_index": 1,
"confidence": "high/medium/low/none",
"reason": "What visible evidence shows that this screenshot matches the post-action state"
}}
If none of the candidates match, set matched_index to null.
MERGE TREE PLANNING PROMPT
You are planning an optimal bottom-up merge tree for a fine-grained desktop tool trajectory.
## Task goal
{goal}
## Fine-grained leaf steps
{leaf_summary}
## Constraints
- Leaf steps are indexed from 0 to {max_leaf_index}.
- Preserve the original left-to-right leaf order exactly.
- Every internal merge node must merge between 2 and {max_branching_factor} contiguous children.
- Children may be either direct leaf indices or nested internal nodes.
- Every internal node must represent a coherent higher-level sub-goal.
- Prefer a tree that maximizes semantic cohesion inside each merge and clear abstraction jumps between levels.
- Avoid unnecessary merges that do not create a meaningful higher-level action.
- The final root must cover all leaves from 0 to {max_leaf_index}.
- The tree height must not exceed {max_coarse_levels} coarse levels above the fine leaves.
- Return English only.
## Output format
{{
"tree": {{
"summary": "Short summary of the root-level task subroutine",
"children": [
0,
{{
"summary": "Merged sub-goal summary",
"children": [1, 2]
}},
{{
"summary": "Another merged sub-goal summary",
"children": [
{{
"summary": "Nested merged sub-goal",
"children": [3, 4]
}},
5
30

## Page 31

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
]
}}
]
}}
}}
Return valid JSON only.
BOTTOM UP MERGE PROMPT
You are performing bottom-up multi-granularity tool synthesis for a desktop task trajectory.
## Task goal
{goal}
## Target granularity level
{target_level}
## Instruction
You are given a contiguous chunk of already-grounded finer-grained tool steps.
Synthesize one broader tool that compresses the whole chunk into a single higher-level semantic action.
The merged tool must still be grounded to the same final UI state reached by the chunk.
## Rules
- The merged tool must summarize the whole chunk, not just the final fine-grained action.
- The merged tool must be semantically broader than each constituent fine-grained tool.
- Do not invent effects beyond the final state already reached by the chunk.
- The merged tool must use`granularity = "coarse"`.
- The merged tool call name in`merged_step.tool_call.tool_name`must exactly match`tool_definition.name`.
- The merged step's screenshot index and result state will be assigned by the caller, so do not include them.
- Keep the tool response grounded to the final fine-grained step in the chunk.
- Do not use terminate semantics.
- Return English only.
## Chunk summary
{chunk_summary}
## Output format
{{
"tool_definition": {{
"name": "lowercase_with_underscores",
"description": "One-sentence broader semantic intent for the whole chunk",
"granularity": "coarse",
"parameters": {{}},
"returns": {{
"success": {{"type": "boolean"}},
"result": {{"type": ["string", "object", "null"]}},
"error_message": {{"type": ["string", "null"]}}
}},
"category": "navigation|interaction|extraction|filesystem|system",
"side_effects": []
}},
"merged_step": {{
"observation": "Observation of the UI state before the merged action starts",
"thought": "Reasoning about why this broader tool covers the whole chunk",
"action": "Short natural-language summary of the merged higher-level action",
"tool_call": {{
"tool_name": "same as tool_definition.name",
"tool_parameters": {{
"parameter_name": "parameter value"
}}
}},
"tool_response": {{
"success": true,
"result": {{}},
"error_message": null
}}
}}
}}
Return valid JSON only.
F. Messages for ToolCUA
Our ToolCUA utilizes the following message construction for training and inference. The system prompt is
composed with predefined GUI actions, optional tool-calling actions, and an "important_reminder” section.
31

## Page 32

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
ToolCUA Messages
System Prompt
IMPORTANT_GUI_ONLY = """<IMPORTANT>
Reminder:
- The`computer_use`function provides **GUI actions** to interact with the computer directly via mouse and keyboard.
- After each GUI action, you will receive a new screenshot reflecting the current state of the screen.
- Always consult the latest screenshot before deciding your next action.
</IMPORTANT>"""
IMPORTANT_WITH_MCP = """<IMPORTANT>
Reminder:
- Use`computer_use`to interact with the computer via mouse and keyboard.
-`computer_use`GUI actions usually only provide a simple success result such as`Success`.
- After each action, you will receive a new screenshot of the current state of the computer.
- If there are other functions, they are MCP Tool actions, used to interact with the MCP server in computer.
- Their results are returned as screenshot and a textual raw JSON string with fields`success`,`result`, and`error_message`.
- Some MCP Tool actions may NOT cause any visible change in the screenshot, so rely on the JSON tool result when appropriate.
- Do NOT use`read_text_file`to read PDF or other non-plaintext files; use GUI actions instead.
- Do NOT repeat the same MCP Tool call if it keeps failing or produces no useful progress -try a different approach or terminate.
- Do NOT repeatedly call`env_info`tools to retrieve file information.
</IMPORTANT>"""
OSWorld_MCP_SYS_PROMPT = (
"# Tools\n\n"
"You may call one or more functions to assist with the user query.\n\n"
"You are provided with function signatures within <tools></tools> XML tags:\n"
"<tools>\n"
"{{"
'"type": "function",'
'"function": {{'
'"name_for_human": "computer_use",'
'"name": "computer_use",'
'"description": ('
'"Use a mouse and keyboard to interact with a computer, and take screenshots.\\n'
'* This is an interface to a desktop GUI. You do not have access to a terminal or applications menu. You must click on
desktop icons to start applications.\\n'
'* Some applications may take time to start or process actions, so you may need to wait and take successive screenshots to
see the results of your actions. E.g. if you click on Firefox and a window doesn\'t open, try wait and taking another
screenshot.\\n'
'* The screen\'s resolution is 1000x1000.\\n'
'* Whenever you intend to move the cursor to click on an element like an icon, you should consult a screenshot to determine
the coordinates of the element before moving the cursor.\\n'
'* If you tried clicking on a program or link but it failed to load even after waiting, try adjusting your cursor position
so that the tip of the cursor visually falls on the element that you want to click.\\n'
'* Make sure to click any buttons, links, icons, etc with the cursor tip in the center of the element. Don\'t click boxes
on their edges unless asked."'
'),'
'"parameters": {{'
'"properties": {{'
'"action": {{'
'"description": ('
'"\\n'
'*`key`: Performs key down presses on the arguments passed in order, then performs key releases in reverse
order.\\n'
'*`type`: Type a string of text on the keyboard.\\n'
'*`mouse_move`: Move the cursor to a specified (x, y) pixel coordinate on the screen.\\n'
'*`left_click`: Click the left mouse button at a specified (x, y) pixel coordinate on the screen.\\n'
'*`left_click_drag`: Click and drag the cursor to a specified (x, y) pixel coordinate on the screen.\\n'
'*`right_click`: Click the right mouse button at a specified (x, y) pixel coordinate on the screen.\\n'
'*`middle_click`: Click the middle mouse button at a specified (x, y) pixel coordinate on the screen.\\n'
'*`double_click`: Double-click the left mouse button at a specified (x, y) pixel coordinate on the screen.\\n'
'*`triple_click`: Triple-click the left mouse button at a specified (x, y) pixel coordinate on the screen (
simulated as double-click since it\'s the closest action).\\n'
'*`scroll`: Performs a scroll of the mouse scroll wheel.\\n'
'*`hscroll`: Performs a horizontal scroll (mapped to regular scroll).\\n'
'*`wait`: Wait specified seconds for the change to happen.\\n'
'*`terminate`: Terminate the current task and report its completion status.\\n'
'*`answer`: Answer a question.\\n'
'"'
'),'
'"enum": ["key", "type", "mouse_move", "left_click", "left_click_drag", "right_click", "middle_click", "
double_click", "scroll", "wait", "terminate"],'
'"type": "string"'
'}},'
'"keys": {{"description": "Required only by`action=key`.", "type": "array"}},'
'"text": {{"description": "Required only by`action=type`.", "type": "string"}},'
'"coordinate": {{"description": "The x,y coordinates for mouse actions.", "type": "array"}},'
'"pixels": {{"description": "The amount of scrolling.", "type": "number"}},'
'"time": {{"description": "The seconds to wait.", "type": "number"}},'
'"status": {{"description": "The status of the task.", "type": "string", "enum": ["success", "failure"]}}'
'}},'
'"required": ["action"],'
'"type": "object"'
'}},'
'"args_format": "Format the arguments as a JSON object."'
'}}'
32

## Page 33

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
'}}\n'
"{tool_list}\n"
"</tools>\n\n"
"For each function call, return a json object with function name and arguments within <tool_call></tool_call> XML tags:\n"
"<tool_call>\n"
'{{"name": <function-name>, "arguments": <args-json-object>}}\n'
"</tool_call>\n\n"
"{important_reminder}\n\n"
"# Response format\n\n"
"Response format for every step:\n"
"1) Action: a short imperative describing what to do in the UI, or specifying which tool to invoke\n"
"2) A single <tool_call>...</tool_call> block containing only the JSON: "
'{{"name": <function-name>, "arguments": <args-json-object>}}.\n\n'
"Rules:\n"
"- Output exactly in the order: Action, <tool_call>.\n"
"- Be brief: one sentence for Action.\n"
"- Do not output anything else outside those parts.\n"
"- If finishing, use action=terminate in the tool call."
)
Message Construction
# We construct a multimodal message list as follows:
# 1) A system message containing the tool-calling specification. The system prompt is composed of three parts:
# (a) the predefined GUI action schema for`computer_use`(always present);
# (b) optional MCP tool definitions appended from obs["tool_list"] (only when action_space == "mcp" and tools exist);
# (c) an important-reminder section -either
# IMPORTANT_WITH_MCP or IMPORTANT_GUI_ONLY -(only when action_space == "mcp", omitted entirely when action_space == "pyautogui").
# 2) For historical context, we keep: steps before the history window [0, t0) as a text-only action history embedded in
instruction_prompt ("Step 1: ..., Step 2: ..., ..."); and at most the most recent history_n (= 5) screenshots (image history), each
paired with its tool-calling result in a <tool_response> block.
# 3) For each retained past step i in [t0, T): append a user message containing -only for the first retained step i == t0 -
instruction_prompt prepended as a text part (task instruction + text-only pre-window action history), followed by a <tool_response>
block consisting of the textual tool-calling result tool_calling_results[i] and screenshot[i] as an image_url part; then append an
assistant message with the model's response at step i (Action + <tool_call>).
# 4) For the current step T: if T == 0 and history_n > 0 (very first step, no tool has been called yet), append a user message with
instruction_prompt and the bare current screenshot as an image_url part (no <tool_response> wrapper); otherwise (T > 0, or T == 0
with history_n == 0), append a user message containing a <tool_response> block with cur_tool_calling_result and the current
screenshot as an image_url part, additionally prepending instruction_prompt when history_n == 0 since no prior turn carried it.
# Key variables:
# - T: current step index (0-based), i.e., T = len(actions)
# - history_n: maximum number of past steps retained as image history, fixed at 5
# - t0: start index of the history window, t0 = max(0, T - history_n)
# - screenshots[i]: the processed screenshot at step i, uploaded as an OSS URL
# - tool_calling_results[i]: the textual tool-calling result received at step i, i.e.,
# obs["exe_result"] after executing step i's action; defaults to "Success" if empty
# - responses[i]: the model's response text at step i (Action + <tool_call>)
# - cur_screenshot: OSS URL of the current screenshot at step T
# - cur_tool_calling_result: tool_calling_results[T], the result received before step T
messages = [
{"role": "system", "content": [{"type": "text", "text": system_prompt}]}
]
t0 = max(0, T - history_n)
previous_actions_str = "None" if t0 == 0 else "\n".join(
[f"Step {i+1}: {actions[i]}" for i in range(t0)]
)
instruction_prompt = f"""Please generate the next move according to the UI screenshot, instruction and previous actions.
Instruction: {instruction}
Previous actions:
{previous_actions_str}"""
for i in range(t0, T):
user_content = []
if i == t0:
user_content.append({"type": "text", "text": instruction_prompt})
user_content += [
{"type": "text", "text": "<tool_response>\n"},
{"type": "text", "text": tool_calling_results[i]},
{"type": "image_url", "image_url": {"url": screenshots[i]}},
{"type": "text", "text": "\n</tool_response>"},
]
messages.append({"role": "user", "content": user_content})
messages.append({"role": "assistant", "content": [{"type": "text", "text": responses[i]}]})
if T == 0 and history_n > 0:
messages.append({
"role": "user",
"content": [
{"type": "text", "text": instruction_prompt},
{"type": "image_url", "image_url": {"url": cur_screenshot}},
]
})
else:
33

## Page 34

ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents
current_user_content = []
if history_n == 0:
current_user_content.append({"type": "text", "text": instruction_prompt})
current_user_content += [
{"type": "text", "text": "<tool_response>\n"},
{"type": "text", "text": cur_tool_calling_result},
{"type": "image_url", "image_url": {"url": cur_screenshot}},
{"type": "text", "text": "\n</tool_response>"},
]
messages.append({"role": "user", "content": current_user_content})
34
