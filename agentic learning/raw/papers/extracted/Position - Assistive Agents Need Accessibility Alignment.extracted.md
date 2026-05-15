# Position: Assistive Agents Need Accessibility Alignment - Extracted Text

- Source note: [[Position - Assistive Agents Need Accessibility Alignment]]
- Source PDF: `assets/Position - Assistive Agents Need Accessibility Alignment.pdf`
- Extracted: 2026-05-14
- Extractor: pypdf
- Pages: 12
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

Position: Assistive Agents Need Accessibility Alignment
Jie Hu 1 Changyuan Yan1 Yu Zheng1 Ziqian Wang1 Jiaming Zhang 1
Abstract
Assistive agents for Blind and Visually Impaired
(BVI) users require accessibility alignment as
a first-class design objective. Despite rapid
progress in agentic AI, most systems are designed
and evaluated under assumptions of sighted inter-
action, low-cost verification, and tolerable trial-
and-error, leading to systematic failures in assis-
tive scenarios that cannot be resolved by model
scaling or post-hoc interface adaptations alone.
Drawing on an analysis of 778 assistance task
instances from prior work, we show that current
agentic AI remain prone to failure in assistive sce-
narios due to mismatches between sighted-user
design assumptions and the verification, risk, and
interaction constraints faced by BVI users. We ar-
gue that accessibility should be treated as an align-
ment problem rather than a peripheral usability
concern. To this end, we introduce accessibility
alignment and propose a lifecycle-oriented design
pipeline for accessibility-aligned assistive agents,
spanning user research, system design, deploy-
ment and post-deployment iteration. We conclude
that BVI-centered assistive tasks provide a critical
stress test for agentic AI and motivate a broader
shift toward inclusive agent design.
1. Introduction
Recent advances in agentic artificial intelligence (Ferrag
et al., 2025; Acharya et al., 2025) have enabled AI sys-
tems to function as increasingly general-purpose assistants,
integrating multi-step reasoning (Zhu et al., 2025), tool
use (Singh et al., 2025), and autonomous decision mak-
ing (Viswanathan, 2025). These capabilities have motivated
growing interest in deploying agents across real-world do-
mains. In accessibility-oriented contexts, agentic AI has
1School of Artificial Intelligence and Robotics, Hunan Uni-
versity, Changsha, China. Correspondence to: Jiaming Zhang
<jiamingzhang@hnu.edu.cn>.
Proceedings of the 43 rd International Conference on Machine
Learning, Seoul, South Korea. PMLR 306, 2026. Copyright 2026
by the author(s).
been explored as a means of supporting BVI users in nav-
igation (Hwang et al., 2025), information access (Natalie
et al., 2025), and everyday task assistance (Oliveira et al.,
2022).
However, assistive settings pose requirements that are not
captured by the ability to generate plausible or task-relevant
responses. The central question is whether users can safely
rely on an agent when independent verification is costly,
interaction bandwidth is limited, and the consequences of
error are asymmetric. This challenge is particularly salient
in assistive navigation, which provides high-stakes and em-
pirically observable examples.
StreetReaderAI (Froehlich et al., 2025) improves the accessi-
bility of street-view exploration through context-aware mul-
timodal interaction, yet its evidence is derived from static
panoramas whereas real-world environments are dynamic.
Consequently, an agent may issue confident guidance about
sidewalks, crossings, or landmarks that have changed due to
construction, temporary barriers, or traffic conditions, while
BVI users may have limited ability to verify such changes
in situ. Similarly, a recent study (Chang et al., 2025) of
ChatGPT live video chat with blind participants reports
that current systems are more reliable in static scenes than
in dynamic situations, with inaccurate spatial judgments
and hallucinations that may introduce confusion and risk.
Even in constrained benchmarks, miscalibration remains
evident. Prior work (He et al., 2024) evaluates ChatGPT-4o
on short-range wayfinding queries and includes cases in
which the appropriate response is to recognize insufficient
evidence, yet incorrect guidance remains common. Collec-
tively, these navigation-centered findings highlight a broader
principle for assistive agents, namely that the capacity to
defer, request additional evidence, or decline to act is as
consequential as the capacity to produce an action plan.
These failures cannot be reduced to interface limitations
alone. They reflect underlying policy decisions about how
an agent solicits evidence, represents and communicates un-
certainty, calibrates autonomy, and supports error recovery.
In navigation, errors in perception or state estimation can
be transformed into fluent instructions, while compressed
non-visual output channels may limit the user’s ability to di-
agnose the basis of a recommendation or recover from an er-
roneous one. Analogous dynamics arise beyond navigation,
1
arXiv:2605.13579v1  [cs.AI]  13 May 2026

## Page 2

Position: Assistive Agents Need Accessibility Alignment
including assistive reading, device operation, and digital
workflows such as form completion, purchasing, schedul-
ing, and smart home control. In these settings, hidden state,
tool failures, partial observability, and irreversible actions
can similarly produce silent failures and overconfident as-
sistance.
The absence of accessibility alignment leads to systematic
failures that cannot be addressed solely through model scal-
ing or post-hoc interface adaptations. For BVI users, many
assistive tasks involve non-verifiable outputs, safety-critical
and asymmetric error costs, heightened cognitive demands,
and elevated privacy risks. Under these conditions, errors
may remain undetected, recovery may be difficult, and mis-
placed trust may have serious consequences. BVI-centered
assistive scenarios therefore constitute a revealing stress test
for agentic AI, exposing design assumptions that may be
acceptable for sighted users but fail in accessibility-critical
contexts.
These observations motivate our central position that as-
sistive agents require accessibility alignment. We define
accessibility alignmentas the compatibility between the ob-
jectives, behaviors, interaction patterns of assistive agents,
and the evaluation criteria and the abilities, constraints, and
lived experiences of BVI users. Accessibility alignment
should not be understood as an automatic consequence of
general capability scaling or as a synonym for interface-level
accessibility compliance. Rather, it constitutes a distinct
alignment objective that determines what an agent optimizes,
how it acts under uncertainty, how it communicates with
users, and how its performance is evaluated.
To substantiate this position, we conducted a large-scale
analysis of assistive tasks extracted from 417 previous
works, comprising 778 task instances related to BVI as-
sistance. From these instances, we derive a task-centric tax-
onomy that characterizes the breadth of real-world assistive
needs. Building on this taxonomy, we analyze why current
agentic AI systems remain insufficiently aligned with such
needs. We argue that the central souce of misalignment
is not merely limited model capabilities, but a mismatch
between prevailing design assumptions and the verification
constraints, error tolerance, autonomy, and interaction con-
ditions of accessibility-critical use. These misalignments
manifest across mobility and safety, reading and text access,
object centered daily operations, and goal directed visual
question answering, indicating that even technically capable
agents may remain unreliable in assistive contexts without
accessibility-specific alignment.
This paper contributes to this discussion by formulating ac-
cessibility alignment as a distinct alignment objective for
assistive agents, where success is defined not only by task
completion but also by verifiability, risk sensitivity, inter-
action efficiency, and recoverability under uncertainty. It
further proposes a lifecycle-oriented pipeline for design-
ing, deploying, and iteration accessibility-aligned assistive
agents, thereby connecting accessibility requirements to sys-
tem specification, runtime policy, evaluation metrics and
post-deployment feedback.
Conflict of Interest Disclosure.The authors declare that
there are no financial conflicts of interest related to this
work.
2. Background
2.1. Assistive Technologies for BVI Users
According to the World Health Organization (Organization
et al., 2019), at least 2.2 billion people worldwide have near
or distance vision impairment. Traditional assistive tech-
nologies such as white canes and screen readers (Lazar et al.,
2007) have long served as essential mediating tools for ac-
cessing physical and digital environments. Recent advances
in computer vision have further enabled AI-powered visual
assistance systems, including smart belts (Arg ¨uello Prada
& Santacruz Forero, 2022), electronic guide canes (Khan
et al., 2021), intelligent smart glasses (Zheng et al., 2024),
and quadrupedal guide robots (Chen et al., 2022b). While
these systems demonstrate meaningful progress, their effec-
tiveness in complex real-world settings is often constrained
by limited adaptability and robustness. Vision-based aids
commonly focus on narrow functions such as obstacle de-
tection, while providing limited support for broader situ-
ational awareness. Wearable systems that rely on GPS,
IMU or other sensors may struggle with localization errors
in signal-degraded environments. Methods built on static
scene assumptions can also become brittle under dynamic
conditions such as moving crowds, changing obstacles, or
unpredictable traffic. These limitations highlight that hard-
ware innovation and perceptual capability alone are insuf-
ficient for reliable assistance. Effective support for BVI
users requires systems that can reason about user intent,
prioritize safety-relevant information, and adapt assistance
strategies in real time. This motivates a shift from isolated,
single-function devices towards assistive agents that inte-
grate perception, reasoning, and autonomous action in a
more holistic and adaptive manner.
2.2. Agentic Systems in Accessibility-Critical Settings
Unlike passive models that primarily process information,
agentic systems (Sapkota et al., 2025) operate as active en-
tities that perceive, plan, and act within an environment.
They coordinate language-based reasoning with tool use
while maintaining task state across interactions, enabling
multi-step behavior over extended horizons rather than iso-
lated single-turn responses (Fang et al., 2025). For BVI
users, these capabilities shift assistance from passive de-
2

