# It's not the Language Model, it's the Tool: Deterministic Mediation for Scientific Workflows - Extracted Text

- Source note: [[It's not the Language Model, it's the Tool - Deterministic Mediation for Scientific Workflows]]
- Source PDF: `assets/It's not the Language Model, it's the Tool - Deterministic Mediation for Scientific Workflows.pdf`
- Extracted: 2026-05-15
- Extractor: pypdf
- Pages: 17
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

It’s not the Language Model, it’s the Tool:
Deterministic Mediation for Scientific Workflows
Marios Adamidis1,2, Danae Katrisioti1,2, Yannis Tzitzikas3,4, and Emmanuel Stratakis2,5
1Department of Materials Science and Technology, University of Crete, Heraklion,
Greece
2Institute of Electronic Structure and Laser, FORTH, Heraklion, Greece
3Computer Science Department, University of Crete, Heraklion, Greece
4Institute of Computer Science, FORTH, Heraklion, Greece
5Department of Physics, University of Crete, Heraklion, Greece
May 13, 2026
Abstract
Language models can produce convincing scientific analyses, but repeated generations on
the same data do not guarantee the same result. A researcher may regenerate an identical
query and receive a different fit, a different peak position or a different analysis procedure,
without an obvious way to decide which output to trust. We proposetyped mediation, a
pattern in which the model orchestrates deterministic tools rather than generating analytical
code. Each tool encodes one researcher’s exact procedure for one instrument, ported through
structured interviews. The model selects which tool to call and with what parameters. The
tool produces the result. Regeneration does not change it. We evaluate this claim by
running the same photoluminescence analysis on four platforms, including three commercial
foundation models, four times each with the same prompt. The typed tool produces identical
results across all runs. The commercial platforms either vary in numerical output and
analytical methodology across runs, or fail to produce valid results on the task. We deploy
this pattern on two instruments serving users over approximately six months, with very
positive user feedback. Both cases are very challenging: they involve proprietary binary
formats and per-seat licensed software, which force the tool to remain on local infrastructure
alongside the data and the instrument it operates. We argue that deployment topology is not
just a preference, but a structural requirement of scientific tool mediation. The result is a
practical pattern for deploying language models in scientific workflows where reproducibility
is mandatory, reducing analysis time from weeks to minutes while guaranteeing identical
outputs across runs.
1 Introduction
Motivation: Reproducibility First.The integration of language models into experimental
data analysis is accelerating, and with it the assumption that the model’s output is reliable
enough to act on. For instance, consider the case of a researcher, who after a long day of
measurements, returns to the laptop to analyze a messy photoluminescence spectrum file1. The
researcher uploads the file to the AI assistant they have used many times before and found
efficient at producing what they consider passable. The model proceeds to work on the file via
code execution and rapidly arrives at a result that appears well crafted and articulated. From
1A photoluminescence spectrum records the light emitted by a material after optical excitation, as a function
of wavelength. It is a standard characterization technique in semiconductor physics.
1
arXiv:2605.13245v1  [cs.AI]  13 May 2026

## Page 2

the peak fit to the plot and the analysis, the output validates the researcher’s hard work. There
is only one simple issue: the researcher forgot to paste the right labels for the measurements, so
they edit the query and press the regenerate button. This time, the peak position has shifted
by 2 eV, the fit is just a bit different. Neither answer is obviously wrong. What is the principled
way for the researcher to act at 9pm on a Thursday?
One important observation is that this failuredoes not go away with a more powerful model.
The model’s view of the project’s semantics is governed by a generic system prompt, not tailored
to any specific researcher’s workflow. The model is capable enough to consistently produce
convincing results. What it cannot do is produce the same result twice. The gap is determinism,
and more model capability does not provide it [1]. Reproducibility is not a luxury in science; it
is the standard that separates real discovery from mere claim.
This widespread issue appears as well in the low adoption of agents in academic research
and medicine, sitting at low single digits of real-life deployment as shown in Anthropic’s recent
report [2]. These fields have been investigated greatly for the potential of AI-related integrations,
butalackoftechnicalknow-how, combinedwiththemarketingpressurethatthemodelisalready
capable enough on its own, has made it impractical for unsupported researchers to graduate from
zero-shot prompting to task-strengthened, specialized harnesses [3].
Motivation: The Need for Privacy.A privacy concern also arises from the interaction.
Many types of laboratory data appear uniformly consistent to the human eye, dampening the
researcher’sinstincttowardswhattheywillshare with thecloudprovider. Afile containingabad
measurement is virtually indistinguishable from one that will lead to an impactful publication.
Sharing raw data and results with the cloud provider creates a non-zero probability that the
data shapes the next checkpoint’s performance in that specific niche [4]. Cutting-edge scientific
output has higher probability of being valuable on later rounds of training when compared to
trivial information extracted from the web.
Figure 1: Three approaches to scientific data analysis. Data collection is identical in all cases.
(a) Traditional: the researcher manually operates analysis software. (b) LLM-assisted: the
model generates analytical code, producing different results on each run. (c) Typed mediation
(proposed): the model orchestrates a deterministic typed tool that encodes the researcher’s exact
workflow on local infrastructure.
Approach.For tackling the above requirements, i.e. reproducibility, and privacy, we propose
an alternative way to leverage models. In particular, we propose encoding the exact manual
2

## Page 3

