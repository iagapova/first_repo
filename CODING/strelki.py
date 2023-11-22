mas = """33 02 23 31 11 20 11 01 03 32 32 03 21 03 30 21 30 23 12 32 12 32 03 13 32 32 13 02 13 03 20 01 20 20 00 00 32 31 30 20 12 33 20 00 33 32 02 01 12 33 02 33 02 11 22 30 11 21 12 03 32 22 13 13 32 00 11 21 30 12 23 30 01 33 10 21 30 13 20 02 10 02 31 30 11 10 00 11 02 10 33 01 21 23 00 00 12 30 13 10 32 12 11 10 23 32 00 03 10 13 21 11 33 21 01 32 10 12 21 22 22 31 01 10 01 02 02 30 03 10 10 13 02 32 12 01 33 03 21 02 11 02 31 13 22 01 23 00 01 20 22 12 10 01 03 20 02 01 30 10 03 22 20 01 03 13 33 33 22 31 33 31 31 20 01 02 01 02 11 23 33 33 21 00 21 13 13 33 30 20 11 31 31 00 00 30 33 22 32 02 12 23 00 13 11 31 30 23 33 21 31 30 20 01 23 23 20 30 13 03 30 30 23 00 20 22 02 10 00 00 00"""
# mas = "32 20 31 23 03 00 00 33 02 23 31 11 20 33"
mmm = mas.split(' ')

# for i in mmm:
#     # m.append()
#     # print(bin(int(i)).removeprefix('0b'))
#     print(i)

my_dict = {
    '00': 0,
    '01': 1,
    '02': 2,
    '03': 3,
    '10': 4,
    '11': 5,
    '12': 6,
    '13': 7,
    '20': 8,
    '21': 9,
    '22': 10,
    '23': 11,
    '30': 12,
    '31': 13,
    '32': 14,
    '33': 15}

# print(my_dict)

new_list = []
new_str = ''
for i in mmm:
    new_list.append(my_dict[i])
   # new_str += str(my_dict[i])

# print(new_list)

for i in new_list:
    a = bin(int(i)).removeprefix('0b')
    if len(a) != 4:
        b = '0'*(4 - len(a)) + a
        # print(b)
    else:
        b = a
    # print(b)
    new_str += b

print('Получили строку: ', new_str)
# print(bin(int(i)).removeprefix('0b'))
# spec = '22'
# print(my_dict[spec])
# print(bin(my_dict[spec]).removeprefix('0b'))

# new_str = '111100101011'
# shifr = '010101'
shifr = '0010010'
decoding = ''

# print('Новая строка:', new_str)
shifr = shifr * (len(new_str) // len(shifr))

# new_str1 = new_str

for i in range(len(new_str)):
    # print(shifr[i], bool(shifr[i]))
    # print(str(int(new_str[i]) ^ int(shifr[i])))
    decoding += str(int(new_str[i]) ^ int(shifr[i]))

print('Прогнали строку через газету: ', decoding)

# разделим на массив из слов в 3 символа


def razb(decoding):
    new_mas = []
    for i in range(0, len(decoding), 3):
        new_mas.append(decoding[i:i+3])
    return (new_mas)


print(razb(decoding))
