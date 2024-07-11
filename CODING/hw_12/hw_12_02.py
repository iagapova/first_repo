import json


def write_contacts_to_file(filename, contacts):
    content = {'contacts': contacts}
    with open(filename, 'w') as file:
        json.dump(content, file)


def read_contacts_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)['contacts']


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

write_contacts_to_file('TEST.json', my_list)
print(read_contacts_from_file('TEST.json'))