task of the researcher behind a tool surface. Then the model orchestrates. Subsequently, the
tool produces deterministic results that reproduce across regenerations. In this way, verification
becomes quick, and the model’s reasoning capacity goes to the parts of the work that actually
need it. Figure 1 gives an overview of the proposed approach. In the left part we see the
traditional method, relying on particular software and manual operation. In the middle part we
see the current trend, i.e. to use an LLM for the analysis, but since LLMs operate stochastically,
their output varies, therefore they derive non-reproducible results. The right part illustrates our
proposal, i.e. to leverageboththe existing software and the LLM for getting reproducible results.
We could say, that we "wrap" existing software in a way that is convenient for the language
model to orchestrate deterministic workflows. This raises the question we address in this paper:
When the workflow lives in the tool rather than the model, how much does model choice matter?
A more refined illustration is given in Figure 2.
Figure 2: Typed mediation architecture. The model orchestrates tool calls through a typed
schema. The tool encodes the scientist’s workflow and drives licensed software on local infras-
tructure.
Evaluation.We have realized this approach as a platform, called FORTHought, we have
deployed it in a research center, and the platform is in use by eleven researchers, across multiple
instrument workflows, for a period of 6 months.
The users have provided very positive feedback, and FORTHought has now become part of
their daily routine. In this paper, we shall focus on (a) the two deployments with the largest
documented impact: a photoluminescence analysis pipeline and a scanning electron microscopy
workflow, and (b) on the evaluation ofreproducibilityby running the same photoluminescence
analysis on our platform and three commercial foundation models, four times each with the
same prompt and the same data.
Contributions.In summary, our work makes four main contributions:
1. we describe atyped-mediation patternin which both the human and the language model
address the laboratory software via the same typed interface, placing the deterministic
core of the workflow in the tool rather than the model,
2. we presenttwo real applicationsported through structured interview sessions with the
researchers who own the workflows, deployed and actively used by researchers who verify
outputs quickly and feed corrections back into the tools,
3

## Page 4

3. we evaluate reproducibility by running the same analysis on four platforms four times each
and show that the typed tool produces identical results across runs while code-generating
approaches vary in both output and analytical methodology, and
4. we argue that deployment topology is a structural requirement of scientific tool mediation,
driven by both privacy concerns and the licensing constraints of most laboratory software,
which together force the tool to live alongside the data and the instrument it operates.
The rest of this paper is organized as follows. Section 2 discusses related work. Section 3
describes our approach, i.e. the typed mediation pattern. Section 4 presents two deployment
cases. Section 5 evaluates reproducibility across platforms. Section 6 concludes and outlines
future directions.
2 Related Work and Novelty
Deployed laboratory agents remain rare. Hellert et al. report a production deployment at a
synchrotron user facility, where an agentic framework manages real-time operations across more
than 230,000 control channels [5]. Vriza et al. evaluated code-generating agents at a national
X-ray nanoprobe facility and found that performance on the same task varies sharply across
models [6]. Xie et al. demonstrated LLM-driven control of a scanning photocurrent microscope,
illustrating both the potential and the fragility of code-generating approaches for instrument
automation [7]. Cissé et al. tested five reasoning models as scientific optimizers over twenty
repeat runs each and observed that a single model can produce outlier results below half its own
average performance [8]. Cui and Alexander ran 480 attempts across six models on the same
data analysis task and found considerable variation in analytical results even under identical
configurations [9]. These results confirm that within-model variance is a structural property of
code-generating approaches, not a failure of any particular model.
Tool-mediated architectures address this by restricting the model to validated tool calls.
Yang et al. report 100% tool selection consistency across three models at maximum sampling
temperature [10]. Xu et al. achieve 100% specification-level reproducibility when the model is
limited to routing decisions [11]. Pan et al. demonstrate MCP-based tool mediation entering
scientific cyberinfrastructure at the national laboratory scale [12]. Strickland et al. formalize
this principle as schema-gated orchestration, where nothing executes unless it validates against a
machine-checkable specification [13]. Doshi et al. propose extending MCP with structured labels
forcapabilities, confidentialityandtrust, enablingdeterministicenforcementofsafetyconstraints
at tool boundaries [14]. Deng et al. present a skill-centric framework for autonomous operation
across ten categories of precision instruments, where reusable operational and analytical skills
connect physical sample handling with scientific interpretation [15].
Ourcontributionisoperationalratherthanarchitectural. Wetaketheschema-gatedprinciple
and apply it to a specific problem that none of these systems address: encoding one researcher’s
exact manual workflow, extracted through structured interviews, as a typed tool that any model
can orchestrate.
3 The FORTHought Approach
At first we should clarify terminology. The key concepts and their terms and descriptions, are
given in Table 1. The reader is suggested to read it, to avoid ambiguities.
4

## Page 5

