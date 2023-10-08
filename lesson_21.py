# Lesson 21 - 30 сентября 2023 года
import json

# Type hinting - Аннотация типов
# MyPy - статический анализатор кода
# Области видимости переменных
# Функции вложенные в функции
# Замыкания
# Декораторы

# Аннотация типов для переменных

# some_int: int = 10
# some_float: float = 10.5
# some_str: str = "Hello"
# some_bool: bool = True
# some_list: list = [1, 2, 3]
# some_tuple: tuple = (1, 2, 3)
# some_set: set = {1, 2, 3}
# some_dict: dict = {"a": 1, "b": 2}
# some_none: None = None
#
# some_or: int | float = 10

from typing import List, Tuple, Set, Dict, Optional, Union, Any, Callable


# some_list_int: List[int] = [1, 2, 3]  # Список из целых чисел
# some_list_str: List[str] = ["a", "b", "c"]  # Список из строк
# some_dict_int_str: Dict[int, str] = {1: "a", 2: "b"}  # Словарь из целых чисел и строк
# some_tuple_int_str: Tuple[int, str] = (1, "a")  # Кортеж из целых чисел и строк
# some_set_int: Set[int] = {1, 2, 3}  # Множество из целых чисел
# some_optional_int: Optional[int] = None  # Целое число или None
# some_union_int_str: Union[int, str] = 10  # Целое число или строка
# some_union_int_str2: int | str = 10  # Целое число или строка
# some_any: Any = 10  # Любой тип данных (мы не знаем)
#

# Функция записи в json файл которая записывает список словарей, где ключи - строки,
# а значения - строки или списки строк
#
# def write_json(data: List[Dict[str, str | List[Any]]], filename: str) -> None:
#     with open(filename, "w") as f:
#         json.dump(data, f)
#

# bad_data = [
#     {'1': "John",
#      10: "John",
#      123: ["football", "programming"]}
# ]
#
# good_data = [
#     {"name": "John",
#      "age": "22",
#      "hobbies": "programming"},
#     {"name": "John",
#      "age": "23",
#      "hobbies": ["football", "programming"]}
# ]
#
# write_json(good_data, "bad_data.json")
# # pip install mypy


# Функции с аннотацией типов
# def get_sum(a: int, b: int) -> int:
#     """
#     Сложение двух чисел
#     :param a:
#     :param b:
#     :return: Сумма двух чисел
#     """
#     return a + b


# def get_all_kiwi(fruits: List[str]) -> List[str]:
#     """
#     Возвращает список из всех киви
#     :param fruits:
#     :return:
#     """
#     return [fruit for fruit in fruits if fruit == 'kiwi']
#
#
# def write_list_dict_json(data: List[Dict[int, Union[str, int]]], filename: str) -> None:
#     """
#     Записывает список словарей в json файл
#     :param data:
#     :param filename:
#     :return:
#     """
#     with open(filename, 'w', encoding='utf-8') as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)


# Проверяем проверку типов в PycCharm - должны быть подсвечены ошибки
# # print(get_sum(1, 1))
# # print(get_all_kiwi(['apple', '123', 'banana']))
# write_list_dict_json([{2: 1, 5: '5'}, {2: 3, 3: 4}], 'data.json')

# Области видимости переменных
# Built-in scope - встроенная область видимости
# Global scope - глобальная область видимости
# Local scope - локальная область видимости
# Nonlocal scope - нелокальная область видимости

# Global scope - глобальная область видимости
# print = 10
# print(print)

# Global scope - глобальная область видимости
# a = 10


# def change_a():
#     # Local scope - локальная область видимости
#     # Global a
#     global a
#     a = 20
#     print(a)


# print(a)
# change_a()
# print(a)


# Non local scope - нелокальная область видимости
# Для доступа к переменным из нелокальной области видимости
# используется ключевое слово nonlocal

# a = 5
#
#
# def outer():
#     a = 10
#
#     def inner():
#         nonlocal a
#         a = 20
#         print(f'inner: {a}')
#
#     print(f'outer: {a}')
#     inner()
#     print(f'outer: {a}')
#
#
# print(f'global: {a}')
# outer()
# print(f'global: {a}')
#
#
def say_name(name):
    def say_goodbye():
        print(f"Goodbye {name}")

    say_goodbye()


# say_name("John")


def say_name2(name: str) -> Callable[[], None]:
    def say_goodbye() -> None:
        print(f"Goodbye {name}")

    return say_goodbye


# sn = say_name2("Олег")
# sn()
"""
Пока sn ссылается на функцию say_name2, 
то она не будет удалена из памяти.
Соответственно и Олег останется в переменной name.

Почему замыкание?

Мы держим внутренние окружения и "замыкаем" их по цепочке
Обратившись к sn

sn -> say_name2 -> say_goodbye -> name = "Олег" 
"""

# sn = say_name2("Олег")
# sn2 = say_name2("Петя")

# sn()
# sn2()


def counter(start: int = 0) -> Callable[[], int]:
    def step() -> int:
        nonlocal start
        start += 1
        return start

    return step


# c1 = counter(10)
# c2 = counter()
#
# print(c1(), c2())
# print(c1(), c2())
# print(c1(), c2())


"""
аннотация List[str] указывает, что fruits должен быть списком строк, 
и аннотация Callable[[], List[str]] указывает, что возвращаемое значение является функцией, которая не принимает аргументы (пустые скобки) и возвращает список строк.
"""


# Функция с кешем
def sort_fruits(fruits: List[str]) -> Callable[[], List[str]]:
    """
    Сортируем список и сохраняем результат в кеш
    :param fruits:
    :return:
    """
    cache: list = []

    def sort() -> List[str]:
        nonlocal cache
        if not cache or len(cache) != len(fruits):
            cache = sorted(fruits)
        return cache

    return sort


fruits = ["apple", "banana", "cherry", "kiwi", "mango", "lemon", "orange", "grape"]

# Тестируем функцию кеширования данных. Поместили кеш в замыкание
sort = sort_fruits(fruits)

# Вызвали замыкание
print(sort())

# Изменили список
fruits.append("melon")

# Вызвали замыкание
print(sort())

