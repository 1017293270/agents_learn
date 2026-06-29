"""Train simple baseline models on the synthetic factor dataset."""

from pathlib import Path

import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "synthetic_factors.csv"
RESULTS_DIR = ROOT / "results"
METRICS_PATH = RESULTS_DIR / "model_metrics.csv"
IMPORTANCE_PATH = RESULTS_DIR / "feature_importance.csv"

FEATURES = ["momentum", "value", "volatility", "quality", "size"]
TARGET = "future_return"


def rmse(y_true, y_pred) -> float:
    return mean_squared_error(y_true, y_pred) ** 0.5


def evaluate_predictions(name: str, y_true: pd.Series, y_pred) -> dict:
    result = pd.DataFrame({"y_true": y_true.to_numpy(), "y_pred": y_pred})
    result["pred_rank"] = result["y_pred"].rank(pct=True)

    top = result[result["pred_rank"] >= 0.8]["y_true"].mean()
    bottom = result[result["pred_rank"] <= 0.2]["y_true"].mean()

    return {
        "model": name,
        "rmse": rmse(result["y_true"], result["y_pred"]),
        "mae": mean_absolute_error(result["y_true"], result["y_pred"]),
        "r2": r2_score(result["y_true"], result["y_pred"]),
        "spearman_ic": result["y_true"].corr(result["y_pred"], method="spearman"),
        "top_20pct_avg_return": top,
        "bottom_20pct_avg_return": bottom,
        "top_minus_bottom": top - bottom,
    }


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Cannot find {DATA_PATH}. Run src/01_generate_synthetic_factors.py first."
        )

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH, parse_dates=["date"])
    df = df.sort_values(["date", "asset_id"]).reset_index(drop=True)

    split_date = df["date"].quantile(0.8)
    train_df = df[df["date"] <= split_date]
    test_df = df[df["date"] > split_date]

    x_train = train_df[FEATURES]
    y_train = train_df[TARGET]
    x_test = test_df[FEATURES]
    y_test = test_df[TARGET]

    models = {
        "LinearRegression": Pipeline(
            [
                ("scaler", StandardScaler()),
                ("model", LinearRegression()),
            ]
        ),
        "RandomForest": RandomForestRegressor(
            n_estimators=200,
            max_depth=5,
            random_state=42,
        ),
        "GradientBoosting": GradientBoostingRegressor(
            n_estimators=150,
            max_depth=3,
            learning_rate=0.05,
            random_state=42,
        ),
    }

    metrics = []
    importances = []

    for name, model in models.items():
        model.fit(x_train, y_train)
        predictions = model.predict(x_test)
        metrics.append(evaluate_predictions(name, y_test, predictions))

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

    metrics_df = pd.DataFrame(metrics)
    importances_df = pd.DataFrame(importances)

    metrics_df.to_csv(METRICS_PATH, index=False, encoding="utf-8")
    importances_df.to_csv(IMPORTANCE_PATH, index=False, encoding="utf-8")

    print("Train rows:", len(train_df))
    print("Test rows:", len(test_df))
    print()
    print(metrics_df.round(6))
    print()
    print("Saved metrics to:", METRICS_PATH)
    print("Saved feature importance to:", IMPORTANCE_PATH)


if __name__ == "__main__":
    main()
