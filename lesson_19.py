from pprint import pprint

from marvel import full_dict

# Lesson 20
# Повторение функций. Области видимости переменных
# Selenuim
"""
1. Скачать и установить ChromeDriver
2. Создать объект драйвера
3. Открыть страницу
4. Залогиниться
5. Функция которая ищет количество страниц в текущей теме
6. Функция которая собирает посты с текущей темы
7. Функция обходчик (используем функции 5 и 6)
"""

# --------------------------------------------------
# Простой пример функций. Одна вызывает другую

"""
1. Запросим у пользователя имя
2. Сформируем строку с приветствием
3. Выведем приветствие
"""


def get_username() -> str:
    """

    :return: Возвщает имя пользователя
    """
    username = input('Введите ваше имя: ')
    return username


def get_hello_message(username: str) -> str:
    """
    Функция принимает имя пользователя и возвращает строку с приветствием
    :param username:
    :return:
    """
    return f'Привет, {username}!'


def print_hello_message(hello_message: str) -> None:
    """
    Функция принимает строку с приветствием и выводит её
    :param hello_message:
    :return:
    """
    print(hello_message)


def run() -> None:
    """
    Функция запускает программу
    :return:
    """
    username = get_username()
    hello_message = get_hello_message(username)
    print_hello_message(hello_message)


# run()


# --------------------------------------------------
# Аргументы функций

def print_two_strings(string_1: str, string_2: str):
    """
    Функция принимает две строки и выводит их
    :param string_1:
    :param string_2:
    :return:
    """
    print(string_1, end=' ')
    print(string_2)


# print_two_strings('Привет', 'Мир')
# print_two_strings('Мир', 'Привет')
# print_two_strings(string_2='Привет', string_1='Мир')


# Значения по умолчанию
def print_two_strings2(string_1: str, string_2: str, end: str = ' '):
    """
    Функция принимает две строки и выводит их
    :param end:
    :param string_1:
    :param string_2:
    :return:
    """
    # Прверка на тип данных в переменной end
    if not isinstance(end, str):  # if type(end) != str:
        raise TypeError('end должен быть строкой а не ' + str(type(end)))
    print(string_1, end=end)
    print(string_2)


# print_two_strings2('Привет', 'Мир', end='--')
# print_two_strings2('Мир', 'Привет')
# print_two_strings2(string_2='Привет', string_1='Мир', end=[])


def nonn() -> None:
    """
    Функция не возвращает ничего
    :return:
    """
    pass


# print(nonn())
# print(print('f'))


def get_range() -> int:
    for i in range(0, 10):
        if i == 15:
            break
    else:
        return 10


# print(get_range())

# Распаковка * и **
names_dict = {
    'Иван': 'Иванов',
    'Петр': 'Петров',
    'Сидор': 'Сидоров',
}

# print(names_dict)

# print(*names_dict, 'еще один')
# print(*names_dict.keys())
# print(*names_dict.values())
# print(*names_dict.items())

name_lst = ['Иван', 'Петр', 'Сидор']


# print(*name_lst)
# print('Иван', 'Петр', 'Сидор')
# print(*name_lst, sep='|')


def print_names(*names):
    print(type(names))
    print(names)


def print_names2(**names):
    print(type(names))
    print(names)


print_names('Иван', 'Петр', 'Сидор')
print_names(*name_lst)

print_names2(Иван='Иванов', Петр='Петров', Сидор='Сидоров')
print_names2(**names_dict)


def some_func(a, b, c=10, *args, **kwargs):
    print(a, b, c)
    print(args)
    print(kwargs)

first_names = ['Иван', 'Петр', 'Сидор']
last_names = ['Иванов', 'Петров', 'Сидоров', 'Николаев']

# persons_dict = zip(first_names, last_names)

# Делаем нумерованный словарь 0: Иванов из списка фамилий
# persons_dict = dict(enumerate(last_names, 10))
# print(persons_dict)

