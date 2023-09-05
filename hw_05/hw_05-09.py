def formatted_numbers():
    list = []
    # формируем заголовок
    s = ("|{: ^10}|{: ^10}|{: ^10}|".format('decimal', 'hex', 'binary')) 
    list.append(s)
    # формируем список сторок для списка
    for i in range(16):
        num = ('|{:<10d}|{: ^10x}|{: >10b}|'.format(i, i, i))   
        list.append(num)
    return list


for el in formatted_numbers():
    print(el)