class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        # добавляет нолик спереди если состоит из одной цифры
        return str(x).rjust(2, "0")

    def __add__(self, other):  # = self + other
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError(
                "Значение должно быть числом либо классом Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):  # = other + self
        return self + other  # тут уже срабатывает метод __add__

    def __iadd__(self, other):  # += other
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError(
                "Значение должно быть числом либо классом Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        self.seconds += sc
        return self

    def __mul__(self, other):  # = self * other
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError(
                "Значение должно быть числом либо классом Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds * sc)

    def __rmul__(self, other):  # = other * self
        return self * other  # тут уже срабатывает метод __mul__

    def __imul__(self, other):  # *= other
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError(
                "Значение должно быть числом либо классом Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        self.seconds *= sc
        return self

    def __sub__(self, other):  # = self - other
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError(
                "Значение должно быть числом либо классом Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
            print('class')
        print(f'{self.seconds} - {sc}')
        return Clock(self.seconds - sc)

    def __rsub__(self, other):  # = other - self
        print(f'--- {self} - {other}')
        return (self - other)*(-1)   # тут уже срабатывает метод __sub__

    def __isub__(self, other):  # -= other
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError(
                "Значение должно быть числом либо классом Clock")
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        self.seconds -= (sc)
        return self


# c1 = Clock(3600)
# print('c1 = ', c1.get_time())
# c1 = c1 + 60
# print('c1 + 60 = ', c1.get_time())  # __add__
# c2 = Clock(120)
# print('c2 = ', c2.get_time())
# c3 = c1 + c2
# print('c1 + c2 = ', c3.get_time())  # __add__
# c4 = 60 + c2
# print('60 + c2 = ', c4.get_time())  # __radd__
# c2 += 60
# print('c2 += 60 = ', c2.get_time())  # __iadd__

print()
r1 = Clock(60)
print('r1 = ', r1.get_time())
# r1 = r1 - 120
# print('r1 - 120 = ', r1.get_time())  # __sub__
r2 = Clock(120)
print('r2 = ', r2.get_time())
r3 = r1 - r2
print('r1 - r2 = ', r3.get_time())  # __sub__
r4 = 60 - r2
print('60 - r2 = ', r4.get_time())  # __rsub__
r2 -= 180
print('r2 -= 60 = ', r2.get_time())  # __isub__
print()

m1 = Clock(15)
print('m1 = ', m1.get_time())
m1 = m1 * 1
print('m1 * 3 = ', m1.get_time())  # __add__
m2 = Clock(60)
print('m2 = ', m2.get_time())
m3 = m1 * m2
print('m1 * m2 = ', m3.get_time())  # __add__
m4 = 15 * m2
print('15 * m2 = ', m4.get_time())  # __radd__
m2 *= 15
print('m2 *= 60 = ', m2.get_time())  # __iadd__
