from genericpath import exists, isdir
from pathlib import Path
import os
from sysconfig import get_path, get_path_names

# my_path = Path('/Users').joinpath('irina.agapova').joinpath(
#     'Desktop').joinpath('!!!HOMEWORK')
# print('---')
# print(my_path)
# if my_path.exists():
#     print('YES')
# else:
#     print('NO')

# def normalize(path):

text = """ЭЭЭвыо hijdsh iu sdjkh kj олырво kh23 jkdsh !@@ 3ор qwerty 4d """
my_dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
           'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': 'j', 'ы': 'i', 'ь': 'j', 'э': 'e', 'ю': 'yu', 'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'J', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': 'J', 'Ы': 'I', 'Ь': 'J', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'}
# l = {}
# for k, v in my_dict.items():
#     l[k.capitalize()] = v.capitalize()
# print(l)


def normalize(text):
    """Нормалізує им.я файлу"""
    pos = text.rfind('.')
    ext = text[pos:]
    name = text[:pos]
    for i in name:
        if i in my_dict.keys():
            # print(i, 'True', my_dict[i])
            name = name.replace(i, my_dict[i])
        elif not i.isalpha() and not i.isdigit():
            name = name.replace(i, '_')
    return name + ext


# print(normalize('ПривеТ!!! 88 Iryna 0306-(81).xlsx'))

my111 = Path('/Users').joinpath('irina.agapova').joinpath(
    'Downloads').joinpath('111')
# print(my111)
# print(isdir(my111))

# print(os.listdir(my111))


def walk(path, list_dir, new_list=[]):
    os.chdir(path)  # назначаем os локейшн для path
    # у path получаем список всех папок, сортируем
    list_dir = sorted(list(filter(os.path.isdir, os.listdir())))
    # получаем копию списка для верного удаления
    original_list = list(list_dir)
    for el in original_list:
        new_list.append(el)  # забираем элемент в наш список на вывод

        prev_el_path = Path(path).joinpath(el)  # пусть к элементу

        # -- case #1 --
        prev_el_dir = []
        # получаем список папок элемента
        [prev_el_dir.append(el) for el in sorted(
            list(Path(prev_el_path).iterdir())) if Path(el).is_dir()]

        # # -- case #2 --
        # os.chdir(Path(path).joinpath(el))
        # # получаем список всех папок для el, сортируем
        # prev_el_dir = sorted(
        #     list(filter(os.path.isdir, os.listdir(prev_el_path))))
        # os.chdir(path)

        # проверяем есть ли что-то в папке и погнали рекурсию
        if prev_el_dir != []:
            walk(Path(path).joinpath(el), prev_el_dir, new_list)

    return sorted(new_list)


print(walk(my111, []))
