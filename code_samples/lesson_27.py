"""
Lesson 27
22.10.2023

Темы:
Повторение материала
Функции str и repr в Python
Магические методы str и repr в Python
Сравнение объектов в Python
Другие методы сравнения объектов в Python
Модуль dataclasses в Python
"""


# Функции str и repr в Python
# Проверяем на встроенных типах данных (У них тоже есть методы str и repr)
# print(str(1))
# print(repr(1))
#
# print(str('1'))
# print(repr('1'))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Класс Person. Имя: {self.name}, {self.age} лет"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"


# Неформальное представление:
jane = Person("Jane", 30)

print(jane)  # Jane, 30 years old
print(str(jane))  # Jane, 30 years old

# Формальное представление:
print(repr(jane))  # Person('Jane', 30)

# Получили строку, которая содержит код, который можно использовать для создания объекта.
repr_str = repr(jane)

# eval - функция, которая принимает строку и выполняет ее как код Python
# Обратное преобразование repr в объект:
recreated_jane = eval(repr_str)
print(type(recreated_jane))

## **Запись объектов в файл и их восстановление из файла с использованием `__repr__()`**:

import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return json.dumps({"name": self.name, "age": self.age})


# Сериализация и запись объекта в файл
person = Person("Alice", 30)
with open("person.json", "w") as file:
    file.write(repr(person))

# Десериализация и восстановление объекта из файла
with open("person.json", "r") as file:
    person_json = file.read()
    person = Person.from_json(person_json)

print(person.name)  # Вывод: 'Alice'
print(person.age)  # Вывод: 30
