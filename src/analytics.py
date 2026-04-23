import duckdb
import pandas as pd

DB_FILE = "warehouse/analytics.duckdb"
OUTPUT_FILE = "data/processed/rate_summary.csv"

def main():
    conn = duckdb.connect(DB_FILE)

    query = """
    SELECT
        rate_category,
        COUNT(*) AS currency_count,
        ROUND(AVG(rate), 4) AS avg_rate,
        ROUND(MAX(rate), 4) AS max_rate,
        ROUND(MIN(rate), 4) AS min_rate
    FROM exchange_rates
    GROUP BY rate_category
    ORDER BY currency_count DESC
    """

    df = conn.execute(query).df()
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Analytics summary saved to {OUTPUT_FILE}")

    conn.close()

if __name__ == "__main__":
    main()