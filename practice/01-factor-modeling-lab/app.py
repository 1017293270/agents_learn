"""Gradio UI for the first factor modeling practice lab."""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import gradio as gr
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


FEATURES = ["momentum", "value", "volatility", "quality", "size"]
TARGET = "future_return"


@dataclass(frozen=True)
class ExperimentConfig:
    n_days: int
    n_assets: int
    signal_strength: float
    noise: float
    random_forest_depth: int
    gbdt_learning_rate: float
    seed: int


def generate_synthetic_factors(config: ExperimentConfig) -> pd.DataFrame:
    rng = np.random.default_rng(seed=config.seed)
    dates = pd.date_range("2024-01-01", periods=config.n_days, freq="B")
    asset_ids = [f"asset_{i:03d}" for i in range(config.n_assets)]

    rows = []
    for date in dates:
        market_noise = rng.normal(0.0, 0.01 * config.noise)
        for asset_id in asset_ids:
            momentum = rng.normal(0.0, 1.0)
            value = rng.normal(0.0, 1.0)
            volatility = rng.lognormal(mean=-0.2, sigma=0.35)
            quality = rng.normal(0.0, 1.0)
            size = rng.normal(0.0, 1.0)
            idiosyncratic_noise = rng.normal(0.0, 0.05 * config.noise)

            future_return = (
                config.signal_strength * 0.030 * momentum
                + config.signal_strength * 0.020 * value
                - config.signal_strength * 0.025 * volatility
                + config.signal_strength * 0.018 * quality
                + config.signal_strength * 0.006 * size
                + market_noise
                + idiosyncratic_noise
            )

            rows.append(
                {
                    "date": date,
                    "asset_id": asset_id,
                    "momentum": momentum,
                    "value": value,
                    "volatility": volatility,
                    "quality": quality,
                    "size": size,
                    "future_return": future_return,
                    "future_return_positive": int(future_return > 0),
                }
            )

    return pd.DataFrame(rows)


def rmse(y_true: pd.Series, y_pred: np.ndarray) -> float:
    return mean_squared_error(y_true, y_pred) ** 0.5


def evaluate_predictions(name: str, y_true: pd.Series, y_pred: np.ndarray) -> dict:
    result = pd.DataFrame({"y_true": y_true.to_numpy(), "y_pred": y_pred})
    result["pred_rank"] = result["y_pred"].rank(pct=True)
    result["direction_correct"] = (result["y_true"] >= 0) == (result["y_pred"] >= 0)

    top = result[result["pred_rank"] >= 0.8]["y_true"].mean()
    bottom = result[result["pred_rank"] <= 0.2]["y_true"].mean()

    return {
        "model": name,
        "rmse": rmse(result["y_true"], result["y_pred"]),
        "mae": mean_absolute_error(result["y_true"], result["y_pred"]),
        "r2": r2_score(result["y_true"], result["y_pred"]),
        "spearman_ic": result["y_true"].corr(result["y_pred"], method="spearman"),
        "direction_accuracy": result["direction_correct"].mean(),
        "top_20pct_avg_return": top,
        "bottom_20pct_avg_return": bottom,
        "top_minus_bottom": top - bottom,
    }


def build_models(config: ExperimentConfig) -> dict:
    return {
        "LinearRegression": Pipeline(
            [
                ("scaler", StandardScaler()),
                ("model", LinearRegression()),
            ]
        ),
        "RandomForest": RandomForestRegressor(
            n_estimators=200,
            max_depth=config.random_forest_depth,
            random_state=config.seed,
        ),
        "GradientBoosting": GradientBoostingRegressor(
            n_estimators=150,
            max_depth=3,
            learning_rate=config.gbdt_learning_rate,
            random_state=config.seed,
        ),
    }


