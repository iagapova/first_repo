def flatten(data):
    if data == []:
        return []
    if type(data[0]) == list:
        print(data[0][0], '---list-->', data[0][1:] + data[1:])
        # откусываем первый элемент внутреннего списка + [остальные элементы внутреннего списка + все остальное]
        return flatten([data[0][0]]) + flatten(data[0][1:] + data[1:])

    else:
        print(data[0], '---not list-->', data[1:])
        # откусываем первый элемент + все остальные элементы списка
        return [data[0]] + flatten(data[1:])
