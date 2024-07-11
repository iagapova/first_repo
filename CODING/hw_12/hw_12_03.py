import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w') as file:
        field_names = ['name', 'email', 'phone', 'favorite']

        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for i in contacts:
            writer.writerow(i)


def read_contacts_from_file(filename):
    contacts = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # конвертируем значение в булевское
            row['favorite'] = True if row['favorite'] == 'True' else False
            contacts.append(row)  # добавляем строку в список
    return contacts


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

write_contacts_to_file('TEST.CSV', my_list)
print()
print(read_contacts_from_file('TEST.CSV'))
