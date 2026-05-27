import os
import sys
from datetime import datetime


def create_path(dirs: list) -> str:
    return os.path.join(*dirs)


def check_for_flag(command: list[str], flag: str) -> int | None:
    try:
        return command.index(flag, 1)
    except ValueError:
        return None


def write_terminal_to_file(filename: str) -> None:
    with open(filename, "a") as file:
        file_size = os.path.getsize(filename)
        line = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        counter = 0
        while line != "stop":
            file.write(
                (
                    str(counter) + " " if counter > 0
                    else ("" if file_size == 0 else "\n")
                )
                + line + "\n"
            )
            counter += 1
            line = input("Enter content line: ")


command = sys.argv

ind_md = check_for_flag(command, "-d")
ind_mf = check_for_flag(command, "-f")

if ind_md:
    if not ind_mf or (ind_mf and ind_mf < ind_md):
        path_list = command[ind_md + 1:]
    else:
        path_list = command[ind_md + 1:ind_mf]
    os.makedirs(create_path(path_list), exist_ok=True)
else:
    path_list = []

if ind_mf:
    full_file_name = create_path(path_list + command[ind_mf + 1:ind_mf + 2])
    write_terminal_to_file(full_file_name)
