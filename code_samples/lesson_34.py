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

from datetime import datetime


class LoggerDecorator:

    def __init__(self, func):
        self.func = func

    @staticmethod
    def get_current_datetime():
        return datetime.now().strftime('%d.%m.%Y %H:%M:%S')

    def get_name(self):
        return self.func.__qualname__  # __qualname__ - полное имя класса и метода

    def get_log_string(self, ex):
        return (f'[{self.get_current_datetime()}] '
                f'В {self.get_name()} произошла ошибка: {ex}\n')

    def write_to_file(self, ex):
        with open('logs.txt', 'a', encoding='utf-8') as file:
            file.write(self.get_log_string(ex))

    def __call__(self, *args, **kwargs):
        try:
            # Удаление из аргументов self - сделает это декоратор функции
            return self.func(self, *args, **kwargs)
        except Exception as ex:
            self.write_to_file(ex)
            # raise  # Проброс исключения, если нужен raise


class Math:
    @LoggerDecorator
    def division(self, a, b):
        return a / b


m = Math()
m.division(1, 0)  # Приведет к ZeroDivisionError и будет залогировано


@LoggerDecorator
def division(a, b):
    return a / b


division(1, 0)  # Приведет к ZeroDivisionError и будет залогировано
