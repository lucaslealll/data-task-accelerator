import gspread
import pandas as pd
from time import sleep


def gsheets_get_worksheet(gsheets_credentials, worksheet_name, sheet_name):
    """
    Import a worksheet object from gsheets

    Parameters
    ----------
    `gsheets_credentials` : Credentials to authorize project access on the google platform
    `worksheet_name` : name of the worksheet you want to get information about
    `sheet_name` : sheet page name you want to get data from
    `head_row` : row where data header starts

    By default:----------
        - the function consider row 1 as header_

    Examples
    --------
    Get the Google Sheets worksheet object
    >>> worksheet = gsheets_get_worksheet(GSHEETS_CREDENTIAL, "worksheet name", "data page name", 6)
    """
    worksheet = (
        gspread.authorize(gsheets_credentials)
        .open(worksheet_name)
        .worksheet(sheet_name)
        # .get_all_records(head=head_row)
    )
    return worksheet


def gsheets_get_worksheet_df(
    gsheets_credentials, worksheet_name, sheet_name, head_row=1
):
    """
    Import a worksheet object from gsheets as a pandas dataframe

    Parameters
    ----------
    `gsheets_credentials` : Credentials to authorize project access on the google platform
    `worksheet_name` : name of the worksheet you want to get information about
    `sheet_name` : sheet page name you want to get data from
    `head_row` : row where data header starts

    By default: the function consider row 1 as header

    Examples
    --------
    Get the Google Sheets worksheet object

    ```
    worksheet = get_gsheets_worksheet_df(GSHEETS_CREDENTIAL, "worksheet name", "data page name", 6)
    ```
    """
    worksheet = gsheets_get_worksheet(gsheets_credentials, worksheet_name, sheet_name)
    df = pd.DataFrame(worksheet.get_all_records(head=head_row))
    return df


def gsheets_dedup(
    gsheets_credentials,
    col_subset,
    worksheet_name,
    sheet_name,
    keep_option="first",
    first_cell="A1",
    last_cell="ZZ",
):
    """Returns dataframe where the column passed as parameter is considered the core set for duplicate data row remover.

    Parameters
    ----------
    `gsheets_credentials` : Credentials to authorize project access on the google platform
    `col_subset`: column(s) to consider to check for duplicate data in it
    `worksheet_name` : name of the worksheet you want information about
    `sheet_name` : sheet page name you want to get data from

    By default:
        - `keep_option` : Line 1 as data to be kept
        - `first_cell` : Cell "A1" as the starting point for dataframe cleaning and reordering
        - `last_cell` : The cell "ZZ" as the endpoint for dataframe cleaning and reordering

    Examples
    --------
    Get the Google Sheets worksheet object

    ```
    dedup_df = gsheets_dedup(GSHEETS_CREDENTIAL, "post_title", "facebook_posts", "all_posts", "last", "A5")
    ```
    """
    worksheet = (
        gspread.authorize(gsheets_credentials)
        .open(worksheet_name)
        .worksheet(sheet_name)
    )
    df = gsheets_get_worksheet_df(gsheets_credentials, worksheet_name, sheet_name)
    df = df.astype(str).drop_duplicates(subset=col_subset, keep=keep_option)
    df.batch_clear([f"{first_cell}:{last_cell}"])
    worksheet.update(
        f"{first_cell}",
        df.values.tolist(),
        value_input_option="USER_ENTERED",
    )

    return df


def gsheets_worksheet_next_available_row(worksheet, col):
    """
    Return the ID of the next cell into which data can be entered

    Parameters
    ----------
    `worksheet` : the worksheet "object" so that the function can identify the data
    `col` : column which function should be considered to check cell continuity

    Examples
    --------
    Get, from the facebook posts spreadsheet, in the column where the comments of all the posts are, the next line where the new data can be inserted

    ```
    df = gsheets_worksheet_next_avaible_row(worksheet, "A")
    A237
    ```
    """
    string_list = list(filter(None, worksheet.col_values(2)))
    last_row_plus_one = str(len(string_list) + 1)
    return str(col + last_row_plus_one)


