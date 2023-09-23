import re

text = """1.23e5 
4.56e-3 
-2.34e10 
6.78e2 
9.87e-6 
3.0e8 
-1.234e-4 
2.22e12 
7.777e1 
-5.5e-2 
1.2
    1.0e-55  
         1e-12
  +4.1234567890E-99999           
 *******
 1. 
      e-12   
  6.5E 
  
  7.6e+12.5 
   99 """

pattern = r'[+-]?\d(?:(?:.\d+)?(?:[eE][+-]?\d+)|.\d+\b)'


def find_and_check_exp_numbers(text):
    # разбиваем на слова
    num = re.findall(r'.+[^\s]', text, flags=re.MULTILINE)
    # собираем паттерн

    return num


num = find_and_check_exp_numbers(text)
for item in num:
    if re.fullmatch(pattern, item.strip()):  # не забываем убрать пробелы!!!
        print(item.strip(), ' is legal.')
    else:
        print(item.strip(), ' is illegal.')
