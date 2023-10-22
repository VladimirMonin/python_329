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


"""
Практика!
Создайте класс Гиря.
У Гири 2 аттрибута - название и вес
Опишите методы сравнения с использованием @total_ordering
Создайте 2 экземпляра класса Гиря
Проведите сравнение и получите правильный результат
"""
from functools import total_ordering


@total_ordering
class Kettlebell:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __eq__(self, other):
        return self.weight == other.weight and self.name == other.name

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return f'Гиря {self.name} весом {self.weight} кг'

    def __repr__(self):
        return f'Kettlebell({self.name}, {self.weight})'

    # Свой метод сравнения гирь только по имени
    def is_equal_name(self, other):
        return self.name == other.name


ket1 = Kettlebell('Кеттл 1', 16)
ket2 = Kettlebell('Кеттл 2', 24)

print(ket1)
print(ket2)

print(ket1 == ket2)
print(ket1 != ket2)
print(ket1 > ket2)
print(ket1 < ket2)
print(ket1 >= ket2)
print(ket1 <= ket2)

# Используем свой метод
print(ket1.is_equal_name(ket2))

# Делаем сортировку списка гирь
kettlebells = [Kettlebell('Кеттл 1', 16), Kettlebell('Кеттл 2', 24), Kettlebell('Кеттл 3', 12)]
print(kettlebells)
kettlebells.sort()
print(kettlebells)

# Сортировка через key - сортировка по имени передачи is_equal_name
kettlebells.sort(key=lambda x: x.is_equal_name(ket1))
