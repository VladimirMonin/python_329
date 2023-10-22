"""
Lesson 27
22.10.2023

Темы:
Повторение материала
Функции str и repr в Python
Магические методы str и repr в Python
Сравнение объектов в Python
Другие методы сравнения объектов в Python
__call__ в Python
Модуль dataclasses в Python
"""
from typing import Dict, Union, Any


# __call__ - это специальный метод, который позволяет вызывать экземпляр класса как функцию.

class Pizza:
    def __init__(self):
        self.price = None
        self.size = None

    def get_order(self, price, size):
        self.price = price
        self.size = size

    def __call__(self, **kwargs: Dict[Any, str | int]) -> str:
        # Определяем цену и размер из kwargs
        self.get_order(kwargs['price'], kwargs['size'])
        # Получаем пиццу
        # Тут должен быть явный возврат значения, чтобы мы могли получить результат работы функции
        return self.get_pizza()

    def get_pizza(self):
        return f'Доставка пиццы размера {self.size} по цене {self.price}'

    # def get_vacation(self):
    #     self.get_order(100, 'big')
    #     self.get_pizza()


pizza = Pizza()
my_pizza = pizza(price=100, size='big')
print(my_pizza)
