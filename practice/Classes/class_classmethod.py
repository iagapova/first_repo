class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = 0
        self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    @staticmethod  # просто функция внутри класса
    def norm(x, y):
        return x*x + y*y


pt = Vector(103, 2)
print(pt.__dict__)
print(pt.norm(5, 2))
