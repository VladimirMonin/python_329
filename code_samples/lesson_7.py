# import random
# from random import randint, choice
# # import selenium
# import marvel
from data.marvel import full_dict


# print(marvel.simple_set)


# print(ss)

# print(small_dict)

# Пары №13 10мин №14 (20мин)  №15 10 мин №16
# Повторим материал

# Мы прошли строки / методы строк / списки / методы списков

# Методы строк ------------------------------
# split() - разбивает строку на элементы списка по разделителю
# ' '.join() - объединяет элементы списка в строку

# lower() - преобразует строку в нижний регистр
# upper() - преобразует строку в верхний регистр
# replace() - заменяет одну подстроку на другую
# strip() - удаляет пробелы в начале и в конце строки
# find() - Поиск подстроки в строке. Возвращает номер первого вхождения или -1
# index() - Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError
# count() - Возвращает количество вхождений подстроки в строке
# isdigit() - Проверяет, состоит ли строка из цифр. Возвращает True или False
# isalpha() - Проверяет, состоит ли строка из букв. Возвращает True или False
# isalnum() - Проверяет, состоит ли строка из цифр или букв. Возвращает True или False
# capitalize() - Переводит первый символ строки в верхний регистр, а все остальные в нижний
# title() - Переводит первый символ каждого слова строки в верхний регистр, а все остальные в нижний


# Методы списков ------------------------------
# append - добавляет элемент в конец списка
# insert - добавляет элемент в список по индексу
# extend - расширяет список другим списком
# remove - удаляет элемент из списка по значению
# pop - удаляет элемент из списка по индексу и возвращает его
# clear - очищает список
# index - возвращает индекс элемента
# count - возвращает количество элементов
# sort - сортирует список
# reverse - переворачивает список
# copy - копирует список
# del - удаляет элемент по индексу или срез. Пишется как функция del list[0]

# for - цикл для перебора итерируемых объектов
# итерируемые объекты - строки, списки, кортежи, словари, множества


# цикл while - цикл с предусловием. Выполняется пока условие истинно
# while условие:
# Можно прописать условия во вне. Например, is_stopped = False
# while not is_stopped:
# is_stopped = True


# Операторы break и continue. Оператор break прерывает цикл, оператор continue прерывает текущую итерацию цикла

# Множества.
# Set - 1. неупорядоченная коллекция 2. уникальные элементы. Не поддерживает индексирование
# Множества можно создавать двумя способами:

# 1. set() - функция  (по аналогии с list() и dict() или str() int() float())
# 2. {} - литерал (не поддерживает пустое множество - сделает пустой словарь)

# first_set = set()
# second_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(second_set)
#
# for i in second_set: # Можно получить чистый рандом
#     print(i)

# Сеты могут содержать в себе только уникальные элементы.
# Поддерживаемые типы данных в set (неизменяемые типы) - int, float, str, tuple, bool, None
# Не поддерживаемые типы данных в set(изменяемые типы) - list, dict, set

# Методы множеств
# add - добавляет элемент в множество
# remove - удаляет элемент из множества
# discard - удаляет элемент из множества, если он там есть
# pop - удаляет случайный элемент из множества и возвращает его
# clear - очищает множество
# copy - копирует множество


# Множества можно использовать для удаления дубликатов из списка
# shop_lst = ['apple', 'banana', 'orange', 'apple', 'banana']
# shop_set = set(shop_lst)
#
# print(shop_set)
# print(' + '.join(shop_set))

# for film in simple_set:
#     print(film, end=' || ')

# Практика №1. Что бы мне посмотреть из Марвел?
# Цикл while пока не введу exit. Выводим рандомный фильм из списка
# while, pop(), input, print, break

# """
# Наша программа предлагает пользователю к просмотру фильм Марвел
# Пока пользователь не введет exit, программа будет предлагать фильмы
# Программа предложила фильм. Спросила, ещё? Если НЕ exit - предложить ещё фильм
# Фильмы рандомные. Рандом через pop()
#
# 1. Импортируем фильмы из файла
# 2. Объявляем цикл (while)
# 3. Input - ввод пользователя
# 4. Проверка на exit
# 5. Рандомный выбор фильма
# 6. Вывод фильма
# 7. Идем на шаг 3
# """
# is_stoped = False
# while not is_stoped:
#     user_input = input('Посмотрим фильм Марвел? (exit - выход) ')
#     if user_input != 'exit':
#         film = simple_set.pop()
#         print(f'Предлагаю посмотреть {film}')
#     else:
#         is_stoped = True


# Методы множеств (математические)
# union - объединяет множества (оператор | )
# intersection - возвращает пересечение множеств (оператор &)
# difference - возвращает разность множеств (оператор -)
# symmetric_difference - возвращает симметричную разность множеств (оператор ^)

films_olga = {'Мстители', 'Человек-паук',
             'Черная пантера', 'Железный человек'}


films_alex = {'Мстители', 'Человек-паук',
             'Тор', 'Халк', 'Капитан Америка'}



# Какие фильмы смотрели оба?
# print(films_olga.intersection(films_alex))

# Какие фильмы смотрел только Алекс?
# print(films_alex.difference(films_olga))

# Какие фильмы смотрел только Алекс или только Оля?
# print(films_alex.symmetric_difference(films_olga))

# Практика №2. Какие фильмы есть в нашей базе?
# 1. В цикле while предложить пользователю ввести фильмы через
# 2. После ввода фильмов - вывести список фильмов, которые есть в нашей базе

"""
1. Делаем цикл while
2. В цикле while делаем input
3. Делаем сплит и сет (метод split() и set())
4. Делаем пересечение с нашим сетом (метод intersection())
5. Выводим результат
"""

