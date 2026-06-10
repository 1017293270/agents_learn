---
title: "Embedding 向量与语义搜索"
type: concept
status: draft
confidence: high
depth: deep
source:
  - title: "RAG 与知识库检索参考资料"
    type: reference
    url: "../../90-references/rag-knowledge-retrieval-references.md"
    accessed: "2026-06-10"
  - title: "OpenAI Embeddings"
    type: official-doc
    url: "https://platform.openai.com/docs/guides/embeddings"
    accessed: "2026-06-10"
  - title: "Dense Passage Retrieval for Open-Domain Question Answering"
    type: paper
    url: "https://arxiv.org/abs/2004.04906"
    accessed: "2026-06-10"
created: "2026-06-10"
updated: "2026-06-10"
tags: ["embedding", "vector-search", "semantic-search", "retrieval", "rag", "beginner"]
---

# Embedding 向量与语义搜索

## 一句话结论

Embedding 是把文本变成向量表示的方法，语义搜索则利用向量之间的相似度找到“意思相近”的内容；它解决的是关键词搜索找不到同义表达的问题，但不能自动保证检索结果真实、完整或有权限。

## 概念定位

- 它是什么：把文本、图片或其他对象映射到多维数值空间，让相似对象在空间里更接近。
- 它不是什么：不是把知识“理解透了”，也不是数据库主键、全文搜索或事实校验器。
- 相邻概念：vector search、semantic search、BM25、hybrid search、reranking、ANN、top-k。
- 前置知识：向量、相似度、token、检索、RAG、文档切分。

初学者可以这样理解：

```text
关键词搜索：找字面上出现了哪些词。
语义搜索：找意思上接近哪些内容。
```

例如用户问“怎么让模型按资料回答”，资料里写的是“RAG 能把外部文档作为上下文提供给模型”。关键词不完全一样，但语义相近，embedding 搜索可能找得到。

## 缩写全称速查

| 缩写 | 英文全称 | 中文解释 | 初学者理解 |
| --- | --- | --- | --- |
| NLP | Natural Language Processing | 自然语言处理 | 让计算机处理人类语言 |
| RAG | Retrieval-Augmented Generation | 检索增强生成 | 用检索结果增强模型回答 |
| IR | Information Retrieval | 信息检索 | 从大量资料里找到相关内容 |
| BM25 | Best Matching 25 | 经典稀疏检索排序函数 | 按词频、逆文档频率和文档长度给文本相关性打分 |
| TF-IDF | Term Frequency-Inverse Document Frequency | 词频-逆文档频率 | 衡量一个词对某篇文档是否重要 |
| DPR | Dense Passage Retrieval | 稠密段落检索 | 用 dense embedding 做开放域问答检索 |
| ANN | Approximate Nearest Neighbor | 近似最近邻 | 在大量向量里快速找相似向量的算法思路 |
| HNSW | Hierarchical Navigable Small World | 分层可导航小世界图 | 一种常见 ANN 索引结构，用图来加速近邻搜索 |
| IVF | Inverted File Index | 倒排文件索引 | 向量检索里常见的聚类分桶索引思路 |
| MMR | Maximal Marginal Relevance | 最大边际相关性 | 在相关性和多样性之间折中，避免结果都太重复 |
| API | Application Programming Interface | 应用程序编程接口 | 调用 embedding 模型或向量数据库的接口 |

注意：Embedding 不是缩写。它的直译是“嵌入”，在机器学习里通常指把对象映射成向量表示。

## 核心概念

### 1. 什么是向量

向量可以理解成一串数字：

```text
[0.12, -0.03, 0.88, ...]
```

对人来说这串数字没什么意义，但对模型和检索系统来说，它代表一段文本在语义空间里的位置。

如果两段文本意思接近，它们的向量通常也更接近：

```text
"如何做 RAG 检索"
"怎么从知识库找资料给模型回答"
```

这两句话字面不同，但意思相近，所以 embedding 可能把它们放得比较近。

### 2. 什么是相似度

常见相似度或距离指标：

