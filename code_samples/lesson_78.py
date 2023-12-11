"""
Lesson 78
10.12.2023
# Тема: Marshmallow
Расширение схемы marshmallow созданной на основе датакласса другой схемой
Сохранение схемы marshmallow в JSON схему

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

Встроенный валидатор validate
- Length - Длина строки или списка (validate.Length(min=3, max=20))
- Range - Диапазон чисел (validate.Range(min=0, max=100))
- Equal - Равенство значений (validate.Equal(10))
- OneOf - Одно из значений (validate.OneOf([1, 2, 3]))
- NoneOf - Ни одно из значений (validate.NoneOf([1, 2, 3]))
- Regexp - Регулярное выражение (validate.Regexp(regex=r"^[a-zA-Z0-9_.+-]+$"))
- Predicate - Предикат. Проверяет значение на истинность (validate.Predicate(lambda x: x > 10))
- URL - Ссылка (validate.URL())
- Email - Почта (validate.Email())
- UUID - Уникальный идентификатор. Проверяет значение на соответствие формату UUID (validate.UUID())
- InstanceOf - Экземпляр класса  (validate.InstanceOf(int))
- Nested - Вложенная схема (validate.Nested(Schema)) Проверяет вложенные данные на соответствие схеме
- List - Список (validate.List([validate.Length(min=3, max=20), validate.Email()]))
- Tuple - Кортеж (validate.Tuple([validate.Length(min=3, max=20), validate.Email()]))
- Dict - Словарь (validate.Dict([validate.Length(min=3, max=20), validate.Email()]))
- Callable - Вызываемый объект проверяет значение на истинность (validate.Callable(lambda x: x > 10))
- Method - Метод проверяет значение на истинность (validate.Method("validate_name"))
- Function - Функция проверяет значение на истинность (validate.Function(lambda x: x > 10))
- AllOf - Все из значений (validate.AllOf([validate.Length(min=3, max=20), validate.Email()]))
- AnyOf - Любое из значений (validate.AnyOf([validate.Length(min=3, max=20), validate.Email()]))
- NoneOf - Ни одно из значений (validate.NoneOf([validate.Length(min=3, max=20), validate.Email()]))
- ContainsOnly - Содержит только (validate.ContainsOnly([validate.Length(min=3, max=20), validate.Email()]))
- ContainsNoneOf - Не содержит ни одного из (validate.ContainsNoneOf([validate.Length(min=3, max=20), validate.Email()]))
- ContainsAnyOf - Содержит любое из (validate.ContainsAnyOf([validate.Length(min=3, max=20), validate.Email()]))
- ContainsAllOf - Содержит все из (validate.ContainsAllOf([validate.Length(min=3, max=20), validate.Email()]))
- ContainsOnly - Содержит только (validate.ContainsOnly([validate.Length(min=3, max=20), validate.Email()]))
- ContainsSchema - Содержит схему (validate.ContainsSchema(Schema))
- KeysSubset - Ключи подмножества (validate.KeysSubset([validate.Length(min=3, max=20), validate.Email()]))
- KeysEqual - Ключи равны (validate.KeysEqual([validate.Length(min=3, max=20), validate.Email()]))
- KeysOrdered - Ключи упорядочены (validate.KeysOrdered([validate.Length(min=3, max=20), validate.Email()]))
- KeysUnique - Ключи уникальны (validate.KeysUnique([validate.Length(min=3, max=20), validate.Email()]))
- ValuesSubset - Значения подмножества (validate.ValuesSubset([validate.Length(min=3, max=20), validate.Email()]))
- ValuesEqual - Значения равны (validate.ValuesEqual([validate.Length(min=3, max=20), validate.Email()]))
- ValuesOrdered - Значения упорядочены (validate.ValuesOrdered([validate.Length(min=3, max=20), validate.Email()]))
- ValuesUnique - Значения уникальны (validate.ValuesUnique([validate.Length(min=3, max=20), validate.Email()]))
- Schema - Схема (validate.Schema(Schema))



"""
import json
from dataclasses import dataclass
from pprint import pprint
from typing import List

from marshmallow import Schema, fields, ValidationError, validate
from marshmallow_dataclass import class_schema

from marshmallow_jsonschema import JSONSchema

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

# Создание экземпляра JSONSchema и преобразование схемы marshmallow в JSON схему
# pip install marshmallow-jsonschema
json_schema = JSONSchema().dump(ExtendedLessonSchema())

# Сохранение JSON схемы в файл
with open("lesson_78.json", "w", encoding="utf-8") as f:
    json.dump(json_schema, f, indent=4)