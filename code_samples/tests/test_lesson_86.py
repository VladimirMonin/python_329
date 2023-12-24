import pytest

from code_samples.lesson_86 import get_sum, get_marvel_data_set


# Праметризация фикстур

@pytest.fixture(params=[(2, 3, 5), (3, 4, 7), (4, 5, 9), (5, 5, 10), (2, 2, 4)])
def data_set(request):
    return request.param


def test_get_sum(data_set):
    """
    Параметризованный тест для функции get_sum
    """
    a, b, expected = data_set
    assert get_sum(a, b) == expected, f'Должно быть {expected}'


# Мокирование функций
"""
Для мокирования используется библиотека pytest-mock (обвертка над unittest.mock)
Чтобы мокировать функцию, нужно использовать фикстуру mocker.patch()

Аргументом в mocker.patch() является строка, которая содержит 
путь к функции, которую нужно замокировать.

Это может быть встроенная функция в Python, например, open, print, input и т.д.
Тогда мы должны указать полный путь к функции, например, builtins.open (зона видимости builtins)
"""

mock_data = [
    {
        "title": "Железный человек",
        "year": 2008,
        "director": "Джон Фавро",
        "screenwriter": "Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй",
        "producer": "Ави Арад и Кевин Файги",
        "stage": "Первая фаза"
    }
]



# Мокирование функции open. Вместо того, чтобы читать данные из файла,
# мы будем возвращать список словарей mock_data

def test_get_marvel_data_set(mocker):
    mocker.patch('code_samples.lesson_86.json.load', return_value=mock_data)
    # Проверяем наличие ключей и типы данных через match case
    for item in get_marvel_data_set(r'D:\Syncthing\Работа\Academy_Top\ПРИМЕРЫ КОДА\python_329_code\data\marvel.json'):
        assert item['title']
        assert item['year']
        assert item['stage']
        assert isinstance(item['title'], str)
        assert isinstance(item['year'], int)
        assert isinstance(item['stage'], str)
