import pytest
from code_samples.lesson_84 import multiply, is_palindrome


def test_true():
    """
    Тест, который всегда проходит
    """
    assert True, "Удивительно, но True не True"


def test_positive_multiply():
    """
    Тест для функции multiply
    """

    assert multiply(2, 3) == 6, "Должно быть 6"


@pytest.mark.xfail(reason="Негативный тест, который всегда падает")
def test_negative_multiply():
    """
    Негативный тест для функции multiply
    """
    assert multiply(2, 3) == 7


# Параметризация тестов - это когда мы передаем
# в тест несколько значений

# @pytest.mark.parametrize("a, b, expected", [
#     (2, 3, 6),
#     (3, 4, 12),
#     (4, 5, 20),
#     (5, 5, 25),
#     (2, 2, 4),
# ])
# def test_multiply(a, b, expected):
#     """
#     Параметризованный тест для функции multiply
#     """
#     assert multiply(a, b) == expected, f'Должно быть {expected}'
#

data_set = [
    (2, 3, 6),
    (3, 4, 12),
    (4, 5, 20),
    (5, 5, 25),
    (2, 2, 4),
]


@pytest.mark.parametrize("a, b, expected", data_set)
def test_multiply(a, b, expected):
    """
    Параметризованный тест для функции multiply
    """
    assert multiply(a, b) == expected, f'Должно быть {expected}'


# Параметризация xfail

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (3, 4, 12),
    (4, 5, 20),
    pytest.param(5, 5, 26, marks=pytest.mark.xfail),  # помечаем тест, который всегда падает
    (2, 2, 4),
])
def test_multiply(a, b, expected):
    """
    Параметризованный тест для функции multiply
    """
    assert multiply(a, b) == expected, f'Должно быть {expected}'


# Фикстура для теста функции is_palindrome которая прочитает
# ../data/palindromes.json и вернет рандомный палиндром (из списка словарей по ключу слово)
# будет генерироваться для каждой функции, которая ее вызывает
# (т.е. для каждого теста)

@pytest.fixture
def palindrome():
    """
    Фикстура для теста функции is_palindrome которая прочитает
    ../data/palindromes.json и вернет рандомный палиндром (из списка словарей по ключу слово)
    """
    import random
    import json
    # Кодировка файла - utf-8
    with open(r'D:\Syncthing\Работа\Academy_Top\ПРИМЕРЫ КОДА\python_329_code\data\palindromes.json', encoding='utf-8') as f:
        # загружаем данные из файла в переменную data
        data = json.load(f)
    # выбираем рандомный словарь
    random_dict = random.choice(data)
    print(random_dict)
    # возвращаем значение по ключу слово
    return random_dict['слово']

# Тест
def test_palindrome(palindrome):
    """
    Тест для функции is_palindrome
    """
    assert is_palindrome(palindrome), f'{palindrome} должно быть палиндромом'