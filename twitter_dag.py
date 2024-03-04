from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import run_twitter_etl
from airflow.utils.email import send_email
import pendulum


default_args = { 'owner': 'airflow',
                'depends_on_past': False,
                'start_date': pendulum.datetime(2024,2,27),
                'email':['example.domain.com'],
                'email_on_failure': True,
                'email_on_retry': True,
                'retries': 1,
                'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args = default_args,
    description='My First Twitter ETL Airflow Code'
    )

run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag)

run_etl
