---
title: "RAG 失败模式"
type: concept
status: draft
confidence: high
depth: deep
source:
  - title: "RAG 与知识库检索参考资料"
    type: reference
    url: "../../90-references/rag-knowledge-retrieval-references.md"
    accessed: "2026-06-10"
  - title: "Sufficient Context: A New Lens on Retrieval Augmented Generation Systems"
    type: article
    url: "https://research.google/blog/sufficient-context-a-new-lens-on-retrieval-augmented-generation-systems/"
    accessed: "2026-06-10"
  - title: "RAGAs: Automated Evaluation of Retrieval Augmented Generation"
    type: paper
    url: "https://arxiv.org/abs/2309.15217"
    accessed: "2026-06-10"
created: "2026-06-10"
updated: "2026-06-10"
tags: ["rag", "failure-modes", "hallucination", "retrieval", "evaluation", "grounding", "stale-info"]
---

# RAG 失败模式

## 一句话结论

RAG 答错通常不是一个原因，而是资料、切分、检索、重排、上下文、生成、引用、权限或评估某一环出了问题；排查时要先定位失败发生在哪一步。

## 概念定位

- 它是什么：对 RAG 系统常见错误路径的分类和诊断框架。
- 它不是什么：不是把所有问题都归因于“模型幻觉”，也不是加更多资料就能解决。
- 相邻概念：hallucination、retrieval failure、grounding、citation error、context sufficiency、RAG evaluation。
- 前置知识：RAG 问答流程、embedding、chunk、metadata、trace、eval。

初学者可以先记住：

```text
RAG 出错时，先问：正确证据有没有进入模型上下文？
如果没有，是检索问题。
如果有但答错，是生成或约束问题。
如果证据本身错，是知识库治理问题。
```

## 缩写全称速查

| 缩写 | 英文全称 | 中文解释 | 初学者理解 |
| --- | --- | --- | --- |
| RAG | Retrieval-Augmented Generation | 检索增强生成 | 先检索资料再回答 |
| LLM | Large Language Model | 大语言模型 | 生成答案的模型 |
| Eval | Evaluation | 评估 | 判断 RAG 表现是否可靠 |
| QA | Question Answering | 问答 | 用户问，系统答 |
| PII | Personally Identifiable Information | 个人可识别信息 | 可能泄露个人身份的数据 |
| ACL | Access Control List | 访问控制列表 | 记录谁能访问某个资源 |
| RBAC | Role-Based Access Control | 基于角色的访问控制 | 按角色控制资料访问 |
| SLA | Service Level Agreement | 服务等级协议 | 对系统可用性和响应时间的承诺 |
| P95 | 95th Percentile | 第 95 百分位 | 95% 请求比这个延迟值更快，用来看尾部体验 |
| MTTR | Mean Time To Recovery | 平均恢复时间 | 系统出错后恢复正常平均需要多久 |

Hallucination 不是缩写，通常译为“幻觉”。在 RAG 里，它指模型输出了资料不支持、事实不成立或引用不真实的内容。

## 核心概念

RAG 失败可以按链路分成八类：

| 环节 | 失败类型 | 表现 |
| --- | --- | --- |
| 资料 | 知识库错误 | 文档过时、来源不明、互相冲突 |
| 切分 | chunk 错误 | 片段太碎、太长、标题丢失 |
| 检索 | 召回失败 | 正确资料没有进候选 |
| 排序 | 排名失败 | 正确资料有但排太后 |
| 上下文 | 证据不足 | 模型看到的上下文不够支持答案 |
| 生成 | 忠实度失败 | 模型没有按资料回答 |
| 引用 | 引用失败 | 来源不支持结论或引用不存在 |
| 权限 | 安全失败 | 检索到用户不该看的资料 |

Google Research 的 sufficient context 视角很有启发：要先判断提供给模型的上下文是否足以回答问题。如果上下文本身不够，模型答错不是单纯“模型不行”，而是 RAG 输入条件不成立。

