# Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning - Extracted Text

- Source note: [[Are Tools Always Beneficial - Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning]]
- Source PDF: `assets/Are Tools Always Beneficial - Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning.pdf`
- Extracted: 2026-05-20
- Extractor: pypdf
- Pages: 26
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for
Dual-Mode Multimodal LLM Reasoning
Qinghe Ma 1 Zhen Zhao 2 Yiming Wu3 Jian Zhang 1 Lei Bai 2 Yinghuan Shi 1 4
Abstract
Tool-augmented reasoning has emerged as a
promising direction for enhancing the reasoning
capabilities of multimodal large language mod-
els (MLLMs). However, existing studies mainly
focus on enabling models to perform tool invoca-
tion, while neglecting the necessity of invoking
tools. We argue that tool usage is not always
beneficial, as redundant or inappropriate invo-
cations largely increase reasoning overhead and
even mislead model predictions. To address this
issue, we introduce AutoTool, a model that adap-
tively decides whether to invoke tools according
to the characteristics of each query. Within a re-
inforcement learning framework, we design an
explicit dual-mode reasoning strategy with mode-
specific reward functions to guide the model to-
ward producing accurate responses. Moreover,
to prevent premature bias toward a single reason-
ing mode, AutoTool jointly explores and balances
tool-assisted and text-centric reasoning through-
out training, and promotes free exploration in later
stages. Extensive experiments demonstrate that
AutoTool exhibits outstanding performance and
high efficiency, yielding a 21.8% accuracy gain on
V* benchmark compared to the base model, and
a 44.9% improvement in efficiency over existing
tool-augmented methods on POPE benchmark.
Code is available at https://github.com/
MQinghe/AutoTool.
1The State Key Laboratory for Novel Software Technol-
ogy, Nanjing University, Nanjing, China 2Shanghai Artificial
Intelligence Laboratory, Shanghai, China 3School of Comput-
ing and Data Science, The University of Hong Kong, Hong
Kong, China 4The Institute of Brain-Computer Interface, Nan-
jing University, Nanjing, China. Correspondence to: Zhen Zhao
<zhaozhen@pjlab.org.cn>, Yinghuan Shi<syh@nju.edu.cn>.
Proceedings of the 43 rd International Conference on Machine
Learning, Seoul, South Korea. PMLR 306, 2026. Copyright 2026
by the author(s).
1. Introduction
By decomposing complex problems into a sequence of rea-
soning steps, chain-of-thought (CoT) prompting (Wei et al.,
2022; Kojima et al., 2022) has endowed multimodal large
language models (MLLMs) (Team et al., 2023; Liu et al.,
2023; Wang et al., 2024b; Bai et al., 2025) with stronger
reasoning capabilities. However, most existing approaches
follow the textual reasoning paradigm of large language
models (LLMs) (Achiam et al., 2023; Dubey et al., 2024;
Guo et al., 2025), leaving current MLLMs constrained by
linguistic bias that limits their ability to effectively lever-
age multimodal information. The multimodal CoT (MCoT)
prompt (Zhang et al., 2025; Wang et al., 2025a), exempli-
fied by the “Thinking with Images” approach of OpenAI
o3 (OpenAI, 2025), injects multimodal context into reason-
ing to strengthen visual cues and cross-modal interactions.
In MCoT, visual information is typically derived from ex-
ternal tools such as additional search engines (Fan et al.,
2024; Komeili et al., 2021), multiple visual models (Ma
et al., 2025c; Qi et al., 2024), or image processing meth-
ods (Su et al., 2025b; Zheng et al., 2025). Recent progress
in reinforcement learning (Shao et al., 2024; Guo et al.,
2025; Chen et al., 2025) allows models to acquire tool-usage
skills in a more cost-efficient and flexible way (Su et al.,
2025b; Zheng et al., 2025; Su et al., 2025a). While MCoT
demonstrates superior reasoning capabilities compared to
text-centric CoT on multiple benchmarks, it also introduces
two major challenges.The first lies in the significantly
increased training and inference costs.Existing tool-
augmented reasoning models, such as OpenThinkIMG (Su
et al., 2025b) and DeepEyes (Zheng et al., 2025), often
rely on fixed tool invocation orchestration or inadequate
reward designs. Consequently, theyimplicitlyfocus on
learning how to invoke tools correctly and generate accu-
rate answers, while neglecting whether tool usage is truly
necessary. As illustrated in Figure 1(c) and Figure 1(d),
taking DeepEyes (Zheng et al., 2025) as an example, it
consistently encourages tool invocation regardless of task
difficulties. Even for simple queries, the model tends to
engage in unnecessary multi-turn reasoning, substantially
increasing computational overhead during both training and
inference. Hence, DeepEyes requires 44.9 training hours,
1
arXiv:2605.19852v1  [cs.CL]  19 May 2026

## Page 2

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
Which side of the car is the person sitting on?
Qwen2.5-VL
<think>The person is sitting 
on the front part of the car ...
<answer> A. Front (hood)
<think> To determine ... I will use the zoom_in tool to .... 
{"bbox_2d": [1000, 1750, 2030, 2850], "label": "the car"}
<answer>B. Driver’s side
 DeepEyes
<tool_off>
<think> ... The person is positioned in a way that suggests 
they are sitting on the hood ...
<answer>A. Front (hood)
What is the color of the SUV car?
Qwen2.5-VL
<think>The image shows ... it 
is not clearly visible to 
determine its color.
<answer> The correct answer 
cannot be determined from 
the given options.
<think> ... In the background, there is a car ... 
{"bbox_2d": [1413, 719, 1476, 752], "label": "SUV car"}
<think> ... car in the background is silver.
<answer>A. The color of the  SUV car is silver.
 DeepEyes
<tool_on>
<think>... have a closer look at the car in the image ...
{"bbox_2d": [1380, 695, 1480, 760], "label": "the SUV car"}
<think> ... it is clear that the SUV car is silver in color.
<answer>A. The color of the SUV car is silver.AutoTool
（a） （b）
（c）
AutoTool
（d）
Tool Assistance is Beneficial Tool Assistance is Unnecessary
Figure 1.(a, b) Representative queries that do or do not trigger the zoom-in tool, illustrating that tool usage is not always necessary, while
AutoTool adaptively invokes tools when beneficial. (c, d) Comparison of the proportion of tool-augmented reasoning trajectories during
training, as well as the training and inference time costs between our AutoTool and SOTA DeepEyes (Zheng et al., 2025).
20.3% more than adaptive tool invocation, indicating that
redundant tool usage severely slows down the reasoning
process.Furthermore, erroneous tool invocations may
interfere with reasoning.As shown in Figure 1(b), when
answering a question about the spatial relationship between
a person and a car, the model should rely on global un-
derstanding, where zoom-in tool invocation is unnecessary.
However, DeepEyes incorrectly invokes the tool to focus
solely on the car region, rather than the combined area of the
car and the person, introducing redundant visual informa-
tion that distracts the reasoning process and ultimately leads
to hallucinated responses. In such cases, the autoregressive
nature of LLMs makes frequent tool invocations particu-
larly problematic, as they amplify irrelevant visual cues and
cause error accumulation, further intensifying reasoning
distraction and hallucination.
In our opinion, when handling a multimodal query, an ideal
model should carefullydetermine whether tool assistance
is necessarybefore invocation. Taking the zoom-in op-
eration as an example, intuitively, if a question requires
close inspection or verification of fine-grained visual details,
the zoom-in tool becomes essential. As illustrated in Fig-
ure 1(a), where the task involves identifying a specific object
among multiple candidates, zooming into the target region
substantially improves the likelihood of a correct answer.
In contrast, as shown in Figure 1(b), when the question in-
volves global understanding, overall layout reasoning, or
when the target region is already sufficiently clear, invoking
the zoom-in tool yields negligible benefit and may even
introduce unnecessary distractions.
To address the issue of existing methods that overempha-
size tool usage, we introduceAutoTool, which empowers
the model to adaptively decide when to engage in “Think
with Images” reasoning, reconsidering the common belief
that “tools are always beneficial”. Byexplicitlycontrolling
tool usage through two special tokens, <tool on> and
<tool off>, AutoTool employs dual reasoning modes
that leverage tools for complex problems while recognizing
that simple queries can be solved without tool assistance.
This paradigm improves both training and inference effi-
ciency, as well as mitigating hallucinated responses. Instead
of relying on carefully curated SFT data for cold-start train-
ing, we adopt an end-to-end reinforcement learning frame-
work that encourages the model to fully explore the two
reasoning modes in a simple yet effective manner.
Within this explicit dual-mode paradigm, we design distinct
reward functions to evaluate reasoning trajectories under dif-
ferent reasoning modes, which we refer to asMode-Specific
Policy Optimization (MSPO). For the <tool on> mode,
the model is trained to accurately utilize the tool while pro-
viding correct answers. Unlike prior methods (Su et al.,
2025b; Zheng et al., 2025) that primarily emphasize tool
invocation, we penalize instances where the model invokes
tools but produces incorrect answers, reducing unneces-
sary or ineffective tool operations. For the <tool off>
mode, the model relies entirely on its internal reasoning
to generate accurate answers. However, learning to master
dual reasoning modes is nontrivial. Due to the inherent rea-
2

## Page 3

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
soning bias of the foundation model, the policy model tends
to prefer the <tool off> mode, which often yields higher
rewards more easily, leaving the <tool on> mode un-
derexplored. To mitigate this imbalance, we propose an
Adaptive Mode Balancing (AMB)strategy that dynami-
cally adjusts the reward coefficients to control the frequency
of the two modes, ensuring sufficient exploration for both.
The constraint is relaxed in the later stage of training, allow-
ing the model to freely determine its preferred mode. Our
contributions can be summarized as follows:
• We analyze the pros and cons of tool-assisted reason-
ing for MLLMs. While tool invocation can enhance
reasoning capabilities, blindly encouraging tool usage
increases both training and inference costs and may
introduce distracting or redundant information.
• We design Mode-Specific Policy Optimization
(MSPO), with distinct optimization objectives to dif-
ferent reasoning modes, enabling the model to learn
adaptive reasoning with or without tools.
• We propose Adaptive Mode Balancing (AMB), which
adaptively and dynamically adjusts the frequency of
the two modes to ensure sufficient exploration of dual
reasoning modes throughout training.
Extensive experiments on multiple multimodal benchmarks
demonstrate that AutoTool achieves superior reasoning ca-
pability and high efficiency.
2. Related Work
2.1. Multimodal Large Language Models
The emergence of multimodal large language models
(MLLMs) (Liu et al., 2023; Team et al., 2023; Hurst et al.,
2024; Bai et al., 2025; Fa et al., 2026; Li et al., 2026)
marks a major milestone in artificial intelligence and has
substantially promoted the development of diverse appli-
cation domains (Ma et al., 2024; 2025a;b; Duan et al.,
2025; Yang et al., 2025; Wang et al., 2025d). Early works
such as LLaV A (Liu et al., 2023; 2024), BLIP (Li et al.,
2022; 2023a), and Qwen-VL (Bai et al., 2023; Wang et al.,
2024b; Bai et al., 2025) adopt modular architectures that
pair pretrained visual encoders (e.g., CLIP-ViT (Cherti
et al., 2023; Radford et al., 2021), InternViT (Chen et al.,
2024)) with LLMs, laying the foundation for MLLM devel-
opment. These models typically involve large-scale multi-
modal alignment training followed by instruction tuning for
task adaptation. Subsequent studies like Flamingo (Alayrac
et al., 2022) and Cambrian-1 (Tong et al., 2024) integrate
multiple encoders for richer visual representations, while
EVE (Diao et al., 2024), MonoInternVL (Luo et al., 2025),
and SAIL (Lei et al., 2025) pursue end-to-end architectures
that process raw image patches and text tokens within a
unified Transformer. Recently, reinforcement learning has
further advanced chain-of-thought (CoT) reasoning (Shao
et al., 2024; Guo et al., 2025; Chen et al., 2025), yet most
approaches remain text-centric (Fan et al., 2025; Yao et al.,
2025), limiting the model’s understanding of visual content.
To address this, we propose adaptive tool-assisted zoom-in
reasoning for complex problems, enabling deeper visual
exploitation and more interpretable answers.
2.2. Tool-Augmented Reasoning in MLLMs
The multimodal information processing capability of
MLLMs enables human-like “Thinking with Images”
through multimodal chain of thought (MCoT) reason-
ing (Zhang et al., 2025; Wang et al., 2025a; Su et al., 2025c;
Zheng et al., 2025; OpenAI, 2025). Recent works such as
Visual Sketchpad (Hu et al., 2024), OpenThinkIMG (Su
et al., 2025b), and Thyme (Zhang et al., 2025) equip mod-
els with planning and orchestration abilities, leveraging
diverse external tools, such as semantic segmentation (Kir-
illov et al., 2023; Ravi et al., 2024), OCR, and depth esti-
mation (Yang et al., 2024b;c), to inject rich visual cues into
the reasoning process. Beyond explicit tool usage, meth-
ods like BAGEL (Deng et al., 2025), Visual Planning (Xu
et al., 2025), and GoT (Fang et al., 2025) unify generation
and reasoning, generating new explicit or implicit visual
states from contextual semantics to facilitate subsequent
reasoning steps. Current approaches for acquiring tool-use
capability typically fall into three categories: prompt-based
methods that rely on in-context learning (Hu et al., 2024; Li
et al., 2025), supervised fine-tuning that teaches procedural
competence from examples (Wu & Xie, 2024; Ma et al.,
2025c), and reinforcement learning that optimizes tool-use
policies through feedback (Su et al., 2025b; Lai et al., 2025).
However, existing studies mainly emphasize how to teach
models to use tools correctly, neglecting the critical question
of whether tool invocation is necessary. Thus, our method
adaptively decides when and how to invoke tools, achieving
a balance between reasoning efficiency and reliability.
2.3. Reinforcement Learning in Large Models
Reinforcement learning has demonstrated remarkable po-
tential in enhancing the reasoning capabilities of large mod-
els (Shao et al., 2024; Guo et al., 2025; Chen et al., 2025).
DeepSeek-R1 (Guo et al., 2025) shows that even simple rule-
based RL strategies can effectively induce strong reasoning
behaviors, inspiring a surge of research into RL-based rea-
soning enhancement. Building on this trend, recent works
such as DeepEyes (Zheng et al., 2025), TreeVGR (Wang
et al., 2025a), and Thyme (Zhang et al., 2025) employ Group
Relative Policy Optimization (GRPO) (Shao et al., 2024) to
guide models in performing accurate tool-assisted reason-
ing. Distinct from these approaches, our method leverages
3