Table 1: Key terminology of FORTHought
Concept Definition
SoftwareAny application a human operates directly: a spreadsheet program, a licensed in-
strument suite, a standalone script. Designed for human interaction.
ToolA function exposed to the language model through a programmatic interface. The
model calls it; the user does not operate it directly.
SchemaA machine-readable specification of a tool’s expected inputs and outputs: parameter
names, types, allowed values and return format. It acts as the contract between the
model and the tool.
Typed toolA tool whose interface is defined by a strict schema. A call that violates the schema
is rejected before execution. A call that conforms executes the same deterministic
procedure every time, regardless of which model issued it.
MCPThe Model Context Protocol [16]: an open standard that exposes typed tools to lan-
guage models. It defines how a model discovers available tools, reads their schemas,
and issues calls.
SkillA configuration document that defines the model’s behavior for a specific instrument
or researcher workflow. It specifies which tools are available, what the researcher’s
preferences are, and how results should be presented. Each deployment case has its
own skill. An example in given in Appendix A.
Workflow specifica-
tion
The output of the structured interview process: the complete set of analytical de-
cisions a researcher applies to their data fitting model, spectral window, quality
thresholds, preprocessing steps. Each typed tool encodes exactly one workflow spec-
ification. An example in given in Appendix B.
We could summarize the entire approach as follows:
Eachtyped toolencodes aworkflow specificationextracted throughstructured interviews
with the researcher,wrapsthe operations ofexisting licensed software, and isexposed to
the modelvia MCP. A per-instrumentskilltells the model which tools are available and
how the researcher expects results to be handled. The model calls the tool, and the tool
drives the software.
3.1 Typed Mediation
Typed Mediation.We use the termtyped mediationto refer to a pattern in which the language
model does not perform the analysis itself, but selects and invokes a deterministic tool that
encodes the researcher’s exact procedure through a typed schema.
Determinism.Typed mediation places a deterministic tool between the software that the
researcher was manually using and the model. A system prompt and an accompanying per-
experimentSkill.MDfile define the model’s appropriate behavior towards the task relevant to
the user’s profiled requests. An example of a "skills file", is given in Appendix A. The model
will decide which tool to execute and with what parameters as input. The tool then proceeds
to deliver the precise results back to the model, which is instructed to just serve or reason upon
the results. This interface follows the Model Context Protocol [16], which is an open standard
that exposes each tool through a typed schema specifying its inputs, outputs and execution
requirements. The tool does not act as a generic API wrapper. It encodes one researcher’s exact
procedure for one instrument or experiment, for example what despiking parameters they use,
the spectral window they fit over and the peak boundaries they integrate between. Simply, the
model picks which tool to call, and the tool itself already knows how the work is done.
Architecture Overview.Figure 2 summarizes the typed mediation architecture. The model
operates above the typed interface and is replaceable. The tool sits below it, anchored to the
5

## Page 6

same machine as the licensed software and the instrument.
Why we need typed mediation.By design, language models are stochastic, which is both a
curse and a blessing. It allows them to appear creative and energetic in domains where verbatim
recall would fail. But in applications such as scientific analysis, the methodology used directly
affects the immediate result and the relationship between data produced in different sessions. A
deterministic tool surface allows for the creativity of the model to be utilized towards detecting
vital insights from within the process and provide better analyses using the tool output as
grounding. The model’s reasoning traces get occupied by science-related reasoning rather than
what code to execute to please the user’s requirements. Recent work confirms this empirically:
100% tool selection consistency across three models set at maximum sampling temperature [10],
and100%specification-levelreproducibilitywhenthemodelisrestrictedtoroutingdecisions[11].
The other path is to let the model generate the code required to satisfy the user’s demands,
call generic APIs or reason about the workflow itself. This is the current approach of most
users, as reported by Anthropic [2]. In a recent study, Vriza et al. evaluated this directly at a
national user facility (X-ray nanoprobe + robotic thin-film). On the hardest task, performance
ranged from 0% on weaker models such as GPT-4o-mini, to 25% on Claude 3.5 Sonnet with
high variance, to 100% on OpenAI’s O3 model [6]. This apparent spread on the same task casts
doubt on even the most seemingly consistently performant models, because it proves that the
process itself is volatile.
That volatility disappears when the model is restricted to selecting which tool to call. The
typed schema accepts valid parameters and executes the same procedure regardless of which
model issues the call. But the tool itself cannot move. Proprietary binary formats open only
inside their licensed application, per-seat licenses bind that application to one workstation, and
instrument-specific calibration files encode settings that apply to one physical device [17]. A
typed interface exposed through MCP resolves this asymmetry: the tool remains where the
work lives, and any model that can issue a valid call can orchestrate it, from bench instruments
to national-scale cyberinfrastructure [12].
3.2 Problem Statement and Approach Formally
The problem of stochastic analytical variance.LetDbe a scientific dataset andPbe a
naturallanguageprompt describing ananalyticalprocedure. Ina code-generatingLLMworkflow
(the "LLM-assisted method"), the analysis is treated as a stochastic functionfθ parameterized
by the model weightsθ. The outputRis generated as:R i =f θ(D, P, τ, si)whereτis the sam-
pling temperature andsi is the random seed for runi. The problem is defined by thevariance
of methodologyVar(f θ(D, P))̸= 0, i.e. even whenDandPremain constant,R i ̸=R j be-
cause the model reconstructs the analytical methodology (e.g., peak fitting models, background
subtraction, spectral windows) stochastically at runtime. In a scientific context, this lack of
determinism preventsRfrom being a "verifiable scientific result".
Proposed Solution.We propose a transformation where the LLM is restricted from generating
code and is instead limited toparameterizinga deterministic tool. LetTbe atyped toolthat
encodes a fixed analytical workflowW. The tool is governed by a schemaS, which defines the
valid input spaceX.
In particular, the workflowWis defined by theinterview(that extracts the researcher’s
methodology) and implemented (with the assistance of a developer) in the tool code (T), while
theskill filedefinesS(the schema), i.e. it tells the model how to call the tool, not what the tool
does internally (we could say that the skill file is the menu, not the kitchen). To summarize, the
process is:Interview
what analysis to do
− − − − − − − − − − − − →W
code impl.
− − − − − − →T, andSkill filellm− − →interfaceSofT.
According to this approach, the process is decomposed into two distinct phases:
•Orchestration (Stochastic): The LLM acts as amediatorm θ that maps(D, P)to a set
6

