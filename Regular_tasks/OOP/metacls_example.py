class Meta(type):
    def create_local_attrs(self, *args, **kwargs):  # инициализатор для класса Women
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs
        # инициализатор для класса Women, create_local_attrs - ссылка на функцию
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    title = 'заголовок'
    content = 'контент'
    photo = 'путь к фото'


w = Women()
print(w.__dict__)