def train_models(df: pd.DataFrame, config: ExperimentConfig) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    df = df.sort_values(["date", "asset_id"]).reset_index(drop=True)
    split_date = df["date"].quantile(0.8)
    train_df = df[df["date"] <= split_date]
    test_df = df[df["date"] > split_date]

    x_train = train_df[FEATURES]
    y_train = train_df[TARGET]
    x_test = test_df[FEATURES]
    y_test = test_df[TARGET]

    metrics = []
    importances = []
    predictions = pd.DataFrame({"date": test_df["date"], "asset_id": test_df["asset_id"], "actual": y_test})

    for name, model in build_models(config).items():
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        metrics.append(evaluate_predictions(name, y_test, y_pred))
        predictions[name] = y_pred

        if name == "LinearRegression":
            coefficients = model.named_steps["model"].coef_
            importances.extend(
                {"model": name, "feature": feature, "importance": value}
                for feature, value in zip(FEATURES, coefficients)
            )
        elif hasattr(model, "feature_importances_"):
            importances.extend(
                {"model": name, "feature": feature, "importance": value}
                for feature, value in zip(FEATURES, model.feature_importances_)
            )

    return pd.DataFrame(metrics), pd.DataFrame(importances), predictions


def plot_predictions(predictions: pd.DataFrame, model_name: str):
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(predictions[model_name], predictions["actual"], s=16, alpha=0.55)
    ax.axhline(0, color="#d0d0d0", linewidth=1)
    ax.axvline(0, color="#d0d0d0", linewidth=1)
    ax.set_xlabel("Predicted future_return")
    ax.set_ylabel("Actual future_return")
    ax.set_title(f"{model_name}: predicted vs actual")
    ax.grid(True, alpha=0.18)
    fig.tight_layout()
    return fig


def plot_feature_importance(importances: pd.DataFrame, model_name: str):
    model_importance = importances[importances["model"] == model_name].copy()
    model_importance["abs_importance"] = model_importance["importance"].abs()
    model_importance = model_importance.sort_values("abs_importance", ascending=True)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.barh(model_importance["feature"], model_importance["importance"], color="#10a37f")
    ax.axvline(0, color="#d0d0d0", linewidth=1)
    ax.set_xlabel("Importance")
    ax.set_title(f"{model_name}: feature importance")
    ax.grid(True, axis="x", alpha=0.18)
    fig.tight_layout()
    return fig


def build_prediction_detail(predictions: pd.DataFrame, model_name: str) -> pd.DataFrame:
    detail = predictions[["date", "asset_id", "actual", model_name]].copy()
    detail = detail.rename(
        columns={
            "date": "日期",
            "asset_id": "资产",
            "actual": "真实未来收益",
            model_name: "模型预测收益",
        }
    )
    detail["预测误差"] = detail["模型预测收益"] - detail["真实未来收益"]
    detail["绝对误差"] = detail["预测误差"].abs()
    detail["真实方向"] = np.where(detail["真实未来收益"] >= 0, "上涨", "下跌")
    detail["预测方向"] = np.where(detail["模型预测收益"] >= 0, "上涨", "下跌")
    detail["方向判断正确"] = np.where(detail["真实方向"] == detail["预测方向"], "是", "否")
    detail["预测分位"] = detail["模型预测收益"].rank(pct=True)
    detail["日期"] = detail["日期"].dt.strftime("%Y-%m-%d")

    numeric_columns = ["真实未来收益", "模型预测收益", "预测误差", "绝对误差", "预测分位"]
    detail[numeric_columns] = detail[numeric_columns].round(6)
    return detail


def build_error_detail(predictions: pd.DataFrame, model_name: str) -> pd.DataFrame:
    detail = build_prediction_detail(predictions, model_name)
    return detail.sort_values("绝对误差", ascending=False).head(20).reset_index(drop=True)


def build_quantile_summary(predictions: pd.DataFrame, model_name: str) -> pd.DataFrame:
    summary = predictions[["actual", model_name]].copy()
    summary = summary.rename(columns={"actual": "真实未来收益", model_name: "模型预测收益"})
    summary["预测分位"] = summary["模型预测收益"].rank(pct=True, method="first")
    summary["预测组"] = pd.qcut(summary["预测分位"], q=5, labels=False, duplicates="drop") + 1
    summary["方向判断正确"] = (summary["真实未来收益"] >= 0) == (summary["模型预测收益"] >= 0)

    grouped = (
        summary.groupby("预测组", observed=True)
        .agg(
            样本数=("真实未来收益", "size"),
            平均预测收益=("模型预测收益", "mean"),
            平均真实收益=("真实未来收益", "mean"),
            方向准确率=("方向判断正确", "mean"),
        )
        .reset_index()
    )
    grouped["预测组"] = grouped["预测组"].astype(int).map(lambda value: f"第{value}组")
    grouped[["平均预测收益", "平均真实收益", "方向准确率"]] = grouped[
        ["平均预测收益", "平均真实收益", "方向准确率"]
    ].round(6)
    return grouped


