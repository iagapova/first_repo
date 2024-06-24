class ReadIntX:
    # NON-DATA DESCRIPTOR
    # owner - ссылка на экземпляр класса Point3D, name - x, y или z
    def __set_name__(self, owner, name):
        self.name = "_x"

    # owner - ссылка на экземпляр класса Point3D, instance - ссылка на экземпляр класса integer
    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer:
    # DATA DESCRIPTOR
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Значение координаты должно быть целым числом")

    # owner - ссылка на экземпляр класса Point3D, name - x, y или z
    def __set_name__(self, owner, name):
        self.name = "_" + name

    # owner - ссылка на экземпляр класса Point3D, instance - ссылка на экземпляр класса integer
    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):  # instance - ссылка на экземпляр класса integer
        self.verify_coord(value)
        print(f"__set__: {self.name} = {value}")
        # формируем локальное свойство и его значение
        setattr(instance, self.name, value)


class Point3D:
    # формируем дескрипторы
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
print(p.__dict__, p.xr)  # тут xr это значение _x
# p.z = 'ddd'
p.z = -1
# создаем аттрибут xr поскольку он имеет такой же приоритет как и _x (!такое работает для нон дата дескрипторов)
p.xr = 100
print(p.__dict__, p.xr)
