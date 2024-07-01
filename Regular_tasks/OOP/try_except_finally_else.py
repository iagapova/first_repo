print("Program is started")

try:
    x, y = map(int, input('Введите значения x, y: ').split())
    print(x/y)
except ValueError:  # можно указать except ArithmeticError чтобы охватить дочерние ошибки
    print('Неверное значение y')
except ZeroDivisionError as z:
    print(z)
except:  # указываем родительский класс чтобы охватить почти все ошибки
    print('Ошибка')
else:
    print("Не произошло никаких исключений. Программа завершена")
finally:
    print("Не важно была ли ошибка или нет - мы пишем это сообщение")
