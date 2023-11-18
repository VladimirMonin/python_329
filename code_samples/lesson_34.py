"""
Lesson 34
18.11.2023

Тема: Декораторы классов и методов.
- Вспоминаем что такое декораторы
- Print vs return
- Два декоратора на функцию
- Пример с HTML тегами
"""
from typing import Callable


# Декоратор класса. Добавим классу поле и метод
def add_field_and_method(cls: type) -> type:
    # self: type - указываем, что метод принимает экземпляр класса
    # __class__ - возвращает класс экземпляра
    # __name__ - возвращает имя класса
    def some_method(self: type) -> None:
        print(f'Вызван метод some_method у экземпляра класса {self.__class__.__name__}')

    # Метод который принимает Фамилию и Имя. Создает новое поле full_name, ложит данные туда
    # Делает сплит и кладет в поле first_name и last_name
    def add_full_name(self: type, full_name: str) -> None:
        self.full_name = full_name
        self.first_name, self.last_name = full_name.split()

    cls.some_method = some_method
    cls.add_full_name = add_full_name

    return cls


# Класс который мы будем декарировать и добавлять ему функционал и поля
@add_field_and_method
class SomeClass:
    def __init__(self, name: str) -> None:
        self.first_name = name

    def get_name(self) -> str:
        return self.name


# Создаем экземпляр класса и вызываем методы
some_class = SomeClass(name='Иван')  # Создаем экземпляр класса
some_class.some_method()  # Вызываем метод some_method (который был добавлен декоратором)
some_class.add_full_name('Иван Иванов')  # Вызываем метод add_full_name (который был добавлен декоратором)
print(some_class.full_name)  # Выводим поле full_name (которое было добавлено декоратором)
print(some_class.first_name)  # Выводим поле first_name (которое было изначально)
print(some_class.last_name)  # Выводим поле last_name (которое было добавлено декоратором)


