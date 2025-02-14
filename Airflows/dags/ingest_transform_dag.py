from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 2, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "ingest_transform_dag",
    default_args=default_args,
    description="ETL DAG for DigitalXC",
    schedule_interval=timedelta(days=1),
)

def load_data():
    os.system("python /opt/airflow/scripts/load_data.py")

def run_dbt():
    os.system("dbt run --project-dir /opt/dbt/dbt_project")

load_data_task = PythonOperator(
    task_id="load_data",
    python_callable=load_data,
    dag=dag,
)

dbt_transform_task = PythonOperator(
    task_id="dbt_transform",
    python_callable=run_dbt,
    dag=dag,
)

load_data_task >> dbt_transform_task