def gsheets_update(worksheet, current_df, pivot_col):
    """
    Update a Google Sheets spreadsheet from a reference column

    Parameters
    ----------
    `worksheet`: the "object" of the worksheet so that the function can identify the data
    `current_df`: the dataframe "object" so the function can transfer to the worksheet
    `pivot_col`: column which the function must be considered to establish the upload

    Examples
    --------
    Upload the face dataframe data, in the facebook statistics worksheet, considering the pivot column "A3"

    ```
    gsheets_worksheet_update(worksheet, facebook_metrics_df, "A3")
    ```
    """
    current_df = current_df.astype(str)

    worksheet.update(
        f"{pivot_col}",
        current_df.values.tolist(),
        value_input_option="USER_ENTERED",
    )


def open_worksheet_with_retries(gc, spreadsheet, worksheet, retries=5, sleep_time=60):
    """
    Opens a worksheet in a Google Sheets spreadsheet by its name, with retry logic 
    to handle potential errors during the operation.

    Args:
        gc (gspread.Client): The authenticated gspread client object.
        spreadsheet (str): The name of the Google Sheets spreadsheet to open.
        worksheet (str): The name of the worksheet to access within the spreadsheet.
        retries (int, optional): The maximum number of retry attempts in case of failure. Defaults to 5.
        sleep_time (int, optional): The time (in seconds) to wait between retry attempts. Defaults to 60.

    Returns:
        gspread.models.Worksheet: The worksheet object if successfully opened.

    Raises:
        Exception: If the function fails to open the worksheet after the specified number of retries.

    Example:
        Get spreadsheet named "Planilha do Lucas Godoi" on worksheet "Aba teste".

        worksheet = open_worksheet_with_retries(gc, "Planilha do Lucas Godoi", "Aba Teste")
    """
    attempts = 0
    while attempts < retries:
        try:
            return gc.open(spreadsheet).worksheet(worksheet)
        except Exception as e:
            attempts += 1
            print(f'Tentativa {attempts} planilha {spreadsheet} worksheet {worksheet} falhou com a exceção: \n{e}')
            if attempts < retries:
                print(f'Aguardando {sleep_time} segundos antes de tentar novamente...')
                sleep(sleep_time)
            else:
                print(f'Except Sheet -> worksheet = gc.open({spreadsheet}).worksheet({worksheet})')
                print(f'Falhou em acessar a planilha depois de {retries} tentativas.')
                raise  # Levanta a exceção novamente se todas as tentativas falharem


def open_worksheet_by_url_with_retries(gc, url, worksheet, retries=5, sleep_time=60):
    """
    Opens a worksheet in a Google Sheets spreadsheet by its URL, with retry logic 
    to handle potential errors during the operation.

    Args:
        gc (gspread.Client): The authenticated gspread client object.
        url (str): The URL of the Google Sheets spreadsheet.
        worksheet (str): The name of the worksheet to open.
        retries (int, optional): The maximum number of retry attempts in case of failure. Defaults to 5.
        sleep_time (int, optional): The time (in seconds) to wait between retry attempts. Defaults to 60.

    Returns:
        gspread.models.Worksheet: The worksheet object if successfully opened.

    Raises:
        Exception: If the function fails to open the worksheet after the specified number of retries.

    Example:
        Opens by the url specified on sheet "Aba teste".

        worksheet = open_worksheet_by_url_with_retries(gc, "https://docs.google.com/spreadsheets/d/XXXXX", "Aba teste")
    """
    attempts = 0
    while attempts < retries:
        try:
            return gc.open_by_url(url).worksheet(worksheet)
        except Exception as e:
            attempts += 1
            print(f'Tentativa {attempts} url {url} worksheet {worksheet} falhou com a exceção: \n{e}')
            if attempts < retries:
                print(f'Aguardando {sleep_time} segundos antes de tentar novamente...')
                sleep(sleep_time)
            else:
                print(f'Except Sheet -> gc.open_by_url({url}).worksheet({worksheet})')
                print(f'Falhou em acessar a planilha depois de {retries} tentativas.')
                raise  # Levanta a exceção novamente se todas as tentativas falharem


