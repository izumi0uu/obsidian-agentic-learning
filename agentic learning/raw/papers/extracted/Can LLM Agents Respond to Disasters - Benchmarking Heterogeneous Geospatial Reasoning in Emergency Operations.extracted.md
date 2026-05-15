# Can LLM Agents Respond to Disasters? Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations - Extracted Text

- Source note: [[Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations]]
- Source PDF: `assets/Can LLM Agents Respond to Disasters - Benchmarking Heterogeneous Geospatial Reasoning in Emergency Operations.pdf`
- Extracted: 2026-05-14
- Extractor: pypdf
- Pages: 13
- Quality note: 自动抽取为纯文本；公式、表格、图、脚注、参考文献和双栏阅读顺序可能有损失。精读引用仍需回到 PDF 页码 / section 校验。

## Page 1

Can LLM Agents Respond to Disasters?
Benchmarking Heterogeneous Geospatial Reasoning
in Emergency Operations
Junjue Wang1∗, Weihao Xuan1,2∗, Heli Qi2,3, Pengyu Dai1,2, Kunyi Liu3, Hongruixuan Chen1,
Zhuo Zheng4, Junshi Xia2, Stefano Ermon4, Naoto Yokoya1,2†
1The University of Tokyo,2RIKEN AIP,3Waseda University,4Stanford University
*Equal Contribution†Corresponding Author
Abstract-Operational disaster response goes beyond damage assessment, requiring responders to integrate multi-sensor signals,
reasonoverroadnetworks, populationsandkeyfacilities, planevacuations, andproduceactionablereports. However, priorwork
largelyisolatesremote-sensingperceptionorevaluatesgenerictooluse,leavingtheend-to-endworkflowsofemergencyoperations
underexplored. Inthispaper,weintroduceDisasterOperationalResponseAgentbenchmark(DORA),thefirstagenticbenchmark
for end-to-end disaster response: 515 expert-authored tasks across 45 real-world disaster events spanning 10 types, paired with
expert-verified, replayable gold trajectories totaling 3,500 tool-call steps. Tasks span five dimensions that cover the operational
disaster-response pipeline: disaster perception, spatial relational analysis, disaster operational planning, temporal evolution rea-
soning,andmulti-modalreportsynthesis. Agentscomposecallsfroma108-toolMCPlibraryoverheterogeneousgeospatialdata:
optical,SAR,andmulti-spectralimageryacrosssingle-,bi-,andmulti-temporalsequences(0.015–10mGSD),complementedby
elevation and social vector layers. We comprehensively evaluate 13 frontier LLMs on our benchmark, revealing three persistent
challenges: 1)disaster-domaingroundingexposesuniquefailuremodes(damage-semanticgrounding,sensor-modalitymismatch,
anddisaster-pipelinecomposition);2)agentsaredoublybottleneckedbytoolselectionandargumentgrounding,wheregoldtool-
orderhintsimproveaccuracybyonly1.08–4.40%,andalternativescaffoldsyieldatmosta3.24%gain;3)compositionalfragility
scales with trajectory length, the agent-to-gold gap widening from 7% to 56% on long pipelines. DORA establishes a rigorous
testbed for operationally reliable disaster-response agents.
Keywords:disaster response, LLM agents, geospatial reasoning, remote sensing, benchmark
1. Introduction
Natural and man-made disasters (earthquakes, floods, hurricanes, landslides, and explosions) claim tens of thousands of lives
annuallyandinflicthundredsofbillionsofdollarsininfrastructuredamage[1,2]. Effectivedisasterresponserequirescompound
analytical capabilities: perceiving damage from heterogeneous sensor data, reasoning about spatial relationships among affected
assets, estimating operationalresources under real-worldconstraints, tracking disasterevolution over time, andsynthesizing find-
ings into actionable reports. These tasks cannot be addressed by visual inspection alone but demand the tight integration of
multi-sensor remote sensing (RS) imagery, social geospatial vector data, domain-specific analytical tools, and multi-step compo-
sitional reasoning.
RecentadvancesinLLM-basedagentshavedemonstratedstrongcapabilitiesinmulti-steptooluse,compositionalreasoning,
and long-horizon task execution across general-purpose domains (web browsing, code generation, database querying, etc.) [3–5].
These developments have also begun to push the boundaries of remote sensing applications: agents can now automate geospatial
workflows [6–8], answer multi-step queries over satellite imagery with specialized tools. However, disaster operations uniquely
combineheterogeneousdatafusion,longcompositionalpipelines,anddisaster-specificknowledgegroundingthatprioragentand
RS benchmarks rarely test together, leaving the full operational pipeline of disaster response largely unexplored. To this end,
we introduce DORA, a disaster agent benchmark grounded in 45 real-world disaster events that systematically evaluates state-
of-the-art LLM agents across diverse disaster scenarios, providing a reliable AI platform for advancing humanitarian efforts in
emergency response.
arXiv:2605.11633v1  [cs.AI]  12 May 2026

## Page 2

Geoscience (POI, DEM, Slope, etc.) Remote Sensing (Optical, SAR, Multi-spectral)
DEM/Slope
Q1: Estimate the area of the largest damaged 
building and tell me its social function.
GSD 60cm / Beirut explosion in Lebanon
Optical SAR
damaged building seg.
building mask
vectorize
damaged list
ranking largest#1
POIs
social attributes
Answer: The largest 
damaged building is a 
131 𝑚2 warehouse.
Optical 
Multi-spectral
Slope
DEM
GSD 10m / Nepal Landslide
Q2: For risk estimati-
on, please calculate 
landslide area within
50m of the reservoir.
data fusion
fused image
detect water
detect landslide
water mask
landslide mask
vectorize
lands. poly.
water. poly.
buffer fuc.
lands. poly.
intersected?
Answer: 
242𝑚2
Vector Layer
OpenStreetMap
Q4: With Wako Kindergarten collapsed, find the shortest 
undamaged road from here to the nearest hospital or clinic.
Q3: How long to clear this debris with the available 
cars in this scene? Each car clears 10m² per hour. 
car det.
car polygons
available 
counting
area counting
number
debris
calculate
Answer: 49h
GSD 10cm / Hurricane Michael in U.S GSD 80cm / Noto Earthquake in Japan
Wako 
Kindergarten
Point of Interest
Name Beirut Port Grain Silos
Type Warehouse
Long. 35.52°E
Lat. 33.90°N
Funaki Clinic
Nakagishi Orthopedic Clinic
Nadogaya Memorial Hospital
Optical Optical 
 damaged road seg.
POIs Hospitals
Wako
find [Hospital]
find [Wako Kind.]
extract centerline
centerlines build road graph road graph
Hospitals Wako
find the nearest intact road 
Answer: Nakagishi Orthopedic Clinic is the
nearest hospital, and the shortest intact 
path is 696m and stored in path.geojson
intact paths
min dis.
road mask
+
+
+
loop
GSD 60cm / Flooding in U.S
Q: Determine how many 
buildings were submerged at 
the peak of the flood.
Optical 𝒕𝟏
damaged building seg.
damaged road seg.
flooding seg.
loop by timestamp
aggregated results
line chart drawing
POIs
𝒕𝟐
 𝒕𝟓
𝒕𝟑 𝒕𝟒
summarize
line chart for 
flooding areas
grounding building 
pixels with POIs
report synthesisbuilding 
damage details
Answer 
At t2, floodwaters began to submerge the 
central area, affecting three restaurants. By t3, 
nearly the entire area was inundated, impacting 
five restaurants, two convenience stores, and 
one hospital. At t4, the flooding reached its 
peak, after which the water gradually receded. 
Two northeastern restaurants were the first …
Flooding process report
1.5cm-10cm 30cm-80cm
 80cm–1.2m
 10m
