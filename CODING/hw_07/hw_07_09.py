def all_sub_lists(data):
    new_list = [[]]
    for i in range(len(data)):
        for j in range(len(data)):
            if i+j < len(data):
                # print(j, i+j+1, '     ', data[j:j+i+1])
                new_list.append(data[j:j+i+1])
    return new_list
