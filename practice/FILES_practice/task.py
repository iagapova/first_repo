from genericpath import exists
from pathlib import Path

my_path = Path.cwd().joinpath('practice').joinpath(
    'FILES_practice').joinpath('NEW_FOLDER')

first_file = my_path / 'file_1.txt'
second_file = my_path / 'file_2.txt'


# if not my_path.exists():
#     my_path.mkdir()

my_path.mkdir(exist_ok=True)  # создаем каталог даже если он существует

with open(first_file, 'w') as file_1:
    file_1.write("First line of text\n")
    file_1.write("Second line of text\n")

with open(first_file) as file_1:
    print(file_1.read())

with open(second_file, 'w') as file_2:
    lines = ["first1first1first", "second2second2second", "third3third3third"]
    for i in lines:
        file_2.write(i + "\n")

with open(second_file) as file_2:
    # for i in file_2.readlines():
    #     print(i.upper())
    while True:
        line = file_2.readline()
        if not line:
            break
        print(line.upper().strip())


first_file.unlink()  # удаляем файл
second_file.unlink()  # удаляем файл

if my_path.exists():
    print(my_path.rmdir())  # удаляем директорию (удаляет только пустую!)
