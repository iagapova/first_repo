import base64
# входные данные
username = 'David'
password = 'SlozhniyParol:)'

# объединение username и password и кодировка в base64
token = base64.b64encode(f'{username}:{password}'.encode())

print(f'Ваш токен: {token.decode()}')

# украли токен и проводим расшифровку токена
token = 'RGF2aWQ6U2xvemhuaXlQYXJvbDop'
decoded_token = base64.b64decode(token)

print(f'Расшифровка токена: {decoded_token.decode()}')
