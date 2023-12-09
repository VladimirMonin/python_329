"""
Lesson 44
03.12.2023

Тема: Marshmallow
- Установка pip install marshmallow
- Импорт основных классов и инструментов
- Создание схемы для валидации данных
- Валидация данных, метод load
- Many=True
- ValidationError
- Marshmallow Dataclass
- Десериализация данных
- Создание схемы на основе датакласса (marshmallow_dataclass)
- Сериализация данных, метод dumps
- Десериализация данных, метод loads
-

"""

from marshmallow import Schema, fields, ValidationError
from marshmallow_dataclass import class_schema
from dataclasses import dataclass
from pprint import pprint
import json

from data.marvel import full_dict

"""
Практика десериализации данных!

Создайте датакласс для валидации данных о фильме на основе json файла.
Создайте схему на основе датакласса, используя библиотеку marshmallow_dataclass
Создайте объект схемы и валидируйте данные из json файла (many=True)
Получите на выходе список объектов датакласса
"""