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
from dataclasses import dataclass
from pprint import pprint
from typing import List

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


# Окультуриваем код. Делаем датакласс для пользователей, класс для валидации и класс для сериализации
# Класс сериализации будет принимать весь список словарей и иметь __call__ метод, который будет возвращать
# список объектов User.

@dataclass
class User:
    email: str
    username: str


class UserValidator:
    def __init__(self, schema: dict):
        self.schema = schema

    def validate_user(self, user: dict, is_checker=False) -> bool:
        try:
            validate(user, self.schema,
                     format_checker=jsonschema.FormatChecker() if is_checker else None)
            return True
        except ValidationError as e:
            return False


class UserSerializer:
    def __init__(self, users_data: List[dict], data_validator: UserValidator):
        self.users_data = users_data
        self.data_validator = data_validator
        self.__validated_data: List[dict] | None = None
        self.serialize_data: List[User] | None = None

    def __call__(self) -> List[User]:
        # Валидация и сериализация данных
        self.__validated_data = [user_data for user_data in self.users_data
                                 if self.data_validator.validate_user(user_data, is_checker=True)]

        self.serialize_data = [User(**user_data) for user_data in self.__validated_data]
        return self.serialize_data


user_validator = UserValidator(schema)
user_serializer = UserSerializer(users_data, user_validator)
result = user_serializer()

pprint(result)
