# ena = (chr(i) for i in range(ord('a'), ord('z') + 1)) - массив
ena = 'abcdefghijklmnopqrstuvwxyz'
ENA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rua = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
RUA = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
RUA1 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

message = "ХРМ ЛЮЦ ЦЖТО ПЙЖЦИМК ПЙЮЯЩЗ А ПЙГВСЬЧЖУ ПМММЯЧГЛЖЭУ НГОГУМВЖК ЛЮ ЦЖТО АЖЕГЛГОЮ ИЙЬХГАМГ ПЙМАМ ЫРМ ПИОЩРЩЗ ПЖКАМЙ ПКГОРЖ ЛЮ КМГЗ ЙЬЯЖКМЗ ИЮОРЖЛГ БМЙЪЯГЗЛЮ ИМЛГФ"
message2 = "ЗЪСЪЁИ Щ ЛПЬЪМГЁ ЬЛА СМИ ЛЖИЭ ЗЪДМГ ЙИБЪЁНДЛМЪ ЬЯКЗГМЯ ЬЛЯ ЛПЯЖХ ПКЪЗГЁГУЪ Г ЛГЭЗЪЁГВЪРГГ ЬХЫКЪЗЗИЭИ ЫЪЗЕЪ ЕИЮИЬИЯ ЗЪВЬЪЗГЯ ЮИЖЪ Л ЛЯДОИЖ ВЪМЯЖЗЯЗГЯ ЙЯКЯБГЬЪШ"


def shifr(text, step, RUA, set):
    string = ''
    for i in text:
        if i in RUA:
            string += RUA[(RUA.find(i) + step) % set]
        else:
            string += i
    return string


print(shifr(message.upper(), 2, RUA, 32))
print()
print(shifr(message2.upper(), 6, RUA1, 33))
