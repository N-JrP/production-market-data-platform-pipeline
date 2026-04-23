import requests
import pandas as pd
from datetime import datetime, timezone

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
OUTPUT_FILE = "data/raw/exchange_rates.csv"

def fetch_data():
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()
    return response.json()

def process_data(data):
    rates = data["rates"]
    df = pd.DataFrame(list(rates.items()), columns=["currency", "rate"])
    df["base"] = data["base"]
    df["api_date"] = data["date"]
    df["ingested_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    return df

def save_data(df):
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    data = fetch_data()
    df = process_data(data)
    save_data(df)