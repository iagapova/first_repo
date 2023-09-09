import re

text = r"""
Он --- серо-буро-малиновая редиска!! 
>>>:-> 
А не кот. 
www.kot.ru
""" 

print(len(re.findall(r'\b[a-zа-я-]+\b', text, flags=re.IGNORECASE)))
print(re.findall(r'\b[a-zа-я-]+\b', text, flags=re.IGNORECASE))
