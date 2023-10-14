# Lesson 24
# 14.10.2023
"""
1. Разбор ДЗ №20 - Декоратор с параметрами
2. Обозначение проблемы - зачем нужно ООП?
3. Синтаксис именования классов
"""

"""
Правила именования классов в Пайтон:
1. Имя класса должно быть в CamelCase
2. Имя класса должно быть существительным
3. Имя класса должно быть в единственном числе
4. Имя класса должно быть уникальным
5. Имя класса не должно быть длинным
6. Имя класса не должно быть слишком коротким

"""


class NestedDoll:
    pass

# Создаем объекты класса NestedDoll
mattr_1 = NestedDoll()
mattr_2 = NestedDoll()
mattr_3 = NestedDoll()

# type - это тип объекта
# Мы создали 3 объекта, но у них одинаковый тип
print(type(mattr_1))
print(type(mattr_2))
print(type(mattr_3))

# id - это уникальный идентификатор объекта в памяти
# Мы создали 3 объекта, но у них разные id
print(id(mattr_1))
print(id(mattr_2))
print(id(mattr_3))
