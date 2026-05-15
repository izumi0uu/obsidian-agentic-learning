---
type: source
source_type: repo
site: github.com
repo: "guoguo-tju/agent_java_offer"
topic:
  - "interview"
  - "java"
  - "backend"
status: inbox
created: 2026-05-09
updated: 2026-05-09
url: "https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/10_%E7%BD%91%E7%BB%9CI_O%E4%B8%8E%E5%8F%91%E5%B8%83%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md"
source: "https://github.com/guoguo-tju/agent_java_offer"
source_path: "docs/interview_prep/02_后端/10_网络I_O与发布治理/01_核心问答.md"
commit: "12bf4c915cca01f513e040935e1917d3687f8b35"
entry_type: "question"
direction: "02_后端"
category: "10_网络I_O与发布治理"
last_checked: 2026-05-09
freshness: watch
sha256: c39aa02f077daa10f46bcd7cbda9ad8c715c38156051f2fa27f1fae614eeecaa
license: "CC BY-NC 4.0"
related:
  - "[[agent_java_offer Repo]]"
  - "[[raw/repos/agent_java_offer/agent_java_offer 面试题索引]]"
  - "[[资料收集索引]]"
---

# 堆外内存（off-heap）

原始仓库：<https://github.com/guoguo-tju/agent_java_offer>  
原始文件：[docs/interview_prep/02_后端/10_网络I_O与发布治理/01_核心问答.md](https://github.com/guoguo-tju/agent_java_offer/blob/12bf4c915cca01f513e040935e1917d3687f8b35/docs/interview_prep/02_%E5%90%8E%E7%AB%AF/10_%E7%BD%91%E7%BB%9CI_O%E4%B8%8E%E5%8F%91%E5%B8%83%E6%B2%BB%E7%90%86/01_%E6%A0%B8%E5%BF%83%E9%97%AE%E7%AD%94.md)  
提交：`12bf4c9`  
分类：`02_后端` / `10_网络I_O与发布治理`  
条目类型：`question`  
许可证：CC BY-NC 4.0；本页保留为 raw source evidence，后续再决定是否拆入概念卡或面试复盘页。

## 相关知识 wiki


## 题目正文

### 堆外内存（off-heap）

使用 `ByteBuffer.allocateDirect()` 可以申请堆外内存。优势是：
- 网络 I/O 或文件 I/O 时，数据本来就会进入堆外区域；
- 如果直接使用堆外内存，就可以减少一次从堆内到堆外的拷贝。

回收要点：
- 可通过 `-XX:MaxDirectMemorySize` 限制最大堆外内存；
- DirectByteBuffer 对象失去引用后，在 GC 时可能回收并释放堆外内存；
- 堆外内存如果持续泄漏，也会触发 OOM。

## 边界提醒

这是来自面试资料库的原始题目/答案片段，适合练习口述和追问。涉及概念定义、工程边界或时效性事实时，仍需要回到论文、官方文档、框架源码或 `wiki/concepts/` 校准。
