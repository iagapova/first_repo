def print_if_num_is_even(num):
    """Prints and checks if number is odd or even

    Args:
        num (int): integer number

    Returns: 
        int: same number
    """
    if num % 2 == 0:
        print(num, 'Number is even')
    else:
        print(num, 'Number is odd')
    return num


def print_square(num):
    """Prints num * num result

    Args: num(int) - calculates num * num
    """
    print('Square is = ', num * num)


def process_number(number, callback_fn):
    """функция вызова другой функции"""
    callback_fn(number)


temp_num = int(input('Please provide any number: '))
process_number(temp_num, print_if_num_is_even)  # вызов функции коллбека
process_number(temp_num, print_square)  # вызов функции коллбека
print_if_num_is_even
