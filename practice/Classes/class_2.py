class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, size):
        self.resolution = size

    def change_ext(self, ext):
        self.extension = ext

    def change_title(self, title):
        self.title = title
    # конвертируем класс в строку

    def __str__(self):
        return self.title.capitalize() + '.' + self.extension.upper()


first_foto = Image('800x600', 'first', 'JPG')
print(first_foto.__dict__)
second_foto = Image('300x100', 'second', 'PNG')
print('Resolution: ', second_foto.resolution)
print('Titile: ', second_foto.title)
print('Extension: ', second_foto.extension)
print()
first_foto.resize('1024x768')
print('We changed size: ', first_foto.__dict__)
first_foto.change_ext('gif')
print('We changed extension: ', first_foto.__dict__)
first_foto.change_title('initial')
print('We changed title: ', first_foto.__dict__)
print(first_foto)
print()
print(first_foto, 'has extension', first_foto.extension)
print(second_foto, 'has extension', second_foto.extension)
