from pathlib import Path
from os import path

print('используем функцию модуля:')
print(path.abspath('.'))  # используем функцию модуля
# /Users/irina.agapova/Documents/Projects/My repo/first_repo
print(type(path))
# <class 'module'>

print()

print('используем экземпляр класса:')
print(Path('.').absolute())  # используем экземпляр класса
# /Users/irina.agapova/Documents/Projects/My repo/first_repo
print(type(Path))
# <class 'type'>