## Page 3

Position: Assistive Agents Need Accessibility Alignment
Figure 1.Task-Centric Taxonomy of Blind Assistance and
Distribution of Assistive Task Instances.Distribution of 778
assistive task instances across four domains and their subcategories,
highlighting dominant needs in Reading and Text Access (35%)
and Mobility and Safety (34%).
scription to goal-directed task support. An assistive agent
may, for instance, navigate graphical interfaces to obtain
services or guide users through physical spaces rather than
merely identify objects or describe scenes. However, this
shift also makes accessibility failures more consequential.
Mainstream agents are typically trained and evaluated un-
der assumptions that users can verify intermediate outputs,
tolerate trial-and-error correction, and recover from mis-
takes with low cost. In accessibility-critical deployments,
these assumptions often break down because BVI users have
limited access to visual evidence, constrained interaction
bandwidth, and asymmetric exposure to the consequences
of error. Agentic systems therefore require accessibility-
specific alignment rather than direct transfer of general-
purpose agent design.
3. Task Taxonomy and Practical Needs of BVI
Users
To establish an empirical foundation for assistive agent de-
sign, we conducted a systematic literature review covering
work from 2012 to 2025. We surveyed 417 publications
across Computer Vision (Zhang et al., 2022), Generative
AI (Fu et al., 2025), Robotics (Lu et al., 2021), and Human-
Computer Interaction (HCI) (Jeanneret Medina et al., 2022).
To bridge the gap between abstract system capabilities and
concrete user needs, we distilled high-level task descriptions
into 778 fine-grained task instances.
Through qualitative coding based on task interdependence
and constraint types, we organized these instances into four
primary categories: (1) Mobility and Safety, (2) Reading and
Text Access, (3) Object Recognition and Daily Operations,
and (4) VQA Goal-directed Query. As shown in Fig. 1, the
frequency distribution of these tasks reflects the dominant
research emphases in assistive technology while also pro-
viding an empirical proxy for recurring, high-priority needs
in BVI users’ daily lives.
3.1. Mobility and Safety
This category covers tasks that support safe locomotion and
navigation in physical environments. For BVI users, mo-
bility is central to independent living and often requires
continuous, closed-loop interaction with dynamic and par-
tially observable surroundings. Errors in this category are
especially consequential, as failures can directly lead to
immediate hazards or physical harm.
Safety-first autonomy under uncertainty.
Assistive agents for mobility and safety must support conser-
vative, risk-aware decision-making that accounts for asym-
metric and safety-critical error costs. This requires pri-
oritizing safety over efficiency and modulating autonomy
according to environmental uncertainty and user context.
Hazard Perception and Alerts (108 instances).This task
category concerns the perception and communication of
potential hazards, including static (Tang et al., 2021) and
dynamic (Kuribayashi et al., 2024) obstacles, overhead dan-
gers (Rangam et al., 2025), and broader environmental risks
such as traffic or construction zones (Aljarbouh et al., 2024;
Zhang et al., 2025). Existing systems have adapted percep-
tion techniques to identify hazards and deliver audio (Kim
et al., 2025) or haptic (Galapia et al., 2024) alerts. However,
work in this area often inherits modeling assumptions from
non-assistive settings, which can obscure user-specific costs
and misalign design priorities in safety-critical assistance.
For BVI users, hazard perception may serve as a primary
source of environmental awareness, making both missed
hazards and poorly calibrated alerts directly safety-relevant.
These properties require accessibility-aware prioritization,
uncertainty handling, and alert timing beyond generic per-
ception accuracy.
Path Planning and Navigation (116 instances).Path plan-
ning (AbuJabal et al., 2024) and navigation (Abidi et al.,
2024) involve guiding users toward a destination through
safe and efficient routes, often requiring instructions at mul-
tiple levels of granularity. These instructions may range
from high-level directions (Chen et al., 2022a) such as “turn
left after the curb” to fine-grained (Hong et al., 2020), action-
level guidance, such as “walk straight for ten meters and
turn left” . In assistive contexts, navigation systems must
adapt to user walking speed, environmental changes, and
unexpected obstacles while avoiding excessive instruction
3

## Page 4

