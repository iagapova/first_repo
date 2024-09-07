from dataclasses import dataclass


class Singleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


@dataclass
class Settings(metaclass=Singleton):
    db: str = "MySQL"
    port: int = 3306


class NewSettings(Settings):
    pass


if __name__ == '__main__':
    connect = Settings()
    print('connect:', connect)
    print('connect.port:', connect.port)
    connect_two = Settings()
    print('connect_two:', connect_two)
    print('connect_two.port:', connect_two.port)
    t = NewSettings()
    print()
    print('-- changing port to 5432 --')
    connect_two.port = 5432
    print('connect.port:', connect.port)
    print('connect_two.port:', connect_two.port)
    print()

    print('t.port', t.port)
    print('connect:', connect)
    print('connect_two:', connect_two)
    print('t:', t)
