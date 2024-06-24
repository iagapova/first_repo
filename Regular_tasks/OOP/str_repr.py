
class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        # str для пользователей (для печати и str представления)
        return f"{self.name}"

    def __repr__(self):
        # repr вывод служебной информации для отладки - вызов в консоли как имя экземпляра
        return f"Имя моего кота - {self.name}. {self.__class__}"


cat = Cat("Васька")
print(cat.__repr__())  # cat
print(cat)  # print(cat), str(cat)
