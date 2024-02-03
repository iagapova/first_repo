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


def add_employee_to_file(record, path):
    fh = open(path, 'a')
    fh.write(record + "\n")
    fh.close()

# end of program for task!


employee_list = [['Robert Stivenson,28',
                  'Alex Denver,30'], ['Drake Mikelsson,19']]

write_employees_to_file(employee_list, 'test.txt')

add_employee_to_file("Iryna Agapova,42", 'test.txt')

with open('test.txt', 'r') as f:
    print(f.read())


# удаляем файл
Path('test.txt').unlink()
