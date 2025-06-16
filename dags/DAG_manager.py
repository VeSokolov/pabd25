import datetime
import pendulum
from airflow.sdk import dag, task, DAG

from src.lifecycle import parse_cian, preprocess_data, train_model, test_model

@dag(
    dag_id="process_data",
    schedule="@weekly",
    start_date=pendulum.datetime(2025, 6, 3, tz="UTC"),
    catchup=True,
    dagrun_timeout=datetime.timedelta(minutes=60),
)

def pipeline():
    @task()
    def get_data(*args) -> None:
        parse_cian(args)
        # return result

    @task()
    def process_data(*data) -> None:
        preprocess_data(data)
        # return data

    @task()
    def train(*model) -> None:
        train_model(model)

    @task()
    def test(*model) -> None:
        test_model(model)

    get_data() >> process_data() >> train() >> test()

pipeline()
