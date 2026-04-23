import duckdb

DB_FILE = "warehouse/analytics.duckdb"

def main():
    conn = duckdb.connect(DB_FILE)

    total_rows = conn.execute("SELECT COUNT(*) FROM exchange_rates").fetchone()[0]
    null_currency = conn.execute("SELECT COUNT(*) FROM exchange_rates WHERE currency IS NULL").fetchone()[0]
    null_rate = conn.execute("SELECT COUNT(*) FROM exchange_rates WHERE rate IS NULL").fetchone()[0]
    negative_rates = conn.execute("SELECT COUNT(*) FROM exchange_rates WHERE rate < 0").fetchone()[0]
    null_ingestion = conn.execute("SELECT COUNT(*) FROM exchange_rates WHERE ingested_at IS NULL").fetchone()[0]

    print(f"Total rows: {total_rows}")
    print(f"Null currency count: {null_currency}")
    print(f"Null rate count: {null_rate}")
    print(f"Negative rate count: {negative_rates}")
    print(f"Null ingested_at count: {null_ingestion}")

    if total_rows == 0 or null_currency > 0 or null_rate > 0 or negative_rates > 0 or null_ingestion > 0:
        print("Validation failed")
    else:
        print("Validation passed successfully")

    conn.close()

if __name__ == "__main__":
    main()