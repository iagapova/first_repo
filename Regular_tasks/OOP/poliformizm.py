# методы, которые обязательно нужно переопределять в дочерних классах и которые не имеют собственной реализации = абстракты
class Geom:
    def get_pr(self):  # хорошая практика отлавливать не заимплеменченный функционал
        raise NotImplementedError(
            "В дочернем классе должен быть переопредлен метод get_pr()")


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4*self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # def get_pr(self):
    #     return self.a + self.b + self.c


items = [Rectangle(1, 2), Rectangle(3, 4), Square(5),
         Triangle(1, 2, 3), Square(3)]
for i in items:
    print(i.get_pr())
