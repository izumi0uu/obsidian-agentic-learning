---
type: source
source_type: web
site: xiaolinnote.com
topic:
  - interview
  - ai
  - llm
status: inbox
created: 2026-05-07
updated: 2026-05-17
url: https://xiaolinnote.com/ai/llm/llm_info.html
source: https://xiaolinnote.com/ai/llm/llm_info.html
last_checked: 2026-05-17
freshness: watch
sha256: 9b4b3b11dac8e7c07822ad2a3cc9daec96045ca22542185bd8b7fd60ee308b77
related:
  - "[[raw/repos/xiaolinnote/xiaolinnote 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[LLM]]"
  - "[[LLM 主题]]"
  - "[[LLM Training Pipeline]]"
---

# [[LLM|大模型]]工程面试题介绍

原始链接：https://xiaolinnote.com/ai/llm/llm_info.html

抓取范围：来自 `https://xiaolinnote.com/sitemap.xml`。本页保留为 raw source evidence，后续再从中拆概念卡。

## 相关知识 wiki

- [[LLM]]
- [[LLM 主题]]
- [[LLM Training Pipeline]]

## 页面正文

# 大模型工程面试题介绍

原创[公众号@小林面试笔记](https://xiaolinnote.com)LLM大约 9 分钟约 2686 字

---

# [大模型工程面试题介绍](#大模型工程面试题介绍)

[![](https://cdn.xiaolincoding.com//picgo/cb600c1b8d1950c1ee64dad0e3a58139.png)](https://www.xiaolincoding.com/other/llm_offer.html)

大家好，我是小林。

最近一两年大模型面试问得越来越深，特别是 Agent、AI 应用工程师、大模型工程师这类岗位，光会调 OpenAI API 和用 LangChain 已经远远不够了，面试官真正想考察的，是你对 LLM 底层原理的理解。

我对照了一下网上各家大厂（字节、阿里、快手、DeepSeek 这些）的真实面经，发现大模型底层这块的面试考察其实非常集中，主要围绕下面这五条主线展开。

**第一条主线是「Transformer 架构原理」**。Attention 公式里为什么除以 √d\_k、Q/K/V 是怎么从输入投影出来的、Multi-Head 多在哪儿，这些是基础必考。再往上是 MHA 的优化（MQA、GQA、Flash Attention），是 2024 年之后新加的高频考点，特别是面 DeepSeek、阿里、字节这种自研大模型的公司，几乎必问。位置编码（RoPE 怎么用旋转表示相对位置）也是 100% 会问的点。

**第二条主线是「训练流程」**。预训练 + SFT + 对齐三阶段是大模型训练的标准框架，每个阶段在做什么、为什么必须按这个顺序、缺一会怎样，是面试官最爱追问的。延伸的高频点包括 Scaling Law（Chinchilla 1:20 配比、涌现能力）、LoRA / QLoRA 微调、RLHF / DPO / GRPO 对齐。特别是 GRPO，因为 DeepSeek R1 的火爆，2026 年成了几乎必问的新热点，你说不出「砍掉 Value Model 用组内归一化代替」这一句，面试官就知道你没跟上最新进展。

**第三条主线是「推理优化」**。这一块是 Agent 开发岗最容易延伸到的地方，包括温度/Top-P/Top-K 采样参数、KV Cache + Prompt Caching、量化（INT4/AWQ/GPTQ）、解码策略（为什么 LLM 不用 Beam Search）、MoE（DeepSeek V3 为什么 671B 参数但推理只用 37B）、部署框架（vLLM vs SGLang 怎么选）。面试官问到「你这个项目为什么用 X 模型」「推理成本怎么压下来的」这种问题，基本都会往这一块带。

**第四条主线是「Prompt 工程和应用层」**。Prompt 怎么写好（五要素、Few-shot、CoT 触发词）、CoT 为什么有效、幻觉为什么会出现以及怎么缓解，是所有 LLM 应用岗的必问基础。这一块上手最容易，但要答到能让面试官点头，得能讲出「Prompt 不是写完就完，是工程问题」「幻觉的根因是 LLM 是续写器不是数据库」这种工程视角。

**第五条主线是「评测与选型」**。包括学术 Benchmark 的局限（数据污染问题）、业务测试集怎么建、实际项目里选什么模型。特别是「你们项目为什么选这个模型不选那个」，几乎每场面试都会有这道开放题。能答出「合规 + 成本 + 延迟 + 能力四维度匹配业务需求」这种判断框架，就比一般候选人深一层。

把这五条主线吃透，大模型底层这块的面试基本就稳了。我从这些真实面经里筛了 22 道最高频的题，按上面的主线分块组织，每道题都按照的「面试翻车现场 + 知识点讲透」的方式写。目的不是让你背一套标准答案，而是让你真正理解了，不管面试官怎么换着花样问，你都能自己推出来。

## [题目目录](#题目目录)

下面按完整顺序列出 22 道题，你可以挑自己不熟的看。整体内容分成六块。

**第一块（Q1-Q5）是认知与基础原理**，先讲清楚 LLM 是什么、和传统 NLP 的区别，然后展开 Transformer 架构、MHA 优化（MQA/GQA/Flash Attention）、位置编码（RoPE 等）、分词器（Tokenizer）。这五题是底层原理的地基，搞不清楚后面所有的东西都讲不透。

**第二块（Q6-Q11）是训练全景与微调**，从「大模型怎么训练出来」这个全景题开始，展开 Scaling Law（参数和数据怎么配）、微调方案（全量 vs LoRA vs QLoRA）、LoRA 的深入分析、Post-Training 家族（RLHF / DPO / GRPO / 拒绝采样 / RLAIF）、DPO vs PPO 的对比。

**第三块（Q12-Q15）是推理与生成**，讲清楚模型生成文本时怎么选下一个 token（贪心、Beam Search、采样）、采样参数怎么调（温度/Top-P/Top-K）、KV Cache 和 Prompt Caching 的工程优化、大模型量化（INT4/INT8/AWQ/GPTQ）。这一块是部署优化的核心。

**第四块（Q16-Q18）是应用与 Prompt 工程**，讲 Prompt 怎么写好（五要素 + 进阶技巧）、CoT 怎么用、幻觉为什么会出现以及怎么缓解。这一块是 LLM 应用开发直接相关的实战内容。

**第五块（Q19-Q20）是架构演进与部署**，讲 MoE 混合专家模型（DeepSeek V3 为什么便宜）、推理框架对比（vLLM / SGLang / TGI / llama.cpp 怎么选）。

**第六块（Q21-Q22）是评测与选型**，讲大模型评测指标（学术 Benchmark 的局限、业务测试集的构建）、实际项目选型（合规 + 成本 + 延迟 + 能力四维度）。

- [1. 什么是大语言模型？和传统 NLP 模型有什么区别？](/ai/llm/what_is_llm.html)
- [2. 讲讲 Transformer 架构基本原理？Encoder 和 Decoder 是什么？](/ai/llm/transformer_architecture.html)
- [3. 多头注意力（MHA）有哪些局限？MQA、GQA、Flash Attention 怎么解决？](/ai/llm/mha_mqa_gqa_flash_attention.html)
- [4. 大模型的位置编码是干什么用的？sin/cos、RoPE、ALiBi 有什么区别？](/ai/llm/position_encoding.html)
- [5. 什么是大模型项目的分词器？原理是什么？](/ai/llm/tokenizer.html)
- [6. 大模型是怎么训练出来的？](/ai/llm/llm_training.html)
- [7. 什么是 Scaling Law？大模型的「涌现能力」是怎么回事？](/ai/llm/scaling_law_emergence.html)
- [8. 大模型微调的方案有哪些?](/ai/llm/finetuning.html)
- [9. 请讲一下 LoRA 技术，除了减少参数量，它还有哪些优点？](/ai/llm/lora.html)
- [10. SFT 之后还有哪些 Post-Training？RLHF、DPO、GRPO、拒绝采样什么关系？](/ai/llm/post_training.html)
- [11. 大模型的 DPO 和 PPO 的区别是什么？](/ai/llm/dpo_vs_ppo.html)
- [12. 大模型生成文本时的解码策略有哪些？贪心、Beam Search、采样分别什么时候用？](/ai/llm/decoding_strategies.html)
- [13. 大模型的参数：温度值、Top-P、Top-K 分别是什么？各个场景下的最佳设置是什么？](/ai/llm/temperature_top_p_top_k.html)
- [14. KV Cache 是什么？Prompt Caching 的原理是什么？](/ai/llm/kv_cache_prompt_caching.html)
- [15. 大模型量化是什么？INT8/INT4/AWQ/GPTQ 怎么选？](/ai/llm/quantization.html)
- [16. 如何写好 Prompt？分享下 Prompt 工程实践经验？](/ai/llm/prompt_engineering.html)
- [17. 什么是 CoT？为啥效果好？它有什么缺点或局限性？](/ai/llm/cot.html)
- [18. 大模型为什么会出现幻觉？怎么缓解？](/ai/llm/hallucination.html)
- [19. MoE 混合专家模型是什么？DeepSeek V3、Qwen 为什么用 MoE？](/ai/llm/moe.html)
- [20. 大模型部署有哪些主流方案？vLLM、TGI、llama.cpp、SGLang 实际项目里怎么选？](/ai/llm/deployment_frameworks.html)
- [21. 大模型能力评测指标有哪些？](/ai/llm/evaluation_metrics.html)
- [22. 对比使用过哪些主流大模型？你们项目中最终选用了哪个模型？为什么？](/ai/llm/model_selection.html)

## [针对 Agent 开发同学的阅读意见](#针对-agent-开发同学的阅读意见)

很多林友是冲着 Agent 开发求职来的，时间又比较紧（一般 1-2 个月内要面试），不可能 22 题平均用力。我按「跟 Agent 开发的相关度」把这 22 题分成三档优先级，你可以照着安排时间。

### [第一档：必看，直接关系 Agent 开发实战（9 道）](#第一档-必看-直接关系-agent-开发实战-9-道)

这一档是 Agent 开发**每天都会用到**的知识，也是面试官追问 Agent 架构时最容易延伸到的地方。这 9 道题如果答不上来，Agent 开发岗位的面试基本走不远。

**应用与生成层（5 道）**：Q1 什么是 LLM（认知打底，快速过即可）、Q13 温度/Top-P/Top-K（Agent 输出稳定性的关键，调过 OpenAI API 的应该都熟）、Q16 Prompt 工程（写 Agent System Prompt 的基本功）、Q17 CoT（Agent 推理增强必备，ReAct、Plan-and-Execute 这些范式背后都是 CoT 的延伸）、Q18 幻觉（Agent 输出靠谱性的核心问题，必须懂缓解手段）。

**推理优化与部署（4 道）**：Q14 KV Cache + Prompt Caching（Agent 调用次数多，Prompt Caching 能省 90% 输入 token 费用）、Q20 部署框架（vLLM、SGLang 是 Agent 部署的两个主流选择，SGLang 在多轮对话场景比 vLLM 省 50%+ 显存）、Q21 评测指标（Agent 效果怎么量化、业务测试集怎么建）、Q22 模型选型（选什么模型直接决定 Agent 的上限，国内项目还有合规约束）。

把这 9 道吃透，Agent 开发岗的 LLM 部分面试就有 70% 的把握了。

### [第二档：选看，理解原理为主（6 道）](#第二档-选看-理解原理为主-6-道)

这一档是「面试可能被追问到，但 Agent 开发实战里用得少」的内容。建议作为「补充阅读」，不需要每道都吃透到能默写公式的程度，理解大致原理 + 能在面试里说清楚关键概念就够了。

**底层架构（3 道）**：Q2 Transformer 架构（基础原理，面试经常追问 Q/K/V 投影、√d\_k 的作用）、Q3 MHA 优化（理解推理成本来源，MQA/GQA/Flash Attention 这套优化是为什么 LLM 推理这么贵的答案）、Q5 分词器（理解 token 计费、上下文管理为什么按 token 算）。

**推理和架构演进（3 道）**：Q12 解码策略（理解为什么 LLM 不用 Beam Search 而用采样）、Q15 量化（部署相关，INT4 量化 + AWQ/GPTQ 算法）、Q19 MoE（理解 DeepSeek V3 这种「671B 总参数但只激活 37B」的模型为什么这么便宜）。

### [第三档：可跳，短期 Agent 开发用不上（7 道）](#第三档-可跳-短期-agent-开发用不上-7-道)

这一档是「大模型训练相关」的题。如果你是 Agent 开发求职，**短期 1-2 个月内不需要深入这块**。这些题更适合后期想往大模型训练、对齐方向转的同学，或者面试时间有富余的话作为拓展看。

**训练原理（3 道）**：Q4 位置编码（sin/cos、RoPE、ALiBi 是训练时的设计）、Q6 大模型怎么训练（预训练 + SFT + 对齐三阶段）、Q7 Scaling Law（理论性强，Chinchilla 配比、涌现能力）。

**微调和对齐（4 道）**：Q8 微调方案、Q9 LoRA、Q10 Post-Training 全景、Q11 DPO vs PPO 的区别。

这 7 道题不是不重要，是「**对 Agent 开发求职的优先级不高**」。如果有时间，完全可以补一下，对面试也有帮助。但如果时间紧，第一档 + 第二档先吃透，第三档面试前快速过一遍要点就行。

---

对了，大模型面试题会在「**公众号@小林面试笔记题**」持续更新，林友们赶紧关注起来，别错过最新干货哦！

![](https://cdn.xiaolincoding.com//picgo/扫码_搜索联合传播样式-标准色版.png)

## 页面链接

- [跳至主要內容](https://xiaolinnote.com/ai/llm/llm_info.html#main-content)
- [小林面试笔记](https://xiaolinnote.com/)
- [首页](https://xiaolinnote.com/)
- [大模型面试题](https://xiaolinnote.com/ai/)
- [Agent项目](https://www.xiaolincoding.com/project/aioncallagent.html)
- [Agent训练营](https://www.xiaolincoding.com/other/llm_offer.html)
- [后端图解](https://xiaolincoding.com/)
- [大模型工程面试题介绍](https://xiaolinnote.com/ai/llm/llm_info.html)
- [1. 什么是大语言模型？和传统 NLP 模型有什么区别？](https://xiaolinnote.com/ai/llm/what_is_llm.html)
- [2. 讲讲 Transformer 架构基本原理？Encoder 和 Decoder 是什么？](https://xiaolinnote.com/ai/llm/transformer_architecture.html)
- [3. 多头注意力（MHA）有哪些局限？MQA、GQA、Flash Attention 怎么解决？](https://xiaolinnote.com/ai/llm/mha_mqa_gqa_flash_attention.html)
- [4. 大模型的位置编码是干什么用的？sin/cos、RoPE、ALiBi 有什么区别？](https://xiaolinnote.com/ai/llm/position_encoding.html)
- [5. 什么是大模型项目的分词器？原理是什么？](https://xiaolinnote.com/ai/llm/tokenizer.html)
- [6. 大模型是怎么训练出来的？](https://xiaolinnote.com/ai/llm/llm_training.html)
- [7. 什么是 Scaling Law？大模型的「涌现能力」是怎么回事？](https://xiaolinnote.com/ai/llm/scaling_law_emergence.html)
- [8. 大模型微调的方案有哪些？](https://xiaolinnote.com/ai/llm/finetuning.html)
- [9. 请讲一下 LoRA 技术，除了减少参数量，它还有哪些优点？](https://xiaolinnote.com/ai/llm/lora.html)
- [10. SFT 之后还有哪些 Post-Training？RLHF、DPO、GRPO、拒绝采样什么关系？](https://xiaolinnote.com/ai/llm/post_training.html)
- [11. 大模型的 DPO 和 PPO 的区别是什么？](https://xiaolinnote.com/ai/llm/dpo_vs_ppo.html)
- [12. 大模型生成文本时的解码策略有哪些？贪心、Beam Search、采样分别什么时候用？](https://xiaolinnote.com/ai/llm/decoding_strategies.html)
- [13. 大模型的参数：温度值、Top-P、Top-K 分别是什么？各个场景下的最佳设置是什么？](https://xiaolinnote.com/ai/llm/temperature_top_p_top_k.html)
- [14. KV Cache 是什么？Prompt Caching 的原理是什么？](https://xiaolinnote.com/ai/llm/kv_cache_prompt_caching.html)
- [15. 大模型量化是什么？INT8/INT4/AWQ/GPTQ 怎么选？](https://xiaolinnote.com/ai/llm/quantization.html)
- [16. 如何写好 Prompt？分享下 Prompt 工程实践经验？](https://xiaolinnote.com/ai/llm/prompt_engineering.html)
- [17. 什么是 CoT？为啥效果好？它有什么缺点或局限性？](https://xiaolinnote.com/ai/llm/cot.html)
- [18. 大模型为什么会出现幻觉？怎么缓解？](https://xiaolinnote.com/ai/llm/hallucination.html)
- [19. MoE 混合专家模型是什么？DeepSeek V3、Qwen 为什么用 MoE？](https://xiaolinnote.com/ai/llm/moe.html)
- [20. 大模型部署有哪些主流方案？vLLM、TGI、llama.cpp、SGLang 实际项目里怎么选？](https://xiaolinnote.com/ai/llm/deployment_frameworks.html)
- [21. 大模型能力评测指标有哪些？](https://xiaolinnote.com/ai/llm/evaluation_metrics.html)
- [22. 对比使用过哪些主流大模型？你们项目中最终选用了哪个模型？为什么？](https://xiaolinnote.com/ai/llm/model_selection.html)
- [公众号@小林面试笔记](https://xiaolinnote.com)
- [大模型工程面试题介绍](https://xiaolinnote.com/ai/llm/llm_info.html#大模型工程面试题介绍)
- [https://www.xiaolincoding.com/other/llm_offer.html](https://www.xiaolincoding.com/other/llm_offer.html)
- [题目目录](https://xiaolinnote.com/ai/llm/llm_info.html#题目目录)
- [8. 大模型微调的方案有哪些?](https://xiaolinnote.com/ai/llm/finetuning.html)
- [针对 Agent 开发同学的阅读意见](https://xiaolinnote.com/ai/llm/llm_info.html#针对-agent-开发同学的阅读意见)
- [第一档：必看，直接关系 Agent 开发实战（9 道）](https://xiaolinnote.com/ai/llm/llm_info.html#第一档-必看-直接关系-agent-开发实战-9-道)
- [第二档：选看，理解原理为主（6 道）](https://xiaolinnote.com/ai/llm/llm_info.html#第二档-选看-理解原理为主-6-道)
- [第三档：可跳，短期 Agent 开发用不上（7 道）](https://xiaolinnote.com/ai/llm/llm_info.html#第三档-可跳-短期-agent-开发用不上-7-道)
- [下一页 1. 什么是大语言模型？和传统 NLP 模型有什么区别？](https://xiaolinnote.com/ai/llm/what_is_llm.html)
- [粤ICP备2025467464](https://beian.miit.gov.cn/)
