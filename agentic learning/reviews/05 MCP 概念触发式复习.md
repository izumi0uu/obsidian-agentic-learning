---
type: review
topic:
  - agent
  - tools
  - protocol
  - review
  - feynman
status: active
created: 2026-05-19
updated: 2026-05-20
source:
  - "[[MCP]]"
  - "[[Tool Calling]]"
  - "[[Tool 接口层对比]]"
  - "[[MCP Transport]]"
  - "[[Model Context Protocol 官方文档]]"
  - "[[OpenAI Function Calling 文档]]"
related:
  - "[[reviews/复习记录索引]]"
  - "[[MCP]]"
  - "[[MCP Transport]]"
  - "[[Tool Calling]]"
  - "[[Tool 接口层对比]]"
  - "[[Tool Registry]]"
  - "[[Tool Permissioning]]"
  - "[[Least Privilege Tools]]"
  - "[[Approval Gate]]"
  - "[[Tool Poisoning]]"
  - "[[Prompt]]"
  - "[[A2A MCP ANP 对比]]"
  - "[[02 问题池]]"
  - "[[05 Query 写回队列]]"
---

# 05 MCP 概念触发式复习

日期：2026-05-19

这页记录 [[MCP]] 的概念触发式复习：重点检查我能不能把 MCP 从“模型能调工具”切到“host / client / server + tools / resources / prompts + tool selection + [[Tool Calling|Function Calling]] + permissioning 的协议连接层”。它不是 raw evidence，也不替代 [[MCP]] 概念卡。

## 触发概念

- 概念：[[MCP]]
- 触发原因：刚补充了 MCP host / client / server 角色分工、Tools / Resources / Prompts 三类能力、工具选择流程、MCP 与 [[Tool Calling|Function Calling]] 的边界，以及 filesystem server 的调用流程图；现在需要用追问检查这些边界是否真正能复述。

## 目标

用费曼方式检查我是否真的理解 MCP：不是背 Model Context Protocol 的全称，而是能说清它解决什么工程问题、client/server/host 分别是谁、和 [[Tool Calling|Function Calling]] 的边界在哪里、为什么接入工具越容易越需要权限和审计。

## 复习节奏规则

- 默认只做一轮追问：用来暴露主要误解和边界缺口。
- 如果第一轮仍有关键卡点，最多追加一轮第二轮追问；第二轮只聚焦 1-3 个最影响理解的缺口。
- 第二轮之后必须收束：只做总结、写回候选、补概念卡或加入 [[02 问题池]] / [[05 Query 写回队列]]，不再生成第三轮追问。
- 如果还没懂，说明 [[MCP]] 或相关对比页需要重写，而不是继续加问。

## 作答前最小边界

先不要把 MCP 解释成“Agent 调工具”。更稳的入口是：

```text
host = AI 应用 / 模型宿主 / 权限策略入口
client = host 里面连接某个 server 的协议连接模块
server = 外部能力的标准化包装和执行端

Tools = 主动执行，可能有副作用
Resources = 被动提供数据，通常只读
Prompts = 可复用提示模板，影响任务 framing

Function Calling / Tool Calling = 模型输出结构化调用意图的接口
MCP = host/client/server 连接外部能力的协议
```

小边界：MCP client 在 Agent 应用这一侧，但它本身不是 Agent。Agent / host / harness 负责模型调用、状态、权限、审批和编排；MCP client 只是把调用请求按协议发给某个 MCP server，并把结果带回来。

对比入口：[[Tool 接口层对比]]。这页把 [[Tool Use]]、[[Tool Calling|Function Calling]]、[[Tool Registry]]、[[Tool Permissioning]]、[[MCP]] 和 [[MCP Registry]] 放在同一张工具接口层地图里。复习时先记住：Function Calling 解决“模型如何提出一次结构化调用请求”，MCP 解决“外部能力如何被标准化发现、连接和调用”。

工具选择的最小链路：

```text
MCP client list_tools()
  -> host / tool registry 把工具描述和 schema 转成模型可见格式
  -> LLM 根据用户问题和工具描述提出 tool call 意图
  -> host 做参数、权限、审批、风险检查
  -> MCP client 转发给 MCP server 执行
  -> 工具结果回到 host，再进入上下文 / state / trace
```

## 我的原始解释

>

## 我已经说对的点

- 待我回答后补。

## 需要更精确的点

- 待我回答后补。

## 第一轮追问

