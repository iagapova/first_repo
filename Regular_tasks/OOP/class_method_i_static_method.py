class Vector:
    MAX_COORD = 10
    MIN_COORD = 0

    @classmethod
    # для проверки внутри класса, используется для работы с аттрибутами класса
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

            print('Тут мы тоже можем вызвать статик метод: ', self.norm2(5, 5))
        else:
            print("Введены некорректные значения")

    def get_coord(self):
        return (self.x, self.y)

    @staticmethod
    # независимый, сервисный метод который можем юзать как внутри класса так и вне
    def norm2(x, y):
        return x**2 + y**2


v1 = Vector(-3, 5)
print(v1.get_coord())
print()
v2 = Vector(3, 5)
print(v2.get_coord())

print(v1.norm2(10, 5))
