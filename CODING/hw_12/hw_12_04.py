import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        self.filename = filename
        if contacts is None:
            contacts = []
        self.contacts = contacts

    def save_to_file(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self, file)  # сохраняет экземпляр класса

    def read_from_file(self):
        with open(self.filename, 'rb') as file:
            result = pickle.load(file)
        return result


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


persons = Contacts('_hw_12_04.bin', contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)  # False
print(persons.contacts[0])
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True
