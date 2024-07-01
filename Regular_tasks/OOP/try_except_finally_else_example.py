def get_values():
    try:
        x, y = map(int, input('Введите значения x, y: ').split())
        return x, y
    except ValueError:  # можно указать except ArithmeticError чтобы охватить дочерние ошибки
        print('Неверное значение y')
        return 0, 0
    finally:
        # ! ВАЖНО что это действие выполняется ДО return
        print("finally выполняется ДО return")


x, y = get_values()
print(x, y)
