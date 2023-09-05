import re
text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
word = "Python"

def find_word(text, word):
    res = re.search(word, text)
    if  res != None: # если нашлось слово
        dict = {'result': True, 
                'first_index': res.span()[0], # начало слова
                'last_index': res.span()[1], # конец слова
                'search_string': res.group(), # найденное слово
                'string': res.string} # фрагмент строки где найдено слово
    else: # если не нашли слово
        dict = {'result': False, 
                'first_index': None, 
                'last_index': None, 
                'search_string': word, 
                'string': text} 
    return dict

print(find_word(text, word))