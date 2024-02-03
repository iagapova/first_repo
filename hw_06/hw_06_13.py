from contextlib import ExitStack
from genericpath import exists
import shutil
from pathlib import Path


def create_backup(path, file_name, employee_residence):
    if not path.exists():
        Path.mkdir(path)
    with open(f'{path}/{file_name}', 'wb') as my_file:
        for k, v in employee_residence.items():
            item = f"{k} {v}\n"
            my_file.write(item.encode())
    my_zip = shutil.make_archive('backup_folder', 'zip', path)
    return my_zip


path = Path.cwd().joinpath('hw_06/111')
file_name = '!hw_06_13_BIN_FILE.bin'
employee_residence = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}

print(create_backup(path, file_name, employee_residence))

Path('backup_folder.zip').unlink()
Path('hw_06/111/!hw_06_13_BIN_FILE.bin').unlink()
Path('hw_06/111').rmdir()
