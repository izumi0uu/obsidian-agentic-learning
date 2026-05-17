---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - ai
  - agent
  - framework
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/08_%E6%A1%86%E6%9E%B6%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%8C%96/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/08_框架协议与工程化/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 08_框架协议与工程化
last_checked: 2026-05-09
freshness: watch
sha256: cf96c74e9c5830346d84f7a6a2e8083ddee0742786ce464ff2ea8bcb7853dc55
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Tool Calling]]"
  - "[[Tool Use]]"
  - "[[Durable Execution]]"
  - "[[Agent]]"
  - "[[LLM]]"
  - "[[Agent Framework]]"
---

# Tool Use 是扩展 Agent 能力的有效途径。请解释 LLM 是如何学会调用外部 API 或工具的？（可以从 Function Calling 的角度解释）

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/08_框架协议与工程化/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/08_%E6%A1%86%E6%9E%B6%E5%8D%8F%E8%AE%AE%E4%B8%8E%E5%B7%A5%E7%A8%8B%E5%8C%96/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `08_框架协议与工程化`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Tool Calling]]
- [[Tool Use]]
- [[Durable Execution]]
- [[Agent]]
- [[LLM]]
- [[Agent Framework]]

## 题目正文

### 2. 子问题：[[Tool Use]] 是扩展 [[Agent]] 能力的有效途径。请解释 [[LLM]] 是如何学会调用外部 API 或工具的？（可以从 [[Tool Calling|Function Calling]] 的角度解释）

答：
Function Calling 的核心是给模型一份结构化工具说明（名称、功能、参数 Schema），让它在对话中先判断“要不要调工具”，再输出结构化调用参数。agent编排层执行工具后，把结果回填给模型做二次生成。面试可补一句：线上稳定性取决于参数校验、超时重试、幂等处理和失败降级，不只是模型会不会调用。

**Function Calling的工作原理如下：**

1. **工具定义与注册 (Tool Definition & Registration):**
  - 对于每一个工具，我们需要定义：
    - **函数名称 (Function Name):**
    - **函数描述 (Function Description):** 用自然语言清晰地描述这个函数的功能。
    - **参数列表 (Parameters):** 定义函数需要哪些输入参数，每个参数的名称、类型、和描述。
2. **LLM的决策与意图识别 (LLM's Decision & Intent Recognition):**
  - 在与用户交互时，我们将用户的提问**连同所有已注册的工具描述**一起发送给LLM。
  - LLM会分析用户的意图。如果它认为只靠自身知识无法回答，且用户的意图与某个工具的功能相匹配，它就会决定调用该工具。
3. **生成结构化的调用指令 (Generating Structured Calling Instructions):**
  - 当LLM决定调用工具时，它的输出**不再是自然语言文本**，而是一个特殊格式的、结构化的**JSON对象**（或其他格式）。
  - 这个JSON对象会精确地包含：
    - **要调用的函数名称**。
    - **一个包含所有参数名和值的对象**。
  - 例如，对于用户提问“今天新加坡天气怎么样？”，LLM可能输出：
    ```
    {
      "tool_call": {
        "name": "get_current_weather",
        "arguments": {
          "location": "Singapore",
          "unit": "celsius"
        }
      }
    }
    ```
4. **外部执行与结果返回 (External Execution & Result Return):**
  - Agent的控制代码（Orchestrator）会捕获这个特殊的JSON输出。
  - 它会解析JSON，找到函数名和参数，然后在**外部环境中实际执行**这个函数（例如，调用一个真实的天气API）。
  - 函数执行完毕后，会返回一个结果（例如，`{"temperature": 32, "condition": "sunny"}`）。
5. **整合结果并生成最终回复 (Integrating Result & Generating Final Response):**
  - 控制代码将工具的返回结果**再次格式化**，并将其作为新的上下文信息，连同之前的对话历史一起，再次发送给LLM。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
