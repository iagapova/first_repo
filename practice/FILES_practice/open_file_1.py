from pathlib import Path

print(Path.cwd())
my_path = Path.cwd().joinpath('practice').joinpath('FILES_practice')
file_path = Path.cwd().joinpath('practice').joinpath(
    'FILES_practice').joinpath('os_dir.py')
print(my_path)
print(Path('my_file.txt').exists())  # проверка в корне питона
print(Path('os_dir.py').exists())  # проверка в корне питона
print(file_path.exists())
print()

with open(my_path / 'my_file.txt') as my_file:
    print(my_file.read())

with open(my_path / 'my_file.txt') as my_file:
    print(my_file.readlines())
print()

with open(my_path / 'my_file.txt', 'w') as my_file:
    my_file.write("First line of my file\n")

with open(my_path / 'my_file.txt') as my_file:
    print(my_file.read())

with open(my_path / 'my_file.txt', 'a') as my_file:
    my_file.write("Second line of my file\n")

with open(my_path / 'my_file.txt') as my_file:
    print(my_file.read())

new_file = open('TEST.txt', 'w')  # создание файла в корне питона
