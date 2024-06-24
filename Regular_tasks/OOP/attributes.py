from typing import Any
# https://www.youtube.com/watch?v=CAx-NLFc-Z4&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E&index=8&ab_channel=selfedu


class Point:
    MIN_VALUE = 0
    MAX_VALUE = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 0

    def get_coord(self, x, y):
        return (self.x, self.y)

    @classmethod
    # изменение аттрибута класса
    def change_right_bound(cls, value):
        cls.MAX_VALUE = value

    def __getattribute__(self, item):
        # метод для вызова аттрибута и можно иногда запрещать доступ к некоторым аттрибутам
        if item == "z":
            raise AttributeError("Доступ запрещен")
        else:
            print("__getattribute__ был вызван")
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        # метод для применения аттрибута
        if key == "zzz":
            raise AttributeError("Недопустимое имя аттрибута")
        else:
            print("__setattr__ был вызван")
            object.__setattr__(self, key, value)
            # или так, чтобі не возникла рекурсия:
            # self.__dict__[key] = value

    def __getattr__(self, item):
        # обращение к несуществующему аттрибуту класса - pt.xxx
        print("__getattr__ был вызван")
        return False  # если хотим False в случае если нет аттрибута и идет к нему обращение

    def __delattr__(self, item):
        # удаление аттрибута класса
        print("__delattr__ был вызван")
        object.__delattr__(self, item)


pt = Point(1, 5)
print(pt.MAX_VALUE)
pt.change_right_bound(100)
print(pt.MAX_VALUE)
print(pt.__dict__)
# print(Point.__dict__)
# print(pt.z)
# pt.zzz = 3