## Page 7

of parametersx∈ Xsuch thatxsatisfies the constraints ofS, i.e. we can writex=
mθ(D, P, S).
•Execution (Deterministic): The toolTexecutes the workflowWusing parametersx, i.e.
R=T(D, x).
Thisguarantees reproducibilitysinceTis a non-stochastic function implemented in local
infrastructure, and thus it satisfies the property:∀i, j:x i =x j ⇒T(D, xi) =T(D, x j). By
enforcingxthrough atyped schema(Schema-Gated Orchestration), the system ensures that as
long as the model’s tool-selectionxis consistent, the scientific resultRis perfectly reproducible.
This shifts the burden of "correctness" from the model’s creative generation to a validated,
researcher-defined tool surface.
Summary of Formal Contributions
•Separation of Concerns: Decoupling the reasoning (LLM) from the computation (Typed Tool)
•Topology Constraint: Formalizing thatTmust reside on local infrastructure due to propri-
etary licenses and data privacy, whilemθ may reside in the cloud.
•Zero-Variance Methodology: Ensuringσ 2 = 0for the analytical procedure across multiple
model regenerations. The deeper finding is that atight enough schemamakes the LLM’s
parameter selection deterministic too. For example ifbis the intensity exponent that we
are looking for, with our approach we getσ 2
b ≈0. We could further analyze, and define:
σ2
total =σ 2
mediation +σ 2
execution, whereσ 2
execution = 0by construction andσ 2
mediation ≈0, empiri-
cally whenSis sufficiently constrained.
4 Deployment Cases of FORTHought
As stated earlier, here we describe two deployment cases, that have significant impact. A few
statistics about these two cases, i.e. number of typed functions, users, logged sessions, time (i.e.
before and after FORTHought), validation, and other constraints, are given in Table 2.
7

## Page 8

Figure 3: Typed mediation pipeline applied to photoluminescence spectroscopy. Left: the user
describes the analysis in natural language; the model selects the tool and constructs a typed
call; the tool validates the schema, executes the deterministic workflow on local infrastructure
and returns identical results on every run. Right: core visualizations and fit metrics produced
by the tool. The bottom strip summarizes both deployment cases (PL spectroscopy and SEM
periodicity analysis).
Table 2: Deployment summary. Both tools have been in continuous use for approximately six
months.
PL spectroscopy SEM periodicity
Typed functions 22 8
Active users 1 primary + group 3
Logged sessions 60+ 15+
Manual time∼2 weeks∼2 days
Tool time minutes minutes
Validation∆≤0.02calibration-checked
Local constraint binary format, device-specific
per-seat license calibration
4.1 Photoluminescence Analysis
The first deployment case is a photoluminescence analysis pipeline for semiconductor thin films.
The proprietary analysis software stores each excitation power level as a separate workbook
inside a binary project file. A typical measurement campaign produces more than twenty such
workbooks, each sharing the same wavelength axis but containing a different excitation power,
8

## Page 9

meaning a different emission spectrum. The researcher must open each one, apply the same
sequence of operations, extract the results and combine them into a single notebook. The initial
tool automated this merging step. Figure 3 illustrates the full pipeline: the researcher describes
the analysis in natural language, the model constructs a typed tool call, and the tool executes
the workflow deterministically on local infrastructure.
The tool became useful, but it was not yet correct. To move from automation to fidelity,
we conducted a structured interview of thirty questions across two sessions with the researcher
who owns the workflow. An example in given in Appendix B. Each answer refined the tool.
The fitting model was Voigt (a convolution of Gaussian and Lorentzian components that better
captures peak shape in noisy spectra), not the pure Lorentzian we had assumed. The spectral
window adapts per power level, narrowing around the emission peak as it shifts with excitation
power, rather than staying fixed. The quality threshold is approximatelyR2 ≥0.90, evaluated
visually, not the 0.95 cutoff we had implemented. Peak intensity is read as raw counts at the
maximum, not as integrated area. For an example case, the power dependence uses two separate
fits split at a saturation boundary near10µW, not a single allometric fit. None of these details
were documented. They existed in the researcher’s routine, refined over four years of doctoral
work. The final tool encodes this routine across twenty-two typed functions. The right panel of
Figure 3 shows the core visualizations and fit metrics that the tool produces from a single run.
The raw measurement files use a proprietary binary format. They open only inside the
licensed desktop application. The license is bound to one workstation. Institutional policy also
prevents uploading raw experimental files to external services. This is the normal condition
of many experimental laboratories. The model cannot open the file, cannot run the licensed
software and cannot ask the researcher to export data she is unwilling to share. The tool has to
run on the same workstation as the data and the software.
We did not build tools that imitate a result. We ported the exact workflow the scientist was
already using into a typed tool that the model orchestrates.
Manual analysis of one measurement campaign previously took approximately two weeks.
The time was spent on repeated file handling across twenty-one power levels. Each level required
thesamesequenceofoperationsinsidetheproprietaryapplication. Theportedworkflowexecutes
in minutes. The exponent from the automated split power law fit matches the researcher’s
manual result within∆≤0.02. Regeneration on the same data returns the same numbers every
time. The researcher can now verify the output in minutes because she knows what the correct
answer should look like.
The researcher is a fourth-year doctoral student working on optical spectroscopy of two-
dimensional materials. She was initially skeptical because her existing workflow already worked.
After the tool reproduced her method, she began using it regularly. Over approximately six
months, she has accumulated more than sixty interaction sessions, including more than eleven
sessions on the spectral analysis model. She has also introduced the platform to members of her
research group. The deployment is now part of her working routine.
4.2 Scanning Electron Microscopy
The second case is a scanning electron microscopy workflow for periodic structure analysis on
laser-processed surfaces. The tool encodes the calibration of one specific microscope, including
pixel scale, magnification mapping and detector configuration. A different instrument of the
same model would require different values.
The porting followed the same method. The researcher’s analysis procedure was extracted
through structured interviews and encoded as typed functions. The model selects the tool. The
tool validates the input schema, executes the analysis locally and returns deterministic results.
Three researchers now use this tool for periodic structure analysis on their respective samples.
This case is included to show that the pattern generalizes beyond spectroscopy. The instru-
ment, the file format and the analysis are different. The architectural constraint is the same:
9

