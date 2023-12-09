"""
Lesson 44
03.12.2023

Тема: Marshmallow
- Установка pip install marshmallow
- Импорт основных классов и инструментов

"""

from marshmallow import Schema, fields, ValidationError
from dataclasses import dataclass
from pprint import pprint

from data.marvel import small_dict

"""
Основные классы и инструменты:
- Schema - базовый класс для создания схемы
- fields - классы для создания полей
- ValidationError - класс для обработки ошибок валидации

Schema - Наследуемся от этого класса для создания "схемы" для валидации данных.
fields - Классы для создания полей. Все они наследуются от класса Field.
В них есть параметры, которые позволяют задавать правила валидации, а так же инструменты, как нарприер, метод validate.
"""

# Опишем схему для валидации данных для проверки ключей и значений словаря.

marvel_films = [
    {
        "title": "The Avengers",
        "year": 2012
    },
    {
        "title": "Avengers: Age of Ultron",
        "year": 2015,
    },
    {
        "title": 13,
        "year": "Avengers"
    },
]

# Создадим класс схемы для валидации данных. Наследуемся от класса Schema.
# В нем описываем поля, которые будут валидироваться.
# Поля описываются как атрибуты класса. Передаем в них классы полей из библиотеки marshmallow.
# Поля валидируются в порядке их описания в классе.


class FilmSchema(Schema):
    title = fields.Str()
    year = fields.Int()


# Создаем экземпляр класса схемы.
film_schema = FilmSchema()

# Валидируем данные. Передаем в метод load данные для валидации.
# Используем many=True

try:
    result = film_schema.load(marvel_films, many=True)
    pprint(result)

except ValidationError as err:
    pprint(err.messages)