from copy import deepcopy

dict_one = {
    'Name': 'Iryna',
    'Surname': 'Agapova',
    'Age': 42,
    'Friends': []
}
print()
dict_two = dict_one  # копируем id словаря
dict_three = dict_one.copy()  # копируем словарь, но с id списка
dict_four = deepcopy(dict_one)  # копируем словарь, но без id списка

dict_one['City'] = 'Kharkiv'
dict_two['Friends'].append('Hanna')

print('dict_one (original): ', dict_one)
print()
print('dict_two (id copy): ', dict_two)
print()
print('dict_three (shallow copy): ', dict_three)
print()
print('dict_four (deep copy): ', dict_four)
