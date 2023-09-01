def is_check_name(fullname, first_name):
    Flag = False
    if len(fullname.removeprefix(first_name)) == (len(fullname) - len(first_name)):
        Flag = True
    print(Flag)
    return Flag
    
is_check_name('Taras Gogol', 'Taras')   