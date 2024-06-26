class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __getitem__(self, key):
        if type(key) != int or key <= 0 or key >= len(self.marks):
            raise IndexError("Wrong index")
        return self.marks[key]

    def __setitem__(self, key, value):
        if type(key) == int and 0 <= key:
            if key > len(self.marks):
                off = key + 1 - len(self.marks)
                self.marks.extend([None]*off)

            self.marks[key] = value
        else:
            raise IndexError("Wrong index")

    def __delitem__(self, key):
        if type(key) != int:
            raise IndexError("Wrong index")
        del self.marks[key]


s1 = Student('Iryna', [5, 5, 3, 2, 5])
print(s1.marks[2])  # но хотим обращаться просто по индексу s1.[2]
print(s1[3])
s1[6] = 'abc'
print(s1.marks)
del s1[5]
print(s1.marks)
