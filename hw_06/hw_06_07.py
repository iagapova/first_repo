from pathlib import Path


def write_employees_to_file(content, path):
    fn = open(path, 'w')
    for i in content:
        if type(i) is list:
            for j in i:
                fn.write(j + "\n")
        else:
            fn.write(i + "\n")
    fn.close()
# program for task!


def sanitize_file(source, output):
    with open(source, 'r') as f1:
        text = f1.read()
        for i in '0123456789':
            text = text.replace(i, '')

    with open(output, 'w') as f2:
        f2.write(text)

# end of program for task!


content = ["60b90c1c13067a15887e1ae1,Tayson,3",
           "60b90c2413067a15887e1ae2,Vika,1",
           "60b90c2e13067a15887e1ae3,Barsik,2",
           "60b90c3b13067a15887e1ae4,Simon,12",
           "60b90c4613067a15887e1ae5,Tessi,5"]

write_employees_to_file(content, 'test1.txt')
write_employees_to_file(content, 'test2.txt')

# print(get_recipe('test.txt', "60b90c3b13067a15887e1ae4"))

sanitize_file('test1.txt', 'test2.txt')
with open('test2.txt', 'r') as f:
    print(f.read())


# удаляем файл
Path('test1.txt').unlink()
Path('test2.txt').unlink()
