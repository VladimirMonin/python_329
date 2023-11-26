"""
Lesson 38
26.11.2023

Сериализация и десериализация
- JSON
- Сериализация и десериализация + JSON
"""
import json
from dataclasses import dataclass

"""
Дата-сет от Евгения - данные API Wildberries
URL:
https://search.wb.ru/exactmatch/ru/common/v4/search?TestGroup=no_test&TestID=no_test&appType=1&curr=rub&dest=-445278&query=%D0%91%D0%BB%D1%83%D0%B7%D0%BA%D0%B8%20%D0%B8%20%D1%80%D1%83%D0%B1%D0%B0%D1%88%D0%BA%D0%B8&resultset=catalog&sort=popular&spp=27&suppressSpellcheck=false
"""
# Dataclass товара из данных API Wildberries
"""
Данные необходимые нам лежат в datadict['data']['products']
Возьмем следующие ключи:
name - название товара
brand - бренд
sale - скидка
priceU - цена (надо разделить на 100)
salePriceU - цена со скидкой (надо разделить на 100)
rating - рейтинг
feedbacks - количество отзывов
"""

# TODO
"""
Задание:
Нам нужно произвести десириализацию данных из JSON в дата-классы.
Для этого необходимо
1. Создать дата-класс для товара и для данных API
2. Создать класс для десериализации данных
"""

"""
Без order=True: По умолчанию, без явного указания order=True, 
датаклассы генерируют только методы __eq__ и __repr__. 
Метод __eq__ используется для проверки равенства экземпляров класса, 
а __repr__ предоставляет строковое представление объекта.

С order=True: Когда вы устанавливаете параметр order=True в декораторе @dataclass, 
Python автоматически генерирует дополнительные методы для сравнения экземпляров:
 __lt__ (меньше), __le__ (меньше или равно), __gt__ (больше), и __ge__ (больше или равно). 
 
 Эти методы позволяют объектам класса участвовать в операциях сравнения и сортировки.
 
 Протокол передачи гипертекста (HTTP) 400 Bad Request код состояния ответа указывает, 
 что сервер не может или не будет обрабатывать запрос из-за чего-то, что 
 воспринимается как ошибка клиента (например, неправильный синтаксис запроса, 
 неверная структура сообщения запроса или обманчивая маршрутизация запроса). 
"""


# @dataclass(order=True)
@dataclass
class Product:
    name: str
    brand: str
    salePriceU: int
    sale: int
    priceU: int
    rating: float | int
    feedbacks: int


class ProductSerializer:
    """
    Класс для десериализации данных.
    Работает со списком словарей. Словари подаются в метод deserialize
    в качестве аргумента. Есть методы для проверки данных.

    Методы:
    deserialize - десериализует данные, возвращает экземпляры дата-классов
    check_rating_range - проверяет рейтинг на вхождение в диапазон от 0 до 5
    check_price_range - проверяет цену на вхождение в диапазон от 0 до 100000000
    check_len_name - проверяет длину названия на вхождение в диапазон от 0 до 500
    """

    def __init__(self):
        """
        Конструктор класса
        """
    @staticmethod
    def deserialize(data: list[dict]) -> list[Product]:
        """
        Метод десериализует данные, возвращает экземпляры дата-классов
        :param data: список словарей
        :return: список экземпляров дата-класса
        """
        products = []
        for product in data:
            # TODO

            # Проверяем данные на валидность
            # Если данные не валидны, то мы returtn status_code=400
            # Если данные валидны, то добавляем экземпляр дата-класса Product в список products
            # Создаем экземпляр дата-класса Product и добавляем в список products

            # Проверка на валидность данных
            if not ProductSerializer.check_rating_range(product['rating']):
                # return 400
                continue
            if not ProductSerializer.check_price_range(product['priceU']):
                #                 return 400
                continue
            if not ProductSerializer.check_price_range(product['salePriceU']):
                #                 return 400
                continue
            if not ProductSerializer.check_len_name(product['name']):
                #                 return 400
                continue

            # Создаем экземпляр дата-класса Product и добавляем в список products
            products.append(Product(
                name=product['name'],
                brand=product['brand'],
                salePriceU=product['salePriceU'],
                sale=product['sale'],
                priceU=product['priceU'],
                rating=product['rating'],
                feedbacks=product['feedbacks']
            ))
        return products

    @staticmethod
    def check_rating_range(rating: float | int) -> bool:
        """
        Метод проверяет рейтинг на вхождение в диапазон от 0 до 5
        :param rating: рейтинг
        :return: True если рейтинг в диапазоне от 0 до 5, иначе False
        """
        if 0 <= rating <= 5:
            return True

    @staticmethod
    def check_price_range(price: int) -> bool:
        """
        Метод проверяет цену на вхождение в диапазон от 0 до 100000000
        :param price: цена
        :return: True если цена в диапазоне от 0 до 100000000, иначе False
        """
        if 0 <= price <= 100000000:
            return True

    @staticmethod
    def check_len_name(name: str) -> bool:
        """
        Метод проверяет длину названия на вхождение в диапазон от 0 до 500
        :param name: название
        :return: True если длина названия в диапазоне от 0 до 500, иначе False
        """
        if 0 <= len(name) <= 500:
            return True


# Производим десериализацию данных из JSON в дата-классы

if __name__ == '__main__':
    # Создаем экземпляр класса ProductSerializer
    product_serializer = ProductSerializer()

    # Получаем данные из JSON файла
    with open('D:\Syncthing\Работа\Academy_Top\ПРИМЕРЫ КОДА\python_329_code\data\wb_api.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Десериализуем данные
    products = product_serializer.deserialize(data['data']['products'])

    # Выводим результат
    for product in products:
        print(product)

