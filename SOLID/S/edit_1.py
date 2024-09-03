class Contact:
    def value_of(self):
        raise NotImplementedError


class ContactPhone(Contact):
    def __init__(self, operator_code: str, phone: str):
        self.phone = phone
        self.operator_code = operator_code

    def value_of(self):
        return f"+38{self.operator_code}-{self.phone}"


class ContactAddress(Contact):
    def __init__(self, city: str, street: str):
        self.city = city
        self.street = street

    def value_of(self):
        return f"{self.city} {self.street}"


class Person:
    def __init__(self, name: str, phone: Contact, address: Contact):
        self.name = name
        self.phone = phone
        self.address = address

    def get_phone_number(self):
        return f"{self.name}: {self.phone.value_of()}"

    def get_address(self):
        return f"{self.name}: {self.address.value_of()}"


if __name__ == '__main__':
    phone_1 = ContactPhone('099', '922-0607')
    addr_1 = ContactAddress('Харьков', '23 Августа')
    person = Person("Alexander", phone_1, addr_1)
    print(person.get_phone_number())
    print(person.get_address())
