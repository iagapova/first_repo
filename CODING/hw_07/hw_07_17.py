def encode(data):
    data = ''.join(data)
    if data == '':
        return []
    # если в списке все буквы одинаковы
    if data.count(data[0]) == len(data):
        return [data[0]] + [len(data)]
    else:
        i = 1
        # считаем сколько повторяющихся символов + отрезаем остаток
        while data[0] == data[i]:
            i += 1
        return [data[0]] + [i] + encode([data[i:]])