## 机制与原理

排查 RAG 失败时，可以按这个顺序：

```text
1. 用户问题是什么？
2. 正确答案需要哪些证据？
3. 知识库里有没有这些证据？
4. 文档有没有被正确切分和标注？
5. 检索 top-k 里有没有正确 chunk？
6. 重排后正确 chunk 是否仍在上下文中？
7. 模型是否按照上下文回答？
8. 引用是否支持具体主张？
9. 用户是否有权限看到这些资料？
```

这比直接改 prompt 更可靠。很多 RAG 问题不是 prompt 能解决的。

### 失败定位表

| 现象 | 可能原因 | 优先检查 |
| --- | --- | --- |
| 完全答不到点 | query 改写或检索失败 | 检索 top-k |
| 答案只对一半 | chunk 缺上下文或证据不完整 | chunk 和 context |
| 答案很流畅但无来源 | 生成约束弱 | prompt 和引用逻辑 |
| 引用文件存在但不支持结论 | citation grounding 失败 | 引用到句子级证据 |
| 总是答旧版本 | 索引未刷新或 metadata 排序错 | updated_at 和索引重建 |
| 低权限用户看到内部资料 | 权限过滤缺失 | retrieval 前权限过滤 |
| 有时很慢 | top-k 太大、rerank 太重、索引慢 | latency trace |

## 适用场景

- RAG 知识库问答上线前质检。
- 用户反馈“答案不准”后的问题定位。
- 设计 RAG eval 样例。
- 比较不同切分、embedding、rerank 策略。
- 给 agent 添加 retrieval 工具前做风险审查。

## 不适用场景

- 纯创意写作，不要求外部资料。
- 精确数据库查询错误，应先检查业务 API。
- 用户问题本身没有明确答案，不能用单一正确性评估。
- 资料还没整理，过早做复杂诊断意义不大。

## 前提、边界与反例

- 必要前提：能记录 trace，能看到检索候选、上下文和最终答案。
- 适用边界：失败模式能帮助定位问题，但不能自动修复资料质量。
- 反例或例外：如果知识库没有相关资料，RAG 正确行为应是拒答，不是努力编一个答案。
- 结论可能失效的条件：没有日志、检索系统黑箱、用户问题涉及外部最新事实但知识库未更新。

## 对比与替代方案

| 排查方式 | 优点 | 局限 |
| --- | --- | --- |
| 看最终答案 | 快 | 无法定位过程 |
| 看检索 top-k | 能发现召回问题 | 不知道模型如何使用上下文 |
| 看完整 trace | 最利于诊断 | 需要记录和隐私治理 |
| 人工标注失败类型 | 质量高 | 成本高 |
| 自动 RAG eval | 可规模化 | 指标和 grader 需要校准 |
| 用户反馈按钮 | 贴近真实使用 | 信号稀疏且不稳定 |

## 示例或最小实验

问题：

```text
RAG 能不能保证没有幻觉？
```

### 情况 A：检索失败

检索结果：

```text
1. Embedding 的定义
2. MCP 的作用
3. Tool calling 的流程
```

诊断：没有召回 RAG 失败模式或常见误区，属于 retrieval failure。

### 情况 B：上下文不足

检索结果：

```text
RAG 能降低幻觉。
```

诊断：这句话不够支持“能不能保证没有幻觉”。需要召回“RAG 不能彻底解决幻觉”的边界说明。

### 情况 C：生成失败

检索结果包含：

```text
RAG 能降低一部分知识幻觉，但检索错、资料错、模型忽略资料时仍会幻觉。
```

模型回答：

```text
RAG 可以完全消除幻觉。
```

诊断：证据已进入上下文，但模型没有忠实回答，属于 faithfulness failure。

## 失败模式与风险

### 1. 知识库治理失败

- 来源不明。
- 内容过时。
- 同一概念多篇笔记互相冲突。
- 草稿和验证内容混在一起。
- 用户个人经验被写成事实。

