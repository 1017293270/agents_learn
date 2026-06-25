---
title: "机器学习基础模型与特征建模参考资料"
type: reference
status: verified
confidence: high
depth: deep
source:
  - title: "scikit-learn User Guide"
    type: official-doc
    url: "https://scikit-learn.org/stable/user_guide.html"
    accessed: "2026-06-25"
  - title: "scikit-learn Linear Models"
    type: official-doc
    url: "https://scikit-learn.org/stable/modules/linear_model.html"
    accessed: "2026-06-25"
  - title: "scikit-learn Decision Trees"
    type: official-doc
    url: "https://scikit-learn.org/stable/modules/tree.html"
    accessed: "2026-06-25"
  - title: "scikit-learn Ensemble Methods"
    type: official-doc
    url: "https://scikit-learn.org/stable/modules/ensemble.html"
    accessed: "2026-06-25"
  - title: "scikit-learn Model Evaluation"
    type: official-doc
    url: "https://scikit-learn.org/stable/modules/model_evaluation.html"
    accessed: "2026-06-25"
  - title: "scikit-learn Cross-validation"
    type: official-doc
    url: "https://scikit-learn.org/stable/modules/cross_validation.html"
    accessed: "2026-06-25"
  - title: "scikit-learn Preprocessing"
    type: official-doc
    url: "https://scikit-learn.org/stable/modules/preprocessing.html"
    accessed: "2026-06-25"
  - title: "XGBoost Documentation"
    type: official-doc
    url: "https://xgboost.readthedocs.io/en/stable/"
    accessed: "2026-06-25"
  - title: "LightGBM Documentation"
    type: official-doc
    url: "https://lightgbm.readthedocs.io/en/stable/"
    accessed: "2026-06-25"
  - title: "CatBoost Documentation"
    type: official-doc
    url: "https://catboost.ai/docs/"
    accessed: "2026-06-25"
  - title: "Random Forests"
    type: paper
    url: "https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf"
    accessed: "2026-06-25"
  - title: "Greedy Function Approximation: A Gradient Boosting Machine"
    type: paper
    url: "https://statweb.stanford.edu/~jhf/ftp/trebst.pdf"
    accessed: "2026-06-25"
created: "2026-06-25"
updated: "2026-06-25"
tags: ["machine-learning", "feature-modeling", "linear-model", "tree-model", "ensemble-learning", "evaluation", "official-doc", "paper", "source-review"]
---

## 一句话结论

第五章的基础模型、特征建模、评估和验证内容，主要由 scikit-learn 官方文档、XGBoost/LightGBM/CatBoost 官方文档，以及随机森林和梯度提升树经典论文支撑。

## 资料定位

这张参考卡不是教程，而是本章的证据入口。它用于说明：哪些定义来自官方文档，哪些机制来自经典论文，哪些判断属于实践推论或金融场景下的谨慎迁移。

## 资料分层

| 层级 | 资料 | 用途 |
| --- | --- | --- |
| Tier 1 | scikit-learn 官方文档 | 基础模型、预处理、指标、交叉验证、模型评估 |
| Tier 1 | XGBoost、LightGBM、CatBoost 官方文档 | 工业级梯度提升树框架的能力、参数和使用边界 |
| Tier 1 | Breiman Random Forests 论文 | 随机森林的原始方法依据 |
| Tier 1 | Friedman Gradient Boosting 论文 | 梯度提升机的核心方法依据 |

## 可支持的核心主张

| 主张 | 证据 | 可信度 | 限制 |
| --- | --- | --- | --- |
| 机器学习建模应包含训练、验证、测试和评估指标，而不是只看训练集表现。 | scikit-learn model evaluation 与 cross-validation 文档 | high | 文档给出通用方法，具体业务仍需自定义指标 |
| 线性模型是重要基线，正则化可约束模型复杂度。 | scikit-learn linear model 文档 | high | 金融等非平稳场景中，线性关系可能随时间变化 |
| 决策树容易过拟合，集成方法可降低单棵树的不稳定性。 | scikit-learn tree 与 ensemble 文档，Breiman 论文 | high | 集成方法并不自动解决数据泄露或分布漂移 |
| GBDT 通过逐步拟合损失函数下降方向来提升模型。 | Friedman 论文与 scikit-learn ensemble 文档 | high | 不同框架的实现细节、默认参数和类别特征处理不同 |
| 特征工程和预处理必须放在验证流程内部，避免用验证/测试信息污染训练过程。 | scikit-learn preprocessing、pipeline、cross-validation 文档 | high | 真实项目还需要结合时间、主体、权限和数据生成过程检查 |

## 本章使用方式

- 用于第五章所有知识卡片的 `来源与证据`。
- 对官方定义、模型机制和评估方法，优先引用这张资料卡。
- 对金融因子实践判断，只作为方法迁移的参考，不标记为投资结论。

## 待验证问题

- 在后续真实金融因子数据中，哪些验证方法最适合当前数据频率和交易约束？
- 未来如果使用具体库版本，是否需要建立一张按版本记录参数和默认行为的资料卡？
- 是否需要补充金融机器学习专门资料，例如时间序列交叉验证、purging、embargo、回测偏差等主题？

## 变更记录

- 2026-06-25：新增第五章统一参考资料卡。