## Page 4

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
What is the color of 
the tail? You are a 
helpful assistant ... 
Policy  Model
Tool assistance is necessary?
<tool_off>
<tool_on>
other tokens
First token distributions <tool_on> <think> The picture shows a 
cat ... zoom in on the tail area 
<tool_call> ... [381, 208, 442, 230] ... 
<answer> The color of the tail is black. 
Outputon1
Outputoffj+1
Outputonj
......
update
input rollout
Accuracy Reward:
Prediction
- A
- B
- The bus is Blue
- The tail is 
black in color.
GT
- A
- C. Left
- Black
- The color of the 
tail is black
Format Reward:
- <tool_on> <think> ... <tool_call> ... <answer> ...
- <tool_off> <think> ... <answer> ... <answer> ...
Rule-based
Judge Model
Tool Reward:
- <tool_on>: tool usage & correct answer
- <tool_off>: without tool & correct answer
MSPO
Reward 
Calculation
Normalization
Rewardon1
Rewardonj
Rewardoffj+1
RewardoffG
......
Advon1
Advonj
Advoffj+1
AdvoffG
......
Rule-based
Judge Model
AMB
Sufficient 
exploration
Free 
exploration
λtoolon 
λtooloff 
Fon
λtoolon 
λtooloff 
Training stage
0 step 80 step
<tool_off> <think> The picture shows a 
cat ... no need for a close inspection ...
<answer> The color of the tail is black. 
OutputoffG
Figure 2.Illustration of the AutoTool training framework. Given a multimodal problem, the policy model first decides whether the
subsequent reasoning process requires tool invocation. For each batch of generated reasoning trajectories, different reward functions
are applied to evaluate the trajectories under distinct reasoning modes via the Mode-Specific Policy Optimization (MSPO), and the tool
invocation reward coefficient is estimated through the Adaptive Mode Balancing (AMB) strategy. The model is optimized via the GRPO.
RL not only to reinforce proper tool invocation, but also to
explore and coordinate multiple reasoning modes, fostering
more adaptive and context-aware multimodal reasoning.
3. Method
3.1. Problem Formulation and Preliminary
Given a multimodal query X= (Q, V), where Q denotes
the textual query and V represents the visual inputs, we first
revisit the traditionaltext-centric reasoning paradigm.
In this paradigm, the policy model πθ performs reasoning
purely in the textual space by generating a sequence of inter-
mediate reasoning steps R={T i}I
i=1, where Ti represents
the internal reasoning text at the i-th step. At each step, the
reasoning state Ri ∼π θ(· |X, R1, . . . , Ri−1) is sampled
from πθ conditioned on the initial query and all previous
steps. Each new reasoning step is appended to the context
and fed back into the policy model for subsequent reasoning.
This iterative process continues until the model outputs the
final answer Y , or until a predefined limit on context length
is reached. Accordingly, the complete textual reasoning
trajectoryγ t can be formulated as:
γt ={X,(T 1), . . . ,(TI, Y)}.(1)
Different from the text-only paradigm,multimodal reason-
ing paradigmaugments each step with tool interactions.
Specifically, the reasoning state at thei-th step is represented
as a triplet Ri = (Ti, Ai, Oi), where Ti denotes the internal
reasoning text, Ai denotes the tool action along with its
parameters, and Oi denotes the observation returned by exe-
cuting the tool action. The complete multimodal reasoning
trajectory γm alternates between reasoning and interaction,
and terminates with a final textual answer Y . Accordingly,
the resulting multimodal reasoning trajectory is defined as:
γm ={X,(T i, Ai, Oi)I−1
i=1 ,(T I, Y)}.(2)
3.2. Overview
Compared with the text-centric reasoning paradigm, mul-
timodal reasoning extends visual information processing
from a one-time encoding to an iterative editing process
through explicit tool invocation. This paradigm allows the
model to step out of the textual bias and effectively leverage
multimodal cues for reasoning. However, indiscriminately
encouraging the model to invoke tools leads to two major
issues: (1) the reasoning cost increases significantly during
both training and inference, and (2) unnecessary or incorrect
tool usage may introduce noisy or misleading information,
thereby deteriorating the reasoning reliability.
We introduceAutoToolto break the conventional assump-
tion that “tools are always beneficial” in multimodal rea-
soning. It adaptively decides whether tool invocation is
necessary for each task and selects the more suitable rea-
soning mode, achieving a better balance between reasoning
efficiency and answer reliability. As illustrated in Figure 2,
given a user-provided multimodal query, AutoTool first de-
termines whether the current question requires the assistance
of the tool. If tool usage is deemed necessary, the policy
model invokes a zoom-in function to locate the region of
interest that is most relevant to the query, and appends the re-
sulting cropped visual observation to the reasoning context
4

## Page 5

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
for subsequent inference. Otherwise, the policy model per-
forms purely textual reasoning to directly produce the final
answer in a more efficient manner. The policy for whether
and how to invoke tools is learned through reinforcement
learning, as detailed in the following sections.
3.3. Explicit Dual Reasoning Modes
We define two special control tokens, <tool on> and
<tool off>, explicitly indicating whether the model em-
ploys tools in subsequent reasoning. <tool on> trig-
gers tool-augmented reasoning with <tool call> and
<tool response> structures, while <tool off> cor-
responds to pure textual reasoning without tool usage. We
carefully design the prompts, as detailed in the supplemen-
tary material, to explicitly define the applicable scenarios
and output formats for both reasoning modes. The policy
model is trained via Group Relative Policy Optimization
(GRPO) (Shao et al., 2024), a reinforcement learning al-
gorithm that enables effective and efficient exploration of
different reasoning strategies without relying on hard-to-
obtain SFT data.
Specifically, given a multimodal query X= (Q, V) ,
we sample a group of G candidate reasoning trajectories
{oi}G
i=1 from the policy model. For each trajectory oi from
the old policy πθold, we compute a scalar rewardri based on
both the final answer and the intermediate reasoning process,
as detailed in Section 3.4. The rewards {ri}G
i=1 are then
normalized to obtain the advantages { ˆAi}G
i=1. Formally, the
optimization objective of GRPO is defined as:
JGRPO(θ) =EX,{oi}G
i=1∼πθold
"
1
G
GX
i=1
min
 
πθ(oi|X)
πθold (oi|X)
ˆAi,
clip
 πθ(oi|X)
πθold (oi|X) ,1−ϵ,1 +ϵ