# while True:
#     user_input = input('Введите фильмы через запятую: ')
#     if user_input == 'стоп':
#         break
#     user_films = set(user_input.split(','))
#     # ищем пересечение user_films с сетом simple_set
#     print(user_films.intersection(simple_set))
#
#
# # Тожесамое только на списках
#
# while True:
#     user_input = input('Введите фильмы через запятую: ')
#     if user_input == 'стоп':
#         break
#     user_films = user_input.split(',')
#     db_films = list(simple_set)
#     a = [film for film in user_films if film in db_films]
    # for film in user_films:
    #     if film in db_films:
    #         print(film)

# Exception - исключение. Ошибка, которую можно обработать.

# num_input = input('Введите числа через запятую: ')
# num_list = num_input.split(',')
#
# new_lst = []
# for num in num_list:
#     new_lst.append(int(num))


# try - попробуй
# except - исключение
# finally - выполняется всегда

# num_input = input('Введите числа через запятую: ')
# num_list = num_input.split(',')
#
# new_lst = []
#
# for num in num_list:
#     try:
#         item = int(num)
#     except ValueError:
#         print(f'Это не число: {num}')
#         continue
#     new_lst.append(item)
#

# Пользователь вводит 2 числа, мы делим одно на другое
# a = input('Введите первое число: ')
# b = input('Введите второе число: ')
#
# try:
#     int_a = int(a)
#     int_b = int(b)
#     print(int_a / int_b)
#
# except ValueError:
#     print('Это не число')
# except ZeroDivisionError as err:
#     print(f'На ноль делить нельзя: {err}')
#
# finally:
#     print('Это выполняется всегда')

# rise - вызвать исключение

# a = input('Введите первое число: ')
# b = input('Введите второе число: ')
#
# if a.isdigit() and b.isdigit():
#     print(int(a) / int(b))
# else:
#     print('Это не число')
#     raise ValueError('Это не число. Введите число')

# Практика №3.
# Проверка на кратность 2.
"""
Пользователь вводит числа через запятую. 
Делаем список из этих чисел.
Проверить, что все числа кратны 2.
Работаем с исключениями. raise - вызвать исключение
Если будет введено не число - TypeError
Если будет введено число не кратное 2 - ValueError
"""

# user_input = input('Введите числа через запятую: ')
# user_list = user_input.split(',')
# new_list = []
#
# for num in user_list:
#     if not num.isdigit():
#         raise TypeError('Это не число')
#
#     if int(num) % 2 != 0:
#         raise ValueError('Число не кратно 2')
#
#     new_list.append(int(num))
#
# print(new_list)

# Cловари в Python. dict - словарь
# Словарь - это структура данных, которая хранит данные в формате ключ: значение

# Создание словаря
d = {}
d = dict()
dd = {'key': 'value', 'key2': 'value2'}


# Ключ - любой неизменяемый тип данных (число, строка, кортеж, булево значение)
# Значение - любой тип данных

# ddd = {1: 'value',
#        'key2': 2,
#        (1, 2, 3): [1, 2, 3]
#       }
# Ключи уникальны в рамках одного словаря

# print(small_dict)

# Методы словарей (сортированы по частоте использования)
# get - получить значение по ключу
# keys - получить все ключи словаря
# values - получить все значения словаря
# items - получить все пары ключ-значение словаря
# update - обновить словарь, добавить новые пары ключ-значение
# pop - получить значение по ключу и удалить ключ
# clear - очистить словарь
# popitem - получить и удалить последнюю пару ключ-значение
# setdefault - получить значение по ключу, если его нет - создать ключ со значением по умолчанию

# class_ = {'name': '11a',
#           'students': 20,
#           'teacher': 'Ivan Ivanovich'}
#
# print(class_['name']) # получить значение по ключу
# # print(class_['name1'])
#
# print(class_.get('name1', 'Такого ключа нет')) # получить значение по ключу
#

# .keys() - получить все ключи словаря
# .values() - получить все значения словаря
# .items() - получить все пары ключ-значение словаря

# for key in class_.keys():
#     print(key)
#
# for key in class_:
#     print(key)

# print(list(class_.keys())) # По умолчанию это не список а dict_keys
# print(type(list(class_.keys())))
#
# print(type(class_.values())) # По умолчанию это не список а dict_values
# print(type(list(class_.values())))
#
# print(class_.items()) # По умолчанию это не список а dict_items

# Практика №4.
# Пользователь вводит название фильма
# Мы печатаем год выхода фильма

"""
Пользовательский ввод: Введите название фильма:
Метод get или прямое обращение по ключу
Принт (f'Фильм {user_input} вышел в {year}')
"""

# итерация по словарю
# for key in small_dict:
#     print(key)

# итерация по значениям
# for value in small_dict.values():
#     print(value)
#
# for key, value in small_dict.items():
#     print(f'key:{key}, value:{value}')
#
# print(small_dict.items())

# Выводим фильмы N года
# user_input = input('Введите год: ')
# result = []
# for key, value in small_dict.items():
#     if value == int(user_input):
#         result.append(key)
#
# if result:
#     print(f'Фильмы вышедшие в {user_input} году: {result}')
# else:
#     print(f'Фильмы вышедшие в {user_input} году не найдены')

# Читаем вложенные словари
# item = full_dict[1]['title']
# print(item)

# Мы выводим все названия фильмов (из вложенных словарей)
# for key in full_dict:
#     print(full_dict[key]['title'])

# Мы вывыодим названия фильмов, которые относятся к первой фазе
# for key in full_dict:
#     if full_dict[key]['stage'] == 'Первая фаза':
#         print(full_dict[key]['title'])
#
print(full_dict.items())
for key, value in full_dict.items():
    if value['stage'] in ['Первая фаза', 'Вторая фаза']:
        print(value['title'])