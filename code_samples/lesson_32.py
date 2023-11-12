"""
Lesson 32
12.11.2023

Тема: Абстрактные классы. Полиморфизм
- Разбор ДЗ службы доставки
- Потребность в абстрактных классах
"""
from abc import ABC, abstractmethod

"""
Для описания абстрактных классов в питоне используется модуль abc
Абстрактный класс наследуется от ABC

from abc import ABC

#     Абстрактный метод - это метод, который должен быть реализован в дочерних классах
#     Абстрактные методы объявляются с помощью декоратора @abstractmethod
#     Абстрактные методы не имеют реализации
#     Абстрактные методы не могут быть вызваны
#     Абстрактные методы могут быть вызваны только в дочерних классах
"""


class Delivery(ABC):
    """
    Абстрактный класс для доставки
    """

    def __init__(self, address):
        """
        Конструктор класса
        :param address: Адрес доставки
        """
        self.address = address

    def deliver(self):
        """
        Метод доставки
        :return: None
        """
        print(f'Доставка по адресу {self.address}')

    @abstractmethod
    def calculate_cost(self, start_cost: float) -> float:
        """
        Метод для расчета стоимости доставки
        :param start_cost:
        :param product: Объект товара
        :return: Стоимость доставки
        """
        pass


class DeliveryServiceA(Delivery):
    """
    Класс для доставки сервисом A
    """

    def calculate_cost(self, start_cost: float) -> float:
        """
        Метод для расчета стоимости доставки
        :param start_cost:

        :return: Стоимость доставки
        """
        return start_cost * 0.1


class DeliveryServiceB(Delivery):
    """
    Класс для доставки сервисом B. У него есть
    международная доставка, поэтому мы используем миксин InternationalMixin
    """


class DeliveryServiceC(Delivery):
    """
    Класс для доставки сервисом C. У него есть
    международная доставка, поэтому мы используем миксин InternationalMixin
    """


dev = DeliveryServiceA('Москва')  # Будет работать нормально, у него есть реализация абстрактного метода
dev.deliver()
# dev = DeliveryServiceB('Москва') # TypeError: Can't instantiate abstract class DeliveryServiceB with abstract method calculate_cost
