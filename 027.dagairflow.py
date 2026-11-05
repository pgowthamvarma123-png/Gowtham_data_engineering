from datetime import datetime
from AIRFLOW import DAG
from airflow.operators.bash import bashoperator
from airflow.operators.python import pythonoperator
from google.cloud import bigquery

email = ['gowtham@gamil.com','varma@gmail.com']

default_arguments = {
    'start_date': airflow.utils.date.days_ago(0),
    'depends_on_past' : False,
    'email':email,
    'email_on_failure':True,
    'email_on_retry':True,
    'retries': 3,
    'retry_delay': timedelta(minutes = 10)
}

dag = DAG('temporary task',default_args = default_arguments,description = 'a smaple dag',
          sle_interval = timedelta(days=1))

task1 = bashoperator(task_id = "11223",bash_command = "gsutil mb gs://bucket",DAG = dag)
task2 = bashoperator(task_id = '11222',bash_command = 'gdhddhhdvd',DAG = dag)
task3 = pythonoperator(task_id = '123123',python_callable = cre8dataset(),DAG = dag)

def cre8dataset():
    client = bigquery.clint()
    dataset_name = bigquery.Dataset("gowtham1996.datasetname")
    dataset = client.create_dataset(dataset_name)
