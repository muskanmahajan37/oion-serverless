import os
from flask import Flask
from src.data_process import generate_df_to_json_response
from src.dataframe import df

app = Flask(__name__)


@app.route("/")
def get_root():
    return {"message": f"Hello from oion-serverless application [env:{os.getenv('ENVIRONMENT')}]"}


@app.route("/health")
def health_check():
    return {"message": "OK"}


@app.route('/employees')
def get_employees():
    employees_json = generate_df_to_json_response(df)
    return employees_json


if __name__ == "__main__":
    app.run(debug=True)
