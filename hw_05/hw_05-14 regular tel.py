import re


def find_all_phones(text):
    # берем \+, 380, скобку, две цифры, скобку, три цифры, \- (1 и 3 цифры или 2 и 2 цифры)) 
    result = re.findall(r"(\+380\(\d{2}\)\d{3}\-(?:\d{1}\-\d{3}|\d{2}\-\d{2}))", text)

    return result

text = '+380(67)757-1-333 +380(67)777-77-77 +380(99)922-06-07 380(67)922-06-07 +380(99)922-1-22'
text = 'Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'
print(find_all_phones(text))

import re


def find_all_phones(text):
    # берем \+, 380, скобку, две цифры, скобку, три цифры, \- 1-2 цифры, \-, 2-3 цифры  
    result = re.findall(r"(\+380\(\d{2}\)\d{3}\-\d{1,2}\-\d{2,3})", text)
    #[print(i[0:17]) for i in result if (len(i) >= 17)]
    result = [i[0:17] for i in result if (len(i) >= 17)]
    return result