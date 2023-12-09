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

marvel_films_json = """
[
    {
        "title": "The Avengers",
        "year": 2012
    },
    {
        "title": "Avengers: Age of Ultron",
        "year": 2015
    },
    {
        "title": "Человек-паук: Вдали от дома",
        "year": "2023"
    }
]
"""


# Опишем датакласс, на основе которого будет создана схема для валидации данных

@dataclass
class Film:
    title: str
    year: int

    def __str__(self):
        return f"{self.title} ({self.year})"

    def __repr__(self):
        return f"{self.title} ({self.year})"


# pip install marshmallow_dataclass
# Создадим схему для валидации данных на основе датакласса Film

FilmSchema = class_schema(Film)

# Делаем валидацию и десериализацию данных - на выходе получаем объекты Film
# Используем many=True, так как валидируем список словарей

try:
    films = FilmSchema(many=True).loads(marvel_films_json)


except ValidationError as err:
    print(err.messages)

# Проверяем тип данных в списке - это объекты Film
# [print(type(film)) for film in films]

# Делаем обратное преобразование - сериализацию данных в JSON строку и выводим на печать
films_list = FilmSchema(many=True)
films_json = films_list.dumps(films)
pprint(films_list)
print(type(films_json))
print(films_json)

# Делаем из full_dict список словарей и сохраняем в JSON файл
result = []

for film in full_dict.values():
    result.append(film)

print(result)

with open("../data/marvel.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)
