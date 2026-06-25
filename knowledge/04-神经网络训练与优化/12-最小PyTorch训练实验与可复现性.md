---
title: "最小 PyTorch 训练实验与可复现性"
type: practice
status: draft
confidence: high
depth: deep
source:
  - title: "Zeroing out gradients in PyTorch"
    type: official-doc
    url: "https://docs.pytorch.org/tutorials/recipes/recipes/zeroing_out_gradients.html"
    accessed: "2026-06-25"
  - title: "Reproducibility - PyTorch"
    type: official-doc
    url: "https://docs.pytorch.org/docs/stable/notes/randomness.html"
    accessed: "2026-06-25"
  - title: "Saving and Loading Models - PyTorch"
    type: official-doc
    url: "https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html"
    accessed: "2026-06-25"
  - title: "torch.utils.data - PyTorch"
    type: official-doc
    url: "https://docs.pytorch.org/docs/stable/data.html"
    accessed: "2026-06-25"
created: "2026-06-25"
updated: "2026-06-25"
tags: ["pytorch", "training-loop", "reproducibility", "experiment", "checkpoint", "beginner"]
---

# 最小 PyTorch 训练实验与可复现性

## 一句话结论

学神经网络不能只看概念，至少要能跑通一个最小训练循环，并记录随机种子、数据划分、模型配置、指标和 checkpoint；否则调参结果很难复盘。

## 概念定位

- 它是什么：把第四章的前向、损失、反向、优化器、训练循环、验证和保存串成一个最小可复现实验。
- 它不是什么：不是生产级训练框架，也不是追求最高准确率的模板。
- 相邻概念：training loop、small-batch overfit、seed、checkpoint、experiment log、train/eval mode。
- 前置知识：张量 shape、损失函数、反向传播、优化器。

初学者可以先记住：

```text
先让一个很小的实验正确跑通。
再让小 batch 能过拟合。
最后再谈大数据、大模型和复杂调参。
```

## 缩写全称速查

| 缩写 | 英文全称 | 中文解释 | 初学者理解 |
| --- | --- | --- | --- |
| API | Application Programming Interface | 应用程序编程接口 | 框架提供的调用方式 |
| RNG | Random Number Generator | 随机数生成器 | 影响初始化、shuffle、dropout 等随机过程 |
| OOS | Out-of-Sample | 样本外 | 未参与训练的数据 |
| CKPT | Checkpoint | 检查点 | 保存训练状态，便于恢复 |
| CPU | Central Processing Unit | 中央处理器 | 通用计算硬件 |
| GPU | Graphics Processing Unit | 图形处理器 | 常用于加速张量计算 |

## 核心概念

### 1. 最小训练循环

一个训练 step 至少包含：

```text
optimizer.zero_grad()
prediction = model(x)
loss = loss_fn(prediction, y)
loss.backward()
optimizer.step()
```

这正好对应：

- 清空旧梯度。
- 前向传播。
- 计算损失。
- 反向传播。
- 更新参数。

### 2. 小 batch 过拟合

Small-batch overfit 是训练管线健康检查。

如果模型连 16 或 32 条样本都无法记住，通常先查：

- 标签是否对齐。
- loss 是否用对。
- shape 是否正确。
- 梯度是否存在。
- 学习率是否合理。

### 3. 可复现性

可复现性不是“每次结果一定完全一样”。PyTorch 官方文档明确提醒，不同版本、平台、CPU/GPU 执行之间不能保证完全一致。

更实际的目标是：

```text
在同一环境、同一数据、同一配置下，尽量让结果可重复，并能解释差异来源。
```

### 4. 实验记录

一次实验至少记录：

- 数据版本和划分方式。
- 随机种子。
- 模型结构。
- loss。
- optimizer。
- learning rate 和 scheduler。
- batch size。
- 训练轮数。
- train/validation 指标。
- 代码 commit 或文件版本。

### 5. Checkpoint

如果要恢复训练，checkpoint 不应只保存模型权重。通常还要保存：

- model state。
- optimizer state。
- scheduler state。
- epoch/step。
- random seed state。
- scaler state，如果使用 AMP。
- best metric。

## 机制与原理

最小实验的逻辑：

```text
造一批简单数据
  -> 定义小模型
  -> 训练
  -> 看 loss 是否下降
  -> 看模型能否拟合小样本
  -> 保存和恢复 checkpoint
  -> 记录配置和结果
```

它的价值不是模型强，而是验证训练管线正确。

## 适用场景

- 初学 PyTorch。
- 写新的模型或 loss。
- 训练 loss 不降。
- 修改数据管线。
- 准备做金融因子神经网络实验。
- 需要对比不同优化器或学习率。

## 不适用场景

- 只做模型推理，不训练。
- 已经有成熟训练框架且只做配置层调整。
- 数据合规、权限、业务规则等确定性问题。

但即使使用高级框架，最小实验仍然是定位问题的好方法。

## 前提、边界与反例

必要前提：

- 数据样本和标签可被读取。
- 输入 shape 与模型匹配。
- loss 能得到有限标量。
- 参数能产生梯度。
- optimizer 能更新参数。

反例：

