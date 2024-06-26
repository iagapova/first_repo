# a = iter(range(5))
# print(next(a)) # 0
# print(next(a)) # 1
# print(next(a)) # 2
# print(next(a)) # 3
# print(next(a)) # 4
# print(next(a)) # 5
class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.fr)
        else:
            raise StopIteration


fr0 = FRange(0, 2, 0.5)
# print(next(fr0))  # ==  print(fr0.__next__())
# print(next(fr0))
# print(next(fr0))
# print(next(fr0))
print()

for i in iter(fr0):
    print(i)

# fr = FRange2D(0, 2, 0.5, 4)
# for row in fr:
#     for i in row:
#         print(i, end=" ")
#     print()
