def lookup_key(data, value):
    s = []
    for i, v in data.items():
        if v == value:
            #print(i)
            s += [i]
    return s