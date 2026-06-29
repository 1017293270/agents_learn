# 01 最小因子建模实验

这个实验的目标不是预测真实市场，而是先跑通一个完整建模闭环：

```text
生成模拟因子数据
-> 用 pandas 读取和检查
-> 构造训练集/测试集
-> 用 scikit-learn 训练基线模型
-> 看指标和特征重要性
-> 写实验复盘
```

## 为什么先用模拟数据

真实金融数据会立刻引入很多额外问题：

- 复权价格。
- 停牌和缺失值。
- 成分股变化。
- 财报发布日期。
- 交易成本。
- 幸存者偏差。
- 时间序列泄露。

这些都很重要，但不适合作为第一步。第一步先让你熟悉“因子、标签、模型、验证、解释”的完整流程。

## 文件结构

```text
01-factor-modeling-lab/
  README.md
  requirements.txt
  experiment-log.md
  data/
    .gitkeep
  results/
    .gitkeep
  src/
    01_generate_synthetic_factors.py
    02_train_baseline_models.py
```

## 运行步骤

进入实验目录：

```powershell
cd D:\agents学习\practice\01-factor-modeling-lab
```

安装依赖：

```powershell
python -m pip install -r requirements.txt
```

生成数据：

```powershell
python .\src\01_generate_synthetic_factors.py
```

训练模型：

```powershell
python .\src\02_train_baseline_models.py
```

## 你要观察什么

第一次跑时，不要急着调参，先观察：

- `data/synthetic_factors.csv` 有哪些列。
- `future_return` 是怎么由因子和噪声生成的。
- 训练集和测试集是怎么按时间切分的。
- 线性模型、随机森林、GBDT 哪个表现更好。
- 哪些因子被模型认为更重要。
- 模型指标好，是否一定代表真实金融策略好。

## 当前实验不会说明什么

这个实验不能说明任何真实投资结论。原因：

- 数据是模拟的。
- 没有真实交易成本。
- 没有真实行情微结构。
- 没有真实市场非平稳性。
- 没有处理停牌、退市、复权、财报延迟等问题。

它只用于建立建模流程直觉。

## 完成标准

你完成本实验时，应该能说清楚：

1. 什么是因子。
2. 什么是标签。
3. 为什么不能只看训练集。
4. 为什么要按时间切分。
5. RMSE、MAE、R2 大概在衡量什么。
6. 特征重要性为什么不是因果证明。
7. 一个实验应该如何记录和复盘。
