from copy import copy


class Users:
    def __init__(self):
        self.user_list = []

    def add_user(self, user):
        self.user_list.append(user)

    # def __copy__(self):
    #     print('COPY method is used')
    #     copied_users = Users()
    #     copied_users.user_list = self.user_list
    #     return copied_users

    def __copy__(self):
        print('DEEPCOPY method is used')
        deepcopied_users = Users()
        deepcopied_users.user_list = [copy(user) for user in self.user_list]
        return deepcopied_users


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __copy__(self):
        copied_user = User(self.name, self.age)
        return copied_user


user_1 = User('John', 19)
user_2 = User('Jack', 20)
list_1 = Users()
list_1.add_user(user_1)
list_1.add_user(user_2)

print()
print('list_1:', id(list_1), list_1.user_list)
copied_list_1 = copy(list_1)
print('copied_list_1:', id(copied_list_1), copied_list_1.user_list)
print()
print('user_1:', id(user_1), user_1)
copied_user_1 = copy(user_1)
print('copied_user_1:', id(copied_user_1), copied_user_1)
print()
