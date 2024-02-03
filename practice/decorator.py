def decorator_function(origin_fn):
    def wrapper(*args, **kwargs):
        # text before the origin function
        print("This is my text before the origin function")
        result = origin_fn(*args, **kwargs)
        # text after the origin function
        print("This is my text after the origin function")
        return result

    return wrapper


@decorator_function  # вызов декоратора
def my_func(a, b):
    print("It's my origin function")
    return ([a, b])


result = my_func(5, 3)
print(result)
