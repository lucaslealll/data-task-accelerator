<div align="center">
	<picture>
	<source media="(prefers-color-scheme: dark)" srcset="assets/dta_white.svg">
		<img alt="DTA Logo" src="assets/dta.svg" width="100%">
	</picture>
	<br> <br>
	<hr>
	<img src="https://img.shields.io/badge/Version-1.0.0-23c4be.svg">
	<img src="https://img.shields.io/badge/Python-3.10-23c4be.svg">
	<img src="https://img.shields.io/badge/Code Style-Black-23c4be.svg">
	<!-- <img src="https://img.shields.io/badge/Airflow-2.7.1-017CEE?logo=apache-airflow&logoColor=white"> -->
	<!-- <img src="https://img.shields.io/badge/PostgreSQL-13-336791?logo=postgresql&logoColor=white"> -->
	<!-- <img src="https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white"> -->
	<br>
	<img src="https://img.shields.io/badge/License-MIT-BE23C4.svg">
	<img src="https://img.shields.io/badge/Status-In Development-C4BE23">
	<img src="https://img.shields.io/badge/By-lucaslealll-23c4be.svg">
	<br> <br>
</div>
<h1><b>dta: A Powerful Python Data Task Accelerator Toolkit</b></h3>


**dta** provides dynamic functions aimed at data engineering, offering
a wide range of collections to accelerate development. It has a comprehensive and
flexible ecosystem of **tools**, **libraries**, and **community resources**,
allowing data engineers to build and deploy applications with ease.

**dta** was originalvly developed to facilitate and streamline the development of ETL scripts. However, the framework is versatile enough to be used in other areas.

