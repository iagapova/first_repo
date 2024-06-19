def token_parser(s):
    new_list = []
    if s == '':
        return new_list
    else:
        s = s.replace(' ', '')
        item = ''
        for i in s:
            if i in ['*', '/', '+', '-', ')', '(']:
                if item != '':
                    new_list.append(item)
                new_list.append(i)
                item = ''
            else:
                item += i
        new_list.append(item)
        return new_list
