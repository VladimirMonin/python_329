"""
Lesson 84: Pytest
- Зачем нам нужны тесты?
- Какие есть библиотеки для тестирования?
- Что такое юнит-тесты?
- Установка pytest (pip install pytest)
- assert
"""

# assert - это проверка условия,
# утверждение, которое должно быть истинным,
# иначе будет ошибка.

# Пример 2+2=4
assert 2 + 2 == 4, "Ожидалось 4"


# assert 2 + 2 == 5, "Ожидалось 4"

def sum(a, b):
    return a + b


# assert sum(2, 2) == 4, "Ожидалось 4"

# Скрипт с услоивем if и assert
if __name__ == "__main__":
    try:
        assert sum(2, 2) == 4, f"Ожидалось 4 получили {sum(2, 2)}"
    except AssertionError as e:
        print(e)

    try:
        assert sum(3, 3) == 6, f"Ожидалось 6 получили {sum(3, 3)}"
    except AssertionError as e:
        print(e)

# Негативный тест с ожиданием исключения

# Функция деления
def divide(a, b):
    return a / b

# Тест деления на 0
try:
    divide(2, 0)
except ZeroDivisionError as e:
    print(e)