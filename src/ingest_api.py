import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from config.cloud_config import RAW_ZONE


API_URL = "https://api.exchangerate-api.com/v4/latest/EUR"

LOCAL_RAW_DIR = PROJECT_ROOT / "data" / "raw"
LOCAL_RAW_FILE = LOCAL_RAW_DIR / "exchange_rates.csv"

LOCAL_RAW_DIR.mkdir(parents=True, exist_ok=True)


def fetch_exchange_rates() -> dict:
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()
    return response.json()


def save_raw_json_to_data_lake(raw_data: dict) -> None:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    raw_json_file = RAW_ZONE / f"exchange_rates_{timestamp}.json"

    with open(raw_json_file, "w", encoding="utf-8") as file:
        json.dump(raw_data, file, indent=2)

    print(f"Raw API response saved to data lake: {raw_json_file}")


def save_raw_csv_locally(raw_data: dict) -> None:
    base_currency = raw_data.get("base", "EUR")
    api_date = raw_data.get("date")
    ingested_at = datetime.now(timezone.utc).isoformat()

    rates = raw_data.get("rates", {})

    rows = [
        {
            "currency": currency,
            "rate": rate,
            "base": base_currency,
            "base_currency": base_currency,
            "api_date": api_date,
            "ingested_at": ingested_at,
        }
        for currency, rate in rates.items()
    ]

    df = pd.DataFrame(rows)
    df.to_csv(LOCAL_RAW_FILE, index=False)

    print(f"Data saved locally to: {LOCAL_RAW_FILE}")


def main() -> None:
    raw_data = fetch_exchange_rates()
    save_raw_json_to_data_lake(raw_data)
    save_raw_csv_locally(raw_data)


if __name__ == "__main__":
    main()