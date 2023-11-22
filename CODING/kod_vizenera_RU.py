RUA = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ENA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# message = "ПРИВЕТ, ИРА!"
# message = "ЗЦЪЗХКОВЁ"
message = "ЗЪСЪЁИЩЛЬПЪМГЁЬЛАСМИЛЖИЭЗЪДМГЙИБЪЁНДЛМЪЬЯКЗГМЯЬЛЯЛПЯЖХПКЪЗГЁГУЪГЛГЭЗЪЁГВРГГЬХЫКЪЗЗИЭИЫЪЗЕЪЕИЮНГЬИЯЪВЬЪЗГВЯЮИЖЪЛЛЯДОИЖВЪМЯЖЗЯЗГЯЙЯКЯБГЬЪШ"
message = """дпшфуяфзявкчычаажящь
бжуёйцтфубшщскяъофчщ
ьшдивсъоыаижзквьочщу
ёшсощсьощпйжфжкенётг
ишрфяцэулъздёухэетры
йбтёэнуфъсэафхсгуфвг
бзцкхэёиройякэнгффсй
эёоебачсхаижэшцяоещш
шекуъдвждыъууёзъъцла
ибхфюаяоытшьцёдсхфьщ
щбефгдёзмгэйффтккущх
зжйчьсткъыжвуёуарнрь
эгфуцз"""
shifr = 'ЧЧЕЕРРЕЕПП'


def correct_format(message):
    result = [i.upper() for i in message if i.isalpha()]
    en = ''.join(result)
    return en


en = correct_format(message)
# print(en)


def encoding(en):
    enc_message = ''
    for i in range(len(en)):
        # не шифрованная буква, ее позиция, соответствующая ей буква из шифра, соответствующая сдвижка
        # print(en[i], RUA.find(en[i])+1, (i) % len(shifr), RUA.find(shifr[(i) % len(shifr)])+1)

        # получаем код буквы в алфавите
        en_letter_pos = RUA.find(en[i])+1

        # получаем позицию буквы из шифра
        sh_letter_pos = RUA.find(shifr[(i) % len(shifr)])+1

        # получаем позицию зашифрованной буквы
        pos = (en_letter_pos + sh_letter_pos) % 33

        # print(en[i], pos)
        enc_message += RUA[pos-1]
    return enc_message


def decoding(en):
    dec_message = ''
    for i in range(len(en)):
        # не шифрованная буква, ее позиция, соответствующая ей буква из шифра, соответствующая сдвижка
        # print(en[i], RUA.find(en[i])+1, (i) % len(shifr), RUA.find(shifr[(i) % len(shifr)])+1)

        # получаем код буквы в алфавите
        en_letter_pos = RUA.find(en[i])+1

        # получаем позицию буквы из шифра
        sh_letter_pos = RUA.find(shifr[(i) % len(shifr)])+1

        # получаем позицию зашифрованной буквы
        pos = (en_letter_pos - sh_letter_pos) % 33

        # print(en[i], pos)
        dec_message += RUA[pos-1]
    return dec_message


print('кодируем: ', encoding(en))

print('раскодируем: ', decoding(en))
