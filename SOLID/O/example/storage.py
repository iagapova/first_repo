import pathlib
import json
import yaml


class Storage:
    # создаем абстракцию
    def get_value(self, key):
        raise NotImplementedError


class JSONStorage(Storage):
    # Json сторадж, вытягиваем контент из стораджа и возвращаем значение по ключу
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r') as fd:
            data = json.load(fd)
            return data[key]


class YAMLStorage(Storage):
    # Yaml сторадж, вытягиваем контент из стораджа и возвращаем значение по ключу
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r') as fd:
            data = yaml.safe_load(fd)
            return data[key]


class Service:
    # создаем сервис для работы со стораджами. Подается сторадж и ключ - вытягивается значение
    def __init__(self, storage: Storage):
        self.storage = storage

    def get(self, key):
        return self.storage.get_value(key)


if __name__ == '__main__':

    storage_json = JSONStorage(pathlib.Path() / 'O' / 'example' / 'data.json')
    service_one = Service(storage_json)
    print(service_one.get('name'))

    storage_yaml = YAMLStorage(pathlib.Path() / 'O' / 'example' / 'data.yaml')
    service_two = Service(storage_yaml)
    print(service_two.get('name'))
