def lookup_key(data, value):
    s = []
    for i, v in data.items():
        if v == value:
            #print(i)
            s += [i]
    print(s)
lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2)
