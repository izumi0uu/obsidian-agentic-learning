---
type: source
source_type: repo
site: github.com
repo: guoguo-tju/agent_java_offer
topic:
  - interview
  - ai
  - agent
  - memory
status: inbox
created: 2026-05-09
updated: 2026-05-15
url: https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/04_%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B%E4%B8%8E%E8%AE%B0%E5%BF%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md
source: https://github.com/guoguo-tju/agent_java_offer
source_path: docs/interview_prep/01_AI/04_上下文工程与记忆/01_核心问答.md
commit: 12bf4c915cca01f513e040935e1917d3687f8b35
entry_type: question
direction: 01_AI
category: 04_上下文工程与记忆
last_checked: 2026-05-09
freshness: watch
sha256: 67aba5b482caca71e3d07220245dafffe15d7f3860bf7c4e10008395f14f8ca3
license: CC BY-NC 4.0
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Evaluation]]"
  - "[[Benchmark]]"
  - "[[Task Success Rate]]"
  - "[[RAG]]"
  - "[[Context Engineering]]"
  - "[[Agent]]"
  - "[[Observability]]"
  - "[[Top-K]]"
  - "[[Prompt]]"
  - "[[Token]]"
  - "[[Agent 主题]]"
---

# [[Prompt]] Engineering 及 Prompt 优化策略有哪些？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/04_上下文工程与记忆/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/04_%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B%E4%B8%8E%E8%AE%B0%E5%BF%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `04_上下文工程与记忆`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Evaluation]]
- [[Benchmark]]
- [[Task Success Rate]]
- [[RAG]]
- [[Context Engineering]]
- [[Agent]]
- [[Observability]]
- [[Top-K]]
- [[Prompt]]
- [[Token]]
- [[Agent 主题]]

## 题目正文

### 3. 子问题：Prompt Engineering 及 Prompt 优化策略有哪些？

答：

“我会把 Prompt 当成预算管理问题来做，核心是**高信号、低冗余**。具体有五个手段：

1. **分层提示**：把稳定不变的规则放 system，任务相关信息放 user，避免每次重复拼接大段固定文本。
2. **最小必要上下文**：只传当前任务必需信息，历史对话做摘要而不是全量回放。
3. **检索按需注入**：[[RAG]] 只注入 [[Top-K|top-k]] 片段，并设置 [[Token|token]] 上限，不把整篇文档塞进去。
4. **结构替代长文本**：用 schema、枚举、字段约束替代长篇文字说明，减少 token 同时提升可控性。
5. **监测与A/B实验**：监控首 token 时延、总 token、[[Task Success Rate|成功率]]和成本，按指标裁剪 Prompt

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