1. 请用一句话区分 MCP host、MCP client、MCP server，必须出现“协议连接模块”。
2. 为什么说 MCP client 在 Agent 应用这一侧，但 MCP client 本身不等于 Agent？
3. MCP 和 [[Tool Calling|Function Calling]] 分别处在哪一层？请用“模型输出调用意图”和“应用连接外部 server”两个短语解释。
4. Tools、Resources、Prompts 的最小区别是什么？为什么 `read_file` 这种例子在协议调用和安全分级上容易让人混淆？
5. Claude 或其他 LLM 是如何决定使用哪个 MCP 工具的？请按工具发现、模型可见 schema、模型选择、执行前检查、MCP server 执行、结果整合六步解释。
6. 如果一个 MCP server 暴露了 `delete_file`、`read_customer_data`、`summarize_logs` 三个能力，你会分别放在哪些权限 / 审批 / 审计策略里？为什么？

## 追加追问：Tool Calling / Function Calling

7. [[Tool Calling|Function Calling]] 的“两轮对话 + 中间执行”闭环是什么？请按第一轮模型输出 tool call、runtime 执行、第二轮模型整合结果来解释。
8. Tool schema 里的 `name`、`description`、`parameters/inputSchema` 分别影响什么？哪个字段最容易影响模型“选错工具”？
9. 为什么 Function Calling 只解决“结构化调用请求”，不自动解决权限、幂等、重试、超时、审计和结果可信？

## 追加追问：Tool 接口层对比

10. 请用一句话分别区分 [[Tool Use]]、[[Tool Calling|Function Calling]]、[[Tool Registry]]、[[Tool Permissioning]]、[[MCP]]、[[MCP Registry]]。
11. 如果一个 Agent “会输出合法 tool call，但经常选错工具或越权调用”，问题更可能落在哪几层？请至少点名两个层。
12. 什么时候只用 Function Calling 就够了，什么时候应该引入 MCP？请用“单应用私有函数 / 多 host 复用外部能力 / server 生态”这三个短语回答。
13. 为什么有了 [[Tool Calling]] 还需要 [[MCP]]？请用“调用意图”和“外部能力接入标准”两个短语回答，并说明两者为什么不是替代关系。

## 我的费曼回答区

### Q1：请用一句话区分 MCP host、MCP client、MCP server，必须出现“协议连接模块”。

我的回答：


反馈：


写回：


### Q2：为什么说 MCP client 在 Agent 应用这一侧，但 MCP client 本身不等于 Agent？

我的回答：


反馈：


写回：


### Q3：MCP 和 Function Calling / Tool Calling 分别处在哪一层？请用“模型输出调用意图”和“应用连接外部 server”两个短语解释。

我的回答：


反馈：


写回：


### Q4：Tools、Resources、Prompts 的最小区别是什么？为什么 read_file 这种例子在协议调用和安全分级上容易让人混淆？

我的回答：


反馈：


写回：


### Q5：Claude 或其他 LLM 是如何决定使用哪个 MCP 工具的？请按工具发现、模型可见 schema、模型选择、执行前检查、MCP server 执行、结果整合六步解释。

我的回答：


反馈：


写回：


### Q6：如果一个 MCP server 暴露了 delete_file、read_customer_data、summarize_logs 三个能力，你会分别放在哪些权限 / 审批 / 审计策略里？为什么？

我的回答：


反馈：


写回：


### Q7：Tool Calling / Function Calling 的“两轮对话 + 中间执行”闭环是什么？

我的回答：


反馈：


写回：


### Q8：Tool schema 里的 name、description、parameters/inputSchema 分别影响什么？哪个字段最容易影响模型“选错工具”？

我的回答：


反馈：


写回：


### Q9：为什么 Function Calling 只解决“结构化调用请求”，不自动解决权限、幂等、重试、超时、审计和结果可信？

我的回答：


反馈：


写回：


### Q10：请用一句话分别区分 Tool Use、Function Calling、Tool Registry、Tool Permissioning、MCP、MCP Registry。

我的回答：


反馈：


写回：


### Q11：如果一个 Agent “会输出合法 tool call，但经常选错工具或越权调用”，问题更可能落在哪几层？请至少点名两个层。

我的回答：


反馈：


写回：


### Q12：什么时候只用 Function Calling 就够了，什么时候应该引入 MCP？

我的回答：


反馈：


写回：


### Q13：为什么有了 Tool Calling 还需要 MCP？

我的回答：


反馈：


写回：


## 写回候选