Position: Assistive Agents Need Accessibility Alignment
load. Unlike navigation for sighted users or fully embodied
robots, assistive navigation cannot assume that route choices
and corrections can be visually verified by the end user.
Localization, Orientation, and Relocation (29 instances).
Localization (Apostolopoulos et al., 2014) and orienta-
tion (Fernandes et al., 2019) tasks concern estimating a
user’s current position and relation to surrounding land-
marks or goals, while relocation involves guiding users
from the current location to a specific target. These tasks
commonly rely on GPS (Drawil et al., 2012), vision-based
localization (Adorni et al., 2001), or indoor positioning
systems (Wahab et al., 2022). For BVI users, localization
errors or delays can propagate into navigation errors with
compounding safety implications. Localization in assistive
agents should therefore be integrated with navigation and
hazard perception rather than treated as an isolated technical
module.
3.2. Reading and Text Access
This category covers tasks related to accessing, interpret-
ing, and interacting with textual information in physical and
digital environments. Reading and text access enable BVI
users to engage with documents, interfaces, and everyday
informational artifacts, but errors can become consequen-
tial when text mediates safety, finance, health or access to
services.
Verifiable information mediation.
Assistive agents for reading and text access must align in-
formation delivery with high accuracy, explicit uncertainty
communication, and calibrated confidence. Accessibility
alignment in this category requires treating reading not
merely as visual perception, but as trustworthy information
mediation.
General Document Reading (95 instances).This cate-
gory includes short-form text (Kuzdeuov et al., 2024), such
as labels, signs and menus, as well as longer structured
documents (Tang et al., 2025; Huynh & Lin, 2024), such
as articles, books, or reports. Assistive systems must sup-
port both rapid access to brief information and sustained
interaction with extended text, including navigation across
sections, headings, and references. Although these tasks
differ in scale, they share common accessibility challenges
related to accuracy, context preservation, and error detec-
tion.
Interactive Digital Reading and UI Navigation (100 in-
stances).Interactive digital reading includes navigating
web pages (Huynh & Lin, 2024; Moterani & Lin, 2025),
emails (Sharevski & Zeidieh, 2024), PDFs (Kumar & Wang,
2024), and application interfaces (Sunkara et al., 2025), of-
ten mediated through screen readers. These tasks frequently
require searching (Moon et al., 2024), locating (Xu et al.,
2023), and interacting with interface elements such as but-
tons (Mowar et al., 2024), forms (Schmitt-Koopmann et al.,
2025). Unlike passive reading, digital interaction couples
text understanding with user actions, increasing the conse-
quences of misinterpretation and the cognitive demands on
users.
Non-linear Visual Documents (98 instances).Non-linear
visual documents include charts (Alcaraz-Martinez et al.,
2024), graphs (Srinivasan et al., 2023), and complex ta-
bles (Kumar & Wang, 2024) that do not follow a simple
linear text structure. Assistive systems must translate these
representations into accessible formats that preserve rela-
tionships, trends, and spatial organization. Errors or over-
simplifications in such translations can fundamentally dis-
tort meaning, making faithful abstraction a central accessi-
bility concern..
3.3. Object Recognition and Daily Operations
This category focuses on tasks involving understanding,
locating, and interacting with objects in everyday environ-
ments. Such tasks often require tightly coupling perception
and action, since recognition alone is insufficient without
reliable guidance for subsequent user behavior.
Grounded perception for reliable action.
Assistive agents for object recognition and daily operations
must align perception and action with context-sensitive
grounding and reliable action guidance, moving beyond ob-
ject labeling toward actionable, situation-aware assistance.
Object Understanding (56 instances).Object understand-
ing encompasses recognizing objects and interpreting their
attributes or states (Do et al., 2025), such as size (Bhowmick
& Hazarika, 2017), color (Kuzdeuov et al., 2024), tempera-
ture (Mathis & Sch¨oning, 2025), or whether an appliance is
on or off (Jiang et al., 2024). For BVI users, misidentifying
object properties or states can lead to inappropriate or unsafe
actions, highlighting the need for grounded, context-aware
interpretation rather than isolated recognition.
Object-Centered Interaction and Manipulation (35 in-
stances)These tasks (Jiang et al., 2024; Xu et al., 2023)
involve assisting users with household devices such as mi-
crowaves, washing machines, or televisions. These tasks
require translating perceptual information into step-by-step
operational guidance, often under time pressure or safety
constraints. Reliability and clarity are therefore critical, as
incorrect instructions can result in device misuse or hazards.
3.4. VQA Goal-directed Query
This category captures tasks in which users ask goal-
oriented questions grounded in visual context, and seek
information that directly informs decisions or actions. Un-
4

## Page 5

Position: Assistive Agents Need Accessibility Alignment
like generic visual question answering, these queries are
embedded in real-world intent and often require responses
that support immediate action.
Intent-aware answers that support action.
Assistive agents for goal-directed visual queries must align
responses with user intent, provide action-oriented an-
swers, and preserve contextual continuity across interac-
tions. Purely descriptive responses are insufficient when
queries are situated within real-world decision-making.
Situational Understanding (96 instances).Situational
understanding (Chang et al., 2025) includes describing
scenes and interpreting ongoing activities or events. This
may involve explaining spatial layouts, identifying dynamic
changes, or recognizing behaviors relevant to the user’s
goals. For BVI users, situational understanding supports
anticipatory decision-making rather than passive awareness
alone.
Goal-directed Object Queries (45 instances).Goal-
directed object queries (Bigham et al., 2010; Tseng et al.,
2022) focus on locating or identifying specific objects in
service of an immediate goal, such as finding an exit or
determining the position of a particular item. Effective assis-
tance requires integrating spatial reasoning with actionable
guidance rather than merely producing factual answers.
4. Why Assistive Agents Fail Without
Accessibility Alignment
Current agentic AI often fails in assistive settings because
its objectives, policies, and interaction assumptions are not
aligned with accessibility-grounded constraints. We struc-
ture the diagnosis by first identifying the environmental
stressors that characterize assistive tasks for BVI users, then
analyzing the recurring failure modes those stressors pro-
duce, and finally explaining why generic capabilities such
as planning or tool use are insufficient to address them.
We subsequently define accessibility alignment as a four-
dimensional framework that directly responds to these fail-
ures.
4.1. The Stressors That Define BVI Assistive Settings
Assistive scenarios operate under constraints that violate the
standard assumptions of general-purpose agent development.
We identify four such stressors.
Limited verifiability.Users frequently cannot indepen-
dently verify agent outputs. When an agent describes a
crosswalk as clear, a blind user has no immediate means
to confirm that assessment before acting. Under limited
verifiability, overconfident completion becomes hazardous
because users may unknowingly rely on false or incomplete
information.
High-cost errors.Error costs in assistive contexts are often
severe and irreversible. While a hallucination in a low-stakes
creative task may be benign, a hallucination in mobility guid-
ance can cause physical injury, a misreading of a medication
label can cause medical harm, and a mistake in a financial
interaction can cause material loss. Assistive agents must
therefore minimize worst-case risk rather than optimizing
only for average-case helpfulness.
Cognitive burden.BVI users commonly rely on audio
or haptic feedback while simultaneously navigating phys-
ical spaces or maintaining situational awareness. Verbose
or poorly structured output imposes cognitive load during
safety-critical tasks, forcing users to filter, parse, and recon-
struct spatial information under real-time demands.
Privacy exposure.Assistance interactions routinely cap-
ture sensitive data, such as views of private interiors, med-
ical records, and bystanders in public spaces. An agent
optimized primarily for convenience may over-collect or
vocalize such information without explicit user consent. Pri-
vacy exposure is therefore not peripheral to accessibility but
integral to the risk structure of assistive deployment.
4.2. Recurring Failure Modes in Assistive Agents
Under the four stressors identified above, unaligned agents
exhibit recurring failure patterns that are especially conse-
quential in accessibility-critical use. We identify four such
patterns and trace each to its driving stressor combination.
Silent failures.The agent acts on incorrect informa-
tion without exposing uncertainty or provenance. In
goal-directed visual question answering, confident but
wrong answers can mask hallucinations and leave users
unaware of the risk. This pattern is driven primarily by
limited verifiability and asymmetric error costs, because the
user cannot cheaply detect discrepancies and the cost of
undetected errors is severe.
Overconfident hallucinations.The agent generates plausi-
ble but incorrect content to fill evidential gaps. When read-
ing a blurred prescription label or interpreting an ambiguous
crossing, plausibility becomes a safety hazard because the
user lacks independent means of verification. This pattern
is a direct consequence of limited verifiability interacting
with an agent design that prioritizes fluent completion over
uncertainty signaling.
Miscalibrated autonomy.The agent fails to adjust its de-
cision authority to the risk and confidence of the situation.
It may book a ride to an unverified location without confir-
mation or, conversely, demand unnecessary clarifications in
low-risk tasks. This pattern stems from asymmetric error
costs and constrained bandwidth, which together limit the
5

