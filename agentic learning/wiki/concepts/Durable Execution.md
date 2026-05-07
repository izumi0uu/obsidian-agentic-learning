---
type: concept
topic:
  - agent
  - workflow
  - infrastructure
status: seed
created: 2026-05-06
updated: 2026-05-06
last_checked: 2026-05-07
freshness: stable
conflicts: []
source:
  - "[[Agent 工程基础设施主源]]"
  - "[[Agent 工程基础设施主源]]"
evidence:
  - "[[Agent 工程基础设施主源#为什么收]]"
  - "[[Agent 工程基础设施主源#为什么收]]"
related:
  - "[[Agent Loop]]"
  - "[[Memory]]"
  - "[[Replay]]"
  - "[[Agent Harness]]"
---

# Durable Execution

## 一句话

Durable Execution 是让长任务可以暂停、恢复、重试、记录状态并在失败后继续执行的运行能力。

## 它解决什么问题

Agent 任务可能持续几分钟到几天，中途会遇到网络失败、工具失败、人工等待、进程重启和模型错误。没有 durable execution，任务状态容易丢失。

代表生态包括 Temporal、Restate、Inngest、LangGraph durable execution。

## 它不是什么

Durable Execution 不是记忆本身。

它保存的是运行状态和步骤进度；长期用户偏好、知识和经验仍属于 [[Memory]] 或数据库层。

## 最小例子

```text
step 1 retrieve data
step 2 wait for approval
step 3 call tool
step 4 retry if transient failure
step 5 resume after process restart
```

## 常见误解和风险

- 重试不可逆动作可能造成重复付款、重复邮件或重复写入。
- 状态持久化也需要权限和隐私控制。
- durable 不等于正确，仍然要 eval 和 audit。

## 证据锚点

- Source: [[Agent 工程基础设施主源]]
- Source: [[Agent 工程基础设施主源]]
- Anchor: source note 小节级；段落/页码级证据待精读时补。
- Confidence: medium

## 相关链接

- [[Agent Loop]]
- [[Memory]]
- [[Replay]]
- [[Agent Harness]]
