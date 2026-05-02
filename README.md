# 🏗️ Production Data Platform for Market Intelligence

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://market-data-platform-pipeline-lr4zz9sacfdf9hr59h4f6i.streamlit.app/)

End-to-end production-style data platform for ingesting external exchange-rate API data, organizing it in a data lake structure, validating quality, storing analytics-ready data, and visualizing insights through a Streamlit dashboard.

---

## 💼 Business Problem

Organizations rely on external API data for reporting and decision-making.  
Raw API data is often inconsistent, not analytics-ready, and lacks operational visibility.

This project demonstrates how raw external data can be processed through a reliable, reproducible, and cloud-ready data engineering workflow.

---

## 💡 Solution

The project implements a production-style data pipeline with:

- API-based data ingestion
- S3-style local data lake with raw and processed zones
- Data transformation and validation
- DuckDB analytical storage
- Airflow workflow orchestration
- Docker-based reproducible execution
- GitHub Actions CI/CD
- Streamlit analytics dashboard

---

## ⚙️ System Architecture

Exchange Rate API  
        ↓  
Python Ingestion  
        ↓  
Raw Data Lake (`data_lake/raw/`)  
        ↓  
Airflow DAG  
        ↓  
Transformation and Validation  
        ↓  
Processed Data Lake (`data_lake/processed/`)  
        ↓  
DuckDB Analytics Warehouse  
        ↓  
Streamlit Dashboard  
        ↓  
GitHub Actions CI/CD

---

## ☁️ Cloud-Ready Data Lake Design

This project includes an S3-style local data lake to simulate cloud-based storage architecture.

- Raw API responses are stored in `data_lake/raw/`
- Cleaned datasets are stored in `data_lake/processed/`
- Raw and processed zones improve scalability, traceability, and auditability
- The structure follows data lake design patterns and can be extended to cloud object storage such as AWS S3

---

## 🔑 Key Features

- Automated workflow structure using Apache Airflow
- Containerized pipeline and dashboard using Docker Compose
- CI/CD workflow using GitHub Actions
- Data lake layout with raw and processed zones
- Data transformation and validation using Python and DuckDB
- Historical pipeline tracking
- Live Streamlit dashboard for analytics and monitoring

---

## 🛠️ Tech Stack

**Languages:** Python, SQL  
**Data Engineering:** ETL/ELT, Data Modeling, Data Validation  
**Orchestration:** Apache Airflow  
**Storage:** DuckDB, S3-style Data Lake  
**Deployment:** Docker, Docker Compose  
**Automation:** GitHub Actions  
**Visualization:** Streamlit  
**Infrastructure Concept:** Terraform

---

## 🐳 Docker Setup

Run the pipeline:

```bash
docker compose up --build pipeline
```

Run the dashboard:

```bash
docker compose up --build dashboard
```

---

## 🖥️ Docker Execution Preview

The pipeline was successfully executed inside Docker, demonstrating containerized data processing and reproducible execution.

![Docker Pipeline Run](images/docker_pipeline_run.png)

---

## ▶️ Run Locally

Activate environment:

```bash
conda activate doc_rag_project
```

Run pipeline:

```bash
python src/run_pipeline.py
```

Run dashboard:

```bash
streamlit run src/app.py
```

---

## 📌 Project Outcome

Built a production-style market data platform that:

- ingests exchange-rate API data
- stores raw and processed data in a data lake structure
- validates and transforms data into analytics-ready outputs
- stores analytical data in DuckDB
- provides dashboard insights through Streamlit
- supports reproducible execution through Docker and CI/CD

---

## 🧠 Key Learnings

- Designing production-style data pipelines
- Structuring raw and processed data lake zones
- Building cloud-ready data engineering workflows
- Orchestrating pipeline steps with Airflow
- Containerizing data applications with Docker
- Automating validation with CI/CD