## Page 10

the calibration binds the tool to the physical device, and the tool must run where the device
is. Commercial platforms cannot replicate this workflow: the calibration files are device-specific
and the analysis requires pixel-scale parameters that only the local tool encodes. The bottom
of Figure 3 summarizes both deployment cases.
4.3 Application Methodology
Cost for interviews.As regards the cost of applying this approach, note that cost for in-
terviews is relatively small: From our experience, a use case requires at most three sessions of
approximately thirty minutes each.
Cost for software development.The cost for producing a typed tool comprises (a) the
time to develop it (around 1 hour), (b) and time to refine and test it. The cost of this process
does not scale with interview duration or tool assembly time. The tool itself is straightforward
to implement once the interview has specified what to build. The real cost is validation: the
researcher whose workflow is being automated must run the tool against real data and iden-
tify inaccuracies, which are then corrected on either the tool side or the prompt side. In the
photoluminescence case (§4.1), seven of the thirty interview answers contradicted the initial im-
plementation, each requiring a correction-and-validation cycle. The development cost therefore
scales with the number of methodological corrections required, not with the duration of the
interview or the assembly of the tool. For the Scanning Electron Microscopy case (§4.2), the
tool comprised eight typed functions and the full cycle from interview to validated deployment
took approximately one day.
Skills file.As regards the skills file, writing it takes minutes. It is a configuration document,
not code. The skill file is written last, after the tool has been built and validated against real
data. Its purpose is to constrain the model’s behavior during orchestration: which tools to call
in what order, what parameter values to prefer, and how to respond when the user’s prompt is
underspecified or when the tool returns an ambiguous error.
The content of the skill file matters more than its length. Modern language models are
trained to be helpful, which means that when an error occurs they will attempt to use their
reasoning and any available tools to find alternative solutions. In a scientific workflow this is
dangerous because the alternative solution may produce a plausible but incorrect result. The
skill file preempts this by defining predetermined behavior for failure modes, user preferences,
and workflow-specific edge cases. For example, the PL skill file (Appendix A) specifies exact
parameter names and rejects plausible-sounding alternatives that the typed schema would not
accept.
A poorly written skill file is worse than having no skill file at all. Without one, the model still
has the system prompt and the tool descriptions that accompany every call, and it can operate
on those alone. Recent studies of over ten thousand MCP servers confirm that the quality of
tool descriptions has a measurable impact on agent tool selection and argument passing [18, 19].
A bad skill file actively forces the model to pick tools and processes that do not match the user’s
pace or requests. This is why the skill file must be tailored to the specific user and their tasks.
The methodology for producing a correct skill file is: (1) build and validate the tool against
real data until the researcher confirms the outputs match their manual procedure, (2) observe
where the model makes wrong choices during interactive testing with realistic prompts, and (3)
write the skill to close those gaps. Testing follows the same principle: the researcher runs the
tool through the model on representative datasets and checks whether the model’s tool selection
and parameter choices match what they would have done manually. Mismatches are corrected
in the skill file and retested until the model’s orchestration is stable.
10

## Page 11

