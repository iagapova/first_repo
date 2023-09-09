import re

# Найдите все натуральные числа (возможно, окружённые буквами);
text1 = 'The price of the 11product is $25. The temp55erature is 25°C. There are 1001 reasons to smile, but -15°C is too cold.'
result1 = re.findall(r"[1-9]\d*", text1)
#print(result1)


# !!! Найдите все «слова», написанные капсом (то есть строго заглавными), возможно внутри настоящих слов (аааБББввв);
text2 = 'This is a SAMPLE Text and aBBBcccDDDeee ПППриВВеТ is WRITTEN in CAPS.'
result2 = re.findall(r"[A-ZА-Я]+", text2)
#print(result2)


# Найдите слова, в которых есть русская буква, а когда-нибудь за ней цифра;
text3 = 'На 22 эта6же нашего до5ма живут 5 семьи, а у каждой из них по 3 детей.'
result3 = re.findall(r"([а-яА-Я]+\d[а-яА-Я\d]+)", text3)
#print(result3)


# !!! Найдите все слова, начинающиеся с русской или латинской большой буквы (\b — граница слова);
text4 = 'На 22 Эта6же Uашего до5ма Живут 5 Sемьи, аD у кажЖдой из них по 3 ДЕтей.'
result4 = re.findall(r"\b[А-ЯЁA-Z]+\w+", text4)
#print(result4)


# !!! Найдите слова, которые начинаются на гласную (\b — граница слова);;
text5 = 'На 22 Эта6же Uашего до5ма Живут 5 Sемьи, аD у кажЖдой из них по 3 ДЕтей.'
result5 = re.findall(r"\b[аоуэиеёю]\w*", text5, flags = re.IGNORECASE)
#print(result5)


# Найдите все натуральные числа, не находящиеся внутри или на границе слова;
text6 = 'The price of the22 11product is $25. The tempe55rature is 25°C. There are 1001 reasons to smile, but -15°C is too cold.'
result6 = re.findall(r"\b[1-9]\d*\b", text6)
#print(result6)


# !!! Найдите строчки, в которых есть символ * (. — это точно не конец строки!);
text7 = """The* price 
*of the22* 
11product is
fd**$25
"""
result7 = re.findall(r".*\*.*", text7)
#print(result7)


# !!! Найдите строчки, в которых есть открывающая и когда-нибудь потом закрывающая скобки;
text8 = """(The* pr)ice) 
*of t(he22* 
11produ)dfjh(ct is
f(d**$2)5
"""
result8 = re.findall(r".*\(.*\).*", text8)
#print(result8)


# !!!Выделите одним махом весь кусок оглавления (в конце примера, вместе с тегами);
text9 = """QwertyЙцукен

+-,/[](), *** (***), a*(b+[c+d])*e/f+g-h

!!$$$$$%%%%%&&&'''(((())***++++,,,,,-----..//:::;;;;<<<<<===>>>????

@@@@@[[[[\\\]]]]]^^^__`````{{{{|||||}}}}}~~~~~
<a href="*#10">10: CamelCase -> under_score</a>;
<a href="#11">11: Удаление повторов</a>;
<a href="#12*">12: Близкие слова</a>;
**<a href="#13">13: Форматирование больших чисел</a>;
<a href="#14">14: Разделить текст на предложения</a>;
<a href="#15">15: Форматирование номера телефона</a>;
<a href="#16">16: Поиск e-mail'ов — 2</a>;"""
result9 = re.findall(r"<.*?>;", text9)
#for match in matches:
    #print(match)

    
# !!!Выделите одним махом только текстовую часть оглавления, без тегов;
text10 = """ <a href="*#10">10: CamelCase -> under_score</a>;
<a href="#11">11: Удаление повторов</a>;
<a href="#12*">12: Близкие слова</a>;
**<a href="#13">13: Форматирование больших чисел</a>;
<a href="#14">14: Разделить текст на предложения</a>;
<a href="#15">15: Форматирование номера телефона</a>;
<a href="#16">16: Поиск e-mail'ов — 2</a>;"""

pattern = r'<a href=".*?"(.*?)<\/a>;'
matches10 = re.findall(pattern, text10)

#for match in matches10:
    #if match.strip():  # Исключить пустые строки
        print(match.strip())
 
        
# !!! Найдите пустые строчки;

text11 = """Регулярные

выражения представляют собой похожий
fffdffd

инструмент"""
result11 = re.findall(r"\n\s*\n", text)
result11 = len(result11)
#print(result11)


