---
title: "RAG 与知识库检索参考资料"
type: reference
status: verified
confidence: high
depth: deep
source:
  - title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    type: paper
    url: "https://arxiv.org/abs/2005.11401"
    accessed: "2026-06-10"
  - title: "Dense Passage Retrieval for Open-Domain Question Answering"
    type: paper
    url: "https://arxiv.org/abs/2004.04906"
    accessed: "2026-06-10"
  - title: "Precise Zero-Shot Dense Retrieval without Relevance Labels"
    type: paper
    url: "https://arxiv.org/abs/2212.10496"
    accessed: "2026-06-10"
  - title: "RAGAs: Automated Evaluation of Retrieval Augmented Generation"
    type: paper
    url: "https://arxiv.org/abs/2309.15217"
    accessed: "2026-06-10"
  - title: "OpenAI Embeddings"
    type: official-doc
    url: "https://platform.openai.com/docs/guides/embeddings"
    accessed: "2026-06-10"
  - title: "OpenAI File search"
    type: official-doc
    url: "https://platform.openai.com/docs/guides/tools-file-search"
    accessed: "2026-06-10"
  - title: "LangChain Retrieval-augmented generation"
    type: official-doc
    url: "https://python.langchain.com/docs/tutorials/rag/"
    accessed: "2026-06-10"
  - title: "Sufficient Context: A New Lens on Retrieval Augmented Generation Systems"
    type: article
    url: "https://research.google/blog/sufficient-context-a-new-lens-on-retrieval-augmented-generation-systems/"
    accessed: "2026-06-10"
created: "2026-06-10"
updated: "2026-06-10"
tags: ["rag", "retrieval", "embedding", "vector-search", "evaluation", "official-doc", "paper", "source-review"]
---

# RAG 与知识库检索参考资料

## 来源信息

- 标题：RAG 原论文、DPR、HyDE、RAGAS、OpenAI Embeddings、OpenAI File search、LangChain RAG、Google Research sufficient context
- 作者或机构：Meta AI、Facebook AI Research、University of Waterloo、Exploding Gradients、OpenAI、LangChain、Google Research 等
- 类型：论文、官方文档、研究博客
- 访问日期：2026-06-10

## 一句话结论

RAG 的可靠性来自“检索是否能找到足够相关且可信的上下文”与“生成是否被上下文约束并能正确引用”，因此学习 RAG 必须同时理解 embedding、检索、切分、索引、重排、上下文构造、引用和评估。

## 核心观点

- RAG，全称 Retrieval-Augmented Generation，最初是把参数化记忆中的生成模型和非参数化记忆中的外部文档检索结合起来，用于知识密集型任务。
- Embedding，全称可理解为 vector embedding，是把文本映射成向量，用距离或相似度支持语义搜索。
- Dense retrieval 通过稠密向量检索相关段落，DPR 论文是开放域问答中密集检索的重要代表。
- HyDE，全称 Hypothetical Document Embeddings，通过先生成假设文档再检索，可以改善某些零样本检索场景，但会引入额外模型调用和潜在偏差。
- RAGAS 关注 RAG 评估中的 faithfulness、answer relevance、context relevance 等维度，提醒评估不能只看最终答案。
- OpenAI embeddings 和 file search 文档适合支持 OpenAI 平台下 embedding、vector store 和文件检索工具行为。
- Google Research 的 sufficient context 视角强调：很多 RAG 失败不是生成模型“不会答”，而是检索上下文根本不足以支持答案。

## 资料可信度评估

- 来源层级：原始论文与官方文档属于 Tier 1；Google Research 博客属于 Tier 2；LangChain 官方文档属于框架官方资料，适合工程流程参考。
- 是否为一手资料：RAG、DPR、HyDE、RAGAS 论文和 OpenAI 文档是一手资料。
- 是否有实验、数据、代码或可复现证据：论文包含实验；官方文档包含 API 和框架流程；本知识库尚未做本地复现实验。
- 是否可能过时：是。OpenAI 文件检索、embedding 模型、向量库参数和框架 API 会变化。
- 适合引用范围：适合支持 RAG 概念、检索增强思想、embedding 与向量搜索、RAG 评估维度、工程流程和失败模式。

