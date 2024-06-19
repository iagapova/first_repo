def real_len(text):
    s = text.replace('\n', '').replace('\f', '').replace('\r', '').replace('\t', '').replace('\v', '')
    print(len(s))
    return(len(s))