import pickle
from pathlib import Path

# сериализация обьектов
print('--- сериализация обьектов ---')
a = (1, 2, 3)
serialized = pickle.dumps(a)
print('serialized tupple: ', serialized)
b = pickle.loads(serialized)
print('deserialized tupple: ', b, type(b))
print()
# файловая сериализация
print('--- сериализация файлов ---')
# print(Path.cwd())
my_path = Path.cwd().joinpath('CODING').joinpath('hw_12').joinpath('test.bin')
# print(my_path)

with open(my_path, 'wb') as file:  # сериализация в файл
    pickle.dump(a, file)

with open(my_path, 'rb') as file:  # десериализация из файла
    new_a = pickle.load(file)

print('deserialized file: ', new_a)
print()

# сериализация классов
print('--- сериализация классов ---')


class Character:
    def __init__(self, name):
        self.name = name


char = Character('Irina')
serialized_class = pickle.dumps(char)
print('serialized class: ', serialized_class)
deserialized_class = pickle.loads(serialized_class)
print('deserialized class: ', deserialized_class, deserialized_class.name)
print()

# сериализация классов через файл
# ВАЖНО! если распаковка идет в другом файле - то нельзя десереализовать без самого класса. У класса должно совпадать имя и аттрибуты!
my_path_class = Path.cwd().joinpath('CODING').joinpath(
    'hw_12').joinpath('test_class.bin')
with open(my_path_class, 'wb') as file:
    pickle.dump(char, file)

with open(my_path_class, 'rb') as file:
    deserialized_cl = pickle.load(file)
print('deserialized class from file: ', deserialized_cl, deserialized_cl.name)
print()
