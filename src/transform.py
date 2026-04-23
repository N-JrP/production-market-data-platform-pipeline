import pandas as pd

INPUT_FILE = "data/raw/exchange_rates.csv"
OUTPUT_FILE = "data/processed/exchange_rates_cleaned.csv"

def categorize_rate(rate):
    if rate >= 1.5:
        return "high"
    elif rate >= 0.5:
        return "medium"
    return "low"

def main():
    df = pd.read_csv(INPUT_FILE)

    df["rate"] = df["rate"].round(4)
    df["rate_category"] = df["rate"].apply(categorize_rate)
    df["is_strong_vs_usd"] = df["rate"].apply(lambda x: "yes" if x > 1 else "no")

    df = df[
        [
            "currency",
            "rate",
            "rate_category",
            "is_strong_vs_usd",
            "base",
            "api_date",
            "ingested_at",
        ]
    ]

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Cleaned data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()