### 2. 解析和切分失败

- PDF 表格错位。
- Markdown 标题丢失。
- 代码块被截断。
- 表格表头和数据分离。
- chunk 没有来源路径。

### 3. 检索失败

- 用户问题和文档表达不同。
- 缩写没有全称，导致检索不到。
- top-k 太小。
- embedding 模型不适合中文或领域术语。
- 关键词、向量和 metadata 没有结合。

### 4. 上下文失败

- 相关资料太多，超过上下文窗口。
- 只放结论，没放条件和反例。
- 把冲突资料混在一起但不提示模型。
- 把低可信资料和高可信资料同等对待。

### 5. 生成失败

- 模型过度补全资料没有说的内容。
- 模型忽略“资料不足就说不知道”的指令。
- 模型把来源 A 的结论归到来源 B。
- 模型用常识覆盖知识库内容。

### 6. 产品失败

- UI 不显示来源。
- 用户看不到资料不足。
- 错误状态只显示“失败”，不说明是检索、权限还是模型错误。
- 没有反馈入口。
- 没有人工复盘流程。

## 常见误区

- 误区：RAG 错了就是模型太弱。
  - 修正：先检查资料是否召回、上下文是否足够、引用是否支持。
- 误区：提高 top-k 就能修复召回。
  - 修正：top-k 增大可能同时带来噪声，需要看 context precision。
- 误区：重排器能修复所有检索问题。
  - 修正：如果初始召回没有正确资料，重排也救不了。
- 误区：答案带引用就可信。
  - 修正：引用必须支持具体句子，否则可能是引用幻觉。
- 误区：用户没投诉就说明 RAG 没问题。
  - 修正：用户可能没发现错误，尤其是专业知识场景。

## 实践判断

- 什么时候应该重点排查检索：正确资料明明存在，但答案没用到。
- 什么时候应该重点排查生成：正确资料进入上下文，但答案仍然违背资料。
- 什么时候应该重点排查知识库：多个来源冲突、资料过时、无证据。
- 落地时最先验证什么：每个失败答案的正确证据是否进入上下文。
- 可观察指标或检查点：context recall、context precision、faithfulness、citation accuracy、stale retrieval rate、permission leak rate。

## 来源与证据

- 来源：`90-references/rag-knowledge-retrieval-references.md`；Google Research sufficient context；RAGAS 论文。
- 证据摘要：Google Research 提供 sufficient context 视角，强调上下文是否足以回答问题；RAGAS 将 RAG 评估拆成上下文和答案质量维度；本卡的失败定位表来自 RAG 工程实践和本知识库质量规则。
- 可信度判断：失败模式分类可信度高；具体指标和阈值需要根据本知识库 RAG 实验建立。

### 关键主张表

| 主张 | 证据 | 来源 | 可信度 | 局限 |
| --- | --- | --- | --- | --- |
| RAG 失败应先看上下文是否足够 | sufficient context 视角 | Google Research | high | 具体判断可能需要人工或 grader |
| 最终答案评估不足以定位问题 | RAGAS 拆分 context 与 answer 维度 | RAGAS paper | high | 自动指标需校准 |
| 引用不等于证据支持 | 引用可能错位或不支持结论 | 工程推断 | high | 句子级验证较难 |
| 权限过滤必须在检索阶段前后都考虑 | 检索可能召回无权资料 | 安全工程实践 | high | 具体实现依赖权限系统 |

## 待验证问题

- 本知识库是否要为每篇笔记增加 `verified_claims` 区域，方便 RAG 引用。
- viewer 是否需要显示“资料不足”的显式状态。
- 中文 RAG 评估中，faithfulness 是否适合用模型 grader 初筛。
- 如何记录每次问答的 top-k 结果，方便后续复盘。

## 变更记录

- 2026-06-10：创建深度初稿，补充 RAG 失败分类、诊断流程、示例、评估指标和产品风险。
