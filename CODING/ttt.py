# Ваш словник
my_dict = {'a': 3, 'b': 1, 'c': 2}

# Сортування словника за значеннями і отримання відсортованого списку кортежів (ключ, значення)
sorted_list = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

# Перетворення відсортованого списку кортежів в словник
sorted_dict = dict(sorted_list)

print(sorted_dict)
