from genericpath import exists, isdir
from pathlib import Path
import os
import shutil
from sysconfig import get_path, get_path_names

my_dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
           'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': 'j', 'ы': 'i', 'ь': 'j', 'э': 'e', 'ю': 'yu', 'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'J', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': 'J', 'Ы': 'I', 'Ь': 'J', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'}


def normalize(path):
    """Нормалізує им'я файлу"""
    path = Path(path)
    name = path.stem
    for i in name:
        if i in my_dict.keys():
            name = name.replace(i, my_dict[i])
        elif not i.isalpha() and not i.isdigit():
            name = name.replace(i, '_')
    return Path(str(path.parent) + '/' + name + str(path.suffix))


def appendix(file):
    """функция добавляет аппендикс к имени"""
    return file.with_name(f"{file.stem}_copy").with_suffix(file.suffix)


def find_extensions(path):
    """Собираем набор уникальных экстеншинов из всех файлов папки"""
    os.chdir(path)
    all_ext = set()
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == '.DS_Store':
                os.remove(os.path.join(root, file))
            all_ext.add(Path(file).suffix)
    return all_ext


def handle_extensions(all_ext):
    """Разгребаем все экстеншины и сортируем по папкам"""
    other_ext = set()
    images = set()
    documents = set()
    video = set()
    audio = set()
    archives = set()
    fonts = set()
    for el in all_ext:
        # print(el)
        if el.lower() in ['.jpg', '.png', '.heic', '.svg', '.jpeg', '.gif', '.tiff']:
            images.add(el)
        elif el.lower() in ['.xlsx', '.xls', '.doc' '.ods', '.odt', '.rft', '.docx', '.txt', '.pdf', '.html', '.README', '.fb2', '.rtf', '.pptx', '.doc', '.ppt', '.xodt', '.xods', '.pages']:
            documents.add(el)
        elif el.lower() in ['.ttf']:
            fonts.add(el)
        elif el.lower() in ['.mov']:
            video.add(el)
        elif el.lower() in ['.mp3', '.wav', '.avi', '.mp4']:
            audio.add(el)
        elif el.lower() in ['.zip', '.dmg', '.msi', '.apk', '.pkg']:
            archives.add(el)
        else:
            other_ext.add(el)
    return [other_ext, images, documents, fonts, video, audio, archives]


def create_folders(new_path):
    # создаем новые папки
    if not new_path.exists():
        os.mkdir(new_path)
    os.chdir(new_path)
    if not new_path.joinpath('SORTED').exists():
        os.mkdir('SORTED')
    os.chdir(new_path.joinpath('SORTED'))
    my_folders = ['IMAGES', 'DOCUMENTS', 'AUDIO',
                  'FONTS', 'VIDEO', 'ARCHIVES', 'OTHERS']
    for el in my_folders:
        if not os.path.exists(el):
            os.mkdir(el)


def get_folder(ext):
    if ext in images:
        return 'IMAGES'
    elif ext in documents:
        return 'DOCUMENTS'
    elif ext in fonts:
        return 'FONTS'
    elif ext in video:
        return 'VIDEO'
    elif ext in audio:
        return 'AUDIO'
    elif ext in archives:
        return 'ARCHIVES'
    else:
        return 'OTHERS'


def poryadok(path, new_path):
    """получаем все файлы в path, юзаем функцию normalize и отправляем файлы по нужным папкам"""
    os.chdir(path)
    create_folders(new_path)
    new_path = new_path.joinpath('SORTED')
    new_file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == '.DS_Store':
                os.remove(os.path.join(root, file))
            new_file_list.append(os.path.join(root, file))
    # print(new_file_list)
    # проходим по каждому найденному файлу
    for el in new_file_list:
        new_file_name = normalize(el).name  # нормализуем имя
        # через экстеншн и функцию get_folder получаем нужную папку куда мувать
        new_file_path = new_path.joinpath(get_folder(Path(el).suffix))
        new_file = new_file_path / new_file_name

        # удаляем файл, но сначала проверяем есть ли такой уже
        if new_file.exists():
            # добавляем аппендикс к файлу
            shutil.move(el, appendix(new_file))
        else:
            shutil.move(el, new_file)

    # спрашиваем у юзера готов ли он распрощаться с уже пустым каталогом
    answer = input(
        """Кажется закончили, проверьте что папки пустые.\nГрохнем папку? - 'Yes/No': """)
    if answer == 'Yes':
        shutil.rmtree(path)


if __name__ == '__main__':
    my_folder_to_clean = Path('/Users/irina.agapova/Downloads/111')
    # my_folder_to_clean = Path('/Users/irina.agapova/Desktop/!!!HOMEWORK')

    if my_folder_to_clean.exists():

        xxx = Path('/Users').joinpath('irina.agapova').joinpath(
            'Downloads').joinpath('12345')

        all_ext = find_extensions(my_folder_to_clean)
        # print('Все экстеншины: ', all_ext)
        mas = handle_extensions(all_ext)

        new_all_ext = mas[0]
        images = mas[1]
        documents = mas[2]
        fonts = mas[3]
        video = mas[4]
        audio = mas[5]
        archives = mas[6]

        # print()
        # print('Images: ', images)
        # print('Documents: ', documents)
        # print('Video: ', video)
        # print('Audio: ', audio)
        # print('Archives: ', archives)

        print()
        poryadok(my_folder_to_clean, xxx)

        print()
        if new_all_ext == set():
            print('Все файлы разобраны')
        else:
            print("Неразобранные файлы с экстеншинами в папке 'OTHERS': ",
                  sorted(new_all_ext))
    else:
        print('Сорян! Такой папки не существует')
