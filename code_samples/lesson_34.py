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
            class_name = args[0].__class__.__name__  # args[0] - это self
            # Формируем лог строку
            log_string = f'[{current_datetime}] В классе {class_name} в методе {function_name} произошла ошибка: {ex}\n'
            # Записываем в файл
            with open('logs.txt', 'a', encoding='utf-8') as file:
                file.write(log_string)

            return log_string

    return wrapper


# Такой же декоратор, но реализованный через класс с несколькими методами:
# Реализуем в РАЗНЫХ методах следующее:
# - определение даты и времени
# - определение имени функции
# - определение имени класса
# - формирование лог строки
# - запись в файл

class LoggerDecorator:
    def __init__(self, func):
        self.func = func

    # Метод определяет дату и время
    @staticmethod
    def get_current_datetime():
        return datetime.now().strftime('%d.%m.%Y %H:%M:%S')

    # Метод определяет имя функции
    def get_function_name(self):
        return self.func.__name__

    # Метод определяет имя класса
    @staticmethod
    def get_class_name(instance):
        return instance.__class__.__name__

    # Метод формирует лог строку
    def get_log_string(self, instance, ex):
        return (f'[{self.get_current_datetime()}] '
                f'В классе {self.get_class_name(instance)} в '
                f'методе {self.get_function_name()} произошла ошибка: {ex}\n')

    # Метод записывает в файл
    def write_to_file(self, instance, ex):
        with open('logs.txt', 'a', encoding='utf-8') as file:
            file.write(self.get_log_string(instance, ex))

    def __call__(self, *args, **kwargs):
        try:
            args = list(args)
            kwargs = dict(kwargs)

            result = self.func(*args, **kwargs)
            return result
        except Exception as ex:
            self.write_to_file(args[0], ex)
            return self.get_log_string(args[0], ex)


class Math:

    # @staticmethod
    @LoggerDecorator
    def devision(self, a, b):
        return a / b


m = Math()
m.devision(1, 1)
