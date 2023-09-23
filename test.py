import re

text = 'Это был тяжелый 2022 год'
match = re.search(r'\d+', text)
print(match[0])
print(match.start())
print(match.end())


def repl(m):
    return '>censored(' + str(len(m[0])) + ')<'


text = "Некоторые хорошие слова подозрительны: хор, хоровод, хороводоводовед."
print(re.sub(r'\b[хХxX]\w*', repl, text))
