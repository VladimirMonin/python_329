# Повторение материала! Lesson 29-30

# Типы данных
"""
int() - целое число
float() - число с плавающей точкой
str() - строка
bool() - булевый тип данных
none - пустота

Итерируемые типы данных
list() - список
Список упорядоченный, изменяемый тип данных
tuple() - кортеж
Кортеж упорядоченный, неизменяемый тип данных
set() - множество
Множество неупорядоченный, изменяемый тип данных
dict() - словарь
Словарь неупорядоченный, изменяемый тип данных

Списки. Методы списков
.append() - добавление элемента в конец списка
.pop() - удаление элемента из списка по индексу и возврат удаленного элемента
.remove() - удаление элемента из списка по значению
.index() - получение индекса элемента по значению
.count() - получение количества элементов по значению
.sort() - сортировка списка
.reverse() - разворот списка
.copy() - копирование списка
.clear() - очистка списка
.extend() - расширение списка


"""
from pprint import pprint


# shop_list = [
#     'молоко',
#     'хлеб',
#     'яйца',
#     'сыр',
#     'колбаса',
#     'хлеб',
# ]


# count
# print(shop_list.count('хлеб'))
# Почистим от дублей через трансформацию в сет и обратно в список
# shop_unique_list = list(set(shop_list))

# index
# print(shop_list.index('хлеб'))

# pop
# import random

# rand_int = random.randint(0, len(shop_list) - 1)

# random_element = shop_list.pop(rand_int)
# print(random_element)
# print(shop_list)

# NAME = 'John'
# AGE = 25
# WEEK = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')
#
# MARKS = 2, 3, 4, 5, None
#
# FIRST_DAY = WEEK[0]

# Sets - множества
# Неупорядоченный тип данных, изменяемый тип данных
# Множества содержат только уникальные элементы
# Элементы множества не индексируются
# Элементом множества может быть только неизменяемый тип данных
# (строка, число, кортеж)

# Создание множества
# set() - пустое множество
# {} - пустой словарь

# shop_list = [
#     'молоко',
#     'хлеб',
#     'яйца',
#     'сыр',
#     'колбаса',
#     'хлеб',
# ]

# shop_set = set(shop_list)
# print(shop_set.pop())
# print(shop_set)


# set_calendar = {
#     (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
#     ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'),
#     ('Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн',)
# }
# set_id = {1, 2, 3, 4, 5}
# shop_set = {'молоко', 'хлеб', 'яйца', 'сыр', 'колбаса', 'хлеб', 1, 2, 3, 4, 5,
#             ('пн', 'вт')}
# o_product = set()

# for item in shop_set:
#     print(type(item))

# excel_table = [['Имя', 'Фамилия', 'Возраст'],
#                ['John', 'Smith', 25],
#                ['Ivan', 'Ivanov', 30],
#                ['Anna', 'Smith', 18]]
#
# for first_name, last_name, age in excel_table[1:]:
#     print(f'{first_name} | {last_name} | {age}')


# Функции
# def - определение функции

# def print_hello():
#     print('Hello, world!')
#
#
# def get_hello():
#     return 'Hello, world!'
#
#
# print_hello()
# result_get_hello = get_hello()
#
# print('result_get_hello', result_get_hello)


# shop_list = [
#     'молоко',
#     'сыр',
#     'яйца',
#     'сыр',
#     'колбаса',
#     'хлеб',
# ]
#
# count = 0
# new_list = []
# for product in shop_list:
#     if len(product) >= 4: # Если длина элемента больше или равна 4 - добавляем в новый список
#         new_list.append(product)
#     count += 1

# Аргументы функции
# Позиционные аргументы
# Именованные аргументы
# Позиционные аргументы и именованные аргументы


def hello_friend(name, lastname):
    return f'Привет, {name} со славной фамилией {lastname}!'


# print(hello_friend('Иванов', 'Иван'))
# print(hello_friend(lastname='Иванов', name='Иван'))


def hello_friend(name, lastname, status='друг'):
    return f'Привет, {status}, {name}, со славной фамилией {lastname}!'


# print(hello_friend(lastname='Иванов', name='Иван'))
# print(hello_friend("Иван", "Иванов", status='коллега'))
#

# *args - позиционные аргументы
# **kwargs - именованные аргументы

def get_sum(*integers):
    return sum(integers)


# Кортавая функция
"""
Функция принимает на вход любое количество 
строк, на выходе возвращает кортеж из тех строк где есть буква Р
"""

# num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(get_sum(1, 2, 3, 4, 5, 6, 7, 8))
#
# print(get_sum(*num_lst))
#
# print(num_lst)
# print(*num_lst)
#
#
# def check_r(*args):  # Функция ожидает много элементов через запятую
#     result = []
#     for word in args:
#         if 'р' in word.lower():
#             result.append(word)
#     return tuple(result)
#
#
# words_lst = ['Трактор', 'Автомобиль',
#              'Самолет', 'Поезд',
#              'Велосипед', 'Самокат',
#              'Самовар', 'Самолет']
#
# print(check_r(words_lst[0], words_lst[1], words_lst[2],
#               words_lst[3], words_lst[4], words_lst[5], words_lst[6]))
#
# print(check_r('Трактор', 'Автомобиль'))
#
# print(check_r(*words_lst))
#
# word = 'Трактор'
# print(*word)


# Функция для чтения md файла
