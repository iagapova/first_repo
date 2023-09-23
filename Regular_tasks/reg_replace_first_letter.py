import re


def take_abbr_from_text(text):
    abbr = re.findall(r'\b\w', text)  # собираем первые буквы
    s = ''.join(i.capitalize() for i in abbr)  # собираем массив в слово
    return s


def take_abbr_from_text1(text):
    mas = re.split(r'\W+', text)  # разбиваем предложения на слова
    s = ''.join(i[0].capitalize()
                for i in mas)  # собираем первые буквы в слово
    return s


text = """Московский государственный, институт международных отношений"""
# text = """микоян авиацию снабдил алкоголем, народ доволен работой авиаконструктора"""
print(take_abbr_from_text(text))
print(take_abbr_from_text1(text))
