import pytest

from lesson_84 import multiply


def test_true():
    """
    Тест, который всегда проходит
    """
    assert True


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
    pytest.param(5, 5, 26, marks=pytest.mark.xfail), # помечаем тест, который всегда падает
    (2, 2, 4),
])
def test_multiply(a, b, expected):
    """
    Параметризованный тест для функции multiply
    """
    assert multiply(a, b) == expected, f'Должно быть {expected}'