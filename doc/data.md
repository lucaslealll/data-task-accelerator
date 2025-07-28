# Dataframes

Provides methods to quickly adjust dataframes.

> [!NOTE]
> ```py
> from quati.data.df_normalizer import <FUNCTION>
> ```

- [`norm_str_num_values()`](data.md#norm_str_num_values): Converts string-based number values to their numerical equivalents
- [`norm_rename_columns()`](data.md#norm_rename_columns): Renames DataFrame columns based on a normalization function
v
---

### `norm_str_num_values()`
The `norm_str_num_values()` function converts string-based number values (like "1K" or "10.3M") into their corresponding numerical values. It’s useful for normalizing data inputs with suffixes like "K" for thousand, "M" for million, etc.

```py
In  [1]: norm_str_num_values("1K")
Out [1]: 1000

In  [2]: norm_str_num_values("550.1K")
Out [2]: 550100

In  [3]: norm_str_num_values("10.3M")
Out [3]: 10300000
```

### `norm_rename_columns()`
The `norm_rename_columns()` function renames DataFrame columns using a specified normalization function. It’s helpful for standardizing column names across datasets.

```py
In  [1]: 
    Col_A    Cól-B_    cOl__C    col_d
0       3        ar        zz       11
1      12        tg        aa       22

In  [1]: df.columns = df.columns.map(normalize_and_rename_columns)
Out [1]: 
    col_a    col_b    col_c    col_d
0       3       ar       zz       11
1      12       tg       aa       22
```