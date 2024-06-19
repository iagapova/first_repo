from pathlib import Path


def write_employees_to_file(content, path):
    fn = open(path, 'w')
    fn.write(str(content))
    fn.close()
# program for task!


def save_applicant_data(source, output):
    i = []
    for item in source:
        i.append(
            f"{item['name']},{item['specialty']},{item['math']},{item['lang']},{item['eng']}\n")
    with open(output, "w") as fh:
        fh.writelines(i)


# end of program for task!
vedomost = [
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


save_applicant_data(vedomost, 'test.txt')

# with open('test.txt', 'r') as fh:
#     print(fh.read())
#     print('---')

# удаляем файл
Path('test.txt').unlink()
