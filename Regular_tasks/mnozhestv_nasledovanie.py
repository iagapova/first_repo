class A:
    def __init__(self, x, y):
        # вызов инициализатора класса # не указывать дополнительных параметров!
        super().__init__()
        print('Init A')
        self.x = x
        self.y = y

    def print_info(self):
        print('Вызов из класса A')


class B:
    ID = 0

    def __init__(self):  # не указывать дополнительных параметров!
        super().__init__()  # вызов инициализатора класса следующего класса
        print('Init B')
        # make some functional here

    def print_info(self):
        print('Вызов из класса B')


class C:
    def __init__(self):  # не указывать дополнительных параметров!
        print('Init C')
        # make some functional here

    def print_info(self):
        print('Вызов из класса C')


class D(A, B, C):  # не важно какой параметр если не указывать доп параметры в init методах
    def print_info(self):
        # чтобы всегда обходить порядок запуска ==  C.print_info(aaa)
        C.print_info(self)


aaa = D(1, 2)
print(aaa)
aaa.print_info()  # та же логика приоритизации для методов с одним именем
print()
B.print_info(aaa)
print(D.__mro__)
print()
