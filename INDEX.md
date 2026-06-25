# 知识库索引

这是 agents 学习知识库的主题入口。新增知识点后，优先更新本索引、`tags.md` 和 `viewer/manifest.json`。

## 模块索引

| 模块 | 目录 | 主题范围 | 当前状态 |
| --- | --- | --- | --- |
| 01 | `knowledge/01-大模型的使用与训练/` | 大模型基础、Prompt、推理部署、SFT、RLHF、模型对比 | 已补充 6 个小节 |
| 02 | `knowledge/02-Agent基础与工具调用/` | Agent 基础、tool calling、工具安全、MCP、评估 | 已补充 5 个小节 |
| 03 | `knowledge/03-RAG与知识库检索/` | RAG、embedding、语义搜索、文档切分、索引、失败模式 | 已补充 6 个小节 |
| 04 | `knowledge/04-神经网络训练与优化/` | 神经网络基础、因子组合、损失、梯度、优化器、训练执行 | 已补充 10 个小节 |
| 05 | `knowledge/05-机器学习基础模型与特征建模/` | 机器学习流程、线性/树/集成模型、指标、验证、解释 | 已补充 10 个小节 |

## 01 大模型的使用与训练

| 小节 | 文件 | 状态 | 深度 | 备注 |
| --- | --- | --- | --- | --- |
| 01 | `knowledge/01-大模型的使用与训练/01-大模型基础概念.md` | draft | deep | 大模型定义、分类、Transformer、训练链路和学习路线 |
| 02 | `knowledge/01-大模型的使用与训练/02-Prompt工程.md` | draft | deep | 面向初学者解释 prompt 的组成、写法、技巧、边界和练习 |
| 03 | `knowledge/01-大模型的使用与训练/03-模型推理与部署.md` | draft | deep | 推理流程、部署方式、参数、优化和失败模式 |
| 04 | `knowledge/01-大模型的使用与训练/04-SFT监督微调.md` | draft | deep | SFT 的定义、适用场景、数据、流程和风险 |
| 05 | `knowledge/01-大模型的使用与训练/05-RLHF人类反馈强化学习.md` | draft | deep | RLHF 英文拆解、强化学习基础、流程、奖励模型、RFT 关系和风险 |
| 06 | `knowledge/01-大模型的使用与训练/06-常用大模型对比.md` | draft | deep | 常见模型家族、选型维度、适用场景和评估模板 |

## 02 Agent 基础与工具调用

| 小节 | 文件 | 状态 | 深度 | 备注 |
| --- | --- | --- | --- | --- |
| 01 | `knowledge/02-Agent基础与工具调用/01-Tool-Calling.md` | draft | deep | 模型请求工具、应用执行工具、结果回传模型的代理能力扩展机制 |
| 02 | `knowledge/02-Agent基础与工具调用/02-Agent基础概念.md` | draft | deep | Agent 定义、组件、workflow 区别、缩写全称、机制和边界 |
| 03 | `knowledge/02-Agent基础与工具调用/03-工具安全与权限.md` | draft | deep | 工具权限、guardrails、风险分级、敏感数据和高风险动作控制 |
| 04 | `knowledge/02-Agent基础与工具调用/04-MCP与远程工具.md` | draft | deep | MCP 全称、host/client/server、远程工具、协议边界和风险 |
| 05 | `knowledge/02-Agent基础与工具调用/05-Agent评估.md` | draft | deep | Eval、trace、grader、任务成功率、工具准确率和质量闭环 |

## 03 RAG 与知识库检索

| 小节 | 文件 | 状态 | 深度 | 备注 |
| --- | --- | --- | --- | --- |
| 01 | `knowledge/03-RAG与知识库检索/01-RAG基础概念.md` | draft | deep | RAG 全称、机制、适用边界、示例、失败模式和证据 |
| 02 | `knowledge/03-RAG与知识库检索/02-Embedding向量与语义搜索.md` | draft | deep | Embedding、向量、语义搜索、BM25、ANN、top-k 和混合检索 |
| 03 | `knowledge/03-RAG与知识库检索/03-文档切分与索引.md` | draft | deep | Chunk、metadata、index、overlap、reranking 和索引维护 |
| 04 | `knowledge/03-RAG与知识库检索/04-RAG问答流程.md` | draft | deep | 问题理解、检索、重排、上下文组装、生成、引用和拒答 |
| 05 | `knowledge/03-RAG与知识库检索/05-RAG失败模式.md` | draft | deep | 检索失败、上下文不足、忠实度失败、引用幻觉和权限风险 |
| 06 | `knowledge/03-RAG与知识库检索/06-RAG与Agent的关系.md` | draft | deep | RAG、tool calling、memory、workflow、agent 的边界和组合方式 |

## 04 神经网络训练与优化

