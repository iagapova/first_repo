class Car:
    def __init__(self, brand, model, year):
        self.brand = brand.upper()
        self.model = model.capitalize()
        self.year = year

    def change_year(self, year):
        self.year = year

    def print_car_info(self):
        print(f'My car {self.brand} {self.model} is produced in {self.year}')

    # конвертируем класс в строку
    def __str__(self):
        return f"My car {self.brand} {self.model} is produced in {self.year}"

    @staticmethod
    def print_date(year):
        return 2023 - year


first_car = Car('Shevrolet', 'aveo', '2000')
print(first_car.__dict__)
first_car.change_year('2008')
first_car.print_car_info()
print(first_car)
print('Aveo is ', Car.print_date(2012), 'years old')
print('Edge is ', first_car.print_date(2018), 'years old')
