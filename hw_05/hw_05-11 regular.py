import re

text = "I pythOn boug8ht 77 pYthoN pYthoN nu pYthoN, pythOn, PYTHOn 110 for pythOn 6$ and 110 bolts (220) for 3$."
word = 'pYthoN'

def find_all_words(text, word, flags = False):
    if flags == False:
        num = re.findall(word, text, re.IGNORECASE)
    else: 
        num = re.findall(word, text)
    return num # возвращаем список вхождений

print(find_all_words(text, word, True))


