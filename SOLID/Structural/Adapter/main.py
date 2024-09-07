from old_system import LegacySystem
# делаем адаптер, скармливаем туда старую систему и обертываем в адаптер


class NewSystem:
    def execute(self, operation, value1, value2):
        if operation == '+':
            return value1 + value2
        elif operation == '-':
            return value1 - value2
        else:
            raise ValueError("Unknown operation")


class AdapterSystem:  # адаптируем старую систему под новые реалии
    def __init__(self, system_: LegacySystem):
        self.system_ = system_

    def execute(self, operation, value1, value2):
        if operation == '+':
            return self.system_.execute(value1, value2, "add")
        elif operation == '-':
            return self.system_.execute(value1, value2, "sub")
        else:
            raise ValueError("Unknown operation")


if __name__ == '__main__':
    # legacy = NewSystem()
    # result = legacy.execute("+", 5, 5)
    # print(result)
    # result = legacy.execute("-", 5, 5)
    # print(result)
    legacy = AdapterSystem(LegacySystem())
    result = legacy.execute("+", 5, 5)
    print(result)
    result = legacy.execute("-", 5, 5)
    print(result)
