from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    if len(password) != 8:
        return False
    
    has_upper = any(i.isupper() for i in password)
    has_lower = any(i.islower() for i in password)
    has_digit = any(i.isdigit() for i in password)
    
    return has_upper and has_lower and has_digit


def get_password(max_attempts=100):
    for _ in range(max_attempts):
        my_pass = get_random_password()
        if is_valid_password(my_pass):
            return my_pass
            break
    return "Could not generate a valid password."
