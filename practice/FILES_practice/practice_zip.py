from pathlib import Path
from zipfile import ZipFile

# Path('my_dir_to_zip').mkdir()  # создали директорию

# создаем файлы с контентом в папке
# with open('my_dir_to_zip/my_first_file.txt', 'w') as fh:
#     fh.write('Content of first file')
# with open('my_dir_to_zip/my_second_file.txt', 'w') as fh:
#     fh.write('Content of second file')

# with ZipFile('my_dir_to_zip.zip', mode='w') as my_zip_file:
#     for file in Path('my_dir_to_zip').iterdir():
#         print(file)
#         my_zip_file.write(file)

with ZipFile('my_dir_to_zip.zip', mode='r') as my_zip_file:
    my_zip_file.extractall('my-files-unzipped')
    my_zip_file.extract('my_dir_to_zip/my_first_file.txt', '!!!extracted_file')