def fetch_worksheet_records_with_retries(worksheet, retries=5, sleep_time=60, head=0, include_header=True):
    """
    Fetches records from a Google Sheets worksheet and converts them into a Pandas DataFrame, 
    with retry logic to handle potential errors during the fetch process.

    Args:
        worksheet (gspread.models.Worksheet): The worksheet object to fetch records from.
        retries (int, optional): The maximum number of retry attempts in case of failure. Defaults to 5.
        sleep_time (int, optional): The time (in seconds) to wait between retry attempts. Defaults to 60.
        head (int, optional): Specifies the row to use for column headers. Defaults to 0 (first row).
        include_header (bool, optional): Whether to use the first row as column headers. Defaults to True.

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the fetched records.

    Raises:
        Exception: If the function fails to fetch records after the specified number of retries.

    Example:
        Get data from worksheet as a dataframe, including first row (number 0) as header.

        dataframe = fetch_worksheet_records_with_retries(worksheet, head=0, include_header=True)

    """
    retry_count = 0

    while retry_count < retries:
        try:
            records = worksheet.get_all_values()
            if include_header:
                df = pd.DataFrame(records[1:], columns=records[head])
            else:
                df = pd.DataFrame(records)

            return df
        except Exception as e:
            retry_count += 1
            print(f"Retry {retry_count}")
            if retry_count < retries:
                sleep(sleep_time)
            else:
                raise Exception(f"Failed to fetch records after {retries} attempts. Last error: {str(e)}")

def get_next_available_worksheet_row_with_retries(worksheet, start_cell=1, retries=4, sleep_time = 60):
    """
    Retrieves the next available row number in a Google Sheets worksheet, 
    with retry logic to handle potential failures.

    Args:
        worksheet (gspread.models.Worksheet): The Google Sheets worksheet object.
        start_cell (int, optional): The starting column for checking values. Defaults to 1 (column A).
        retries (int, optional): The maximum number of retry attempts in case of an error. Defaults to 4.
        sleep_time (int, optional): The time (in seconds) to wait between retries. Defaults to 60.

    Returns:
        int: The row number of the next available empty row in the worksheet.

    Raises:
        Exception: If the function fails after the specified number of retries.

    Example:
        Get next available row given a column number.

        next_row = get_next_available_worksheet_row_with_retries(worksheet, start_cell=2)
    """
    
    retry_count = 0

    while retry_count < retries:
        try:
            # Obtemos os valores da coluna 1 (A) e removemos os vazios
            values = worksheet.col_values(start_cell)

            # Filtramos apenas as linhas não vazias
            non_empty_values = list(filter(None, values))

            # Retorna o número da próxima linha disponível
            return len(non_empty_values) + 1  # +1 para a próxima linha
        
        except Exception as e:
            if retry_count < retries:
                sleep(sleep_time)  # Wait before retrying
            else:
                raise Exception(f"Failed to update worksheet after {retries} attempts. Last error: {str(e)}")


def update_worksheet_with_retries(worksheet, start_cell, new_data, retries=5, sleep_time=60):
    """
    Updates a Google Sheets worksheet with the provided data, 
    using retries to handle potential errors during the update process.

    Args:
        worksheet (gspread.models.Worksheet): The worksheet object to update.
        start_cell (str): The starting cell or range for the update (e.g., "A12"). 
                Use `get_next_available_row_with_retry()` to determine available rows based on specific columns.
        new_data (pandas.DataFrame): The data to be inserted, converted to a list of lists.
        retries (int, optional): The maximum number of retry attempts in case of failure. Defaults to 5.
        sleep_time (int, optional): The time (in seconds) to wait between retry attempts. Defaults to 60.

    Returns:
        None

    Raises:
        Exception: If the function fails to update the worksheet after the specified number of retries.

    Example:
        Update worksheet with dataframe data. For the parameter start_cell is highly 
        recommended the use of the function get_next_available_worksheet_row_with_retries().

        next_row = get_next_available_worksheet_row_with_retries(worksheet, start_cell=2)
            - supose next_row is 5
            
        start_cell = "B" + str(next_row)
            - then start_cell will be "B5"

        update_worksheet_with_retries(worksheet, start_cell="B5", dataframe.astype(str))

    """
    retry_count = 0

    while retry_count < retries:
        try:
            # Update worksheet
            worksheet.update("{}".format(start_cell), new_data.values.tolist(), value_input_option='RAW')
            print("Worksheet updated successfully!")
            return
        except Exception as e:
            retry_count += 1
            print(f"Attempt {retry_count} to update failed: {e}")
            if retry_count < retries:
                sleep(sleep_time)  # Wait before retrying
            else:
                raise Exception(f"Failed to update worksheet after {retries} attempts. Last error: {str(e)}")
