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
        "teacher_mail": "/&&*@mail.ru"
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


class LessonSchema(Schema):
    lesson = fields.String(required=True)
    datetime = fields.DateTime(required=True, format="%Y-%m-%d:%H-%M-%S")
    teacher = fields.String(required=True)
    students = fields.List(fields.String(), required=True)
    subject = fields.String(required=True)
    teacher_mail = fields.Email(required=True,
                                validate=[
                                    validate.Length(min=3, max=20, error="Email must be between 3 and 20 characters long"),
                                    validate.Email(error="Not a valid email address"),
                                    validate.Regexp(regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", error="Not a valid email address")
                                ])

    # Meta - класс для управления поведением схемы
    class Meta:
        # ordered = True - сохраняет порядок полей в схеме
        # unknown = "EXCLUDE" - игнорирует неизвестные поля
        # fields - список полей, которые будут включены в схему
        # exclude - список полей, которые будут исключены из схемы
        # additional - дополнительные поля, которые будут включены в схему
        # load_only - поля, которые будут доступны только при загрузке данных
        # dump_only - поля, которые будут доступны только при выгрузке данных
        # dateformat - формат даты
        pass


@dataclass
class Lesson:
    lesson: str
    datetime: str
    teacher: str
    students: List[str]
    subject: str
    teacher_mail: str


# Проводим валидацию и десериализацию данных в список объектов датакласса
# Получаем объекты пайтон
data = json.loads(json_string_datetime_lessons)
# Создаем объект схемы
schema = LessonSchema(many=True)
# Валидируем и десериализуем данные в список объектов датакласса Lesson


lessons = schema.load(data)

pprint(lessons)
print(type(lessons))
print(type(lessons[0]))
print(lessons[0]['datetime'])

