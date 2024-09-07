from abc import ABC, abstractmethod


class Car:  # класс для создания авто
    def __init__(self):
        self.parts = {}

    def add(self, key: str, value: str):
        self.parts[key] = value

    def show(self):
        print("Автомобиль состоит из:")
        for key, value in self.parts.items():
            print(f"{key}: {value}")


class GazCar():
    def __init__(self):
        self.car = Car()

    def build_wheels(self):
        self.car.add("Колеса", "4")

    def build_doors(self):
        self.car.add("Двери", "4")

    def build_engine(self):
        self.car.add("Газовый мотор", "2.0")

    def get_result(self) -> Car:  # возвращаем класс авто
        return self.car


class ElectricCar():
    def __init__(self):
        self.car = Car()

    def build_wheels(self):
        self.car.add("Колеса", "4")

    def build_doors(self):
        self.car.add("Двери", "3")

    def build_engine(self):
        self.car.add("Электрический мотор", "200")

    def get_result(self) -> Car:  # возвращаем класс авто
        return self.car


class Director():  # движок
    def __init__(self, builder):
        self.builder = builder

    def contructor(self):  # сборка авто
        self.builder.build_wheels()
        self.builder.build_doors()
        self.builder.build_engine()


if __name__ == "__main__":
    auto_builder1 = GazCar()  # создаем движок газового авто
    director = Director(auto_builder1)  # директор принял билдер
    # директор создает авто через конструктор (теперь в автобилдере есть авто )
    director.contructor()
    auto1 = auto_builder1.get_result()
    auto1.show()
    print()
    auto_builder2 = ElectricCar()
    director = Director(auto_builder2)
    director .contructor()
    auto2 = auto_builder2.get_result()
    auto2.show()
