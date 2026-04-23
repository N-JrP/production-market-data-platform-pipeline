# API Data Pipeline for Market Intelligence

Data pipeline for ingesting external data from a public API, transforming it into structured datasets, and enabling analytics for decision-making.

## Business Problem

Organizations depend on external data sources such as APIs for reporting, monitoring, and analysis. Raw API data is often not directly usable for analytics because it must be cleaned, structured, validated, and stored.

## Solution

This project builds an end-to-end pipeline that ingests exchange-rate data from a public REST API, transforms and validates it, stores it in DuckDB, and exposes analytics through a Streamlit dashboard.

## What it does

- Fetches real-time exchange-rate data from a public API
- Transforms and categorizes rate values
- Loads structured data into DuckDB
- Validates data quality
- Preserves historical pipeline runs
- Generates analytics summaries
- Displays insights in Streamlit

## Business Impact

- Demonstrates external API ingestion used in production-style data workflows
- Converts raw API data into analytics-ready datasets
- Supports reporting and decision-making with structured summaries
- Tracks pipeline history for operational visibility

## Tech Stack

Python • REST API • Pandas • DuckDB • SQL • Streamlit

## Run locally

```bash
conda activate doc_rag_project
python src\run_pipeline.py
streamlit run src\app.py