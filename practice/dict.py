my_dict = {}
print(my_dict)
print(type(my_dict))


# keys = []
# for i in range(3):
#     print('введите ', i+1, '-й ключ:', sep='')
#     keys.append(input())

keys = []
values = []


def get_info(my_dict):
    k = input(f'введите ключ: ')
    v = input(f'введите значение для {k}: ')
    my_dict[k] = v
    return my_dict


for i in range(3):
    get_info(my_dict)

# for i in range(3):
#     # [keys.append(input(f'введите {i+1}-й ключ:')) for i in range(3)]
#     keys.append(input(f'введите {i+1}-й ключ: '))
#     values.append(input(f'введите значение для {keys[i]} :'))
#     my_dict[keys[i]] = values[i]


# my_dict = {}
# for i in range(3):
#     my_dict[keys[i]] = values[i]

# my_dict = {keys[i]: values[i] for i in range(3)}

print('Мой созданный словарь: ', my_dict)
my_dict['City'] = 'Kharkiv'
print()
print('Мой созданный словарь с новым значением: ', my_dict)
my_dict.pop('test')
print()
print('Мой созданный словарь без ключа: ', my_dict)
