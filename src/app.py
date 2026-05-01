import streamlit as st
import duckdb
import pandas as pd

DB_FILE = "warehouse/analytics.duckdb"

st.set_page_config(page_title="API Data Pipeline for Market Intelligence", layout="wide")

st.title("Production Data Platform for Market Intelligence")
st.write(
    "Production-style data platform that ingests exchange-rate data from a public API, "
    "orchestrates workflows, validates data quality, stores analytics in DuckDB, "
    "and provides dashboard insights for decision-making."
)

conn = duckdb.connect(DB_FILE)

exchange_rates_df = conn.execute("""
    SELECT *
    FROM exchange_rates
    ORDER BY ingested_at DESC, currency
""").df()

latest_snapshot_df = conn.execute("""
    SELECT *
    FROM exchange_rates
    WHERE ingested_at = (SELECT MAX(ingested_at) FROM exchange_rates)
    ORDER BY currency
""").df()

summary_df = conn.execute("""
    SELECT
        rate_category,
        COUNT(*) AS currency_count,
        ROUND(AVG(rate), 4) AS avg_rate,
        ROUND(MAX(rate), 4) AS max_rate,
        ROUND(MIN(rate), 4) AS min_rate
    FROM exchange_rates
    WHERE ingested_at = (SELECT MAX(ingested_at) FROM exchange_rates)
    GROUP BY rate_category
    ORDER BY currency_count DESC
""").df()

top_rates_df = conn.execute("""
    SELECT currency, rate, rate_category, api_date, ingested_at
    FROM exchange_rates
    WHERE ingested_at = (SELECT MAX(ingested_at) FROM exchange_rates)
    ORDER BY rate DESC
    LIMIT 10
""").df()

bottom_rates_df = conn.execute("""
    SELECT currency, rate, rate_category, api_date, ingested_at
    FROM exchange_rates
    WHERE ingested_at = (SELECT MAX(ingested_at) FROM exchange_rates)
    ORDER BY rate ASC
    LIMIT 10
""").df()

run_history_df = conn.execute("""
    SELECT
        ingested_at,
        COUNT(*) AS rows_loaded
    FROM exchange_rates
    GROUP BY ingested_at
    ORDER BY ingested_at DESC
""").df()

conn.close()

col1, col2, col3 = st.columns(3)
col1.metric("Latest Snapshot Rows", len(latest_snapshot_df))
col2.metric("Total Historical Rows", len(exchange_rates_df))
col3.metric("Pipeline Runs", len(run_history_df))

st.divider()

st.subheader("Filters")
all_categories = ["All"] + sorted(latest_snapshot_df["rate_category"].dropna().unique().tolist())
selected_category = st.selectbox("Filter by rate category", all_categories)

filtered_df = latest_snapshot_df.copy()
if selected_category != "All":
    filtered_df = filtered_df[filtered_df["rate_category"] == selected_category]

st.subheader("Latest Exchange Rates Snapshot")
st.dataframe(filtered_df, use_container_width=True)

st.divider()

st.subheader("Rate Summary")
st.dataframe(summary_df, use_container_width=True)
if not summary_df.empty:
    st.bar_chart(summary_df.set_index("rate_category")["currency_count"])

st.divider()

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Top 10 Highest Rates")
    st.dataframe(top_rates_df, use_container_width=True)

with right_col:
    st.subheader("Top 10 Lowest Rates")
    st.dataframe(bottom_rates_df, use_container_width=True)

st.divider()

st.subheader("Pipeline Run History")
st.dataframe(run_history_df, use_container_width=True)

st.divider()

st.subheader("Business Value")
st.write("- Demonstrates external API ingestion for production-style pipelines")
st.write("- Converts raw API responses into structured, analytics-ready datasets")
st.write("- Supports historical tracking of pipeline runs for monitoring and reporting")