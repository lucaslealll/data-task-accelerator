# Features & Functions

## *Dataframes*
Provides methods to quickly adjust dataframes.

> [!NOTE]
> ```py
> from dta.data.df_normalizer import <FUNCTION>
> ```

- [`norm_str_num_values()`](data.md#norm_str_num_values): Converts string-based number values to their numerical equivalents
- [`norm_rename_columns()`](data.md#norm_rename_columns): Renames DataFrame columns based on a normalization function

## *Google*
Provides methods to interact with Google resources sucha as Sheets and BigQuery, to boost data manipulation.

### *BigQuery*

> [!NOTE]
> ```py
> from dta.google.big_query import <FUNCTION>
> ```

- [`sync_dtypes_with_table()`](google.md#sync_dtypes_with_bigquery_table): Synchronize the data types of a Pandas DataFrame with a BigQuery table's schema
- [`quick_query()`](google.md#quick_query): Executes a BigQuery SQL query and returns the result as a Pandas DataFrame

### *Google Sheets*

> [!NOTE]
> ```py
> from dta.google.sheets import <FUNCTION>
> ```

- [`gsheets_get_worksheet()`](google.md#gsheets_get_worksheet): Import a worksheet object from gsheets
- [`gsheets_get_worksheet_df()`](google.md#gsheets_get_worksheet_df): Import a worksheet object from gsheets as a pandas dataframe
- [`gsheets_dedup()`](google.md#gsheets_dedup): Returns dataframe where the column passed as parameter is considered the core set for duplicate data row remover
- [`gsheets_worksheet_next_available_row()`](google.md#gsheets_worksheet_next_available_row): Return the ID of the next cell into which data can be entered
- [`gsheets_update()`](google.md#gsheets_update): Update a Google Sheets spreadsheet from a reference column

## *Messengers & Alerts*
Provides methods to send alerts and informations via email from just a few lines of code.

> [!NOTE]
> ```py
> from dta.messenger.gmail import <FUNCTION>
> ```

- [`send_alert_email()`](messenger.md#send_alert_email): Send an email (Types: error, tip, note, important or warning) with main info about it

## *Headers & Constants*
Defines constants and functions for managing ETL (Extract, Transform, Load) processes, date and time formatting, logging levels, API scopes, database connections, and various data operations.

> [!NOTE]
> ```py
> from dta.header.manager import <ITEM>
> ```

[`Text Constants for ETL Phases` • `Google Sheets API Scope` • `Date and Time` • `Paths and File Locations` • `Database Connection` • `Data Sources` • `Miscellaneous Constants` • `Logging Levels` • `Email Configuration` • `ETL Process Status` • `Data Formats and Locations` • `ETL Configuration` • `Error Handling` • `Throttling and Rate Limits` • `Security` • `Data Export and Serialization` • `File Encoding` • `Data Validation` • `AWS S3 Paths` • `Encryption` • `Data Export Formats` • `Data Backup` • `Data Sampling`](header.md)

## *Log Messages*
This Python file defines error and success messages, log levels, and ETL process statuses. These constants standardize messaging and facilitate debugging and monitoring of the system.

> [!NOTE]
> ```py
> from dta.logger.manager import <LOG_MESSAGE>
> ```

[`Error`](logger.md#error) • [`Success`](logger.md#success) • [`ETL Process Status`](logger.md#etl-process-status)

## *System Utilities*
Provides several methods to use system functionality from just a few lines of code.

> [!NOTE]
> ```py
> from dta.system.linux_utils import <FUNCTION>
> ```

- [`delete_file()`](system.md#delete_file): Deletes any specified file
- [`rename_file()`](system.md#rename_file): Renames a file
- [`search_file()`](system.md#search_file): Searches for the existence of a file
- [`progress_bar()`](system.md#progress_bar): Waits for the specified number of seconds with an optional progress bar
- [`get_system_info()`](system.md#get_system_info): Retrieves system information using the 'uname -a' command

## *Web Scrapping*
Provides a set of tools for automating browser interactions, allowing you to perform web scraping tasks with minimal code.

### *Selenium*

> [!NOTE]
> ```py
> from dta.scrapping.selenium import <FUNCTION>
> ```

- [`start_browser()`](scrapping.md#start_browser): Initialize a Chrome browser using Selenium
- [`export_cookies()`](scrapping.md#export_cookies): Export cookies from browser
- [`import_cookies()`](scrapping.md#import_cookies): Import cookies to browser
- [`check_element()`](scrapping.md#check_element): Function to check if an element exists on a web page based on the provided XPath
- [`esc_or_click()`](scrapping.md#esc_or_click): Function to either press the ESC key or click on an element on a web page

<hr>

[⇧ Go to Top](#table-of-contents)