## Page 6

Position: Assistive Agents Need Accessibility Alignment
user’s capacity to supervise every agent decision.
Interaction-induced cognitive overload.The agent deliv-
ers verbose, non -linear, or poorly timed information that
demands excessive attention. In physically situated tasks,
such failures distract users from real-world hazards and di-
rectly undermine safety. This pattern expresses constrained
interaction bandwidth under real-time task demands.
These four modes reinforce one another. Silent failures
and hallucinations erode trust, which increases cognitive
burden as users attempt to mentally verify every output.
Mis-calibrated autonomy amplifies this effect by obstructing
verification when risk is highest and by consuming band-
width with unnecessary interaction when risk is low. Ad-
dressing accessibility failures therefore requires a unified
framework that targets all four patterns simultaneously.
4.3. Origins of Misalignment: Assumptions and
Capability Gaps
The failure modes diagnosed above arise from two layers
of structural misalignment between current agent design
practices and the requirements of assistive deployment.
Implicit design assumptions.Current agentic systems are
typically developed under three assumptions that do not
transfer to accessibility-critical contexts. The verification
assumption presumes that users can rapidly audit agent out-
puts, often through visual inspection. For BVI users, such
auditing is frequently infeasible, and its absence directly
enables silent failures and overconfident hallucinations. The
error-tolerance assumption presumes that mistakes are visi-
ble and recoverable through iterative correction. In mobility
or medication tasks, however, users cannot safely test a
dangerous route or an uncertain dosage to determine cor-
rectness, which leaves mis-calibrated autonomy unchecked.
The shared -context assumption presumes that users and
agents perceive the same visual environment. In practice,
BVI users depend on the agent to construct and communi-
cate that context, creating an information asymmetry that
agents are rarely trained to bridge and that contributes to
interaction-induced cognitive overload.
Capability-need mismatch.Even when these assumptions
are made explicit, general agent capabilities do not natively
accommodate accessibility-specific requirements. Path plan-
ning can optimize for efficiency but lacks interfaces for
encoding conservative risk preferences, such as avoiding
unlit crossings or favoring routes with tactile pavement. Vi-
sion tools can return labels and confidence scores yet often
lack abstention mechanisms that would prevent hallucina-
tions from being communicated authoritatively. Memory
modules can store user preferences for personalization but,
without privacy-aware constraints, may also retain sensitive
contextual histories in ways that undermine trust. In each
case, the capability exists in principle, yet the architecture
may provide no explicit mechanism for incorporating the
safety margins, abstention policies, and privacy controls that
assistive tasks demand. Accessibility failures therefore re-
flect not only insufficient capability but also a structural gap
between what agent architectures expose and what assistive
contexts require.
4.4. A Four-dimensional Framework of Accessibility
Alignment
We define accessibility alignment along four dimensions,
each addressing a specific requirement that current agen-
tic systems underspecify. In assistive settings, alignment
is not limited to task completion. It also requires satisfy-
ing accessibility-defined success criteria under safety con-
straints, non-visual interaction, and persistent uncertainty.
Goal alignment.This dimension addresses the gap between
generic task completion and accessibility-defined success.
Reaching a destination does not constitute success if the re-
sulting route involves unsafe crossings or offers no recovery
opportunity after navigation errors. Document reading is
not successful if critical fields such as dosage or contraindi-
cations are inaccurate or unsupported by sufficient evidence.
Goal alignment requires explicit safety margins, reliabil-
ity guarantees for critical information, and error recovery
procedures under uncertainty.
Interaction alignment.Failures in interaction design of-
ten stem from paradigms that assume visual context and
high-bandwidth feedback. For BVI users, effective as-
sistance requires concise, structured, and immediately ac-
tionable communication. It further demands confirmation
strategies compatible with non-visual modalities, including
chunked instructions, explicit landmark references, and ro-
bust correction loops that enable efficient error detection
and recovery. Interaction alignment is especially critical in
multi-turn assistance and device operation.
Risk alignment.This dimension addresses failures un-
der uncertainty in safety-critical and privacy-sensitive con-
texts. Many agentic systems are optimized to maximize task
success or produce coherent outputs rather than to adopt
conservative policies that account for asymmetric risk. In
assistive settings, uncertainty should systematically trigger
safety-oriented behavior, including requesting additional
context, proposing safer alternatives, pausing, or declin-
ing to act. Risk alignment also requires privacy-respecting
behavior, with data minimization by default and explicit
communication of privacy implications whenever sensing
or sharing may occur.
Lifecycle alignment.Sustaining long -term trust requires
preventing silent performance degradation over time. As-
sistive agents operate over extended periods in dynamic en-
6

## Page 7

