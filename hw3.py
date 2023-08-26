
def format_ingredients(items):
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        print(items[0])
        return items[0]
    else:
        s1 = items[:-2]
        s2 = items[-2:]
        if s1 != []:
            s2.insert(1, 'and')
            s = ', '.join(s1) + ', ' + ' '.join(s2)
            print(s)
            return s
        else:
            s2.insert(1, 'and')
            s = ' '.join(s2)
            print(s)
            return s
format_ingredients(["2 eggs"])


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
    
#format_ingredients(["2 eggs"])

format_ingredients(["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"])