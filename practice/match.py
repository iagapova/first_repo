temp = input('Please provide a number: ')

match temp:
    case "404":
        print('Server is not available')
    case "200":
        print('Successful')
    case _:
        print('I have no answer')