Position: Assistive Agents Need Accessibility Alignment
vironments, alongside evolving user routines and changing
device configurations. Without monitoring and feedback,
errors accumulate unnoticed, leading to brittle behavior and
eroded user confidence. Lifecycle alignment therefore de-
mands logging and auditing mechanisms, closed-loop user
feedback, and update processes that prioritize safety, stabil-
ity, and accountability.
These four dimensions form a coupled system rather than
independent modules. Goal alignment defines what counts
as high-risk, interaction alignment specifies how confirma-
tions operate under non-visual constraints, risk alignment
enforces conservative behavior when uncertainty is elevated,
and lifecycle alignment ensures that these properties remain
stable across deployment. The dimensions jointly respond
to the four stressors and, taken together, constitute the op-
erational definition of accessibility alignment for assistive
agents.
5. An Accessibility-Aligned Pipeline for
Assistive Agents
To operationalize the four alignment dimensions, we pro-
pose a lifecycle-oriented pipeline that translates accessibil-
ity constraints into concrete specifications, runtime policies,
evaluation targets, and post-deployment update mechanisms.
The pipeline embeds risk management, non-visual interac-
tion, and user trust across three phases: design, deployment,
and post-deployment iteration.
5.1. Phase I: Design for Alignment
The design phase converts an assistive need into an imple-
mentable specification through six artifacts.
Task Card.Task anchoring situates the target functionality
within the taxonomy and defines operational boundaries,
including environment dynamics, user constraints, and ex-
plicitly disallowed conditions.
Accessibility Success Specification.Success criteria are
defined in accessibility terms beyond generic task comple-
tion. They specify safety margins, reliability and provenance
expectations for critical information, and explicit error re-
covery procedures.
Interaction Contract.Interaction is formalized as a
low-bandwidth, non-visual protocol. It specifies how in-
structions are chunked, how landmarks and orientation cues
are expressed, when confirmations are required, and how
correction loops operate.
Risk and Uncertainty Policy.Observable uncertainty sig-
nals are bound to conservative actions, such as requesting
additional context, proposing safer alternatives, pausing, or
declining to proceed.
Privacy Manifest.Data minimization rules and user -facing
authorization requirements make sensing, retention, and
sharing implications explicit.
Autonomy Calibration Specification.Autonomy is de-
fined as a dynamic variable controlled by risk, confidence,
and user context. Explicit user overrides and safe fallback
behaviors are specified.
Together, these artifacts define what constitutes success,
how the agent communicates, and when it must adopt a
more conservative stance.
5.2. Phase II: Deployment
Deployment translates design artifacts into enforceable
runtime behavior and establishes a controlled operational
boundary.
Pre-deployment validation centers on the unacceptable fail-
ure set defined in theAccessibility Success Specification.
Stress tests target safety -critical, uncertainty -heavy, and
privacy-sensitive scenarios. Validation further verifies that
theInteraction Contractremains usable under non -visual
constraints.
At runtime, guardrails enforce risk -triggered downgrades
in autonomy, safe pause and escalation pathways, and
user-accessible controls for immediate intervention. On-
boarding materials communicate capability boundaries and
interaction expectations, including how confirmations work,
how to correct mistakes, and how privacy settings affect
sensing and logging. Deployment succeeds when conser-
vative behavior is enforced rather than left to discretionary
model behavior, and when users can reliably predict agent
behavior under uncertainty.
5.3. Phase III: Post-deployment Iteration
The iteration phase prevents failures from accumulating
silently across evolving environments, routines, and device
configurations.
The system maintains a minimal, privacy-respecting logging
and feedback plan that captures near -misses, uncertainty
triggers, and user corrections without excessive reporting
burden. Observed issues are triaged by mapping incidents to
specific stressors and failure modes, then diagnosing which
alignment dimension is underspecified or violated. Updates
follow a safe update protocol with regression tests that tar-
get red-line scenarios, interaction contract compliance, and
risk-policy consistency. Rollback mechanisms are required
when updates introduce safety regressions. Over time, con-
trolled personalization is enabled through explicit user set-
tings and transparent adaptation rules, while conservative
defaults are preserved.
This three-phase structure provides a direct pathway from
7

## Page 8

Position: Assistive Agents Need Accessibility Alignment
Table 1.Operationalizing accessibility alignment through navigation and medication-reading case studies.
Case Red-line failures Uncertainty triggers Evaluation shift Runtime implications
Navigation
assistance
for safe
mobility
Decisive crossing or route
instructions when local-
ization, curb geometry, or
obstacle status cannot be
reliably assessed.
Localization drift,
occlusion, ambiguous
map orlandmark
evidence, dynamic
obstacles, poor sensing
conditions, inconsistent
trafficcues.
From {SPL, path length,
and travel time } to
{unsafe instruction rate,
risk-trigger compliance,
recovery success, instruc-
tion latency, and confidence
calibration}.
Uncertainty estimation,
conservative route selection,
autonomy downgrade,
landmark-basednon -visual
instructions,safe pause, es-
calation to human assistance
under high uncertainty.
Medication
label and
leaflet read-
ing
Confidently reporting
unsupported dosage,
frequency, contraindi-
cations, adverse effects,
interactions, or unit
conversions from partial
or ambiguous evidence.
Blur, occlusion, folded
or curved packages,
dense typography,
conflicting OCRor
VLM candidates,low
confidenceon numeric
fields, layout ambiguity.
From {OCR accuracy,
CER/WER, and answer
accuracy} to {critical-field
accuracy, critical hallu-
cination rate, abstention
precision and recall, and
recapture success}.
Field-level confidence, am-
biguity detection, structured
output templates, recapture
policy,critical -field verifi-
cation,abstention, escala-
tion to pharmacist when key
information is unverifiable.
observed failures to revised specifications, deployment
mechanisms, and continual improvement.
5.4. Operationalizing the Pipeline Through Two Case
Studies
We instantiate the pipeline in two representative high-stakes
scenarios: navigation assistance and medication reading.
The following table contrasts the unaligned baseline with
the accessibility-aligned design across four operational di-
mensions. Table 1 summarizes how the two cases translate
accessibility alignment into red-line failures, uncertainty
triggers, evaluation shifts, and runtime implications.
Case 1: Navigation assistance for safe mobility.TheTask
Cardspecifies outdoor navigation in dynamic traffic and
explicitly disallows decisive crossing instructions at uncon-
trolled intersections when critical signals cannot be reliably
assessed. TheAccessibility Success Specificationencodes
safety margins, alternative-route requirements, and recov-
ery procedures for localization drift. TheInteraction Con-
tractmandates landmark -based, chunked instructions with
mandatory confirmations at high-risk points and immediate
stop controls. TheRisk and Uncertainty Policyenumerates
signals such as localization instability and occlusion, bind-
ing them to pausing, requesting additional cues, or propos-
ing safer detours. During deployment, validation stresses
red-line scenarios including crossings and intersection han-
dling, and onboarding clarifies capability boundaries and
override mechanisms. Post -deployment, near-misses and
user corrections are mapped back to stressors and alignment
gaps, with regression tests preserving conservative behavior
on safety-critical maneuvers.
Case 2: Reading medication leaflets and labels.TheTask
Carddefines likely inputs such as folded leaflets and bottle
labels under variable lighting and dense typography. TheAc-
cessibility Success Specificationelevates dosage, frequency,
contraindications, and interactions as critical fields requiring
reliability signaling and explicit recovery when extraction is
ambiguous. TheInteraction Contractenforces a structured
output format supporting field navigation and confirmation
of high-stakes values. TheRisk and Uncertainty Policy
treats blur, occlusion, and conflicting field candidates as
triggers for recapture, alternative presentation, pausing, or
escalation to a pharmacist. Deployment validation covers
hard layouts, low-light conditions, and numeric-unit edge
cases, ensuring the system never collapses ambiguity into
definitive statements. Post -deployment, user corrections
and recapture patterns are triaged by stressor and alignment
dimension, and regression suites maintain conservative be-
havior for all critical fields.
Across both cases, three shared patterns emerge from
the alignment pipeline. The first pattern is that evalu-
ation shifts from task -completion metrics to safety - and
verifiability-aware metrics, each directly encoding a stressor
from Sec. 4.1. A second, related pattern concerns where un-
certainty is represented in the architecture. In the navigation
case, localization uncertainty triggers route downgrading
and a pause; in the medication case, field-level confidence
triggers recapture or escalation to a pharmacist. In both
settings, uncertainty is surfaced at the decision point rather
than buried in upstream processing. Together, these patterns
point to a third, overarching principle. Conservative behav-
ior is not an optional post -hoc adjustment but a property
enforced through runtime guardrails and escalation path-
ways, making safety the default operating mode. These
patterns generalize across assistive domains and constitute
the operational core of accessibility alignment for assistive
agents.
8

