import re

text = """Уважаемые! 00:00Если вы к 09:00 не вернёте 05:30 15:17
чемодан, то уже в 09:00:01 я за себя не отвечаю.15:66 
PS. С отношением 25:50 всё нормально!"""

def find_all_time(text):
    
    result = re.sub(r"(?:([01]\d|2[0-4])(?::[0-5]\d){1,2})", '(TBD) ', text)
    return result
    

print(find_all_time(text))

    