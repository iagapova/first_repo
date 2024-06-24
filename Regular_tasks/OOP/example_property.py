from string import ascii_letters
S_RUS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя-"
S_RUS_UPPER = S_RUS.upper()


class Person:

    def __init__(self, fio, age, passport, weight):
        self.validate_fio(fio)  # валидируем ФИО

        self.__fio = fio.split()
        self.age = age
        self.passport = passport
        self.weight = weight

    @classmethod
    def validate_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        letters = ascii_letters + S_RUS + S_RUS_UPPER
        f = fio.split()  # делим на слова
        if len(f) != 3:  # если ФИО не из 3х слов
            raise TypeError("Неверный формат ФИО, необходимо 3 слова")

        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть минимум один символ")
            # выкидываем все что не буквы и тире и если что-то осталось то ошибка
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО должны быть только буквы или тире")

    @classmethod
    def validate_age(cls, age):
        if type(age) != int or age < 14 or age > 120:
            raise ValueError(
                "Возраст должен быть целым числом в диапазоне [14: 120]")

    @classmethod
    def validate_weight(cls, weight):
        if type(weight) not in (int, float) or weight < 20:
            raise ValueError(
                "Вес должен быть числом больше 20")

    @classmethod
    def validate_passport(cls, passport):
        if type(passport) != str or len(passport) != 8:
            raise TypeError("Неверный формат паспорта")
        print(passport[0:2], passport[0:2].isdigit())
        print(not passport[2:].isdigit())
        if (not passport[0:2].isalpha()) or (not passport[2:].isdigit()):
            raise ValueError("Неверный формат паспорта (XX123456)")

    @property
    def fio(self):
        return self.__fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.validate_age(age)  # валидируем возраст
        self.__age = age

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.validate_passport(passport)  # валидируем вес
        self.__passport = passport

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.validate_weight(weight)
        self.__weight = weight


ira = Person("Агапова Ирина Ивановна", 43, "FH708560", 70.0)
print(ira.__dict__)
ira.age = 20
print()
print('ФИО: ', ira.fio)
print('Возраст: ', ira.age)
print('Паспорт: ', ira.passport)
print('Вес: ', ira.weight)
