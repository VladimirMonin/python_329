# Lesson 21 - 30 сентября 2023 года
from typing import List, Callable, Any


# Type hinting - Аннотация типов
# MyPy - статический анализатор кода
# Области видимости переменных
# Функции вложенные в функции
# Замыкания
# Декораторы


# Функции вложенные в функции и замыкания

def say_name(name):
    def say_goodbye():
        print(f"Goodbye {name}")

    say_goodbye()


# say_name("John")


def say_name2(name):
    def say_goodbye():
        print(f"Goodbye {name}")

    return say_goodbye


# sn = say_name2("Олег")
# sn()
"""
Пока sn ссылается на функцию say_name2, то она не будет удалена из памяти.
Соответственно и Олег останется в переменной name.

Почему замыкание?

Мы держим внутренние окружения и "замыкаем" их по цепочке
Обратившись к sn

sn -> say_name2 -> say_goodbye -> name = "Олег" 
"""

# sn = say_name2("Вася")
# sn2 = say_name2("Петя")

# sn()
# sn2()

"""Создается два разных замыкания, со своими переменными name"""


def counter(start: int = 0):
    def step():
        nonlocal start
        start += 1
        return start

    return step


c1: Callable = counter(10)
c2: Callable = counter()

print(c1(), c2())
print(c1(), c2())
print(c1(), c2())

# Замыкание для кеширования данных
# Сортируем список и сохраняем результат в кеш

fruits = ["apple", "banana", "cherry", "kiwi", "mango", "lemon", "orange", "grape"]

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


# ДЕКОРАТОРЫ

def print_decorator(func: Callable) -> Callable:
    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


def some_func() -> None:
    print("Вызов функции some_func")


# some_func()
# f: Callable = print_decorator(some_func)
# f()

# Изменяем поведение функции some_func
# some_func: Callable = print_decorator(some_func)
# some_func()


# Синтаксис @ - сахар для декораторов

@print_decorator
def some_func2() -> None:
    print("Вызов функции some_func2")


# some_func2()


@print_decorator
def some_func3(name: str) -> None:
    print(f"Вызов функции some_func3 с параметром {name}")


# some_func3("John") # TypeError: wrapper() takes 0 positional arguments but 1 was given

# Частный случай. Но не универсальный.
def print_decorator(func: Callable) -> Callable:
    def wrapper(name: str) -> None:
        print("Start")
        func(name)
        print("End")

    return wrapper


# Args kwargs
def print_decorator(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> None:
        print("Start")
        func(*args, **kwargs)
        print("End")

    return wrapper


# Делаем возвращаемое значение функции
def some_func4(name: str) -> str:
    return f"Вызов функции some_func4 с параметром {name}"


# some_func4 = print_decorator(some_func4)  # Ничего. Декоратор не возвращает значение


# Делаем возвращаемое значение функции
def print_decorator(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper


# Декораторы с параметрами

def print_decorator_msg(msg: str) -> Callable:
    def print_decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(msg)
            result = func(*args, **kwargs)
            return result

        return wrapper

    return print_decorator


def some_func5(name: str) -> str:
    return f"Вызов функции some_func5 с параметром {name}"


# Передача параметров вглубь декораторов работает автоматически - запрограммировано в языке
# some_func5 = print_decorator_msg("Hello")(some_func5)


@print_decorator_msg("Hello")
def some_func6(name: str) -> str:
    return f"Вызов функции some_func6 с параметром {name}"


# Тест получить результат функции и декаратора и напечатать
print(some_func6("John"))

marvel_dict = {
    40: {
        'title': 'Мстители: Секретные войны',
        'year': 2027,
        'director': 'TBA',
        'screenwriter': 'Майкл Уолдрон',
        'producer': 'Нет данных',
        'stage': 'Шестая фаза'
    },
    41: {
        'title': 'Войны в доспехах',
        'year': 'TBA',
        'director': 'TBA',
        'screenwriter': 'Яссер Лестер',
        'producer': 'Кевин Файги и Джонатан Шварц',
        'stage': 'Шестая фаза'}

}
