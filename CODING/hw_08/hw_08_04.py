from random import randrange


def get_numbers_ticket(min, max, quantity):
    if min <= 0 or max > 1000 or (max - min < quantity) or (quantity < 1):
        return []
    my_list = []
    # пока наш список не включит в себя количество символов = quantity:
    while len(my_list) < quantity:
        # выбираем рандомное число
        item = randrange(min, max)
        if item not in my_list:
            # добавляем в список если такого нет
            my_list.append(item)
    my_list.sort()
    return my_list
