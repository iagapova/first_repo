class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def show_info(self):
        return f"My car {self.model} is produced in {self.year}"


class Owner:
    def __init__(self, name):
        self.name = name

    def show_owner(self):
        return f"The lucky owner is {self.name}"


# ПРОСТО
print()
print("ПРОСТО:")
aveo = Car('Shevrolet', 2008)
print(aveo.show_info())
irina = Owner('Iryna')
print(irina.show_owner())
print("-------------------")
print()


# КОМПОЗИЦИЯ


class Kuga(Car):
    def __init__(self, model, year, name):
        super().__init__(model, year)
        self.owner = Owner(name)

    def show(self):
        return f"My car {self.model} is produced in {self.year} and the owner is {self.owner.name}"


ford_composition = Kuga('KUGA', 2012, 'Irina')
print("КОМПОЗИЦИЯ:")
print(ford_composition.show())


# АБСТРАКЦИЯ


class Edge(Car):
    def __init__(self, model, year, owner: Owner):
        super().__init__(model, year)
        self.owner = owner

    def show(self):
        return f"My car {self.model} is produced in {self.year} and the owner is {self.owner.name}"


print("-------------------")
print()

ford_asbraction = Edge('EDGE', 2018, Owner('Irina'))
print("АБСТРАКЦИЯ:")
print(ford_asbraction.show())
