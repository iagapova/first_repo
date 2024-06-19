from pathlib import Path


def write_employees_to_file(employee_list, path):
    fn = open(path, 'w')
    for i in employee_list:
        if type(i) is list:
            for j in i:
                fn.write(j + "\n")
        else:
            fn.write(i + "\n")
    fn.close()
# program for task!


def read_employees_from_file(path):
    my_list = []
    fn = open(path, 'r')
    for line in fn:
        my_list.append(line.strip())
    fn.close()
    return my_list

# end of program for task!


employee_list = [['Robert Stivenson,28',
                  'Alex Denver,30'], ['Drake Mikelsson,19']]

write_employees_to_file(employee_list, 'test.txt')

print(read_employees_from_file('test.txt'))
# удаляем файл
Path('test.txt').unlink()
