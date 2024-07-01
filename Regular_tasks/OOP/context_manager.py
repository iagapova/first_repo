class DefenedVector:  # кастомный класс менеджера контекста
    def __init__(self, v):
        self.__v = v

    def __enter__(self):  # делаем копию вектора
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):  # ловим ошибки
        if exc_type is None:  # если ошибок нет - переопределяем вектор
            self.__v[:] = self.__temp

        return False  # если False то исключения в менеджере контекста обрабатываться не будут


v1 = [1, 2, 3]
v2 = [-1, -2]

try:
    with DefenedVector(v1) as dv:
        for i, k in enumerate(dv):
            dv[i] += v2[i]
except Exception:
    print("Ошибка")

print(v1)
print()
v2 = [-1, -2, - 3]
try:
    with DefenedVector(v1) as dv:
        for i, k in enumerate(dv):
            dv[i] += v2[i]
except Exception:
    print("Ошибка")
print(v1)