Visual Spectrum SAR Multi-Spectrum
sample
T1: Disaster Perception and Assessment T2: Spatial Relational Analysis
T3: Disaster Operational Planning
T4: Temporal Evolution Reasoning
flooding seg.
loop by timestamp
aggregated results
temporal argmax
𝒕𝟏
damaged building seg.
building mask
Answer: At peak 𝒕𝟒, 108
buildings were submerged.  
connectivity area count
T5: Multi-modal Report Synthesis
Population
Q:Mapping the area changes in the flooding process with a line chart and reporting the affected key building facilities following the timeline.
𝒕𝟒
Figure. 1. Representative task examples in DORA across different disaster operational categories. Each example illustrates the
heterogeneous data inputs and multi-step tool chains required to produce concrete, decision-ready outputs.
To comprehensively evaluate LLM agents with diverse disaster-response capabilities, we organize tasksintofive comple-
mentary analytical dimensions that collectively span the information-processing demands of disaster intelligence: 1) disaster
perception and assessment, 2) spatial relational analysis, 3) disaster operational planning, 4) temporal evolution reasoning, and
5) multi-modal report synthesis. A single disaster scenario may simultaneously require capabilities from multiple dimensions,
and each dimension exercises a distinct combination of tools, reasoning patterns, and data modalities. This design ensures that
DORA measures not merely whether an agent can invoke individual tools, but whether it cantranslateoperational knowledge
intoexecutabletoolpipelines: selectingtherighttools,composingtheminthecorrectorder,andinterpretingintermediateoutputs
to produce decision-ready results. Our main contributions are:
1. We introduce DORA, the first agentic benchmark for operational disaster response, comprising 515 expert-authored tasks
grounded in 45 real-world disaster sites spanning 10 disaster types (hurricanes, earthquakes, floods, wildfires, etc.), with
2

## Page 3

expert-verified gold trajectories totaling 3,500 tool-call steps across five complementary analytical dimensions from atomic
perception to multi-modal report synthesis.
2. Wedesignandreleaseapurpose-builtgeospatialMCPtoollibraryof108toolsorganizedintosixfunctionalmodules(percep-
tion,raster,vector,logic,visualization,summarization)coveringRSinterpretation,spatialcomputation,routing,POIquerying,
logistics estimation, and report generation, the most comprehensive disaster-specific tool ecosystem to date.
3. We benchmark 13 frontier LLMs through dimension-wise failure-mode, instruction-following, modality-stratified, trajectory-
length, and scaffolding analyses, surfacing three persistent challenges: disaster-domain grounding exposes unique failure
modes; agents are doubly bottlenecked by tool selection and argument usage (neither oracle tool-order hints nor alternative
scaffolds close the gap); and compositional fragility scales sharply with trajectory length, revealing concrete directions for
future disaster-response agent design.
2. Related Work
GeneralLLMAgents.AkeychallengeinbuildingLLMagentsisclosingtheloopbetweenreasoningandexecution,motivating
work on planning, self-correction, and experiential learning. ReAct [9] establishes the core paradigm of interleaving reasoning
traces with environment actions, enabling dynamic planning within a single inference loop. ExpeL [10] extends this with experi-
entiallearningbyextractinginsightsfromaccumulatedtrajectories,andAutoGuide[11]generatescontext-awareguidelinesfrom
offline experiences to steer agents in unfamiliar domains. More recently, ReasoningBank [12] distills generalizable reasoning
strategies from self-judged outcomes, enabling agents to self-evolve across task streams. To systematically measure these capa-
bilities,WebArena[13],OSWorld[14],andAgentBench[5]benchmarkwebnavigation,desktopcontrol,andmulti-environment
digitaltasks,whileSWE-bench[15],OctoBench[16],andFeatureBench[17]targetsoftware-engineeringworkflows. GAIA[18]
furtherprobesgeneralassistantsonmulti-steptool-usetasks. Unlikethesebenchmarksoperatingindigitalenvironments,DORA
evaluates LLM agents on real-world disaster response, where heterogeneous geospatial data, domain-specific tool orchestration,
and operational decision-making collide in a single task.
Table 1. Comparison of DORA with representative agent benchmarks.
Benchmark Domain #Tasks #Tools #Modality GSD(m) Annotate Temporal Eval Level Avg Steps
GAIA [18] General QA 466 – 2 – Human – Final –
GTA [19] General tools 229 14 2 – Human – Step+Final 2.4
m&m’s [20] Multi-modal 4K+ 33 2 – Auto – Step+Final 2.7
WebArena [13] Web navigation 812 – 2 – Human – Execution –
AgentBench [5] Digital envs 8 envs – 2 – Human – Execution –
GeoLLM-Engine [21] Geospatial 500K+ 175+ 1 0.5–30 Auto 1 Final 5.2
ThinkGeo [22] Remote sensing 486 14 2 0.1–30 Human 1+2 Step+Final 3.6
UniVEarth [23] Remote sensing 140 – 1 15-1000 Human 1 Final –
Earth-Agent [6] Remote sensing 248 104 3 0.3–10 Human 1+N Step+Final 5.4
OpenEarthAgent [7] Remote sensing 1169 28 4 0.1–30 LLM+Valid. 1+2 Step+Final 6.0
DORA (Ours) Disaster ops. 515 108 8 0.015–10 Human 1+2+N Step+Final 6.8
Earth observation LLM Agents.Early RS agents treat LLMs as orchestrators of specialized visual models: RS-Agent [24] in-
vokes RS models for multi-step interpretation, and Change-Agent [25] focuses on bi-temporal change analysis with LLM-driven
captioning. GeoLLM-Engine [21] offers a realistic copilot environment reflecting analyst workflows, and ThinkGeo [22] intro-
duces a 486-task RS benchmark under a ReAct-style loop. UniVEarth [23] grounds queries in Google Earth Engine API calls,
while Earth-Agent [6] and OpenEarthAgent [7] couple multi-step reasoning with executable tools. However, these rely on gen-
eral geospatial datasets, LLM-synthesized queries, and general-purpose toolsets, missing the operational complexity of disaster
response. Disaster-specificperceptionresources like xBD [26] and DisasterM3 [27] supply expert-verified damage masks and
single-step VQA benchmarks. DORA reuses their imagery but advances evaluation from perception and short-form QA to end-
to-end operational reasoning: agentscomposeheterogeneous tools across perception, routing, logistics, and synthesis to produce
operationallyactionableoutputs(rescueroutes, resourceallocations, multi-modalbriefings)beyondanysingleperceptionmodel.
DORA exposes three disaster-critical competencies untested elsewhere (Fig. 7): 1)cross-modal reasoning, i.e., choosing opti-
cal, SAR, vector, or DEM under cloud, night, or terrain constraints, appears in 28.7% of DORA tasks versus<3% in prior RS
3

## Page 4

