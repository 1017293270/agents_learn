"""Generate a tiny synthetic factor dataset for the first practice lab.

This file intentionally uses simple Python, numpy, and pandas so beginners can
read it line by line.
"""

from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTPUT_PATH = DATA_DIR / "synthetic_factors.csv"


def main() -> None:
    rng = np.random.default_rng(seed=42)
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    n_days = 300
    n_assets = 20
    n_rows = n_days * n_assets

    dates = pd.date_range("2024-01-01", periods=n_days, freq="B")
    asset_ids = [f"asset_{i:03d}" for i in range(n_assets)]

    rows = []
    for date in dates:
        market_noise = rng.normal(0.0, 0.01)
        for asset_id in asset_ids:
            momentum = rng.normal(0.0, 1.0)
            value = rng.normal(0.0, 1.0)
            volatility = rng.lognormal(mean=-0.2, sigma=0.35)
            quality = rng.normal(0.0, 1.0)
            size = rng.normal(0.0, 1.0)
            idiosyncratic_noise = rng.normal(0.0, 0.05)

            # Synthetic rule: momentum, value, and quality are helpful;
            # volatility is harmful; size is weakly helpful.
            future_return = (
                0.030 * momentum
                + 0.020 * value
                - 0.025 * volatility
                + 0.018 * quality
                + 0.006 * size
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

    df = pd.DataFrame(rows)
    df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")

    print(f"Generated {n_rows} rows")
    print(f"Saved to {OUTPUT_PATH}")
    print()
    print(df.head())


if __name__ == "__main__":
    main()
