class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(cls, name, base, attrs)


class Point(metaclass=Meta):  # передает name = Point, base - список базовых классов, attrs - список аттрибутов (функция get_coords)
    def get_coords(self):
        return (0, 0)


pt = Point()
print(pt.MAX_COORD)
print(pt.get_coords())
