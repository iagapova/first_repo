import requests
import os

# Ваш токен доступа
access_token = "vk1.a.IWuQWBjaye3U3kJvs4b2XcRVTBBXK-R5GOgSdAFE1Qad6kDvcto31-qACsMt0skvdxzKhMA07VKElk5aMB1fCs9ZXdKKClTEdY_CAxm4rzZmzimTuVLhV1QpLFYugnmw2xfMaDdJCl65wSh-8fgUwkH9NzFwfyrB6lhBKX83-YwBqc2dYZ6J5RJYVA-di73U"

# ID пользователя (ваш ID)
user_id = "rY4Ousr7xtKugJIzpU2I"

# API метод для получения фотографий
photo_api_url = f"https://api.vk.com/method/photos.get?owner_id=rY4Ousr7xtKugJIzpU2I&album_id=profile&access_token=vk1.a.IWuQWBjaye3U3kJvs4b2XcRVTBBXK-R5GOgSdAFE1Qad6kDvcto31-qACsMt0skvdxzKhMA07VKElk5aMB1fCs9ZXdKKClTEdY_CAxm4rzZmzimTuVLhV1QpLFYugnmw2xfMaDdJCl65wSh-8fgUwkH9NzFwfyrB6lhBKX83-YwBqc2dYZ6J5RJYVA-di73U&v=5.131"

response = requests.get(photo_api_url)
data = response.json()

if "response" in data:
    photos = data["response"]["items"]
    
    for photo in photos:
        photo_url = photo["sizes"][-1]["url"]
        photo_id = photo["id"]
        file_extension = os.path.splitext(photo_url)[1]
        
        # Загрузка фото
        response = requests.get(photo_url)
        with open(f"{photo_id}{file_extension}", "wb") as file:
            file.write(response.content)
        
    print("Фотографии успешно скачаны.")
else:
    print("Ошибка при получении данных.")
