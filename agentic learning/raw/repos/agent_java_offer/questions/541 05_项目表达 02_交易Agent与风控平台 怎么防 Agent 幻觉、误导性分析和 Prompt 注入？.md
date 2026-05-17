---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - project-expression
  - agent
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/05_%E9%A1%B9%E7%9B%AE%E8%A1%A8%E8%BE%BE/02_%E4%BA%A4%E6%98%93Agent%E4%B8%8E%E9%A3%8E%E6%8E%A7%E5%B9%B3%E5%8F%B0/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/05_项目表达/02_交易Agent与风控平台/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 05_项目表达
category: 02_交易Agent与风控平台
last_checked: 2026-05-09
freshness: watch
sha256: 22745b697456cb7520291616f97a79f224b51658c42f03eba0bd3ce63a41a177
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Prompt Injection]]"
  - "[[Indirect Prompt Injection]]"
  - "[[Guardrails]]"
  - "[[Human-in-the-loop]]"
  - "[[Approval Gate]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[Agent]]"
  - "[[Agent 主题]]"
---

# 怎么防 Agent 幻觉、误导性分析和 Prompt 注入？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/05_项目表达/02_交易Agent与风控平台/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/05_%E9%A1%B9%E7%9B%AE%E8%A1%A8%E8%BE%BE/02_%E4%BA%A4%E6%98%93Agent%E4%B8%8E%E9%A3%8E%E6%8E%A7%E5%B9%B3%E5%8F%B0/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`05_项目表达` / `02_交易Agent与风控平台`  
条目类型：`question`  
父级题组：你最该准备的 12 道题
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Prompt Injection]]
- [[Indirect Prompt Injection]]
- [[Guardrails]]
- [[Human-in-the-loop]]
- [[Approval Gate]]
- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[Agent]]
- [[Agent 主题]]

## 题目正文

**6. 怎么防 [[Agent]] 幻觉、误导性分析和 [[Prompt Injection|Prompt 注入]]？**
这题在交易场景尤其要命。你应该准备：
模型输出结构化约束、只允许白名单工具、引用证据、敏感动作二次确认、风控规则优先、注入隔离、工具输出校验、策略与执行分层。
牛客的 AI 工程整理里把**幻觉、Prompt 注入攻击、自动化[[Evaluation|评估]]体系**都列成高频追问。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
