# print(bool(123))
# print(bool(-123))
# print(bool(0))  # False только для пустых элементов


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        return self.x == self.y


p1 = Point(1, 2)
p2 = Point(3, 3)

print(bool(p1))  # всегда True для обьектов пользовательского класса
print(bool(p2))
p3 = Point(0, 0)
print(bool(p3))  # теперь после переопределения функции len будет 0
# использование
if p2:
    print('Сработал наш переопределенный метод bool')
else:
    print('Вернулся False у нашего метода bool')
