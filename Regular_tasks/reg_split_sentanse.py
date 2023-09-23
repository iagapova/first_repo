import re

text = """В        этом 
предложении разрывы строки... Но это 
не так важно! Совсем? Да, совсем! И это 

не    должно мешать."""


def split_to_strings(text):

    result = re.findall(r"[А-ЯЁ][а-я ,\n]+[.!?;]+", text)
    # заменяем пробелы на один,       убираем \n символ
    return [re.sub(r' {2,}', ' ', item.replace('\n', '')) for item in result]


[print(i) for i in split_to_strings(text)]
