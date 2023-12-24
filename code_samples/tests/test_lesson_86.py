import pytest

from code_samples.lesson_86 import get_sum


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