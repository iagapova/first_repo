import random


def get_random_winners(quantity, participants):
    part_list = []
    if quantity > len(participants):
        return []
    # собрали список ключей
    for k in participants.keys():
        part_list.append(k)
    # перемешали список
    random.shuffle(part_list)
    # выбираем рандомно победителей
    viners = random.sample(part_list, k=quantity)
    return viners
