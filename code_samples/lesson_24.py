# Lesson 24
# 14.10.2023
"""
1. Разбор ДЗ №20 - Декоратор с параметрами
"""
import csv
from typing import Callable


# Декоратор без параметра который проверяет что в юзернейм нет пробелов. Если есть - райзит
# исключение ValueError
def username_validator(func: Callable) -> Callable:
    def wrapper(username: str, password: str) -> None:
        if ' ' in username:
            raise ValueError("В юзернейме не должно быть пробелов!")
        func(username, password)

    return wrapper


# Декоратор с параметрами.
# password_validator
# Параметры:
# min_lenght - минимальная длина пароля
# min_uppercase - минимальное количество заглавных букв
# min_lowercase - минимальное количество строчных букв
# min_special_chars - минимальное количество спец символов

def password_validator(min_length: int = 8, min_uppercase: int = 1,
                       min_lowercase: int = 1, min_special_chars: int = 2) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str) -> None:
            bad_log_string = ''

            if len(password) < min_length:
                bad_log_string += f"Пароль должен быть не менее {min_length} символов\n"
            if sum(1 for c in password if c.isupper()) < min_uppercase:
                bad_log_string += f"Пароль должен содержать не менее {min_uppercase} заглавных букв\n"
            if sum(1 for c in password if c.islower()) < min_lowercase:
                bad_log_string += f"Пароль должен содержать не менее {min_lowercase} строчных букв\n"
            if sum(1 for c in password if not c.isalnum()) < min_special_chars:
                bad_log_string += f"Пароль должен содержать не менее {min_special_chars} спец символов\n"

            if bad_log_string:
                raise ValueError(bad_log_string)

            func(username, password)

        return wrapper

    return decorator


@password_validator(min_length=10, min_uppercase=2, min_lowercase=2, min_special_chars=2)
@username_validator
def write_user_to_csv(username: str, password: str) -> None:
    """
    Записывает пользователя в файл users.csv.
    Разделитель - точка с запятой. Кодировка windows-1251
    :param username:
    :param password:
    :return:
    """
    with open('../users.csv', 'a', encoding='windows-1251') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow([username, password])


# Тестируем декоратор
write_user_to_csv('user-two', '123456')
