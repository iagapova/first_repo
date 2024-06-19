def format_phone_number(func):
    def inner(phone):
        result = func(phone)
        if result.startswith('380'):
            result = '+' + result
        else:
            result = '+38' + result
        return result
    return inner


@format_phone_number
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
