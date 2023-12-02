"""
Lesson 40
02.12.2023

Тема: Разбор ДЗ по игре в города на ООП - HW_25.md
- Добавление ручной сериализации и валидации данных + dataclass
- JSON Schema - потребность в поиске более удобного способа валидации данных
- Установка и использование библиотеки jsonschema

pip install jsonschema
"""
import jsonschema
from jsonschema import validate

# "additionalProperties": false - запрещает добавлять в словарь новые ключи. Импорт
# из jsonschema необходим для работы этого параметра



