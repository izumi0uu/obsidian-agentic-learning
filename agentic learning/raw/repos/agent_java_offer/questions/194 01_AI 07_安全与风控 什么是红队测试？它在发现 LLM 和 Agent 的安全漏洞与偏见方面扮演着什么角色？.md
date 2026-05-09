---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "ai"
  - "agent"
  - "security"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/07_%E5%AE%89%E5%85%A8%E4%B8%8E%E9%A3%8E%E6%8E%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/01_AI/07_安全与风控/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "01_AI"
category: "07_安全与风控"
last_checked: 2026-05-09
freshness: watch
sha256: 7c2e01b3a4e624b13e55aa3d3c259520dc944993e906f27d4f4dbf6008f22b11
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
  - "[[Agent Loop]]"
  - "[[Agent]]"
  - "[[LLM]]"
  - "[[Guardrails]]"
---

# 什么是红队测试？它在发现 LLM 和 Agent 的安全漏洞与偏见方面扮演着什么角色？

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/01_AI/07_安全与风控/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/01_AI/07_%E5%AE%89%E5%85%A8%E4%B8%8E%E9%A3%8E%E6%8E%A7/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`01_AI` / `07_安全与风控`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki

- [[Agent Loop]]
- [[Agent]]
- [[LLM]]
- [[Guardrails]]

## 题目正文

### 3. 子问题：什么是红队测试？它在发现 LLM 和 Agent 的安全漏洞与偏见方面扮演着什么角色？

答：
它的价值是发现常规测试覆盖不到的高风险边界情况，尤其对 Agent 很关键，因为 Agent 具备执行能力。红队测试是用攻击者视角主动找Agent系统弱点, 以评估和提升其安全性和鲁棒性。常见手法有越权请求、提示注入、越狱诱导、工具滥用。实践上红队结果应回流到规则护栏、权限策略和训练数据，形成持续加固闭环。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
