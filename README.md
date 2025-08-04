<div style="font-family: 'Outfit'">

<div align="center">
	<picture>
	<!-- <source media="(prefers-color-scheme: dark)" srcset="assets/quati_white.svg"> -->
	<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/quati-dev/quati/refs/heads/main/assets/quati.svg">
		<img src="https://raw.githubusercontent.com/quati-dev/quati/refs/heads/main/assets/quati.svg" width="100%">
	</picture>
	<br><br><br>
	<hr>
<h1>quati: A python <u>Quick Actions Toolkit</u> for data engeneering</h1>

<img src="https://img.shields.io/badge/Author-lucaslealll-blue?logo=github&logoColor=white"> <img src="https://img.shields.io/badge/Status-Beta-DF1F72"> <img src="https://img.shields.io/badge/License-MIT-750014.svg">
<br>
<img src="https://img.shields.io/pypi/v/quati.svg?label=Version&color=white"> <img src="https://img.shields.io/pypi/pyversions/quati?logo=python&logoColor=white&label=Python"> <img src="https://img.shields.io/badge/Code Style-Black Formatter-111.svg"> 
<br>
<img src="https://img.shields.io/pypi/dm/quati.svg?label=PyPI Downloads"> 
</div>

## What is it?
**quati** provides dynamic functions aimed at data engineering, offering
a wide range of collections to accelerate development. It has a comprehensive and
flexible ecosystem of **tools**, **libraries**, and **community resources**,
allowing data engineers to easily build and deploy applications.

<h2>Table of Contents</h2><br>

- [What is it?](#what-is-it)
- [Main Features](#main-features)
- [Where to get it / Install](#where-to-get-it--install)
- [Documentation](#documentation)
- [License](#license)
- [Dependencies](#dependencies)

## Main Features
Here are just a few of the things that pandas does well:

- [`norm_str_num_values()`](doc/data.md#norm_str_num_values): Converts string-based number values to their numerical equivalents
- [`norm_rename_columns()`](doc/data.md#norm_rename_columns): Renames DataFrame columns based on a normalization function
- [`sync_dtypes_with_table()`](doc/google.md#sync_dtypes_with_bigquery_table): Synchronize the data types of a Pandas DataFrame with a BigQuery table's schema
- [`quick_query()`](doc/google.md#quick_query): Executes a BigQuery SQL query and returns the result as a Pandas DataFrame
- [`gsheets_get_worksheet()`](doc/google.md#gsheets_get_worksheet): Import a worksheet object from gsheets
- [`gsheets_get_worksheet_df()`](doc/google.md#gsheets_get_worksheet_df): Import a worksheet object from gsheets as a pandas dataframe
- [`gsheets_dedup()`](doc/google.md#gsheets_dedup): Returns dataframe where the column passed as parameter is considered the core set for duplicate data row remover
- [`gsheets_worksheet_next_available_row()`](doc/google.md#gsheets_worksheet_next_available_row): Return the ID of the next cell into which data can be entered
- [`gsheets_update()`](doc/google.md#gsheets_update): Update a Google Sheets spreadsheet from a reference column
- [`send_email()`](doc/messenger.md#send_email): Send an email (Types: error, tip, note, important or warning) with main info about it
- [`delete_file()`](doc/system.md#delete_file): Deletes any specified file
- [`rename_file()`](doc/system.md#rename_file): Renames a file
- [`search_file()`](doc/system.md#search_file): Searches for the existence of a file
- [`progress_bar()`](doc/system.md#progress_bar): Waits for the specified number of seconds with an optional progress bar
- [`get_system_info()`](doc/system.md#get_system_info): Retrieves system information using the 'uname -a' command
<!-- - [`start_browser()`](doc/scrapping.md#start_browser): Initialize a Chrome browser using Selenium -->
<!-- - [`export_cookies()`](doc/scrapping.md#export_cookies): Export cookies from browser -->
<!-- - [`import_cookies()`](doc/scrapping.md#import_cookies): Import cookies to browser -->
<!-- - [`check_element()`](doc/scrapping.md#check_element): Function to check if an element exists on a web page based on the provided XPath -->
<!-- - [`esc_or_click()`](doc/scrapping.md#esc_or_click): Function to either press the ESC key or click on an element on a web page -->

## Where to get it / Install
The source code is currently hosted on GitHub at: https://github.com/quati-dev/quati

<!-- 
> [!IMPORTANT]
> It's essential to **upgrade pip** to the latest version to ensure compatibility with the library.
> ```sh
> # Requires the latest pip
> pip install --upgrade pip
> ```
-->
- [PyPI](https://pypi.org/project/quati/)
	```sh
	# PyPI
	pip install quati
	```
- GitHub
	```sh
	# or GitHub
	pip install git+https://github.com/quati-dev/quati.git
	```

## Documentation
The official documentation is here [Documentation](doc/DOCUMENTATION.md).

## License
[MIT](LICENSE)

## Dependencies
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Selenium](https://www.selenium.dev/)
- [gspread](https://docs.gspread.org/)

See the [full installation instructions](INSTALLATION.md) for minimum supported versions of required, recommended and optional dependencies.

<hr>

[⇧ Go to Top](#table-of-contents)

</div>