5 Evaluating Reproducibility
Models Evaluated.To test whether typed mediation eliminates result variance in practice,
we ran the same analysis on four platforms: (a) FORTHought, (b) GPT-5.5 with Extended
Thinking, (c) Claude Sonnet 4.6 with Adaptive Thinking, and (d) Gemini 3.1 Pro.
Evaluation Dataset and Workflow.We used the photoluminescence dataset from Section 4,
exported from the proprietary analysis software as a CSV file. Each platform received the same
file and the same natural-language prompt asking for fits across all power levels, extraction of
peak intensity and position for each power, and allometric fits of the resulting power dependence.
This is the typical workflow of an experimental scientist: export data from instrument software,
uploadtoanAIassistant, describethedesiredanalysisinplainlanguage. Nopromptengineering,
no parameter tuning, no specialized configuration. We ran each platform four times with no
modifications between runs.
Evaluation Setup.We use four runs as a repeatability check under identical inputs, prompts
and data. For the typed workflow, the analysis procedure is fixed in the tool, so repeated
execution should return the same result unless the implementation or input changes. For the
code-generating workflows, any change in fitting method, preprocessing step or numerical output
across repeated runs shows that the procedure is being reconstructed at regeneration time. This
is the risk we target: in scientific use, even one inconsistent rerun can affect which result a
researcher decides to trust.
Table 3: Reproducibility comparison across four platforms. Same dataset, same prompt, four
runs each. Intensitybis the exponent from the allometric fitI=aP b.
FORTHought GPT-5.5 Claude 4.6 Gemini 3.1
Valid results 4/4 4/4 4/4 0/4
Deterministic 4/4 0/4 0/4 0/4
b(range) 1.025 0.899–1.000 1.001–1.025 0.237 †
σb 0.000 0.041 0.010 —
Intensity spread<0.01% 54.8% 30.1% N/A
Avg. time/run 0:34 4:21 5:15 1:50
†FitR 2 = 0.005; centered on incorrect spectral region.
11

## Page 12

Figure 4: Reproducibility evaluation across four runs per platform. (a) Intensity exponentbfrom
the allometric power-law fit. Our platform produces the same value across all runs (σb = 0);
commercial platforms vary by an order of magnitude in spread. Gemini 3.1 returned values
clustered nearb≈0.24from invalid fits (R 2 = 0.005); the y-axis is broken to show this. The
dotted line marks the reference value from the researcher’s own analytical procedure. (b) Time
to completion, sorted by mean. Bars show mean across four runs, error bars show one standard
deviation, dots show individual runs. Gemini 3.1 produced no valid results despite finishing
fastest among commercial platforms.
12

## Page 13

Evaluation Results.Table 3 and Figure 4 summarize the results. We can see that:
•Our platform produced identical results across all four runs:b= 1.025withR 2 = 0.995.
The output files from two of the four runs were byte-for-byte identical. A third differed by
one digit in the fifth decimal place of a single coefficient due to floating-point arithmetic.
•GPT-5.5 produced valid outputs in all four runs but applied a different analytical proce-
dure each time. Run 1 identified one emission peak. Runs 2 through 4 identified two. The
background subtraction model changed between runs, with linear, quadratic and poly-
nomial variants appearing across the four runs. The intensity of the primary peak at
the lowest excitation power varied by 54.8% across runs. These differences do not repre-
sent numerical fluctuations around a stable methodology. Each run constitutes a different
experiment performed on the same data.
•Claude Sonnet 4.6 was qualitatively more consistent, always identifying one peak, though
in most runs it selected the wrong emission feature rather than the primary peak. The fit
window varied from 122 to 145 nm across the four runs, with no two runs using the same
bounds. Intensity values at shared power levels disagreed by up to 30.1%.
•Gemini 3.1 Pro failed on all four runs. Every run missed a required preprocessing step
(axis unit conversion in the exported data) and produced fits withR2 ≈0.005centered on
incorrect spectral regions.
All three commercial platforms were accessed through their respective paid subscription
plans with all available features enabled, including code execution environments and extended
context.
Our platform also completed each run in under one minute (mean 0:34), compared to 1:50–
5:15 for the commercial platforms, reflecting the absence of code generation overhead.
The typed tool does not encode the expected answer. It encodes one researcher’s analytical
procedure: which fitting model to use, what spectral window to fit over, what despiking param-
eters to apply. If the input data changes, the result changes, but the procedure stays the same.
An independent Lorentzian fit (deliberately different from the tool’s Voigt profile) of the same
dataset using a different spectral window and no despiking producesb= 1.036(R 2 = 0.997),
which differs from the tool’s output by∆b= 0.011, within the fit uncertainty of±0.027. The
value ofbdepends on methodology. What the typed tool guarantees is that the methodology
does not change between runs.
6 Concluding Remarks
In this paper (a) we proposed a typed-mediation pattern in which both the human and the
language model address the laboratory software via the same typed interface, placing the deter-
ministic core of the workflow in the tool rather than the model, (b) we presented two deployed
applications, ported through structured interview sessions with the researchers who own the
workflows, from a broader platform serving eleven active users over approximately six months,
(c) we evaluated reproducibility by running the same analysis on our platform and three com-
mercial foundation models and showed that the typed tool produces identical results across runs
(σb = 0) while the commercial platforms vary in both numerical output and analytical method-
ology on every run, and (d) we argued that deployment topology is a structural requirement of
scientific tool mediation, driven by both privacy concerns and the licensing constraints of most
laboratory software, which together force the tool to live alongside the data and the instrument
it operates.
In the primary case, a photoluminescence analysis workflow that previously required approx-
imately two weeks of manual processing per measurement campaign now executes in minutes
13

## Page 14

