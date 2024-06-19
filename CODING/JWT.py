# импорт библиотек
import jwt
import random
import string

# генерация секретного ключа из рандомных чисел и букв, длиной в 16 символов
secret_key = ''.join(random.choices(
    string.ascii_letters + string.digits, k=16))

# пример данных пользователя (payload)
payload = {'username': 'REST API', 'email': 'Best@Course.com'}

# генерация токена, с использование алгоритма шифрования HS256
token = jwt.encode(payload, secret_key, algorithm='HS256')

print(f'Ваш токен: {token}')
print(f'Ваш секретный ключ: {secret_key}')
