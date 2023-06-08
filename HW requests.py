# Кто самый умный супергерой

from pprint import pprint
import requests


url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)
super_heroes = []
for num, hero in enumerate(response.json()):
    if hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or hero['name'] == 'Thanos' :
        super_heroes.append([hero['name'], hero['powerstats']['intelligence']])
super_heroes.sort(key=lambda x: x[1], reverse=True)
print(f'Самый умный супергерой из списка - {super_heroes[0][0]}')

print('===============================================================================================================')

# Отправка файла в YD

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):

        """Метод загружает файлы по списку file_list на яндекс диск"""

        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        with open(file_path, encoding='utf-8') as file:
            name_file = file.name.split('/')[-1]
        params = {"path": name_file}
        headers = {"Accept": "application/json",
                   "Authorization": f"OAuth {self.token}"
                   }
        response = requests.get(url=url, params=params, headers=headers)
        href = response.json()['href']
        save_in_disk = requests.put(url=href, data=open("C:/Users/yumak/Desktop/Test.txt", "rb"))

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "C:/Users/yumak/Desktop/Test.txt"
    token = ''
    uploader = YaUploader(token)
    # response = requests.get(token)
    # print(uploader.__dict__)
    result = uploader.upload(path_to_file)