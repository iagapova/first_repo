import re

text = """Иван Иванович! 
Нужен ответ на письмо от ivanoff@ivan-chai.ru. 
Не забудьте поставить в копию 
serge'o-lupin@mail.ru- это важно.
NO: foo.@ya.ru, foo@.ya.ru, foo@foo@foo
NO: +foo@ya.ru, foo@ya-ru
NO: foo@ya_ru, -foo@ya.ru-, foo@ya.ru+
NO: foo..foo@ya.ru 
YES: (boo1@ya.ru), boo2@ya.ru!, boo3@ya.ru"""


pattern = r'(?<=[ \n(])[a-z0-9\'_][a-z0-9-_+\']+[^\.\+\- ]@[a-z0-9]+[a-z0-9-]+\.[a-z0-9]+(?=[ ,.!\n)]?)'

matches = re.findall(pattern, text)

for match in matches:
    print(match)
