import re

def is_spam_words(text, spam_words, space_around=False):
    flag = False
    # cleaned_text = text
    if space_around: # если флаг True то делаем чистый список слов без символов и пробелов
        print('а флаг ща у нас (пошли по if)', space_around)
        # symbols = [',', '.', '!', '?', '-']
        # for symbol in symbols:
        #     cleaned_text = cleaned_text.replace(symbol, '')
        # words = cleaned_text.split()
        words = re.findall(r'\w+', text) # то же самое что и предыдущий блок
        print(words)
        flag = any(word.lower() in spam_words for word in words)
    else: # если флаг True то делаем грубый список слов 
        print('а флаг ща у нас (пошли по else)', space_around)
        words = text
        flag = any(re.search(r'{}'.format(re.escape(word.lower())), words, re.IGNORECASE) for word in spam_words)
        #for string in words:
        #    for word in spam_words:
                # pattern = r'{}'.format(re.escape(word))
                # print('pattern= ', pattern)
        #        if re.search(word, string, re.IGNORECASE):
        #            flag = True
        #            break    
    #flag = any(word.lower() in spam_words for word in words) 
    return flag    
        


s = "Молох бог ужасен."
w = ["косел", "лох", "осел", "коза"]
print(is_spam_words(s, w, False))

#is_spam_words('Молох бог ужасен.', ['лох']) == True


