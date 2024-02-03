class AccessLevel:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def __eq__(self, other):
        return self.level == other.level

    def __lt__(self, other):
        return self.level < other.level

    def __gt__(self, other):
        return self.level > other.level


class AccessObject:
    def __init__(self, name, content, access_level):
        self.name = name
        self.content = content
        self.access_level = access_level


class User():
    def __init__(self, login="Guest", mandatum=""):
        self.login = login
        self.__mandatum = mandatum

    def greet(self):
        print(f"Hi, my login is {self.login}")

    @property
    def mandatum(self):
        return self.__mandatum

    @mandatum.setter
    def mandatum(self, value):
        print('MI TYT BILI!')
        if value.isinstanse(AccessLevel):
            # if value.name and value.level:
            self.__mandatum = value
        else:
            print('OPPPPPPPPPPAAAAAAA!')

    def get_access(self, access_object):
        if (self.__mandatum == access_object.access_level) or (self.__mandatum > access_object.access_level):
            print(access_object.content)
        else:
            print(f"Access to {access_object.name} denied!")


if __name__ == '__main__':
    unclassified = AccessLevel("Unclassified", 1)
    secret = AccessLevel("Secret", 2)
    top_secret = AccessLevel("Top Secret", 3)

    # alice = User("Alice", top_secret)
    alice = User("Alice", "top_secret")
    bob = User("Bob", "unclassified")

    password_database = AccessObject(
        "Password Database",
        "Alice - C00peR, Bob - uNc1e",
        secret
    )

    alice.greet()
    alice.get_access(password_database)
    # print(alice._User__mandatum)

    bob.greet()
    bob.get_access(password_database)

    print('----')
    print()
