import re


text = """Вечер за окном. / Еще один день прожит. / Жизнь скоротечна..."""
text = """Просто текст"""
text = """Как вишня расцвела! / Она с коня согнала / И князя-гордеца."""
text = """На голой ветке / Ворон сидит одиноко… / Осенний вечер!"""
text = """Тихо, тихо ползи, / Улитка, по склону Фудзи, / Вверх, до самых высот!"""
text = """Жизнь скоротечна… / Думает ли об этом / Маленький мальчик."""


def count_slogs(text):
    mas_strok = re.split(r'/', text)  # разделили на строки
    result = []
    for i in mas_strok:
        # считаем количество гласных в каждой строке и добавляем в массив
        result.append(len(re.findall(r'[ауеоёиюяэ]', i, flags=re.IGNORECASE)))
    return result


result = count_slogs(text)
h_result = [5, 7, 5]
if len(result) != 3:
    print('Не хайку. Должно быть 3 строки.')
else:
    if result == h_result:
        print('Хайку!')
    else:
        for i in range(3):
            if result[i] != h_result[i]:
                print('Не хайку. В ', i+1,
                      ' строке слогов не ', h_result[i], ' а ', result[i], '.')
                break
