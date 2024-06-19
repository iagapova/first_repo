def normal_name(list_name):
    new_list = []
    for item in map(lambda item: item.capitalize(), list_name):
        new_list.append(item)
    return new_list
