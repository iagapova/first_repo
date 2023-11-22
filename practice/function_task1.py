# def merge_lists_to_dict(list1, list2):
#     return dict(zip(list1, list2))


# my_list1 = ['Name', 'Surname', 'Age']
# my_list2 = ['Iryna', 'Agapova', '21']

# print(merge_lists_to_dict(my_list1, my_list2))

# def sum_tuple(*arg):
#     print(arg[0])
#     print(sum(arg))


# sum_tuple(2, 5, 3)

def get_dict(**person):
    print(person)
    # {'name': 'Iryna', 'posts': 21}
    return f"{person['name']} wrote {person['posts']} posts"


info = get_dict(name='Iryna', posts=21)
print(info)