| 小节 | 文件 | 状态 | 深度 | 备注 |
| --- | --- | --- | --- | --- |
| 01 | `knowledge/04-神经网络训练与优化/01-神经网络基础概念.md` | draft | deep | 神经元、层、参数、权重、偏置、激活函数和模型容量 |
| 02 | `knowledge/04-神经网络训练与优化/02-因子与特征表示.md` | draft | deep | 因子、特征、连续/离散特征、embedding、归一化和数据泄露 |
| 03 | `knowledge/04-神经网络训练与优化/03-因子组合与特征交互.md` | draft | deep | 线性组合、特征交叉、FM、DeepFM、attention 和交互建模 |
| 04 | `knowledge/04-神经网络训练与优化/04-前向传播与损失函数.md` | draft | deep | forward pass、logits、activation、loss、objective 和常见损失 |
| 05 | `knowledge/04-神经网络训练与优化/05-反向传播与梯度.md` | draft | deep | backpropagation、chain rule、gradient、autograd 和梯度问题 |
| 06 | `knowledge/04-神经网络训练与优化/06-优化器基础.md` | draft | deep | GD、SGD、mini-batch SGD、momentum 和更新规则 |
| 07 | `knowledge/04-神经网络训练与优化/07-常用优化器对比.md` | draft | deep | Adagrad、RMSProp、Adam、AdamW、Lion 的差异和选择 |
| 08 | `knowledge/04-神经网络训练与优化/08-学习率与训练稳定性.md` | draft | deep | learning rate、scheduler、warmup、weight decay、gradient clipping |
| 09 | `knowledge/04-神经网络训练与优化/09-执行算法与训练流程.md` | draft | deep | dataloader、batch、epoch、计算图、GPU、AMP、checkpoint |
| 10 | `knowledge/04-神经网络训练与优化/10-失败模式与调参判断.md` | draft | deep | loss 不降、过拟合、欠拟合、梯度爆炸/消失和调参排查顺序 |

## 05 机器学习基础模型与特征建模

| 小节 | 文件 | 状态 | 深度 | 备注 |
| --- | --- | --- | --- | --- |
| 01 | `knowledge/05-机器学习基础模型与特征建模/01-机器学习建模流程.md` | draft | deep | 从问题定义、数据、特征、模型、验证到上线监控的完整流程 |
| 02 | `knowledge/05-机器学习基础模型与特征建模/02-线性回归与逻辑回归.md` | draft | deep | 线性回归、逻辑回归、系数、正则化、概率和基线建模 |
| 03 | `knowledge/05-机器学习基础模型与特征建模/03-决策树与随机森林.md` | draft | deep | 决策树分裂、过拟合、bagging、随机森林和特征重要性 |
| 04 | `knowledge/05-机器学习基础模型与特征建模/04-GBDT-XGBoost-LightGBM-CatBoost.md` | draft | deep | 梯度提升树、XGBoost、LightGBM、CatBoost 的机制、差异和适用边界 |
| 05 | `knowledge/05-机器学习基础模型与特征建模/05-分类回归排序任务与指标.md` | draft | deep | 分类、回归、排序任务和 Accuracy、AUC、F1、RMSE、NDCG 等指标 |
| 06 | `knowledge/05-机器学习基础模型与特征建模/06-特征工程与数据预处理.md` | draft | deep | 缺失值、异常值、编码、缩放、pipeline、泄露和金融因子预处理 |
| 07 | `knowledge/05-机器学习基础模型与特征建模/07-交叉验证与时间序列验证.md` | draft | deep | KFold、StratifiedKFold、TimeSeriesSplit、walk-forward、purging 和 embargo |
| 08 | `knowledge/05-机器学习基础模型与特征建模/08-过拟合正则化与模型选择.md` | draft | deep | bias-variance、正则化、早停、超参数搜索、nested CV 和模型选择 |
| 09 | `knowledge/05-机器学习基础模型与特征建模/09-模型解释与特征重要性.md` | draft | deep | 系数、树重要性、permutation importance、PDP、ICE、SHAP 和解释风险 |
| 10 | `knowledge/05-机器学习基础模型与特征建模/10-从传统机器学习到神经网络和金融因子.md` | draft | deep | 传统 ML、神经网络、金融因子建模、模型选择和学习路线 |

## 资料来源

| 资料 | 文件 | 来源层级 | 备注 |
| --- | --- | --- | --- |
| OpenAI Prompt Engineering References | `90-references/openai-prompt-engineering.md` | Tier 1 | Prompt 工程官方资料引用卡 |
| LLM 使用与训练参考资料 | `90-references/llm-use-training-references.md` | Tier 1 | 大模型基础、推理部署、SFT、RLHF、模型对比统一引用卡 |
| OpenAI Function Calling Guide | `90-references/openai-function-calling.md` | Tier 1 | Tool calling 官方资料引用卡 |
| Agent 基础与工具调用参考资料 | `90-references/agent-basics-tools-references.md` | Tier 1/2 | Agent、guardrails、MCP、eval 与 trace grading 统一引用卡 |
| RAG 与知识库检索参考资料 | `90-references/rag-knowledge-retrieval-references.md` | Tier 1/2 | RAG、embedding、DPR、HyDE、RAGAS、file search 和 sufficient context |
| 神经网络训练与优化参考资料 | `90-references/neural-network-training-optimization-references.md` | Tier 1 | Deep Learning Book、PyTorch、Adam、AdamW、FM、DeepFM |
| 机器学习基础模型与特征建模参考资料 | `90-references/machine-learning-models-feature-modeling-references.md` | Tier 1/2 | scikit-learn、XGBoost、LightGBM、CatBoost、Random Forest、GBDT |
| OpenAI Design Guidelines | `90-references/openai-design-guidelines.md` | Tier 1 | UI 方向与品牌边界 |
