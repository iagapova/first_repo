from random import randint


def draw_map():
    """Функция отрисовки мапы"""
    world_map = ''  # очищаем мапу перед рисованием
    for i in range(SIZE_Y):
        row = '|'
        for j in range(SIZE_X):
            if i == char_y and j == char_x:
                row += f'{char_sign}|'
            elif i == exit_y and j == exit_x:
                row += 'O|'
            else:
                row += ' |'
        world_map += f"{row}\n"
    print(world_map)


def get_random_coord():
    """"Функция назначает рандомные координаты соответственно мапе"""
    return randint(0, SIZE_X - 1), randint(0, SIZE_Y - 1)


def get_win_condition():
    """Функция определяет победа или нет и возвращает нужный char_sign для отрисовки мапы"""
    global char_sign
    if char_x == exit_x and char_y == exit_y:
        char_sign = 'W'
        return True
    else:
        char_sign = 'X'
        return False


def is_record():
    if len(records_table) == level_amount:
        record = min(records_table)
        print(f'ПЕМЕРОГА!!! Ты прошел все уровни!')
        if record == 1:
            print(f'Твой лучший результат: {record} шаг!')
        elif record in [2, 3, 4]:
            print(f'Твой лучший результат: {record} шага!')
        else:
            print(f'Твой лучший результат: {record} шагов!')


# определяем начальные данные
SIZE_X = 5
SIZE_Y = 5
level_amount = 3
direction = ''  # переменная для выхода или смены хода
records_table = []  # массив рекордов
attempts_limit = 10


for level in range(level_amount):  # начало игры ПО УРОВНЯМ

    if direction == 'exit':  # если юзер выбрал 'exit' сразу выходим
        break
    else:  # НАЧИНАЕМ ИГРУ
        print()
        print('----------------------------------------------')
        print(
            f'Приветствую на уровне {level + 1}! Наша мапа {SIZE_X}x{SIZE_Y}')

        # начальное положение координат игрока и выхода
        char_x, char_y = get_random_coord()
        exit_x, exit_y = get_random_coord()
        steps = 0

        while True:  # погнали играть!
            # понимаем выиграли или нет по сравнению координат и получаем char_sign
            get_win_condition()
            draw_map()  # рисуем мапу через функцию

            if get_win_condition():  # если выиграли

                print(
                    f'Круто! Уровень {level + 1} пройден! Количество шагов: {steps}')
                # дописываем шаги в массив рекордов
                records_table.append(steps)
                SIZE_X += 1  # увеличиваем размер мапы для следующего уровня
                SIZE_Y += 1  # увеличиваем размер мапы для следующего уровня
                break

            # обрабатываем ввод хода игрока
            direction = input('Enter direction (u / d / l / r): ')
            steps += 1
            if (direction == 'r' or direction == 'к') and char_x < SIZE_X - 1:
                char_x += 1
            elif (direction == 'l' or direction == 'д') and char_x > 0:
                char_x -= 1
            elif (direction == 'u' or direction == 'г') and char_y > 0:
                char_y -= 1
            elif (direction == 'd' or direction == 'в') and char_y < SIZE_Y - 1:
                char_y += 1
            elif direction == 'exit':
                print('Эх! Жаль, что не доиграли :(')
                break
            if char_x == exit_x and char_y == exit_y:
                char_sign = 'W'

# проверяем длину массива результатов чтобы понять выводить ли сообщение о рекорде
is_record()
print()
print('GAME OVER!.....')