benchmarks. 2)damage-semantic grounding(e.g., flood vs. landslide debris, collapsed vs. flooded buildings) is the dominant
failuremode(20.3%)forfrontierLLMs. 3)disasterpipelinecompositionaccountsfor56.3%oferrors,whichstemfrompipeline
structure rather than individual tool misuse.
3. DORA Dataset
3.1. Data source overview
As shown in Fig. 2, we broadly collect open-source disaster imagery and geospatial resources to ensure diversity in disaster
types,sensormodalities,andgeographiccoverage. High-resolutionopticalpre-andpost-disastersatelliteimagepairsaresourced
from the xBD dataset [26] (covering hurricanes, earthquakes, wildfires, volcanic eruptions, floods, tsunamis, and tornadoes),
complemented by optical–SAR pairs from DisasterM3 [27] and BRIGHT [28]. For multi-temporal sequences, we newly collect
flood progression and post-disaster reconstruction scenes spanning 3–5 observation phases from NAIP [29] and the Maxar Open
Data Program [30]. For multi-spectral terrain scenes, Landslide4Sense [31] and GVLM-CD [32] provide composites with DEM
and slope layers, further complemented by Planet imagery for urban flood risk analysis. For aerial imagery, we incorporate
RescueNet [33] and CRASAR-U-DRoIDS [34] for fine-grained disaster scene analysis. For heat-island analysis, land surface
temperature and digital surface models are drawn from OpenEarthMap [35] and the Japan Meteorological Agency [36]. Co-
registered social geospatial layers come from OpenStreetMap [37] and Our World in Data [38], including POIs, road networks,
population rasters, and facility footprints.
.
-0.6
.
-5
120°W 60°W 0° 60°E 120°E 180°
60°N30°N0°30°
60°N30°N0°30°
120°W 60°W 0° 60°E 120°E 180°
fire (4)
tornado (4)
earthquake (4)
explosion (1)
tsunami (1)
volcano (4)
hurricane (5)
flooding (6)
landslide (15)
heat island (1)
Disaster legend
xbd
xbd
xbd
xbdxbd
dm3
dm3 dm3
dm3
bright
bright
gvlm
gvlm
gvlmgvlm
gvlmgvlm
gvlm
rescue
planet
new-heat
new-mt
new-mt
new-mt
ls4 ls4
Task count by disaster type
0
50
100 97 91
5354 49 47 4345
20 16
crasar
Opt.-Aerial Opt.-Satellite SAR Multi-Spe.
new-heat
rescue
crasar dm3 xbd
planet new-mt
gvlm dm3
bright
ls4
1.5cm-10cm 30cm-80cm 0.8m-1.2m
 10m
xbd dm3/
bright gvlm rescue/
crasar planet ls4 new-
heat
new-
mt
Opt. ○ ○ ○ ○ ○ ○ ○
SAR ○
Multi-
Spe. ○
DEM/
Slope ○
DSM/
LST ○
Social ○ ○ ○ ○ ○
Phase 2 2 2 1 1 1 1 3-5
Abbreviations: rescue (rescuenet), crasar (CRASAR-U-
DRoIDS), dm3 (disasterm3), ls4 (landslide4sense), new-heat 
(new-heatisland), new-mt (new-multi-temporal), LST (land 
surface temperature)
Figure. 2. DORA aggregates multi-modal data from 10 open-source databases into 45 disaster events distributed across five
continents, including 2,850 remote sensing images, 460 vector layers and 515 expert-designed tasks across 10 disaster types.
‘new’ denotes our self-constructed samples.
3.2. Agent tasks in the context of disasters
Task formulation.As shown in Fig. 3, each DORA task is defined as a tuple(Q,D,T∗,A∗).Qis a natural-language query
grounded in an operational need.Dis aheterogeneous data manifestthat bundles georeferenced raster layers across optical,
SAR, and multi-spectral modalities (with metadata on modality, pixel size, coordinate reference system, band specification, etc.)
alongside social geospatial vector layers (POIs, road networks, facility footprints) in GeoJSON format.T∗=⟨𝑡 1, . . . , 𝑡𝐾⟩is the
expert-verified gold tool-call trajectory, andA∗is a structured JSON final answer whose fields (apart from rendered visualiza-
tions) fall into seven typed categories:scalar(count, area, ratio),string(damage grade, disaster type),point(epicenter, target
location),line(shortest-path route),polygon(damage extent, flood boundary),set(affected facilities, buildings), anddict(per-
phasestatistics,compositesituationreports). Atinferencetimetheagentobservesonly(Q,D)andmustautonomouslycompose
the correct tool chain from the 108-tool library (§3.3) to produceA.
Analyticaldimensions.Fig.4classifiesthe515tasksintofivetaskdimensions,eachwithadistincttool-usageprofile,reasoning
pattern, and output modality. This taxonomy is motivated by two rationales.Substantively, the five dimensions mirror canonical
stages of geospatial information processing (damage perception, spatial modeling, decision support, temporal analysis, and inte-
4

## Page 5

Raster (*.tif, *.png) Vector (*.geojson)
Meta data (*.json)
𝑡1 𝑡2 𝑡3
opt
sar
{
  sample_id: "beirut_explosion1",
 question (𝒬): “How many intact hospitals 
situated within 800 m of the Beirut Port 
Grain Silos explosion site's center.“,
input_data (𝒟): {
pre_image: {
  image_path: "pre_disaster1.tif",
modality: "optical",
  GSD_m: 0.8,
  coordinate_system: "WGS84",
  band: ["R", "G", "B"] },
  post_image: {
  image_path: "post_disaster1.tif",
  modality: "SAR",
  GSD_m: 0.8,
  coordinate_system: "WGS84",
  band: "intensity"},
  poi_data: {
  path: "poi.geojson"},
  …..},
  trajectory (𝒯): {[{
  call: "poi.search_by_name",
  args: {
  geojson_path: "poi.geojson",
      name: "Beirut Port Grain Silos"},
  obs: {
  latitude: 33.9009381,
longitude: 35.5182691,
  type: “establishment", …}
  ],
 answer (𝒜): 5,
}
point
line
polygon
Figure.3. EachsampleisstoredasaJSONmetafilelinkingthequery(Q),
heterogeneous input data (D, rasters and vectors), tool-call trajectory (T),
and final answer (A).
T4
Temporal Evolution 
Reasoning
61
17
38
23
14
 DORA
515 tasks
45 disasters
other
Figure. 4. Distribution of 515 tasks across five an-
alytical dimensions (inner ring) and disaster types
(outer bars).
grated reporting), each recognized as a distinct operational need by international disaster-response frameworks (UNOSAT [39],
Copernicus EMS [40], FEMA ICS [41], UN OCHA [42]).Methodologically, each dimension isolates a progressively more
demandingagentcapability: atomictoolinvocationandoutputparsing(T1);toolcompositionwithspatialsemantics(T2);opera-
tionalknowledgegrounding(T3);temporalabstractionanditerativestatetracking(T4);andcross-modalsynthesiswithstructured
generation(T5). Thiscapabilityhierarchymanifestsasincreasingtrajectorylengthandbroadeningtool-categorycoverageacross
T1–T5 (Fig. 5(a)).
0
2
4
6
8
10
12
14
T1 T2 T3 T4 T5
Average Tool Calls per Task
Perception Tools
Raster Tools
Vector Tools
Logical Tools
Visualization Tools
Summarization Tools
8.5
13.32
3.35
5.625.58
9.58
11.96
T1: Disaster Perception and 
Assessment
T2: Spatial Relational Analysis T3: Disaster Operational Planning
T4: Temporal Evolution Reasoning T5: Multi-modal Report Synthesis
image
POIs
raster
results
Answer:[scaler]
perception
filter_by
image
 perception
1
raster
1
vectorize
1
image
 perception
2
raster
2
vectorize
2
poly buffer_result
poly
1 1
buffer
1
2
intersect
Answer:[polygon]
3
1 1
1 1
image
POIs
path_search
perception
1
raster
 centerline_ext
1 1
3
paths
argmin
3
vectorize
cons_graph graph
1
results
2
poi_search
2
Answer:[line]
3
vector
1 1
image_t1
image_t2
image_t3
image_t4
vectorize
raster
perception
poly polygon_list
sub-pipeline
reduce
loop
gather_datadam_area_list Answer:[list]
1
1
1 1 1
image
 perception raster
 dam_count statistics
cons_graph path
raster
 centerline_ext vector
perception
graph
 shortest_path
pie_chart
routine_map
Answer:[report]statistics
chart
map
chart
map
text
summarize
 vis_report
1 1 1 1 1
12 2 2 2
2 2 2 2
2 2
3 3
3
3
3 3
(a) Average tool calls per task across the five task dimensions. (b) Representative tool-call trajectories for each task dimension.
Figure. 5. Complexity and tool-usage profiles across DORA’s five dimensions. (a) Trajectory length grows from3.35(T1) to
11.96steps (T5), with distinct tool-category distributions per dimension. (b) Representative trajectories show the progression
from linear perception chains (T1) to full-stack report synthesis (T5); node colors match (a).
Task Taxonomy.Fig. 5 (b) shows some representative trajectories for each dimension, respectively.
T1: Disaster Perception & Assessment (PA).T1 covers atomic geospatial quantification from single- or bi-temporal imagery.
Typical tasks extract damaged areas, building counts, or debris volumes viaperceptionandrastertools. More complex
instances cross-reference perception outputs with POI records to assess damage at specific facilities (e.g., “how many hospitals
fall within the severe-damage zone”), following UNOSAT rapid structural damage grading products [39].
5

## Page 6

T2: Spatial Relational Analysis (SR).T2 requires composing multiple perception and GIS tools across data layers with explicit
spatialsemanticssuchasproximity,containment,andoverlay,followingthemulti-layerexposureanalysisinFEMA’sHazusframe-
work [43]. A representative pattern first segments two thematic layers independently (e.g., lava extent and building footprints),
vectorizeseach,thenappliesbufferandintersectionoperationstoanswerquerieslike“identifyintactbuildingsthatliewithin100
m of the lava flow boundary.”
T3: Disaster Operational Planning (OP).T3 translates geospatial outputs into actionable resource allocation, logistics, or route
planning decisions, invokinglogicaltools and probing operational knowledge under domain-specific constraints (clearance
rates, vehicle capacities, shortest accessible routes), following following FEMA’s Urban Search and Rescue System [41].
T4: Temporal Evolution Reasoning (TE).T4 tracks disaster dynamics across 3–5 observation phases (e.g., flood progression,
wildfirespread,orpost-disasterreconstruction)byiterativelyinvokingthesameanalyticalsub-pipelineperphaseandaggregating
cross-phase results to identify trends, peaks, and phase transitions, following Copernicus EMS Monitoring products [40].
T5: Multi-modal Report Synthesis (RS).T5 integrates capabilities from T1–T4 and additionally requiresvisualizationand
summarizationtools to produce situation reports with damage maps, trend charts, and narrative summaries, following UN
OCHA reporting standards [42]. T5 yields the longest average trajectories in the benchmark.
3.3. Tool library
DORA provides a library of 108 MCP-compliant tools spanning six functional categories (Table 2): 1)Perception, semantic
segmentationmodelsforbuildings,roads,floods,landslides,lava,vehicles,andotherdisaster-relevantobjectsfromoptical,SAR,
ormulti-sensorimagery. Thesesegmentationmodelsweretrainedonpublicdatasets(xBD[26],DisasterM3[27],BRIGHT[28],
GVLM [32], RescueNet [33], etc) or borrowed from the challenge champion solutions (Landslide4Sense [31], SpaceNet-7 [44]).
To prevent data leakage,we train all perception tools only on the publictrainingsplits and construct DORA tasksexclusively
from the held-outtestsplits. 2)Raster: pixel-level operations including area, zonal statistics, thresholding, grid windowing,
and vectorization. 3)Vector: geometric operations such as buffering, intersection, connected-component analysis, POI query-
ing, and graph-based path routing. 4)Logical: control-flow primitives (logi.loop, logi.reduce, logi.truck_trips) that enable
iterativereasoninganddomain-specificplanning. 5)Visualization: maprendering, charting, andmulti-panelreportlayout.
6)Summarization: fixed report-generation tools for evidence extraction and narrative rendering, shared by all agents as part
of the environment. All tools are implemented as MCP servers, exposing a uniform JSON-RPC interface with typed input and
outputschemas. Thisdesigndecouplestoolimplementationfromagentlogic,allowinganyMCP-compatibleagentframeworkto
be evaluated without modification. Tool implementation details and perception model accuracies are reported in Appendix § C.
Table 2. Overview of the DORA tool library.
Category # Scope Representative Tools Output Implementation
Perception31 Semantic segmentation of
disaster-relevant objects
seg.building_damage, seg.flood,
seg.road_damage Raster mask DinoV3, SegFormer,
HRNet, SwinUperNet
Raster18 Raster algebra and conversion ras.area, ras.diff, ras.vectorize scalar, polygon GDAL, Rasterio
Vector31 GIS operations, graph construction,
POI querying
vec.intersect, vec.shortest_path,
poi.filter_by_damage
scalar, point,
line, polygon
Shapely, NetworkX,
GeoPandas
Logical15 Control flow and planning logi.loop, logi.reduce decision Python
Visualization11 Map rendering and report layout vis.damage_map, vis.route_map,
vis.report_page image Matplotlib
Summarization2 Evidence extraction and rendering m.extract_evidence,
m.summarize text Fixed report backend
3.4. Annotation Pipeline
Buildingareliabletool-usebenchmarkrequiresground-truthtrajectoriesthatarebothsemanticallyfaithful(eachtoolcallreflects
a genuine analytical step) andnumerically grounded(observation values come from real ground truths). DORA’s construction
pipelineachievesthis throughathree-stageprocess illustratedinFig. 6.1) Experttaskdesign.Eachtaskis authoredbydomain
6

