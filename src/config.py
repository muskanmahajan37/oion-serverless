import os

EMPLOYEES_CSV_S3_URI = os.getenv("EMPLOYEES_CSV_OBJECT_KEY", "employees_dev.csv")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME", "oion-serverless-dev")
