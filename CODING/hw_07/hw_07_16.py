def decode(data):
    if data == []:
        return []
    if data[0].isalpha():
        # print([data[0]]*data[1], '---->', data[2:])
        return [data[0]]*data[1] + decode(data[2:])