## Page 7

expertswithremote-sensinganddisaster-managementbackgrounds. GivenadisastersceneanddatamanifestD,theexpertwrites:
(i) a natural-language queryQgrounded in an operational need; (ii) a gold tool-call sequenceT∗ =⟨𝑡 1, . . . , 𝑡𝐾⟩specifying
each tool name, its purpose, and its input arguments. When an argument depends on a previous tool’s output, it is written as
a symbolic reference (e.g.,<mask_path> from trajectory[2].obs). This template-based design keeps the trajectory
logically complete and decoupled from any execution environment.2) Fill-the-blank execution.A deterministic replay engine
resolves all symbolic references and executes the trajectory. During annotation construction, perception calls are replaced by
human-annotated GT-mask lookups, while all downstream tools run normally to produce the curated reference answerA. This
GT-mask replay is used only for annotation and is never exposed to agents during evaluation.3) Quality control.We perform
systematiccross-validationoverquestion-answeralignment,eval-speccompleteness(zerounknown-typefields),andnumerical
sanity checks (Appendix § D).
4. Experiments
Evaluation Protocol.Following prior work [6, 19, 20, 45], we adopt a dual-level protocol covering both reasoning trajectory
and final answer.1) Trajectory metrics.Given goldT★ and predictedTpred trajectories, we report four measures [6]: Tool-
Any-Order (order-agnostic tool-set recall), Tool-In-Order (longest common subsequence of tool identifiers, normalized by|T★|),
Tool-Exact-Match (longest matching prefix length, normalized by|T★|), and Parameter Accuracy (per-step argument matching,
conditionedoncorrecttoolnames).2)Finalanswermetrics.TheseventypedfieldsofA ∗definedin§3.2reducetofouratomic
scoringoperators(Tab.3):scalarcloseness,normalizedstringexact-match,pointEuclidean-distancegate,andpolygonIoUgate.
Composite types inherit these atoms: adictaverages per-key scalar scores over the key union; asetis scored by F1 over string-
matched elements; alinedecomposes into start point, end point, and total length. For free-form𝑇5 summaries, we extract key
statistics and categorical labels for deterministic scoring. Since multiple trajectories can be valid, we treat final-answer metrics
as primary and trajectory metrics as diagnostic. We additionally adopt LLM-as-Judge and human scoring in Appendix § F.3)
Efficiency.Eff=|T ★|/max(|Tpred|,|T★|)∈(0,1]rewards agents that reach correct answers without redundant tool calls.
EvaluationMethodsWeevaluate13LLMsspanningcommercialmodels(GPT-5.4series[46],Claude-Sonnet-4.6[47],Gemini-
3.0-Flash [48], Grok-4.1 Fast [49]) and open-source models (Qwen3.5-series [50], MiMo-V2-Pro [51], Step-3.5-Flash [52],
DeepSeek-V3.2 [53], Gemma-4-31B [54], GPT-OSS-120B [55], MiniMax-M2.7 [56]). Two advanced vision-language models
(Qwen3-VL-235B [57] and Gemini-3.0 Flash [48]) receive the raw imagery and question without access to any tools, serving
as a tool-free baseline on visual reasoning. We also report Gold Trajectory that executes the expert-authored tool sequence. It
usesmodel-backedperceptiontoolsratherthanGTmasks,makingitaplanning-and-argumentoracleratherthanaperfect-answer
oracle. All agents are implemented under a ReAct-style [9] agent loop. In addition, we evaluate three alternative scaffolds (Plan-
then-Execute [58], Reflexion [59], and ReWOO [60]) to test mainstream agent paradigms. Implementation details are provided
in Appendix § E.
4.1. Benchmark results
DORA is challenging for all models.As shown in Tab. 4, even the strongest model, Gemini-3.0-Flash, achieves only 53.74%
average accuracy, 26% below the gold trajectory. The tool-free baselines Qwen3-VL-235B and Gemini-3.0-Flash without tools
confirmthatvisualreasoningalonecannotsubstituteforcompositionaltooluse. GPT-OSS-120Battainsthehighestefficiencywith
symbolic trajectory (𝒯’)
1) Expert task design
Guidelines
 Data manifest (𝒟)
