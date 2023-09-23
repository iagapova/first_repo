import re

text = """Довольно распространённая ошибка ошибка — это лишний повтор  повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод."""


def repl(m):  # делаем функцию для проверки двойное ли слово m = match.group(0)
    words = m.group(0).split()
    return words[0] if words[0] == words[1] else m.group(0)

    # words = re.split(r' +', m[0])
    # if words[0] == words[1]:
    #     return words[0]
    # else:
    #     return m[0]


def replace(text):  # делаем функцию по отбору двух слов между которых пробел и меняем юзая функцию
    result = re.sub(r'\b(\w+)\s+\1\b', repl, text)
    return result


print(replace(text))
