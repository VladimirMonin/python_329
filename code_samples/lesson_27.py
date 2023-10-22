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

# Сравнение объектов в Python
# Декоратор @total_ordering
# Это специальный декоратор из модуля functools, который позволяет нам определить только два метода сравнения объектов, а остальные методы будут определены автоматически.
# Нам необходимо определить только два метода сравнения объектов:
# __eq__ - для сравнения на равенство
# __lt__ - для сравнения на меньше

from functools import total_ordering


@total_ordering
class Pizza:
    def __init__(self, size):
        self.size = size

    def __eq__(self, other):
        return self.size == other.size

    def __lt__(self, other):
        return self.size < other.size

    def __str__(self):
        return f'Пицца размером {self.size}'

    def __repr__(self):
        return f'Pizza({self.size})'


pizza_1 = Pizza(30)
pizza_2 = Pizza(35)

print(pizza_1)
print(pizza_2)

print(pizza_1 == pizza_2)
print(pizza_1 < pizza_2)
print(pizza_1 > pizza_2)
print(pizza_1 <= pizza_2)
print(pizza_1 >= pizza_2)
