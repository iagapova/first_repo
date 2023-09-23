def format_ingredients(items):
    if len(items) == 1:
        s = items[0]
    elif len(items) == 0:
        return ''
    else:
        s1 = ', '.join(items[:-2])
        s2 = ' and '.join(items[-2:])
        s = f"{s1}, {s2}"
    print(s)
    return s


format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"])