…
Experts
Disaster query (𝒬)
Toolbox
symbolic trajectory (𝒯’)
Perception 
(GT masks)
Raster/Vector/Logical
/Vis (Real Compute)
Deterministic Replay Engine
(Resolve symbolic refs)
Gold Annotations
⚫ Gold trajectory (𝒯)
⚫ Gold final answer (𝒜)
⚫ Data manifest (𝒟)
⚫ Disaster query (𝒬)
DORA
AI-Assisted Evaluation 
Q-A Alignment
Eval-spec Comp. 
Numerical Sanity
2) Deterministic Trajectory Replay 3) Quality control
refine
Figure.6. Ourannotationpipeline: (1)expertsauthorqueriesandsymbolictrajectories;(2)adeterministicreplayengineresolves
references to produce gold annotations; (3) AI-assisted evaluation.
7

## Page 8

Table 3. Atomic scoring operators used by DORA. All typed fields are ultimately reduced to these four rules.𝑦𝑝, 𝑦𝑔 denote
predicted and gold values;nrm(·)applies string normalization.
Operator Scoring function Parameter
scalar|𝑦 𝑝 −𝑦 𝑔|≤𝜏 𝑟 |𝑦 𝑔|𝜏 𝑟=0.2
stringnrm(𝑦 𝑝)=nrm(𝑦 𝑔)–
point∥(𝑦 𝑥
𝑝, 𝑦
𝑦
𝑝)−(𝑦 𝑥
𝑔, 𝑦
𝑦
𝑔)∥2 ≤𝜏 px 𝜏px =20px
polygonIoU(𝑦 𝑝, 𝑦𝑔)≥𝜏 IoU 𝜏IoU =0.5
composite mean of atomic scores over expanded elements inherits atoms
Table4. MainresultsontheDORAbenchmark. Wereportfinal-answeraccuracy(%)pertaskdimension, trajectorymetrics(%),
and efficiency.
Final Answer (%) Trajectory (%)
Model AVG 𝑇1(PA)𝑇 2(SR)𝑇 3(OP)𝑇 4(TE)𝑇 5(RS) T-Any-O T-In-Ord T-Exact-M ParAcc Eff.
•Baselines
Gold Trajectory 80.48 71.31 63.19 83.63 90.77 93.50 100 100 100 100 100
Gemini-3.0-Flash [48] 18.55 5.98 19.91 17.48 29.36 20.03 Single-step prediction without tool use.
Qwen3-VL-235B [57] 18.30 5.53 28.63 12.63 27.75 16.95 Single-step prediction without tool use.
•Commercial Models
Gemini-3.0-Flash [48] 53.74 54.19 49.0059.8260.40 45.31 75.17 66.5735.55 42.6383.05
Grok-4.1-Fast [49] 52.10 53.0753.4054.23 55.28 44.52 59.15 53.19 28.09 31.96 86.83
GPT-5.4 [46] 47.63 52.85 50.80 53.50 51.90 29.11 66.84 59.43 31.82 37.71 88.46
GPT-5.4-Nano [46] 38.14 44.40 33.41 39.98 45.55 27.37 54.96 49.06 21.81 27.02 84.36
Claude-Sonnet-4.6 [47] 52.01 54.4348.23 51.82 60.05 45.53 76.2966.92 31.43 39.48 75.32
•Open-Source Models
Qwen3.5-397B-A17B [50]53.45 51.0353.4051.82 61.83 49.17 75.44 66.97 32.13 36.50 76.54
Qwen3.5-35B-A3B [50] 24.01 14.15 13.89 33.08 37.62 21.30 55.20 48.91 23.10 27.08 80.39
Gemma-4-31B [54] 51.17 51.46 49.00 52.33 61.03 42.03 69.89 62.58 32.82 38.23 86.43
MiMo-V2-Pro [51] 52.89 53.68 47.43 55.48 63.5844.26 74.0567.1334.26 38.45 79.11
MiniMax-M2.7 [56] 48.35 51.87 48.53 50.16 50.59 40.62 62.89 55.19 25.32 29.68 79.33
DeepSeek-V3.2 [53] 48.23 49.80 49.15 50.57 50.62 41.01 74.26 65.99 30.39 34.69 72.44
Step-3.5-Flash [52] 46.68 49.70 44.91 48.33 48.90 41.58 62.59 55.91 25.33 29.43 78.29
GPT-OSS-120B [55] 35.11 42.70 37.58 42.00 24.43 28.84 48.69 43.60 22.79 26.2490.42
a low accuracy, indicating that agents confidently select few tools but often thewrongones. On the open-source side, Qwen3.5-
397B-A17BnarrowsthegaptoGeminitowithin0.3%,Gemma-4-31BandMiMo-V2-Proformastrongsecondtier,andallthree
surpass GPT-5.4-Nano by more than 12%; strikingly, the 31B Gemma also outperforms GPT-OSS-120B despite using 4×fewer
parameters, indicating that agentic post-training quality matters more than raw parameter scale.
Tool heterogeneity amplifies compositional fragility.Across all models,Tool-Any-OrderexceedsTool-Exact-Matchby over
30%onaverage,indicatingthatevenwhenagentsknowwhichtoolstocall,theyrarelygettheorderandargumentsright.Param-
eter Accuracyreveals the same fragility: argument grounding (damage indices, GSD, path references, etc.) remains unreliable.
This fragility compounds withcompositional diversityrather than raw length alone. Although𝑇4 involves long trajectories, its
steps largely consist of repeated invocations of the same tools across multiple temporal phases, a simple and regular pattern that
agents handle comparatively well. In contrast,𝑇5 chainsdistincttools spanning perception, analysis, visualization, and summa-
rization, where a single early error cascades through a heterogeneous pipeline. All models suffer large drop on𝑇5, confirming
thattool heterogeneityis the dominant source of compositional failure.
Disaster-domain grounding exposes unique failure modes.Beyond generic compositional fragility, DORA exposes three
disaster-domain failure modes (Fig. 7): 1)Damage-semantic grounding(20.3%): agents struggle to map damage terminology
(“partial damaged”, “total destroyed”, “affected”, “flooded”) to class-index lists, and how indices evolve as multi-class masks
8

