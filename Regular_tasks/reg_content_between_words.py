import re

text = """Да он олень, а не заяц! Жил был олень, козел, свинья, бегемот, слон и косой заяц. 
Олень как говорил Галыгин не Заяц) """


# def count_parts_between_two_words(text):
#     result = re.findall(r'\bолень.+?заяц\b', text, flags=re.IGNORECASE)
#     # print(result)
#     for item in result:
#         count_words = len(re.findall(r'\w+', item))
#         if count_words > 7:
#             result.remove(item)
#     return (result)
# print(count_parts_between_two_words(text))

def count_parts_between_two_words(text):
    # Используем re.finditer() с флагом re.IGNORECASE
    matches = re.findall(
        r'\bолень\W+(?:\w+\W+){0,5}заяц\b', text, flags=re.IGNORECASE)
    return matches


# Проходим по всем совпадениям и выводим их
for match in count_parts_between_two_words(text):
    print(match)
