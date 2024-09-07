from abc import ABC, abstractmethod
from enum import Enum


class TypeShape(str, Enum):
    circle = "cirle"
    square = "square"


class Drawings(ABC):
    @abstractmethod
    def draw_shape(self, x, y, shape):
        pass


class DrawingRed(Drawings):
    def draw_shape(self, x, y, shape):
        print(f"Red drawing a {shape} at {x} and {y}")


class DrawingBlue(Drawings):
    def draw_shape(self, x, y, shape):
        print(f"Blue drawing a {shape} at {x} and {y}")


class Shape(ABC):
    def __init__(self, x, y, drawing: Drawings):  # тут создали мост
        self.x = x
        self.y = y
        self.drawing = drawing

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        self.drawing.draw_shape(self.x, self.y, TypeShape.circle.value)


class Square(Shape):
    def draw(self):
        self.drawing.draw_shape(self.x, self.y, TypeShape.square.value)


if __name__ == '__main__':
    kruzhok = Circle(0, 0, DrawingRed())
    kvadrat = Square(1, 1, DrawingBlue())
    kruzhok.draw()
    kvadrat.draw()
