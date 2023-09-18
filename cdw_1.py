# исполняющий файл

import requests
from bs4 import BeautifulSoup
#
url = "https://www.codewars.com/users/EdSever"

headers = {
    'Accept': '*/*',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.734 Yowser/2.5 Safari/537.36"


}
req = requests.get(url, headers=headers)
src = req.text
# print(src)

with open("index.html", "w") as file:
    file.write(src)


with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "html.parser")

stat_elements = soup.find_all('div', class_='stat')

for element in stat_elements:
    # Проверяем, содержит ли элемент текст "Honor:"
    if 'Honor:' in element.text:
        # Извлекаем значение из элемента
        value = element.text.split(':')[-1].strip()
        print("Мой ранг на сайте codewars =", value)

