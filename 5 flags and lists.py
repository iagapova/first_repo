def is_spam_words(text, spam_words, space_around=False):
    cleaned_text = text
    if space_around: # если флаг True то делаем чистый список слов без символов и пробелов
        print('а флаг ща у нас (пошли по if)', space_around)
        symbols = [',', '.', '!', '?', '-']
        for symbol in symbols:
            cleaned_text = cleaned_text.replace(symbol, '')
        words = cleaned_text.split()
    else: # если флаг True то делаем грубый список слов 
        print('а флаг ща у нас (пошли по else)', space_around)
        words = [text]
    flag = any(word.lower() in spam_words for word in words) 
    return flag    
        


s = "Молох бог ужасен."
w = ["лох", "осел", "коза"]
print(is_spam_words(s, w))

#is_spam_words('Молох бог ужасен.', ['лох']) == True