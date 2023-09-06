def is_valid_password(password):
    if len(password) != 8:
        return False
    
    has_upper = any(i.isupper() for i in password)
    has_lower = any(i.islower() for i in password)
    has_digit = any(i.isdigit() for i in password)
    
    return has_upper and has_lower and has_digit

is_valid_password('shd7*jФh')
