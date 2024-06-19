import re


def generator_numbers(string=""):
    numbers = re.findall(r'\d+', string)
    for item in numbers:
        yield int(item)


def sum_profit(string):
    s = 0
    for item in generator_numbers(string):
        s += item
    return s
