message1 = "ХРМЛЮЦЦЖТОПЙЖЦИМКПЙЮЯЩЗАПЙГВСЬЧЖУПМММЯЧГЛЖЭУНГОГУМВЖКЛЮЦЖТОАЖЕГЛГОЮИЙЬХГАМГПЙМАМЫРМПИОЩРЩЗПЖКАМЙПКГОРЖЛЮКМГЗЙЬЯЖКМЗИЮОРЖЛГБМЙЪЯГЗЛЮИМЛГФ"
message2 = "ЗЪСЪЕИ Щ ЛПЬЪМГЕ ЬЛА СМИ ЛЖИЭ ЗЪДМГ ЙИБЪЕНДЛМЪЬЯКЗГМЯЬЛЯЛПЯЖХПКЪЗГЕГУЪГЛГЭЗЪЕГВЪРГГЬХЫКЪЗЗИЭИЫЪЗЕЪЕИЮBMИЯХЪВЬЪЗГЯЮИЖЪЛЛЯДОИЖ ВЪМЯЖЗЯЗГЯ ЙЯКЯБГЬЪШ"

# НАДО ПЕРЕДЕЛАТЬ ПРОСТО ПОД СЛОВАРЬ БЕЗ Ё а не из кодировки!!!!

# print(ord("а"), ord("я"))
# print(ord("А"), ord("Я"))
# message = """дпшфуяфзявкчычаажящь
# бжуёйцтфубшщскяъофчщ
# ьшдивсъоыаижзквьочщу
# ёшсощсьощпйжфжкенётг
# ишрфяцэулъздёухэетры
# йбтёэнуфъсэафхсгуфвг
# бзцкхэёиройякэнгффсй
# эёоебачсхаижэшцяоещш
# шекуъдвждыъууёзъъцла
# ибхфюаяоытшьцёдсхфьщ
# щбефгдёзмгэйффтккущх
# зжйчьсткъыжвуёуарнрь
# эгфуцз"""


def cesar(message):
    encoded_message = ""
    for ch in message:
        if ch.isalpha() and ch.isupper():
            # print(ch, ord(ch.lower()))
            pos = ord(ch.lower()) - 1072
            pos = (pos + offset) % 32
            encoded_message += chr(pos + 1072).upper()
        elif ch.isalpha() and ch.lower():
            pos = ord(ch.lower()) - 1072
            pos = (pos + offset) % 32
            encoded_message += chr(pos + 1072)
        else:
            encoded_message += ch
    return encoded_message


offset = 2
print(cesar(message1))
print()
offset = 6
print(cesar(message2))

# перебор всех вариков!!!
# for offset in range(32):
#     print('ШАГ = ', offset)
#     print(cesar(message))
