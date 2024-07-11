import pickle
from pathlib import Path


class Reader:
    ### принимает файл и создает файловый дескриптор внутри себя ###
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name)
        self.a = 123

    def read(self):
        return self.file.read()

    # этот метод вызывается при реализации и по умолчанию возвращает: return self.__dict__
    def __getstate__(self):
        attrs = self.__dict__.copy()
        attrs['file'] = None
        print('before serialization: ', attrs)
        print()
        return attrs

    def __setstate__(self, attrs):
        self.__dict__ = attrs
        self.file = open(self.file_name)
        print('after serialization: ', self.__dict__)
        print()


my_path = Path.cwd().joinpath('CODING').joinpath('hw_12').joinpath('TEXT.txt')
# print(my_path)
reader = Reader(my_path)
print(reader)
print(reader.__dict__)
print()
serialized = pickle.dumps(reader)
print('serialized= ', serialized)
print()
deserialized = pickle.loads(serialized)
print('deserialized= ', deserialized)
print(deserialized.read())
