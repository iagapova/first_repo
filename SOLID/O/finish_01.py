from math import pi


class Shape:
    def area_of(self):
        raise NotImplementedError


class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_of(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area_of(self):
        return self.radius**2 * pi


class AreaCalculator:
    def __init__(self, shapes: list[Shape]):
        self.shapes = shapes

    def total_area(self) -> float:
        sum = 0
        for el in self.shapes:
            sum += el.area_of()
        return sum


if __name__ == '__main__':

    ar_sh = AreaCalculator([Rect(10, 10), Rect(4, 5), Circle(20), Rect(3, 3)])
    area = ar_sh.total_area()
    print(area)
