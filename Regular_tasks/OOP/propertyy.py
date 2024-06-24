class Person:

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    # обьект свойство для работы с защищенным свойством
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old


ira = Person('Iryna', 20)
print(ira.__dict__)
print(ira.old)

ira.old = 43
print(ira.old)
print(ira.__dict__)
del ira.old
print(ira.__dict__)
