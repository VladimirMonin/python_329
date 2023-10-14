# Lesson 24
# 14.10.2023
"""
1. Разбор ДЗ №20 - Декоратор с параметрами
"""


# Функциональный подход против ООП
# Функции покраски

def get_nested_doll() -> str:
    return 'Nested doll'


def get_red_color(doll: str) -> str:
    doll += " .Color RED"
    return doll


def get_green_color(doll: str) -> str:
    doll += " .Color GREEN"


# Позже, мы могли бы сделать кастомные матрешки с 10-20 мелкими внутри
# Это ещё один модуль а потом ещё один....

# Где-то у нас была бы функия main которая бы перекладывала бы
# результат выполнения одних фукнций в другие.

# А ещё их надо было бы имортировать с разных - разных модулей и пакетов
a = get_nested_doll()
b = get_nested_doll()
c = get_nested_doll()
