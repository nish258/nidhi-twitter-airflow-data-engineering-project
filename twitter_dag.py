from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from twitter_etl import run_twitter_etl
from airflow.utils.email import send_email



default_args = {'owner': 'airflow',
                'depends_on_past': False,
                'start_date': datetime(2024,3,5),
                'email':['nish258@gmail.com'],
                'email_on_failure': True,
                'email_on_retry': True,
                'retries': 1,
                'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'twitter_dag',
    default_args = default_args,
    schedule_interval = timedelta(minutes=10), # Created a batch schedule so this runs every 10 mins
    description='My First Twitter ETL Airflow Code'
    )

run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=run_twitter_etl,
    dag=dag)

run_etl
