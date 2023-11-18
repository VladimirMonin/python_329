"""
Lesson 34
18.11.2023

Тема: Декораторы классов и методов.
- Вспоминаем что такое декораторы
"""
from typing import Callable


# Декоратор принт до принт после

def print_decorator1(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        if False:
            return func(*args, **kwargs)

    return wrapper


def print_decorator2(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@print_decorator2
@print_decorator1
def some_print():
    return ("Hello world")


print(some_print())
