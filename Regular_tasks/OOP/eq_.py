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
    def check_value(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError(
                "Правый операнд долженбыть целым числом или экзепляром класса Clock")
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):  # c1 != c2    ==   not(c1 == c2)  т.е. необязательно определять метод __ne__
        sc = self.check_value(other)
        return self.seconds == sc

    def __lt__(self, other):  # c1 > c2    ==   not(c1 < c2)  т.е. необязательно определять метод __gt__
        sc = self.check_value(other)
        return self.seconds < sc

    def __le__(self, other):  # c1 >= c2    ==   not(c1 <= c2)  т.е. необязательно определять метод __ge__
        sc = self.check_value(other)
        return self.seconds <= sc


c1 = Clock(1000)
c2 = Clock(1000)
c3 = Clock(200)
print(c1 == c2)
print(c1 == 1000)
print(c3 == c2)
# c1 != c2    ==   not(c1 == c2)  т.е. необязательно определять метод __ne__
print(c3 < c2)
print(c3 >= c2)
