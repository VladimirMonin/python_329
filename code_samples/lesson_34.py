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
from datetime import datetime


# Функция для декорирования методов класса
# Делает попытку вызова метода, если успешно, то возвращает результат, если нет, то логирует исклчение в файл

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as ex:
            # Определяем дату и время
            current_datetime = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            # Определяем имя функции
            function_name = func.__name__
            # Определяем имя класса
            class_name = args[0].__class__.__name__ # args[0] - это self
            # Формируем лог строку
            log_string = f'[{current_datetime}] В классе {class_name} в методе {function_name} произошла ошибка: {ex}\n'
            # Записываем в файл
            with open('logs.txt', 'a', encoding='utf-8') as file:
                file.write(log_string)

            return log_string


    return wrapper


# Класс для декорирования (Math) с методом деления а на б

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @logger_decorator
    def division(self):
        return self.a / self.b


# Создаем объект класса Math
math = Math(10, 0)

# Вызываем метод division
print(math.division())

# Пробуем декоратор на функции а не на методе класса. Функция деления


@logger_decorator
def get_division_func(a, b):
    return a / b


# Вызываем функцию
print(get_division_func(10, 0))
