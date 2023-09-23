import re


def replace_to_cube(text):
    def repl(m):
        return str(int(m[0])**3)
    text = re.sub(r'\d+', repl, text)
    return text


text = """Было закуплено 12 единиц техники 
по 410.37 рублей."""

print(replace_to_cube(text))
