# распаковка списка
my_list = [1, 2, 3]
first_l, second_l, third_l = my_list
first, *remaining_list = my_list

print(first_l)
print(second_l)
print(third_l)
print('---------')
print(first)
print(remaining_list)
print('--- распаковка кортежа ------')

# распаковка кортежа
my_tuple = ('one', 'two', 'three')
first_t, second_t, third_t = my_tuple
first_tt, *remaining_tuple = my_tuple

print(first_t)
print(second_t)
print(third_t)
print('---------')
print(first_tt)
print(remaining_tuple)
print('--- распаковка словаря ------')

# распаковка словаря
my_dict = {
    'name': 'Iryna',
    'quantity': 5
}


def write_award(name, quantity=0):
    if not quantity:
        return f"{name} has no medals..."
    return f"{name} has {quantity} medals!"


print(write_award(**my_dict))

fff, sss = my_dict.values()
print(fff)
print(sss)
print('--- вызов словаря ------')
# вызов словаря
my_list1 = ['Iryna', 5]


def make_text(name, quantity):
    return f"{name} has {quantity} medals"


print(make_text(*my_list1))
