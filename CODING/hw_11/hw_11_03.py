class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is int or type(x) is float:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is int or type(y) is float:
            self.__y = y


point = Point("a", 10)

print(point.x)  # None
print(point.y)  # 10
