class Car:
    def __init__(self):
        self.type = None

    def get_type(self):
        return self.type


class SportCar(Car):
    def __init__(self):
        super().__init__()
        self.type = "SportCar"


class FamilyCar(Car):
    def __init__(self):
        super().__init__()
        self.type = "FamilyCar"


# фабрика-класс, создает экземпляры классов


class CarFactory:
    def __init__(self):
        self.cars = {}

    def register(self, car_type, car_class):
        self.cars[car_type] = car_class

    def create_car(self, car_type):
        if car_type in self.cars:
            return self.cars[car_type]()
        raise ValueError(f'Invalid car type: {car_type}')


if __name__ == '__main__':
    factory = CarFactory()
    factory.register('sport', SportCar)
    factory.register('family', FamilyCar)

    car1 = factory.create_car('sport')
    print(car1.get_type())

    car2 = factory.create_car('family')
    print(car2.get_type())
