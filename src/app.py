import streamlit as st
import duckdb
import pandas as pd
from pathlib import Path

DB_FILE = Path("warehouse/analytics.duckdb")

st.set_page_config(
    page_title="Production Data Platform for Market Intelligence",
    page_icon="🏗️",
    layout="wide",
)

st.title("🏗️ Production Data Platform for Market Intelligence")

st.write(
    "Production-style data platform that ingests exchange-rate data from a public API, "
    "runs automated pipeline steps, validates data quality, stores analytics-ready data in DuckDB, "
    "and provides dashboard insights for decision-making."
)

st.info(
    "Platform capabilities: API ingestion • workflow orchestration with Airflow • "
    "containerized execution with Docker • CI/CD with GitHub Actions • "
    "data validation • historical monitoring"
)

if not DB_FILE.exists():
    st.error(
        "DuckDB warehouse not found. Please run the pipeline first using "
        "`python src/run_pipeline.py` or `docker compose up --build pipeline`."
    )
    st.stop()

conn = duckdb.connect(str(DB_FILE))

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

st.subheader("Pipeline System Overview")

overview_col1, overview_col2, overview_col3 = st.columns(3)

with overview_col1:
    st.markdown("**Orchestration**")
    st.write("Airflow DAG controls ingestion, transformation, validation, and analytics steps.")

with overview_col2:
    st.markdown("**Containerization**")
    st.write("Docker Compose runs the pipeline and dashboard in reproducible environments.")

with overview_col3:
    st.markdown("**Automation**")
    st.write("GitHub Actions validates the pipeline during CI/CD execution.")

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
st.markdown(
    """
- Demonstrates production-style data engineering with orchestration, containerization, and CI/CD
- Converts raw API responses into structured, analytics-ready datasets
- Tracks historical pipeline executions for monitoring and operational visibility
- Shows cloud-ready system design using S3-style storage and Terraform infrastructure definition
- Provides a reproducible dashboard layer for business-facing analytics
"""
)