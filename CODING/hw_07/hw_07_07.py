def data_preparation(list_data):
    new_list = []
    for i in list_data:
        if len(i) < 3:
            new_list.extend(i)
        else:
            i.remove(max(i))
            i.remove(min(i))
            new_list.extend(i)
    new_list.sort(reverse=True)
    return new_list
