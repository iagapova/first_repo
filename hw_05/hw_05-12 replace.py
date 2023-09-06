import re

# сложнее код
def replace_spam_words(text, spam_words):
    # создаем функции замены на звездочки
    def replace_with(match):
        return '*' * len(match.group(0))
    
    # Создаем регулярное выражение, объединяя запрещенные слова через |
    pattern = '|'.join(map(re.escape, spam_words)) 
    #print('pattern = ', pattern)
    text = re.sub(pattern, replace_with, text, flags=re.IGNORECASE)
    return(text)

text = "МолоХ бог лОх ужасен."
spam_words = ["косел", "лох", "осел", "коза", "лох,"]

#        решение проще 
#for i in spam_words:
#    pattern = '(' + i + ')'
#    text = re.sub(pattern, i * len(i), text, flags=re.IGNORECASE)
print(replace_spam_words(text, spam_words)) 

# проще код
def replace_spam_words1(text, spam_words):
    for i in spam_words:
        pattern = '(' + i + ')'
        text = re.sub(pattern, '*' * len(i), text, flags=re.IGNORECASE)
    
    return(text)

print(replace_spam_words1(text, spam_words)) 