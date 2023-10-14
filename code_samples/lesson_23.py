# Lesson 23. Декораторы с параметрами
# 07.10.2023
import time
from typing import Callable, Any


# Декораторы с параметрами
# Декораторы с параметрами - это функции, которые принимают параметры и возвращают декоратор.

def print_decorator(func: Callable) -> Callable:
    def wrapper() -> None:
        print("Start")
        func()
        print("End")

    return wrapper


# Этот же декоратор, но чтобы он принимал 2 параметра, это префикс и постфикс
def print_decorator2(prefix: str, postfix: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(name) -> None:
            print(prefix)
            func(name)
            print(postfix)

        return wrapper

    return decorator


def print_hello(name: str) -> None:
    print(f'Hello {name}')


# print('start')
# f: Callable = print_decorator2("Start", "End")(print_hello)
# f("Олег")


# Используем синтаксис декораторов

# @print_decorator2("Start", "End")
# def print_hello2(name: str) -> None:
#     print(f'Hello {name}')


# Декоратор с одним параметром, коим является функция. Напремер мы можем передать параметром декоратора функцию len или type
# А декоратор будет делать принт f-строки с результатом работы функции len или type

def print_len_or_type_decorator(func: Callable) -> Callable:
    def decorator(work_func: Callable) -> Callable:
        def wrapper(name) -> None:
            print(f'Результат работы функции {func.__name__} - {func(name)}')
            work_func(name)

        return wrapper

    return decorator


# "Магический" метод __name__ - это имя функции, которую мы передаем в декоратор
# print(len.__name__)


def time_decorator(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> None:
        start_time = time.time()
        func(*args, **kwargs)
        finish_time = time.time()
        print(f"Программа выполнялась {finish_time - start_time} секунд")

    return wrapper



@print_len_or_type_decorator(type)
def print_hello3(name: str) -> None:
    print(f'Hello {name}')


# print_hello3("Олег")

# Мы можем разместить 2 декоратора и более на одной функции
# Порядок работы декораторов - снизу вверх


@time_decorator
@print_len_or_type_decorator(type)
def print_hello4(name: str) -> None:
    print(f'Hello {name}')


print_hello4('Николай')