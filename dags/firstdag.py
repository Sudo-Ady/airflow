from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


dag = DAG('firstdag', description='Simple tutorial DAG',
          schedule_interval='0 12 * * *',catchup=False,start_date=datetime(2020, 1, 1))

def print_hello():
    return 'Hello world!'

hello_operator = PythonOperator(task_id='hello_task',python_callable=print_hello,dag=dag)

hello_operator