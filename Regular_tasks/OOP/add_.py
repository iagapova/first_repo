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


c1 = Clock(1000)
c1 = c1 + 100
c2 = Clock(1000)
c3 = c1 + c2
print('c1 + 100 = ', c1.get_time())  # __add__
print('c1 + c2 = ', c3.get_time())  # __add__
c4 = 100 + c2
print('100 + c2 = ', c4.get_time())  # __radd__
c2 += 100
print('c2 += 100 = ', c2.get_time())  # __iadd__
