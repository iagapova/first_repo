class Point:
    def __init__(self, x, y):
        self.__x = self.__y = 0
        if self.__check_values(x) and self.__check_values(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_values(cls, arg):
        """метод класса на перепроверку значения"""
        return type(arg) in (int, float)

    def set_coord(self, x, y):
        if self.__check_values(x) and self.__check_values(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Не верный формат")

    def get_value(self):
        return self.__x, self.__y


pt = Point(103, 2)
print(pt.__dict__)
pt.set_coord(5, '6')
print(pt.__dict__)