# Разбор HW 16

"""
1. Сделайте импорт `full_dict` из документа `Marvel.py`
2. Напишите пользовательский ввод цифр через пробел, разбейте его на список, и примените к каждому элементу списка `int` используя `map`, но только в том случае, если этот элемент списка число, иначе замените его на `None`
4. Используйте `filter` и получите аналогичный по структуре словарь, который будет содержать исходные `id` и остальные ключи, но только тех фильмов, `id` которых есть в полученном списке в п.2
5. Составьте `set comprehension` (генератор множества) собрав множество содержимого ключа `director` словаря дата-сета
6. Составьте `dict comprehension` (генератор словаря) сделав копию исходного словаря `full_dict`, при этом применим в к каждому `'year'` значению, функцию `str`

7. Используйте `filter` и получите аналогичный по структуре словарь, 
который будет содержать исходные `id` и остальные ключи, но только тех 
фильмов, которые начинаются на букву `Ч
"""
# 7. Используйте `filter` и получите аналогичный по структуре словарь,
result_dict = dict(filter(lambda film: film[1]['title'][0] == 'Ч', full_dict.items()))
# pprint(result_dict)

films_set = [film for film in full_dict.values() if film['title'][0] == 'Ч']
dict_films = {film[0]:film[1] for film in full_dict.items() if film[1]['title'][0] == 'Ч'}
pprint(dict_films)


# 22 lesson
from pprint import pprint

from marvel import full_dict

# Повторение материала

# map пользовательского ввода - применяем int к каждому элементу списка
# user_input = input('Введите числа через пробел: ').split()
# int_lst = list(map(int, user_input))

# однострочник
# int_lst = list(map(int, input('Введите числа через пробел: ').split()))

# Map int input lambda if is digit

# TODO Попробуйте реализовать этот пример и напишите в чат + :)
# int_lst = list(map(lambda x: int(x) if x.isdigit() else None, input('Введите числа через пробел: ').split()))
# print(int_lst)

# Same list comprehension
# int_lst = [int(x) if x.isdigit() else None for x in input('Введите числа через пробел: ').split()]

# Same full version with for
# user_input = input('Введите числа через пробел: ').split()
# int_lst = []
# for x in user_input:
#     if x.isdigit():
#         int_lst.append(int(x))
#     else:
#         int_lst.append(None)

# Filter - фильтрует элементы по условию, принимает функцию и итерируемый объект
# Функция должна возвращать True или False
# Итерируемый объект - список, кортеж, словарь, строка, работает со всеми итерируемыми объектами

# Фильтруем full_dict - ищем фильмы в названии которых есть мстител и возвращаем их
# request = input('Введите название  фильма')
# result = filter(lambda items: request.lower() in items[1]['title'].lower(), full_dict.items())
# pprint(dict(result))

# Sort и Sorted
# Sort - метод списка, сортирует список на месте, не возвращает новый список
# Sorted - функция, которая работает с любыми итерируемыми объектами, возвращает новый список

# sort - простая реализация на списке

fruits_lst = ['apple', 'banana', 'orange', 'kiwi', 'apple', 'banana', 'orange', 'kiwi', 'a']
fruits_lst.sort()
# print(fruits_lst)
fruits_lst.sort(reverse=True)
# print(fruits_lst)

# Сортируем в sort по lambda функции в key по последней букве
fruits_lst.sort(key=lambda x: x[-1])
# print(fruits_lst)

# Сортируем в sort по lambda функции в key по длине слова (reverse=True - по убыванию)
fruits_lst.sort(key=lambda x: len(x), reverse=True)
# print(fruits_lst)

# sorted - функция, которая возвращает новый список
# Аргументы: итерируемый объект, key, reverse

# фильмы 2023 года
# result = sorted(full_dict, key=lambda x: x.values()['year'] if x.values()['year']  != 'TBA' else 0, reverse=False)
# pprint(result)