## Page 9

{1,2,3}are binarized{0,255}by tools likeras.compose_classesorras.threshold; 14.3% pass stale indices to
vectorization while 6.0% select wrong granularity. 2)Sensor-modality mismatch(14.8%): 9.1% mistake raster for vector re-
lational operations, while 5.7% involve modality swaps (optical↔SAR, aerial↔satellite, bi-temporal↔multi-spectral) or GSD
mis-specification. 3)disaster-pipeline composition(56.3%): agents mis-decompose compound spatial concepts, 12.8% miss key
toolsvec.intersectandvec.buffer;38.5%linkdownstreamtoolstothewrongupstreammask;and3.5%pickthewrong
phenomenon tool (e.g., invokingseg.landslideon a hurricane scene without any landslides). These show that LLM agents
lack disaster-semantic grounding for operational reasoning. Visualized examples are provided in Appendix § H.
0 5 10 15 20 25 30 35 40
Damage encoding evolution
Damage term mismatch
Raster replaces vector
Vector replaces raster
Aerial/Satellite mismatch
GSD numeric
Optical/SAR mismatch
Wrong upstream reference
Missing spatial tools
Wrong phenomenon tool
Length vs area confusion
(%)
14.3%
6.0%
9.1%
2.0%
2.0%
1.2%
0.5%
38.5%
12.8%
3.5%
1.5%
1) Damage-semantic grounding
2) Sensor-modality mismatch
3) Disaster-pipeline composition
Exclusive (only this error in the group)
Shared (co-occurs with another error in 
the same group)
Figure. 7. Failure modes in disaster domain.
Table 5. AP versus IF mode.
Protocol T-Any-O T-In-Ord T-Exact-M ParAcc AVG
Gold Trajectory 100 100 100 100 80.48
Gemini-3.0-Flash
w. AP 75.17 66.57 35.55 42.63 53.74
w. IF 82.56 82.03 62.53 53.49 55.71
ΔAP→IF ↑7.39↑15.46↑26.98↑10.86↑1.97
Gemma-4-31B
w. AP 69.89 62.58 32.82 38.23 51.17
w. IF 79.80 79.63 61.76 50.24 52.25
ΔAP→IF ↑9.91↑17.05↑28.94↑12.01↑1.08
MiniMax-M2.7
w. AP 62.89 55.19 25.32 29.68 48.35
w. IF 80.85 79.83 50.95 43.98 52.75
ΔAP→IF ↑17.96↑24.64↑25.63↑14.30↑4.40
4.2. Ablation Study
Even with the right tools, argument grounding remains highly challenging.We evaluate agents under two protocols:auto-
planning(AP,thedefault)andinstruction-following(IF,additionallygivenonlythegoldtool-orderhintsandmuststillissuetool
calls and infer all arguments themselves). Tab. 5 reveals a striking decoupling: IF yields substantial trajectory gains, confirming
that agentscan follow agiven pipeline oncetools are specified. Yetfinal-answer accuracy improves byonly 1.08–4.40%, leaving
all three models 25–28% below the gold trajectory. Even after tool-order uncertainty is reduced, inferring correct arguments
(filepaths,damageclassindices,GSDparameters)andextractingtherightintermediateoutputsremaindominantresidualfailure
modes. DORA is therefore doubly bottlenecked: agents must both select the right toolsanduse the right arguments, with errors
at either step propagating downstream.
Optical
Optical+Vector 
Optical+SAR
MS+DEM+Slope
Optical+DSM+Thermal
Average
Accuracy(%)
Different input modalities
0
10
20
30
40
50
60
70
Figure. 8. Agent performances (%) decomposed by input modality configuration.
Accuracy varies sharply with modality configuration.Fig. 8 decomposes agent performance by sensor configuration. Aux-
iliary modalities universally degrade accuracy: the pure-optical baseline reaches 52–59%, but adding OSM vector layers drops
accuracyto18–27%,andoptical-SARfusionto24–36%. Additionalmodalitiesdemandlongerplanningoverabroadertoolspace,
amplifyinggroundingerrorsateachstep. AllagentsstrugglewithMS+DEM+Slope: thesetaskschaingeometricoperationslike
computing susceptibility over terrain strata and composing landslide pipelines beyond image perception. Thermal-augmented
tasks remain tractable because land-surface temperature has clear numerical semantics (◦C) aligned with generic knowledge pri-
9

## Page 10

ors, reducing specialized grounding needs. Current agents handle pure-optical perception well but struggle with symbolic fusion
(OSM), cross-sensor alignment (SAR), and compositional geometric reasoning (slope, DEM).
0
20
40
60
80
100
2-3 (n=109) 4-5 (n=150) 6-7 (n=92) 8-10 (n=94) ≥11(n=70)
Final answer accuracy (%) 
56%
34%
19%22%7%
Gold Trajectory
Gemini-3.0-Flash
Qwen3.5-397B-
A17B
Gemma-4-31B
Step-3.5-Flash
Qwen3.5-35B-
A3B
Agent→Gold gap
Figure. 9. Agents vs. gold trajectory: compositional
fragility scales with length.
Table 6. Agent scaffolding ablation.
Scaffold AVG T-Exact-M ParAcc Latency (s/task)
ReAct 51.17 32.82 38.23 80
PE [58] 54.41 38.83 47.27179
Δ ↑3.24↑6.01↑9.04↑99
Reflexion [59] 52.74 36.21 40.05 167
Δ ↑1.57↑3.39↑1.82↑87
ReWOO [60] 44.26 25.18 25.92 82
Δ ↓6.91↓7.64↓12.31↑2
Compositional fragility scales with trajectory length.Fig. 9 bins all tasks by gold-trajectory length and reports per-bucket
final-answeraccuracyacrossrepresentativemodels. Theagent-to-goldgapwidensdramaticallywithlength: topmodelstrackthe
gold ceiling within 7% on short pipelines (2–3 steps) but fall 56% behind at≥11 steps. Notably, the gold ceiling itselfriseson
longtrajectories,sothewideninggapreflectsagent-sidecompositionaldecayratherthanharderunderlyingtasks: eachadditional
toolcallmultipliesthechanceofanupstreamargumentorsequencingerrorpropagatingtothefinalanswer. Hence,the8–10and
≥11 buckets exhibit the largest gaps, confirming long-horizon synthesis as the most fragile compositional regime.
Scaffolding helps modestly but does not close the gap.We evaluate three scaffolds on Gemma-4-31B, i.e., Plan-then-Execute
(PE) [58], Reflexion [59] and ReWOO [60] (Tab. 6). PE provides the largest gain (+3.24%), as upfront planning avoids agent
misdirection from intermediate observations on DORA’s long compositional pipelines. Reflexion offers a marginal +1.57% at
2.1×latency, as self-correction yields limited returns when failures stem from disaster-domain grounding rather than reasoning
slips. ReWOO collapses, confirming that removing observation feedback hurts data-heavy tasks driven by intermediate masks
and geometries. Critically, even the best scaffold trails the gold ceiling by over 26%, showing the dominant bottleneck remains
domain-specific knowledge and tool-argument grounding, not scaffolding strategy.
5. Conclusion
We presented DORA, the first agentic benchmark for operational disaster response, with 515 expert-authored tasks, 108 disaster-
tailored tools, and five analytical dimensions over heterogeneous geospatial data. Evaluating 13 frontier LLMs reveals three
persistent challenges: disaster-domain grounding exposes unique failure modes; agents are doubly bottlenecked by tool selection
and argument usage; and compositional fragility scales sharply with trajectory length, with the gold-ceiling gap reaching 56%
on long pipelines. We will release DORA with all data, tools, and evaluation protocols to drive progress toward operationally
reliable disaster-response AI agents.
Acknowledgments
This work was supported by JST CRONOS (Grant Number JPMJCS25K5), JST NEXUS (Grant Number JPMJNX25CA), and
KAKENHI (25K03145, 26K21244). Weihao Xuan is supported by RIKEN Junior Research Associate (JRA) Program. Pengyu
Dai is supported by RIKEN Incentive Research Project 2026. We also thank Ritwik Gupta for sharing the valuable xBD dataset
and for his expertise in disaster response guidance.
References
[1] J. Xu, D. J. Nair, and S. T. Waller, “Implementing equitable wildfire response plans,”Science, vol. 388, no. 6743, pp. 158–
159, 2025.
[2] E. Frankenberg, C. Sumantri, and D. Thomas, “Effects of a natural disaster on mortality risks over the longer term,”Nature
sustainability, vol. 3, no. 8, pp. 614–619, 2020.
10

