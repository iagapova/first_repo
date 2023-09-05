articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon ocean Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]
letter_case = False
key = 'Ocean'
temp_dict = []
for i in articles_dict:
    for value in i.items():      
        if ((str(value).find(key) != -1 and letter_case == True) or (str(value).lower().find(key.lower()) != -1 and letter_case == False)):
            temp_dict.append(i)
            break
print(temp_dict)

def find_articles(key, letter_case=False):
    temp_dict = []
    for i in articles_dict:
    for value in i.items():      
        if ((str(value).find(key) != -1 and letter_case == True) or (str(value).lower().find(key.lower()) != -1 and letter_case == False)):
            temp_dict.append(i)
            break
    print(temp_dict)
    return(temp_dict)   
        
#find_articles('less')