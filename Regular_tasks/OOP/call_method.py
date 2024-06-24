class Counter:
    def __init__(self):
        self.counter = 0

    # def __call__(self, *args, **kwds):
    def __call__(self, step=1):
        # реагирует на круглые скобки, вызывает экземпляр класса как функцию
        print('__call__ вызван')
        self.counter += step
        return self.counter


c1 = Counter()
c2 = Counter()
print(c1.counter)
c1()
c1()
c1()
c2()
res1 = c1.counter
res2 = c2.counter
print(res1, res2)