- [Install](#install)
- [Features \& Functions](#features--functions)
		- [*Dataframes*](#dataframes)
		- [*Google*](#google)
			- [*BigQuery*](#bigquery)
			- [*Google Sheets*](#google-sheets)
		- [*Messengers \& Alerts*](#messengers--alerts)
		- [*Headers \& Constants*](#headers--constants)
		- [*Log Messages*](#log-messages)
		- [*System Utilities*](#system-utilities)
		- [*Web Scrapping*](#web-scrapping)
			- [*Selenium*](#selenium)
- [Authors](#authors)
- [Contributing](#contributing)
		- [Current Maintainers](#current-maintainers)
		- [References](#references)

<br> <br> 

# Install
> [!IMPORTANT]
> It's essential to **upgrade pip** to the latest version to ensure compatibility with the library.
> ```sh
> # Requires the latest pip
> pip install --upgrade pip
> ```

Install the stable version of **dta** directly from the GitHub repository.

```sh
# Install
pip install git+https://github.com/lucaslealll/data-task-accelerator.git

# Upgrade
pip install --upgrade git+https://github.com/lucaslealll/data-task-accelerator.git
```

> [!TIP]
>
> **If you don't have a TOKEN, use the command below:**
> ```
> pip install git+https://github.com/lucaslealll/data-task-accelerator.git
> ```

<br> <br>

# Features & Functions

### *Dataframes*
Provides methods to quickly adjust dataframes.

> [!NOTE]
> ```py
> from dta.data.df_normalizer import <FUNCTION>
> ```

- [`norm_str_num_values()`](doc/data.md#norm_str_num_values): Converts string-based number values to their numerical equivalents
- [`norm_rename_columns()`](doc/data.md#norm_rename_columns): Renames DataFrame columns based on a normalization function

---

### *Google*
Provides methods to interact with Google resources sucha as Sheets and BigQuery, to boost data manipulation.

#### *BigQuery*

> [!NOTE]
> ```py
> from dta.google.big_query import <FUNCTION>
> ```

- [`sync_dtypes_with_table()`](doc/google.md#sync_dtypes_with_bigquery_table): Synchronize the data types of a Pandas DataFrame with a BigQuery table's schema
- [`quick_query()`](doc/google.md#quick_query): Executes a BigQuery SQL query and returns the result as a Pandas DataFrame

#### *Google Sheets*

> [!NOTE]
> ```py
> from dta.google.sheets import <FUNCTION>
> ```

- [`gsheets_get_worksheet()`](doc/google.md#gsheets_get_worksheet): Import a worksheet object from gsheets
- [`gsheets_get_worksheet_df()`](doc/google.md#gsheets_get_worksheet_df): Import a worksheet object from gsheets as a pandas dataframe
- [`gsheets_dedup()`](doc/google.md#gsheets_dedup): Returns dataframe where the column passed as parameter is considered the core set for duplicate data row remover
- [`gsheets_worksheet_next_available_row()`](doc/google.md#gsheets_worksheet_next_available_row): Return the ID of the next cell into which data can be entered
- [`gsheets_update()`](doc/google.md#gsheets_update): Update a Google Sheets spreadsheet from a reference column

---

### *Messengers & Alerts*
Provides methods to send alerts and informations via email from just a few lines of code.

> [!NOTE]
> ```py
> from dta.messenger.gmail import <FUNCTION>
> ```

- [`send_alert_email()`](doc/messenger.md#send_alert_email): Send an email (Types: error, tip, note, important or warning) with main info about it

---

### *Headers & Constants*
Defines constants and functions for managing ETL (Extract, Transform, Load) processes, date and time formatting, logging levels, API scopes, database connections, and various data operations.

> [!NOTE]
> ```py
> from dta.header.manager import <ITEM>
> ```

[`Text Constants for ETL Phases` • `Google Sheets API Scope` • `Date and Time` • `Paths and File Locations` • `Database Connection` • `Data Sources` • `Miscellaneous Constants` • `Logging Levels` • `Email Configuration` • `ETL Process Status` • `Data Formats and Locations` • `ETL Configuration` • `Error Handling` • `Throttling and Rate Limits` • `Security` • `Data Export and Serialization` • `File Encoding` • `Data Validation` • `AWS S3 Paths` • `Encryption` • `Data Export Formats` • `Data Backup` • `Data Sampling`](doc/header.md)

---

### *Log Messages*
This Python file defines error and success messages, log levels, and ETL process statuses. These constants standardize messaging and facilitate debugging and monitoring of the system.

> [!NOTE]
> ```py
> from dta.logger.manager import <LOG_MESSAGE>
> ```

[`Error`](doc/logger.md#error) • [`Success`](doc/logger.md#success) • [`ETL Process Status`](doc/logger.md#etl-process-status)

---

### *System Utilities*
Provides several methods to use system functionality from just a few lines of code.

> [!NOTE]
> ```py
> from dta.system.linux_utils import <FUNCTION>
> ```

- [`delete_file()`](doc/system.md#delete_file): Deletes any specified file
- [`rename_file()`](doc/system.md#rename_file): Renames a file
- [`search_file()`](doc/system.md#search_file): Searches for the existence of a file
- [`progress_bar()`](doc/system.md#progress_bar): Waits for the specified number of seconds with an optional progress bar
- [`get_system_info()`](doc/system.md#get_system_info): Retrieves system information using the 'uname -a' command

---

### *Web Scrapping*
Provides a set of tools for automating browser interactions, allowing you to perform web scraping tasks with minimal code.

#### *Selenium*

> [!NOTE]
> ```py
> from dta.scrapping.selenium import <FUNCTION>
> ```

- [`start_browser()`](doc/scrapping.md#start_browser): Initialize a Chrome browser using Selenium
- [`export_cookies()`](doc/scrapping.md#export_cookies): Export cookies from browser
- [`import_cookies()`](doc/scrapping.md#import_cookies): Import cookies to browser
- [`check_element()`](doc/scrapping.md#check_element): Function to check if an element exists on a web page based on the provided XPath
- [`esc_or_click()`](doc/scrapping.md#esc_or_click): Function to either press the ESC key or click on an element on a web page

<br> <br>

# Authors
-   [@lucaslealll](https://github.com/lucaslealll)

<br> <br>

# Contributing
Contributions to this library are always welcome and highly encouraged.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for more information on how to get started.

### Current Maintainers
-	...

---
---

### References
- WHITTLE, Michael. How to create a Python trading library: My first Python library using EOD Historical Data (EODHD APIs). Medium - Plain English. Available at: https://python.plainenglish.io/create-a-python-trading-library-719a471bb367.

- EISINGA, Kia. How to create a Python library. Medium - Analytics Vidhya. Available at: https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f.

- GATHUKU, Kevin Ndung'u. Testing Python applications with Pytest. Semaphore. April 3, 2024. Available at: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest.