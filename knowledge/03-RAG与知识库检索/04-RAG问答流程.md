---
title: "RAG 问答流程"
type: concept
status: draft
confidence: high
depth: deep
source:
  - title: "RAG 与知识库检索参考资料"
    type: reference
    url: "../../90-references/rag-knowledge-retrieval-references.md"
    accessed: "2026-06-10"
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    type: paper
    url: "https://arxiv.org/abs/2005.11401"
    accessed: "2026-06-10"
  - title: "RAGAs: Automated Evaluation of Retrieval Augmented Generation"
    type: paper
    url: "https://arxiv.org/abs/2309.15217"
    accessed: "2026-06-10"
created: "2026-06-10"
updated: "2026-06-10"
tags: ["rag", "question-answering", "retrieval", "reranking", "grounding", "citation", "beginner"]
---

# RAG 问答流程

## 一句话结论

一个可靠的 RAG 问答流程不是“搜一下然后回答”，而是要经历问题理解、检索、过滤、重排、上下文组装、受约束生成、引用展示和质量评估的完整链路。

## 概念定位

- 它是什么：用户提问后，RAG 系统从知识库中找证据并生成答案的运行时流程。
- 它不是什么：不是只把搜索结果拼到 prompt 里，也不是让模型自由发挥。
- 相邻概念：query rewriting、retrieval、reranking、context packing、grounded generation、citation、abstention。
- 前置知识：RAG 基础、embedding、chunk、metadata、prompt、上下文窗口。

初学者可以先记住：

```text
RAG 问答 = 找证据 + 判断证据够不够 + 基于证据回答 + 告诉用户证据来自哪里。
```

## 缩写全称速查

| 缩写 | 英文全称 | 中文解释 | 初学者理解 |
| --- | --- | --- | --- |
| RAG | Retrieval-Augmented Generation | 检索增强生成 | 先检索资料，再基于资料回答 |
| QA | Question Answering | 问答 | 根据问题生成答案 |
| LLM | Large Language Model | 大语言模型 | 负责理解问题和生成答案 |
| IR | Information Retrieval | 信息检索 | 找相关资料 |
| BM25 | Best Matching 25 | 经典关键词检索排序函数 | 适合精确词、术语、编号 |
| MMR | Maximal Marginal Relevance | 最大边际相关性 | 选择相关但不重复的多个片段 |
| HyDE | Hypothetical Document Embeddings | 假设文档嵌入 | 先让模型生成一个假设答案/文档，再用它做检索 |
| CoT | Chain of Thought | 思维链 | 让模型显式或隐式分步推理；生产系统不一定展示给用户 |
| UI | User Interface | 用户界面 | 展示回答、引用、加载、错误和拒答状态 |
| UX | User Experience | 用户体验 | 用户是否觉得系统清楚、可控、可信 |

Abstention 不是缩写，意思是“拒答”或“保留回答”。在 RAG 中，如果证据不足，系统应该能说“不知道”。

## 核心概念

RAG 问答流程里有四个关键判断：

1. 用户到底在问什么。
2. 知识库里哪些资料可能相关。
3. 这些资料是否足够支持答案。
4. 答案是否忠实于资料。

如果只做第 2 步，系统很容易变成“有搜就答”。可靠 RAG 必须在检索之后继续判断证据质量。

## 机制与原理

一个完整流程可以拆成九步。

### 1. 接收问题

输入可能是：

```text
RAG 和 agent 是什么关系？
```

系统需要保留：

- 原始问题。
- 用户身份和权限。
- 当前会话上下文。
- 可用知识库范围。

### 2. 问题理解或改写

用户问题可能口语化、含省略或上下文引用。

例子：

```text
那它和 tool calling 有什么区别？
```

这里的“它”可能指 RAG。系统可以改写成：

```text
RAG 和 tool calling 有什么区别？
```

Query rewriting 指“查询改写”，用于把用户问题改写成更适合检索的查询。但改写可能引入误解，所以要谨慎。

### 3. 检索候选资料

可以组合多种检索：

- 关键词检索：找精确术语。
- 向量检索：找语义相似。
- metadata 过滤：限定章节、时间、权限、标签。
- hybrid search：关键词和向量结合。

