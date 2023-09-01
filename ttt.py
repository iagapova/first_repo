s = 'Python is the, most. powerful language'
print(s.lower())
if 'p' in s.lower():
    print('YEEES')
s1 = s
symbols = [',', '.', '!', '?', '-'] # удаляем символы из строки
for c in symbols:
    s1 = s1.replace(c, '')
s1 = s1.split()         # разделитель это пробел
print(s1)