"""
Lesson 27
22.10.2023

Темы:
Повторение материала
Функции str и repr в Python
Магические методы str и repr в Python
Сравнение объектов в Python
Другие методы сравнения объектов в Python
Модуль dataclasses в Python
"""


# Сравнение объектов в Python
# __eq__()  == . Метод, который сравнивает два объекта и возвращает True, если они равны, и False, если они не равны.
# __ne__()  != . Метод, который сравнивает два объекта и возвращает True, если они не равны, и False, если они равны.
# __lt__()  < . Метод, который сравнивает два объекта и возвращает True, если первый объект меньше второго, и False, если первый объект больше второго.
# __gt__()  > . Метод, который сравнивает два объекта и возвращает True, если первый объект больше второго, и False, если первый объект меньше второго.
# __le__()  <= . Метод, который сравнивает два объекта и возвращает True, если первый объект меньше или равен второму, и False, если первый объект больше второго.
# __ge__()  >= . Метод, который сравнивает два объекта и возвращает True, если первый объект больше или равен второму, и False, если первый объект меньше второго.


class Pizza:
    def __init__(self, name: str, weight: float, price: float):
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other):
        """
        Метод, который сравнивает два объекта и возвращает True, если они равны, и False, если они не равны.
        :param other:
        :return:
        """
        if not isinstance(other, Pizza): # Проверка на принадлежность к классу
            raise ValueError('Сравнивать можно только объекты класса Pizza')
        # Задаем условия сравнения (какое выражение должно вернуть True чтобы объекты были равны)
        return self.name == other.name and self.weight == other.weight and self.price == other.price

    def __gt__(self, other):
        """
        Метод, который сравнивает два объекта и возвращает True, если первый объект больше второго, и False, если первый объект меньше второго.
        :param other:
        :return:
        """
        if not isinstance(other, Pizza):
            raise ValueError('Сравнивать можно только объекты класса Pizza')
        return self.price > other.price

    def __lt__(self, other):
        """
        Метод, который сравнивает два объекта и возвращает True, если первый объект меньше второго, и False, если первый объект больше второго.
        :param other:
        :return:
        """
        if not isinstance(other, Pizza):
            raise ValueError('Сравнивать можно только объекты класса Pizza')
        return self.price < other.price

    def __ge__(self, other):
        """
        Метод, который сравнивает два объекта и возвращает True, если первый объект больше или равен второму, и False, если первый объект меньше второго.
        :param other:
        :return:
        """
        if not isinstance(other, Pizza):
            raise ValueError('Сравнивать можно только объекты класса Pizza')
        return self.price >= other.price

    def __le__(self, other):
        """
        Метод, который сравнивает два объекта и возвращает True, если первый объект меньше или равен второму, и False, если первый объект больше второго.
        :param other:
        :return:
        """
        if not isinstance(other, Pizza):
            raise ValueError('Сравнивать можно только объекты класса Pizza')
        return self.price <= other.price

    def __ne__(self, other):
        """
        Метод, который сравнивает два объекта и возвращает True, если они не равны, и False, если они равны.
        :param other:
        :return:
        """
        if not isinstance(other, Pizza):
            raise ValueError('Сравнивать можно только объекты класса Pizza')
        return self.price != other.price

    def __str__(self):
        """
        Метод, который возвращает строковое представление объекта
        :return:
        """
        return f'Название: {self.name}, вес: {self.weight}, цена: {self.price}'

    def __repr__(self):
        """
        Метод, который возвращает строковое представление объекта
        :return:
        """
        return f'Название: {self.name}, вес: {self.weight}, цена: {self.price}'






# Проверка работы. Создаем 2 одинаковых пиццы и проверяем на равенство

pizza_1 = Pizza('Маргарита', 0.75, 650)
pizza_2 = Pizza('Маргарита', 0.5, 500)

print(pizza_1 < pizza_2)  # True
pizza_list = [pizza_2, pizza_1]

print(pizza_list)
# Сортируем от дорогой к дешевой
pizza_list.sort(reverse=True)
print(pizza_list)