import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        new_copy = Person(self.name, self.email, self.phone, self.favorite)
        # print('-', new_copy.__dict__)
        # print('-', new_copy.__dict__)
        return new_copy


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        new_copy = Contacts(self.filename, self.contacts)
        # new_copy.filename = copy.copy(self.filename)
        new_copy.contacts = copy.copy(self.contacts)
        return new_copy

    def __deepcopy__(self, memo):
        new_deepcopy = Contacts(self.filename, self.contacts)
        # new_deepcopy.filename = copy.deepcopy(self.filename)
        new_deepcopy.contacts = copy.deepcopy(self.contacts)
        return new_deepcopy


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

irina = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)