## Page 9

Position: Assistive Agents Need Accessibility Alignment
6. Alternative Views and Limitations
6.1. Generalization vs. Accessibility
“General-purpose agents will eventually solve this.”
A common counterargument holds that accessibility chal-
lenges for BVI users will resolve naturally as agentic AI
systems become more general, capable, and robust. Un-
der this view, advances in reasoning, perception, and plan-
ning driven by larger models and broader training data will
eventually cover assistive needs without requiring dedicated
design.
We argue that this position conflates generalization with
accessibility. Generalization concerns an agent’s ability to
perform well across tasks and environments, typically under
benchmarked or average conditions. Accessibility concerns
whether an agent’s goals, behaviors, and interactions fit
the abilities, constraints, and risk profiles of specific user
populations. An agent can generalize across tasks while
remaining unreliable for users with disabilities (Chang et al.,
2025; He et al., 2024). Crucially, increased autonomy and
confidence, often treated as markers of progress in general-
purpose agents, can worsen accessibility outcomes when
users cannot independently detect errors or recover from
them (Froehlich et al., 2025). Our analysis of 778 task
instances suggests that many failures in BVI assistive sce-
narios do not arise from a lack of task competence but from
misaligned assumptions about verification, error tolerance,
interaction pacing, and autonomy that persist even when
agents exhibit strong general-purpose performance.
Accessibility is therefore neither a special case of generaliza-
tion nor a property that reliably emerges from scale (Ferrag
et al., 2025). It constitutes a distinct alignment objective
that must be addressed explicitly in agent design, evaluation,
and deployment. Treating accessibility as a downstream
problem to be solved later risks systematically excluding
users whose needs do not match the assumptions embedded
in current agentic systems.
6.2. HCI vs. AI
“It is not an AI, but a HCI problem.”
Another frequent response is that accessibility challenges
should be handled primarily through human-computer in-
teraction rather than AI system design. Under this framing,
the difficulties BVI users face are treated as interface limi-
tations, solvable through improved input modalities, better
screen reader support, or refined interaction flows, with the
underlying agent architecture left unchanged (Lazar et al.,
2007; Jeanneret Medina et al., 2022).
While HCI plays a crucial role in accessibility, this framing
becomes inadequate in the context of agentic AI. Unlike
traditional interactive systems, agentic AI systems are not
passive tools that merely respond to user input. They are
decision-making entities that plan actions and operate au-
tonomously over extended time horizons (Sapkota et al.,
2025; Fang et al., 2025). As a result, accessibility con-
straints shape not only how users interact with agents but
also how agents should reason, act, and manage uncertainty.
Many of the failures identified in our analysis originate up-
stream of the interface. These include inappropriate auton-
omy, miscalibrated confidence, unsafe action selection, and
a failure to account for asymmetric error costs (Chang et al.,
2025). Such failures cannot be corrected solely through
interface adaptations because they reflect misalignment in
agent goals, decision policies, and evaluation criteria. We
therefore argue that accessibility for assistive agents is not
only an HCI concern but a foundational AI design problem.
Addressing it requires integrating accessibility requirements
into agent architectures, planning and control mechanisms,
interaction strategies, and post-deployment learning. Treat-
ing accessibility as an interface-layer issue encourages post-
hoc fixes at the expense of establishing accessibility as a
core requirement for responsible agentic AI.
6.3. Limitations
Our taxonomy is derived from published task instances and
may underrepresent real-world practices of BVI users out-
side research settings. The proposed pipeline remains a
design framework rather than an implementation specifi-
cation, defining lifecycle stages and design artifacts while
leaving architectural choices and system trade-offs to future
work. Future work should validate the framework through
longitudinal deployments, quantitative measures of trust
and uncertainty calibration, and standardized benchmarks
reflecting the constraints documented in our taxonomy.
7. Conclusion
In this position paper, we grounded our claim through a
large-scale analysis of 417 prior works and 778 assistive
task cases, producing a task-centric taxonomy of blind as-
sistance and surfacing recurring failure patterns that persist
despite strong general-purpose capabilities. We proposed ac-
cessibility alignment as a practical framing for agent design
and evaluation, and outlined a lifecycle-oriented pipeline to
operationalize it. We hope this perspective encourages the
community to build assistive agents that are not only more
capable, but also more accessible for the BVI users.
Acknowledgment.This work was supported by National
Natural Science Foundation of China under Grant No.
62503166.
9

## Page 10

