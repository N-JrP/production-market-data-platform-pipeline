import duckdb
import pandas as pd
import os

DB_FILE = "warehouse/analytics.duckdb"
INPUT_FILE = "data/processed/exchange_rates_cleaned.csv"

def main():
    os.makedirs("warehouse", exist_ok=True)

    conn = duckdb.connect(DB_FILE)
    df = pd.read_csv(INPUT_FILE)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rates (
            currency VARCHAR,
            rate DOUBLE,
            rate_category VARCHAR,
            is_strong_vs_usd VARCHAR,
            base VARCHAR,
            api_date VARCHAR,
            ingested_at VARCHAR
        )
    """)

    conn.register("incoming_df", df)
    conn.execute("""
        INSERT INTO exchange_rates
        SELECT * FROM incoming_df
    """)
    conn.unregister("incoming_df")

    total_rows = conn.execute("SELECT COUNT(*) FROM exchange_rates").fetchone()[0]
    print(f"Data loaded into DuckDB table: exchange_rates | Total rows: {total_rows}")

    conn.close()

if __name__ == "__main__":
    main()