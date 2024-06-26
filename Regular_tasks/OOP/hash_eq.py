# print(hash(123))
# print(hash("Python"))
# print(hash((1, 2, 3)))

# hash вычисляется только для не изменяемых обьектов
# hash перестает работать если переопределен метод


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point(1, 2)
p2 = Point(1, 2)
# print(hash(p1), hash(p2), sep="\n")   # работает если есть нет метода __eq__ и хеши разные
# print(p1 == p2) # => False если есть нет метода __eq__

# print(hash(p1), hash(p2), sep="\n")   # не работает если есть есть метод __eq__ - unhashable type
# print(p1 == p2) # => True если есть метод __eq__

# подправляем работу хеша с переопределенным методом через метод __hash__
print(hash(p1), hash(p2), sep="\n")
print(p1 == p2)

d = {}
d[p1] = 1
d[p2] = 2
print(d)  # из-за переопределенного hash это один ключ
