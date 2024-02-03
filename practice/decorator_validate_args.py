def validate_args(fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(
                    f"Type of the '{arg}' is {type(arg)}. All argements must be 'int' or 'float'")
        return fn(*args, **kwargs)
    return wrapper


@validate_args
def sum(a, b):
    return a + b


try:
    print(sum(3, 2))
    print(sum(10.3, 4.7))
    print(sum(5, '4'))
    print(sum(5, b='2.0'))
except ValueError as e:
    print(e)
