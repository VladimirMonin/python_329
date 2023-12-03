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
import jsonschema
from jsonschema import validate, ValidationError

# "additionalProperties": false - запрещает добавлять в словарь новые ключи. Импорт
# из jsonschema необходим для работы этого параметра

from data.marvel import simple_set

# Схема для валидации данных, которые импортируем из data.marvel
# У нас массив, состоящий из строк, длинной от 3 до 100 символов
schema = {
    "type": "array",
    "items": {
        "type": "string",
        "minLength": 3,
        "maxLength": 100
    }
}

# Валидация данных
simple_list = list(simple_set)
try:
    validate(instance=simple_list, schema=schema)
except ValidationError as error:
    print(error)
else:
    print('Данные валидны')
finally:
    print('Валидация завершена')