```text
训练 100 个 epoch，loss 不动。
```

不要先换大模型。先检查：

```text
loss.backward() 后参数是否有 grad？
optimizer.step() 后参数是否变化？
标签和输入是否错位？
```

## 对比与替代方案

| 做法 | 适合 | 局限 |
| --- | --- | --- |
| 最小手写 training loop | 学习、调试、验证管线 | 不适合复杂生产训练 |
| 高层 Trainer | 快速训练常规模型 | 细节被隐藏 |
| Notebook 实验 | 探索概念 | 可复现性容易差 |
| 脚本 + 配置文件 | 可复现实验 | 初期稍重 |
| 实验追踪系统 | 多实验管理 | 需要额外工具 |

## 示例或最小实验

下面是一个只用于理解训练流程的最小二分类实验。它不追求真实业务效果，只验证训练链路。

```python
import random
import numpy as np
import torch
from torch import nn

seed = 42
random.seed(seed)
np.random.seed(seed)
torch.manual_seed(seed)

# 1. 构造 toy data：如果 x0 + x1 > 0，则标签为 1。
n = 256
x = torch.randn(n, 2)
y = ((x[:, 0] + x[:, 1]) > 0).float().unsqueeze(1)

# 2. 切分训练和验证。
x_train, y_train = x[:200], y[:200]
x_val, y_val = x[200:], y[200:]

# 3. 定义小模型。
model = nn.Sequential(
    nn.Linear(2, 8),
    nn.ReLU(),
    nn.Linear(8, 1),
)

loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-2)

# 4. 训练。
for epoch in range(100):
    model.train()
    optimizer.zero_grad()
    logits = model(x_train)
    loss = loss_fn(logits, y_train)
    loss.backward()
    optimizer.step()

    if epoch % 20 == 0:
        model.eval()
        with torch.no_grad():
            val_logits = model(x_val)
            val_loss = loss_fn(val_logits, y_val)
        print(epoch, float(loss), float(val_loss))
```

如果这段实验 loss 不降，优先检查代码、shape、loss 和学习率，而不是先换复杂模型。

## 失败模式与风险

- 随机种子没记录：结果复盘困难。
- 数据切分没保存：下一次实验不是同一问题。
- 只看训练集：不知道是否泛化。
- 只保存模型权重：无法恢复训练状态。
- 忘记 `model.eval()`：验证指标受 dropout/batch norm 影响。
- 忘记 `torch.no_grad()`：验证占用额外显存。
- 反复调测试集：测试集被污染。
- Notebook 手动改来改去：无法知道哪个配置产生了结果。

## 常见误区

- 误区：设置 seed 后就一定完全复现。
  - 修正：PyTorch 官方文档提醒，不同版本、平台和设备之间不能保证完全一致。
- 误区：训练脚本能跑就说明实验可靠。
  - 修正：还要记录数据、配置、指标和代码版本。
- 误区：checkpoint 只需要 model weights。
  - 修正：恢复训练通常还需要 optimizer、scheduler、step 和随机状态。
- 误区：小实验没意义。
  - 修正：小实验能最快暴露训练管线错误。

## 实践判断

每次新任务先跑四个检查：

1. 一个 batch 能否成功前向。
2. loss 是否是有限标量。
3. backward 后参数是否有梯度。
4. 小 batch 能否过拟合。

如果这四个不通过，不要进入正式调参。

金融因子实验还要额外记录：

- 标签定义和预测周期。
- 特征可得时间。
- 时间切分方式。
- 是否有未来信息泄露。
- 指标是否包含交易成本或风险约束。

## 来源与证据

- PyTorch zeroing gradients 教程支持训练循环中 `zero_grad -> forward -> loss -> backward -> step` 的基本流程，并说明梯度默认会累积。
- PyTorch reproducibility 文档说明跨版本、平台和设备无法保证完全复现，但可通过控制随机性和确定性算法减少不确定性。
- PyTorch saving/loading 文档说明模型和优化器都有 `state_dict`，可用于保存和恢复状态。
- PyTorch data 文档支持 DataLoader 作为可迭代数据加载接口。

### 关键主张表

| 主张 | 证据 | 来源 | 可信度 | 局限 |
| --- | --- | --- | --- | --- |
| 梯度会累积，训练循环需要清梯度 | PyTorch zeroing gradients 教程 | high | 梯度累积训练会故意延迟清零 |
| 完全复现不总是可保证 | PyTorch reproducibility 文档 | high | 同一环境内可尽量控制 |
| optimizer 也有状态需要保存 | PyTorch saving/loading 文档 | high | 不同框架 checkpoint 格式不同 |
| 小 batch 过拟合可作为管线检查 | 工程实践 | medium | 强正则或特殊任务下需调整判断 |

## 待验证问题

- 是否在仓库中加入可运行的 `experiments/minimal-pytorch-training.py`。
- 是否需要模板化实验记录文件，例如 `templates/training-debug-log.md`。
- 后续金融因子实验是否要固定统一的实验目录和配置格式。

## 变更记录

- 2026-06-25：新增本节，补齐最小 PyTorch 训练实验、可复现性、实验记录和 checkpoint 规范。
