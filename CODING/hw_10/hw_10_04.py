class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        Animal.color = color


first_animal = Animal("First Animal", 25)
second_animal = Animal("Second Animal", 22)
first_animal.change_color("red")
print(Animal.color)
