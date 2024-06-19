from genericpath import exists
from pathlib import Path


def save_credentials_users(path, users_info):
    with open(path, "wb") as fh:
        for k, v in users_info.items():
            item = (f'{k}:{v}\n').encode()
            fh.write(item)


path = Path.cwd().joinpath('test.bin')
users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}
save_credentials_users(path, users_info)

# main function of task


def get_credentials_users(path):
    my_list = []
    with open(path, 'rb') as fh:
        #     print((fh.read().decode()).split('\n'))
        for items in fh.readlines():
            my_list.append(items.decode().replace('\n', ''))
    return my_list


print(get_credentials_users(path))
Path('test.bin').unlink()