ˆAi
!#
,
(3)
ˆAi = ri −mean({r 1, r2, . . . , rG})
std({r1, r2, . . . , rG}) ,(4)
where ϵ is the clipping hyperparameter and we do not in-
clude a KL regularization term.
Nevertheless, due to the intrinsic reasoning bias inherited
from the foundation model, the policy model exhibits a ten-
dency to over-prefer the <tool off> mode, which yields
higher rewards with less effort and consequently hinders ad-
equate exploration of the <tool on> mode. To encourage
sufficient exploration across both reasoning modes, we pro-
pose theAdaptive Mode Balancing (AMB)strategy that
dynamically regulates their respective reward coefficients,
ensuring that neither mode is neglected during training.
For a batch of N samples {Xi}N
i=1, we obtain N×G
rollouts from different reasoning modes. We record the
occurrence counts of the two modes as Non and Noff, re-
spectively, and compute the tool invocation frequency as
Fon = Non
Non+Noff
. Based on the initial tool invocation reward
coefficientλ base
tool , we dynamically adjust it as
λmode
tool =
(
λbase
tool + 0.5−Fon,if mode=on,
λbase
tool −0.5 +Fon,if mode=off,
(5)
where λmode
tool denotes the adaptive tool invocation reward co-
efficient, determined by the reasoning mode of the trajectory.
When the tool invocation frequency becomes too high, λon
tool
decreases while λoff
tool increases, encouraging the model to ex-
plore the <tool off> mode more actively, and vice versa.
Through adaptive adjustment, the model is encouraged to
sufficiently explore both modes during training.
As training progresses, the model becomes proficient in both
reasoning modes. At the final stage of training (e.g., the
last 20 steps), we remove this adaptive constraint and set
λon
tool =λ off
tool =λ base
tool , allowing the policy to autonomously
determine which reasoning mode to employ for each query
based on its internal confidence and problem characteristics.
This transition enables the model to shift from guided explo-
ration to self-directed reasoning, achieving a more natural
integration of both reasoning paradigms.
3.4. Mode-Specific Policy Optimization
To encourage the model to explore different reasoning
modes through reinforcement learning while ensuring that it
correctly follows the required output formats and performs
valid tool invocations for accurate question answering, we
design the following reward.
The overall reward consists of three components: accuracy
reward Racc, format compliance reward Rformat, and mode-
specific tool invocation rewardR tool,
R=R acc +R format +λ mode
tool Rtool.(6)
Accuracy reward Racc:We evaluate whether the predicted
answer is semantically equivalent to the ground truth using
a combination of rule-based metrics and an online reward
model (e.g., Qwen2.5-72B-Instruct).
Format reward Rformat:This ensures that the reasoning
process and final answer adhere to the prescribed output
format,i.e., enclosed within <think></think> and
<answer></answer>tags, respectively.
Mode-specific tool reward Rtool:For the <tool on>
mode, the model receives Rtool = 1when it correctly per-
forms the zoom-in tool invocations and produces a correct
answer. If the tool is invoked but the answer is incorrect,
a penalty Rtool =−0.5 is applied to account for the extra
5

## Page 6

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
cost of tool usage. In all other cases, Rtool = 0. For the
<tool off> mode, the model is rewarded Rtool = 1only
if it does not invoke the zoom-in tool and provides a correct
answer; otherwise,R tool = 0.
3.5. Inference
During inference, we employ the same prompting scheme
as used in training. The model can autonomously select the
reasoning mode based on the characteristics of the query.
Alternatively, the reasoning mode can be manually speci-
fied, either by explicitly instructing the model in prompt to
perform or skip tool invocation, or by appending the special
token <tool on> or <tool off> to the input sequence.
4. Experiments
4.1. Benchmarks and Metrics
We evaluate our model across three categories of bench-
marks to comprehensively assess its performance and com-
pare it with existing methods.
Perception benchmarks.These include the V* (Wu & Xie,
2024) and HRbench (Wang et al., 2025b) datasets, which
consist of high-resolution images (ranging from 2K to 8K).
The questions in these datasets focus mainly on single-object
attributes, object counting, or relative spatial relationships.
The evaluation metric is the question answering accuracy.
Grounding benchmarks.This category includes Ref-
COCO (Caesar et al., 2018), RefCOCO+ (Caesar et al.,
2018), RefCOCOg (Kazemzadeh et al., 2014), and Reason-
Seg (Lai et al., 2024). Both the COCO series and ReasonSeg
require the model to output the bounding-box of the referred
object within an image. We evaluate grounding accuracy by
computing the Intersection-over-Union (IoU) between the
predicted and ground-truth regions, with a threshold of 0.5
to determine whether the prediction is considered correct.
Hallucination benchmark.POPE (Li et al., 2023b)
serves as a hallucination detection benchmark that eval-
uates whether the target object truly exists in the image, and
its metric is the prediction accuracy.
Reasoning benchmarks.These include MathVista (Lu
et al., 2023), MathVerse (Zhang et al., 2024), MathVi-
sion (Wang et al., 2024a), WeMath (Qiao et al., 2024),
DynaMath (Zou et al., 2024), and LogicVista (Xiao et al.,
2024). The tasks cover a wide range of reasoning types,
including mathematical reasoning, geometric pattern recog-
nition, logical and physical reasoning, chart interpretation,
and commonsense reasoning in real-world scenarios. Some
questions require the model to infer implicit information
from the given text or image context. The performance
metric is the accuracy of the answer.
4.2. Implementation Details
Following DeepEyes (Zheng et al., 2025), the training data
include fine-grained samples from the V* (Wu & Xie, 2024)
dataset, chart data from ArxivQA (Li et al., 2024b), and
reasoning data from ThinkLite-VL (Wang et al., 2025c).
The inclusion of reasoning data aims to enhance the general
reasoning robustness of the model and mitigate overfitting to
modality-specific patterns, where purely textual reasoning
and answer generation are performed without relying on
tool-based interactions. We use Qwen2.5-VL-7B (Bai et al.,
2025) as the base policy model and train it with GRPO (Shao
et al., 2024; Sheng et al., 2024) for 80 iterations on eight
H200 GPUs. An additional two H200 GPUs are used to de-
ploy the reward model, Qwen2.5-72B-Instruct (Yang et al.,
2024a), via the vLLM (Kwon et al., 2023) inference en-
gine. Each training batch contains 256 samples, which are
divided into 4 PPO mini-batches. For each query, the model
generates 16 rollouts. The initial tool invocation reward
coefficient λbase
tool is set to 1.2, and the clipping parameter ϵ is
set to 0.2. We adopt the AdamW optimizer with an initial
learning rate of 1×10 −6. The maximum response length
of the policy model is set to 20,480 tokens.
4.3. Main Results
Perception benchmarks.Table 1 presents the comparison
results of our AutoTool with existing models on perception
benchmarks. All models first generate internal reasoning be-
fore producing a final answer. Visual grounding reasoning
models rely on their respective system prompts to trigger
tool usage, whereas AutoTool adaptively decides whether to
invoke tools using the same system prompt as during train-
ing. Across the majority of splits in both datasets, AutoTool
consistently achieves state-of-the-art performance, signifi-
cantly surpassing both proprietary and open-source general
MLLMs. Remarkably, AutoTool still maintains a clear ad-
vantage even over much larger models such as Qwen2.5-VL-
32B and InternVL3-38B. Compared with models that also
rely on visual grounding–based reasoning, our approach
breaks away from a single reasoning paradigm, effectively
leveraging the advantages of localized reasoning after ac-
curate grounding, while avoiding redundant or misleading
information introduced by unnecessary or incorrect local-
ization. Compared with the base model Qwen2.5-VL-7B,
our training paradigm leads to substantial improvements on
perception tasks, achieving 21% and 11% accuracy gains
on HRbench and V* datasets, respectively.
Grounding benchmarks.As shown in Table 2, AutoTool
consistently outperforms models of comparable size across
all splits of the four datasets. This improvement stems from
our training design: in the <tool on> mode, trajectories
that correctly invoke tools and produce accurate answers are
rewarded, which encourages the model to precisely localize
6

## Page 7

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
Table 1.Performance comparison of different models on perception benchmarks. For models with similar sizes, the best performance for
each metric is marked asbold, and the second-best is underlined .
Model Size HRbench-4K HRbench-8K V*
FSP FCP Overall FSP FCP Overall Attribute Spatial Overall
Proprietary General MLLMs
GPT-4o[2023] (Achiam et al., 2023) - 66.8 63.3 65.0 60.8 58.5 59.6 72.2 60.5 67.5
o3 [2025] (OpenAI, 2025) - - - - - - - - - 95.7
Open-Source General MLLMs
Qwen2.5-VL-7B[2025] (Bai et al., 2025) 7B 81.8 57.5 69.6 74.0 52.0 63.0 67.0 72.4 69.1
Qwen2.5-VL-32B[2025] (Bai et al., 2025) 32B 87.5 65.0 76.3 85.8 61.8 73.8 78.3 80.3 79.1
InternVL3-8B[2025] (Zhu et al., 2025) 8B 75.863.869.8 59.0 58.8 58.9 75.7 81.6 78.0
InternVL3-38B[2025] (Zhu et al., 2025) 38B 81.0 67.0 74.0 64.8 60.3 62.5 78.3 77.6 78.0
LLaV A-OneVision[2024] (Li et al., 2024a) 7B 72.8 53.8 63.3 60.5 50.3 55.4 74.8 68.4 72.3
Visual Grounded Reasoning Models
SEAL[2024] (Wu & Xie, 2024) 7B - - - - - - 74.8 76.3 75.4
DyFo[2025] (Li et al., 2025) 7B - - - - - - 80.0 82.9 81.2
ZoomEye[2025] (Shen et al., 2024) 7B 84.3 55.0 69.6 88.550.0 69.3 93.985.5 90.6
Pixel-Reasoner[2025] (Su et al., 2025a) 7B 86.0 60.3 72.9 80.0 54.4 66.9 83.5 76.3 80.6
DeepEyes[2025] (Zheng et al., 2025) 7B 92.0 57.8 74.9 85.5 57.5 71.5 90.4 82.9 87.4
Ours
AutoTool 7B 92.5 61.3 76.9 88.0 60.0 74.0 91.3 88.2 90.1
∆v.s.Qwen2.5-VL-7B - ↑10.7 ↑3.8 ↑7.3 ↑14.0 ↑8.0 ↑11.0 ↑24.3 ↑15.8 ↑21.0
Table 2.Performance comparison of different models on grounding benchmarks. The best performance for each metric is marked asbold.
Model Size refCOCO refCOCOg refCOCO+ ReasonSeg
test testA testB val test val testA testB val test val
Qwen2.5-VL-7B (Bai et al., 2025) 7B 84.7 86.6 78.1 83.4 77.0 76.6 82.1 68.5 76.3 51.1 59.5
DeepEyes (Zheng et al., 2025) 7B 86.0 90.5 79.6 86.1 80.3 80.4 87.2 67.8 79.2 50.6 61.5
AutoTool 7B 88.5 92.5 83.1 88.6 82.8 82.7 89.7 72.6 81.6 53.3 63.0
∆v.s.Qwen2.5-VL-7B - ↑3.8 ↑5.9 ↑5.0 ↑5.2 ↑5.8 ↑6.1 ↑7.6 ↑4.1 ↑5.3 ↑2.2 ↑3.5
the region of interest. Conversely, trajectories that invoke
tools but yield incorrect answers are penalized, reducing the
likelihood of erroneous localizations. In contrast, DeepEyes
may still rewards trajectories where tool-based localization
is incorrect but the final answer happens to be correct. Our
introduction of the <tool off> mode mitigates this issue
by encouraging reasoning without relying on potentially
misleading tool-based cues. All models are evaluated using
the same prompt, and the detailed prompt specifications are
provided in the supplementary material.
Hallucination and reasoning benchmark.As illustrated
in Table 3, our model demonstrates improved performance
in reducing hallucinations. The adaptive tool invocation
capability is also effective for hallucination tasks: when
determining whether a target object is present in the im-
age, AutoTool carefully inspects similar objects or poten-
tial regions in the <tool on> mode. Consistent with the
perception benchmarks, all models first generate internal
reasoning before providing a final answer, with DeepEyes
and AutoTool leveraging tool invocation. Our model main-
tains robust reasoning capabilities and achieves excellent
performance across six benchmarks encompassing a diverse
range of reasoning tasks. All models are evaluated under
the same prompt setting, where each model first conducts
internal reasoning before producing the final answer.
We further showcase visual examples on the test bench-
marks, as detailed in the supplementary material.
4.4. Ablation and Analysis
The influence of each module.As shown in Table 4,Tool
ondenotes the reasoning process assisted by the zoom-in
tool, whileTool offrepresents pure text-based reasoning.
MSPOpenalty refers to the negative reward Rtool =−0.5
applied when the model invokes a tool but produces an in-
correct answer. AMBfree indicates that the AMB constraint
is removed in the later training stage, allowing the model to
freely explore dual reasoning modes.
In the #1 setting, Qwen2.5-VL-7B is trained on the training
dataset via pure-text GRPO, which substantially improves
performance over the base model. In #2, DeepEyes always
employs the zoom-in tool for every query, leading to further
improvement compared with #1 setting. In #3, a carefully
designed prompt with RL training is adopted under mode-
7

## Page 8

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
Table 3.Performance comparison on hallucination and reasoning benchmarks. The best performance for each metric is marked asbold.
Model Size POPE MathVistaMathVerse MathVision WeMathDynaMathLogicVistaAdversarial Popular Random Overall test testmini
Qwen2.5-VL-7B (Bai et al., 2025) 7B85.9 87.0 88.9 87.2 70.6 43.6 14.8 16.1 30.8 57.2 45.5
InternVL3-8B (Zhu et al., 2025) 8B 87.288.1 90.8 88.7 68.3 47.8 17.416.8 37.9 57.8 46.0
LLaV A-OneVision (Li et al., 2024a) 7B84.7 87.6 90.4 87.6 58.4 34.5 9.6 12.5 37.5 35.4 28.3
DeepEyes (Zheng et al., 2025) 7B 81.4 85.0 91.7 86.0 71.6 45.2 15.1 19.4 32.6 57.7 45.3
AutoTool 7B 86.1 88.4 92.3 88.9 72.8 45.9 15.0 19.4 34.0 58.0 46.7
∆v.s.Qwen2.5-VL-7B - ↑0.2 ↑1.4 ↑3.4 ↑1.7 ↑2.2 ↑2.3 ↑0.2 ↑3.3 ↑3.2 ↑0.8 ↑1.2
Table 4.Ablation experiments of each module. The best performance for each metric is marked asbold.
ID Tool on Tool off MSPO penalty AMBfree
HRbench-4K HRbench-8K V*
FSP FCP Overall FSP FCP Overall Attribute Spatial Overall
1 ✓ 88.0 59.3 73.6 81.8 58.8 70.2 87.8 81.6 85.3
2 ✓ 92.0 57.8 74.9 85.5 57.5 71.5 90.4 82.9 87.4
3 ✓ ✓ 91.8 58.8 75.3 86.3 58.5 72.4 88.7 88.2 88.5
4 ✓ ✓ ✓ 93.358.3 75.8 87.3 59.3 73.3 89.6 88.2 89.0
5 ✓ ✓ ✓ 92.8 60.8 76.8 85.061.573.2 89.689.589.5
6 ✓ ✓ ✓ ✓ 92.5 61.3 76.9 88.0 60.0 74.0 91.3 88.2 90.1
Table 5.Effect of removing the mode-balancing constraint at
different training steps. The best performance is marked asbold.
Step HRbench-4K HRbench-8K V*FSP FCP Overall FSP FCP Overall Attribute Spatial Overall
0 92.5 55.8 74.1 84.5 57.3 70.9 85.3 84.2 84.350 92.8 60.8 76.8 85.061.573.2 90.4 86.8 89.060 92.561.3 76.9 88.0 60.074.0 91.388.290.170 92.5 59.5 76.0 89.058.0 73.5 89.689.589.580 93.358.3 75.8 87.3 59.3 73.3 89.6 88.2 89.0
Table 6.Effect of the initial tool invocation reward coefficientλbase
tool .
The best performance is marked asbold.
λbase
tool 0.0 0.5 1.0 1.2 1.4 3.0 5.0
HRbench-4K 72.4 75.5 76.0 76.977.375.0 71.4
HRbench-8K 69.8 72.8 73.974.073.5 72.1 68.4
V* 84.3 88.5 89.590.1 90.188.0 83.8
ratio constraints, guiding the model to fully explore both
modes. Compared with #2 setting, this flexible reasoning
mode mitigates the negative impact of incorrect tool usage.
In the #4 setting, a penalty is introduced when the model
invokes a tool but produces an incorrect answer, enforcing
more precise grounding behavior. In #5, the mode-balancing
constraint is removed in the later training stage encouraging
free exploration and yielding further performance gains.
Finally, the #6 setting integrates all these advantageous
components and achieves the best overall performance.
Effect of mode-balancing removal step.Table 5 reports
the impact of removing the mode-balancing constraint at
different training steps. We observe that disabling the AMB
constraint from the beginning (i.e., step 0) leads to a pre-
mature dominance of the <tool off> mode, resulting in
inferior performance on fine-grained perception tasks. As
training progresses, the model benefits from maintaining the
constraint for a sufficient period, which promotes balanced
exploration between the two reasoning modes. The best
Table 7.Sensitivity analysis of the efficiency penalty term.
Penalty HRbench-4K HRbench-8K V*FSP FCP OverallFSP FCP OverallAttribute Spatial Overall
0 92.8 60.8 76.8 85.0 61.5 73.2 89.6 89.5 89.5-0.2 92.3 61.0 76.6 87.5 59.5 73.5 91.3 86.8 89.5-0.5 92.5 61.3 76.9 88.0 60.0 74.0 91.3 88.2 90.1-0.8 92.5 61.5 77.0 87.8 59.5 73.6 90.4 89.5 90.1
Table 8.Training and inference efficiency comparison between
AutoTool and DeepEyes.
Phase Dataset Split DeepEyes AutoTool Speedup (%)
Training - - 44.9 h 35.8 h 20.3
Inference
V* Direct 2.23 min 1.68 min 24.7
Relative 1.50 min 1.07 min 28.7
HRbench 4K 48.35 min 31.95 min 33.9
8K 53.45 min 33.08 min 38.1
POPE
Adversarial 14.27 min 8.78 min 38.5
Popular 12.13 min 7.73 min 36.3
Random 13.07 min 7.20 min 44.9
overall results are achieved for HRBench-4K, HRBench-
8K, and V * benchmarks when the constraint is removed
at around 60 iterations. Further delaying the removal (e.g.,
step 70) yields a slight performance decline, likely because
the model becomes overly constrained and less adaptive to
problem-specific reasoning strategies in later stages.
Effect of the coefficient λbase
tool .We further analyze the sen-
sitivity of the initial tool invocation reward coefficient λbase
tool ,
including both moderate and extreme settings. The results
are shown in Table 6. The model achieves stable perfor-
mance around the default value (λbase
tool = 1.2) and remains
robust within a moderate range (0.5∼3.0 ), suggesting that
AMB is not sensitive to precise hyperparameter tuning.
However, extreme values lead to clear performance degrada-
tion due to reward imbalance. When λbase
tool is too small, the
contribution of the tool reward becomes negligible, weak-
ening supervision on tool-usage behavior and causing re-
8

## Page 9

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
HRbench V* POPE 31.1%
 33.4%
 18.9% 16.6%
Tool off
Tool on HRbench-8K
534HRbench-4K
497
HRbench-4K
303
HRbench-8K
266
52.9%
27.2%
7.3%
12.6%
Tool on
Spatial
52
Attribute
101
Attribute
14
Spatial
24
18.0%
17.2%
15.3%
16.2%
Tool on Random
1409
Adversarial
1623
Popular
1456
Random
1591Tool off
15.7%
17.7%
Tool off
Adversarial
1377
Popular
1544
Figure 3.The outer ring shows the proportion of the dual reason-
ing modes on three datasets, while the inner ring presents their
distribution across different splits within each dataset.
ward hacking. For example, when λbase
tool = 0.0, the model
frequently selects the <tool on> mode while perform-
ing pure text reasoning without valid tool calls, exploiting
Ron
tool = 0while benefiting from a larger λoff
tool. In contrast,
excessively large values reduce the relative influence of the
task reward and bias the policy toward the foundation model
preference, resulting in collapse to the <tool off> mode.
We additionally observe degraded adherence to the required
reasoning format under such settings. Overall, the default
coefficient provides a good balance between adaptive tool
usage and reasoning quality.
Sensitivity to the efficiency penalty.The efficiency penalty
in the mode-specific reward is introduced to discourage
unnecessary tool usage, particularly when tool invocation
leads to incorrect answers. Specifically, for the<tool on>
mode, trajectories with incorrect answers after tool invoca-
tion receive a negative reward. To evaluate the sensitivity
of this design, we vary the efficiency penalty term within
{0,−0.2,−0.5,−0.8} while keeping all other hyperparam-
eters unchanged. The results are shown in Table 7. Em-
pirically, the performance varies only marginally across
different penalty values, indicating that the proposed re-
ward design maintains a robust operating range and does
not require careful dataset-specific tuning.
Time efficiency and tool mode analysis.As shown in Ta-
ble 8, we report the training and inference time costs of
existing visual grounding–based reasoning models such as
DeepEyes and our AutoTool. Under the same data and
number of training iterations, our method reduces the total
training time by approximately 9 hours. The inference time
across all three datasets is also significantly shortened, with
a 44.9% reduction observed on the POPE dataset.
In addition, we analyze the occurrence frequency of the dual
reasoning modes across different benchmarks. As illustrated
in Figure 3, the proportion of these two modes is not fixed
as in the training stage but rather dynamically varies depend-
ing on the characteristics of the dataset. For high-resolution
datasets such as HRbench and V*, where target objects of-
ten occupy a small region of the image, the <tool on>
mode appears more frequently. In contrast, POPE contains
relatively smaller images with larger target objects, leading
to a notably higher proportion of <tool off> mode dur-
ing inference. The ratio of the dual reasoning modes during
training is illustrated in Figure 1(c). In the early and middle
stages of training, we adaptively control the reward factor to
encourage sufficient exploration of both reasoning modes,
resulting in a roughly balanced distribution of about 50% for
each. In the later stage, we remove this constraint to allow
the model to freely choose its preferred reasoning strategy,
where a slight increase in the proportion of the<tool on>
mode can be observed.
5. Conclusion
In this work, we reveal that tool-augmented reasoning is not
always beneficial for MLLMs. To address this limitation,
we propose AutoTool, a model that dynamically determines
whether to invoke zoom-in tools based on the characteristics
of each query. This design significantly improves both train-
ing and inference efficiency while mitigating the adverse
effects of unnecessary or incorrect tool usage. Based on the
reinforcement learning framework, our approach optimizes
dual reasoning modes with carefully designed reward func-
tions and guides the model to fully explore both. Extensive
experiments on various benchmarks demonstrate that Auto-
Tool achieves superior reasoning capability and efficiency
compared to existing models.
Acknowledgements
This work was supported by NSFC Project (62536005,
62192783, 62506162), Jiangsu Science and Technology
Project (BG2024031, BK20251241), Fundamental and In-
terdisciplinary Disciplines Breakthrough Plan of the Min-
istry of Education of China (No. JYB2025XDXM118),
“111 Center” (No. B26023), and Fundamental Research
Funds for the Central Universities (KG202508).
Impact Statement
This work studies adaptive tool invocation for multimodal
large language models (MLLMs). By enabling models to
selectively determine whether external tool assistance is
necessary, our method improves reasoning efficiency while
reducing redundant computation and unnecessary tool inter-
actions. Our approach also reduces hallucinations caused
by inappropriate tool usage, potentially improving the re-
liability of multimodal reasoning systems. However, the
proposed method does not eliminate risks associated with
MLLMs, such as incorrect reasoning or failures in com-
plex scenarios. Careful evaluation and appropriate human
oversight remain important for real-world deployment.
References
Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I.,
Aleman, F. L., Almeida, D., Altenschmidt, J., Altman, S.,
9

## Page 10

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
Anadkat, S., et al. Gpt-4 technical report.arXiv preprint
arXiv:2303.08774, 2023.
Alayrac, J.-B., Donahue, J., Luc, P., Miech, A., Barr, I.,
Hasson, Y ., Lenc, K., Mensch, A., Millican, K., Reynolds,
M., et al. Flamingo: a visual language model for few-shot
learning.Advances in Neural Information Processing
Systems, 35:23716–23736, 2022.
Bai, J., Bai, S., Yang, S., Wang, S., Tan, S., Wang, P., Lin,
J., Zhou, C., and Zhou, J. Qwen-vl: A versatile vision-
language model for understanding, localization, text read-
ing, and beyond.arXiv preprint arXiv:2308.12966, 2023.
Bai, S., Chen, K., Liu, X., Wang, J., Ge, W., Song, S., Dang,
K., Wang, P., Wang, S., Tang, J., et al. Qwen2. 5-vl
technical report.arXiv preprint arXiv:2502.13923, 2025.
Caesar, H., Uijlings, J., and Ferrari, V . Coco-stuff: Thing
and stuff classes in context. InProceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pp. 1209–1218, 2018.
Chen, H., Tu, H., Wang, F., Liu, H., Tang, X., Du, X., Zhou,
Y ., and Xie, C. Sft or rl? an early investigation into
training r1-like reasoning large vision-language models.
arXiv preprint arXiv:2504.11468, 2025.
Chen, Z., Wu, J., Wang, W., Su, W., Chen, G., Xing, S.,
Zhong, M., Zhang, Q., Zhu, X., Lu, L., et al. Internvl:
Scaling up vision foundation models and aligning for
generic visual-linguistic tasks. InProceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pp. 24185–24198, 2024.
Cherti, M., Beaumont, R., Wightman, R., Wortsman,
M., Ilharco, G., Gordon, C., Schuhmann, C., Schmidt,
L., and Jitsev, J. Reproducible scaling laws for con-
trastive language-image learning. InProceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pp. 2818–2829, 2023.
Deng, C., Zhu, D., Li, K., Gou, C., Li, F., Wang, Z., Zhong,
S., Yu, W., Nie, X., Song, Z., et al. Emerging proper-
ties in unified multimodal pretraining.arXiv preprint
arXiv:2505.14683, 2025.
Diao, H., Cui, Y ., Li, X., Wang, Y ., Lu, H., and Wang,
X. Unveiling encoder-free vision-language models.Ad-
vances in Neural Information Processing Systems, 37:
52545–52567, 2024.
Duan, Y ., Chen, T., Qi, L., and Shi, Y . Divide-and-conquer
for enhancing unlabeled learning, stability, and plasticity
in semi-supervised continual learning. InProceedings of
the IEEE International Conference on Computer Vision,
pp. 583–593, 2025.
Dubey, A., Jauhri, A., Pandey, A., Kadian, A., Al-Dahle,
A., Letman, A., Mathur, A., Schelten, A., Yang, A., Fan,
A., et al. The llama 3 herd of models.arXiv e-prints, pp.
arXiv–2407, 2024.
Fa, Z., Duan, Y ., Zhang, J., Qi, L., and Shi, Y . One to-
ken, two fates: A unified framework via vision token
manipulation against mllms hallucination.arXiv preprint
arXiv:2603.10360, 2026.
Fan, K., Feng, K., Lyu, H., Zhou, D., and Yue, X. Sophiavl-
r1: Reinforcing mllms reasoning with thinking reward.
arXiv preprint arXiv:2505.17018, 2025.
Fan, W.-C., Rahman, T., and Sigal, L. Mmfactory: A uni-
versal solution search engine for vision-language tasks.
arXiv preprint arXiv:2412.18072, 2024.
Fang, R., Duan, C., Wang, K., Huang, L., Li, H., Yan, S.,
Tian, H., Zeng, X., Zhao, R., Dai, J., et al. Got: Unleash-
ing reasoning capability of multimodal large language
model for visual generation and editing.arXiv preprint
arXiv:2503.10639, 2025.
Guo, D., Yang, D., Zhang, H., Song, J., Zhang, R., Xu, R.,
Zhu, Q., Ma, S., Wang, P., Bi, X., et al. Deepseek-r1: In-
centivizing reasoning capability in llms via reinforcement
learning.arXiv preprint arXiv:2501.12948, 2025.
Hong, J., Zhao, C., Zhu, C., Lu, W., Xu, G., and Yu, X.
Deepeyesv2: Toward agentic multimodal model.arXiv
preprint arXiv:2511.05271, 2025.
Hu, Y ., Shi, W., Fu, X., Roth, D., Ostendorf, M., Zettle-
moyer, L., Smith, N. A., and Krishna, R. Visual sketch-
pad: Sketching as a visual chain of thought for multi-
modal language models.Advances in Neural Information
Processing Systems, 37:139348–139379, 2024.
Hurst, A., Lerer, A., Goucher, A. P., Perelman, A., Ramesh,
A., Clark, A., Ostrow, A., Welihinda, A., Hayes, A.,
Radford, A., et al. Gpt-4o system card.arXiv preprint
arXiv:2410.21276, 2024.
Kazemzadeh, S., Ordonez, V ., Matten, M., and Berg, T.
Referitgame: Referring to objects in photographs of nat-
ural scenes. InProceedings of the 2014 Conference on
Empirical Methods in Natural Language Processing, pp.
787–798, 2014.
Kirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C.,
Gustafson, L., Xiao, T., Whitehead, S., Berg, A. C., Lo,
W.-Y ., et al. Segment anything. InProceedings of the
IEEE International Conference on Computer Vision, pp.
4015–4026, 2023.
Kojima, T., Gu, S. S., Reid, M., Matsuo, Y ., and Iwasawa, Y .
Large language models are zero-shot reasoners.Advances
10

## Page 11

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
in Neural Information Processing Systems, 35:22199–
22213, 2022.
Komeili, M., Shuster, K., and Weston, J. Internet-augmented
dialogue generation.arXiv preprint arXiv:2107.07566,
2021.
Kwon, W., Li, Z., Zhuang, S., Sheng, Y ., Zheng, L., Yu,
C. H., Gonzalez, J., Zhang, H., and Stoica, I. Efficient
memory management for large language model serving
with pagedattention. InProceedings of the 29th Sym-
posium on Operating Systems Principles, pp. 611–626,
2023.
Lai, X., Tian, Z., Chen, Y ., Li, Y ., Yuan, Y ., Liu, S., and
Jia, J. Lisa: Reasoning segmentation via large language
model. InProceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pp. 9579–
9589, 2024.
Lai, X., Li, J., Li, W., Liu, T., Li, T., and Zhao, H. Mini-o3:
Scaling up reasoning patterns and interaction turns for
visual search.arXiv preprint arXiv:2509.07969, 2025.
Lei, W., Wang, J., Wang, H., Li, X., Liew, J. H., Feng, J., and
Huang, Z. The scalability of simplicity: Empirical analy-
sis of vision-language learning with a single transformer.
arXiv preprint arXiv:2504.10462, 2025.
Li, B., Zhang, Y ., Guo, D., Zhang, R., Li, F., Zhang, H.,
Zhang, K., Zhang, P., Li, Y ., Liu, Z., et al. Llava-
onevision: Easy visual task transfer.arXiv preprint
arXiv:2408.03326, 2024a.
Li, G., Xu, J., Zhao, Y ., and Peng, Y . Dyfo: A training-
free dynamic focus visual search for enhancing lmms in
fine-grained visual understanding. InProceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pp. 9098–9108, 2025.
Li, J., Li, D., Xiong, C., and Hoi, S. Blip: Bootstrapping
language-image pre-training for unified vision-language
understanding and generation. InInternational Confer-
ence on Machine Learning, pp. 12888–12900. PMLR,
2022.
Li, J., Li, D., Savarese, S., and Hoi, S. Blip-2: Bootstrapping
language-image pre-training with frozen image encoders
and large language models. InInternational Conference
on Machine Learning, pp. 19730–19742. PMLR, 2023a.
Li, L., Wang, Y ., Xu, R., Wang, P., Feng, X., Kong, L.,
and Liu, Q. Multimodal arxiv: A dataset for improving
scientific comprehension of large vision-language models.
arXiv preprint arXiv:2403.00231, 2024b.
Li, Y ., Du, Y ., Zhou, K., Wang, J., Zhao, W. X., and Wen,
J.-R. Evaluating object hallucination in large vision-
language models.arXiv preprint arXiv:2305.10355,
2023b.
Li, Y ., Peng, Z., Zhang, J., Guo, J., Duan, Y ., and
Shi, Y . When shared knowledge hurts: Spectral
over-accumulation in model merging.arXiv preprint
arXiv:2602.05536, 2026.
Liu, H., Li, C., Wu, Q., and Lee, Y . J. Visual instruction tun-
ing.Advances in Neural Information Processing Systems,
36:34892–34916, 2023.
Liu, H., Li, C., Li, Y ., and Lee, Y . J. Improved baselines
with visual instruction tuning. InProceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pp. 26296–26306, 2024.
Liu, Y ., Peng, B., Zhong, Z., Yue, Z., Lu, F., Yu, B.,
and Jia, J. Seg-zero: Reasoning-chain guided seg-
mentation via cognitive reinforcement.arXiv preprint
arXiv:2503.06520, 2025.
Lu, P., Bansal, H., Xia, T., Liu, J., Li, C., Hajishirzi,
H., Cheng, H., Chang, K.-W., Galley, M., and Gao,
J. Mathvista: Evaluating mathematical reasoning of
foundation models in visual contexts.arXiv preprint
arXiv:2310.02255, 2023.
Luo, G., Yang, X., Dou, W., Wang, Z., Liu, J., Dai, J., Qiao,
Y ., and Zhu, X. Mono-internvl: Pushing the boundaries
of monolithic multimodal large language models with
endogenous visual pre-training. InProceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pp. 24960–24971, 2025.
Ma, Q., Zhang, J., Qi, L., Yu, Q., Shi, Y ., and Gao, Y . Con-
structing and exploring intermediate domains in mixed
domain semi-supervised medical image segmentation. In
Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pp. 11642–11651, 2024.
Ma, Q., Zhang, J., Li, Z., Qi, L., Yu, Q., and Shi, Y . Steady
progress beats stagnation: Mutual aid of foundation and
conventional models in mixed domain semi-supervised
medical image segmentation. InProceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pp. 5175–5185, 2025a.
Ma, Q., Zhang, J., Qi, L., Yu, Q., Shi, Y ., and Gao, Y .
Unleashing the power of intermediate domains for mixed
domain semi-supervised medical image segmentation.
IEEE Transactions on Medical Imaging, 2025b.
Ma, Z., Zhang, J., Liu, Z., Zhang, J., Tan, J., Shu, M.,
Niebles, J. C., Heinecke, S., Wang, H., Xiong, C., et al.
Taco: Learning multi-modal models to reason and act
11

## Page 12

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
with synthetic chains-of-thought-and-action. InWorkshop
on Reasoning and Planning for Large Language Models,
2025c.
Meta, A. Llama 3.2: Revolutionizing edge ai and vision
with open, customizable models.Meta AI Blog. Retrieved
December, 20:2024, 2024.
OpenAI. Thinking with images. https://openai.
com/index/thinking-with-images/, 2025.
Accessed: 2025-10-26.
Qi, J., Ding, M., Wang, W., Bai, Y ., Lv, Q., Hong, W., Xu,
B., Hou, L., Li, J., Dong, Y ., et al. Cogcom: Train large
vision-language models diving into details through chain
of manipulations. 2024.
Qiao, R., Tan, Q., Dong, G., Wu, M., Sun, C., Song,
X., GongQue, Z., Lei, S., Wei, Z., Zhang, M., et al.
We-math: Does your large multimodal model achieve
human-like mathematical reasoning?arXiv preprint
arXiv:2407.01284, 2024.
Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G.,
Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J.,
et al. Learning transferable visual models from natural
language supervision. InInternational Conference on
Machine Learning, pp. 8748–8763. PMLR, 2021.
Ravi, N., Gabeur, V ., Hu, Y .-T., Hu, R., Ryali, C., Ma, T.,
Khedr, H., R ¨adle, R., Rolland, C., Gustafson, L., et al.
Sam 2: Segment anything in images and videos.arXiv
preprint arXiv:2408.00714, 2024.
Schick, T., Dwivedi-Yu, J., Dess`ı, R., Raileanu, R., Lomeli,
M., Hambro, E., Zettlemoyer, L., Cancedda, N., and
Scialom, T. Toolformer: Language models can teach
themselves to use tools.Advances in Neural Information
Processing Systems, 36:68539–68551, 2023.
Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang,
H., Zhang, M., Li, Y ., Wu, Y ., et al. Deepseekmath: Push-
ing the limits of mathematical reasoning in open language
models.arXiv preprint arXiv:2402.03300, 2024.
Shen, H., Zhao, K., Zhao, T., Xu, R., Zhang, Z., Zhu, M.,
and Yin, J. Zoomeye: Enhancing multimodal llms with
human-like zooming capabilities through tree-based im-
age exploration.arXiv preprint arXiv:2411.16044, 2024.
Sheng, G., Zhang, C., Ye, Z., Wu, X., Zhang, W., Zhang,
R., Peng, Y ., Lin, H., and Wu, C. Hybridflow: A flexi-
ble and efficient rlhf framework.arXiv preprint arXiv:
2409.19256, 2024.
Su, A., Wang, H., Ren, W., Lin, F., and Chen, W.
Pixel reasoner: Incentivizing pixel-space reasoning with
curiosity-driven reinforcement learning.arXiv preprint
arXiv:2505.15966, 2025a.
Su, Z., Li, L., Song, M., Hao, Y ., Yang, Z., Zhang, J., Chen,
G., Gu, J., Li, J., Qu, X., et al. Openthinkimg: Learning to
think with images via visual tool reinforcement learning.
arXiv preprint arXiv:2505.08617, 2025b.
Su, Z., Xia, P., Guo, H., Liu, Z., Ma, Y ., Qu, X., Liu, J., Li,
Y ., Zeng, K., Yang, Z., et al. Thinking with images for
multimodal reasoning: Foundations, methods, and future
frontiers.arXiv preprint arXiv:2506.23918, 2025c.
Team, G., Anil, R., Borgeaud, S., Alayrac, J.-B., Yu, J., Sori-
cut, R., Schalkwyk, J., Dai, A. M., Hauth, A., Millican,
K., et al. Gemini: a family of highly capable multimodal
models.arXiv preprint arXiv:2312.11805, 2023.
Thawakar, O., Dissanayake, D., More, K. P., Thawkar, R.,
Heakl, A., Ahsan, N., Li, Y ., Zumri, I. Z. M., Lahoud, J.,
Anwer, R. M., et al. Llamav-o1: Rethinking step-by-step
visual reasoning in llms. InFindings of the Association
for Computational Linguistics: ACL 2025, pp. 24290–
24315, 2025.
Tong, P., Brown, E., Wu, P., Woo, S., IYER, A. J. V ., Akula,
S. C., Yang, S., Yang, J., Middepogu, M., Wang, Z., et al.
Cambrian-1: A fully open, vision-centric exploration
of multimodal llms.Advances in Neural Information
Processing Systems, 37:87310–87356, 2024.
Wang, H., Li, X., Huang, Z., Wang, A., Wang, J., Zhang,
T., Zheng, J., Bai, S., Kang, Z., Feng, J., et al. Traceable
evidence enhanced visual grounded reasoning: Evalua-
tion and methodology.arXiv preprint arXiv:2507.07999,
2025a.
Wang, K., Pan, J., Shi, W., Lu, Z., Ren, H., Zhou, A., Zhan,
M., and Li, H. Measuring multimodal mathematical
reasoning with math-vision dataset.Advances in Neu-
ral Information Processing Systems, 37:95095–95169,
2024a.
Wang, P., Bai, S., Tan, S., Wang, S., Fan, Z., Bai, J., Chen,
K., Liu, X., Wang, J., Ge, W., et al. Qwen2-vl: Enhancing
vision-language model’s perception of the world at any
resolution.arXiv preprint arXiv:2409.12191, 2024b.
Wang, W., Ding, L., Zeng, M., Zhou, X., Shen, L., Luo, Y .,
Yu, W., and Tao, D. Divide, conquer and combine: A
training-free framework for high-resolution image per-
ception in multimodal large language models. InProceed-
ings of the AAAI Conference on Artificial Intelligence, pp.
7907–7915, 2025b.
Wang, X., Yang, Z., Feng, C., Lu, H., Li, L., Lin, C.-C., Lin,
K., Huang, F., and Wang, L. Sota with less: Mcts-guided
sample selection for data-efficient visual reasoning self-
improvement.arXiv preprint arXiv:2504.07934, 2025c.
12

## Page 13

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
Wang, X., Zhang, J., Qi, L., and Shi, Y . Balanced direction
from multifarious choices: Arithmetic meta-learning for
domain generalization. InProceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition,
pp. 30577–30587, 2025d.
Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F.,
Chi, E., Le, Q. V ., Zhou, D., et al. Chain-of-thought
prompting elicits reasoning in large language models.
Advances in Neural Information Processing Systems, 35:
24824–24837, 2022.
Wu, P. and Xie, S. V?: Guided visual search as a core
mechanism in multimodal llms. InProceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pp. 13084–13094, 2024.
Xiao, Y ., Sun, E., Liu, T., and Wang, W. Logicvista: Multi-
modal llm logical reasoning benchmark in visual contexts.
arXiv preprint arXiv:2407.04973, 2024.
Xu, Y ., Li, C., Zhou, H., Wan, X., Zhang, C., Korhonen,
A., and Vuli´c, I. Visual planning: Let’s think only with
images.arXiv preprint arXiv:2505.11409, 2025.
Yang, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B.,
Li, C., Liu, D., Huang, F., Wei, H., Lin, H., Yang, J., Tu,
J., Zhang, J., Yang, J., Yang, J., Zhou, J., Lin, J., Dang,
K., Lu, K., Bao, K., Yang, K., Yu, L., Li, M., Xue, M.,
Zhang, P., Zhu, Q., Men, R., Lin, R., Li, T., Tang, T., Xia,
T., Ren, X., Ren, X., Fan, Y ., Su, Y ., Zhang, Y ., Wan, Y .,
Liu, Y ., Cui, Z., Zhang, Z., Qiu, Z., and . . . . Qwen2.5
technical report. arXiv preprint arXiv:2412.15115, 2024a.
Version 2, submitted 3 Jan 2025.
Yang, L., Kang, B., Huang, Z., Xu, X., Feng, J., and Zhao,
H. Depth anything: Unleashing the power of large-scale
unlabeled data. InProceedings of the IEEE/CVF Con-
ference on Computer Vision and Pattern Recognition, pp.
10371–10381, 2024b.
Yang, L., Kang, B., Huang, Z., Zhao, Z., Xu, X., Feng,
J., and Zhao, H. Depth anything v2.Advances in Neu-
ral Information Processing Systems, 37:21875–21911,
2024c.
Yang, M., Li, Z., Zhang, J., Qi, L., and Shi, Y . Taste
more, taste better: Diverse data and strong model boost
semi-supervised crowd counting. InProceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pp. 24440–24451, 2025.
Yao, H., Yin, Q., Zhang, J., Yang, M., Wang, Y ., Wu,
W., Su, F., Shen, L., Qiu, M., Tao, D., et al. R1-
sharevl: Incentivizing reasoning capability of multimodal
large language models via share-grpo.arXiv preprint
arXiv:2505.16673, 2025.
Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan,
K. R., and Cao, Y . React: Synergizing reasoning and
acting in language models. InThe eleventh International
Conference on Learning Representations, 2022.
Zhang, R., Jiang, D., Zhang, Y ., Lin, H., Guo, Z., Qiu, P.,
Zhou, A., Lu, P., Chang, K.-W., Qiao, Y ., et al. Math-
verse: Does your multi-modal llm truly see the diagrams
in visual math problems? InEuropean Conference on
Computer Vision, pp. 169–186. Springer, 2024.
Zhang, Y .-F., Lu, X., Yin, S., Fu, C., Chen, W., Hu, X., Wen,
B., Jiang, K., Liu, C., Zhang, T., et al. Thyme: Think
beyond images.arXiv preprint arXiv:2508.11630, 2025.
Zheng, Z., Yang, M., Hong, J., Zhao, C., Xu, G., Yang, L.,
Shen, C., and Yu, X. Deepeyes: Incentivizing” thinking
with images” via reinforcement learning.arXiv preprint
arXiv:2505.14362, 2025.
Zhu, J., Wang, W., Chen, Z., Liu, Z., Ye, S., Gu, L., Tian,
H., Duan, Y ., Su, W., Shao, J., et al. Internvl3: Exploring
advanced training and test-time recipes for open-source
multimodal models.arXiv preprint arXiv:2504.10479,
2025.
Zou, C., Guo, X., Yang, R., Zhang, J., Hu, B., and Zhang, H.
Dynamath: A dynamic visual benchmark for evaluating
mathematical reasoning robustness of vision language
models.arXiv preprint arXiv:2411.00836, 2024.
13

## Page 14

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
A. Prompt Design for Training and Evaluation
To ensure consistent interaction between the model and the environment, we carefully design the system and user prompts
for both the training and inference stages. The prompts aim to explicitly distinguish between the dual reasoning modes,
guiding the model to generate reasoning trajectories accordingly.
A.1. Training Prompts
During training, the system prompt defines the model’s role and available reasoning modes. The user prompt provides
multimodal inputs (text and images) and instructs the model to reason under the specified mode.
System Prompt:
You are a helpful assistant.
At the beginning of your first response, you must output either <tool on>or <tool off>to indicate whether tools will be
used to assist with subsequent answers.
-<tool on>means that you may call tools to help answer the query.
-<tool off>means that you will answer entirely without tool usage.
# When to choose<tool on>
Use<tool on>if the question requires close inspection or verification of fine details in an image, such as:
- identifying a specific object among multiple objects,
- checking small or unclear regions, sub-tables, or fine textures,
- verifying visual details that may affect the correctness of the answer.
In these cases, call the zoom-in tool as needed to focus on the relevant region.
# When to choose<tool off>
Use<tool off>if:
- the question needs global or overall image understanding (scene, layout, general context), or the relevant region or
object is already clear enough without zooming in,
- zooming in would not provide useful additional information.
# Tool calling format
You may call one or more functions to assist with the user query.
You are provided with function signatures within<tools></tools>XML tags:
<tools>
{“type”: “function”, “function”: {“name”: “image zoom in tool”, “description”: “Zoom in on a specific region of an
image by cropping it based on a bounding box (bbox) and an optional object label.”, “parameters”: {“type”: “object”,
“properties”: {“bbox 2d”: {“type”: “array”, “items”: {“type”: “number”}, “minItems”: 4, “maxItems”: 4, “description”:
“The bounding box of the region to zoom in, as [x1, y1, x2, y2], where (x1, y1) is the top-left corner and (x2, y2) is
the bottom-right corner.”}, “label”: {“type”: “string”, “description”: “The name or label of the object in the specified
bounding box (optional).”}}, “required”: [“bbo 2d”]}}}
</tools>
# How to call a tool
Return a json object with function name and arguments within<tool call></tool call>XML tags:
<tool call>
{“name”:<function-name>, “arguments”:<args-json-object>}
</tool call>
**Example**:
<tool call>
{“name”: “image zoom in tool”, “arguments”:{“bbox 2d”: [10, 20, 100, 200], “label”: “the apple on the desk”}}
<tool call>
14

## Page 15

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
User Prompt:
Question:{question}
Please follow these instructions strictly:
1. First, determine whether you will use a tool by outputting<tool on>or<tool off>.
2. Then, show your reasoning inside<think>...</think>.
3. If tool usage is required (<tool on>), call the image zoom in tool using <tool call>...</tool call>, and DO NOT
provide an<answer>yet — wait for the zoomed image in the next round.
4. If no tool is needed (<tool off>), provide your final answer inside<answer>...</answer>.
Format strictly as:
<tool on> < think> ... </think> < tool call> ... </tool call> OR <tool off> < think> ...
</think> <answer>...</answer>
A.2. Evaluation Prompts
For the Perception and Hallucination benchmarks, we use the same prompt as in the training phase to evaluate the model’s
ability in adaptive tool invocation. For the Reasoning datasets, we adopt the official prompts provided by each benchmark.
For the Grounding benchmark, following Seg-Zero (Liu et al., 2025), we employ the user prompt template as:
System Prompt:
You are a helpful assistant.
User Prompt:
Please find “{Question}” with bboxs.
Compare the difference between object(s) and find the most closely matched object(s).
Output the thinking process in<think></think>and final answer in<answer></answer>tags.
Output the bbox(es) inside the interested object(s) in JSON format.
i.e.<think>thinking process here</think> <answer>{{“bbox 2d”: [10,100,200,210]} }</answer>
B. Reward Function Details
Accuracy reward Racc:We evaluate whether the predicted answer is semantically equivalent to the ground truth. The
reward takes values in{0,0.8}, where 0 corresponds to an incorrect answer and 0.8 to a correct one. Evaluation is performed
using a combination of rule-based metrics and an online reward model (e.g.Qwen2.5-72B-Instruct). Specifically, we first
perform an exact string matching between the model output and the ground-truth answer. If the two strings are identical, the
prediction is directly regarded as correct. Otherwise, we further evaluate semantic equivalence via an online reward model.
The reward model is prompted to judge whether the predicted answer conveys the same meaning as the ground truth under a
fixed system prompt, as detailed below.
User Prompt:
Below are two answers to a question. Question is [Question], [Standard Answer] is the standard answer to the question,
and [Model answer] is the answer extracted from a model’s output to this question. Determine whether these two
answers are consistent.
Note that [Model Answer] is consistent with [Standard Answer] whenever they are essentially the same. If the meaning
is expressed in the same way, it is considered consistent, for example, ’pink’ and ’it is pink’.
If they are consistent, Judement is 1; if they are different, Judement is 0. Just output Judement and don’t output anything
else.
15

## Page 16

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
[Question]: Is the countertop tan or blue?
[Standard Answer]: The countertop is tan.
[Model answer] : tan
Judgement: 1
[Question]: On which side of the picture is the barrier?
[Standard Answer]: The barrier is on the left side of the picture.
[Model answer] : left
Judgement: 1
[Question]: Is the kite brown and large?
[Standard Answer]: Yes, the kite is brown and large.
[Model answer] : Yes
Judgement: 1
[Question]: Are the spots on a giraffe?
[Standard Answer]: No, the spots are on a banana.
[Model answer] : no
Judgement: 1
[Question]: Who is wearing pants?
[Standard Answer]: The boy is wearing pants.
[Model answer] : The person in the picture is wearing pants.
Judgement: 1
[Question]: Is the man phone both blue and closed?
[Standard Answer]: Yes, the man phone is both blue and closed.
[Model answer] : No.
Judgement: 0
[Question]: What color is the towel in the center of the picture?
[Standard Answer]: The towel in the center of the picture is blue.
[Model answer] : The towel in the center of the picture is pink.
Judgement: 0
[Question]:{question}
[Standard Answer]:{ground truth}
[Model answer] :{predict str}
Judgement:
As shown above, the prompt provides seven illustrative examples covering both consistent and inconsistent cases. The
target question is placed at the end. The reward model is instructed to output a binary judgment, where Judgement
= 1 indicates semantic consistency between the prediction and the standard answer, and Judgement = 0 otherwise.
This hybrid evaluation strategy combines strict rule-based verification with flexible semantic evaluation, enabling reliable
supervision for both factual and open-ended responses.
Format reward Rformat:This reward ensures that the reasoning process and final answer adhere to the prescribed
output format, i.e., enclosed within <think></think> and <answer></answer> tags. The reward takes values in
{−0.2,0}, where−0.2indicates a format violation and0indicates correct formatting.
16

## Page 17

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
Mode-specific tool rewardR tool:The computation ofR tool follows the procedure described in Section 3.4. The reward is
further modulated byλ mode
tool as defined in Equation (5).
C. Comparison with Prior Tool-Use Methods in LLMs
Prior work on adaptive tool use in LLMs, such as ReAct (Yao et al., 2022) and Toolformer (Schick et al., 2023), primarily
relies on prompt structures or local training signals to guide tool invocation. ReAct interleaves reasoning and actions through
carefully designed prompts, enabling the model to decide whether and how to call tools during generation. Toolformer
introduces a self-supervised objective that retains tool calls based on changes in prediction cross-entropy with and without
tool usage.
While effective, these approaches determine tool usage based on local or proxy signals, rather than directly assessing whether
tool invocation is necessary for producing a correct final answer. In contrast, our method rolls out complete reasoning
trajectories under different reasoning modes (e.g. <tool on> and <tool off>) and rewards trajectories based on answer
correctness. This outcome-driven formulation allows AutoTool to learn when tool invocation is genuinely beneficial, without
relying on intermediate heuristics.
D. Detailed Training Information
To gain a deeper understanding of how AutoTool learns to balance and adapt its reasoning behaviors, we further analyze
training dynamics, focusing on the distribution of reasoning modes, the trends in tool invocation frequency and response
length as shown in Figure 4.
/uni00000013/uni00000015/uni00000013/uni00000017/uni00000013/uni00000019/uni00000013/uni0000001b/uni00000013
/uni00000036/uni00000057/uni00000048/uni00000053
/uni00000013/uni00000011/uni00000013
/uni00000013/uni00000011/uni00000018
/uni00000014/uni00000011/uni00000013
/uni00000014/uni00000011/uni00000018/uni00000035/uni00000048/uni0000005a/uni00000044/uni00000055/uni00000047
/uni0000000b/uni00000044/uni0000000c/uni00000003/uni00000035/uni00000048/uni0000005a/uni00000044/uni00000055/uni00000047/uni00000056
/uni0000001f/uni00000057/uni00000052/uni00000052/uni0000004f/uni00000042/uni00000052/uni00000051/uni00000021
/uni0000001f/uni00000057/uni00000052/uni00000052/uni0000004f/uni00000042/uni00000052/uni00000049/uni00000049/uni00000021
/uni00000035/uni00000048/uni00000044/uni00000056/uni00000052/uni00000051/uni0000004c/uni00000051/uni0000004a
/uni00000032/uni00000059/uni00000048/uni00000055/uni00000044/uni0000004f/uni0000004f
/uni00000013/uni00000015/uni00000013/uni00000017/uni00000013/uni00000019/uni00000013/uni0000001b/uni00000013
/uni00000036/uni00000057/uni00000048/uni00000053
/uni00000013/uni00000011/uni0000001c/uni00000013
/uni00000013/uni00000011/uni0000001c/uni00000018
/uni00000014/uni00000011/uni00000013/uni00000013
/uni00000014/uni00000011/uni00000013/uni00000018
/uni00000014/uni00000011/uni00000014/uni00000013/uni00000030/uni00000048/uni00000044/uni00000051/uni00000003/uni00000026/uni00000044/uni0000004f/uni0000004f/uni00000056
/uni0000000b/uni00000045/uni0000000c/uni00000003/uni00000024/uni0000004a/uni00000048/uni00000051/uni00000057/uni00000003/uni00000037/uni00000052/uni00000052/uni0000004f/uni00000003/uni00000026/uni00000044/uni0000004f/uni0000004f/uni00000003/uni00000030/uni00000048/uni00000044/uni00000051
/uni00000037/uni00000052/uni00000052/uni0000004f/uni00000003/uni00000026/uni00000044/uni0000004f/uni0000004f/uni00000003/uni00000030/uni00000048/uni00000044/uni00000051
/uni00000013/uni00000015/uni00000013/uni00000017/uni00000013/uni00000019/uni00000013/uni0000001b/uni00000013
/uni00000036/uni00000057/uni00000048/uni00000053
/uni00000014/uni00000017/uni00000013
/uni00000014/uni00000018/uni00000013
/uni00000014/uni00000019/uni00000013
/uni00000014/uni0000001a/uni00000013
/uni00000014/uni0000001b/uni00000013
/uni00000014/uni0000001c/uni00000013/uni00000037/uni00000052/uni0000004e/uni00000048/uni00000051/uni00000056
/uni0000000b/uni00000046/uni0000000c/uni00000003/uni00000035/uni00000048/uni00000056/uni00000053/uni00000052/uni00000051/uni00000056/uni00000048/uni00000003/uni0000002f/uni00000048/uni00000051/uni0000004a/uni00000057/uni0000004b/uni00000003/uni0000000b/uni00000057/uni00000052/uni0000004e/uni00000048/uni00000051/uni00000056/uni0000000c
/uni00000035/uni00000048/uni00000056/uni00000053/uni00000052/uni00000051/uni00000056/uni00000048/uni00000003/uni0000002f/uni00000048/uni00000051/uni0000004a/uni00000057/uni0000004b
Figure 4.Detailed training-phase analysis. (a) Dual reasoning trajectories, general reasoning data, and overall average reward curves. (b)
Average number of tool invocations under the <tool on> mode. (c) Response length variations throughout training. The shaded regions
denote the standard deviation across multiple runs.
For each batch of training data, we add tool-invocation prompts to the samples from the V* (where the V* here is distinct
from the V* used in evaluation benchmarks) and ArxivQA datasets, while the samples from the ThinkLite-VL dataset
adopt purely text-centric reasoning and answer generation to preserve general reasoning capability. Figure 4(a) presents the
average reward curves for three reasoning types, along with the overall average reward for all samples. All rewards show a
steady upward trend, demonstrating the effectiveness of our training strategy. Figure 4(b) illustrates the average number
of tool invocations in <tool on> reasoning trajectories during training. The model quickly learns the correct invocation
format in the early stage, and the average number of tool calls gradually stabilizes just above one per query, reflecting a
more deliberate and efficient tool-usage behavior. Figure 4(c) shows the curve of the average number of generated tokens,
which gradually decreases and stabilizes around 150. Combined with the increasing reward trend, this indicates that our
method enables the model to produce more accurate answers with lower reasoning cost.
E. Accuracy Analysis under Different Reasoning Modes
We report the accuracy under different reasoning modes across three benchmarks in Figure 5. As shown, the error rate of
the <tool off> mode is consistently lower than that of the tool-on mode on all benchmarks (10.8% vs. 13.8%, 1.6% vs.
8.4%, and 4.4% vs. 6.7%, respectively).
This observation is expected, as AutoTool tends to select the<tool off> mode for relatively simple queries that can be
reliably solved using the model’s internal knowledge alone. In such cases, invoking external tools may introduce unnecessary
17

## Page 18

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
operations or error propagation, leading to higher failure rates. In contrast, the<tool on> mode is predominantly activated
for more complex or visually challenging questions, where the overall task difficulty is inherently higher.
HRbench V* POPE
50.7%
13.8%
 24.5%
10.8%
Tool off
Tool on
False
220
True
811
True
396
False
173
71.7%
8.4%
18.3%
1.6%
Tool on
False
16
True
137
True
35
False
3
6.7%
44.8%
Tool onTrue
3973
True
4030
False
394
Tool off
4.4%
Tool off
False
60344.1%
Figure 5.Accuracy comparison between both reasoning modes across three benchmarks.
F. Comparison with other Baselines
We further compare AutoTool with prompt-based baselines on Qwen2.5-VL-7B (Bai et al., 2025), where reasoning modes
are controlled solely through prompt design. We additionally include LlamaV-o1 (Thawakar et al., 2025) for comparison,
which is built upon Llama-3.2-11B-Vision-Instruct (Meta, 2024) and trained via SFT to follow a fixed reasoning pattern,
generating detailed reasoning steps and final answers after producing summaries and descriptions. As shown in Table 9,
although prompt engineering can partially affect tool usage, it lacks reliable and stable control. In contrast, our RL-based
method (MSPO+AMB) consistently outperforms prompt-only baselines. Notably, AutoTool outperforms LlamaV-o1 even
with a smaller model size, highlighting the efficiency and adaptability of RL-based strategy.
Table 9.Comparison with other Baselines.
Exp HRbench-4K HRbench-8K V* POPE
FSP FCP FSP FCP Attribute Spatial Adversarial Popular Random
Base Modelprompt 87.8 60.3 82.5 58.5 87.0 81.6 80.1 80.3 80.8
LlamaV-o1 66.5 56.3 52.3 49.0 60.0 79.0 85.1 87.8 90.4
AutoTool 92.5 61.3 88.0 60.0 91.3 88.2 86.1 88.4 92.3
G. Results on Other Base Models
To evaluate the robustness of our method across different base models, we conduct additional experiments using Qwen2.5-
VL-3B as the foundation model. Training is performed on four H200 GPUs, while an additional two H200 GPUs are used
to deploy the reward model. Table 10 reports results on a diverse set of benchmarks. Across all benchmarks, AutoTool3B
consistently outperforms the corresponding base model. These results indicate that the proposed method is not tied to a
specific model scale and generalizes well to other base models.
Table 10.Results on Other Base Models
Exp HRbench-4K HRbench-8K V* POPE
FSP FCP FSP FCP Attribute Spatial Adversarial Popular Random
Base Model-3B87.8 60.3 82.5 58.5 87.0 81.6 80.1 80.3 80.8
AutoTool-3B 92.5 61.3 88.0 60.0 91.3 88.2 86.1 88.4 92.3
Exp refCOCO refCOCOg refCOCO+
test testA testB val test val testA testB val
Base Model-3B 82.0 46.0 77.3 42.8 52.2 56.6 73.1 73.5 74.0
AutoTool-3B 86.5 54.0 81.8 49.3 79.1 61.8 85.6 87.4 91.77
Exp ReasonSeg MathVistaMathVerse MathVision WeMath DynaMathLogicVistatest val test testmini
Base Model-3B28.4 34.0 56.5 33.2 11.7 14.1 23.1 47.0 40.6
AutoTool-3B 41.9 52.0 62.5 36.0 12.8 17.4 33.5 50.1 41.7
18

## Page 19

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
H. Additional Comparison on Hallucination Benchmarks
HallusionBench is a benchmark that evaluates both visual illusion and knowledge hallucination in MLLMs. We conduct
experiments on its image split to complement POPE, which mainly focuses on object existence hallucination. For all
baseline models, including Qwen2.5-VL-7B (Bai et al., 2025), InternVL3-8B (Zhu et al., 2025), LLaV A-OneVision-7B (Li
et al., 2024a), and DeepEyes-7B (Zheng et al., 2025), we use the same prompting strategy as in the POPE experiments. As
shown in Table 11, AutoTool achieves the best performance on HallusionBench, demonstrating that our method generalizes
beyond POPE and effectively reduces both visual and knowledge hallucinations.
Table 11.Comparison of different models on HallusionBench.
Benchmark Qwen2.5-VL-7BInternVL3-8BLLaV A-OneVision-7BDeepEyes-7BAutoTool-7B
HallusionBench 57.8 59.7 52.9 58.5 60.9
I. Further Ablation Studies
To further analyze the design choices of our method, as shown in Table 12, we conducted additional ablation experiments.
AutoToolSFT performs an additional SFT stage before GRPO using a small amount of data that matches the dual reasoning
mode. Although the model learns both reasoning types, this rigid and forced training procedure disrupts the model’s inherent
knowledge, leading to a significant performance drop.
AMBlinear linearly decreases the influence of Fon on λmode
tool during training, following λmode
tool =λ tool ± t
tmax
(0.5−F on),
where t denotes the current training step and tmax represents the total number of training steps. This schemes still impose
a residual constraint throughout training, merely reducing its strength over time without granting the model full freedom.
AutoToolw/o AMB conduct an ablation without the AMB module, leaving the rollout proportions of the two reasoning
modes uncontrolled. Due to the inherent reasoning bias of the foundation model, the policy strongly favors <tool off>,
converging to pure text-based reasoning. Results show a clear performance drop compared to AutoTool, highlighting the
importance of balanced mode constraint. In contrast, our method focuses on balanced exploration of dual reasoning modes
during the early and middle stages of training, and completely removes the constraint in the later stage, allowing the model
to freely explore and consolidate its preferred reasoning strategy.
Table 12.Further Ablation experiments.
Exp HRbench-4K HRbench-8K V*
FSP FCP Overall FSP FCP Overall Attribute Spatial Overall
AutoToolSFT 59.0 56.5 57.8 52.0 53.3 52.6 50.4 64.5 56.0
AMBlinear 92.3 59.3 75.8 86.5 58.5 72.5 90.4 86.8 89.0
AutoToolw/o AMB 87.8 60.3 74.0 82.5 58.5 70.5 87.0 81.6 84.8
AutoTooldelay 92.7 61.3 77.0 87.560.373.9 90.4 88.2 89.5
AutoToolnotoken 92.3 60.8 76.5 87.0 60.0 73.5 89.689.589.5
AutoToolw/ KL 91.5 59.8 75.6 86.5 59.3 72.9 89.6 88.2 89.0
AutoTool 92.5 61.3 76.9 88.0 60.0 74.0 91.3 88.2 90.1
To study whether the first-step tool decision is overly restrictive, we also evaluate a variant that delays the generation of
<tool on> or <tool off> until after an explicit thinking phase. Specifically, the model follows <think> ...
</think> <tool on> <tool call> ... </tool call> or <think> ... </think> <tool off>
<answer> ... </answer> . The results are reported as AutoTooldelay. We observe no significant performance
improvement from delaying the decision token. This suggests that deciding whether to invoke a tool can be reliably
determined from the image–question pair alone, without requiring extended intermediate reasoning. Moreover, the delayed
design complicates inference-time control, as enforcing a specific reasoning mode requires multi-stage decoding. Overall, the
first-step decision provides a simpler and more practical design without sacrificing performance. We further study the training
strategy without explicit <tool on> / <tool off> tokens, where the model follows <think> ... </think>
<tool call> ... </tool call> or <think> ... </think> <answer> ... </answer> . The cor-
responding results are reported as AutoToolnotoken. Similar to AutoTooldelay, the decision of whether to invoke a tool is made
after the thinking phase. Although the overall performance is comparable to that of our AutoTool, this design remains less
flexible at test time as it does not allow direct control over the reasoning mode.
In our method, we do not include a KL regularization term, allowing the model to freely explore and converge faster. For
19

## Page 20

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
comparison, AutoToolw/ KL reports results with a KL coefficient of 0.01. Introducing KL restricts the model’s exploration,
making it harder to learn more optimal reasoning strategies.
J. Effect of Reward Model Scale
In our main experiments, we adopt Qwen2.5-72B-Instruct (Yang et al., 2024a) as the reward model. To study the impact of
reward model capacity, we conduct an ablation using smaller models from the same Qwen2.5-Instruct family, including
32B, 14B, and 7B. The quantitative results are summarized in Table 13. As shown in the results, larger reward models
consistently lead to better downstream performance. We attribute this improvement to their stronger ability to provide
more accurate feedback for open-ended responses, which is particularly important in reinforcement learning with verifiable
rewards. In contrast, smaller reward models tend to produce noisier or less discriminative reward signals, making it harder
for the policy to distinguish between subtly different reasoning outcomes. Despite these differences, our method consistently
improves performance compared with base model (i.e.Qwen2.5-VL-7B (Bai et al., 2025)) across all reward model scales,
demonstrating its robustness to the choice of reward model.
Table 13.Effect of Reward Model Scale.
Exp HRbench-4K HRbench-8K V*
FSP FCP Overall FSP FCP Overall Attribute Spatial Overall
Base Model 81.8 57.5 69.6 74.0 52.0 63.0 67.0 72.4 69.1
AutoToolReward-7B 87.5 58.8 73.1 81.0 55.0 68.0 83.5 75.0 80.1
AutoToolReward-14B 91.3 59.0 75.1 86.0 58.3 72.1 88.7 81.6 85.9
AutoToolReward-32B 91.8 60.3 76.0 87.3 59.3 73.3 89.6 85.5 88.0
AutoToolReward-72B 92.5 61.3 76.9 88.0 60.0 74.0 91.3 88.2 90.1
K. Mode-forced Evaluation
In addition to adaptive tool invocation, our model also allows manually constraining its reasoning behavior by inserting
special tokens or prompt instructions that enforce a specific reasoning mode. As shown in Table 14, both the fully tool-
assisted (<tool on>) and tool-free (<tool off>) variants achieve competitive performance, demonstrating that each
reasoning mode is well trained under our training strategy. The fully tool-assisted mode achieves slightly higher accuracy on
certain splits but incurs additional inference overhead. By contrast, the adaptive mode selection of AutoTool achieves the
best overall performance by dynamically choosing the most suitable reasoning strategy according to the characteristics of
each query. We further explore the effect of forcing AutoTool to use a reasoning mode opposite to its preferred choice at test
time. Specifically, we enforce <tool on> for samples where AutoTool originally predicts <tool off>, and vice versa.
The corresponding results are reported as AutoToolreverse. The majority of samples are forced into unsuitable reasoning
modes, leading to the worst overall performance among all variants. This observation further highlights the importance of
selecting an appropriate reasoning mode for each instance.
Table 14.Mode-forced evaluation results.
Exp HRbench-4K HRbench-8K V*
FSP FCP Overall FSP FCP Overall Attribute Spatial Overall
AutoToolon 93.361.377.3 88.0 59.8 73.9 89.689.589.5
AutoTooloff 92.3 59.0 75.6 86.5 58.3 72.4 89.6 82.9 86.9
AutoToolreverse 91.5 58.5 75 86.3 57.5 71.9 87.8 81.6 85.3
AutoTool 92.5 61.3 76.9 88.0 60.0 74.0 91.3 88.2 90.1
L. Test Performance over Training Progress
To illustrate the evolution of downstream performance during RL training, we report test accuracy on three representative
benchmarks (HRBench-4K, HRBench-8K and V*) measured every 10 training steps over the full 80-step schedule. Figure 6
plots the performance curves for each benchmark. Each curve reports the performance of Overall, FSP, and FCP (or
Attribute/Spatial for V*) as the model progresses from 10 to 80 training steps. The results demonstrate that AutoTool
steadily improves across all benchmarks throughout training.
20

## Page 21

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
/uni00000014/uni00000013/uni00000015/uni00000013/uni00000016/uni00000013/uni00000017/uni00000013/uni00000018/uni00000013/uni00000019/uni00000013/uni0000001a/uni00000013/uni0000001b/uni00000013
/uni00000036/uni00000057/uni00000048/uni00000053
/uni00000019/uni00000013
/uni0000001a/uni00000013
/uni0000001b/uni00000013
/uni0000001c/uni00000013/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c/uni00000003/uni0000000b/uni00000008/uni0000000c
/uni0000000b/uni00000044/uni0000000c/uni00000003/uni0000002b/uni00000035/uni00000025/uni00000048/uni00000051/uni00000046/uni0000004b/uni00000010/uni00000017/uni0000002e
/uni00000032/uni00000059/uni00000048/uni00000055/uni00000044/uni0000004f/uni0000004f
/uni00000029/uni00000036/uni00000033
/uni00000029/uni00000026/uni00000033
/uni00000014/uni00000013/uni00000015/uni00000013/uni00000016/uni00000013/uni00000017/uni00000013/uni00000018/uni00000013/uni00000019/uni00000013/uni0000001a/uni00000013/uni0000001b/uni00000013
/uni00000036/uni00000057/uni00000048/uni00000053
/uni00000019/uni00000013
/uni00000019/uni00000018
/uni0000001a/uni00000013
/uni0000001a/uni00000018
/uni0000001b/uni00000013
/uni0000001b/uni00000018/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c/uni00000003/uni0000000b/uni00000008/uni0000000c
/uni0000000b/uni00000045/uni0000000c/uni00000003/uni0000002b/uni00000035/uni00000025/uni00000048/uni00000051/uni00000046/uni0000004b/uni00000010/uni0000001b/uni0000002e
/uni00000032/uni00000059/uni00000048/uni00000055/uni00000044/uni0000004f/uni0000004f
/uni00000029/uni00000036/uni00000033
/uni00000029/uni00000026/uni00000033
/uni00000014/uni00000013/uni00000015/uni00000013/uni00000016/uni00000013/uni00000017/uni00000013/uni00000018/uni00000013/uni00000019/uni00000013/uni0000001a/uni00000013/uni0000001b/uni00000013
/uni00000036/uni00000057/uni00000048/uni00000053
/uni0000001b/uni00000013/uni00000011/uni00000013
/uni0000001b/uni00000015/uni00000011/uni00000018
/uni0000001b/uni00000018/uni00000011/uni00000013
/uni0000001b/uni0000001a/uni00000011/uni00000018
/uni0000001c/uni00000013/uni00000011/uni00000013/uni00000024/uni00000046/uni00000046/uni00000058/uni00000055/uni00000044/uni00000046/uni0000005c/uni00000003/uni0000000b/uni00000008/uni0000000c
/uni0000000b/uni00000046/uni0000000c/uni00000003/uni00000039/uni0000000d
/uni00000032/uni00000059/uni00000048/uni00000055/uni00000044/uni0000004f/uni0000004f
/uni00000024/uni00000057/uni00000057/uni00000055/uni0000004c/uni00000045/uni00000058/uni00000057/uni00000048
/uni00000036/uni00000053/uni00000044/uni00000057/uni0000004c/uni00000044/uni0000004f
Figure 6.Test accuracy across different training steps on HRBench-4K, HRBench-8K, and V*.
M. Extension to the Multi-tool Setting
Although the main experiments focus on a zoom-in tool for clarity and controlled analysis, our method is not restricted
to a single tool type. To evaluate its generality, we further study our method in a multi-tool setting based on Deep-
EyesV2 (Hong et al., 2025), a recently proposed framework that supports interleaved invocation of heterogeneous tools,
including programmatic code execution and web retrieval, going well beyond simple image cropping.
In DeepEyesV2, multi-tool capabilities are primarily elicited through curated SFT data, which encourages the model to
invoke appropriate tools during reasoning. During the subsequent RL stage, only accuracy and format rewards are applied,
deliberately avoiding explicit tool-use rewards. While this design partially alleviates excessive tool invocation, the heavy
reliance on tool-centric SFT data still biases the model toward frequent tool usage. As a result, the model exhibits a strong
preference for invoking tools, and its tool-free reasoning capability remains under-optimized.
Table 15.Performance in Multi-tool Setting.
Exp Size Training HRbench-4K HRbench-8K V*FSP FCP Inference FSP FCP Inference Attribute Spatial Inference
DeepEyesV2 7B 50.3 h 90.5 62.0 55.75 min 87 60.8 63.12 min 86.1 82.9 2.62 min
DeepEyesV2AMB+MSPO7B 40.4 h 92.3 62.8 37.52 min88.8 61.5 42.25 min 88.7 84.2 1.82 min
  37.8%
 38.6%
12.2% 11.4%
Without Tool
With Tool HRbench-8K
617HRbench-4K
605
HRbench-4K
195
HRbench-8K
183
DeepEyesV2
HRbench  
56.5%
34.6%
3.7%
5.2%
With Tool
Spatial
66
Attribute
108
Attribute
7
Spatial
10
Without Tool
DeepEyesV2
V*  31.4%
 33.6%
18.6% 16.4%
Tool off
Tool on HRbench-8K
537HRbench-4K
503
HRbench-4K
297
HRbench-8K
263
DeepEyesV2
w/ ABM+MSPO
HRbench
 
53.4%
28.8%
6.8%
11.0%
Tool on
Spatial
55
Attribute
102
Attribute
13
Spatial
21
Tool off
DeepEyesV2
w/ ABM+MSPO
V*
Figure 7.The outer ring shows the proportion of the dual reasoning modes on two datasets, while the inner ring presents their distribution
across different splits within each dataset. The left two plots correspond to DeepEyesV2, and the right two plots correspond to DeepEyesV2
integrated with AMB and MSPO.
This SFT-then-RL training paradigm shares a closely aligned objective with our AMB: both aim to first establish tool-use
competence and subsequently enable more flexible exploration. However, AMB explicitly balances the relative importance
of tool-based and tool-free reasoning modes, preventing premature collapse into tool-dominant behaviors. We integrate
AMB and MSPO into the DeepEyesV2 training pipeline, demonstrating that our method is plug-and-play with existing
reinforcement learning with verifiable rewards (RLVR) algorithms. Quantitative results are reported in Table 15, showing
that our approach achieves higher overall task performance while significantly reducing both training and inference overhead.
Figure 7 further illustrates the tool invocation ratios across different benchmarks for DeepEyesV2 with and without
AMB+MSPO. The results indicate that our method generalizes well to heterogeneous multi-tool settings and effectively
mitigates tool over-reliance beyond the single zoom-in tool studied in the main paper.
21

## Page 22

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
N. More Cases
We provide several representative question–answer examples generated by our AutoTool, covering various task types
including perception, hallucination, grounding, and reasoning, as illustrated in Figure 8, Figure 9, and Figure 10. These
examples provide qualitative evidence of the model’s capability across different dimensions.
We also present several failure cases in Fig. 11. In the first example, which involves counting the number of computers, the
model incorrectly assesses the task as simple during mode selection and therefore chooses not to invoke the tool, failing to
detect the second computer. In the second example, the model selected the correct reasoning mode but localized the wrong
region, resulting in an incorrect answer. The third example is more deceptive. At a glance, the image appears to contain
three dogs, making the question seem straightforward. However, careful inspection reveals an additional small white dog
located between a black and a yellow dog. In this case, fine-grained visual inspection is required for accurate counting.
These failure cases highlight the challenges of reliable reasoning mode selection and precise visual localization.
O. Limitations and Future Work
Our method explicitly controls whether the model invokes tools in subsequent reasoning by predicting special tokens, and
has been effectively validated in both single-tool and multi-tool settings (Section M). However, in more complex scenarios
involving sequential tool calls, both redundant and insufficient tool usage may lead to incorrect final answers. Accurately
identifying ineffective steps within a tool-call chain therefore becomes a key challenge. A natural direction for future
work is to extend the reward formulation to account for tool-chain quality, enabling more fine-grained supervision over the
contribution of each tool invocation. Possible strategies include measuring the marginal utility of individual tool calls, or
incorporating trajectory-wise evaluation rewards that assess the overall efficiency and coherence of the tool-use sequence.
Exploring such reward designs in a stable and scalable manner remains an open problem.
22

## Page 23

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
<tool_off>
<think>Since the question asks about the piece of equipment prominently visible in the person's possession, and the 
image shows a golf bag with golf clubs, it's clear that a close inspection is not necessary. The equipment is clearly visible 
and identifiable without the need for a zoom-in tool.</think>
<answer>A. A golf bag with golf clubs</answer>
Question: What piece of equipment is prominently visible 
in the person's possession?
A. A golf bag with golf clubs  
B. A fishing rod  
C. A baseball bat  
D. A tennis racket
Question: What is the color of the cyclist's box?
A. The color of the cyclist's box is green.
B. The color of the cyclist's box is black.
C. The color of the cyclist's box is yellow.
D. The color of the cyclist's box is red.
<tool_on>
<think>Since the question asks for the color of the cyclist's box, it's likely that a close inspection of the image is 
necessary. Using the image_zoom_in_tool can help us focus on the specific area where the cyclist's box is located, 
allowing us to verify its color more accurately.</think>
<tool_call>{\"name\": \"image_zoom_in_tool\", \"arguments\": {\"bbox_2d\": [320, 729, 401, 819]}}</tool_call>
<think>The cyclist's box is green, which matches the color of the box in the zoomed image.</think>
<answer>A. The color of the cyclist's box is green.</answer>
Perception
Perception
Figure 8.Qualitative examples of perception benchmark generated by AutoTool.
23

## Page 24

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
<tool_off>
<think>Upon analyzing the image, there is no car present. The image shows a person water skiing, and there are no 
vehicles visible.</think>
<answer>No</answer>
Question: Is there a car in the image?
Question: Is there a person in the image?
<tool_on>
<think>Since the question asks if there is a person in the image, it's likely that a close inspection of the image is 
necessary. Using the image_zoom_in_tool can help us focus on the people in the image, which might be small and not 
clearly visible. This tool will allow us to verify if there are any people present.</think>
<tool_call>{\"name\": \"image_zoom_in_tool\", \"arguments\": {\"bbox_2d\": [35, 199, 135, 234]}}</tool_call>
<think>Upon zooming in, I can see that there are people in the image. The presence of people is confirmed by their 
distinct shapes and positions on the beach.</think>
<answer>Yes, there is a person in the image.</answer>
Hallucination
Hallucination
Figure 9.Qualitative examples of hallucination benchmark generated by AutoTool.
24

## Page 25

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
To find the object \"The blue toothbrush.\", \"The blue handled toothbrush still in its' package.\", I need to identify the 
toothbrushes in the image and determine which one matches the description.
1. **Identify the toothbrushes**: There are two toothbrushes visible in the image. One is blue and the other is red.
2. **Compare the descriptions**: The description specifies a \"blue toothbrush.\" This matches the blue toothbrush in 
the image.
3. **Locate the blue toothbrush**: The blue toothbrush is the one on the left side of the image, still in its packaging.
Given the above reasoning, the most closely matched object is the blue toothbrush.
<answer>{\"bbox_2d\": [163,188,406,348]}</answer>"
Please find \"\"The blue toothbrush.\", \"The blue handled 
toothbrush still in its' package.\"\" with bboxs.
Compare the difference between object(s) and find the most 
closely matched object(s).
Question: As shown in the figure, A, B, C are three points on ⊙ O, 
∠ACB = 25.0, then the degree of ∠BAO is ()
Choices:
(A) 50°
(B) 55°
(C) 60°
(D) 65°
To solve this problem, we need to use the properties of circles and angles.
1. **Identify the given information:**
   - ∠ACB = 25°
   - A, B, and C are points on the circle ⊙ O.
   - O is the center of the circle.
2. **Use the inscribed angle theorem:**
   - The angle subtended by an arc at the center of the circle is twice the angle subtended by the same arc at any 
point on the remaining part of the circle.
   - Therefore, ∠AOB = 2 * ∠ACB = 2 * 25° = 50°.
3. **Determine ∠BAO:**
   - ∠BAO is an angle in the isosceles triangle OAB (since OA and OB are radii of the circle and thus equal).
   - In triangle OAB, ∠OAB = ∠OBA because OA = OB.
   - The sum of the angles in a triangle is 180°.
   - ∠OAB + ∠OBA + ∠AOB = 180°.
   - Let ∠OAB = ∠OBA = x.
   - Then, 2x + 50° = 180°.
   - Solving for x, we get 2x = 130°, so x = 65°.
Therefore, the degree of ∠BAO is 65°.
The correct answer is <answer>D</answer>.
Grounding
Reasoning
Figure 10.Qualitative examples of grounding and reasoning benchmark generated by AutoTool.
25

## Page 26

Are Tools Always Beneficial? Learning to Invoke Tools Adaptively for Dual-Mode Multimodal LLM Reasoning
<tool_off>
<think>Since the question asks for the number of computers visible on the table, and we can directly observe that there 
are four computers on the table, we don't need to use a tool. We can count the computers directly from the image. 
</think>
<answer>D. Four computers</answer>   GT: B. Five computers
How many computers are visible on the table?
A. Three computers
B. Five computers
C. Two computers
D. Four computers
What is the relative position of the pink banner compared to the green trash bin?
A. To the right and slightly in front of the green trash bin
B. Directly above the green trash bin
C. To the left and slightly in front of the green trash bin
D. To the left and slightly behind the green trash bin
<tool_on>
<think>Since the question asks about the relative position of the pink banner compared to the green trash bin, it's 
likely that a close inspection of the image is necessary. Using the image_zoom_in_tool can help us focus on the specific 
areas where the green trash bin and the pink banner are located, allowing us to determine their relative positions 
more accurately.</think>
<tool_call>{\"name\": \"image_zoom_in_tool\", \"arguments\": {\"bbox_2d\": [500, 1500, 2000, 1950], \"label\": 
\"green trash bin\"}}</tool_call>
<think>By observing the zoomed image, it appears that the pink banner is to the right and slightly in front of the 
green trash bin. The green trash bin is covered with a green net, and the pink banner is positioned to the right of 
it.</think>
<answer>A. To the right and slightly in front of the green trash bin</answer> 
 GT: D. To the left and slightly behind the green trash bin
①
②
③
④
⑤
How many dogs are being walked in the image?
A. Four
B. Five
C. Two
D. Three
①
②
③
④
<tool_off>
<think>From the image, it appears that there are three dogs being walked by the person. </think>
<answer>D. Three</answer>   GT: A. Four
Figure 11.Failure cases. Orange boxes denote the ground-truth regions of interest that the model should attend to, while the red boxes
show the regions actually selected for zoom-in.
26
