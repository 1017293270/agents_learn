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
| `neural-network` | 神经网络基础、层、参数、训练机制 |
| `deep-learning` | 深度学习模型和训练方法 |
| `parameters` | 模型参数、权重、偏置、可学习变量 |
| `activation-function` | 激活函数、非线性变换 |
| `feature-engineering` | 特征工程、特征构造和输入处理 |
| `factor` | 因子、影响预测目标的输入因素 |
| `feature-representation` | 特征表示、数值化、embedding、归一化 |
| `normalization` | 特征归一化、标准化、分布稳定 |
| `feature-interaction` | 特征交互、因子组合、特征交叉 |
| `factorization-machine` | Factorization Machine，因子分解机 |
| `deepfm` | DeepFM，结合 FM 和深度网络的特征交互模型 |
| `recommendation` | 推荐系统、CTR/CVR、排序相关模型 |
| `forward-pass` | 前向传播，从输入到输出预测的计算 |
| `loss-function` | 损失函数、训练错误度量 |
| `objective` | 优化目标，loss 与正则项组合 |
| `logits` | softmax 或 sigmoid 前的模型原始分数 |
| `backpropagation` | 反向传播，按链式法则计算梯度 |
| `gradient` | 梯度，loss 对参数的变化率 |
| `autograd` | 自动微分、框架自动计算梯度 |
| `chain-rule` | 链式法则，反向传播的数学基础 |
| `automatic-differentiation` | 自动微分系统 |
| `optimizer` | 优化器、参数更新算法 |
| `gradient-descent` | 梯度下降 |
| `sgd` | Stochastic Gradient Descent，随机梯度下降 |
| `momentum` | 动量优化 |
| `mini-batch` | 小批量训练 |
| `adam` | Adaptive Moment Estimation，自适应矩估计优化器 |
| `adamw` | Adam with Decoupled Weight Decay |
| `rmsprop` | Root Mean Square Propagation 优化器 |
| `adagrad` | Adaptive Gradient Algorithm 优化器 |
| `lion` | Lion 优化器 |
| `learning-rate` | 学习率、参数更新步长 |
| `scheduler` | 学习率调度器 |
| `warmup` | 训练初期学习率预热 |
| `weight-decay` | 权重衰减、正则化 |
| `gradient-clipping` | 梯度裁剪 |
| `training-stability` | 训练稳定性、NaN、发散、震荡 |
| `machine-learning` | 机器学习基础模型、训练、评估和应用 |
| `feature-modeling` | 特征建模，把因子或变量组织成模型输入 |
| `linear-model` | 线性模型、线性回归和逻辑回归 |
| `tree-model` | 决策树、树模型和分裂规则 |
| `ensemble-learning` | 集成学习、bagging、boosting、随机森林和 GBDT |
| `random-forest` | Random Forest，随机森林 |
| `gbdt` | Gradient Boosting Decision Tree，梯度提升决策树 |
| `xgboost` | XGBoost，eXtreme Gradient Boosting |
| `lightgbm` | LightGBM，Light Gradient Boosting Machine |
| `catboost` | CatBoost，Categorical Boosting |
| `classification` | 分类任务，预测离散类别 |
| `regression` | 回归任务，预测连续数值 |
| `ranking` | 排序任务，预测样本相对顺序 |
| `metrics` | 模型评估指标 |
| `cross-validation` | 交叉验证，用多次训练/验证估计泛化能力 |
| `time-series-validation` | 时间序列验证，按时间顺序模拟未来预测 |
| `regularization` | 正则化，约束模型复杂度以降低过拟合 |
| `model-selection` | 模型选择、超参数选择和验证策略 |
| `bias-variance` | 偏差-方差权衡 |
| `model-interpretability` | 模型解释、预测原因和解释边界 |
| `feature-importance` | 特征重要性，模型对特征的依赖程度 |
| `permutation-importance` | 置换重要性，打乱特征后观察指标下降 |
| `shap` | SHAP，SHapley Additive exPlanations |
| `preprocessing` | 数据预处理、缺失值、编码、缩放和转换 |
| `financial-factors` | 金融因子、因子分析和因子建模 |

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
| `training-loop` | 训练循环，取数据、前向、反向、更新和验证 |
| `dataloader` | 数据加载器、batch 生成和并行加载 |
| `batch` | 批量样本，一次训练 step 的数据 |
| `epoch` | 训练集完整遍历一次 |
| `gpu` | GPU 训练、显存、硬件加速 |
| `amp` | Automatic Mixed Precision，自动混合精度 |
| `checkpoint` | 训练检查点、模型和优化器状态保存 |
| `training-diagnostics` | 训练诊断、调参排查 |
| `overfitting` | 过拟合 |
| `underfitting` | 欠拟合 |
| `hyperparameter-tuning` | 超参数调优 |

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
