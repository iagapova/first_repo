import re

# Исходная строка
text = "Молох бог ужасен лох. Лохнесс, козел, баран."

# Используем регулярное выражение для поиска всех чисел в тексте
#numbers = re.findall(r'\d+', text)

numbers = re.findall(r'\d+', text)
words = re.findall(r'\w+', text) 
special_characters = re.findall(r'\W+', text)

print(numbers)
print(words)
print(special_characters)