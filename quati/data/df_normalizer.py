import pandas as pd


def norm_str_num_values(string: str) -> int:
    """Normalize a value that contains characters 'K', 'M', 'B';

    Example
    -------
    ```
    normalize_str_value("1K")
    1000
    normalize_str_value("550.1K")
    550100
    normalize_str_value("10.3M")
    10300000
    ```
    """
    string = string.lower()
    if "k" in string:
        string = int(float(string.replace("k", "")) * 1000)
    elif "m" in string:
        string = int(float(string.replace("m", "")) * 1000000)
    elif "b" in string:
        string = int(float(string.replace("b", "")) * 1000000000)
    return string


def norm_rename_columns(column_name, lowercase: bool = True):
    """
    Clean and rename a column name by removing special characters, replacing spaces with underscores,
    and optionally converting to lowercase or uppercase.

    Args
    ----
        - `column_name` (str): The original column name to be cleaned and renamed.
        - `lowercase` (bool, optional): Whether to convert the result to lowercase (default is True).

    Returns
    -------
        - `str`: The cleaned and renamed column name.

    Example
    -------
    Apply the function to `new_infos` dataframe

    ```
    new_info.columns = new_info.columns.map(normalize_and_rename_columns)
    ```
    """

    # Remove special characters, replace spaces with underscores, and convert to lowercase or uppercase
    cleaned_name = "".join(c if c.isalnum() or c == " " else "_" for c in column_name)
    cleaned_name = "_".join(
        cleaned_name.split()
    )  # Replace multiple spaces with a single underscore
    cleaned_name = cleaned_name.replace("__", "_")

    # Remove underscore as the last character
    cleaned_name = cleaned_name[:-1] if cleaned_name.endswith("_") else cleaned_name

    # Convert to lowercase or uppercase based on the 'lowercase' parameter
    if lowercase:
        return cleaned_name.lower()
    else:
        return cleaned_name.upper()
