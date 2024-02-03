# две реализации проверки формата числа

# С ИСПОЛЬЗОВАНИЕМ ФУНКЦИИ и чекаем каждое число отдельно
def provide_num():
    """Функция ввода числа и проверка его на формат с обработкой ошибки

    Returns:
        num: float(num)
    """
    while True:
        num = input()
        try:
            num = float(num)
        except ValueError:
            print("Ты ввел чушь. Давай мне верное число")
        if type(num) != float:
            continue
        break
    return num


while True:
    print("Введи первое число: ")
    num1 = provide_num()
    print("Введи второе число: ")
    num2 = provide_num()
    # обрабатываем нуляку
    while num2 == 0:
        print("На ноль делить нельзя, ну же, введи второе число: ")
        num2 = provide_num()

    print(f"Наш результат: {num1} / {num2} = {num1/num2}")
    print()
    answer = (input("Посчитаем еще что-нибудь? (yes/no)"))
    # гоняем пока говорит 'yes'
    if answer == 'no':
        print("Спасибо, что использовал нашу программу! До новых встреч!")
        break


# БЕЗ ФУНКЦИЙ и снова вводим пару чисел
# while True:
#     try:
#         num1 = float(input("Введи первое число: "))
#         num2 = float(input("Введи второе число: "))
#         if num2 == 0:
#             print("Ну не ноль же! о_0 Давай по-новому!")
#             continue
#     except ValueError:
#         print("Не, давай с самого начала...")
#         continue

#     print(f"Наш результат: {num1} / {num2} = {num1/num2}")
#     print()
#     answer = (input("Посчитаем еще что-нибудь? (yes/no)"))
#     if answer == 'no':
#         print("Спасибо, что использовал нашу программу! До новых встреч!")
#         break
