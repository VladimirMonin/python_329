"""
Lesson 44
03.12.2023

Тема: Marshmallow
- Установка pip install marshmallow
- Импорт основных классов и инструментов
- Создание схемы для валидации данных
- Валидация данных, метод load
- Many=True
- ValidationError
- Marshmallow Dataclass
- Десериализация данных
- Создание схемы на основе датакласса (marshmallow_dataclass)
- Сериализация данных, метод dumps
- Десериализация данных, метод loads
-

"""

from marshmallow import Schema, fields, ValidationError
from marshmallow_dataclass import class_schema
from dataclasses import dataclass
from pprint import pprint
import json

from data.marvel import full_dict

"""
Практика десериализации данных!

Создайте датакласс для валидации данных о фильме на основе json файла.
Создайте схему на основе датакласса, используя библиотеку marshmallow_dataclass
Создайте объект схемы и валидируйте данные из json файла (many=True)
Получите на выходе список объектов датакласса
"""
"""
Пример json файла:
    [
    {
        "title": "Мстители: Секретные войны",
        "year": 2027,
        "director": "TBA",
        "screenwriter": "Майкл Уолдрон",
        "producer": "Нет данных",
        "stage": "Шестая фаза"
    },
    {
        "title": "Войны в доспехах",
        "year": "TBA",
        "director": "TBA",
        "screenwriter": "Яссер Лестер",
        "producer": "Кевин Файги и Джонатан Шварц",
        "stage": "Шестая фаза"
    },
    ]
"""


# Решение

@dataclass
class Film:
    title: str
    year: int
    director: str
    screenwriter: str
    producer: str
    stage: str


# Создайте схему на основе датакласса, используя библиотеку marshmallow_dataclass
film_schema = class_schema(Film)

# Читаем данные из файла
with open('../data/marvel.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Валидируем и десериализуем данные
# Сразу для всех объектов (ошибка - последние 2 объекта не валидируются)
# try:
#     films = film_schema(many=True).load(data)
# except ValidationError as e:
#     print(e)
#     exit(1)

# Пошагово для каждого объекта
films = []
for film in data:
    try:
        films.append(film_schema().load(film))
    except ValidationError as e:
        print(e)


# Получаем список объектов датакласса
pprint(films, indent=4)