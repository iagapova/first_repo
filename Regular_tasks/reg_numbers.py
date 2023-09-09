import re

text = r"""
С227НА777 
КУ22777 
Т22В7477 
М227К19У9 
 С227НА771 
""" 
private_pattern = r'[(А,В,Е,К,М,Н,О,Р,С,Т,У,Х]{1}\d{3}[А,В,Е,К,М,Н,О,Р,С,Т,У,Х]{2}\d{2,3}'
taxi_pattern = r'[А,В,Е,К,М,Н,О,Р,С,Т,У,Х]{2}\d{5,6}'

num = re.findall(r'.+[^\s]', text, flags=re.MULTILINE)
print(num)
for item in num:
    if re.fullmatch(private_pattern, item):
        print(item, ' Private')
    elif re.fullmatch(taxi_pattern, item):
        print(item, ' Taxi')
    else:
        print(item, ' Fail')
