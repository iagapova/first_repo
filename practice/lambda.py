def hello1(day_time):
    return lambda name: f"Good {day_time}, dear {name}!"


greeting1 = hello1('evening')
print(greeting1('Iryna'))
print()

#####


def hello(day_time):
    return lambda name: lambda how_many: f"Good {day_time}, dear {name}. Glad to see you {how_many}"


greeting = hello('evening')
greet_whom = greeting('Iryna')
print(greet_whom('both'))
print()
########


def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting("Good Morning")
# print(morning_greeting)
print(morning_greeting('Bogdan'))
# Good Morning, Bogdan!

evening_greeting = greeting("Good Evening")
print(evening_greeting('Bogdan'))
# Good Evening, Bogdan!