## Page 11

[3] X. Wang, Y. Chen, L. Yuan, Y. Zhang, Y. Li, H. Peng, and H. Ji, “Executable code actions elicit better llm agents,” in
Forty-first International Conference on Machine Learning, 2024.
[4] J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, and O. Press, “Swe-agent: Agent-computer interfaces
enable automated software engineering,”Advances in Neural Information Processing Systems, vol. 37, pp. 50528–50652,
2024.
[5] X. Liu, H. Yu, H. Zhang, Y. Xu, X. Lei, H. Lai, Y. Gu, H. Ding, K. Men, K. Yang, S. Zhang, X. Deng, A. Zeng, Z. Du,
C. Zhang, S. Shen, T. Zhang, Y. Su, H. Sun, M. Huang, Y. Dong, and J. Tang, “Agentbench: Evaluating LLMs as agents,”
inThe Twelfth International Conference on Learning Representations, 2024.
[6] P. Feng, Z. Lv, J. Ye, X. Wang, X. Huo, J. Yu, W. Xu, W. Zhang, L. BAI, C. He, and W. Li, “Earth-agent: Unlocking the
full landscape of earth observation with agents,” inThe Fourteenth International Conference on Learning Representations,
2026.
[7] A. Shabbir, M. U. Sheikh, M. A. Munir, H. Debary, M. Fiaz, M. Z. Zaheer, P. Fraccaro, F. S. Khan, M. H. Khan, X. X.
Zhu,etal.,“Openearthagent: Aunifiedframeworkfortool-augmentedgeospatialagents,”arXivpreprintarXiv:2602.17665,
2026.
[8] S. Zhao, F. Liu, X. Zhang, H. Chen, X. Gu, Z. Jiang, F. Ling, B. Fei, W. Zhang, J. Wang,et al., “Openearth-agent: From
tool calling to tool creation for open-environment earth observation,”arXiv preprint arXiv:2603.22148, 2026.
[9] S.Yao,J.Zhao,D.Yu,N.Du,I.Shafran,K.Narasimhan,andY.Cao,“React: Synergizingreasoningandactinginlanguage
models,” inInternational Conference on Learning Representations (ICLR), 2023.
[10] A. Zhao, D. Huang, Q. Xu, M. Lin, Y.-J. Liu, and G. Huang, “Expel: Llm agents are experiential learners,” inProceedings
of the AAAI Conference on Artificial Intelligence, vol. 38, pp. 19632–19642, 2024.
[11] Y. Fu, D.-K. Kim, J. Kim, S. Sohn, L. Logeswaran, K. Bae, and H. Lee, “Autoguide: Automated generation and selection
of context-aware guidelines for large language model agents,”Advances in Neural Information Processing Systems, vol. 37,
pp. 119919–119948, 2024.
[12] S.Ouyang,J.Yan,I.Hsu,Y.Chen,K.Jiang,Z.Wang,R.Han,L.T.Le,S.Daruki,X.Tang,etal.,“Reasoningbank: Scaling
agent self-evolving with reasoning memory,”arXiv preprint arXiv:2509.25140, 2025.
[13] S. Zhou, F. F. Xu, H. Zhu, X. Zhou, R. Lo, A. Sridhar, X. Cheng, T. Ou, Y. Bisk, D. Fried, U. Alon, and G. Neubig,
“Webarena: A realistic web environment for building autonomous agents,” inThe Twelfth International Conference on
Learning Representations, 2024.
[14] T.Xie,D.Zhang,J.Chen,X.Li,S.Zhao,R.Cao,T.J.Hua,Z.Cheng,D.Shin,F.Lei,etal.,“Osworld: Benchmarkingmul-
timodal agents for open-ended tasks in real computer environments,”Advances in Neural Information Processing Systems,
vol. 37, pp. 52040–52094, 2024.
[15] J. Yang, C. E. Jimenez, A. L. Zhang, K. Lieret, J. Yang, X. Wu, O. Press, N. Muennighoff, G. Synnaeve, K. R. Narasimhan,
D. Yang, S. Wang, and O. Press, “SWE-bench multimodal: Do AI systems generalize to visual software domains?,” inThe
Thirteenth International Conference on Learning Representations, 2025.
[16] D. Ding, S. Liu, E. Yang, J. Lin, Z. Chen, S. Dou, H. Guo, W. Cheng, P. Zhao, C. Xiao,et al., “Octobench: Benchmarking
scaffold-aware instruction following in repository-grounded agentic coding,”arXiv preprint arXiv:2601.10343, 2026.
[17] Q.Zhou,J.Zhang,H.Wang,R.Hao,J.Wang,M.Han,Y.Yang,S.Wu,F.Pan,L.Fan,D.Tu,andZ.Zhang,“Featurebench:
Benchmarking agentic coding for complex feature development,” inThe Fourteenth International Conference on Learning
Representations, 2026.
[18] G. Mialon, C. Fourrier, T. Wolf, Y. LeCun, and T. Scialom, “GAIA: a benchmark for general AI assistants,” inThe Twelfth
International Conference on Learning Representations, 2024.
[19] J. Wang, Z. Ma, Y. Li, S. Zhang, C. Chen, K. Chen, and X. Le, “Gta: a benchmark for general tool agents,”Advances in
Neural Information Processing Systems, vol. 37, pp. 75749–75790, 2024.
11

## Page 12

