car1 = {'car': 'Shevrolet Aveo',
        'year': 2008}

car2 = {'car': 'Ford Kuga',
        'year': 2012}

car3 = {'car': 'Ford Edge',
        'year': 2018}


my_autopark = [car1, car2, car3]

first, second, third = my_autopark

print(first)
print(second)
print(third)
print('--- my favorite cars ---')


def make_smth(car, year):
    return f"My {car} is issued in {year}"


print(make_smth(**car1))
print(make_smth(**car2))
print(make_smth(**car3))
