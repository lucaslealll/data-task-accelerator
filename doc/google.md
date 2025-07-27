# Google

Provides methods to interact with Google resources sucha as Sheets and BigQuery, to boost data manipulation.

> [!NOTE]
> ```py
> from dta.google.big_query import <FUNCTION>
> ```

- [`sync_dtypes_with_table()`](google.md#sync_dtypes_with_bigquery_table): Synchronize the data types of a Pandas DataFrame with a BigQuery table's schema
- [`quick_query()`](google.md#quick_query): Executes a BigQuery SQL query and returns the result as a Pandas DataFrame

> [!NOTE]
> ```py
> from dta.google.sheets import <FUNCTION>
> ```

- [`gsheets_get_worksheet()`](google.md#gsheets_get_worksheet): Import a worksheet object from gsheets
- [`gsheets_get_worksheet_df()`](google.md#gsheets_get_worksheet_df): Import a worksheet object from gsheets as a pandas dataframe
- [`gsheets_dedup()`](google.md#gsheets_dedup): Returns dataframe where the column passed as parameter is considered the core set for duplicate data row remover
- [`gsheets_worksheet_next_available_row()`](google.md#gsheets_worksheet_next_available_row): Return the ID of the next cell into which data can be entered
- [`gsheets_update()`](google.md#gsheets_update): Update a Google Sheets spreadsheet from a reference column

---

### `sync_dtypes_with_table()`
The `sync_dtypes_with_table()` function imports a specific worksheet from a Google Sheets document. You can specify the worksheet name, the data page name, and the index of the worksheet within the document.

```py
In [1]: df = synced_df = sync_dtypes_with_table(df, "1das34fas", "dataset.tb_a", "credential_file.json", debug=True)
```

### `quick_query()`
The `quick_query()` function executes an SQL query on a Google Sheets document and returns the results as a DataFrame. You can specify the SQL query, the Google Sheets document ID, and the credentials file.

```py
In [1]: df = sync_dtypes_with_table("SELECT * FROM table", "1das34fas", "credential_file.json")
```

---

### `gsheets_get_worksheet()`
The `gsheets_get_worksheet()` function imports a specific worksheet from a Google Sheets document. You can specify the worksheet name, the data page name, and the index of the worksheet within the document.

```py
In [1]: wks = gsheets_get_worksheet(GSHEETS_CREDENTIAL, "worksheet name", "data page name", 6)
```

### `gsheets_get_worksheet_df()`
The `gsheets_get_worksheet_df()` function imports a specific worksheet from Google Sheets and converts it directly into a Pandas DataFrame. This allows for easier data manipulation and analysis.

```py
In [1]: df = get_gsheets_worksheet_df(GSHEETS_CREDENTIAL, "worksheet name", "data page name", 6)
```

### `gsheets_dedup()`
The `gsheets_dedup()` function removes duplicate rows from a DataFrame based on a specified column. The provided column is considered the core set for identifying duplicates in the dataset.

```py
In [1]: dedup_df = gsheets_dedup(GSHEETS_CREDENTIAL, "post_title", "facebook_posts", "all_posts", "last", "A5")
```

### `gsheets_worksheet_next_available_row()`
The `gsheets_worksheet_next_available_row()` function identifies the next available row (ID) in a specified worksheet where data can be entered. This is useful for appending new data without overwriting existing values.

```py
In  [1]: df = gsheets_worksheet_next_avaible_row(worksheet, "A")
Out [1]: 'A237'
```

### `gsheets_update()`
The `gsheets_update()` function updates a Google Sheets worksheet with data from a DataFrame. You can specify the reference column where data insertion should begin.

```py
In [1]: gsheets_worksheet_update(worksheet, metrics_df, "A3")
```