def run_experiment(
    n_days: int,
    n_assets: int,
    signal_strength: float,
    noise: float,
    random_forest_depth: int,
    gbdt_learning_rate: float,
    seed: int,
    selected_model: str,
):
    config = ExperimentConfig(
        n_days=int(n_days),
        n_assets=int(n_assets),
        signal_strength=signal_strength,
        noise=noise,
        random_forest_depth=int(random_forest_depth),
        gbdt_learning_rate=gbdt_learning_rate,
        seed=int(seed),
    )
    df = generate_synthetic_factors(config)
    metrics, importances, predictions = train_models(df, config)

    metrics = metrics.round(6)
    importances = importances.round(6)

    return (
        df.head(20),
        metrics,
        build_prediction_detail(predictions, selected_model),
        build_error_detail(predictions, selected_model),
        build_quantile_summary(predictions, selected_model),
        importances,
        plot_predictions(predictions, selected_model),
        plot_feature_importance(importances, selected_model),
    )


def build_demo() -> gr.Blocks:
    css = """
    .gradio-container { max-width: 1280px !important; margin: auto !important; }
    footer { display: none !important; }
    """
    with gr.Blocks(title="Factor Modeling Lab", css=css) as demo:
        gr.Markdown("# 最小因子建模实验")

        with gr.Row():
            with gr.Column(scale=1, min_width=280):
                n_days = gr.Slider(80, 600, value=300, step=20, label="交易日数量")
                n_assets = gr.Slider(5, 100, value=20, step=5, label="资产数量")
                signal_strength = gr.Slider(0.0, 3.0, value=1.0, step=0.1, label="信号强度")
                noise = gr.Slider(0.1, 3.0, value=1.0, step=0.1, label="噪声强度")
                random_forest_depth = gr.Slider(2, 12, value=5, step=1, label="随机森林深度")
                gbdt_learning_rate = gr.Slider(0.01, 0.2, value=0.05, step=0.01, label="GBDT 学习率")
                seed = gr.Slider(1, 999, value=42, step=1, label="随机种子")
                selected_model = gr.Dropdown(
                    ["LinearRegression", "RandomForest", "GradientBoosting"],
                    value="LinearRegression",
                    label="图表模型",
                )
                run_btn = gr.Button("运行实验", variant="primary")

            with gr.Column(scale=2):
                metrics_table = gr.Dataframe(label="模型指标", interactive=False)
                data_preview = gr.Dataframe(label="数据预览", interactive=False)

        with gr.Row():
            prediction_plot = gr.Plot(label="预测 vs 真实")
            importance_plot = gr.Plot(label="特征重要性")

        prediction_detail = gr.Dataframe(label="预测明细（测试集）", interactive=False)
        error_detail = gr.Dataframe(label="误差最大样本（测试集）", interactive=False)
        quantile_summary = gr.Dataframe(label="预测分组收益（测试集）", interactive=False)
        importance_table = gr.Dataframe(label="特征重要性明细", interactive=False)

        inputs = [
            n_days,
            n_assets,
            signal_strength,
            noise,
            random_forest_depth,
            gbdt_learning_rate,
            seed,
            selected_model,
        ]
        outputs = [
            data_preview,
            metrics_table,
            prediction_detail,
            error_detail,
            quantile_summary,
            importance_table,
            prediction_plot,
            importance_plot,
        ]

        # Gradio 4.42 can hit a FastAPI/Pydantic compatibility issue on
        # /queue/join in some local environments, so this small CPU-bound lab
        # uses direct callbacks instead of queueing.
        run_btn.click(fn=run_experiment, inputs=inputs, outputs=outputs, queue=False)
        demo.load(fn=run_experiment, inputs=inputs, outputs=outputs, queue=False)

    return demo


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=7860)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    build_demo().launch(server_name=args.host, server_port=args.port, share=False)
