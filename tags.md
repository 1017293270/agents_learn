# 标签体系

标签用于让知识卡可检索、可聚合、可复盘。新增标签前先检查本文件，避免同义标签分裂。

## 使用规则

- 使用小写英文 kebab-case。
- 每张知识卡建议 3 到 7 个标签。
- 标签应表达主题、技术域、证据类型或风险维度。
- 不要把状态写成标签，状态使用 frontmatter 的 `status`。
- 不要把深度写成标签，深度使用 frontmatter 的 `depth`。

## 主题标签

| 标签 | 用途 |
| --- | --- |
| `agent` | AI agent 的定义、结构和能力边界 |
| `llm` | 大语言模型基础概念、使用和训练 |
| `model-types` | 模型类型、模型分类、能力边界和模型用途定位 |
| `transformer` | Transformer 架构、attention、现代 LLM 基础 |
| `tokenization` | token、分词、上下文窗口相关知识 |
| `agent-architecture` | agent 架构、控制流、组件关系 |
| `tool-calling` | 函数调用、工具调用、工具结果回传 |
| `mcp` | Model Context Protocol，模型上下文协议 |
| `rag` | 检索增强生成 |
| `retrieval` | 信息检索、召回相关资料 |
| `embedding` | 文本或对象的向量表示 |
| `vector-search` | 向量搜索、相似度检索 |
| `semantic-search` | 语义搜索，按含义而不是只按关键词检索 |
| `grounding` | 让回答基于给定资料或证据 |
| `citation` | 引用来源、出处和证据链 |
| `chunking` | 文档切分，把资料拆成可检索片段 |
| `indexing` | 建立索引，让资料可被快速检索 |
| `metadata` | 关于文档或 chunk 的来源、标题、权限等结构化信息 |
| `reranking` | 对初始检索结果进行重排 |
| `failure-modes` | 系统失败路径、错误类型和诊断框架 |
| `question-answering` | 问答任务，用户提问系统回答 |
| `memory` | agent 记忆、上下文持久化、状态管理 |
| `workflow` | 固定或半固定工作流、流程编排 |
| `planning` | 规划、分解、执行策略 |
| `evaluation` | eval、测试、基准和质量评估 |
| `safety` | 安全、权限、注入、风险控制 |
| `guardrails` | 护栏、输入输出检查、工具前安全边界 |
| `agent-evaluation` | agent 的任务、工具、轨迹和安全评估 |
| `ai-native-ui` | AI 产品交互、状态可见、流式输出 |
| `openai` | OpenAI 官方能力、文档、模型或 API |
| `prompt-engineering` | Prompt 工程、提示词设计和提示词迭代 |
| `zero-shot` | 不给示例、直接描述任务的提示方式 |
| `few-shot` | 在 prompt 中提供少量输入输出示例 |
| `beginner` | 面向初学者的解释型内容 |
| `inference` | 模型推理、生成流程、推理参数 |
| `deployment` | 模型服务部署、运维、成本、延迟 |
| `latency` | 首 token 延迟、总耗时、响应速度 |
| `throughput` | 并发、吞吐、批处理能力 |
| `serving` | 推理服务、模型服务接口、线上运行 |
| `sft` | 监督微调 |
| `fine-tuning` | 微调、训练数据、模型定制 |
| `training-data` | 训练数据、标注、清洗、覆盖范围 |
| `rlhf` | 人类反馈强化学习 |
| `reinforcement-learning` | 强化学习，基于奖励或反馈信号优化行为的机器学习方法 |
| `rft` | 强化微调或基于评分器的强化训练 |
| `alignment` | 模型对齐、人类偏好、安全偏好 |
| `reward-model` | 奖励模型和偏好建模 |
| `human-feedback` | 人类反馈、偏好比较、标注 |
| `model-comparison` | 模型家族、能力、成本和选型对比 |
| `claude` | Anthropic Claude 模型相关内容 |
| `gemini` | Google Gemini 模型相关内容 |
| `mistral` | Mistral 模型相关内容 |

## 工程标签

| 标签 | 用途 |
| --- | --- |
| `api-design` | API 合约、请求响应、错误结构 |
| `remote-tools` | 远程工具、远程 MCP server、外部工具服务 |
| `json-rpc` | JSON-RPC 协议、远程过程调用消息结构 |
| `schema` | JSON Schema、结构化输出、参数约束 |
| `state-machine` | 生命周期、状态机、流程控制 |
| `observability` | 日志、追踪、审计、成本和延迟 |
| `trace` | agent 执行轨迹、工具调用链和过程评分 |
| `permissions` | 权限边界、确认、访问控制 |
| `streaming` | 流式输出、渐进式事件、取消控制 |
| `testing` | 单元测试、集成测试、E2E、实验复现 |

## 证据标签

| 标签 | 用途 |
| --- | --- |
| `official-doc` | 官方文档来源 |
| `paper` | 论文或研究报告 |
| `source-code` | 源码依据 |
| `experiment` | 本地实验或可复现实验 |
| `claim-audit` | 关键主张审查 |
| `source-review` | 资料可信度评估 |

## 风险标签

| 标签 | 用途 |
| --- | --- |
| `prompt-injection` | 提示注入或间接提示注入 |
| `data-leakage` | 数据泄露风险 |
| `tool-abuse` | 工具滥用、越权调用、高风险操作 |
| `hallucination` | 幻觉、错误参数、伪造事实 |
| `stale-info` | 可能过时的信息 |