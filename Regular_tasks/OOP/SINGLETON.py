class MySingleton:
    __instance = None  # ссылка на экземпляр класса

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            # если экземпляра нет то создаем
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_message(cls):  # передаем cls чтобі добраться до иснтанса
        print(f"We wrote a message for exemplar {cls.__instance}")


a1 = MySingleton(1, 2)
a2 = MySingleton(10, 20)

print(id(a1), id(a2))

a1.print_message()
a2.print_message()
