"""
Lesson 42
03.12.2023

Тема: JSON Schema

- JSON Schema - потребность в поиске более удобного способа валидации данных
- Установка и использование библиотеки jsonschema

pip install jsonschema
"""
import jsonschema
from jsonschema import validate, ValidationError

# "additionalProperties": false - запрещает добавлять в словарь новые ключи. Импорт
# из jsonschema необходим для работы этого параметра



