from genericpath import exists
from pathlib import Path


def save_credentials_users(path, users_info):
    with open(path, "wb") as fh:
        for k, v in users_info.items():
            item = (f'{k}:{v}\n').encode()
            fh.write(item)


path = Path.cwd().joinpath('test.bin')
# print(path)
# print(exists(path))
users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}

save_credentials_users(path, users_info)

Path('test.bin').unlink()