Position: Assistive Agents Need Accessibility Alignment
References
Abidi, M. H., Siddiquee, A. N., Alkhalefah, H., and Srivas-
tava, V . A comprehensive review of navigation systems
for visually impaired individuals.Heliyon, 10(11), 2024.
AbuJabal, N., Baziyad, M., Fareh, R., Brahmi, B., Rabie,
T., and Bettayeb, M. A comprehensive study of recent
path-planning techniques in dynamic environments for
autonomous robots.Sensors (Basel, Switzerland), 24(24):
8089, 2024.
Acharya, D. B., Kuppan, K., and Divya, B. Agentic ai:
Autonomous intelligence for complex goals–a compre-
hensive survey.IEEe Access, 2025.
Adorni, G., Cagnoni, S., Enderle, S., Kraetzschmar, G. K.,
Mordonini, M., Plagge, M., Ritter, M., Sablatn¨og, S., and
Zell, A. Vision-based localization for mobile robots.
Robotics and Autonomous Systems, 36(2-3):103–119,
2001.
Alcaraz-Martinez, R., Ribera, M., Roig Marcelino, J., and
Pascual-Almenara, A. Can we create accessible charts
with microsoft excel?: a review of possibilities and limits,
with a special focus to users with low vision. InProceed-
ings of the XXIV International Conference on Human
Computer Interaction, pp. 1–13, 2024.
Aljarbouh, A., Zubov, D., Kupin, A., and Shaidullaev, N.
Traffic-sign recognition for visually impaired pedestrians
in kyrgyzstan: Two-keypoint sift/brisk descriptor with
camerax. InCOLINS (3), pp. 145–156, 2024.
Apostolopoulos, I., Fallah, N., Folmer, E., and Bekris, K. E.
Integrated online localization and navigation for people
with visual impairments using smart phones.ACM Trans-
actions on Interactive Intelligent Systems (TiiS), 3(4):
1–28, 2014.
Arg¨uello Prada, E. J. and Santacruz Forero, L. M. A belt-
like assistive device for visually impaired people: Toward
a more collaborative approach.Cogent Engineering, 9
(1):2048440, 2022.
Bhowmick, A. and Hazarika, S. M. An insight into assistive
technology for the visually impaired and blind people:
state-of-the-art and future trends.Journal on Multimodal
User Interfaces, 11(2):149–172, 2017.
Bigham, J. P., Jayant, C., Ji, H., Little, G., Miller, A., Miller,
R. C., Miller, R., Tatarowicz, A., White, B., White, S.,
et al. Vizwiz: nearly real-time answers to visual questions.
InProceedings of the 23nd annual ACM symposium on
User interface software and technology, pp. 333–342,
2010.
Chang, R.-C., Natalie, R., Xu, W., Yap, J. Z. F., and Guo,
A. Probing the gaps in chatgpt’s live video chat for real-
world assistance for people who are blind or visually
impaired. InProceedings of the 27th International ACM
SIGACCESS Conference on Computers and Accessibility,
pp. 1–14, 2025.
Chen, S., Guhur, P.-L., Tapaswi, M., Schmid, C., and Laptev,
I. Think global, act local: Dual-scale graph transformer
for vision-and-language navigation. InProceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pp. 16537–16547, 2022a.
Chen, Y ., Xu, Z., Jian, Z., Tang, G., Yangli, Y ., Xiao, A.,
Wang, X., and Liang, B. Quadruped guidance robot for
the visually impaired: A comfort-based approach.arXiv
preprint arXiv:2203.03927, 2022b.
Do, L., Mirani, S., Pitcher-Cooper, C., Nguyen, X. D. A.,
Bairaboina, A., and Yoon, I. Youdescribe: Bridging ai ef-
ficiency and human insight for scalable audio description.
InAdjunct Proceedings of the 4th Annual Symposium on
Human-Computer Interaction for Work, pp. 1–7, 2025.
Drawil, N. M., Amar, H. M., and Basir, O. A. Gps localiza-
tion accuracy classification: A context-based approach.
IEEE Transactions on Intelligent Transportation Systems,
14(1):262–273, 2012.
Fang, J., Peng, Y ., Zhang, X., Wang, Y ., Yi, X., Zhang, G.,
Xu, Y ., Wu, B., Liu, S., Li, Z., et al. A comprehensive sur-
vey of self-evolving ai agents: A new paradigm bridging
foundation models and lifelong agentic systems.arXiv
preprint arXiv:2508.07407, 2025.
Fernandes, H., Costa, P., Filipe, V ., Paredes, H., and Barroso,
J. A review of assistive spatial orientation and navigation
technologies for the visually impaired.Universal Access
in the Information Society, 18(1):155–168, 2019.
Ferrag, M. A., Tihanyi, N., and Debbah, M. From llm
reasoning to autonomous ai agents: A comprehensive
review.arXiv preprint arXiv:2504.19678, 2025.
Froehlich, J. E., Fiannaca, A. J., Jaber, N. M., Tsaran, V .,
and Kane, S. K. Making street view accessible using
context-aware, multimodal ai: A demo of streetreaderai.
InProceedings of the 27th International ACM SIGAC-
CESS Conference on Computers and Accessibility, pp.
1–6, 2025.
Fu, B., Hadid, A., and Damer, N. Generative ai in the
context of assistive technologies: Trends, limitations and
future directions.Image and Vision Computing, 154:
105347, 2025.
10

## Page 11

Position: Assistive Agents Need Accessibility Alignment
Galapia, S. B. R., Paglinawan, A. C., and Paglinawan, C. C.
Android-based smart stick using radar with haptic feed-
back for the visually impaired. In2024 16th International
Conference on Computer and Automation Engineering
(ICCAE), pp. 498–501. IEEE, 2024.
He, J., Pundlik, S., and Luo, G. Can chatgpt assist visually
impaired people with micro-navigation?arXiv preprint
arXiv:2408.08321, 2024.
Hong, Y ., Rodriguez, C., Wu, Q., and Gould, S. Sub-
instruction aware vision-and-language navigation. InPro-
ceedings of the 2020 conference on empirical methods in
natural language processing (EMNLP), pp. 3360–3376,
2020.
Huynh, G. K. and Lin, W. Smartcaption ai-enhancing web
accessibility with context-aware image descriptions using
large language models. In2024 International Conference
on Computer and Applications (ICCA), pp. 1–7. IEEE,
2024.
Hwang, H., Yang, S., Monon, J. S., Giudice, N. A., Lee,
S. I., Biswas, J., and Kim, D. Guidenav: User-informed
development of a vision-only robotic navigation assistant
for blind travelers.arXiv preprint arXiv:2512.06147,
2025.
Jeanneret Medina, M., Lalanne, D., and Baudet, C. Human-
computer interaction in artificial intelligence for blind
and vision impairment: An interpretative literature review
based on bibliometrics: L’interaction humain-machine
en intelligence artificielle pour les aveugles et d´eficients
visuels: Une revue de litt ´erature interpr ´etative fond´ee
sur la bibliom´etrie. InAdjunct Proceedings of the 33rd
Conference on l’Interaction Humain-Machine, pp. 1–6,
2022.
Jiang, L., Jung, C., Phutane, M., Stangl, A., and Azenkot,
S. “it’s kind of context dependent”: Understanding blind
and low vision people’s video accessibility preferences
across viewing scenarios. InProceedings of the 2024 CHI
Conference on Human Factors in Computing Systems, pp.
1–20, 2024.
Khan, A., Ashraf, M. A., Javeed, M. A., Sarfraz, M. S., Ul-
lah, A., and Khan, M. M. A. Electronic guidance cane for
users having partial vision loss disability.Wireless Com-
munications and Mobile Computing, 2021(1):1628996,
2021.
Kim, J.-E., Sahas, G., and Bessho, M. Toward assisting
blind individuals in exploring unfamiliar indoor environ-
ments using multimodal llm and smartphone lidar. In
2025 IEEE International Conference on Consumer Elec-
tronics (ICCE), pp. 1–6. IEEE, 2025.
Kumar, A. and Wang, L. L. Uncovering the new acces-
sibility crisis in scholarly pdfs: publishing model and
platform changes contribute to declining scholarly docu-
ment accessibility in the last decade. InProceedings of
the 26th International ACM SIGACCESS Conference on
Computers and Accessibility, pp. 1–16, 2024.
Kuribayashi, M., Uehara, K., Wang, A., Sato, D., Chu,
S., and Morishima, S. Memory-maze: scenario driven
benchmark and visual language navigation model for
guiding blind people.arXiv preprint arXiv:2405.07060,
2024.
Kuzdeuov, A., Mukayev, O., Nurgaliyev, S., Kunbolsyn,
A., and Varol, H. A. Chatgpt for visually impaired and
blind. In2024 International Conference on Artificial
Intelligence in Information and Communication (ICAIIC),
pp. 722–727. IEEE, 2024.
Lazar, J., Allen, A., Kleinman, J., and Malarkey, C. What
frustrates screen reader users on the web: A study of 100
blind users.International Journal of human-computer
interaction, 22(3):247–269, 2007.
Lu, C.-L., Liu, Z.-Y ., Huang, J.-T., Huang, C.-I., Wang,
B.-H., Chen, Y ., Wu, N.-H., Wang, H.-C., Giarr´e, L., and
Kuo, P.-Y . Assistive navigation using deep reinforcement
learning guiding robot with uwb/voice beacons and se-
mantic feedbacks for blind and visually impaired people.
Frontiers in Robotics and AI, 8:654132, 2021.
Mathis, F. and Sch¨oning, J. Lifeinsight: Design and evalu-
ation of an ai-powered assistive wearable for blind and
low vision people across multiple everyday life scenarios.
InProceedings of the 2025 CHI Conference on Human
Factors in Computing Systems, pp. 1–25, 2025.
Moon, Y ., Lee, H., Oh, S., and Jung, H. Sagol: using
minigpt-4 to generate alt text for improving image acces-
sibility. InProceedings of the Thirty-ThirdInternational
Joint Conference on Artificial Intelligence, pp. 8745–
8748. International Joint Conferences on Artificial In-
telligence Organization Jeju . . . , 2024.
Moterani, G. and Lin, W. R. Breaking the linear barrier:
A multi-modal llm-based system for navigating complex
web content. In2025 IEEE 49th Annual Computers,
Software, and Applications Conference (COMPSAC), pp.
2066–2075. IEEE, 2025.
Mowar, P., Gupta, M., and Jain, M. Breaking the news
barrier: Towards understanding news consumption prac-
tices among bvi individuals in india. InProceedings of
the 26th International ACM SIGACCESS Conference on
Computers and Accessibility, pp. 1–11, 2024.
11

