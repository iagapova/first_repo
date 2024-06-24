import math


class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


@Derivate   # аналогично вызову fn_sin = Derivate(fn_sin)
def fn_sin(x):
    return math.sin(x)


# fn_sin = Derivate(fn_sin)
print(fn_sin(math.pi/3))
