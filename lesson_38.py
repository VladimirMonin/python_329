"""
Lesson 38
26.11.2023

Сериализация и десериализация
- JSON
"""

"""
Давай поговорим о сериализации и десериализации в Python. 
Это важные концепции, позволяющие трансформировать объекты Python в формат, 
который можно легко сохранять или передавать, и обратно.

Сериализация - процесс преобразования объекта Python в формат, поддерживаемый 
для хранения или передачи данных. Примерами форматов могут быть JSON, XML, 
бинарные файлы и др. Сериализованные данные легко сохранять в файл, отправлять 
через сеть или хранить в базе данных.

Десериализация - обратный процесс, преобразующий данные из формата 
хранения обратно в объекты Python.

Примеры использования:

Сохранение состояния программы: сохраняем объекты программы в файл, чтобы потом восстановить их состояние.
Передача данных: отправляем данные между разными системами или компонентами 
(например, между сервером и клиентом в веб-приложении).

https://search.wb.ru/exactmatch/ru/common/v4/search?TestGroup=no_test&TestID=no_test&appType=1&curr=rub&dest=-445278&query=%D0%91%D0%BB%D1%83%D0%B7%D0%BA%D0%B8%20%D0%B8%20%D1%80%D1%83%D0%B1%D0%B0%D1%88%D0%BA%D0%B8&resultset=catalog&sort=popular&spp=27&suppressSpellcheck=false
"""

# Читаем json ../data/wb_api.json и сохраняем в переменную
import json
from pprint import pprint

with open(r'D:\Syncthing\Работа\Academy_Top\ПРИМЕРЫ КОДА\python_329_code\data\wb_api.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Сохраняем в json indent=4 ascii=False
with open(r'D:\Syncthing\Работа\Academy_Top\ПРИМЕРЫ КОДА\python_329_code\data\wb_api.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)