# result = sorted(filter(lambda film: film['title'].startswith('Ч'), full_dict.items()), key=lambda film: film['year'])
# pprint(result)

names = {
    'John': 10,
    'Michael': 5,
    'Jack': 15,
    'Bob': 6,
    'Alex': 20,
}


# Сортируем словарь по ключам и выводим в виде словаря
# print(dict(sorted(names.items(), reverse=False)))
# Сортируем словарь по значениям (сортировка цифр от меньшего к большему) и выводим в виде словаря
# print(dict(sorted(names.items(), key=lambda x: x[1], reverse=True)))

# Сортируем словарь по значениям (в первую очередь те у кого вторая буква == о) и выводим в виде словаря
# print(dict(sorted(names.items(), key=lambda x: x[0][1] == 'o', reverse=True)))

# print(names.items())


# функция для сортировки по ключам по двум парамерам ключа (вторая буква о и вторая буква l)
def sort_by_key(x):
    return x[0][1] == 'o', x[0][1] == 'l', x[0][1] == 'a'


print(dict(sorted(names.items(), key=sort_by_key, reverse=True)))
print(dict(sorted(names.items(), key=lambda x: (x[0][1] == 'o', x[0][1] == 'l'), reverse=True)))

# Сортируем фильмы сначала по году (по убыванию, если год == "TBA" запишем 3000) потом по названию (по возрастанию)
result = sorted(full_dict.items(), key=lambda x: (x[1]['year'] if x[1]['year'] != 'TBA' else 0, x[1]['title']))
print(result)

fruits_lst = ['apple', 'banana', 'orange', 'kiwi', 'apple', 'banana', 'orange', 'kiwi', 'a']
# Сортируем names по значениям с передачей функции len в key сортировка списка fruits_lst
print(sorted(names.items(), key=lambda x: len(fruits_lst), reverse=True))

# Пространство имен (namespace)
# Все переменные, функции, классы, модули, и т.д. находятся в пространстве имен
# Все пространства имен находятся в глобальном пространстве имен
# Все глобальные пространства имен находятся в пространстве имен builtins
# Все локальные пространства имен находятся в глобальном пространстве имен
# Все nonlocal пространства имен находятся в локальном пространстве имен

# Пространство имен - это словарь, где ключи - это имена переменных, а значения - это объекты

# print(globals())

x = 5


def print_x():
    global x
    x = 10
    y = 10
    print(x)

#
# print_x()
# print(x)

# Пространство имен nonlocal
# nonlocal - позволяет работать с переменными из родительского пространства имен

# x - глобальная зона видимости
x = 0
def outer():
    x = 5 # локальная зона видимости
    print('outer', x)

    def inner():
        # nonlocal x
        x = 10 # локальная зона видимости (но может переписать внешний x если nonlocal)
        print('inner', x)

    inner()
    print('outer', x)

print(f'Глобально {x=}')
outer()
print(f'Глобально {x=}')


# реши домашку по пайтон. Функция которая принимает строку (это ключ словаря) а так же имеет флаг reversed и возвращает отфильтрованный словарь. Внутри используется лямбда и sorted Часть словаря прилагаю full_dict = {
#     1: {
#         'title': 'Железный человек',
#         'year': 2008,
#         'director': 'Джон Фавро',
#         'screenwriter': 'Марк Фергус и Хоук Остби, Артур Маркам и Мэтт Холлоуэй',
#         'producer': 'Ави Арад и Кевин Файги',
#         'stage': 'Первая фаза'

def get_sort_dict(key: str, reversed: bool = False) -> dict:
    """
    Функция принимает ключ словаря и флаг reversed и возвращает отфильтрованный словарь
    :param key:
    :param reversed:
    :return:
    """
    result = sorted(full_dict.items(), key=lambda x: x[1][key], reverse=reversed)
    return dict(result)