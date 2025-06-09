import os
import datetime
import pendulum
import requests
from airflow.sdk import dag, task
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

@task
def get_data():
    create_table = SQLExecuteQueryOperator(
        task_id="create_table",
        conn_id="tutorial_pg_conn",
        sql="""
            CREATE TABLE IF NOT EXISTS flats (
                "Total Meters" NUMERIC,
                "Floors count" INTEGER, 
                "Rooms 1" INTEGER,
                "Rooms 2" INTEGER,
                "Rooms 3" INTEGER,
                "First floor" INTEGER,
                "Last floor" INTEGER,
            );""",
    )
    pass

@dag(
    dag_id="process_data",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2025, 6, 3, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
)
def process_data():
    pass