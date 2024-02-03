import random

# получаем рандомное число
random_num = random.randint(1, 5)

while True:
    num = int(input("Введи число от 1 до 5: "))
    if num != random_num:
        print("Не верно =( Попробуй снова")
        print()
        continue  # снова возвращаемся в начало цикла
    print("Еее! Ты угадал! Поздравляю!")
    break
