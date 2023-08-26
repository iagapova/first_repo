from random import randint


def get_random_password():
    s = ''
    for i in range(8):
        num = randint(40, 126) # получаем рандомный символ
        s += chr(randint(40, 126))
    print(s)
    return s

get_random_password()