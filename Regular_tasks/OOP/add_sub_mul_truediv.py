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

    @classmethod
    def check_value(cls, arg):
        if not isinstance(arg, (int, Clock)):
            raise ArithmeticError(
                "Значение должно быть числом либо классом Clock")

    def __add__(self, other):  # self.__add__(other)
        self.check_value(other)
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):  # self.__radd__(other):  60 + c2 =  c2.__radd__(60)
        return self + other  # тут уже срабатывает метод __add__

    def __iadd__(self, other):  # self.__iadd__(other): c2.__iadd__(60)
        self.check_value(other)
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        self.seconds += sc  # просто увеличиваем переменную секунды
        return self  # и возвращаем тот же класс (не пересоздаем класс)

    def __mul__(self, other):  # self.__mul__(other)
        self.check_value(other)
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds * sc)

    def __rmul__(self, other):  # self.__rmul__(other)
        return self * other  # тут уже срабатывает метод __mul__

    def __imul__(self, other):  # self.__imul__(other)
        self.check_value(other)
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        self.seconds *= sc
        return self

    def __sub__(self, other):  # self.__sub(other)
        self.check_value(other)
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
            # print('class')
        # print(f'{self.seconds} - {sc}')
        return Clock(self.seconds - sc)

    def __rsub__(self, other):  # self.__rsub(other): 60 - r2 = r2.__rsub(other)
        # print(f'--- {self} - {other}')
        return (self - other)*(-1)   # тут уже срабатывает метод __sub__

    def __isub__(self, other):  # self.__isub__(other): r2 -= 180 = r2.__isub__(180)
        self.check_value(other)
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        self.seconds -= sc
        return self


print('-------------------------- ADD -------------------------')
c1 = Clock(3600)
c2 = Clock(120)
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'item', 'formula', 'method', 'seconds', 'time'))
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'c1',  '---',  '---', f'{c1.seconds}', f'{c1.get_time()}'))
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'c2', '---',  '---', f'{c2.seconds}', f'{c2.get_time()}'))
c1 = c1 + 60

print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format('c1', 'c1 + 60', '__add__',
      f'{c1.seconds}', f'{c1.get_time()}'))
c3 = c1 + c2
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'c3',  'c1 + c2',  '__add__', f'{c3.seconds}', f'{c3.get_time()}'))
c4 = 60 + c2
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'c4',  '60 + c2',  '__radd__', f'{c4.seconds}', f'{c4.get_time()}'))
c2 += 60
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'c2',  'c2 += 60',  '__iadd__', f'{c2.seconds}', f'{c2.get_time()}'))
print()

print('-------------------------- MUL -------------------------')
m1 = Clock(15)
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'item', 'formula', 'method', 'seconds', 'time'))
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'm1',  '---',  '---', f'{m1.seconds}', f'{m1.get_time()}'))
m1 = m1 * 1
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format('m1', 'm1 * 1', '__mul__',
      f'{m1.seconds}', f'{m1.get_time()}'))
m2 = Clock(60)
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'm2',  '---',  '---', f'{m2.seconds}', f'{m2.get_time()}'))
m3 = m1 * m2
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'm3',  'm1 * m2',  '__mul__', f'{m3.seconds}', f'{m3.get_time()}'))
m4 = 15 * m2
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'm4',  '15 * m2',  '__rmul__', f'{m4.seconds}', f'{m4.get_time()}'))
m2 *= 15
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'm2',  'c2 *= 15',  '__iadd__', f'{m2.seconds}', f'{m2.get_time()}'))
print()

print('-------------------------- SUB -------------------------')
r1 = Clock(60)
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'item', 'formula', 'method', 'seconds', 'time'))
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'r1',  '---',  '---', f'{r1.seconds}', f'{r1.get_time()}'))
r1 = r1 - 120

print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'r1', 'r1 - 120',  '__sub__', f'{r1.seconds}', f'{r1.get_time()}'))
r2 = Clock(120)
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format('r2', '---', '---',
      f'{r2.seconds}', f'{r2.get_time()}'))
r3 = r1 - r2
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'r3',  'r1 - r2',  '__sub__', f'{r3.seconds}', f'{r3.get_time()}'))
r4 = 60 - r2
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'r4',  '60 - r2',  '__rsub__', f'{r4.seconds}', f'{r4.get_time()}'))
r2 -= 180
print("|{:^10}|{:^10}|{:^10}|{:^10}|{:^10}|".format(
    'r2',  'r2 -= 180',  '__isub__', f'{r2.seconds}', f'{r2.get_time()}'))
print()
