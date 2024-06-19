from pathlib import Path


def write_employees_to_file(content, path):
    fn = open(path, 'w')
    fn.write(str(content))
    fn.close()
# program for task!


def save_applicant_data(source, output):
    with open(source, 'r') as f1:
        my_list = []
        text = f1.read().replace('[', '').replace(']', '')
        while text:
            start = text.find("{")
            stop = text.find("}")
            item = text[start: stop+1]
            my_list.append(eval(item))
            text = text[stop+1:]

        # new_list = []
        # for item in my_list:
        #     i = ''
        #     for v in item.values():
        #         i = i + str(v) + ','
        #     new_list.append(i[:-1])

        new_list = [','.join(str(v) for v in item.values())
                    for item in my_list]

    with open(output, 'w') as f2:
        f2.writelines(item + "\n" for item in new_list)


# end of program for task!

ved = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

write_employees_to_file(ved, 'test1.txt')
# write_employees_to_file(content, 'test2.txt')

# print(get_recipe('test.txt', "60b90c3b13067a15887e1ae4"))

# with open('test1.txt', 'r') as f1:
#     print(f1.read())
# print('-----------')

# with open('test1.txt', 'r') as f1:
#     my_list = []
#     text = f1.read().replace('[', '').replace(']', '')
#     while text:
#         start = text.find("{")
#         stop = text.find("}")
#         item = text[start: stop+1]
#         my_list.append(eval(item))
#         text = text[stop+1:]

# print(' ++++ ')
# print(my_list)

# new_list = []
# for item in my_list:
#     i = ''
#     for k, v in item.items():
#         i = i + str(v) + ','
#     new_list.append(i[:-1])

# with open('test2.txt', 'w') as f2:
#     for item in new_list:
#         f2.writelines(item + "\n")

save_applicant_data('test1.txt', 'test2.txt')


# удаляем файл
Path('test1.txt').unlink()
Path('test2.txt').unlink()
