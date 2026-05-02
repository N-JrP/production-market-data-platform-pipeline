import sys
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from config.cloud_config import PROCESSED_ZONE


RAW_FILE = PROJECT_ROOT / "data" / "raw" / "exchange_rates.csv"
LOCAL_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
LOCAL_PROCESSED_FILE = LOCAL_PROCESSED_DIR / "exchange_rates_cleaned.csv"
LAKE_PROCESSED_FILE = PROCESSED_ZONE / "exchange_rates_cleaned.csv"

LOCAL_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def categorize_rate(rate: float) -> str:
    if rate < 1:
        return "Low"
    if rate <= 10:
        return "Medium"
    return "High"


def main() -> None:
    df = pd.read_csv(RAW_FILE)

    df["rate"] = pd.to_numeric(df["rate"], errors="coerce")
    df = df.dropna(subset=["currency", "rate"])

    df["rate_category"] = df["rate"].apply(categorize_rate)

    selected_columns = [
        "currency",
        "rate",
        "base",
        "base_currency",
        "api_date",
        "ingested_at",
        "rate_category",
    ]

    df = df[selected_columns]

    df.to_csv(LOCAL_PROCESSED_FILE, index=False)
    df.to_csv(LAKE_PROCESSED_FILE, index=False)

    print(f"Cleaned data saved locally to: {LOCAL_PROCESSED_FILE}")
    print(f"Cleaned data saved to data lake: {LAKE_PROCESSED_FILE}")


if __name__ == "__main__":
    main()