and produces identical results across runs. In the second case, a scanning electron microscopy
workflow for periodic structure analysis is now used by three researchers with calibration-checked
results. The researcher who owns the PL workflow has used it in over sixty sessions across six
months of continuous operation.
The evaluation in this work is limited to one dataset, one instrument workflow and one
set of commercial platforms at a single point in time. We do not claim that code-generating
approaches are inherently incapable of reproducibility, only that they did not achieve it on this
task under standard usage conditions.
Applicability.In general, the proposed approach is appropriate for multi-step analyses where
apart from the result we would like to have reproducibility. The approach is most valuable when-
ever the task involves tooling and the methodology, if performed incorrectly, produces silently
wrong results. Modern language model deployments are almost never tool-free, even baseline in-
terfaces provide web search, code execution and file handling. The relevant boundary is therefore
not between tool-assisted and tool-free tasks, but between tasks where the methodology should
be fixed and tasks where variation is acceptable. Typed mediation offers diminishing returns
for tasks that are inherently exploratory (the researcher has not yet settled on a procedure to
encode), tasks where generic tool use is already consistently correct, and tasks where approxi-
mate results are sufficient. It is most valuable where a non-trivial analytical procedure must be
executed identically every time, which describes the majority of instrument-driven experimental
workflows.
Issues for further work and research include: (i) extending the evaluation to additional
datasets and instrument types, including a user study measuring task completion time and error
rates with and without typed mediation, (ii) extending the pattern to additional instrument
classes and evaluating cross-institutional deployment, and (iii) investigating how the interview-
driven encoding process itself can be partially automated as the number of ported workflows
grows.
14

## Page 15

References
[1] Horace He and Thinking Machines Lab. Defeating nondeterminism in LLM inference,
September 2025. Connectionism blog.
[2] Miles McCain, Thomas Millar, Saffron Huang, Jake Eaton, Kunal Handa, Michael Stern,
Alex Tamkin, Matt Kearney, Esin Durmus, Judy Shen, Jerry Hong, Brian Calvert, Jun Sh-
ern Chan, Francesco Mosconi, David Saunders, Tyler Neylon, Gabriel Nicholas, Sarah Pol-
lack, Jack Clark, and Deep Ganguli. Measuring AI agent autonomy in practice, February
2026.
[3] John R. Kitchin. The evolving role of programming and LLMs in the development of
self-driving laboratories.APL Machine Learning, 3(2):026111, 2025.
[4] Simone Balloccu, Patrícia Schmidtová, Mateusz Lango, and Ondřej Dušek. Leak, cheat,
repeat: Data contamination and evaluation malpractices in closed-source LLMs. InProceed-
ings of the 18th Conference of the European Chapter of the Association for Computational
Linguistics. Association for Computational Linguistics, 2024.
[5] Thorsten Hellert, Drew Bertwistle, Simon C. Leemann, Antonin Sulc, and Marco Venturini.
Agentic artificial intelligence for multistage physics experiments at a large-scale user facility
particle accelerator.Physical Review Research, 8:L012017, 2025.
[6] Aikaterini Vriza, Michael H. Prince, Tao Zhou, Henry Chan, and Mathew J. Cherukara.
Operating advanced scientific instruments with AI agents that learn on the job.npj Com-
putational Materials, 2026.
[7] Yong Xie, Kexin He, and Andres Castellanos-Gomez. Toward full autonomous laboratory
instrumentation control with large language models.Small Structures, 2026.
[8] Abdoulatif Cissé, Max E. Cooper, Mengjia Zhu, Xenophon Evangelopoulos, and Andrew I.
Cooper. Can we automate scientific reasoning in closed-loop experiments using large lan-
guage models?Digital Discovery, 5:1132–1160, 2026.
[9] Jiaxin Cui and Rohan Alexander. Same prompt, different outcomes: Evaluating the repro-
ducibility of data analysis by LLMs. 2026. Preprint.
[10] Chen Yang, Xianyang Zhang, and Jun Chen. ChatSpatial: Schema-enforced agentic orches-
tration for reproducible and cross-platform spatial transcriptomics.bioRxiv, 2026. Preprint.
[11] Yiqing Xu and Leo Yang Yang. Scaling reproducibility: An AI-assisted workflow for large-
scale replication and reanalysis. 2026. Preprint.
[12] Haochen Pan, Ryan Chard, Reid Mello, Christopher Grams, Tanjin He, Alexander Brace,
Owen Price Skelly, Will Engler, Hayden Holbrook, Song Young Oh, Maxime Gonthier,
Michael Papka, Ben Blaiszik, Kyle Chard, and Ian Foster. Experiences with model context
protocol servers for science and high performance computing. 2025. Argonne National
Laboratory / Globus. Preprint.
[13] Joel Strickland, Arjun Vijeta, Chris Moores, Oliwia Bodek, Bogdan Nenchev, Thomas
Whitehead, Charles Phillips, Karl Tassenberg, Gareth Conduit, and Ben Pellegrini. Talk
freely, execute strictly: Schema-gated agentic AI for flexible and reproducible scientific
workflows, March 2026. Preprint.
[14] Aarya Doshi, Yining Hong, Congying Xu, Eunsuk Kang, Alexandros Kapravelos, and Chris-
tian Kästner. Towards verifiably safe tool use for LLM agents. InProceedings of the 2026
15

## Page 16

