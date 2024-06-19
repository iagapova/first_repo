from functools import reduce


def amount_payment(payment):
    # фильтруем положительные элементы
    pos_values = [item for item in filter(lambda x: x > 0, payment)]
    # зовем функцию reduce
    result = reduce((lambda x, y: x + y), pos_values)
    return result
