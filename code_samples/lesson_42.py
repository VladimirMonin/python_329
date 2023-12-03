"""
Lesson 42
03.12.2023

Тема: JSON Schema

- JSON Schema - потребность в поиске более удобного способа валидации данных
- Установка и использование библиотеки jsonschema
- validate
- ValidationError

pip install jsonschema
"""
from pprint import pprint

import jsonschema
from jsonschema import validate, ValidationError

# "additionalProperties": false - запрещает добавлять в словарь новые ключи. Импорт
# из jsonschema необходим для работы этого параметра

from data.marvel import simple_set



users_data = [
    {
        "email": "user1@example.com",
        "username": 2
    },
    {
        "email": "user2@example.com",
        "username": "user2"
    },
    {
        "email": "user3@example.com",
        "username": "user3"
    },
    {
        "email": "user4",
        "username": "user4"
    },
    {
        "email": "invalid-email",
        "username": "user5"
    },
    {
        "email": "user6@example.com",
        "username": "user6"
    },
    {
        "email": "user7@example.com",
        "username": "user7"
    },
    {
        "email": "user8@example.com",
        "username": "user8"
    },
    {
        "email": "user9@example.com",
        "username": "user9"
    },
    {
        "email": 2,
        "username": "user10"
    },
    {
        "email": "user11@example.com",
        "username": "user11"
    },
    {
        "email": "user12@example.com",
        "username": "user12"
    },
    {
        "email": "user13@example.com",
        "username": "user13"
    },
    {
        "email": "user14",
        "username": "user14"
    },
    {
        "email": "invalid-email",
        "username": "user15"
    },
    {
        "email": "user16@example.com",
        "username": "user16"
    },
    {
        "email": "user17@example.com",
        "username": "17"
    },
    {
        "email": "user18@example.com",
        "username": "user18"
    },
    {
        "email": "user19@example.com",
        "username": "user19"
    },
    {
        "email": "user20@example.com",
        "username": "user20"
    },
    {
        "email": "user20@example.com",
        "username": "u&ser20"
    },
    {
        "email": "user20@example.com",
        "username": "us er20"
    },
    {
        "email": "user20@example.com",
        "username": "user_sfsfsfsfsf_sfsfsfddfsf_sfsdf20"
    }
]

"""
Практика!
1. Создать схему для валидации данных из users_data
2. Валидировать данные из users_data в цикле
3. Вывести невалидные данные в консоль
"""

# 1. Создать схему для валидации каждого словаря из users_data,
# используя jsonschema. Для првоерки емейлов - "format": "email"
# Для проверки username - "pattern": "^[a-zA-Z0-9_]{4,20}$"
schema = {
    "type": "object",
    "properties": {
        "email": {
            "type": "string",
            "format": "email"
        },
        "username": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9_]{4,20}$"
        }
    },
    "required": ["email", "username"],
    "additionalProperties": False
}

# 2. Валидировать данные из users_data в цикле
invalid_data = []
valid_data = []
for user in users_data:
    try:
        # Делаем попытку валидировать данные по одному пользователю
        validate(user, schema, format_checker=jsonschema.FormatChecker())
        valid_data.append(user)
        #  Если данные не валидны, то валидатор выкинет ошибку
    except ValidationError as e:
        invalid_data.append(user)
        # print(e)


# 3. Вывести невалидные данные в консоль
pprint(invalid_data)


