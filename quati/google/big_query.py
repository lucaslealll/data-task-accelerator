import pandas as pd
import pandas_gbq
from google.cloud import bigquery
from google.oauth2 import service_account


def sync_dtypes_with_table(
    dataframe, project_id, table, json, debug=False, consider_id_columns: bool = False
):
    """
    Synchronize the data types of a Pandas DataFrame with a BigQuery table's schema.

    This function takes a Pandas DataFrame, a BigQuery table's schema, and updates the data types
    of the DataFrame columns to match the corresponding schema in the BigQuery table.

    Args
    ----
        - `dataframe` (pd.DataFrame): The DataFrame whose data types need to be synchronized.
        - `database_project_id` (str): The Google Cloud Project ID where the BigQuery table is located.
        - `table` (str): The name of the BigQuery table to retrieve the schema from.
        - `credential_file` (str): Path to the service account credential file for authentication.
        - `debug` (bool, optional): Whether to print debug information (default is False).

    Returns
    -------
        - `pd.DataFrame`: The DataFrame with synchronized data types.

    Examples
    --------
        >>> # Synchronize data types with a BigQuery table
        synced_df = sync_dtypes_with_table(
            df, 'your_project_id', 'your_dataset.your_table',
            'path/to/your/credential_file.json', debug=True
        )
    """
    pandas_gbq.context.project = project_id
    instance = bigquery.Client(
        credentials=service_account.Credentials.from_service_account_file(json),
        project=project_id,
    )
    table = instance.get_table(table)

    table_columns_schema = [
        {"name": i.name, "type": i.field_type} for i in table.schema
    ]

    dict = {
        "BOOLEAN": bool,
        "FLOAT": float,
        "INTEGER": int,
        "OBJECT": str,
        "STRING": str,
    }

    date_format = "%Y-%m-%d"
    timestamp_format = "%Y-%m-%d %H:%M:%S:%f"

    for column in table_columns_schema:
        column_name = column["name"]
        column_type = column["type"]

        print(column) if debug else None

        if column_type == "DATE":
            dataframe[column_name] = pd.to_datetime(
                dataframe[column_name], format=date_format, errors="coerce"
            )
        elif column_type == "TIMESTAMP":
            dataframe[column_name] = pd.to_datetime(
                dataframe[column_name], format=timestamp_format, errors="ignore"
            )
        elif consider_id_columns == True and "id" in column_name:
            dataframe[column_name] = dataframe[column_name].astype(str)
        else:
            dataframe[column_name] = dataframe[column_name].astype(dict[column_type])

    return dataframe


# == Retrieve the data from the BigQuery table and convert it to a DataFrame ==
def quick_query(query, project_id, json):
    """
    Executes a BigQuery SQL query and returns the result as a Pandas DataFrame.

    Parameters:
    query (str): The SQL query to execute on BigQuery.

    Returns:
    pandas.DataFrame or None: The result of the query as a DataFrame if successful,
                              None if there was an error.

    Example:
    >>> query = "SELECT * FROM `my_dataset.my_table` LIMIT 10"
    >>> result = bq_query_with_exception(query)
    [10 rows, 5 columns]
    >>> if result is not None:
    >>>     print(result.head())
          column1 column2 column3 column4 column5
    0      value1  value2  value3  value4  value5
    1      value1  value2  value3  value4  value5
    2      value1  value2  value3  value4  value5
    3      value1  value2  value3  value4  value5
    4      value1  value2  value3  value4  value5
    """
    try:
        # Construct the SQL query to retrieve data from the BigQuery table
        df = (
            bigquery.Client(
                credentials=service_account.Credentials.from_service_account_file(json),
                project=project_id,
            )
            .query(query)
            .to_dataframe()
        )
        print(f" [{len(df.index)} rows, {len(df.columns)} columns]")
        return df
    except Exception as e:
        print(f"\n  ❌ Query error: {repr(e)}")
        return None
