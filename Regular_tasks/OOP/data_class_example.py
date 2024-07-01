from dataclasses import dataclass, field, InitVar


@dataclass
class MyAuto:
    marka: str
    model: str
    price: int = field(repr=False)
    km: int
    used_years: int
    fuel: str = field(default="gasoline")
    usage: float = field(init=False, default=0)
    is_gas: InitVar[bool] = False

    def __post_init__(self, is_gas: bool):
        if is_gas:
            self.fuel = f"{self.fuel} + gas"
        self.usage = 9 * self.used_years


if __name__ == "__main__":
    aveo = MyAuto("Shevrolet", "Aveo", 6500, 60000, 3)
    kuga = MyAuto("Ford", "Kuga", 12000, 60000, 5, "disel")
    edge = MyAuto("Ford", "Edge", 25000, 20000, 4, "gasoline", True)

    print(f'{aveo}. Я накатала {aveo.usage} км')
    print(f'{kuga}. Я накатала {kuga.usage} км')
    print(f'{edge}. Я накатала {edge.usage} км')
