import shutil
from pathlib import Path
# имя, расширение, какую папку (если не указано - то берет текущую)!
archive_name = shutil.make_archive(
    'hw_06/000/!!!zzz', 'zip', 'hw_06/my_dir_to_zip')

# основная часть программы


def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)


archive_path = 'hw_06/000/!!!zzz.zip'
path_to_unpack = Path.cwd().joinpath('hw_06/11111')

unpack(archive_path, path_to_unpack)

# зачистка
Path(archive_path).unlink()
Path('hw_06/11111/my_first_file.txt').unlink()
Path('hw_06/11111/my_second_file.txt').unlink()
Path('hw_06/11111').rmdir()
Path('hw_06/000').rmdir()
