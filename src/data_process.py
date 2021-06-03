from flask import Response
from pandas import DataFrame



def generate_df_to_json_response(df: DataFrame):
    """Get the dataframe as a param then convert the dataframe to valid json response for Flask"""

    df_to_json = df.to_json(orient="records")
    if df_to_json:
        return Response(df_to_json, mimetype='application/json')
    return None