import datetime
import glob
import os
import subprocess
import warnings
from datetime import datetime
from time import sleep

from tqdm import tqdm

warnings.filterwarnings("ignore")

DEFAULT_CONFIG_DIR = "./"

DEFAULT_FILE_DIR_PATH = DEFAULT_CONFIG_DIR
DEFAULT_FILENAME = f"{DEFAULT_CONFIG_DIR}filename.txt"
DEFAULT_NEW_FILENAME = f"{DEFAULT_CONFIG_DIR}new_filename.txt"


def rename_file(
    file_dir_path=DEFAULT_FILE_DIR_PATH,
    filename=DEFAULT_FILENAME,
    new_filename=DEFAULT_NEW_FILENAME,
):
    """Rename a file.

    Parameters
    ----------
    `file_dir_path` : Full file path.
    `filename` : Full filename or its prefix.
    `new_filename` : The new name to assign to this file

    Examples
    --------
    Rename a file called test.csv to newname.csv

    ```
    rename_file("/home/computer/Desktop/finalFolder", "test.csv", "newname.csv")
    ```
    """
    for file in glob.glob(f"{file_dir_path}{filename}*"):
        name = file
    os.rename(f"{name}", f"{file_dir_path}{new_filename}")


def delete_file(file_dir_path=DEFAULT_FILE_DIR_PATH, filename=DEFAULT_FILENAME):
    """Delete a file.

    Parameters
    ----------
    `file_dir_path` : Full file path.
    `filename` : Full filename or its prefix.

    Examples
    --------
    Delete a file called test.csv

    ```
    delete_file("/home/computer/Desktop/finalFolder", "test.csv")
    ```
    """
    subprocess.getoutput(f"rm {file_dir_path}{filename}")


def search_file(
    file_dir_path=DEFAULT_FILE_DIR_PATH,
    filename=DEFAULT_FILENAME,
    min_file_size=1,
    timeout=15,
):
    """Checks the existence of a file, returning True or False.

    Parameters
    ----------
    `file_dir_path` : Full file path.
    `filename` : Full filename or is prefix.
    `min_file_size` : The minimum size of a file to be able to use it
    `timeout` : Maximum waiting time to find the file

    By default:
        - `min_file_size` : is considered 1
            - must be informed in bytes
        - `timeout` : wait 15 seconds

    Examples
    --------
    Looking for a file that actually exists, called "teste.txt", with a minimum of 100 Bytes and waiting a maximum of 10 seconds

    ```
    file_exists("/home/computer/Desktop/finalFolder", "test", 100, 10)
    True
    ```
    """

    fully_downloaded_file = False
    start_time = int((datetime.now()).strftime("%H%M%S"))
    current_time = start_time
    stop_time = start_time + timeout

    while fully_downloaded_file == False:
        try:
            for file in glob.glob(f"{file_dir_path}{filename}*"):
                pwd_file = str(file)

            file_exists = os.path.isfile(f"{pwd_file}")

            if file_exists == True:
                file_size_bytes = int(os.stat(f"{pwd_file}").st_size)

                if file_size_bytes < min_file_size:
                    sleep(1)
                elif file_size_bytes >= min_file_size:
                    fully_downloaded_file = True
                    return fully_downloaded_file
        except:
            current_time = int((datetime.now()).strftime("%H%M%S"))
            if fully_downloaded_file == False and current_time >= stop_time:
                return fully_downloaded_file


def progress_bar(seconds=1, progressbar: bool = True):
    """Shows a progress bar while waiting X seconds

    By default:
        - sec = 1

    ```
    progress_bar(5)
    |======>    |100% 6/10s [08 Feb,2023 10:19:49<10:19:59]


    progress_bar(5, progressbar=False)
    ```
    """
    desc = f"Waiting {seconds}s"
    if progressbar:
        for i in tqdm(range(seconds), desc=desc):
            sleep(1)
    else:
        sleep(seconds)


def get_system_info():
    """
    Retrieves system information using the 'uname -a' command.

    Returns:
        `dict`: A dictionary containing the system information with the following keys:
            - `kernel_name`: The name of the kernel.
            - `hostname`: The hostname of the system.
            - `kernel_version`: The version of the kernel.
            - `build_info`: Additional build information.
            - `architecture`: The system architecture.

    Raises:
        subprocess.CalledProcessError: If the 'uname -a' command fails to execute.

    ```
    info = get_system_info()
    print(info['hostname'])
    print(info['kernel_version'])
    ```
    """
    try:
        # Execute the 'uname -a' command
        result = subprocess.run(
            ["uname", "-a"], capture_output=True, text=True, check=True
        )
        # Capture the output of the command
        uname_output = result.stdout.strip()

        # Split the output into parts
        parts = uname_output.split()

        # Create a dictionary with system information
        system_info = {
            "kernel_name": parts[0],
            "hostname": parts[1],
            "kernel_version": parts[2],
            "build_info": " ".join(parts[3:6]),
            "architecture": " ".join(parts[6:]),
        }

        return system_info
    except subprocess.CalledProcessError as e:
        print(f"Error executing uname command: {e}")
        return None
