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


