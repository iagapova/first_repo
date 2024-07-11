import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:

    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.fh = None
        # self.count_save = Contacts.count_save
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)
            self.fh = open(self.filename)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attrs = self.__dict__.copy()
        attrs['fh'] = None
        attrs['count_save'] += 1  # увеличиваем счетчик
        # print(content.__dict__)
        # print('---Contacts.count_save--- ', Contacts.count_save)
        return attrs


contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("_hw_12_05.dat", contacts)
persons.save_to_file()
print(persons.__dict__)
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3
