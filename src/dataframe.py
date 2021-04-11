import pandas as pd
from pandas import DataFrame
from src import config

"""
Reading the csv from the AWS S3.
It always will require to have permissions to perform the action
"""


def read_csv(s3_bucket: str, s3_object_key: str) -> DataFrame:
    if not s3_object_key:
        raise Exception("S3 URL not provided")
    employees_dataframe = pd.read_csv(f"s3://{s3_bucket}/data/{s3_object_key}")
    if not employees_dataframe:
        raise Exception(f"CSV with url {s3_object_key} the provided URL not found")
    return employees_dataframe


df = pd.read_csv(f's3://{config.S3_BUCKET_NAME}/data/{config.EMPLOYEES_CSV_S3_URI}')
