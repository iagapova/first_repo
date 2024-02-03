from pathlib import Path


def total_salary(path):
    total = 0
    fh = open(path, 'r')
    while True:
        line = fh.readline()
        if not line:
            break
        position = line.find(',')
        total += float(line[position+1:])
    fh.close()
    return total


# создаем файл с контентом
with open('test.txt', 'w') as f:
    f.write("Alex Korp,3000\n")
    f.write("Nikita Borisenko,2000\n")
    f.write("Sitarama Raju,1000\n")

print(total_salary('test.txt'))


# удаляем файл!
# Path('test.txt').unlink()
