import re

text = """12 мало 
лучше 123 
6000 почти 
090807 хорошо 
стало 989098 
супер 1234111
12345678904"""


# def insert_comma(m):
#     return ',' + m[0]


def convert_to_cor_format(text):
    # находим по три последние цифры в тексте
    pattern = r'(?<=\d)(\d{3})\b'

    # до тех пор пока находим - добавляем запятую перед тремя цифрами
    while re.findall(pattern, text) != []:
        # text = re.sub(pattern, insert_comma, text)
        text = re.sub(pattern, lambda m: ',' + m[0], text)
    return (text)


print(convert_to_cor_format(text))

# решение от чата GPT:
# import re

# text = """12 мало
# лучше 123
# 1234 почти
# 12354 хорошо
# стало 123456
# супер 1234567"""

# # Используем регулярное выражение для поиска больших целых чисел
# pattern = r'\b(\d+)\b'
# result = re.sub(pattern, lambda x: format(int(x.group(1)), ','), text)

# print(result)
