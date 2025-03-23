from airflow import DAG
from datetime import datetime
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator

dag= DAG("FetchAPIData",
        description='This api fetches data from github endpoint',
        schedule_interval='@hourly',
        start_date=datetime(2025,1,1),
        catchup=False)

checkapi = HttpSensor(
            task_id = 'Check_API_Status',
            dag=dag,
            endpoint='/Sudo-Ady/airflow/refs/heads/main/results.csv',
            http_conn_id='githubcon',
            poke_interval=5 )

def call_fun(res):
    with open('/opt/airflow/dags/results2.csv',mode='w') as f:
        f.write(res)
    return True

Getdatafromapi = SimpleHttpOperator(
            task_id="Fetch_Data",
            dag=dag,
            http_conn_id='githubcon',
            endpoint='/Sudo-Ady/airflow/refs/heads/main/results.csv',
            method='GET',
            response_filter=lambda response: call_fun(response.text),
            log_response=True )

checkapi >> Getdatafromapi