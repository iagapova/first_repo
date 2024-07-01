from dataclasses import dataclass, field, InitVar
from pprint import pprint


@dataclass
class ThingData:
    name: str
    weight: int
    # аргументы со значениями должны быть в конце (только неизменяемые обьекты!)
    price: float = 0
    dims: list = field(default_factory=list)


# __init__(), __repr__(), __eq__() - автоматом созданы, но можно переопредилить

@dataclass
class V3D:

    # аттрибут не участвует в функции repr (в print(v) уже не будет x)
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)  # аттрибут не участвует в сравнения
    calc_len: InitVar[bool] = True  # значение по умолчанию
    # False означает, что этот параметр сразу не будет инициализирован
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len: bool):  # этот метод вызывается самым последним
        if calc_len:
            self.length = (self.x*self.x + self.y *
                           self.y + self.z*self.z) ** 0.5


th = ThingData(name="Учебник по Python", weight=100, price=1024)
# аналог метода __repr__: return f"Thing: {self.__dict__}"
print(th)
# pprint(ThingData.__dict__)
print(th.dims)
th.dims.append(1)
print(th.dims)

v = V3D(1, 2, 3)
print(v)
v2 = V3D(1, 2, 5)
print(v == v2)  # будет True потому что z не участвует в сравнении
v = V3D(1, 2, 3, False)
print(v)
