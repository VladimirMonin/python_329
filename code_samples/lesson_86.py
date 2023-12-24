"""
Lesson 86: Pytest
- Размещение тестов в пакете tests
- Конфигурационный файл pytest.ini
- Фикстуры
- Параметризированные фикстуры
- Концепция мокирования
- pytest-mock - библиотека для мокирования pip install pytest-mock
- Мокирование функций
- Мокирование методов классов?
- Маркировка тестов
"""
import json


def get_sum(a: int, b: int) -> int:
    """
    Сумма двух чисел
    :param a: Число 1
    :param b: Число 2
    :return: Результат сложения
    """
    return a + b


def get_marvel_data_set(file: str = '../data/marvel.json') -> list[dict]:
    """Функция читает данные из файла ../data/marvel.json
    и возвращает список словарей, с измененными ключами
    """
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Меняем ключи в словарях
    result = []
    for item in data:
        result.append({
            'title': item['title'],
            'year': item['year'],
            'stage': item['stage']
        })
    return result
