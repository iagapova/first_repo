class Point:
    def __init__(self, *args):
        self.coords = args  # кортеж координат

    def __len__(self):
        # метод для получения длинны списка координат через экзеспляр класса
        return len(self.coords)

    def __abs__(self):
        # применяем abs к каждому элементу списка координат
        return list(map(abs, self.coords))


p = Point(1, -2, 3)
print(p.coords, type(p.coords))
print(len(p), " - получили длину списка координат через экземпляр класса")
print(abs(p), " - применили abs для каждого элемента списка координат через экземпляр класса")
