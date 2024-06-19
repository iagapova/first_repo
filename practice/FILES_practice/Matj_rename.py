from datetime import datetime
from pathlib import Path
import os


def change_format(file_name, file_suffix):
    if file_name.startswith('GMT'):
        # урезаем дату
        sdate = file_name[3:file_name.find('-')]
        # добавляем тире
        new_date = sdate[0:4] + '-' + sdate[4:6] + '-' + sdate[6:]
        # перегоняем строку в формат datetime
        date_format = "%Y-%m-%d"
        date_obj = datetime.strptime(new_date, date_format)
        # перегоняем строку в формат datetime
        new_format = "%Y-%B-%d"
        # Форматируем объект datetime в нужный формат
        new_date_str = date_obj.strftime(new_format)
        if file_name.endswith('_640x360'):
            formatted_name = new_date_str + '___Natalia'
        elif file_suffix == 'vtt':
            formatted_name = new_date_str + '___Natalia(Transcript)'
        else:
            formatted_name = new_date_str + '___Natalia(Voice)'

        return formatted_name + file_suffix
    else:
        return file_name + file_suffix


def rename_file(folder_to_rename):
    for item in os.listdir(folder_to_rename):
        fulpath = Path(folder_to_rename / item)
        if item == '.DS_Store':
            os.remove(folder_to_rename / '.DS_Store')
            print('REMOVED')
        elif fulpath.is_dir():
            print('SKIP FOLDER')
            pass
        else:
            os.rename(folder_to_rename / item,
                      folder_to_rename / change_format(fulpath.stem, fulpath.suffix))


if __name__ == '__main__':
    source_file = Path('/Users/irina.agapova/Downloads/conv')
    rename_file(source_file)