## Page 12

Position: Assistive Agents Need Accessibility Alignment
Natalie, R., Xu, W., Chang, R.-C., and Guo, A. How well
can vision language models simulate the vision percep-
tion of people with low vision? InProceedings of the 27th
International ACM SIGACCESS Conference on Comput-
ers and Accessibility, pp. 1–7, 2025.
Oliveira, J. D., Engelmann, D. C., Kniest, D., Vieira, R., and
Bordini, R. H. Multi-agent interaction to assist visually-
impaired and elderly people.International Journal of
Environmental Research and Public Health, 19(15):8945,
2022.
Organization, W. H. et al. World report on vision. 2019.
Rangam, K. S., Pukale, P. R., Jitendra, S. P., Lee, D., and
Gao, J. Smart hat 2.0: An energy-aware wearable navi-
gation system for visually impaired. In2025 IEEE Inter-
national Conference on Omni-layer Intelligent Systems
(COINS), pp. 1–6. IEEE, 2025.
Sapkota, R., Roumeliotis, K. I., and Karkee, M. Ai agents
vs. agentic ai: A conceptual taxonomy, applications and
challenges.arXiv preprint arXiv:2505.10468, 2025.
Schmitt-Koopmann, F. M., Huang, E. M., Hutter, H.-P., and
Darvishy, A. Towards more accessible scientific pdfs for
people with visual impairments: Step-by-step pdf reme-
diation to improve tag accuracy. InProceedings of the
2025 CHI Conference on Human Factors in Computing
Systems, pp. 1–16, 2025.
Sharevski, F. and Zeidieh, A. Assessing suspicious emails
with banner warnings among blind and {Low-Vision}
users in realistic settings. In33rd USENIX Security Sym-
posium (USENIX Security 24), pp. 2083–2100, 2024.
Singh, J., Magazine, R., Pandya, Y ., and Nambi, A. Agentic
reasoning and tool integration for llms via reinforcement
learning.arXiv preprint arXiv:2505.01441, 2025.
Srinivasan, A., Harshbarger, T., Hilliker, D., and Mankoff,
J. Azimuth: Designing accessible dashboards for screen
reader users. InProceedings of the 25th International
ACM SIGACCESS Conference on Computers and Acces-
sibility, pp. 1–16, 2023.
Sunkara, M., Kolgar Nayak, A., Kalari, S., Prakash, Y ., Ja-
yarathna, S., Lee, H.-N., and Ashok, V . Adapting online
customer reviews for blind users: A case study of restau-
rant reviews. InProceedings of the 22nd International
Web for All Conference, pp. 135–146, 2025.
Tang, J., Sun, M., Zhu, L., Hu, M., Zhou, M., Zhang, J., Li,
Q., and Zhai, G. Design and optimization of an assistive
cane with visual odometry for blind people to detect ob-
stacles with hollow section.IEEE Sensors Journal, 21
(21):24759–24770, 2021.
Tang, X., Abdolrahmani, A., Gergle, D., and Piper, A. M.
Everyday uncertainty: How blind people use genai tools
for information access. InProceedings of the 2025 CHI
Conference on Human Factors in Computing Systems, pp.
1–17, 2025.
Tseng, Y .-Y ., Bell, A., and Gurari, D. Vizwiz-fewshot:
Locating objects in images taken by people with visual
impairments. InEuropean Conference on Computer Vi-
sion, pp. 575–591. Springer, 2022.
Viswanathan, P. S. Agentic ai: a comprehensive framework
for autonomous decision-making systems in artificial in-
telligence.International Journal of Computer Engineer-
ing and Technology (IJCET), 16(1):862–880, 2025.
Wahab, N. H. A., Sunar, N., Ariffin, S. H., Wong, K. Y .,
Aun, Y ., et al. Indoor positioning system: A review.
International Journal of Advanced Computer Science
and Applications, 13(6), 2022.
Xu, A., Qazwini, M., Liang, C., and Guo, A. Deploying
vizlens: Characterizing user needs, preferences, and chal-
lenges of physical interfaces usage in the wild. InPro-
ceedings of the 25th International ACM SIGACCESS Con-
ference on Computers and Accessibility, pp. 1–4, 2023.
Zhang, H., Falletta, N. J., Xie, J., Yu, R., Lee, S., Billah,
S. M., and Carroll, J. M. Enhancing the travel experience
for people with visual impairments through multimodal
interaction: Navigpt, a real-time ai-driven mobile naviga-
tion system. InCompanion Proceedings of the 2025 ACM
International Conference on Supporting Group Work, pp.
29–35, 2025.
Zhang, J., Yang, K., Ma, C., Reiß, S., Peng, K., and Stiefel-
hagen, R. Bending reality: Distortion-aware transformers
for adapting to panoramic semantic segmentation. In
Proceedings of the IEEE/CVF conference on computer
vision and pattern recognition, pp. 16917–16927, 2022.
Zheng, J., Zhang, J., Yang, K., Peng, K., and Stiefelhagen,
R. Materobot: Material recognition in wearable robotics
for people with visual impairments. In2024 IEEE Inter-
national Conference on Robotics and Automation (ICRA),
pp. 2303–2309. IEEE, 2024.
Zhu, Y ., Qiao, S., Ou, Y ., Deng, S., Lyu, S., Shen, Y .,
Liang, L., Gu, J., Chen, H., and Zhang, N. Knowagent:
Knowledge-augmented planning for llm-based agents. In
Findings of the Association for Computational Linguis-
tics: NAACL 2025, pp. 3709–3732, 2025.
12
