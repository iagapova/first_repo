from dataclasses import dataclass, field
from typing import Any


class GoodsMethodsFactory:
    @staticmethod
    def get_init_measure():
        return [0, 0, 0]


@dataclass
class Goods:
    current_uid = 0  # реализуем счетчик

    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        Goods.current_uid += 1
        self.uid = Goods.current_uid
        print('Goods: post_init')


@dataclass
class Books(Goods):
    title: str = ""
    author: str = ""
    price: float = 0
    weight: int | float = 0
    # можно юзать функцию для определения списка
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)

    def __post_init__(self):
        super().__post_init__()
        print('Books: post_init')


a = Books(10, 20, "My_title", "Agapova")
print(a)
b = Books(11, 22, "My_title1", "Markova")
print(b)
