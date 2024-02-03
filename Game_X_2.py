from random import randint, choice

SIZE_X = randint(5, 10)
SIZE_Y = randint(5, 10)


def draw_map(objects, size_x=SIZE_X, size_y=SIZE_Y):
    """Функция отрисовки мапы"""
    world_map = []  # очищаем мапу перед рисованием
    for j in range(size_y):
        row = []
        for i in range(size_x):
            row.append(' ')
        world_map.append(row)

    for obj in reversed(objects):
        world_map[obj['y']][obj['x']] = obj['sign']
    # world_map[enemy_y][enemy_x] = enemy_sign
    # world_map[exit_y][exit_x] = exit_sign
    # world_map[char_y][char_x] = char_sign
    return world_map


def generate_enemies(N):
    enemies = []
    for _ in range(N):
        enemy = {'x': randint(0, SIZE_X - 1),
                 'y': randint(0, SIZE_Y - 1),
                 'sign': 'E',
                 'type': 'enemy'}
        enemies.append(enemy)
    return enemies


def check_state(objects):
    """Функция определяет победа или нет и возвращает нужный char_sign для отрисовки мапы"""
    for obj in objects:
        if obj['type'] == 'char':
            char = obj
        elif obj['type'] == 'portal':
            portal = obj
        elif obj['type'] == 'enemy':
            loss_condition = char['x'] == obj['x'] and char['y'] == obj['y']
            if loss_condition:
                char['sign'] = 'L'
                print('Ооой! Ты проиграл(((')
                break
    win_condition = char['x'] == portal['x'] and char['y'] == portal['y']

    if win_condition:
        char['sign'] = 'W'
        print(f'Круто! Уровень пройден! Количество шагов: {steps}')

    return win_condition or loss_condition


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


def move(direction, obj, size_x=SIZE_X, size_y=SIZE_Y):
    if (direction == 'r' or direction == 'к') and obj['x'] < size_x - 1:
        obj['x'] += 1
    elif (direction == 'l' or direction == 'д') and obj['x'] > 0:
        obj['x'] -= 1
    elif (direction == 'u' or direction == 'г') and obj['y'] > 0:
        obj['y'] -= 1
    elif (direction == 'd' or direction == 'в') and obj['y'] < size_y - 1:
        obj['y'] += 1


# определяем начальные данные
records_table = []
level_amount = 1
direction = ''  # переменная для выхода или смены хода


if direction == 'exit':  # если юзер выбрал 'exit' сразу выходим
    print('GAME OVER!.....')
else:  # НАЧИНАЕМ ИГРУ
    print()
    print('----------------------------------------------')
    print(
        f'Приветствую! Наша мапа {SIZE_X}x{SIZE_Y}')

    # начальное положение координат игрока и выхода
    char = {'x': randint(0, SIZE_X - 1),
            'y': randint(0, SIZE_Y - 1),
            'sign': 'X',
            'type': 'char'}

    portal = {'x': randint(0, SIZE_X - 1),
              'y': randint(0, SIZE_Y - 1),
              'sign': 'O',
              'type': 'portal'}

    enemies = generate_enemies(5)

    objects = [char, portal] + enemies
    steps = 0

    while True:  # погнали играть!
        # понимаем выиграли или нет по сравнению координат и получаем char_sign
        end_flag = check_state(objects)
        # рисуем мапу через функцию
        world_map = draw_map(objects)
        for row in world_map:
            print(f"|{'|'.join(row)}|")

        if end_flag:
            break

        for obj in objects:
            if obj['type'] == 'enemy':
                direction = choice('rludкдгв')
                move(direction, obj)
            elif obj['type'] == 'char':
                #   обрабатываем ввод хода игрока
                direction = input('Enter direction (u / d / l / r): ')

                steps += 1
                if direction == 'exit':
                    print('Эх! Жаль, что не доиграли :(')
                    break
                else:
                    move(direction, obj)


# проверяем длину массива результатов чтобы понять выводить ли сообщение о рекорде
is_record()
print()
print('GAME OVER!.....')
