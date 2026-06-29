# 实战区

这个目录专门放可运行、可复盘的学习实验。它和 `knowledge/` 的关系是：

- `knowledge/`：沉淀概念、机制、边界和证据。
- `practice/`：动手跑实验、记录现象、踩坑复盘。

实战区的默认规则：

1. 每个实验单独一个编号文件夹。
2. 代码、数据、结果、复盘分开放。
3. 生成的数据和结果默认不提交到 Git，只提交脚本和记录模板。
4. 每个实验结束后，把真正学到的东西再整理回 `knowledge/`。

## 当前实验

| 编号 | 目录 | 目标 |
| --- | --- | --- |
| 01 | `01-factor-modeling-lab/` | 用模拟因子数据跑通 Python + pandas + scikit-learn 的最小建模闭环 |

## 推荐使用方式

先进入第一个实验：

```powershell
cd D:\agents学习\practice\01-factor-modeling-lab
```

安装依赖：

```powershell
python -m pip install -r requirements.txt
```

生成模拟数据：

```powershell
python .\src\01_generate_synthetic_factors.py
```

训练基线模型：

```powershell
python .\src\02_train_baseline_models.py
```

跑完后，把观察写到：

```text
practice/01-factor-modeling-lab/experiment-log.md
```
