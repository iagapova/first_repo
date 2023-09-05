def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    UA = []
    JP = []
    TW = []
    SG = []
    for i in list_phones:
        i = sanitize_phone_number(i)
        if i.removeprefix("3").startswith('80'):
            UA.append(i)
        elif i.removeprefix("3").startswith('81'):
            JP.append(i)
        elif i.removeprefix("3").startswith('886'):
            TW.append(i)
        elif i.removeprefix("3").startswith('65'):
            SG.append(i)
        else:
            UA.append(i)
    result = { 
        "UA": UA,
        "JP": JP, 
        "TW": TW,
        "SG": SG
    }
    return result

list = ["    +38(050)123-32-34",
    "     +810503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ", "+3657658976"]  
#print(list)

result = get_phone_numbers_for_countries(list)
print(result)