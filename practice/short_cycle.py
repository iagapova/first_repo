my_dict = {'car': 'ford',
           'model': 'edge',
           'condition': 'fresh'}


new_dict = {k: v.upper() for k, v in my_dict.items()}

print(new_dict)

my_list = ['bb', 'Irina', 'agapova', 'text', 'MY', 'NaMe', 'a']
new_list = [item for item in my_list if len(item) > 3]

print(new_list)

# генератор
squares = (num * num for num in range(6))
for num in squares:
    print(num)
