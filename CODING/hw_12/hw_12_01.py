import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)


def read_contacts_from_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


my_list = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
},
    {
    "name": "Iryna Agapova",
    "email": "iagapova#gmail.com",
    "phone": "8099-922-0607",
    "favorite": True,
}]

write_contacts_to_file('TEXT.bin', my_list)
print(read_contacts_from_file('TEXT.bin'))
