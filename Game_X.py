from random import randint

SIZE_X = 5
SIZE_Y = 5

level_amount = 3
direction = ''  # переменная для выхода или смены хода
records_table = []

for level in range(level_amount):  # начало игра по уровням
    if direction == 'exit':  # если юзер выбрал 'exit' сразу выходим
        break
    else:  # начинаем игру
        print()
        print('----------------------------------------------')
        print(
            f'Приветствую на уровне {level + 1}! Наша мапа {SIZE_X}x{SIZE_Y}')

        # начальное положение координат игрока
        char_x = randint(0, SIZE_X - 1)
        char_y = randint(0, SIZE_Y - 1)
        char_sign = 'X'

        # начальное положение координат выхода
        exit_x = randint(0, SIZE_X - 1)
        exit_y = randint(0, SIZE_Y - 1)
        steps = 0

        while True:  # погнали играть!
            win_condition = char_x == exit_x and char_y == exit_y
            if win_condition:  # на случай если совпали координаты играка и выхода
                char_sign = 'W'
                records_table.append(steps)

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

            if win_condition:  # если выиграли

                char_sign = 'W'
                print(f'ПЕРЕМОГА!!! Твой результат: {steps} шагов!')
                print(f'Уровень {level + 1} пройден!')
                # records_table.append(steps)
                # увеличиваем размер мапы
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
record = min(records_table)

if len(records_table) == level_amount:
    print(f'Круто! Ты прошел все уровни!')
    print(f'Твой лучший результат: {record} шага(ов)!')
print('GAME OVER!.....')
