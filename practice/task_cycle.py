def dict_to_list(my_dict):
    new_list = []
    for k, v in my_dict.items():
        new_list.append(
            (k, v*2)) if type(v) == int else new_list.append((k, v))
    return new_list


my_dict = {'car': 'Ford',
           'year': 2018,
           'country': 'Italy',
           25: 5,
           10: 1.3}

print(dict_to_list(my_dict))


def filter_list(my_list, my_type):
    new_list = []
    for i in my_list:
        if type(i) == my_type:
            new_list.append(i)
    return new_list


my_list = [1, True, 0, -5, 'Ford', 1.2, 'is', 'my', 3, 'car']

print('Юзаем функцию с циклом: ', filter_list(my_list, int))
print('Юзаем функцию с циклом: ', filter_list(my_list, str))


def filter_list_func(my_list, my_type):
    return list(filter(lambda elem: type(elem) is my_type, my_list))


print('Юзаем функцию filter: ', filter_list_func(my_list, str))
