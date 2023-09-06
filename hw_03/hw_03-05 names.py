def get_fullname(first_name, last_name, middle_name =''):
    if middle_name != '':
        a = first_name + ' ' + middle_name + ' ' + last_name
    else: 
        a = first_name  + ' ' + last_name
    return a