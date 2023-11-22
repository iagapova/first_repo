def merge_lists_to_dict(list1, list2):
    return dict(zip(list1, list2))


my_list1 = ['Name', 'Surname', 'Age']
my_list2 = ['Iryna', 'Agapova', '21']

print(merge_lists_to_dict(list2=[0, 1, True], list1=['a', 'b', 'c']))
print()
print(merge_lists_to_dict(['Name', 'Surname', 'Age'], list2=my_list2))


def update_car_info(**car):
    car['is_available'] = True
    return car


print(update_car_info(brand='Ford', price=20000))
