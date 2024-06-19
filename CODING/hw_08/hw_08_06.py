from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    summ = 0
    for i in number_list:
        summ += Decimal(i)
    return summ/len(number_list)
