import shutil
from pathlib import Path
# имя, расширение, какую папку (если не указано - то берет текущую)!
archive_name = shutil.make_archive('!!!zzz', 'zip', 'hw_06/my_dir_to_zip')

# распаковываем: имя архива и куда
shutil.unpack_archive('!!!zzz.zip', 'hw_06/11111')


for shortcut, description in shutil.get_archive_formats():
    print('{:<10} | {:<10}'.format(shortcut, description))

Path('!!!zzz.zip').unlink()
Path('hw_06/11111/my_first_file.txt').unlink()
Path('hw_06/11111/my_second_file.txt').unlink()
Path('hw_06/11111').rmdir()
