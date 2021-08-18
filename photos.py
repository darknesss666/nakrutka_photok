import vk_api
import time
import datetime
from vk_api import VkUpload

TOKEN = input('🔐Введи сюда токен: ')#тут нужно ввести обрезанный токен kate mobile.
vk_session = vk_api.VkApi(token = TOKEN, api_version = '5.135')
vk_session._auth_token()
upload = VkUpload(vk_session)

name_album = input('~Введи название альбома: ')
opisanie = input('~Введи описание альбома или напиши "пусто", чтобы не делать описание: ')

album = vk_session.method('photos.createAlbum', {'title': name_album, 'description': opisanie if opisanie != 'пусто' else None})
album_id = album['id']

print('~Айди созданного альбома равен', album_id)
photos = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg'] #это картинки, загрузи в папку со скриптом 5 картинок, которые и будут накручиваться, можно 5 разных, но красивее будет, если все будут одинаковыми

album_id = input('~Введи айди альбома: ')
while True:
    opis_one = input(f"~Введи первое описание фотографии: ")
    opis_two = input(f"~Введи второе описание фотографии: ")
    photo_list = upload.photo(photos, album_id = album_id, caption = opis_one + '\n' + opis_two)
    emit = time.strftime("[%d.%m.%Y|%H:%M:%S]", time.localtime())
    print(f"\033[33m{emit} Залил 5 фото")
    time.sleep(30)
print('\033[35m✅Накрутка завершена.')