| 指标 | 英文 | 直觉 |
| --- | --- | --- |
| 余弦相似度 | Cosine similarity | 看两个向量方向是否接近 |
| 点积 | Dot product | 看向量方向和长度的综合关系 |
| 欧氏距离 | Euclidean distance | 看两个点在空间里的直线距离 |

不同 embedding 模型和向量库可能推荐不同度量。不要随便混用，要看模型文档和向量库配置。

### 3. 稀疏检索和稠密检索

| 类型 | 英文 | 代表 | 优点 | 缺点 |
| --- | --- | --- | --- | --- |
| 稀疏检索 | Sparse retrieval | BM25、TF-IDF | 对关键词、专有名词、编号很强 | 不擅长同义表达 |
| 稠密检索 | Dense retrieval | Embedding search、DPR | 擅长语义相似 | 可能错过精确词、容易召回语义相似但事实不相关内容 |
| 混合检索 | Hybrid retrieval | BM25 + embedding | 兼顾关键词和语义 | 系统复杂度更高，需要融合和调参 |

实践里，技术文档、代码、产品名、错误码、法律条文等场景，混合检索通常比只用向量更稳。

## 机制与原理

Embedding 搜索通常分为离线和在线两部分。

### 离线阶段

```text
文档 chunk
  -> embedding model
  -> 向量
  -> 写入 vector index
```

每个 chunk 通常还要一起存 metadata：

- 文件路径。
- 标题。
- 小节名。
- 更新时间。
- 来源 URL。
- 权限范围。

### 在线阶段

```text
用户问题
  -> embedding model
  -> query vector
  -> 在向量索引中找 top-k 相似 chunk
  -> 可选 rerank
  -> 返回给 RAG 生成阶段
```

这里的 top-k 指“取相似度最高的 k 个结果”。例如 top-5 就是取前 5 个候选片段。

### 为什么需要 ANN

如果知识库只有几百条，可以逐个算相似度。可如果有几百万个 chunk，逐个比较会很慢。ANN，全称 Approximate Nearest Neighbor，近似最近邻，就是用索引结构快速找“足够近”的候选。

ANN 的代价是：更快，但可能不是数学上绝对最近的结果。因此检索系统要在速度、召回率、成本之间权衡。

## 适用场景

- 用户表达和文档表达不完全一致，但意思相近。
- 需要跨同义词、改写、口语问题检索资料。
- 文档数量较大，不能靠人工目录找。
- RAG 需要根据问题召回相关段落。
- 推荐、聚类、去重、相似问题匹配等语义任务。

## 不适用场景

- 必须精确匹配编号、代码、订单号、版本号、法规条款号时，关键词或数据库查询更可靠。
- 资料权限复杂但向量索引没有权限过滤。
- 文档很短且数量很小，普通搜索或目录可能够用。
- 需要严格事实判断，embedding 只能找相似，不会判断真假。
- embedding 模型不适合当前语言或领域，例如中文、代码、医学、法律资料表现不佳。

## 前提、边界与反例

- 必要前提：embedding 模型适合目标语言和领域；文本切分合理；向量和 metadata 一起存储。
- 适用边界：embedding 找语义相似，不等于找答案，也不等于证明答案正确。
- 反例或例外：用户问“错误码 E11000”，向量搜索可能找不到精确错误码，BM25 更稳。
- 结论可能失效的条件：模型版本变化、向量维度不一致、旧向量未重建、metadata 丢失、索引参数不合适。

## 对比与替代方案

| 方案 | 适合 | 优点 | 局限 |
| --- | --- | --- | --- |
| 关键词搜索 | 精确词、编号、错误码 | 可解释、稳定 | 同义表达弱 |
| Embedding 搜索 | 语义相似问题 | 能跨表达方式 | 可能召回语义近但事实错的内容 |
| Hybrid search | 技术文档、知识库 | 兼顾精确和语义 | 融合策略更复杂 |
| Reranking | 提高候选排序质量 | 能细看 query 和候选关系 | 增加延迟和成本 |
| 人工目录 | 小型知识库 | 简单、可控 | 难扩展，依赖维护 |

## 示例或最小实验

准备三段资料：

```text
A：RAG 是 Retrieval-Augmented Generation，先检索资料再生成答案。
B：SFT 是 Supervised Fine-Tuning，用示例输入和理想输出训练模型。
C：Tool calling 是模型提出工具调用，应用侧执行真实工具。
```

