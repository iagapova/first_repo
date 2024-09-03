from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


class GasEngine(Engine):
    def start(self):
        return "Gas engine started"


class ElectricEngine(Engine):
    def start(self):
        return "Electric engine started"

# Автомобілі


class Car(ABC):
    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def start(self):
        pass


class GasCar(Car):
    def start(self):
        return f"Gas Car: {self.engine.start()}"


class ElectricCar(Car):
    def start(self):
        return f"Electric Car: {self.engine.start()}"


if __name__ == '__main__':
    gas_engine = GasEngine()
    electric_engine = ElectricEngine()
    mazda = GasCar(gas_engine)
    tesla = ElectricCar(electric_engine)
    print(mazda.start())
    print(tesla.start())
