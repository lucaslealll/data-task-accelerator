# System Utilities

Provides several methods to use system functionality from just a few lines of code.

> [!NOTE]
> ```py
> from quati.system.linux_utils import <FUNCTION>
> ```

- [`delete_file()`](system.md#delete_file): Deletes any specified file
- [`rename_file()`](system.md#rename_file): Renames a file
- [`search_file()`](system.md#search_file): Searches for the existence of a file
- [`progress_bar()`](system.md#progress_bar): Waits for the specified number of seconds with an optional progress bar
- [`get_system_info()`](system.md#get_system_info): Retrieves system information using the 'uname -a' command

---

### `delete_file()`
The `delete_file()` function deletes a specified file from a given directory. This function is useful for removing files that are no longer needed.
```py
In  [1]: delete_file("tmp/finalFolder", "test.csv")
Out [1]: 

In  [2]: delete_file("system.xlsx")
Out [2]: 
```

### `rename_file()`
The `rename_file()` function allows you to rename an existing file from its original name to a new name. It is useful for organizing files or correcting file names.
```py
In  [1]: rename_file("../Desktop/finalFolder", "test.csv", "newname.csv")
Out [1]: 
```

### `search_file()`
The `search_file()` function searches for the existence of a file within a specified directory. It returns `True` if the file is found, or `False` if it is not. You can search to a file size in *bytes* or specify a timeout in seconds.
```py
In  [1]: search_file("/home/computer/Desktop/finalFolder", "test", 100, 10)
Out [1]: True

In  [2]: search_file("test.json")
Out [2]: 
```

### `progress_bar()`
The `progress_bar()` function pauses execution for a specified number of seconds. Optionally, a progress bar can be displayed to show the remaining time during the wait.
```py
In  [1]: progress_bar(5)
Out [1]: |======>    |100% 6/10s [08 Feb, 2023 10:19:49<10:19:59]

In  [2]: progress_bar(5, False)
Out [2]: 
```

### `get_system_info()`
The `get_system_info()` function  Retrieves system information using the 'uname -a'.
```sh
In  [1]: 
    if get_system_info():
        print(info['kernel_name'])
        print(info['hostname'])
        print(info['kernel_version'])
        print(info['build_info'])
        print(info['architecture'])
Out [1]: 
    Linux
    device.hostname
    23.78.0-237.gtaV.x86_64
    #1 SMP PREEMPT_DYNAMIC Wed Jul 9 21:22:20 UTC 2021
    x86_64 x86_64 x86_64 GNU/Linux
```