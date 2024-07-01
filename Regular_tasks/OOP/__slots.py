class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2D:
    # теперь нельзя создать локальное свойство классу / коллекция __dict__ уже не формируется
    __slots__ = ('x', 'y')  # __slots__ = ‘x’,  - запятая обязательна
    MAX_COORDS = 100

    def __init__(self, x, y):

        self.x = x
        self.y = y


pt1 = Point(1, 2)
pt1.z = 3

pt2 = Point2D(1, 2)
pt2.z = 3  # => error
print(pt2.z)
pt2.__dict__  # => error
print(pt2.MAX_COORDS)
