import re

text = """+7 123 456-78-90
8(123)456-78-90
1234567890
7(123) 456-78-90
+7(123 45678-90

123456789
+9 123 456-78-90
+7 123 456+78=90
8(123  456-78-90"""

result = re.split(r'\n', text)

pattern = r'(?:(?:\+?7|8) ?(?:\(?\d{3}\)?) ?(?:\d{3})(?:(?:-\d{2}){2}|\d{2}-\d{2})|\d{10})'
for item in result:
    if re.fullmatch(pattern, item):
        item = re.sub(r'[\s()+-]', '', item)  # Удаление пробелов и символов

        res = '+7 123 ' + item[:3] + '-' + item[3:5] + '-' + item[5:7]
        print(res)
    else:
        print('Fail!')
