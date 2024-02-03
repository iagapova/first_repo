class Car:
    car_type = 'xz'

    def resolve_type(self):
        print(f"self.car_type")


class Ford(Car):
    def __init__(self, marka, year=1900):
        self.marka = 'Ford ' + marka
        self.year = year


class Shevrolet(Car):
    def __init__(self, marka, year=1900):
        self.marka = 'Shevrolet ' + marka
        self.year = year


class DefineCarType:
    def __init(self):
        self.__car_type = None

    @property
    def value(self):
        return self.__car_type

    @value.setter
    def value(self, some_year):
        if some_year <= 2014:
            self.__car_type = 'Taransas'
        else:
            self.__car_type = 'Inomarka'


class CreateDescription:
    def create_description(self, auto, car_type):
        print(
            f"My car is {auto.marka} and it's produced in {auto.year}. It's {auto.car_type}")


print('-- First car --')
aveo = Shevrolet('Aveo')
print(aveo.marka)
aveo.year = 2008
print(aveo.year)
print(aveo.car_type)

print('-- Second car --')
kuga = Ford('Kuga', 2015)
print(kuga.marka)
print(kuga.year)
print(kuga.car_type)
print('-- Third car car --')
edge = Ford('Edge', 2018)
print(edge.marka)
print(edge.year)
print(edge.car_type)
print()

dct = DefineCarType()
dct.value = aveo.year
print(dct.value)

CreateDescription.create_description(aveo, aveo.car_type)

# cd.create_description(aveo)
# cd.create_description(kuga)
# cd.create_description(edge)

# cd.value(aveo.year)
# cd.create_description(aveo)
# cd.create_description(kuga)
# cd.value(aveo)
# cd.create_description(aveo)
# cd.create_description(kuga)
# cd.create_description(edge)
