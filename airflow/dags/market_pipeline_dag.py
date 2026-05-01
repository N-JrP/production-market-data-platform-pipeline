from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
from pathlib import Path


# Add project path so Airflow can find your modules
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(PROJECT_ROOT))


from src.run_pipeline import (
    run_ingestion,
    run_transformation,
    run_warehouse_load,
    run_validation,
    run_analytics,
)


default_args = {
    "owner": "data-engineer",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}


with DAG(
    dag_id="market_data_pipeline",
    default_args=default_args,
    description="Production Market Data Pipeline",
    schedule_interval="@daily",
    catchup=False,
) as dag:

    ingestion = PythonOperator(
        task_id="ingestion",
        python_callable=run_ingestion,
    )

    transformation = PythonOperator(
        task_id="transformation",
        python_callable=run_transformation,
    )

    load = PythonOperator(
        task_id="warehouse_load",
        python_callable=run_warehouse_load,
    )

    validation = PythonOperator(
        task_id="validation",
        python_callable=run_validation,
    )

    analytics = PythonOperator(
        task_id="analytics",
        python_callable=run_analytics,
    )

    # Task dependencies
    ingestion >> transformation >> load >> validation >> analytics