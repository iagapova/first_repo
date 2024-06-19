from pathlib import Path


def encrypt(b_obj, key):
    b_obj_array = bytearray(b_obj)

    for i, b in enumerate(b_obj_array):
        # print(i, b)
        n = b + key
        if n > 255:
            n -= 255

        b_obj_array[i] = n
    return b_obj_array


def decrypt(b_obj, key):
    b_obj_array = bytearray(b_obj)

    for i, b in enumerate(b_obj_array):
        # rint(i, b)
        n = b - key
        if n < 255:
            n += 255

        b_obj_array[i] = n
    return bytes(b_obj_array)


if __name__ == '__main__':
    pwd = input('Enter your password: ')
    pwd_bytes = pwd.encode()
    encrypted_pwd = encrypt(pwd_bytes, 200)

    with open('password.txt', 'wb') as file:
        file.write(encrypted_pwd)
    with open('password.txt', 'rb') as file:
        encrypted_pwd = file.read()
        print(encrypted_pwd)

    print(decrypt(encrypted_pwd, 200))

    Path('password.txt').unlink()
