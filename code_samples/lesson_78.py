"""
Lesson 78
10.12.2023
# Тема: Marshmallow
Поля
- String - Строки
- Integer - Целые числа
- Float - Числа с плавающей точкой
- Boolean - Булевые значения
- Date - Дата
- DateTime - Дата и время
- Time - Время
- Url - Ссылка
- Email - Почта
- List - Список
- Dict - Словарь
- Nested - Вложенные схемы!)
- Function - Результат выполнения функции

Параметры полей
- required - Обязательное поле. По умолчанию False. Если True, то поле не может быть пустым
- allow_none - Разрешить None для поля. По умолчанию False
- default - Значение по умолчанию при процессе сериализации
- missing - Значение по умолчанию при процессе десериализации
- validate - Валидатор. Может принимать функцию, метод или список функций и методов, и имеет свои инструметы, в т.ч. регулярные выражения
- load_only - Только при загрузке данных
- dump_only - Только при выгрузке данных
"""
import json
from dataclasses import dataclass
from pprint import pprint
from typing import List

from marshmallow import Schema, fields, ValidationError, validate
from marshmallow_dataclass import class_schema

json_string_datetime_lessons = """
[
    {
        "lesson": "lesson_1",
        "datetime": "2023-10-10:13-00-00",
        "teacher": "Vladimir",
        "students": ["Bob", "Alice", "John"],
        "subject": "Python",
        "teacher_mail": "mva@mail.ru"
    },
    {
        "lesson": "lesson_2",
        "datetime": "2023-10-11:13-00-00",
        "teacher": "Vladimir",
        "students": ["Bob", "Alice", "John"],
        "subject": "Python",
        "teacher_mail": "vm@mail.ru"
    },
    {
        "lesson": "lesson_3",
        "datetime": "2023-10-12:13-00-00",
        "teacher": "Vladimir",
        "students": ["Bob", "Alice", "John"],
        "subject": "Python",
        "teacher_mail": "mva@mail.ru"
    }
]
"""
"""
У нас несколько вариантов работы.
1. Мы можем сделать детальную Схему(наследование от Schema) и валидировать каждое поле отдельно.
Но на выходе мы получим словарь, а не объект датакласса.

2. Мы можем сделать схему на основе датакласса, но тогда мы не сможем валидировать каждое поле отдельно.
Получим просто базовую валидацию, которая есть в датаклассе.

3. Мы можем сделать схему на основе 
датакласса, и расширить ее, добавив валидацию для каждого поля.
"""


@dataclass
class Lesson:
    lesson: str
    datetime: str
    teacher: str
    students: List[str]
    subject: str
    teacher_mail: str


# Создание схемы на основе датакласса
LessonSchema = class_schema(Lesson)


# Создание схемы на основе датакласса, и расширение ее
class ExtendedLessonSchema(LessonSchema):
    datetime = fields.DateTime(format="%Y-%m-%d:%H-%M-%S", required=True)

    teacher_mail = fields.Email(required=True,
                                validate=[
                                    validate.Length(min=3, max=20,
                                                    error="Email must be between 3 and 20 characters long"),
                                    validate.Email(error="Not a valid email address"),
                                    validate.Regexp(regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
                                                    error="Not a valid email address")
                                ])


# Чтение данных json строки
data = json.loads(json_string_datetime_lessons)

# Создание объекта схемы
schema = ExtendedLessonSchema(many=True)

# Валидация данных
try:
    result = schema.load(data)
    pprint(result)
except ValidationError as e:
    print(e)
    exit(1)

# Генерация JSON схемы
json_schema = LessonSchema().json_schema()

# Сохранение JSON схемы в файл
with open("lesson_78.json", "w", encoding="utf-8") as f:
    json.dump(json_schema, f, indent=4)