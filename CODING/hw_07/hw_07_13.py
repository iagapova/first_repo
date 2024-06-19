def get_employees_by_profession(path, profession):
    my_list = []
    with open(path, 'r') as fh:
        lines = fh.readlines()
        for line in lines:
            # просматриваем каждую строку и есть ли в ней нужная профессия
            if line.find(profession + '\n') != -1:
                my_list.append(line)
        # собираем все в список
        result = ('').join(my_list)
        # возвращаем результат убирая профессию и переносы строк
        return result.replace(profession + '\n', '').rstrip()
