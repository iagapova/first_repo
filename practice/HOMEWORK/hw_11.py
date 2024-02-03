my_users = {'Alice': 'C00peR',
            'Bob': 'uNc1e',
            'Carl': 'ClariNet'}


class User:
    def __init__(self, login="Guest"):
        self.login = login

    def greet(self):
        print(f"Hi, my login is {self.login}")


class AuthenticatedUser(User):
    def __init__(self, login="Guest", password="password"):
        super().__init__(login)
        self.password = password

    def authenticate(self, user_password):
        return True if user_password == self.password else False


class AccessObject(AuthenticatedUser):
    def __init__(self, owner="", content=""):
        super().__init__(owner)
        self.content = content
        self.owner = owner

    def change_owner(self, old_owner_password="", new_owner=""):
        self.old_owner_password = old_owner_password
        if self.owner.authenticate(self.old_owner_password):
            self.new_owner = new_owner
            print(
                f"The ownership changing of {self.name} was successful! New owner is {new_owner.login}")
        else:
            print(
                f"Unauthorised attempt of {self.name} owner changing detected!")


if __name__ == '__main__':
    alice = AuthenticatedUser()
    alice.login = "Alice"
    bob = AuthenticatedUser()
    bob.login = "Bob"
    bob.password = "uNc1e"

    log = AccessObject()
    log.owner = alice
    log.name = "Computer logs"
    log.content = "There is no entries yet"

    security_policy = AccessObject()
    security_policy.owner = bob
    security_policy.name = "Enterprise security policy"
    security_policy.content = "Only authorized users may access objects"

    log.change_owner(bob.password, bob)
    security_policy.change_owner(bob.password, alice)


def get_pass():
    return input('Enter your password, please: ')


def check_password(password):
    user_name = 'Intruder'
    for k, v in my_users.items():
        if v == password:
            user_name = k
            break
    return user_name


def check_auth_code(expected_auth_code):
    return True if expected_auth_code == 1111 else False


def main_func(attempt=3):
    while attempt > 0:
        user_name = check_password(get_pass())
        if user_name in my_users:
            if check_auth_code(int(input('Enter authentication code, please: '))):
                print(f"Welcome, {user_name}! It's nice to see you again")
                break
            else:
                print("Sorry, I don't know you")
                break
        else:
            attempt -= 1
            print("Sorry, password is invalid. Try again!")
            if attempt != 0:
                print(f"{attempt} attemt(s) left")
            else:
                print("Sorry, I don't know you")
                break
#    return user_name


# main_func(3)
