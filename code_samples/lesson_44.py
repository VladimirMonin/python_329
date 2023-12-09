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

small_dict = {
    'Железный человек': 2008,
    'Невероятный Халк': 2008,
    'Железный человек 2': 2010,
    'Тор': 2011,
    'Первый мститель': 2011,
    'Мстители': 2012,
    'Мстsdfители': '222',
}


# Создадим класс схемы, который будет наследоваться от класса Schema.
# В нем будут описаны поля, которые будут проверяться на валидность.

class MovieSchema(Schema):
    # Поле title - строка.
    title = fields.String()
    # Поле year - целое число - тип int. (не строка!)
    year = fields.Integer(validate=lambda n: isinstance(n, int))


# Создаем экземпляр класса схемы и передаем в него данные для валидации.

schema = MovieSchema()

# Проверяем данные на валидность.
# Объявляем цикл по словарю, который будем проверять.
for key, value in small_dict.items():
    # В блоке try вызываем метод load экземпляра класса схемы и передаем в него данные для валидации.
    # В блоке except обрабатываем ошибки валидации.
    try:
        schema.load({'title': key, 'year': value})
    except ValidationError as exc:
        pprint(exc.messages)
