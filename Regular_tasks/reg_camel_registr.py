import re


text = """MyVar17 = OtherVar + YetAnother2Var 
TheAnswerToLifeTheUniverseAndEverything = 42"""


def lowering(m):
    return '_' + m[0].lower()


def convert_to_var(text):
    result = re.sub(r'(?<=[a-z0-9])[A-Z]', lowering, text)
    return result.lower()


print(convert_to_var(text))