IEEE/ACM 48th International Conference on Software Engineering: New Ideas and Emerg-
ing Results (ICSE-NIER ’26), pages 1–5, Rio de Janeiro, Brazil, April 2026. ACM.
[15] Han Deng, Anqi Zou, Hanling Zhang, Ben Fei, Chengyu Zhang, Haobo Wang, Xinru Guo,
Zhenyu Li, Xuzhu Wang, Peng Yang, Fujian Zhang, Weiyu Guo, Xiaohong Shao, Zhaoyang
Liu, Shixiang Tang, Zhihui Wang, and Wanli Ouyang. Owl-AuraID 1.0: An intelligent sys-
tem for autonomous scientific instrumentation and scientific data analysis. 2026. Preprint.
[16] Anthropic. Introducing the model context protocol, November 2024.
[17] Zhuo Diao, Kouma Matsumoto, Linfeng Hou, Masahiro Ohara, Hayato Yamashita, and
Masayuki Abe. Integrating domain-specialized language models with AI measurement tools
for deterministic atomic-resolution experimentation, February 2026. Preprint.
[18] Mohammed Mehedi Hasan, Hao Li, Gopi Krishnan Rajbahadur, Bram Adams, and
Ahmed E. Hassan. Model context protocol (MCP) tool descriptions are smelly! towards
improving AI agent efficiency with augmented MCP tool descriptions. 2026. Preprint.
[19] Peiran Wang, Ying Li, Yuqiang Sun, Chengwei Liu, Yang Liu, and Yuan Tian. From docs
to descriptions: Smell-aware evaluation of MCP server descriptions. 2026. Preprint.
A An Example Skill Document for SEM Periodicity Analysis
Below is a lightly edited excerpt from the skill document for the SEM periodicity tool (Section 4).
The model reads this document before interacting with the tool. Parameter names, types, and
constraints constitute the typed schemaSthrough which the model’s output is channeled.
SEM Analysis — Periodicity & Particle Sizing
Workflow
1. Read magnification from the SEM info bar (e.g.x40000).
2. Identify the uploaded file from its metadata.
3. Decide analysis type: periodicity, particle sizing, or both.
4. Call the tool with exact parameters.
5. Present results with embedded figures.
Analysis Type Selection
User requestparticle_analysis
Periodicity, spacing, LIPSS, FFT omit (defaultfalse)
Particle/grain size, distributiontrue
General “analyze this”true(runs both)
Tool Invocation
Periodicity only:
run("sem_fft", {
"file_id": "<UUID>",
"mag_label": "x40000"
})
With particle sizing:
run("sem_fft", {
"file_id": "<UUID>",
"mag_label": "x40000",
"particle_analysis": true
})
Schema Constraints — Exact Parameter Names
16

## Page 17

Parameter Type Rejected aliases
file_idstring (UUID)image_id,id
mag_labelstringmagnification,mag
particle_analysisbooleananalyze_particles
Extra parameters (crop_bottom_px,roi,preset) are not accepted unless the user explicitly requests
them. The schema rejects any invocation that does not match these exact names and types.
The document instructs the modelwhat to observe(Step 1: read magnification),how to decide
(the analysis-type table), andhow to call the tool(exact parameter names and types). The
model cannot bypass the schema: a call withmagnificationinstead ofmag_labelis rejected.
This is the mechanism by whichx∈ Xis enforced at runtime.
B Structured Interview Excerpt
The workflow encoded in each typed tool was extracted through structured interviews with the
researcher who owns the procedure. Below we list a representative subset of the thirty questions
used in the photoluminescence case (Section 4). Each question targets one analytical decision.
In several cases the answer contradicted the assumption we had implemented, requiring the tool
to be corrected before deployment.
Q1.What fitting profile do you use for the emission peak?
Answer:Voigt.
Impact:We had implemented Lorentzian. Changed to Voigt with free Gaussian and Lorentzian widths.
Q2.Is the fitting window fixed across all excitation power levels?
Answer:No. Wider at high power, narrower at low power to avoid fitting noise in the wings.
Impact:We had used a single fixed window. Changed to adaptive windows.
Q3.What is your R2 quality threshold for accepting a fit?
Answer:Approximately 0.90, evaluated visually by overlaying the fit on the data.
Impact:We had implemented a strict 0.95 cutoff. Relaxed to 0.85 to match real practice.
Q4.How do you extract peak intensity?
Answer:Screen reader — cursor placed on the peak maximum, raw counts read directly. Not from the
integrated area under the fit.
Impact:We had used integrated fit area. Changed the extraction metric to peak height.
Q5.Do you fit a single power law across the full excitation range?
Answer:No. Two separate allometric fits (I=aP b), split at a saturation boundary near∼10µW.
Impact:We had implemented a single fit. Added split fitting with configurable boundary.
Q6.Do you apply smoothing to the spectra before fitting?
Answer:No smoothing. Fits are performed on raw background-subtracted data.
Impact:Confirmed. We had not implemented smoothing, but had considered adding it.
Q7.Do you exclude outlier points from the power-law fit?
Answer:No. All surviving fit results are plotted and fitted as-is.
Impact:We had implemented sigma-clipping outlier rejection. Removed it.
Q8.Do you propagate fit parameters from one power level to the next as initial guesses?
Answer:No. Each spectrum is fitted independently from scratch.
Impact:We retained cascade seeding as an internal optimization (improves convergence) but ensured it
does not change the result.
Each answer encodes a methodological decision that, if guessed incorrectly, changes the nu-
merical output. The full set of thirty questions covered preprocessing (background subtraction,
cosmic ray removal), model selection, quality control, parameter extraction, and post-processing.
The resulting workflow specification was validated against the researcher’s own manual results,
achieving∆≤0.02on the power-law exponentb.
17