[20] Z. Ma, W. Huang, J. Zhang, T. Gupta, and R. Krishna, “m & m’s: A benchmark to evaluate tool-use for m ulti-step m
ulti-modal tasks,” inEuropean Conference on Computer Vision, pp. 18–34, Springer, 2024.
[21] S.Singh,M.Fore,andD.Stamoulis,“Geollm-engine: Arealisticenvironmentforbuildinggeospatialcopilots,”inProceed-
ings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 585–594, 2024.
[22] A. Shabbir, M. A. Munir, A. Dudhane, M. U. Sheikh, M. H. Khan, P. Fraccaro, J. B. Moreno, F. S. Khan, and S. Khan,
“Thinkgeo: Evaluating tool-augmented agents for remote sensing tasks,”arXiv preprint arXiv:2505.23752, 2025.
[23] C. H. Kao, W. Zhao, S. Revankar, S. Speas, S. Bhagat, R. Datta, C. P. Phoo, U. Mall, C. Vondrick, K. Bala,et al., “Towards
llm agents for earth observation,”arXiv preprint arXiv:2504.12110, 2025.
[24] W.Xu, Z.Yu, B.Mu, Z.Wei, Y.Zhang, G.Li, J.Wang, andM.Peng, “Rs-agent: Automatingremotesensingtasksthrough
intelligent agent,”arXiv preprint arXiv:2406.07089, 2024.
[25] C. Liu, K. Chen, H. Zhang, Z. Qi, Z. Zou, and Z. Shi, “Change-agent: Toward interactive comprehensive remote sensing
change interpretation and analysis,”IEEE Transactions on Geoscience and Remote Sensing, vol. 62, pp. 1–16, 2024.
[26] R. Gupta, R. Hosfelt, S. Sajeev, N. Patel, B. Goodman, J. Doshi, E. Heim, H. Choset, and M. Gaston, “xbd: A dataset for
assessing building damage from satellite imagery,”arXiv preprint arXiv:1911.09296, 2019.
[27] J.Wang,W.Xuan,H.Qi,Z.Liu,K.Liu,Y.Wu,H.Chen,J.Song,J.Xia,Z.Zheng,andN.Yokoya,“Disasterm3: Aremote
sensing vision-language dataset for disaster damage assessment and response,” inProceedings of the Neural Information
Processing Systems, 2025.
[28] H. Chen, J. Song, O. Dietrich, C. Broni-Bediako, W. Xuan, J. Wang, X. Shao, Y. Wei, J. Xia, C. Lan,et al., “Bright:
A globally distributed multimodal building damage assessment dataset with very-high-resolution for all-weather disaster
response,”Earth System Science Data, vol. 17, no. 11, pp. 6217–6253, 2025.
[29] USDA Farm Service Agency, “National agriculture imagery program (NAIP).”https://naip-usdaonline.hub.
arcgis.com/, 2022. Accessed: 2025.
[30] Maxar Technologies, “Maxar open data program.”https://www.maxar.com/open-data, 2024. Accessed: 2025.
[31] O. Ghorbanzadeh, Y. Xu, H. Zhao, J. Wang, Y. Zhong, D. Zhao, Q. Zang, S. Wang, F. Zhang, Y. Shi,et al., “The outcome
of the 2022 landslide4sense competition: Advanced landslide detection from multisource satellite imagery,”IEEE Journal
of Selected Topics in Applied Earth Observations and Remote Sensing, vol. 15, pp. 9927–9942, 2022.
[32] X. Zhang, W. Yu, M.-O. Pun, and W. Shi, “Cross-domain landslide mapping from large-scale remote sensing images us-
ing prototype-guided domain-aware progressive representation learning,”ISPRS Journal of Photogrammetry and Remote
Sensing, vol. 197, pp. 1–17, 2023.
[33] M. Rahnemoonfar, T. Chowdhury, and R. Murphy, “Rescuenet: A high resolution uav semantic segmentation dataset for
natural disaster damage assessment,”Scientific data, vol. 10, no. 1, p. 913, 2023.
[34] T. Manzini, P. Perali, R. Karnik, and R. Murphy, “Crasar-u-droids: A large scale benchmark dataset for building alignment
and damage assessment in georectified suas imagery,”arXiv preprint arXiv:2407.17673, 2024.
[35] J.Xia,N.Yokoya,B.Adriano,andC.Broni-Bediako,“Openearthmap: Abenchmarkdatasetforglobalhigh-resolutionland
cover mapping,” inProceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision, pp. 6254–6264,
2023.
[36] Japan Meteorological Agency, “Land surface temperature and climate data.”https://www.jma.go.jp/jma/
indexe.html, 2025. Accessed: 2025.
[37] OpenStreetMap contributors, “Planet dump retrieved from https://planet.osm.org.”https://www.openstreetmap.
org, 2025. Data licensed under ODbL.
[38] M.Roser,H.Ritchie,E.Ortiz-Ospina,L.Rodés-Guirao,J.Hasell,B.Macdonald,D.Beltekian,E.Mathieu,andC.Giattino,
“Our world in data.”https://ourworldindata.org, 2025. Licensed under CC BY. Accessed: 2025.
12

## Page 13

[39] United Nations Institute for Training and Research (UNITAR), “UNOSAT – United Nations Satellite Centre emergency
mapping service.”https://unosat.org/services/, 2024. Accessed: 2026-04-06.
[40] I. Joubert-Boitat, A. Wania, and S. Dalmasso, “Manual for CEMS-rapid mapping products,” Tech. Rep. JRC121741, Euro-
pean Commission, Joint Research Centre (JRC), 2020.
[41] Federal Emergency Management Agency (FEMA), “National urban search and rescue (US&R) response system: Rescue
field operations guide,” Tech. Rep. US&R-23-FG, U.S. Department of Homeland Security, 2008.
[42] UnitedNationsOfficefortheCoordinationofHumanitarianAffairs(OCHA),“ThisisOCHA.”https://www.unocha.
org/ocha, 2024. Established by UN General Assembly Resolution 46/182 (1991).
[43] FederalEmergencyManagementAgency,“Hazusinventorytechnicalmanual,”Tech.Rep.Hazus6.1,DepartmentofHome-
land Security, FEMA, Washington, D.C., 2024.
[44] A. Van Etten, D. Hogan, J. M. Manso, J. Shermeyer, N. Weir, and R. Lewis, “The Multi-Temporal Urban Development
SpaceNet Dataset,” inProceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR),
pp. 6398–6407, 2021.
[45] Y.Qin,S.Liang,Y.Ye,K.Zhu,L.Yan,Y.Lu,Y.Lin,X.Cong,X.Tang,B.Qian,etal.,“Toolllm: Facilitatinglargelanguage
models to master 16000+ real-world apis,” inThe Twelfth International Conference on Learning Representations, 2024.
[46] OpenAI, “GPT-5.4 thinking system card,” tech. rep., OpenAI, March 2026.
[47] Anthropic, “Claude sonnet 4.6 system card,” tech. rep., Anthropic, February 2026.
[48] Google DeepMind, “Introducing Gemini 3 flash: Benchmarks, global availability.”https://blog.google/
products/gemini/gemini-3-flash/, 2026.
[49] xAI, “Grok 4.1 model card,” tech. rep., xAI, November 2025.
[50] Qwen Team, “Qwen3.5: Towards native multimodal agents.”https://qwen.ai/blog?id=qwen3.5, 2026.
[51] LLM-Core, Xiaomi, “MiMo-V2-Pro.”https://mimo.xiaomi.com/mimo-v2-pro, 2026. API model card, re-
leased March 18, 2026.
[52] StepFun, “Step 3.5 Flash: Fast enough to think, reliable enough to act.”https://static.stepfun.com/blog/
step-3.5-flash/, 2025. Technical blog and model card.
[53] DeepSeek-AI, “DeepSeek-V3.2: Pushing the frontier of open large language models,”arXiv preprint arXiv:2512.02556,
2025.
[54] Gemma Team and Google DeepMind, “Gemma 4: Byte for byte, the most capable open models,” tech. rep., Google Deep-
Mind, April 2026.
[55] OpenAI, “gpt-oss-120b & gpt-oss-20b model card,”arXiv preprint arXiv:2508.10925, 2025.
[56] MiniMax AI, “MiniMax-M2.7: A self-evolving agent model,” tech. rep., MiniMax AI, March 2026.
[57] S. Bai, Y. Cai,et al., “Qwen3-VL technical report,” 2025.
[58] G. He, G. Demartini, and U. Gadiraju, “Plan-then-execute: An empirical study of user trust and team performance when
usingllmagentsasadailyassistant,”inProceedingsofthe2025CHIConferenceonHumanFactorsinComputingSystems,
pp. 1–22, 2025.
[59] N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao, “Reflexion: Language agents with verbal reinforcement
learning,”Advances in neural information processing systems, vol. 36, pp. 8634–8652, 2023.
[60] B. Xu, Z. Peng, B. Lei, S. Mukherjee, Y. Liu, and D. Xu, “Rewoo: Decoupling reasoning from observations for efficient
augmented language models,”arXiv preprint arXiv:2305.18323, 2023.
13
