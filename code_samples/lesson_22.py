# Lesson 22 - 01 октября 2023 года
import time
from typing import Any, Callable, List
from data.cities import cities


# TODO - Декоратор может ли принимать несколько функций?
# Декораторы

def print_decorator(func: Callable) -> Callable:
    def wrapper() -> None:
        print("Start")
        func()
        print("End")

    return wrapper


def some_func() -> None:
    print("Вызов функции some_func")


f: Callable = print_decorator(some_func)


# f()


@print_decorator
def some_func2() -> None:
    print("Вызов функции some_func2")


@print_decorator
def some_func3(group: str) -> None:
    print(f"Привет группа {group}!")


# some_func3("Python329") # TypeError: wrapper() takes 0 positional arguments but 1 was given

# Частный случай. Но не универсальный.
def print_decorator2(func: Callable) -> Callable:
    def wrapper(group: str) -> None:
        if group:
            print(f"Собираемся поприветствовать группу: {group}")
            func(group)
            print(f"Поприветствовали группу: {group}")
        else:
            print("Не передана группа")

    return wrapper


@print_decorator2
def some_func4(group: str) -> None:
    print(f"Привет группа {group}!")


@print_decorator2
def some_func5(group: str, theme: str) -> None:
    print(f"Привет группа {group}! Тема занятия: {theme}")


# some_func4(None)

# some_func5("Python329", "Декораторы") # TypeError: wrapper() takes 1 positional argument but 2 were given

def print_decorator3(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> None:
        print("Start")
        func(*args, **kwargs)
        print("End")

    return wrapper


@print_decorator3
def some_func5(group: str, theme: str) -> None:
    print(f"Привет группа {group}! Тема занятия: {theme}")


# some_func5("Python329", "Декораторы")


# Декоратор, который будет засекать время выполнения функции
# Нам понадобится модуль time

# Текущее время
# print(time.time()) # Время в секундах с 1 января 1970 года
# После точки - микросекунды

# Время сейчас в переменную
# start_time = time.time()
# time.sleep(5)
# finish_time = time.time()

# print(f"Прошло {finish_time - start_time} секунд")
# Округляем до 4 знаков после запятой через f строку
# print(f"Прошло {finish_time - start_time:.4f} секунд")


# Декоратор, который будет засекать время выполнения функции

import time
from typing import Callable, Any

import time
from typing import Callable, Any

import time
from typing import Callable, Any

"""
time.perf_counter() — это функция из модуля time в стандартной библиотеке Python, которая предоставляет доступ к 
монотонному счётчику времени с наивысшим доступным разрешением для измерения коротких промежутков времени. 
Вот несколько ключевых моментов об time.perf_counter():

Монотонность: Этот счетчик является монотонным, что означает, что его значения никогда не уменьшаются. 
Это важно для измерения временных интервалов, так как это гарантирует, что разница между концом и началом 
интервала всегда будет положительной или нулевой, даже если системные часы изменяются.

Высокое разрешение: Функция предоставляет время с высокой точностью, что делает ее идеальной для замера 
времени выполнения операций, особенно когда требуется измерить очень короткие промежутки времени.

Независимость от системного времени: Значение, возвращаемое time.perf_counter(), не зависит от системного 
времени и не подвержено изменениям из-за корректировки часов или перехода на летнее/зимнее время.

Использование: Эта функция часто используется для бенчмаркинга и профилирования кода, поскольку 
она предоставляет более точные измерения времени, чем time.time() или time.clock().

Платформонезависимость: time.perf_counter() работает на различных платформах, 
предоставляя стабильный интерфейс для замера времени.

Возвращаемое значение: Функция возвращает время в секундах как число с 
плавающей точкой. С момента запуска Python (или от момента первого вызова time.perf_counter(), 
точное определение зависит от реализации) до момента вызова функции.
"""


def time_decorator(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # pref_counter - точное время
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        finish_time = time.perf_counter()
        elapsed_time = finish_time - start_time
        # Используем format для вывода времени в обычном десятичном формате
        print(f"Программа выполнялась {format(elapsed_time, '.10f')} секунд")
        return result

    return wrapper


# Функция принимает число и проходит циклом по cities и выводит города где население
# cities["population"] больше или равно переданному числу

@time_decorator
def get_cities_by_population(population: int) -> List[str]:
    result_list = []
    for city in cities:
        if city["population"] >= population:
            result_list.append(city["name"])
    # time.sleep(1)
    return result_list


# Аналог на list comprehension
@time_decorator
def get_cities_by_population2(population: int) -> List[str]:
    # time.sleep(1)
    return [city["name"] for city in cities if city["population"] >= population]


# Аналог на filter

@time_decorator
def get_cities_by_population3(population: int) -> List[str]:
    #     time.sleep(1)
    return list(map(lambda city: city["name"], filter(lambda city: city["population"] >= population, cities)))


test1 = get_cities_by_population(500000)
test2 = get_cities_by_population2(500000)
test3 = get_cities_by_population3(500000)