## 可引用事实

- RAG 通过检索外部文档增强生成模型，目标是让回答可利用非参数化外部知识。
- Embedding 可以把文本表示为向量，用于相似度搜索、聚类、推荐和分类等任务。
- Dense retrieval 和 sparse retrieval 是两类常见检索方式；实际系统常做 hybrid retrieval。
- RAG 的质量取决于检索质量、上下文质量和生成约束，不能只靠强模型解决。
- RAG 评估应分开看 retrieval、generation、citation 和 end-to-end task success。

## 关键主张表

| 主张 | 原始证据位置 | 可引用程度 | 局限 | 适合写入哪里 |
| --- | --- | --- | --- | --- |
| RAG 是检索增强生成，不是简单长上下文拼接 | RAG 原论文 | 高 | 论文语境是知识密集型 NLP 任务，工程系统会更复杂 | `01-RAG基础概念.md` |
| Embedding 支持语义相似度搜索 | OpenAI Embeddings 文档 | 高 | 模型、维度、价格和限制会变化 | `02-Embedding向量与语义搜索.md` |
| 文档切分和 metadata 会显著影响检索质量 | LangChain RAG 文档与工程实践 | 中高 | 最佳 chunk 策略依赖文档类型和任务 | `03-文档切分与索引.md` |
| RAG 问答需要检索、上下文构造、生成和引用闭环 | RAG 原论文 + OpenAI File search + LangChain RAG | 高 | 各平台实现细节不同 | `04-RAG问答流程.md` |
| RAG 失败常来自上下文不足或错误上下文 | Google Research sufficient context | 中高 | 研究视角，需要结合本地数据验证 | `05-RAG失败模式.md` |
| RAG 是 agent 的知识访问能力，不等同于 agent | Tool calling 与 RAG 的职责差异 | 高 | 实际产品常把二者组合 | `06-RAG与Agent的关系.md` |

## 机制解释

第三章的完整链路可以概括为：

```text
原始资料
  -> 清洗和切分
  -> embedding
  -> 建索引
  -> 用户问题改写或直接检索
  -> 召回候选片段
  -> 重排和过滤
  -> 构造上下文
  -> 模型基于上下文回答
  -> 引用来源与评估
```

其中任何一步做错，最终答案都可能看起来流畅但不可靠。

## 适用范围

- 支持 `knowledge/03-RAG与知识库检索/` 下所有概念卡。
- 支持以后把本知识库变成可检索的个人知识库。
- 支持 agent 工具调用中的 `search_notes`、`read_note`、`retrieve_context` 等工具设计。

## 局限与风险

- 本卡没有运行本地 RAG 实验，所以所有性能判断都不能当作本项目实测结果。
- OpenAI、LangChain 和向量数据库相关 API 会变化，涉及具体参数时要查最新官方文档。
- RAG 原论文中的任务设定与真实业务系统不同，不能机械套用。
- 中文资料、代码资料、表格资料、PDF 资料的切分和检索策略差异很大。

## 与已有知识关联

- `knowledge/01-大模型的使用与训练/02-Prompt工程.md`
- `knowledge/02-Agent基础与工具调用/01-Tool-Calling.md`
- `knowledge/02-Agent基础与工具调用/05-Agent评估.md`
- `tags.md`: `rag`, `embedding`, `vector-search`, `retrieval`, `reranking`, `citation`, `grounding`

## 短摘录

不保留长摘录。使用时引用论文或官方文档，并在知识卡里用自己的话重建机制、边界和实践判断。

## 待验证问题

- 用当前知识库 Markdown 文件做一个最小 RAG 实验时，最佳 chunk size 和 overlap 应该是多少。
- 中文标题、英文缩写、代码块和表格是否应该用不同切分策略。
- OpenAI file search 的默认切分、索引和引用行为是否满足本知识库的可追溯要求。
- 本项目是否更适合先做本地搜索，还是直接接入向量数据库。

## 变更记录

- 2026-06-10：创建第三章统一引用卡。
