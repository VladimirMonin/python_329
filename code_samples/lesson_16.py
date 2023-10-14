# "Логирование в игре города" через логирование в файл txt и в консоль

LOG_FILE = '../game_log.txt'
MSG_COMPUTER_WIN = 'Компьютер победил, назвав город'
MSG_HUMAN_WIN = 'Пользователь победил, назвав город'


def get_log(message: str, log_file=LOG_FILE) -> None:
    """
    Функция для логирования в файл и в консоль
    :param message:
    :param log_file:
    :return: None
    """
    with open(log_file, 'a', encoding='utf-8') as file:
        file.write(f'{message}\n')
        print(message)


# city = 'Севастополь'
# get_log(f'{MSG_COMPUTER_WIN}: {city}')


# Читаем файл и возвращаем список строк
def read_file(file_name, encoding='utf-8'):
    with open(file_name, 'r', encoding=encoding) as f:
        return f.readlines()


# Чтение файла по строкам с печатью каждой строки
def read_file_print(file_name, encoding='utf-8'):
    with open(file_name, 'r', encoding=encoding) as f:
        print('тест')
        for line in f:
            print(line, end='')


# read_file_print(LOG_FILE)

# ЛОГИКА ЗАПИСИ ПОСЛЕДНИХ 5 ИГР В ФАЙЛ ЛОГА

shop_lst = [
    '1 игра',
    '2 игра',
    '3 игра',
    '4 игра'
]


# shop_lst.reverse()
# Делаем insert
# shop_lst.insert(0, '5 игра')
# shop_lst.insert(0, '6 игра')
# shop_lst.insert(0, '7 игра')

# print(shop_lst[:5:])


# Insert - вставка элемента в список. Элемент вставляется на указанную позицию
# остальные элементы сдвигаются вправо
# list.insert(i, x)

# *ARGS - распаковка аргументов в функции
# **KWARGS - распаковка именованных аргументов в функции


def get_sum(*integers):
    return sum(integers)


# user_input = (input('Введите числа: ')).split()
# nums = [int(num) for num in user_input]
#
# print(get_sum(*nums))

# **KWARGS - распаковка именованных аргументов в функции

kwargs = {'name': 'Иван',
          'lastname': 'Иванов',
          'status': 'коллега'}


def print_users(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} - {value}')


# print_users(**kwargs)


#
# print_users(**small_dict)


# Порядок аргументов в функции
# 1. Позиционные аргументы
# 2. *args
# 3. Именованные аргументы
# 4. **kwargs

# функция со всеми видами аргументов

def func(a, b="s", *args, **kwargs):
    print(a, b, args, kwargs)


"""
Функция поиска фильмов. 
Принимает значение и **kwargs
Возвращает список фильмов, которые содержат в себе значение
"""


def find_film(search, **kwargs):
    films_lst = []
    for film, year in kwargs.items():
        if search == str(year):
            films_lst.append(film)
    return films_lst


# search_input = input('Введите год выхода фильма: ')
# result = find_film(search_input, **small_dict)
# print(result)

"""
В Python существует несколько областей видимости переменных:

1. **Локальная** (Local) - это область видимости, которая определяется внутри функции или метода. 
Переменные, определенные внутри функции, доступны только внутри этой функции.

2. **Обрамляющая** (Enclosing) - это область видимости, которая определяется внутри вложенной функции. 
Переменные, определенные в обрамляющей функции, доступны только внутри этой функции и внутри вложенной функции.

3. **Глобальная** (Global) - это область видимости, которая определяется внутри модуля, 
т.е. вне всех функций и классов. Переменные, определенные в глобальной области видимости, доступны в любом месте модуля.

4. **Встроенная** (Built-in) - это область видимости, которая содержит встроенные функции и имена, 
доступные из любой области видимости. Например, функции `print()`, `len()` и т.д.
"""

name = 'V'


def print_name():
    print(name)


print_name()


def my_function():
    x = 10
    print(x)  # Вывод: 10


# my_function()

# Пример 2: Конфликт имен переменных
x = 10
y = 2


def my_function1():
    x = 20
    print(x)


# my_function1()
print(x)
print(y)

"""
Контрольная работа по функциям
20 минут

Функция проверки пароля. Принимает пароль и проводит проверку по следующим критериям:

- Должен содержать хотя бы один спецзнак
- Не должен содержать пробел
- Должен содержать символы разных регистров (большие и маленькие)
- Должен быть более 7 символов длиной
- Не должен входить в список плохих паролей (определяете сами)

Возвращает True или False
"""
BAD_PASSWORDS = ['12345', '1234567890', 'qwerty', 'password',
                 'password123',]


def validate_password(password: str) -> bool:
    """
    Функция проверки пароля
    :param password:
    :return: bool
    """
    if password in BAD_PASSWORDS:
        return False
    elif ' ' in password:
        return False
    elif len(password) < 7:
        return False
    elif password.islower() or password.isupper():
        return False
    elif password.isalpha():
        return False
    elif password.isdigit():
        return False
    else:
        return True


passwords = ['12345', '1234567890', 'qwerty', 'password', 'password123', 'sfjl&(&dsfsFSF&(']
#
# for password in passwords:
#     print(f'Пароль {password}\n{validate_password(password)}\n{"-" * 20}\n')


pass_input = input('Введите пароль: ')

if validate_password(pass_input):
    print('Пароль подходит')
else:
    print('Пароль не подходит')

