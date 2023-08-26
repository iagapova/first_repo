def is_valid_pin_codes(pin_codes):
    num = set('0123456789') # создаем сет
    flag = True
    if pin_codes == [] or len(pin_codes) != len(set(pin_codes)): 
        # сразу проверяем на пустой сет и на дубликаты пинов
        flag = False
        print('пусто или есть одинаковый пин')    
    else:
        for i in pin_codes:
            if len(i) != 4 or (set(i) | num) != num: 
                # проверяем что все пины длинной 4 и что обьединение двух сетов равно старому сету
                flag = False
                break
            
    print(flag)
    return flag

baza = ['1101', '9034', '0011']
is_valid_pin_codes(baza)