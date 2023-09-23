import re
# code invalid

text = r"""
Иван Иванович! 
Нужен ответ на письмо от ivanoff@ivan-cha+i.ru. 
Не забудьте поставить в копию 
serge'o-lupin@mail.ru- это важно.
NO: foo.@ya.ru, foo@.ya.ru 
PARTLY: booooo@ya_ru, -boo@ya.ru-, foo№boo@ya.ru
Иван Иванович! 
"""

list = re.findall(
    r'\b[\w_\']+[\w.+-_\']*[\w_\']+@[a-z0-9]+[a-z0-9+-]*[a-z0-9+-.]*[a-z0-9]+', text, flags=re.IGNORECASE)
for item in list:
    print(item)
