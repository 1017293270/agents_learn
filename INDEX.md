# 知识库索引

这是 agents 学习知识库的主题入口。新增知识点后，优先更新本索引、`tags.md` 和 `viewer/manifest.json`。

## 模块索引

| 模块 | 目录 | 主题范围 | 当前状态 |
| --- | --- | --- | --- |
| 01 | `knowledge/01-大模型的使用与训练/` | 大模型基础、Prompt、推理部署、SFT、RLHF、模型对比 | 已补充 6 个小节 |
| 02 | `knowledge/02-Agent基础与工具调用/` | Agent 基础、tool calling、工具安全、MCP、评估 | 已补充 5 个小节 |

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

## 资料来源

| 资料 | 文件 | 来源层级 | 备注 |
| --- | --- | --- | --- |
| OpenAI Prompt Engineering References | `90-references/openai-prompt-engineering.md` | Tier 1 | Prompt 工程官方资料引用卡 |
| LLM 使用与训练参考资料 | `90-references/llm-use-training-references.md` | Tier 1 | 大模型基础、推理部署、SFT、RLHF、模型对比统一引用卡 |
| OpenAI Function Calling Guide | `90-references/openai-function-calling.md` | Tier 1 | Tool calling 官方资料引用卡 |
| Agent 基础与工具调用参考资料 | `90-references/agent-basics-tools-references.md` | Tier 1/2 | Agent、guardrails、MCP、eval 与 trace grading 统一引用卡 |
| OpenAI Design Guidelines | `90-references/openai-design-guidelines.md` | Tier 1 | UI 方向与品牌边界 |
