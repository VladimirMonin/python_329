"""
Lesson 34
18.11.2023

Тема: Декораторы классов и методов.
- Вспоминаем что такое декораторы
- Print vs return
- Два декоратора на функцию
- Пример с HTML тегами

Функция - декоратор класса
- Добавляем новые поля
- Добавляем новые методы

Функция - декоратор методов
"""
import time
from datetime import datetime


# Декоратор класс который будет декорировать методы и функции и выводить дату и время выполнения

class TimeIt:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        # pref_counter - точное время
        start_time = time.perf_counter()
        result = self.fn(*args, **kwargs)
        finish_time = time.perf_counter()
        print(f"Время выполнения функции {self.fn.__name__} заняло {finish_time - start_time:.10f} секунд")
        return result

# Функция деления
@TimeIt
def div(a, b):
    return a / b

# Test
print(div(10, 5))
print(div(10, 2))
print(div(10, 1))
