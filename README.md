# 🏗️ Production Data Platform for Market Intelligence

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://market-data-platform-pipeline-lr4zz9sacfdf9hr59h4f6i.streamlit.app/)

End-to-end production-style data platform that ingests external API data, orchestrates workflows, validates quality, and delivers analytics through an automated pipeline system.

---

## 💼 Business Problem

Organizations rely on external API data (e.g., exchange rates) for reporting and decision-making.  
However, raw API data is:
- unstructured  
- inconsistent  
- not analytics-ready  
- lacks reliability and monitoring  

Modern data teams require automated, reliable, and production-grade pipelines to transform this data into usable insights.

---

## 💡 Solution

This project evolves a simple API pipeline into a production-ready data platform by integrating:

- Workflow orchestration  
- Containerization  
- Automated execution (CI/CD)  
- Data validation and logging  
- Cloud-ready data lake architecture  

---

## ⚙️ System Architecture

Exchange Rate API  
        ↓  
Ingestion (Python)  
        ↓  
Raw Data Lake (S3-style local storage)  
        ↓  
Airflow DAG (Orchestration)  
        ↓  
Transformation (DuckDB processing)  
        ↓  
Processed Data Lake  
        ↓  
Analytics Layer  
        ↓  
Streamlit Dashboard  
        ↓  
CI/CD (GitHub Actions)

---

## ☁️ Cloud-Ready Data Lake Design

This project includes an S3-style local data lake to simulate cloud-based storage architecture.

- Raw API responses are stored in `data_lake/raw/`
- Cleaned datasets are stored in `data_lake/processed/`
- Separation of raw and processed zones improves scalability and auditability
- Designed for easy migration to AWS S3 or other cloud object storage systems

---

## 🔑 Key Features

- Automated data pipeline orchestration using Apache Airflow  
- Containerized execution using Docker and Docker Compose  
- CI/CD pipeline using GitHub Actions  
- Data lake architecture with raw and processed zones  
- Data transformation using DuckDB  
- Data validation and pipeline logging  
- Historical tracking of pipeline runs  
- Interactive analytics dashboard using Streamlit  

---

## 📊 Business Impact

- Demonstrates production-grade data engineering practices  
- Converts raw API data into analytics-ready datasets  
- Enables automated, repeatable workflows  
- Improves data reliability and monitoring  
- Simulates cloud-ready system design used in modern data platforms  

---

## 🛠️ Tech Stack

Core Data Stack:  
Python • SQL • DuckDB • Pandas  

Data Engineering & Platform:  
Apache Airflow • Docker • GitHub Actions  

Processing & Streaming (Conceptual):  
Event-driven ingestion (Kafka-style simulation)  

Storage & Infrastructure:  
S3-style Data Lake • Terraform (infrastructure-as-code concept)  

Visualization:  
Streamlit  

---

## 🐳 Docker Setup

Run the full pipeline:

docker compose up --build pipeline

Run the dashboard:

docker compose up --build dashboard

---

## 🖥️ Docker Execution Preview

The pipeline was successfully executed inside Docker, demonstrating containerized data processing and orchestration.

![Docker Pipeline Run](images/docker_pipeline_run.png)

---

## ▶️ Run Locally (without Docker)

Activate environment:

conda activate doc_rag_project

Run pipeline:

python src/run_pipeline.py

Run dashboard:

streamlit run src/app.py

---

## 📌 Project Outcome

A fully automated data platform that:
- ingests real-time API data  
- stores raw and processed data in a data lake  
- transforms and validates datasets  
- and delivers analytics through a dashboard  

---

## 🧠 Key Learnings

- Building production-style data pipelines  
- Designing data lake architectures (raw vs processed zones)  
- Orchestrating workflows with Airflow  
- Containerizing data systems with Docker  
- Implementing CI/CD for data pipelines  
- Designing cloud-ready data platforms  