用户问：

```text
怎么让模型先找资料再回答？
```

关键词里没有直接出现“RAG”，但 embedding 搜索应该更可能召回 A，因为语义上最接近。

再问：

```text
SFT 的全称是什么？
```

这时关键词和向量都可能召回 B。但如果用户问：

```text
错误码 E11000 是什么？
```

就应该优先考虑关键词搜索，因为错误码是精确符号，不是普通语义。

## 失败模式与风险

- 语义近但答案错：检索到“相似主题”，但不是问题答案。
- 专有名词漏召回：产品名、错误码、人名、函数名没有被向量正确捕捉。
- 多义词混淆：同一个词在不同领域含义不同。
- 长 chunk 稀释：一个 chunk 太长，embedding 混合多个主题，检索不准。
- 短 chunk 断裂：一个 chunk 太短，缺少上下文，模型误解。
- 向量陈旧：文档更新后没有重新生成 embedding。
- 维度不一致：换模型后旧向量和新向量不能混用。
- 权限泄露：向量索引召回了用户无权访问的内容。

## 常见误区

- 误区：embedding 表示“模型理解了知识”。
  - 修正：embedding 只是表示相似性，不代表事实验证。
- 误区：向量搜索一定比关键词搜索高级。
  - 修正：错误码、术语、编号、精确法律条文常常需要关键词搜索。
- 误区：top-k 越大越好。
  - 修正：top-k 太大容易塞入噪声，太小又可能漏掉关键资料。
- 误区：向量库就是 RAG。
  - 修正：向量库只负责存储和检索向量，RAG 还包括上下文构造、生成、引用和评估。
- 误区：同一个 embedding 模型适合所有任务。
  - 修正：语言、领域、文本长度和任务类型都会影响效果。

## 实践判断

- 什么时候应该采用：用户问题表达多样、文档较多、需要语义召回。
- 什么时候应该谨慎：精确字段查询、权限复杂、资料高度结构化、专有名词密集。
- 落地时最先验证什么：查询样例能否召回正确 chunk；专有名词和缩写是否能搜到；metadata 是否保留。
- 可观察指标或检查点：Recall@k、Precision@k、MRR、NDCG、无结果率、错误召回率、重排前后提升。

## 来源与证据

- 来源：`90-references/rag-knowledge-retrieval-references.md`；OpenAI Embeddings 文档；DPR 论文。
- 证据摘要：OpenAI 文档支持 embedding 可用于搜索、聚类、推荐等语义任务；DPR 论文支持稠密段落检索在开放域问答中的作用；BM25、hybrid、ANN 等工程判断来自信息检索实践。
- 可信度判断：embedding 与语义搜索的基础机制可信度高；具体模型、维度、相似度指标和向量库参数必须按当前平台验证。

### 关键主张表

| 主张 | 证据 | 来源 | 可信度 | 局限 |
| --- | --- | --- | --- | --- |
| Embedding 可支持语义搜索 | OpenAI Embeddings 文档列出搜索等用途 | OpenAI docs | high | 具体模型效果需实测 |
| Dense retrieval 可用于问答段落检索 | DPR 论文研究开放域问答检索 | DPR paper | high | 英文开放域问答结果不能直接代表中文知识库 |
| 关键词检索在精确符号场景仍重要 | BM25/TF-IDF 的词项匹配特性 | IR 工程实践 | high | 需要和语义检索结合评估 |
| ANN 是速度和召回的权衡 | 近似近邻通过索引加速搜索 | 向量检索实践 | medium | 具体算法依赖向量库 |

## 待验证问题

- 本知识库中文 Markdown 用哪种 embedding 模型效果最好。
- 英文缩写和中文解释是否应该分别建立关键词索引和向量索引。
- top-k 默认值应从 3、5、8 还是 10 开始实验。
- 是否需要在 viewer 里先做纯前端关键词搜索，再接 embedding 检索。

## 变更记录

- 2026-06-10：创建深度初稿，补充 embedding、语义搜索、稀疏/稠密/混合检索、ANN、top-k 和失败模式。
