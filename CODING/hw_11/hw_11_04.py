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
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates
        # делаем словарь из координат с ключами 0 и 1
        self.data = {0: self.coordinates.x, 1: self.coordinates.y}

    def __setitem__(self, index, value):
        # мапаем значения на ключи 0 и 1
        if index in self.data.keys():
            self.data[index] = value
        else:
            print('wrong index')

    def __getitem__(self, index):
        # достаем значения по ключам 0 и 1
        result = self.data[index]
        return result


vector = Vector(Point(1, 10))

print(vector.coordinates.x)  # 1
print(vector.coordinates.y)  # 10

vector[0] = 10  # Встановлюємо координату x вектора 10

print(vector[0])  # 10
print(vector[1])  # 10
