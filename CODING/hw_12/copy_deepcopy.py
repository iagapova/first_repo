from copy import copy, deepcopy


class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.bag = ['potion', 'money']

    def add_to_bag(self, item):
        self.bag.append(item)

    def __copy__(self):
        char = Character(self.name)
        return char

    def __deepcopy__(self, m):
        obj = Character(self.name)
        m[id(self)] = obj

        for k, v in self.__dict__.items():
            setattr(obj, k, deepcopy(v, m))
        return obj


char = Character('Iryna')
char.add_to_bag(['apple', 'beer'])
print(char.bag)
char_copy = copy(char)
char_deepcopy = deepcopy(char)
print(char)
print(char_copy)
print(char_deepcopy)
print()
char.name = 'Irina'
char.bag[2] = 'ice cream'
print(char.name, char.bag, id(char.bag))
print(char_copy.name, char_copy.bag)
print(char_deepcopy.name, char_deepcopy.bag, id(char_deepcopy.bag))