例如：

```text
query: "RAG tool calling agent 区别"
filter: section = "03-RAG与知识库检索" OR "02-Agent基础与工具调用"
```

### 4. 重排和去重

初始检索结果可能很多，也可能重复。Reranking 指“重排”，通常用更精细的模型或规则重新判断 query 和候选片段的相关性。

去重很重要。top-k 里如果 5 条都来自同一个段落的重复版本，就会挤掉其他必要证据。

### 5. 判断证据是否足够

这一步经常被忽略。系统要判断：

- 检索结果是否直接回答问题。
- 是否有定义、机制、对比或例子。
- 是否有冲突资料。
- 是否缺少关键前提。
- 是否包含过时内容。

如果证据不足，不应该硬答。

### 6. 组装上下文

Context packing 指把多个检索片段组织成模型上下文。

好的上下文应该：

- 放入最相关、最可信的片段。
- 保留标题、来源、更新时间。
- 避免重复内容。
- 控制 token 长度。
- 把用户无权查看的资料排除。

### 7. 受约束生成

给模型的指令应该明确：

```text
只根据提供的资料回答。
资料不足时说明不足。
不要编造引用。
回答里标明来源。
如果资料冲突，说明冲突。
```

这一步叫 grounded generation，即“基于证据的生成”。Grounding 的意思是让答案落在资料证据上。

### 8. 引用和不确定性展示

可靠 RAG 输出不应只有答案，还应给来源：

```text
答案：RAG 主要解决知识访问，tool calling 主要解决行动执行。
来源：
- knowledge/03-RAG与知识库检索/06-RAG与Agent的关系.md
- knowledge/02-Agent基础与工具调用/01-Tool-Calling.md
```

如果资料不够：

```text
当前知识库没有足够资料说明这个框架的最新 API 行为，需要查官方文档。
```

### 9. 记录和评估

记录 trace：

- 用户问题。
- 改写后的 query。
- 检索到的 chunk。
- 重排分数。
- 最终上下文。
- 模型答案。
- 引用。
- 用户反馈。

没有 trace，就很难知道 RAG 为什么答错。

## 适用场景

- 知识库问答。
- 技术文档助手。
- 客服 FAQ。
- 内部流程查询。
- 研究资料总结。
- 代码库解释。
- 个人学习资料检索。

## 不适用场景

- 需要精确执行动作，优先 tool calling。
- 需要实时交易数据，优先数据库或业务 API。
- 用户只想要创意写作，不需要外部资料。
- 资料没有清洗、来源不明、冲突严重，却要求确定答案。
- 权限无法过滤，不适合把资料放进统一检索。

## 前提、边界与反例

- 必要前提：知识库可检索、chunk 可引用、权限可过滤、生成指令明确。
- 适用边界：RAG 能提升知识依据，但不能保证资料本身正确。
- 反例或例外：用户问“我这个订单发货了吗”，应该查订单 API，不该从文档里猜。
- 结论可能失效的条件：query 改写错误、召回不足、上下文过长、引用丢失、模型忽略资料。

## 对比与替代方案

| 方案 | 适合 | 优点 | 局限 |
| --- | --- | --- | --- |
| Naive RAG | 快速原型 | 简单 | 容易错召回、无证据判断 |
| Advanced RAG | 生产问答 | 有改写、重排、过滤、引用 | 系统复杂 |
| Agentic RAG | 多步检索和工具组合 | 能分解问题、反复检索 | 成本和不确定性更高 |
| Database QA | 精确结构化数据 | 准确、可审计 | 不适合开放文本解释 |
| Human research | 高风险研究 | 质量高 | 慢、成本高 |

## 示例或最小实验

任务：让知识库回答“为什么 RAG 不能完全解决幻觉？”

### 检索

候选片段：

```text
1. 01-RAG基础概念.md / 常见误区：RAG 可以降低一部分知识幻觉，但检索错、资料错、模型忽略资料时仍会幻觉。
2. 05-RAG失败模式.md / 失败模式：检索不到、检索错、上下文不足、引用幻觉。
```

