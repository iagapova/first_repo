def sequence_buttons(string):
    # создаем для списка согласно задачи
    buttons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    letters = ['.,?!:', 'ABC', 'DEF', 'GHI',
               'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', ' ']
    # собираем словарь типа  'код символа' : 'комбинация клавиш'
    my_dict = {}
    for i in range(len(buttons)):
        for n in range(len(letters[i])):
            my_dict[ord(letters[i][n])] = str(buttons[i])*(n+1)
    # print(my_dict)
    # сама замена
    return string.upper().translate(my_dict)
