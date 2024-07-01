class Geom:
    def __init__(self, x1, y1, x2, y2):
        print(f'Инициализатор класса {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def __draw__(self):
        print('Drawing line')


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)  # ыызов инициализатора базового класса
        print(f'Инициализатор класса Rect')
        self.fill = fill

    def __draw__(self):
        print('Drawing rect')


l = Line(1, 2, 3, 4)
r = Rect(1, 2, 3, 4, 'black')

print(l)
print(r)
print(l.__dict__)
print(r.__dict__)