### 生成指令

```text
请只根据以下资料回答。
如果资料不足，请明确说明。
回答必须包含至少一个来源文件。
```

### 好答案

```text
RAG 不能完全解决幻觉，因为它只是把外部资料引入生成过程；如果检索阶段找错资料、资料本身过时或错误、上下文不够完整，模型仍可能生成错误答案。另外，即使资料正确，模型也可能没有严格按资料回答，出现引用幻觉或脱离资料扩写。

来源：knowledge/03-RAG与知识库检索/01-RAG基础概念.md；knowledge/03-RAG与知识库检索/05-RAG失败模式.md
```

### 坏答案

```text
RAG 可以彻底避免幻觉，因为模型有了知识库。
```

错误：结论过度，且没有来源。

## 失败模式与风险

- Query 改写错：把用户问题改成了另一个问题。
- 检索召回低：正确资料没被拿到。
- 重排误杀：相关资料被 reranker 排到后面。
- 上下文过长：塞太多资料，模型抓不住重点。
- 上下文冲突：资料互相矛盾但模型没说明。
- 引用错位：答案引用了不支持该结论的片段。
- 拒答不足：证据不足时仍然硬答。
- 拒答过度：明明资料够，却因为规则太严不回答。
- 权限绕过：检索阶段没先过滤用户权限。

## 常见误区

- 误区：RAG 只要检索 top-5 就行。
  - 修正：top-k 只是候选数量，还要看相关性、覆盖度、重复和证据充分性。
- 误区：把更多 chunk 放进 prompt 会更准。
  - 修正：更多上下文可能引入噪声，削弱重点。
- 误区：模型会自动知道哪些资料更可信。
  - 修正：需要 metadata、来源质量、更新时间和指令约束。
- 误区：引用文件名就代表答案有证据。
  - 修正：引用必须支持具体主张，否则只是装饰。
- 误区：RAG UI 只显示最终答案就够。
  - 修正：用户需要看到来源、资料不足、加载和错误状态。

## 实践判断

- 什么时候应该采用完整流程：用户依赖答案做决策，知识库较大，答案需要来源。
- 什么时候可以简化：内部原型、资料少、无高风险决策。
- 落地时最先验证什么：正确资料是否进上下文，答案是否引用正确，证据不足时是否拒答。
- 可观察指标或检查点：context precision、context recall、faithfulness、answer relevance、citation accuracy、abstention accuracy。

## 来源与证据

- 来源：`90-references/rag-knowledge-retrieval-references.md`；RAG 原论文；RAGAS 论文。
- 证据摘要：RAG 原论文支持检索文档增强生成；RAGAS 将 RAG 评估拆成 faithfulness、answer relevance、context relevance 等维度，支持不能只看最终答案的判断；本卡的 query rewriting、reranking、context packing 是工程流程扩展。
- 可信度判断：RAG 问答主链路可信度高；不同系统是否需要 HyDE、reranking 或 agentic retrieval 需要实验确认。

### 关键主张表

| 主张 | 证据 | 来源 | 可信度 | 局限 |
| --- | --- | --- | --- | --- |
| RAG 问答需要检索和生成两个核心阶段 | RAG 原论文 | high | 现代系统增加了更多工程步骤 |
| 只看最终答案不足以评估 RAG | RAGAS 把上下文和答案维度分开评估 | RAGAS paper | high | 具体指标实现要校准 |
| 证据不足时应拒答或说明不足 | grounded generation 的可靠性要求 | 工程推断 | high | 拒答阈值依赖业务 |
| 引用必须支持具体主张 | 引用用于可追溯和验证 | 工程推断 | high | 自动判定引用支持很难 |

## 待验证问题

- 本知识库问答是否需要 query rewriting，还是直接搜索标题和正文即可。
- 是否应默认使用 reranking，还是先用 hybrid search。
- 引用应该精确到文件、标题，还是未来精确到 chunk。
- 如果多个笔记冲突，回答应该按最新更新时间排序还是按来源可信度排序。

## 变更记录

- 2026-06-10：创建深度初稿，补充 RAG 问答的九步流程、引用、拒答、trace 和评估维度。
