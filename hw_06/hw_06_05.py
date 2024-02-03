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


def get_cats_info(path):
    my_list = []
    with open(path, 'r') as f:
        for line in f:
            l = line.strip().split(",")
            my_list.append({'id': l[0], 'name': l[1], 'age': l[2]})
    return (my_list)
# end of program for task!


content = ["60b90c1c13067a15887e1ae1,Tayson,3",
           "60b90c2413067a15887e1ae2,Vika,1",
           "60b90c2e13067a15887e1ae3,Barsik,2",
           "60b90c3b13067a15887e1ae4,Simon,12",
           "60b90c4613067a15887e1ae5,Tessi,5"]

write_employees_to_file(content, 'test.txt')

print(get_cats_info('test.txt'))

# with open('test.txt', 'r') as f:
#     print(f.read())


# удаляем файл
Path('test.txt').unlink()