- [ ] 如果 Q1 不能稳定区分 host / client / server，回看 [[MCP#Host / Client / Server 角色分工]]。
- [ ] 如果 Q2 把 MCP client 直接等同于 Agent，把“client 是协议连接模块，不是编排层”写回 [[MCP]] 的边界段。
- [ ] 如果 Q3 混淆 MCP 和 [[Tool Calling|Function Calling]]，回看 [[Tool 接口层对比]]，必要时补一条更短的对照句。
- [ ] 如果 Q4 把 Resources 也简单叫“工具”，回看 [[MCP#三类核心能力]]，并补一个安全分级例子。
- [ ] 如果 Q5 把工具选择说成“LLM 直接调用 server”，回看 [[MCP#工具选择流程]]，补上 host / harness 的执行前检查。
- [ ] 如果 Q6 不能按副作用、敏感数据、审计要求分级，写入 [[02 问题池]] 或更新 [[Tool Permissioning]] 的复习材料。
- [ ] 如果 Q7 不能说清“两轮对话 + 中间执行”，回看 [[Tool Calling#概念详解]] 或 [[raw/repos/xiaolinnote/questions/052 ai tools 1. 什么是 Function Calling ？原理是什么？]]。
- [ ] 如果 Q8 卡在 schema 字段作用，回看 [[Tool Calling#边界细节]]，必要时把“description 影响工具选择，schema 影响参数约束”的例子写回。
- [ ] 如果 Q9 把 Function Calling 当成完整工具治理，回看 [[Tool Permissioning]]、[[Approval Gate]] 和 [[Trace]]。
- [ ] 如果 Q10 不能一口气说出工具接口层地图，回看 [[Tool 接口层对比#核心分层]]。
- [ ] 如果 Q11 只归因到模型差，回看 [[Tool Registry]] / [[Tool Permissioning]] / [[Tool Poisoning]]，补“选错工具不一定是模型能力问题”的边界。
- [ ] 如果 Q12 混淆使用场景，把“单应用私有函数 vs 多 host 复用外部能力”写回 [[Tool 接口层对比]] 或 [[05 Query 写回队列]]。
- [ ] 如果 Q13 把 MCP 说成 Tool Calling 的替代品，回看 [[MCP#边界细节]] 和 [[Tool 接口层对比]]，补上“Tool Calling 管调用意图，MCP 管外部能力接入标准”的对比句。

## 第二轮触发（可选）

只有第一轮暴露关键误解时才追加第二轮。第二轮最多聚焦 1-3 个问题，例如：

> 我能不能在 60 秒内说清：MCP 为什么是协议连接层，而不是 Agent 框架、模型 tool calling 或权限系统本身？

## 校准版（作答后对照）

MCP 是 AI 应用连接外部工具、数据源和提示模板的标准协议。它的核心价值不是让模型“自己会用工具”，而是把外部能力按统一协议暴露出来，让 host/client 可以发现、选择、授权、调用和接收结果。

角色分工上，host 是 AI 应用本身，承载模型、用户界面、权限策略和编排逻辑；client 是 host 里的协议连接模块，一个 client 通常对应一个 server 连接，负责能力发现和调用转发；server 是外部能力提供方，负责暴露 tools/resources/prompts，并真正执行读文件、查库、调用 API 等动作。

MCP 和 [[Tool Calling|Function Calling]] 不在同一层。Function Calling / Tool Calling 描述模型如何输出结构化调用意图；MCP 描述应用如何连接外部 server、发现能力、通过 [[MCP Transport]] 传输请求并接收结果。现代 Agent 往往把两者接起来：host 把 MCP server 暴露的能力映射成模型可见工具，模型输出 tool call，host 经过权限判断后通过 MCP client 调 MCP server。

最小对比句可以背成：Function Calling 是“模型到 runtime 的结构化请求格式”，MCP 是“host/client 到外部 server 的标准连接协议”。前者不自动解决工具从哪里来、是否可信、是否越权；后者不替代模型原生的 tool-call 能力，最终仍要把 server 能力映射成模型能理解的调用接口。

工具选择不是 MCP server 自己决定，也不是模型绕过 host 直接执行。典型流程是：MCP client 先发现 server 暴露的工具；host / tool registry 把工具名称、description、schema 和策略提示转成模型可见格式；模型根据用户问题和工具描述提出 tool call；host 对参数、权限、审批、预算和风险做检查；通过 MCP client 调 server；最后把结果写回上下文、state 或 trace。工具描述质量会直接影响模型是否选对工具，因此 tool metadata 也会成为 [[Tool Poisoning]] 风险面。

Tools / Resources / Prompts 的分界是权限学习重点。Tools 是主动执行，可能改变外部世界；Resources 是被动提供数据，通常只读但仍可能涉及敏感信息；Prompts 是可复用提示模板，不直接执行外部动作，但会影响模型如何理解任务。安全上不能只看名字，必须看能力的副作用、数据敏感度、参数范围、供应链可信度和是否需要审批。
