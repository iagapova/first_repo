def make_request(keys, values):
    my_dict = {}
    if len(keys) != len(values):
        print('Lists lenghts are different')
        return my_dict
    else:
        my_dict = dict(zip(keys, values))
        # for i in range(len(keys)):
        #     my_dict[keys[i]] = values[i]
        return my_dict
