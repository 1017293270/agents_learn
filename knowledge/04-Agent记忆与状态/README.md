# 04 Agent 记忆与状态

本模块用于整理 agent 的上下文、session、state、memory、长期记忆、用户偏好、项目状态、权限、隐私和记忆评估。

本章默认要求：

- 必须区分 `context`、`session`、`state`、`memory`、`RAG`，不能把所有历史信息都叫记忆。
- 记忆相关知识必须说明写入条件、读取条件、更新条件、删除条件和权限边界。
- 涉及用户偏好、个人信息、项目资料、组织数据时，必须讨论隐私、保留周期和可撤回性。
- 不能默认“记得越多越好”。记忆会带来污染、过时、泄露和错误迁移风险。
- 重要设计必须给出 eval 或人工复盘办法。

## 小节目录

| 小节 | 文件 | 状态 | 说明 |
| --- | --- | --- | --- |
| 01 | `01-Memory基础概念.md` | 已补充 | context、session、state、memory、RAG 的边界，记忆治理和失败模式 |

## 推荐阅读顺序

1. 先读 `01-Memory基础概念.md`，建立 agent 记忆的基本边界。
2. 再回看 `knowledge/02-Agent基础与工具调用/02-Agent基础概念.md`，理解 memory 在 agent 组件中的位置。
3. 再读 `knowledge/03-RAG与知识库检索/06-RAG与Agent的关系.md`，区分 memory 与 RAG 的职责。

## 后续建议补充

- `02-Context-Session-State区别.md`
- `03-Memory与RAG的关系.md`
- `04-Memory安全与隐私.md`
- `05-Memory评估.md`
