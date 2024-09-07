import time
from functools import wraps

# если изовать его - теряются многе аттрибуты функции и перебивается враппером!


def wrong_timelogger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start}")
        return result
    return wrapper


def timelogger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start}")
        return result
    return wrapper


@timelogger
def long_loop(num: int):
    """
    Long loop function

    :param num:
    :return: None

    """
    while num > 0:
        num -= 1


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"decorator_1")
        return result
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"decorator_2")
        return result
    return wrapper


@decorator1
@decorator2
def baz(name):
    return f"Hello {name}"


if __name__ == '__main__':
    long_loop(100000)
    print(long_loop.__name__)
    print(long_loop.__doc__)
    print(long_loop.__annotations__)
    print()
    print(baz('Iryna'))
    print()
    print(baz.__wrapped__('Hanna'))
    print()
    print(baz.__wrapped__.__wrapped__('Klim'))
