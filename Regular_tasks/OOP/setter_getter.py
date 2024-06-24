from accessify import private, protected
# принцип инкапсуляции - работа только через публичные методы


class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    # заюзаем его для проверки числа
    def __check_value(cls, arg):
        return type(arg) in (int, float)

    @private  # сделать метод приватным
    @classmethod
    def check_value123(cls, arg):
        return type(arg) in (int, float)

    def set_coord(self, x, y):
        # для изменения приватных аттрибутов класса
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):
        # для получения приватных аттрибутов класса
        return self.__x, self.__y


pt = Point(1, 2)
# print(pt.__x, pt.__y)   # ДАСТ ОШИБКУ потому что доступа нет
pt.set_coord(5, 10)
print(pt.get_coord())
print('--')
# так все равно добраться можно, но не желательно!
print(pt._Point__x, pt._Point__y)
print()
# уже не добраться до метода, он приватен
print(pt.check_value123(555))
print()
pt.set_coord('5', 10)
