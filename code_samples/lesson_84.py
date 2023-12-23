"""
Lesson 84: Pytest
- Зачем нам нужны тесты?
- Какие есть библиотеки для тестирования?
- Что такое юнит-тесты?
- Установка pytest (pip install pytest)
- assert
- @pytest.mark.xfail - помечаем тест, который всегда падает
- @pytest.mark.parametrize - параметризация тестов

"""


def multiply(a: int, b: int) -> int:
    """
    Умножение двух чисел
    :param a: Число 1
    :param b: Число 2
    :return: Результат умножения
    """
    return a * b
