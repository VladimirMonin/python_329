"""
Lesson 38
26.11.2023

Сериализация и десериализация
- JSON
- Сериализация и десериализация + JSON
"""

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

