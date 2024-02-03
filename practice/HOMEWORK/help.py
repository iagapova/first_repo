
users = {'Alice': 'C00per',
         'Bob': 'Unc1e',
         'Carl': 'ClariNet'}


def check_password():
    while True:
        count = 0
        count += 1
        login = input("Enter your login: ")
        password = input("Enter your password: ")
        if login in users and users[login] == password:
            print("hello!", login, "It is nice to see you!")
            break
        else:
            print("Try again!")
        if count > 3:
            break
    print("Sorry! I do not know you")


check_password()
